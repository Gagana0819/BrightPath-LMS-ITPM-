<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useContentStore } from '@/stores/contentStore'

const router = useRouter()
const contentStore = useContentStore()

const isLoggedIn = computed(() => !!localStorage.getItem('access_token'))

const joinSession = (session) => {
  const isLoggedIn = !!localStorage.getItem('access_token')
  const targetPath = `/dashboard/kuppi/play/${session.id}`
  
  if (isLoggedIn) {
    router.push(targetPath)
  } else {
    router.push({ path: '/login', query: { redirect: targetPath } })
  }
}
</script>

<template>
  <section v-if="isLoggedIn && contentStore.recommendedSessions.length > 0" class="py-24 bg-white relative overflow-hidden px-4 sm:px-8 lg:px-20">
    <div class="max-w-[1200px] mx-auto w-full z-10 relative">
      
      <!-- Header -->
      <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
        <div class="space-y-4">
          <div class="inline-flex items-center gap-2 px-3 py-1 bg-indigo-600/10 text-indigo-600 rounded-full text-[10px] font-black uppercase tracking-widest border border-indigo-600/20">
            Interactive Learning
          </div>
          <h2 class="text-3xl md:text-5xl font-black text-[#2C3E50] tracking-tighter">Live <span class="text-indigo-600">Kuppi</span> Sessions</h2>
          <p class="text-slate-500 font-medium text-lg max-w-[600px] leading-relaxed">
            Join student-led discussions and deep-dives happening now or starting soon in your faculty.
          </p>
        </div>
        <router-link to="/sessions" class="group relative px-6 py-3 bg-slate-900 text-white rounded-xl font-bold text-sm shadow-xl transition-all hover:shadow-indigo-200 hover:-translate-y-1 flex items-center gap-2 overflow-hidden">
          <span class="relative z-10 flex items-center gap-2">
            View All Sessions 
            <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </span>
        </router-link>
      </div>

      <!-- Sessions Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div 
          v-for="session in contentStore.recommendedSessions.slice(0, 3)" 
          :key="session.id"
          class="group bg-white rounded-[2rem] border border-slate-100 shadow-sm hover:shadow-2xl transition-all duration-500 overflow-hidden flex flex-col"
        >
          <!-- Thumbnail Area -->
          <div class="relative aspect-video overflow-hidden">
            <img :src="session.thumbnail || '/hqdefault.jpg'" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-transparent to-transparent"></div>
            
            <!-- Badges -->
            <div class="absolute top-4 left-4 flex flex-col gap-2">
              <span v-if="session.is_live" class="px-3 py-1 bg-red-600 text-white text-[10px] font-black rounded-lg shadow-lg animate-pulse">LIVE NOW</span>
              <span class="px-3 py-1 bg-white/20 backdrop-blur-md text-white text-[10px] font-bold border border-white/30 rounded-lg">{{ session.stream }}</span>
            </div>

            <!-- Join Overlay -->
            <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-slate-900/40 backdrop-blur-[2px]">
               <button @click="joinSession(session)" class="bg-white text-slate-900 px-6 py-2.5 rounded-xl font-black text-xs uppercase tracking-widest shadow-2xl hover:scale-110 active:scale-95 transition-all">
                 Join Session
               </button>
            </div>
          </div>

          <!-- Content -->
          <div class="p-8 flex-1 flex flex-col">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-400 font-bold overflow-hidden border border-slate-200">
                <img v-if="session.tutor_avatar" :src="session.tutor_avatar" class="w-full h-full object-cover" />
                <span v-else>{{ (session.tutor_name || 'U')[0] }}</span>
              </div>
              <div>
                <p class="text-[13px] font-bold text-slate-900 leading-none">{{ session.tutor_name }}</p>
                <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest mt-1">Peer Tutor</p>
              </div>
            </div>

            <h3 class="text-xl font-black text-[#2C3E50] mb-3 line-clamp-2 leading-snug group-hover:text-indigo-600 transition-colors">
              {{ session.title }}
            </h3>
            
            <p class="text-slate-500 text-sm font-medium line-clamp-2 mb-6">
              {{ session.description || 'No description provided.' }}
            </p>

            <div class="mt-auto pt-6 border-t border-slate-50 flex items-center justify-between text-[11px] font-black text-slate-400 uppercase tracking-widest">
              <div class="flex items-center gap-1.5">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                {{ session.scheduled_date }}
              </div>
              <div class="flex items-center gap-1.5">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                {{ session.scheduled_time }}
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>
