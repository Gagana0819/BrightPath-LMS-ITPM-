<script setup>
import { ref, onMounted } from 'vue'

const user = ref({
  firstName: 'Student',
  lastName: '',
  email: 'student@university.edu',
  studentId: '',
  verified: false,
  verificationStatus: 'action_required', // 'verified', 'pending', 'action_required'
  verificationDoc: null
})

const isUploadingDoc = ref(false)
const uploadProgress = ref(0)
const showUploadSuccess = ref(false)

const handleDocUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    user.value.verificationDoc = file
    startVerificationUpload()
  }
}

const startVerificationUpload = () => {
  isUploadingDoc.value = true
  uploadProgress.value = 0
  
  const interval = setInterval(() => {
    if (uploadProgress.value < 100) {
      uploadProgress.value += 10
    } else {
      clearInterval(interval)
      isUploadingDoc.value = false
      showUploadSuccess.value = true
      user.value.verificationStatus = 'pending'
    }
  }, 200)
}

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
          
          <div v-if="user.verified" class="inline-flex items-center gap-1.5 px-4 py-2 bg-[#A8E6CF]/20 text-[#2C3E50] rounded-full font-bold text-xs uppercase tracking-widest border border-[#A8E6CF] shadow-sm z-10 animate-in zoom-in duration-300">
            <svg class="w-4 h-4 text-[#2C3E50]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Verified Identity
          </div>
          <div v-else-if="user.verificationStatus === 'pending'" class="inline-flex items-center gap-1.5 px-4 py-2 bg-blue-50 text-blue-700 rounded-full font-bold text-xs uppercase tracking-widest border border-blue-100 shadow-sm z-10">
            <svg class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Review Pending
          </div>
          <div v-else class="inline-flex items-center gap-1.5 px-4 py-2 bg-red-50 text-red-700 rounded-full font-bold text-xs uppercase tracking-widest border border-red-100 shadow-sm z-10">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
            Unverified
          </div>
        </div>
      </div>

      <!-- Right Column: Settings Form -->
      <div class="md:col-span-2 space-y-8">
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

        <!-- Identity Verification Section -->
        <div v-if="!user.verified" class="bg-white rounded-3xl p-8 shadow-sm border border-slate-100 relative overflow-hidden animate-in slide-in-from-top-4 duration-500">
          <div class="flex items-center justify-between mb-8">
            <h3 class="text-xl font-extrabold text-[#2C3E50] flex items-center gap-3">
              <span class="w-8 h-8 rounded-lg bg-red-50 flex items-center justify-center text-red-500">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
              </span>
              Identity Verification
            </h3>
            <span v-if="user.verificationStatus === 'pending'" class="text-[10px] font-black bg-blue-50 text-blue-600 px-3 py-1 rounded-md uppercase tracking-widest border border-blue-100">Under Review</span>
          </div>

          <div v-if="user.verificationStatus === 'action_required'" class="space-y-6">
            <div class="bg-slate-50 border border-dashed border-slate-200 rounded-[24px] p-8 text-center group hover:bg-white hover:border-[#4A90E2] transition-all duration-300 relative cursor-pointer">
              <input type="file" @change="handleDocUpload" class="absolute inset-0 opacity-0 cursor-pointer z-20" />
              <div class="w-16 h-16 bg-white rounded-2xl shadow-sm flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300">
                <svg class="w-8 h-8 text-slate-400 group-hover:text-[#4A90E2]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
                </svg>
              </div>
              <p class="text-slate-600 font-bold mb-1">Click to upload your Student ID or University Document</p>
              <p class="text-[11px] text-slate-400 font-medium uppercase tracking-wider">Supports PDF, PNG, JPG (Max 5MB)</p>
              
              <!-- Progress overlay -->
              <div v-if="isUploadingDoc" class="absolute inset-0 bg-white/90 backdrop-blur-sm z-30 flex flex-col items-center justify-center p-8 rounded-[24px]">
                 <div class="w-full max-w-xs space-y-3">
                   <div class="flex justify-between items-center">
                     <span class="text-xs font-black text-[#4A90E2] uppercase tracking-widest">Uploading Document...</span>
                     <span class="text-xs font-black text-slate-400">{{ uploadProgress }}%</span>
                   </div>
                   <div class="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden border border-slate-200/50">
                     <div class="bg-[#4A90E2] h-full transition-all duration-300 ease-out" :style="{ width: uploadProgress + '%' }"></div>
                   </div>
                 </div>
              </div>
            </div>
            
            <div class="flex items-start gap-4 p-5 bg-blue-50/50 rounded-2xl border border-blue-100/50">
               <svg class="w-5 h-5 text-[#4A90E2] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
               <p class="text-xs font-medium text-slate-600 leading-relaxed">
                 To access specialized content like **Exam Past Papers**, we need to verify your university identity. Our team usually reviews documents within 24-48 hours.
               </p>
            </div>
          </div>

          <div v-else-if="user.verificationStatus === 'pending'" class="py-6 flex flex-col items-center justify-center text-center">
             <div class="w-20 h-20 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center mb-6 shadow-inner animate-pulse">
                <svg class="w-10 h-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
             </div>
             <h4 class="text-lg font-extrabold text-[#2C3E50] mb-2 tracking-tight">Your documents are under review!</h4>
             <p class="text-slate-500 text-sm font-medium">We'll notify you as soon as your account is fully verified.</p>
             <button @click="user.verificationStatus = 'action_required'" class="mt-6 text-[11px] font-black text-slate-400 hover:text-red-500 transition-colors uppercase tracking-widest">Cancel & Re-upload</button>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
