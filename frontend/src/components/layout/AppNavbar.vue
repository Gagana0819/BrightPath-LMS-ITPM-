<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <header class="fixed top-0 left-0 w-full z-50 py-4 transition-all duration-300">
    <div class="max-w-[1800px] mx-auto px-4 lg:px-6 relative flex justify-between items-center h-[80px]">
      
      <!-- Brand -->
      <div 
        class="brand z-20 transition-all duration-300 ease-in-out"
        :class="[isScrolled ? 'opacity-0 invisible -translate-y-4' : 'opacity-100 visible translate-y-0']"
      >
        <RouterLink to="/" class="flex items-center gap-2 text-2xl font-bold text-content tracking-tight">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" class="text-brand">
            <path d="M4 19V5C4 3.89543 4.89543 3 6 3H19V19C19 20.1046 18.1046 21 17 21H6C4.89543 21 4 20.1046 4 19Z" stroke="currentColor" stroke-width="2"/>
            <path d="M4 15L15 3" stroke="currentColor" stroke-width="2"/>
            <path d="M10 12L10 21" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
            <path d="M14 12L14 21" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
          </svg>
          BrightPath
        </RouterLink>
      </div>

      <!-- Center Background Pill -->
      <div class="absolute left-1/2 -translate-x-1/2 w-full max-w-[500px] h-[80px] bg-hero-bg-pill shadow-[0_2px_10px_rgba(0,0,0,0.1)] rounded-[50px] z-0 transition-all duration-300"></div>

      <!-- Navigation Links -->
      <nav class="hidden md:flex gap-12 absolute left-1/2 -translate-x-1/2 z-10 w-full justify-center">
        <RouterLink to="/dashboard" class="text-content font-medium text-[1.3rem] tracking-wide relative pb-1 hover:text-blue-600 transition-colors after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full after:h-[2px] after:bg-blue-600 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:origin-left [&.active]:text-content [&.active]:after:scale-x-100" exact-active-class="active">HOME</RouterLink>
        <RouterLink to="/library" class="text-content font-medium text-[1.3rem] tracking-wide relative pb-1 hover:text-blue-600 transition-colors after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full after:h-[2px] after:bg-blue-600 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:origin-left [&.active]:text-content [&.active]:after:scale-x-100" active-class="active">LIBRARY</RouterLink>
        <RouterLink to="/dashboard/kuppi" class="text-content font-medium text-[1.3rem] tracking-wide relative pb-1 hover:text-blue-600 transition-colors after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full after:h-[2px] after:bg-blue-600 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:origin-left [&.active]:text-content [&.active]:after:scale-x-100" active-class="active">KUPPI</RouterLink>
        <RouterLink to="/courses" class="text-content font-medium text-[1.3rem] tracking-wide relative pb-1 hover:text-blue-600 transition-colors after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full after:h-[2px] after:bg-blue-600 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:origin-left [&.active]:text-content [&.active]:after:scale-x-100" active-class="active">COURSES</RouterLink>
        
      </nav>

      <!-- Action Buttons -->
      <div 
        class="hidden md:flex z-20 items-center gap-4 transition-all duration-300 ease-in-out"
        :class="[isScrolled ? 'opacity-0 invisible -translate-y-4' : 'opacity-100 visible translate-y-0']"
      >
        <button class="relative p-2.5 rounded-full text-content hover:bg-black/5 hover:text-brand transition-all" aria-label="Notifications">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
          </svg>
          <span class="absolute top-1.5 right-2 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white"></span>
        </button>
<<<<<<< HEAD
        <RouterLink to="/login" class="inline-flex items-center justify-center px-8 py-2.5 rounded-full font-bold text-[1.1rem] text-white bg-hero-highlight hover:opacity-90 transition-all shadow-md hover:shadow-lg hover:-translate-y-0.5">
=======
        <RouterLink to="/login" class="inline-flex items-center justify-center px-8 py-2.5 rounded-full font-bold tracking-wider uppercase text-[1.1rem] text-white bg-hero-highlight hover:opacity-90 transition-all duration-200 shadow-md hover:shadow-lg hover:scale-105">
>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
          LOGIN
        </RouterLink>
      </div>
      
    </div>
  </header>
</template>
