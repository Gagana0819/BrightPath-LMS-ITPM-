<script setup>
import { ref, computed } from 'vue'

const fullName = computed(() => localStorage.getItem('full_name') || 'User')
const userRole = computed(() => localStorage.getItem('user_role') || 'STUDENT')
const studentId = computed(() => localStorage.getItem('student_id') || 'STUDENT-XXX')

// Mock notifications consistency
const unreadCount = ref(2) // Consistent with AppNavbar's unread items
</script>

<template>
  <header class="h-[80px] bg-white border-b border-[#e2e8f0] px-4 md:px-8 flex items-center justify-between z-10 shrink-0">
    
    <!-- Mobile Hamburger and Page Title -->
    <div class="flex items-center gap-4">
      <button class="md:hidden p-2 -ml-2 text-content hover:bg-black/5 rounded-lg">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>
      
      <!-- Search Input (Optional) -->
      <div class="hidden md:flex items-center bg-base rounded-full px-4 py-2 border border-slate-200 focus-within:ring-2 focus-within:ring-hero-highlight/20 focus-within:border-hero-highlight w-[300px] transition-all">
        <svg class="w-4 h-4 text-slate-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
        <input type="text" placeholder="Search courses, library..." class="bg-transparent border-none outline-none w-full text-sm text-content placeholder:text-slate-400" />
      </div>
    </div>

    <!-- Right Actions -->
    <div class="flex items-center gap-2 md:gap-4">
      
      <!-- Notification Bell -->
      <button class="relative p-2.5 rounded-full text-content hover:bg-black/5 transition-colors group">
        <svg class="w-6 h-6 group-hover:text-hero-highlight transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
        </svg>
        <span v-if="unreadCount > 0" class="absolute top-[6px] right-[8px] w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white shadow-sm"></span>
      </button>

      <!-- Divider -->
      <div class="h-8 w-px bg-slate-200 hidden md:block mx-1"></div>

      <!-- Profile Avatar -->
      <button class="flex items-center gap-3 p-1 pr-3 rounded-full hover:bg-black/5 transition-colors border border-transparent hover:border-slate-200">
        <img 
          :src="'https://api.dicebear.com/7.x/notionists/svg?seed=' + fullName + '&backgroundColor=e4f8f6'" 
          alt="User Avatar" 
          class="w-10 h-10 rounded-full bg-slate-100 object-cover border border-slate-200"
        />
        <div class="hidden md:flex flex-col items-start leading-tight">
          <span class="text-sm font-semibold text-content block">{{ fullName }}</span>
          <span class="text-xs text-slate-500 font-medium tracking-wide">{{ userRole }}</span>
        </div>
        <svg class="w-4 h-4 text-slate-400 hidden md:block ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
        </svg>
      </button>
    </div>
    
  </header>
</template>
