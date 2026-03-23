<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const isLoggedIn = ref(!!localStorage.getItem('access_token'))

const updateAuthState = () => {
  isLoggedIn.value = !!localStorage.getItem('access_token')
}

onMounted(updateAuthState)
watch(() => route.path, updateAuthState)

const logoTarget = computed(() => isLoggedIn.value ? '/dashboard' : '/')
</script>

<template>
  <header class="fixed top-0 left-0 w-full z-50 transition-all duration-300 bg-white/80 backdrop-blur-md border-b border-slate-200/50 shadow-sm px-20">
    <div class="max-w-[1600px] mx-auto px-4 lg:px-6 relative flex justify-between items-center h-[72px]">
      
      <!-- Brand -->
      <div class="brand z-20 flex-shrink-0">
        <RouterLink :to="logoTarget" class="flex items-center gap-2 text-[1.4rem] font-bold text-brand tracking-tight">
          BRIGHTPATH
        </RouterLink>
      </div>

      <!-- Navigation Links -->
      <nav class="hidden md:flex gap-10 absolute left-1/2 -translate-x-1/2 z-10 justify-center">
        <RouterLink to="/" class="text-slate-600 font-medium text-[0.95rem] tracking-wide relative pb-2 hover:text-brand transition-colors after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full after:h-[3px] after:bg-brand after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:origin-center [&.active]:text-brand [&.active]:font-semibold [&.active]:after:scale-x-100" exact-active-class="active">Home</RouterLink>
        <RouterLink to="/about" class="text-slate-600 font-medium text-[0.95rem] tracking-wide relative pb-2 hover:text-brand transition-colors after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full after:h-[3px] after:bg-brand after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:origin-center [&.active]:text-brand [&.active]:font-semibold [&.active]:after:scale-x-100" active-class="active">About Us</RouterLink>
        <RouterLink to="/digital-library" class="text-slate-600 font-medium text-[0.95rem] tracking-wide relative pb-2 hover:text-brand transition-colors after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full after:h-[3px] after:bg-brand after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:origin-center [&.active]:text-brand [&.active]:font-semibold [&.active]:after:scale-x-100" active-class="active">Digital Library</RouterLink>
        <RouterLink to="/sessions" class="text-slate-600 font-medium text-[0.95rem] tracking-wide relative pb-2 hover:text-brand transition-colors after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full after:h-[3px] after:bg-brand after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:origin-center [&.active]:text-brand [&.active]:font-semibold [&.active]:after:scale-x-100" active-class="active">Sessions</RouterLink>
      </nav>

      <!-- Action Buttons -->
      <div class="hidden md:flex z-20 items-center gap-6 flex-shrink-0">
        <template v-if="!isLoggedIn">
          <RouterLink to="/login" class="font-semibold text-[0.95rem] text-slate-700 hover:text-brand transition-colors">
            Log In
          </RouterLink>
          <RouterLink to="/register" class="inline-flex items-center justify-center px-6 py-2.5 rounded text-[0.95rem] font-bold text-white bg-brand hover:bg-brand-hover transition-all shadow-sm flex-shrink-0">
            Join for Free
          </RouterLink>
        </template>
        <template v-else>
          <RouterLink to="/dashboard" class="inline-flex items-center justify-center px-6 py-2.5 rounded text-[0.95rem] font-bold text-white bg-brand hover:bg-brand-hover transition-all shadow-sm flex-shrink-0 gap-2">
            Go to Dashboard 
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 7l5 5m0 0l-5 5m5-5H6"></path></svg>
          </RouterLink>
        </template>
      </div>
      
    </div>
  </header>
</template>
