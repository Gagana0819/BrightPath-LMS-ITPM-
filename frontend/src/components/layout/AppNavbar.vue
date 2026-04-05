<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'

import { useNotificationStore } from '@/stores/notificationStore'

const router = useRouter()
const route = useRoute()
const notificationStore = useNotificationStore()

const isLoggedIn = ref(false)
const showNotifications = ref(false)

// User state
const userName = ref('STUDENT')
const userInitials = ref('ST')

const unreadNotifications = computed(() => notificationStore.unreadNotifications)
const notificationCount = computed(() => notificationStore.unreadCount)

const timeAgo = (dateStr) => {
  const date = new Date(dateStr)
  const now = new Date()
  const seconds = Math.floor((now - date) / 1000)
  
  if (seconds < 60) return 'Just now'
  const minutes = Math.floor(seconds / 60)
  if (minutes < 60) return `${minutes}m ago`
  const hours = Math.floor(minutes / 60)
  if (hours < 24) return `${hours}h ago`
  const days = Math.floor(hours / 24)
  return `${days}d ago`
}

const updateAuthState = () => {
  const token = localStorage.getItem('access_token')
  isLoggedIn.value = !!token
  
  if (token) {
    const fName = localStorage.getItem('first_name')
    const lName = localStorage.getItem('last_name')
    const fullName = localStorage.getItem('full_name') // backend stores this
    const studentId = localStorage.getItem('student_id') || ''
    
    if (fullName) {
      userName.value = `${studentId ? studentId + ' ' : ''}${fullName}`.toUpperCase()
      const parts = fullName.split(' ')
      userInitials.value = parts.length > 1 
        ? `${parts[0].charAt(0)}${parts[1].charAt(0)}`.toUpperCase() 
        : fullName.substring(0, 2).toUpperCase()
    } else if (fName && lName) {
      userName.value = `${studentId ? studentId + ' ' : ''}${fName} ${lName}`.toUpperCase()
      userInitials.value = `${fName.charAt(0)}${lName.charAt(0)}`.toUpperCase()
    }
  }
}

onMounted(() => {
  updateAuthState()
  document.addEventListener('click', closeDropdowns)
  
  if (isLoggedIn.value) {
    notificationStore.startPolling()
  }
})

watch(isLoggedIn, (newVal) => {
  if (newVal) notificationStore.startPolling()
  else notificationStore.stopPolling()
})

watch(() => route.path, updateAuthState)

onUnmounted(() => {
  document.removeEventListener('click', closeDropdowns)
})

const logoTarget = computed(() => isLoggedIn.value ? '/dashboard' : '/')

const toggleNotifications = (e) => {
  e.stopPropagation()
  showNotifications.value = !showNotifications.value
}

const closeDropdowns = () => {
  showNotifications.value = false
}

const navigateToProfile = () => {
  router.push('/dashboard/profile')
}
</script>

<template>
  <header class="fixed top-0 left-0 w-full z-50 transition-all duration-300 bg-white/80 backdrop-blur-md border-b border-slate-200/50 shadow-sm px-4 lg:px-20">
    <div class="max-w-[1600px] mx-auto relative flex justify-between items-center h-[72px]">
      
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

      <!-- Action Buttons / User Menu -->
      <div class="hidden md:flex z-20 items-center gap-6 flex-shrink-0">
        <template v-if="!isLoggedIn">
          <RouterLink to="/login" class="font-semibold text-[0.95rem] text-[#2C3E50] hover:text-[#4A90E2] transition-colors">
            Log In
          </RouterLink>
          <RouterLink to="/register" class="inline-flex items-center justify-center px-6 py-2.5 rounded text-[0.95rem] font-bold text-white bg-[#4A90E2] hover:bg-[#3A7BC8] transition-all shadow-sm flex-shrink-0">
            Join for Free
          </RouterLink>
        </template>

        <template v-else>
          <div class="flex items-center gap-5">
            <!-- Notifications -->
            <div class="relative">
              <button 
                @click="toggleNotifications" 
                class="relative w-11 h-11 bg-[#2C3E50] hover:bg-[#1a252f] text-white rounded-full flex items-center justify-center transition-colors focus:outline-none focus:ring-2 focus:ring-[#4A90E2]/30 focus:ring-offset-2"
                aria-label="Notifications"
              >
                <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                </svg>
                <!-- Badge -->
                <span class="absolute -top-1.5 -right-2 bg-[#EF4444] text-white text-[10px] font-bold px-1.5 py-0.5 rounded-md border-2 border-white min-w-[24px]">
                  {{ notificationCount }}
                </span>
              </button>

              <!-- Notifications Dropdown -->
              <transition
                enter-active-class="transition ease-out duration-200"
                enter-from-class="opacity-0 translate-y-1 scale-95"
                enter-to-class="opacity-100 translate-y-0 scale-100"
                leave-active-class="transition ease-in duration-150"
                leave-from-class="opacity-100 translate-y-0 scale-100"
                leave-to-class="opacity-0 translate-y-1 scale-95"
              >
                <div v-if="showNotifications" class="absolute right-0 mt-3 w-80 bg-white rounded-2xl shadow-2xl border border-slate-100 overflow-hidden z-[100]" @click.stop>
                  <div class="p-4 border-b border-slate-100 bg-[#F4F7F9] flex justify-between items-center">
                    <h3 class="font-bold text-[#2C3E50]">Notifications</h3>
                    <button 
                      @click="notificationStore.markAllRead"
                      class="text-xs font-semibold text-[#4A90E2] hover:underline"
                    >
                      Mark all read
                    </button>
                  </div>
                  <div class="max-h-[320px] overflow-y-auto">
                    <div v-if="notificationStore.notifications.length === 0" class="p-8 text-center text-slate-400">
                      <p class="text-sm">No notifications yet.</p>
                    </div>
                    <div 
                      v-for="notif in notificationStore.notifications" 
                      :key="notif.id"
                      @click="notificationStore.markAsRead(notif.id)"
                      class="p-4 border-b border-slate-100 transition-colors cursor-pointer flex gap-3"
                      :class="notif.is_read ? 'bg-white' : 'bg-[#F4F7F9]/60 hover:bg-[#F4F7F9]'"
                    >
                      <div 
                        class="w-2 h-2 rounded-full mt-1.5 shrink-0 transition-colors"
                        :class="notif.is_read ? 'bg-slate-200' : 'bg-[#4A90E2]'"
                      ></div>
                      <div>
                        <p class="text-sm font-semibold text-[#2C3E50] leading-tight mb-1">{{ notif.title }}</p>
                        <p class="text-xs text-[#2C3E50]/70 mb-1.5">{{ notif.message }}</p>
                        <p class="text-[10px] font-medium text-[#4A90E2]">{{ timeAgo(notif.created_at) }}</p>
                      </div>
                    </div>
                  </div>
                  <div class="p-3 text-center border-t border-slate-100 bg-[#F4F7F9] hover:bg-slate-100 cursor-pointer transition-colors">
                    <span class="text-xs font-bold text-[#2C3E50]">View all notifications</span>
                  </div>
                </div>
              </transition>
            </div>

            <!-- Profile Area -->
            <div 
              class="flex items-center gap-3 cursor-pointer group px-2 py-1.5 rounded-xl hover:bg-[#F4F7F9] transition-colors border border-transparent hover:border-slate-100"
              @click="navigateToProfile"
              title="Go to Profile Dashboard"
            >
              <!-- Name & Dropdown icon -->
              <div class="flex items-center gap-1">
                <span class="text-[0.95rem] font-bold text-[#2C3E50] group-hover:text-[#4A90E2] transition-colors tracking-tight">
                  {{ userName }}
                </span>
                <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" class="text-slate-400 group-hover:text-[#4A90E2] transition-transform group-hover:translate-y-0.5">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </div>

              <!-- Avatar -->
              <div class="w-12 h-12 rounded-full bg-[#F4F7F9] flex items-center justify-center font-extrabold text-[#2C3E50] text-xl tracking-wider shadow-sm border border-slate-200 group-hover:border-[#4A90E2] transition-all group-hover:shadow-md group-hover:text-[#4A90E2]">
                {{ userInitials }}
              </div>
            </div>

          </div>
        </template>
      </div>
      
    </div>
  </header>
</template>
