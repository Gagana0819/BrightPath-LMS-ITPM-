<script setup>
import { computed } from 'vue'
import { RouterLink, useRoute } from 'vue-router'

const route = useRoute()

// Helper to get role from localStorage
const userRole = computed(() => localStorage.getItem('user_role') || 'STUDENT')

const allNavItems = [
  { name: 'Home', path: '/dashboard/home', icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
  { name: 'My Dashboard', path: '/dashboard', icon: 'M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z' },
  { name: 'Digital Library', path: '/dashboard/library', icon: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253' },
  { name: 'Kuppi Sessions', path: '/dashboard/kuppi', icon: 'M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z' },
  { name: 'Wallet', path: '/dashboard/wallet', icon: 'M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z' },
  
  // Specific role-based items
  { name: 'Upload Course', path: '/dashboard/upload', icon: 'M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12', hideFor: ['STUDENT'] },
  
  { name: 'Profile Settings', path: '/dashboard/profile', icon: 'M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z' }
]

const navItems = computed(() => {
  return allNavItems.filter(item => {
    if (!item.hideFor) return true
    return !item.hideFor.includes(userRole.value)
  })
})

const isActive = (path) => {
  // Exact match for Home and Overview to prevent false highlights
  if (path === '/' || path === '/dashboard') return route.path === path
  // Prefix match for all other paths (e.g. /dashboard/kuppi, /dashboard/library)
  return route.path.startsWith(path)
}

const handleLogout = () => {
  localStorage.clear()
  window.location.href = '/login'
}
</script>

<template>
  <aside class="w-64 bg-[#2C3E50] text-white flex-col h-full shadow-lg z-20 flex transition-all duration-300">
    
    <!-- Brand Header -->
    <div class="h-[80px] flex items-center px-6 border-b border-white/10">
      <RouterLink to="/" class="flex items-center gap-2 text-[22px] font-extrabold tracking-tight hover:opacity-80 transition-opacity cursor-pointer">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" class="text-hero-highlight drop-shadow-md">
          <path d="M4 19V5C4 3.89543 4.89543 3 6 3H19V19C19 20.1046 18.1046 21 17 21H6C4.89543 21 4 20.1046 4 19Z" stroke="currentColor" stroke-width="2"/>
          <path d="M4 15L15 3" stroke="currentColor" stroke-width="2"/>
          <path d="M10 12L10 21" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
          <path d="M14 12L14 21" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
        </svg>
        BrightPath<span class="text-hero-highlight font-normal ml-[-2px]">LMS</span>
      </RouterLink>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 py-8 px-4 flex flex-col gap-2">
      <RouterLink 
        v-for="item in navItems" 
        :key="item.name"
        :to="item.path"
        class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 group"
        :class="isActive(item.path) ? 'bg-hero-highlight text-white shadow-md' : 'text-slate-400 hover:bg-white/5 hover:text-white'"
      >
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" :d="item.icon" />
        </svg>
        <span class="font-medium text-[0.95rem] tracking-wide">{{ item.name }}</span>
      </RouterLink>
    </nav>
    
    <!-- Logout / Bottom Section -->
    <div class="p-4 border-t border-white/10">
      <button @click="handleLogout" class="flex items-center gap-3 px-4 py-3 w-full text-left text-slate-400 hover:text-red-400 hover:bg-red-400/10 rounded-xl transition-all duration-200">
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
        </svg>
        <span class="font-medium">Logout</span>
      </button>
    </div>
  </aside>
</template>
