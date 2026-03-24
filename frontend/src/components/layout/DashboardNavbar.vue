<script setup>
import { ref, computed } from 'vue'

const fullName = computed(() => localStorage.getItem('full_name') || 'User')
const userRole = computed(() => localStorage.getItem('user_role') || 'STUDENT')
const studentId = computed(() => localStorage.getItem('student_id') || 'STUDENT-XXX')

// Mock notifications consistency
const unreadCount = ref(2)
const isNotificationsOpen = ref(false)
const notifications = ref([
  { id: 1, title: 'New Student Joined', message: 'Malithi Perera just joined your OOP session.', time: '2 min ago', type: 'user' },
  { id: 2, title: 'Resource Downloaded', message: 'Your "SQL Joins" PDF was downloaded 15 times.', time: '1 hour ago', type: 'file' }
])

const toggleNotifications = () => {
  isNotificationsOpen.value = !isNotificationsOpen.value
}
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
    </div>

    <!-- Right Actions -->
    <div class="flex items-center gap-2 md:gap-4">
      
      <!-- Notification Bell -->
      <div class="relative">
        <button @click="toggleNotifications" class="relative p-2.5 rounded-full text-content hover:bg-black/5 transition-colors group">
          <svg class="w-6 h-6 group-hover:text-hero-highlight transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
          </svg>
          <span v-if="unreadCount > 0" class="absolute top-[6px] right-[8px] w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white shadow-sm"></span>
        </button>

        <!-- Notification Dropdown -->
        <div v-if="isNotificationsOpen" class="absolute right-0 mt-3 w-80 bg-white rounded-[24px] shadow-2xl border border-slate-100 py-4 animate-in fade-in zoom-in-95 duration-200 z-50">
          <div class="px-6 pb-3 border-b border-slate-50 flex justify-between items-center">
            <h3 class="font-extrabold text-[#1E293B] text-sm italic">Recent Activity</h3>
            <span class="text-[10px] bg-blue-50 text-blue-600 px-2 py-0.5 rounded-full font-bold">New</span>
          </div>
          <div class="max-h-[300px] overflow-y-auto">
            <div v-for="n in notifications" :key="n.id" class="px-6 py-4 hover:bg-slate-50 transition-colors cursor-pointer border-b border-slate-50 last:border-none">
              <div class="flex gap-3">
                <div class="w-8 h-8 rounded-lg bg-blue-50 flex items-center justify-center text-blue-600 text-xs">
                  {{ n.type === 'user' ? '👤' : '📄' }}
                </div>
                <div>
                  <h4 class="text-[13px] font-bold text-slate-800">{{ n.title }}</h4>
                  <p class="text-[11px] text-slate-500 mt-0.5 leading-relaxed">{{ n.message }}</p>
                  <span class="text-[10px] text-slate-400 font-medium mt-1 block">{{ n.time }}</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 pt-3 mt-1 text-center">
            <button class="text-xs font-bold text-blue-600 hover:underline">View All Notifications</button>
          </div>
        </div>
      </div>

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
