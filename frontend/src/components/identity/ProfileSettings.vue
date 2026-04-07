<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { useContentStore } from '@/stores/contentStore'

// API base URL - adjusted for the accounts app
const API_BASE = 'http://127.0.0.1:8000/api/accounts/profile/'

const user = ref({
  full_name: '',
  email: '',
  phone_number: '',
  nic_number: '',
  university: '',
  faculty: '',
  academic_stream: '',
  academic_year: '',
  student_id: '',
  role: '',
  is_peer_tutor: false,
  verified: false // UI only for now
})

const isLoading = ref(true)
const isSaving = ref(false)
const message = ref({ text: '', type: '' }) // type: 'success' or 'error'

const initials = computed(() => {
  if (!user.value.full_name) return '??'
  return user.value.full_name
    .split(' ')
    .map(n => n[0])
    .join('')
    .toUpperCase()
    .slice(0, 2)
})

const fetchProfile = async () => {
  isLoading.value = true
  const token = localStorage.getItem('access_token')
  try {
    const response = await axios.get(API_BASE, {
      headers: { Authorization: `Bearer ${token}` }
    })
    user.value = { ...user.value, ...response.data }
  } catch (err) {
    console.error('Failed to fetch profile:', err)
    message.value = { text: 'Failed to load profile data.', type: 'error' }
  } finally {
    isLoading.value = false
  }
}

const contentStore = useContentStore()

const updateProfile = async () => {
  isSaving.value = true
  message.value = { text: '', type: '' }
  const token = localStorage.getItem('access_token')
  
  // Create update payload (excluding sensitive/read-only fields if necessary)
  const payload = { ...user.value }
  delete payload.id
  delete payload.username
  
  try {
    const response = await axios.patch(API_BASE, payload, {
      headers: { Authorization: `Bearer ${token}` }
    })
    user.value = response.data
    message.value = { text: 'Profile updated successfully!', type: 'success' }
    
    // Update local storage for immediate UI updates in sidebar/navbar
    localStorage.setItem('full_name', user.value.full_name)
    
    // Refresh the recommendations based on the new academic stream/year
    await Promise.all([
      contentStore.fetchRecommendations(),
      contentStore.fetchKuppiRecommendations()
    ])
    
    setTimeout(() => { message.value = { text: '', type: '' } }, 3000)
  } catch (err) {
    console.error('Failed to update profile:', err)
    const errorData = err.response?.data
    let errorText = 'Update failed.'
    
    if (errorData) {
      errorText = Object.entries(errorData)
        .map(([key, val]) => `${key}: ${val}`)
        .join(' | ')
    }
    
    message.value = { text: errorText, type: 'error' }
  } finally {
    isSaving.value = false
  }
}

onMounted(fetchProfile)
</script>

<template>
  <div class="w-full max-w-6xl mx-auto p-4 sm:p-6 lg:p-8 space-y-10 font-sans">
    
    <!-- Skeleton Loading -->
    <div v-if="isLoading" class="animate-pulse space-y-8">
      <div class="h-12 bg-slate-200 rounded-xl w-48"></div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="h-64 bg-slate-100 rounded-[2.5rem]"></div>
        <div class="md:col-span-2 h-96 bg-slate-100 rounded-[2.5rem]"></div>
      </div>
    </div>

    <template v-else>
      <!-- Header Section -->
      <div class="relative">
        <h1 class="text-4xl font-black text-[#2C3E50] tracking-tight mb-2">User Settings</h1>
        <p class="text-slate-500 font-medium tracking-wide">Manage your academic identity and personal profile across BrightPath.</p>
        
        <!-- Global Feedback Message -->
        <transition enter-active-class="animate-in fade-in slide-in-from-top-4" leave-active-class="animate-out fade-out slide-out-to-top-4">
          <div v-if="message.text" 
               :class="message.type === 'success' ? 'bg-[#A8E6CF] text-[#2C3E50] border-emerald-200' : 'bg-red-50 text-red-700 border-red-100'"
               class="absolute -top-4 right-0 px-6 py-3 rounded-2xl border shadow-lg font-bold text-sm z-50">
            {{ message.text }}
          </div>
        </transition>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Sidebar Column: Profile Visual -->
        <div class="lg:col-span-4 space-y-6">
          <div class="bg-white rounded-[2.5rem] p-10 shadow-2xl shadow-slate-200/50 border border-slate-100 flex flex-col items-center text-center relative overflow-hidden group transition-all duration-500 hover:shadow-blue-100/50">
            <div class="absolute inset-0 bg-gradient-to-b from-slate-50/50 to-white -z-0"></div>
            
            <!-- Avatar Circle -->
            <div class="relative mb-8 z-10">
              <div class="w-40 h-40 rounded-full border-[6px] border-white shadow-2xl flex items-center justify-center bg-gradient-to-tr from-[#4A90E2] to-[#2C3E50] text-white text-5xl font-black tracking-tighter transition-transform duration-700 group-hover:scale-105">
                 {{ initials }}
              </div>
              <div class="absolute -bottom-2 -right-2 bg-white p-2 rounded-2xl shadow-xl border border-slate-100">
                <span class="block px-3 py-1 bg-[#4A90E2] text-white rounded-lg text-[10px] font-black uppercase tracking-widest">{{ user.role }}</span>
              </div>
            </div>

            <h2 class="text-2xl font-black text-[#2C3E50] mb-2 leading-tight">{{ user.full_name || 'Set Your Name' }}</h2>
            <p class="text-sm font-bold text-[#4A90E2] uppercase tracking-[0.2em] opacity-80 mb-6">{{ user.student_id || 'ID NOT SET' }}</p>
            
            <div class="w-full h-px bg-slate-100 mb-6"></div>

            <!-- Stats/Simple Tags -->
            <div class="flex flex-wrap justify-center gap-2 z-10">
              <div class="px-4 py-2 bg-slate-50 rounded-xl border border-slate-100 text-[10px] font-black text-slate-500 uppercase tracking-widest">
                {{ user.academic_year || 'YEAR TBD' }}
              </div>
              <div class="px-4 py-2 bg-[#A8E6CF]/10 rounded-xl border border-[#A8E6CF]/30 text-[10px] font-black text-[#2e7d32] uppercase tracking-widest">
                {{ user.faculty || 'FACULTY TBD' }}
              </div>
            </div>
          </div>

          <!-- Quick Security Tip -->
          <div class="bg-gradient-to-br from-[#2C3E50] to-[#1A252F] rounded-[2rem] p-8 text-white shadow-xl relative overflow-hidden group">
            <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-white/5 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            <h4 class="text-lg font-black mb-4 flex items-center gap-2">
              <svg class="w-5 h-5 text-[#4A90E2]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 00-2 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
              Privacy First
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed font-medium">Your data is encrypted and only visible to you and verified academic staff. We never share your personal information with third parties.</p>
          </div>
        </div>

        <!-- Main Content: Form Sections -->
        <div class="lg:col-span-8 space-y-8">
          
          <!-- Section 1: Identity & Bio -->
          <div class="bg-white rounded-[2.5rem] p-10 shadow-sm border border-slate-100 relative group transition-all duration-300 hover:border-[#4A90E2]/20">
            <h3 class="text-xl font-black text-[#2C3E50] mb-8 flex items-center gap-4">
              <span class="w-12 h-12 rounded-2xl bg-blue-50 flex items-center justify-center text-[#4A90E2] shadow-inner group-hover:rotate-6 transition-transform">
                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
              </span>
              Identity Details
            </h3>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">Full Name</label>
                <div class="relative">
                  <input v-model="user.full_name" type="text" class="w-full px-6 py-4 bg-slate-50 border-2 border-transparent rounded-[1.25rem] focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-bold text-[#2C3E50] placeholder:text-slate-300" placeholder="John Doe" />
                  <div class="absolute right-4 top-1/2 -translate-y-1/2 opacity-20"><svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" /></svg></div>
                </div>
              </div>

              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">NIC Number</label>
                <input v-model="user.nic_number" type="text" class="w-full px-6 py-4 bg-slate-50 border-2 border-transparent rounded-[1.25rem] focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-bold text-[#2C3E50]" placeholder="199912345678" />
              </div>

              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">Contact Phone</label>
                <input v-model="user.phone_number" type="text" class="w-full px-6 py-4 bg-slate-50 border-2 border-transparent rounded-[1.25rem] focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-bold text-[#2C3E50]" placeholder="0712345678" />
              </div>

              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">Primary Email</label>
                <div class="relative">
                  <input v-model="user.email" type="email" disabled class="w-full px-6 py-4 bg-slate-100 border-2 border-transparent rounded-[1.25rem] text-slate-400 font-bold cursor-not-allowed opacity-60" />
                  <div class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-300"><svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 00-2 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 2: Academic Path -->
          <div class="bg-white rounded-[2.5rem] p-10 shadow-sm border border-slate-100 relative group transition-all duration-300 hover:border-[#4A90E2]/20">
            <h3 class="text-xl font-black text-[#2C3E50] mb-8 flex items-center gap-4">
              <span class="w-12 h-12 rounded-2xl bg-amber-50 flex items-center justify-center text-[#FFB800] shadow-inner group-hover:-rotate-6 transition-transform">
                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z" /><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" /></svg>
              </span>
              Academic Credentials
            </h3>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">University / Institute</label>
                <input v-model="user.university" type="text" class="w-full px-6 py-4 bg-slate-50 border-2 border-transparent rounded-[1.25rem] focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-bold text-[#2C3E50]" placeholder="SLIIT" />
              </div>

              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">Faculty</label>
                <select v-model="user.faculty" class="w-full px-6 py-4 bg-slate-50 border-2 border-transparent rounded-[1.25rem] focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-bold text-[#2C3E50] appearance-none">
                  <option value="">Select Faculty</option>
                  <option value="Computing">Computing</option>
                  <option value="Business">Business</option>
                  <option value="Engineering">Engineering</option>
                  <option value="Humanities & Sciences">Humanities & Sciences</option>
                </select>
              </div>

              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">Academic Year</label>
                <select v-model="user.academic_year" class="w-full px-6 py-4 bg-slate-50 border-2 border-transparent rounded-[1.25rem] focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-bold text-[#2C3E50] appearance-none">
                  <option value="">Select Year</option>
                  <option value="Year 1">Year 1</option>
                  <option value="Year 2">Year 2</option>
                  <option value="Year 3">Year 3</option>
                  <option value="Year 4">Year 4</option>
                </select>
              </div>

              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">Academic Stream</label>
                <select v-model="user.academic_stream" class="w-full px-6 py-4 bg-slate-50 border-2 border-transparent rounded-[1.25rem] focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-bold text-[#2C3E50] appearance-none">
                  <option value="">Select Stream</option>
                  <option value="Software Engineering">Software Engineering</option>
                  <option value="Data Science">Data Science</option>
                  <option value="Information Technology">Information Technology</option>
                  <option value="Computer Systems & Network">Computer Systems & Network</option>
                  <option value="Interactive Media">Interactive Media</option>
                  <option value="Cyber Security">Cyber Security</option>
                  <option value="Business Management">Business Management</option>
                </select>
              </div>

              <div class="space-y-3">
                <label class="text-[11px] font-black text-slate-400 uppercase tracking-widest ml-1">Student Registration ID</label>
                <input v-model="user.student_id" type="text" class="w-full px-6 py-4 bg-slate-50 border-2 border-transparent rounded-[1.25rem] focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-bold text-[#2C3E50]" placeholder="IT21001122" />
              </div>
            </div>
          </div>

          <!-- Bottom Action Bar -->
          <div class="flex flex-col sm:flex-row gap-4 justify-between items-center bg-[#2C3E50]/5 p-8 rounded-[2.5rem] border border-slate-200/50 transition-all duration-500 hover:bg-[#2C3E50]/10">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-white rounded-xl flex items-center justify-center text-emerald-500 shadow-sm">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
              </div>
              <p class="text-xs font-bold text-slate-500 leading-tight">All changes are immediate. <br/> Make sure your academic details are correct.</p>
            </div>
            
            <button 
              @click="updateProfile"
              :disabled="isSaving"
              class="group relative px-10 py-4 bg-gradient-to-tr from-[#4A90E2] to-[#3A7BC8] text-white rounded-[1.25rem] font-black text-sm uppercase tracking-widest overflow-hidden transition-all hover:scale-105 active:scale-95 disabled:opacity-50 disabled:cursor-wait shadow-xl shadow-blue-200"
            >
              <span v-if="isSaving" class="flex items-center gap-2">
                <svg class="w-4 h-4 animate-spin" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                Syncing...
              </span>
              <span v-else class="flex items-center gap-2">
                Save Profile
                <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M14 5l7 7m0 0l-7 7m7-7H3" /></svg>
              </span>
            </button>
          </div>

        </div>
      </div>
    </template>
  </div>
</template>

<style scoped>
/* Custom transitions/scrollbars if needed */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
