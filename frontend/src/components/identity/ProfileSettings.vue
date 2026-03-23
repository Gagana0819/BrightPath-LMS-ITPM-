<script setup>
import { ref, onMounted } from 'vue'

const user = ref({
  firstName: 'Student',
  lastName: '',
  email: 'student@university.edu',
  studentId: '',
  verified: true
})

onMounted(() => {
  const token = localStorage.getItem('access_token')
  if (token) {
    const fName = localStorage.getItem('first_name')
    const lName = localStorage.getItem('last_name')
    const fullName = localStorage.getItem('full_name')

    if (fullName) {
      const parts = fullName.split(' ')
      user.value.firstName = parts[0]
      user.value.lastName = parts.slice(1).join(' ')
    } else if (fName && lName) {
      user.value.firstName = fName
      user.value.lastName = lName
    }
    
    const email = localStorage.getItem('email') || localStorage.getItem('username')
    if (email) user.value.email = email
    
    const studentId = localStorage.getItem('student_id')
    if (studentId) user.value.studentId = studentId
  }
})
</script>

<template>
  <div class="w-full max-w-4xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500 font-sans">
    
    <!-- Header -->
    <div class="border-b border-slate-200 pb-5">
      <h1 class="text-3xl font-extrabold tracking-tight text-[#2C3E50] mb-2">Profile Settings</h1>
      <p class="text-slate-500 text-[0.95rem]">Manage your identity verified status and personal details.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Left Column: Avatar & Status -->
      <div class="md:col-span-1 space-y-6">
        <div class="bg-[#F4F7F9] rounded-3xl p-8 shadow-sm border border-slate-200/60 flex flex-col items-center text-center relative overflow-hidden group">
          <!-- Decorative Background element -->
          <div class="absolute -top-10 -right-10 w-32 h-32 bg-[#4A90E2]/10 rounded-full blur-2xl"></div>

          <div class="relative mb-5 z-10">
            <div class="w-32 h-32 rounded-full border-4 border-white shadow-xl flex items-center justify-center bg-gradient-to-br from-[#4A90E2] to-[#2C3E50] text-white text-4xl font-black tracking-widest overflow-hidden">
               {{ user.firstName.charAt(0) }}{{ user.lastName.charAt(0) }}
            </div>
            <button class="absolute bottom-1 right-1 bg-[#4A90E2] text-white p-2.5 rounded-full shadow-lg hover:bg-[#3A7BC8] hover:scale-105 transition-all">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
              </svg>
            </button>
          </div>
          <h2 class="text-xl font-extrabold text-[#2C3E50] z-10 uppercase tracking-tight">{{ user.firstName }} <br /> {{ user.lastName }}</h2>
          <p class="text-sm font-semibold text-[#4A90E2] mb-5 z-10">{{ user.studentId }}</p>
          
          <div v-if="user.verified" class="inline-flex items-center gap-1.5 px-4 py-2 bg-[#A8E6CF]/20 text-[#2C3E50] rounded-full font-bold text-xs uppercase tracking-widest border border-[#A8E6CF] shadow-sm z-10">
            <svg class="w-4 h-4 text-[#2C3E50]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Verified Identity
          </div>
        </div>
      </div>

      <!-- Right Column: Settings Form -->
      <div class="md:col-span-2">
        <div class="bg-white rounded-3xl p-8 shadow-sm border border-slate-100 relative overflow-hidden">
          
          <h3 class="text-xl font-extrabold text-[#2C3E50] mb-8 flex items-center gap-3">
            <span class="w-8 h-8 rounded-lg bg-[#F4F7F9] flex items-center justify-center text-[#4A90E2]">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
            </span>
            Personal Information
          </h3>
          
          <div class="space-y-6">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label class="text-xs font-bold text-slate-400 uppercase tracking-wider">First Name</label>
                <input v-model="user.firstName" type="text" class="w-full px-5 py-3.5 bg-[#F4F7F9] text-[#2C3E50] border-2 border-transparent hover:border-slate-200 rounded-2xl focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-semibold" />
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-slate-400 uppercase tracking-wider">Last Name</label>
                <input v-model="user.lastName" type="text" class="w-full px-5 py-3.5 bg-[#F4F7F9] text-[#2C3E50] border-2 border-transparent hover:border-slate-200 rounded-2xl focus:bg-white focus:border-[#4A90E2] focus:ring-4 focus:ring-[#4A90E2]/10 outline-none transition-all font-semibold" />
              </div>
            </div>

            <div class="space-y-2">
              <label class="text-xs font-bold text-slate-400 uppercase tracking-wider">University Email Address</label>
              <input v-model="user.email" type="email" disabled class="w-full px-5 py-3.5 bg-slate-50 border border-slate-200 rounded-2xl text-slate-400 font-medium cursor-not-allowed" />
              <p class="text-[11px] font-bold text-[#A8E6CF] mt-2 tracking-wide uppercase flex items-center gap-1">
                <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                Contact admin to change your primary Academic Email.
              </p>
            </div>

            <div class="pt-6 mt-6 border-t border-slate-100 flex justify-end">
              <button class="px-8 py-3.5 bg-[#4A90E2] hover:bg-[#3A7BC8] hover:shadow-lg hover:-translate-y-0.5 active:scale-[0.98] text-white rounded-2xl font-bold tracking-wide transition-all uppercase text-sm flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" /></svg>
                Save Changes
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
