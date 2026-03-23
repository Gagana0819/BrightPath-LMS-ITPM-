<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api/axios'
import AppNavbar from '../components/layout/AppNavbar.vue'

const router = useRouter()

// 1 = Input Credentials, 2 = Success
const currentStep = ref(1)

const formData = ref({
  email: '',
  nicNumber: '',
  newPassword: '',
  confirmPassword: ''
})

const errors = ref({})
const isLoading = ref(false)
const showNewPassword = ref(false)
const showConfirmPassword = ref(false)

const handleResetPassword = async () => {
  const newErrors = {}
  
  if (!formData.value.email) {
    newErrors.email = 'Email Address is required.'
  } else if (!/^\S+@\S+\.\S+$/.test(formData.value.email)) {
    newErrors.email = 'Please enter a valid email address.'
  }

  if (!formData.value.nicNumber) {
    newErrors.nicNumber = 'NIC Number is required.'
  }

  if (!formData.value.newPassword) {
    newErrors.newPassword = 'New password is required.'
  } else if (formData.value.newPassword.length < 8) {
    newErrors.newPassword = 'Password must be at least 8 characters long.'
  }
  
  if (!formData.value.confirmPassword) {
    newErrors.confirmPassword = 'Confirm your new password.'
  } else if (formData.value.newPassword !== formData.value.confirmPassword) {
    newErrors.confirmPassword = 'Passwords do not match.'
  }

  if (Object.keys(newErrors).length > 0) {
    errors.value = newErrors
    return
  }

  errors.value = {}
  isLoading.value = true
  
  try {
    const response = await api.post('accounts/reset-password/', {
      email: formData.value.email,
      nic_number: formData.value.nicNumber,
      new_password: formData.value.newPassword
    })
    
    if (response.status === 200) {
      currentStep.value = 2
    }
  } catch (err) {
    if (err.response && err.response.data) {
      errors.value = { global: err.response.data.error || 'Reset failed.' }
    } else {
      errors.value = { global: 'An unexpected error occurred.' }
    }
  } finally {
    isLoading.value = false
  }
}

const fillDemoData = () => {
  formData.value.email = 'jane.doe@example.com'
  formData.value.nicNumber = '991234567V'
  formData.value.newPassword = 'NewSecurePassword123!'
  formData.value.confirmPassword = 'NewSecurePassword123!'
  errors.value = {}
}
</script>

<template>
  <div class="min-h-screen bg-hero-bg-pill flex flex-col font-sans text-content relative overflow-hidden">
    <div class="absolute top-0 right-0 w-1/3 h-full bg-hero-bg-right clip-path-slant z-0 opacity-20"></div>

    <AppNavbar class="z-20 relative" />
    
    <main class="flex-1 flex flex-col items-center justify-center p-4 sm:p-8 z-10 relative">
      <div class="w-full max-w-lg bg-white rounded-[2rem] shadow-[0_10px_40px_rgba(0,0,0,0.06)] border border-slate-100 overflow-hidden relative">
        <div class="p-8 sm:p-14 relative z-10 text-center animate-fade-in-up flex flex-col items-center justify-center w-full">
          
          <!-- STEP 1: RESET FORM -->
          <template v-if="currentStep === 1">
            <h1 class="text-3xl font-bold text-slate-800 mb-3">Reset Your Password</h1>
            <p class="text-slate-500 mb-10 text-[1.05rem] leading-relaxed">Enter your Email and NIC number to create a new password.</p>

            <button type="button" @click="fillDemoData" 
              class="absolute top-8 right-8 text-xs font-bold text-brand border-2 border-brand bg-transparent hover:bg-brand/10 px-4 py-1.5 rounded-full transition-all shadow-sm flex items-center gap-1.5 tracking-wide z-20">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              DEMO
            </button>

            <form @submit.prevent="handleResetPassword" novalidate class="w-full space-y-6 text-left">
              <div v-if="errors.global" class="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-xl text-sm font-bold flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                {{ errors.global }}
              </div>

              <div>
                <label for="email" class="block text-sm font-bold text-slate-800 mb-2 tracking-wide">Email Address</label>
                <input type="email" id="email" v-model="formData.email"
                  class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:outline-none focus:ring-2 focus:ring-[#97C4C4] transition-all duration-200"
                  :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.email}"
                  placeholder="Enter your email" />
                <p v-if="errors.email" class="text-red-500 text-sm mt-2 font-bold">{{ errors.email }}</p>
              </div>

              <div>
                <label for="nicNumber" class="block text-sm font-bold text-slate-800 mb-2 tracking-wide">NIC Number</label>
                <input type="text" id="nicNumber" v-model="formData.nicNumber"
                  class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:outline-none focus:ring-2 focus:ring-[#97C4C4] transition-all duration-200"
                  :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.nicNumber}"
                  placeholder="Enter your NIC" />
                <p v-if="errors.nicNumber" class="text-red-500 text-sm mt-2 font-bold">{{ errors.nicNumber }}</p>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label for="newPassword" class="block text-sm font-bold text-slate-800 mb-2">New Password</label>
                  <div class="relative">
                    <input :type="showNewPassword ? 'text' : 'password'" id="newPassword" v-model="formData.newPassword"
                      class="w-full px-4 py-3.5 pr-10 rounded-xl border-[1.5px] border-[#97C4C4]/50 bg-white focus:outline-none focus:ring-2 focus:ring-[#97C4C4] transition-all"
                      :class="{'border-red-400': errors.newPassword}" />
                    <button type="button" @click="showNewPassword = !showNewPassword" class="absolute right-3 top-[14px] text-slate-400">
                      <svg v-if="!showNewPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                      <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path></svg>
                    </button>
                  </div>
                  <p v-if="errors.newPassword" class="text-red-500 text-xs mt-1 font-bold">{{ errors.newPassword }}</p>
                </div>
                <div>
                  <label for="confirmPassword" class="block text-sm font-bold text-slate-800 mb-2">Confirm</label>
                  <div class="relative">
                    <input :type="showConfirmPassword ? 'text' : 'password'" id="confirmPassword" v-model="formData.confirmPassword"
                      class="w-full px-4 py-3.5 pr-10 rounded-xl border-[1.5px] border-[#97C4C4]/50 bg-white focus:outline-none focus:ring-2 focus:ring-[#97C4C4] transition-all"
                      :class="{'border-red-400': errors.confirmPassword}" />
                    <button type="button" @click="showConfirmPassword = !showConfirmPassword" class="absolute right-3 top-[14px] text-slate-400">
                      <svg v-if="!showConfirmPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                      <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path></svg>
                    </button>
                  </div>
                  <p v-if="errors.confirmPassword" class="text-red-500 text-xs mt-1 font-bold">{{ errors.confirmPassword }}</p>
                </div>
              </div>

              <div class="pt-4">
                <button type="submit" :disabled="isLoading"
                  class="w-full bg-hero-highlight hover:bg-hero-highlight/90 text-white font-bold py-4 px-8 rounded-full transition-all duration-200 transform hover:scale-105 shadow-lg disabled:opacity-50 flex items-center justify-center space-x-2 tracking-wide uppercase">
                  <svg v-if="isLoading" class="animate-spin -ml-1 mr-2 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                  <span>{{ isLoading ? 'UPDATING...' : 'UPDATE PASSWORD' }}</span>
                </button>
              </div>
            </form>
          </template>

          <!-- STEP 2: SUCCESS -->
          <template v-else>
            <div class="w-24 h-24 bg-green-100 text-green-500 rounded-full flex items-center justify-center mb-6 mx-auto">
              <svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="3"><path d="M20 6L9 17l-5-5"></path></svg>
            </div>
            <h1 class="text-3xl font-bold text-slate-800 mb-3">Password Updated!</h1>
            <p class="text-slate-500 mb-10 text-[1.05rem]">Your password has been changed successfully. You can now login.</p>
            <router-link to="/login" class="w-full bg-hero-highlight hover:bg-hero-highlight/90 text-white font-bold py-4 px-12 rounded-full transition-all duration-300 block text-center uppercase">Login Now</router-link>
          </template>

          <p v-if="currentStep === 1" class="text-center mt-10 pb-2 text-sm text-slate-500 border-t border-slate-100 pt-8 w-full">
            Back to <router-link to="/login" class="text-hero-highlight font-bold transition-opacity">LOGIN</router-link>
          </p>
        </div>
      </div>
    </main>
  </div>
</template>
