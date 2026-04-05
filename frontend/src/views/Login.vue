<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api/axios'
import AppNavbar from '../components/layout/AppNavbar.vue'

const router = useRouter()

const formData = ref({
  email: '',
  password: ''
})

const errors = ref({})
const isLoading = ref(false)
const showPassword = ref(false)

const validateForm = () => {
  const newErrors = {}
  
  if (!formData.value.email) newErrors.email = 'Email Address is required.'
  else if (!/^\S+@\S+\.\S+$/.test(formData.value.email)) newErrors.email = 'Please enter a valid email address.'
  
  if (!formData.value.password) newErrors.password = 'Password is required.'

  errors.value = newErrors
  return Object.keys(newErrors).length === 0
}

const handleLogin = async () => {
  if (!validateForm()) return
  isLoading.value = true
  errors.value = {}

  try {
    const response = await api.post('accounts/login/', {
      username: formData.value.email, // backend expects 'username' as email
      password: formData.value.password
    })

    if (response.status === 200) {
      localStorage.setItem('access_token', response.data.access)
      localStorage.setItem('refresh_token', response.data.refresh)
      localStorage.setItem('user_role', response.data.role)
      localStorage.setItem('full_name', response.data.full_name)
      localStorage.setItem('user_id', response.data.user_id)
      
      // Redirect to the intended page (e.g. kuppi dashboard) or default dashboard
      const redirectPath = router.currentRoute.value.query.redirect || '/dashboard'
      router.push(redirectPath)
    }
  } catch (err) {
    if (err.response && err.response.data) {
      errors.value = { global: err.response.data.detail || 'Login failed. Please check credentials.' }
    } else {
      errors.value = { global: 'An unexpected error occurred.' }
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-hero-bg-pill flex flex-col font-sans text-content relative overflow-hidden">
    <div class="absolute top-0 right-0 w-1/3 h-full bg-hero-bg-right clip-path-slant z-0 opacity-20"></div>

    <AppNavbar class="z-20 relative" />
    
    <main class="flex-1 flex items-center justify-center p-4 sm:p-8 z-10 relative">
      <div class="w-full max-w-lg bg-white rounded-[2rem] shadow-[0_10px_40px_rgba(0,0,0,0.06)] border border-slate-100 overflow-hidden relative">
        <div class="p-8 sm:p-12 relative z-10 animate-fade-in-up">
          
          <div class="text-center mb-10">
            <h1 class="text-3xl sm:text-4xl font-bold text-slate-800 mb-3">Welcome Back!</h1>
            <p class="text-slate-500 text-lg">Please enter your details to sign in.</p>
          </div>

          <form @submit.prevent="handleLogin" novalidate class="space-y-6">
            <div v-if="errors.global" class="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-xl text-sm font-bold flex items-center gap-2">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
              {{ errors.global }}
            </div>

            <div>
              <label for="email" class="block text-sm font-bold text-content mb-2 tracking-wide">Email Address</label>
              <input type="email" id="email" v-model="formData.email"
                class="w-full px-4 py-3.5 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:outline-none focus:ring-2 focus:ring-[#97C4C4] transition-all duration-200 placeholder:text-slate-400 text-content "
                :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.email}"
                placeholder="user@university.edu" />
              <p v-if="errors.email" class="text-red-500 text-sm mt-2 font-bold">{{ errors.email }}</p>
            </div>

            <div>
              <div class="flex items-center justify-between mb-2">
                <label for="password" class="block text-sm font-bold text-content tracking-wide">Password</label>
                <router-link to="/forgot-password" class="text-sm text-hero-highlight hover:text-hero-highlight/80 font-bold transition-colors">Forgot Password?</router-link>
              </div>
              <div class="relative">
                <input :type="showPassword ? 'text' : 'password'" id="password" v-model="formData.password"
                  class="w-full px-4 py-3.5 pr-12 rounded-xl border-[1.5px] border-[#97C4C4]/50 hover:border-[#97C4C4] bg-white focus:outline-none focus:ring-2 focus:ring-[#97C4C4] transition-all duration-200 placeholder:text-slate-400 text-content "
                  :class="{'border-red-400 focus:border-red-500 bg-red-50/30': errors.password}"
                  placeholder="Enter your password" />
                <button type="button" @click="showPassword = !showPassword" class="absolute right-4 top-[14px] text-slate-400 hover:text-slate-800 transition-colors focus:outline-none">
                  <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                  <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path></svg>
                </button>
              </div>
              <p v-if="errors.password" class="text-red-500 text-sm mt-2 font-bold">{{ errors.password }}</p>
            </div>

            <div class="pt-2">
              <button type="submit" :disabled="isLoading"
                class="w-full bg-hero-highlight hover:bg-hero-highlight/90 text-white font-bold py-4 px-8 rounded-full transition-all duration-200 transform hover:scale-105 shadow-lg disabled:opacity-70 flex items-center justify-center space-x-2 tracking-wider text-[1.1rem] uppercase">
                <svg v-if="isLoading" class="animate-spin -ml-1 mr-2 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span>{{ isLoading ? 'SIGNING IN...' : 'LOGIN' }}</span>
              </button>
            </div>

          </form>

          <p class="text-center mt-10 text-base text-slate-500 border-t border-slate-100 pt-8 w-full">
            Don't have an account? 
            <router-link to="/register" class="text-hero-highlight hover:opacity-80 font-bold tracking-wide transition-opacity">REGISTER</router-link>
          </p>

        </div>
      </div>
    </main>
  </div>
</template>
