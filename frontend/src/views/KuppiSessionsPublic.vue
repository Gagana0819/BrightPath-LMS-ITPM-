<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Recommendation carousel
const vidScrollRef = ref(null)
const vidCanScrollLeft = ref(false)
const vidCanScrollRight = ref(true)

const recommendedVideos = ref([
  { id: 'v1', title: 'OOP Past Paper Walkthrough — 2024 Final', tutor: 'Kasun Bandara', duration: '1h 20min', views: '2.3k', tag: 'Most Watched', gradient: 'from-[#4A90E2] to-indigo-500' },
  { id: 'v2', title: 'SQL Joins & Subqueries — Exam Revision', tutor: 'Nimesha Perera', duration: '45min', views: '1.8k', tag: 'Top Rated', gradient: 'from-emerald-500 to-teal-500' },
  { id: 'v3', title: 'React Hooks Deep Dive — Live Coding', tutor: 'Malithi Fernando', duration: '1h 05min', views: '1.5k', tag: 'Trending', gradient: 'from-violet-500 to-purple-500' },
  { id: 'v4', title: 'Network Security — Firewall Config Demo', tutor: 'Tharindu Silva', duration: '55min', views: '980', tag: 'New', gradient: 'from-red-500 to-rose-500' },
  { id: 'v5', title: 'Spring Boot Microservices Architecture', tutor: 'Sandun Dimantha', duration: '1h 30min', views: '3.1k', tag: 'Popular', gradient: 'from-amber-500 to-orange-500' },
  { id: 'v6', title: 'Machine Learning — Neural Networks Intro', tutor: 'Amaya Jayasinghe', duration: '1h 10min', views: '2.0k', tag: 'AI Trending', gradient: 'from-cyan-500 to-sky-500' },
])

const updateVidScroll = () => {
  const el = vidScrollRef.value
  if (!el) return
  vidCanScrollLeft.value = el.scrollLeft > 10
  vidCanScrollRight.value = el.scrollLeft < el.scrollWidth - el.clientWidth - 10
}

const scrollVid = (dir) => {
  const el = vidScrollRef.value
  if (!el) return
  el.scrollBy({ left: dir === 'left' ? -320 : 320, behavior: 'smooth' })
  setTimeout(updateVidScroll, 350)
}

const upcomingSessions = [
  { id: 1, title: 'Object Oriented Programming — Past Papers', tutor: 'Kasun Bandara', year: 'Year 4', date: 'Oct 25, 2026', time: '6:00 PM', students: '45k', stream: 'Information Technology', tags: ['OOP', 'Past Papers', 'Coding', 'Java'], thumbnail: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=800&auto=format&fit=crop', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Kasun' },
  { id: 2, title: 'Database Optimization Techniques', tutor: 'Nimesha Perera', year: 'Year 3', date: 'Oct 27, 2026', time: '4:00 PM', students: '32k', stream: 'Software Engineering', tags: ['SQL', 'Performance', 'Database', 'Indexing'], thumbnail: '/database-ai-thumbnail.png', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Nimesha' },
  { id: 3, title: 'React Context API Deep Dive', tutor: 'Malithi Fernando', year: 'Year 3', date: 'Oct 28, 2026', time: '5:30 PM', students: '28k', stream: 'Information Technology', tags: ['React', 'Hooks', 'WebDev', 'Frontend'], thumbnail: 'https://images.unsplash.com/photo-1633356122544-f134324a6cee?q=80&w=800&auto=format&fit=crop', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Malithi' },
  { id: 4, title: 'Network Security Fundamentals', tutor: 'Tharindu Silva', year: 'Year 4', date: 'Oct 30, 2026', time: '7:00 PM', students: '19k', stream: 'Cyber Security', tags: ['Network', 'Security', 'Cyber', 'Privacy'], thumbnail: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=800&auto=format&fit=crop', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Tharindu' },
  { id: 5, title: 'Spring Boot Microservices', tutor: 'Sandun Dimantha', year: 'Year 3', date: 'Nov 01, 2026', time: '6:00 PM', students: '55k', stream: 'Software Engineering', tags: ['Java', 'Spring', 'Microservices', 'Backend'], thumbnail: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=800&auto=format&fit=crop', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Sandun' },
  { id: 6, title: 'Machine Learning with Python', tutor: 'Amaya Jayasinghe', year: 'Year 4', date: 'Nov 03, 2026', time: '4:30 PM', students: '38k', stream: 'Data Science', tags: ['ML', 'Python', 'AI', 'DataScience'], thumbnail: '/ml-ai-thumbnail.png', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Amaya' },
]

const selectedFilter = ref('All')
const searchQuery = ref('')
const filters = ['All', 'Information Technology', 'Software Engineering', 'Cyber Security', 'Data Science']

const filteredSessions = ref(upcomingSessions)

const runFilter = () => {
  let results = upcomingSessions

  // Stream filter
  if (selectedFilter.value !== 'All') {
    results = results.filter(s => s.stream === selectedFilter.value)
  }

  // Search filter
  const q = searchQuery.value.toLowerCase().trim()
  if (q) {
    results = results.filter(s =>
      s.title.toLowerCase().includes(q) ||
      s.tutor.toLowerCase().includes(q) ||
      (s.tags && s.tags.some(t => t.toLowerCase().includes(q)))
    )
  }

  filteredSessions.value = results
}

// Automatically re-run filter whenever search query or selected filter changes
watch([searchQuery, selectedFilter], () => {
  runFilter()
}, { immediate: true })

const applyFilter = (filter) => {
  selectedFilter.value = filter
}

const onSearch = () => {
  runFilter()
}

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

<template>  <div class="min-h-screen bg-[#F4F7F9] font-sans pt-[90px] pb-16 relative overflow-hidden kuppi-public">
    <!-- Global Decorative Backgrounds -->
    <div class="absolute inset-0 w-full h-full z-0 opacity-30 fixed pointer-events-none">
      <img src="/hero BG.png" class="w-full h-full object-cover" />
    </div>
    <div class="absolute top-0 left-0 w-[80%] max-w-[800px] z-0 opacity-40 mix-blend-multiply pointer-events-none -translate-y-1/3 -translate-x-1/4 fixed">
      <img src="/BG asset.png" class="w-full h-auto" />
    </div>

    <!-- Main Content -->
    <main class="relative z-10">
      
      <!-- Hero Banner -->
      <div class="max-w-[1200px] mx-auto px-4 mb-10 animate-fade-in-down">
        <div class="relative bg-gradient-to-br from-[#2C3E50] via-[#1a2a3a] to-[#0f1c2e] text-white py-16 px-8 md:px-12 overflow-hidden shadow-2xl rounded-3xl border border-slate-700/50">
          <div class="absolute inset-0 w-full h-full z-0 opacity-40 mix-blend-overlay">
            <img src="/hero BG.png" class="w-full h-full object-cover" />
          </div>
          <!-- Animated Orbs -->
          <div class="orb orb-1"></div>
          <div class="orb orb-2"></div>
          <div class="orb orb-3"></div>

          <div class="absolute top-1/2 right-0 -translate-y-1/2 translate-x-1/4 w-[600px] z-0 opacity-60 mix-blend-screen pointer-events-none">
            <img src="/BG asset.png" class="w-full h-auto" />
          </div>
          <div class="absolute -right-20 -top-20 w-80 h-80 bg-[#4A90E2]/30 blur-3xl rounded-full z-0"></div>
          <div class="absolute -left-10 -bottom-10 w-60 h-60 bg-[#A8E6CF]/20 blur-3xl rounded-full z-0"></div>
          
          <div class="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
            <div class="max-w-[600px] hero-text-enter">
              <div class="flex items-center gap-3 mb-5">
                <span class="bg-white/10 backdrop-blur-md border border-white/20 text-white text-[11px] font-bold px-4 py-1.5 rounded-full uppercase tracking-widest shadow-sm">Peer Tutoring</span>
                <!-- Live Pulse -->
                <span class="flex items-center gap-1.5 bg-emerald-500/20 backdrop-blur-md border border-emerald-400/30 text-emerald-300 text-[11px] font-bold px-3 py-1.5 rounded-full shadow-sm">
                  <span class="relative flex h-2 w-2">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-400"></span>
                  </span>
                  Live Now
                </span>
              </div>
              <h1 class="text-4xl md:text-[3.5rem] font-extrabold tracking-tight mb-4 leading-[1.1]">
                Kuppi <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#8fd4b8] to-[#63B3ED]">Sessions</span> 💡
              </h1>
              <p class="text-slate-300 text-lg max-w-[520px] leading-relaxed">
                Learn from your peers! Join live student-led tutoring sessions, discuss past papers, and ace your exams together.
              </p>
            </div>
            
            <!-- Stats Cards -->
            <div class="flex gap-4 hero-stats-enter shrink-0">
              <div class="stat-card bg-white/10 backdrop-blur-md border border-white/10 rounded-2xl p-5 text-center min-w-[120px] shadow-lg">
                <p class="text-4xl font-extrabold text-[#A8E6CF]">{{ upcomingSessions.length }}</p>
                <p class="text-slate-300 text-[13px] font-medium mt-1">Sessions Available</p>
              </div>
              <div class="stat-card bg-white/10 backdrop-blur-md border border-white/10 rounded-2xl p-5 text-center min-w-[120px] shadow-lg hidden sm:block">
                <p class="text-4xl font-extrabold text-[#4A90E2]">217</p>
                <p class="text-slate-300 text-[13px] font-medium mt-1">Students Joined</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- BrightPath Recommend for You -->
      <div class="max-w-[1200px] mx-auto px-4 mb-10 animate-fade-in-up delay-100">
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-[#4A90E2] to-[#A8E6CF] flex items-center justify-center shadow-md">
              <svg class="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <div>
              <h2 class="text-xl font-extrabold text-[#2C3E50] tracking-tight">BrightPath Recommend for You</h2>
              <p class="text-xs text-slate-400 font-medium">Personalized session recommendations based on your interests</p>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <button @click="scrollVid('left')" :disabled="!vidCanScrollLeft" class="w-9 h-9 rounded-full border border-slate-200 bg-white flex items-center justify-center text-slate-400 hover:text-[#4A90E2] hover:border-[#4A90E2] transition-all disabled:opacity-30 disabled:cursor-not-allowed shadow-sm">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
            </button>
            <button @click="scrollVid('right')" :disabled="!vidCanScrollRight" class="w-9 h-9 rounded-full border border-slate-200 bg-white flex items-center justify-center text-slate-400 hover:text-[#4A90E2] hover:border-[#4A90E2] transition-all disabled:opacity-30 disabled:cursor-not-allowed shadow-sm">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" /></svg>
            </button>
          </div>
        </div>

        <div ref="vidScrollRef" @scroll="updateVidScroll" class="flex gap-5 overflow-x-auto pb-4 scroll-smooth vid-scroll-hide">
          <div
            v-for="vid in recommendedVideos"
            :key="vid.id"
            class="min-w-[280px] max-w-[280px] bg-white rounded-2xl border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-pointer group overflow-hidden flex flex-col shrink-0"
          >
            <!-- Video Thumbnail -->
            <div class="relative h-[160px] overflow-hidden">
              <div :class="'absolute inset-0 bg-gradient-to-br ' + vid.gradient + ' opacity-90'"></div>
              <!-- Play button overlay -->
              <div class="absolute inset-0 flex items-center justify-center">
                <div class="w-16 h-16 rounded-full bg-white/20 backdrop-blur-sm border-2 border-white/40 flex items-center justify-center group-hover:scale-110 group-hover:bg-white/30 transition-all duration-300 shadow-lg">
                  <svg class="w-7 h-7 text-white ml-1" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z"/>
                  </svg>
                </div>
              </div>
              <!-- Tag badge -->
              <span class="absolute top-3 left-3 bg-black/30 backdrop-blur-md text-white text-[10px] font-bold px-2.5 py-1 rounded-lg border border-white/10">{{ vid.tag }}</span>
              <!-- Duration badge -->
              <span class="absolute bottom-3 right-3 bg-black/50 backdrop-blur-sm text-white text-[10px] font-bold px-2.5 py-1 rounded-lg flex items-center gap-1">
                <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3" /></svg>
                {{ vid.duration }}
              </span>
            </div>
            <!-- Content -->
            <div class="p-4 flex flex-col flex-1">
              <h4 class="text-[14px] font-bold text-[#2C3E50] leading-snug mb-3 line-clamp-2 group-hover:text-[#4A90E2] transition-colors">{{ vid.title }}</h4>
              <div class="mt-auto flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <div class="w-7 h-7 rounded-full bg-gradient-to-br from-[#4A90E2]/20 to-indigo-100 flex items-center justify-center text-[#4A90E2] text-[10px] font-bold border border-[#4A90E2]/20">{{ vid.tutor.split(' ').map(n => n[0]).join('') }}</div>
                  <span class="text-xs text-slate-500 font-semibold">{{ vid.tutor }}</span>
                </div>
                <span class="text-[10px] text-slate-400 font-bold flex items-center gap-1">
                  <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" /></svg>
                  {{ vid.views }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

    <div class="max-w-[1200px] mx-auto px-4 mt-8">
      
      <!-- Premium Integrated Search & Filter Control -->
      <div class="mb-10 bg-white/60 backdrop-blur-xl rounded-[32px] p-2 border border-white/80 shadow-[0_8px_32px_rgba(31,38,135,0.07)] animate-fade-in-up delay-200 relative z-30">
        <div class="flex flex-col lg:flex-row items-center gap-2">
          
          <!-- Search Input Section -->
          <div class="relative flex-1 w-full">
            <!-- Icon container with pointer-events-none to allow clicks through to input -->
            <div class="absolute left-6 top-1/2 -translate-y-1/2 flex items-center gap-3 text-[#4A90E2] pointer-events-none z-10">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              <div class="h-4 w-[1px] bg-slate-200"></div>
            </div>
            <input
              v-model="searchQuery"
              @input="onSearch"
              type="text"
              placeholder="Search by session title, tutor name, or topic..."
              class="relative z-0 w-full pl-16 pr-6 py-5 bg-transparent border-none outline-none text-[#2C3E50] font-semibold placeholder:text-slate-400 placeholder:font-medium text-base rounded-[24px]"
            />
          </div>

          <!-- Divider for Desktop -->
          <div class="hidden lg:block w-[1px] h-10 bg-slate-200/60 mx-2"></div>

          <!-- Filter Pills Section (Inline) -->
          <div class="w-full lg:w-auto overflow-x-auto scrollbar-hide px-4 lg:px-2 py-3 lg:py-0">
            <div class="flex items-center gap-2 min-w-max">
              <button 
                v-for="filter in filters"
                :key="filter"
                @click="applyFilter(filter)"
                class="px-5 py-2.5 rounded-[18px] text-[13px] font-bold border transition-all duration-300 whitespace-nowrap"
                :class="selectedFilter === filter 
                  ? 'bg-[#4A90E2] text-white border-[#4A90E2] shadow-lg shadow-blue-200 translate-y-[-1px]' 
                  : 'bg-white/50 text-[#64748B] border-slate-200/60 hover:border-[#4A90E2]/40 hover:text-[#4A90E2] hover:bg-white'"
              >
                {{ filter }}
              </button>
            </div>
          </div>

        </div>
      </div>

      <transition-group name="list" tag="div" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-4 gap-y-10 animate-fade-in-up delay-200 relative">
        <div 
          v-for="(session, index) in filteredSessions" 
          :key="session.id"
          class="video-card flex flex-col cursor-pointer group fade-up"
          :style="{ animationDelay: (0.3 + index * 0.08) + 's' }"
          @click="joinSession(session)"
        >
          <!-- Thumbnail Container -->
          <div class="relative aspect-video rounded-xl overflow-hidden mb-3 shadow-sm group-hover:shadow-md transition-shadow duration-300 bg-slate-200">
            <img 
              :src="session.thumbnail" 
              :alt="session.title" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              @error="(e) => e.target.src = 'https://picsum.photos/seed/error/800/450'"
            />
            
            <!-- Play Button Overlay -->
            <div class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
              <div class="w-12 h-12 bg-white/90 rounded-full flex items-center justify-center shadow-lg transform scale-90 group-hover:scale-100 transition-transform duration-300">
                <svg class="w-6 h-6 text-[#4A90E2] ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg>
              </div>
            </div>

            <!-- Badges -->
            <div class="absolute inset-0 p-2 flex flex-col justify-between pointer-events-none">
              <div class="flex justify-start">
                <span class="bg-[#4A90E2] text-white text-[10px] font-bold px-2 py-0.5 rounded shadow-sm opacity-90">
                  {{ session.stream }}
                </span>
              </div>
              <div class="flex justify-end">
                <span class="bg-red-600 text-white text-[10px] font-bold px-1.5 py-0.5 rounded shadow uppercase tracking-tighter">
                  Live
                </span>
              </div>
            </div>
          </div>
          
          <!-- Content Section -->
          <div class="flex gap-3 px-1">
            <!-- Tutor Avatar -->
            <div class="shrink-0 pt-0.5">
              <div class="w-9 h-9 rounded-full overflow-hidden border border-slate-100 shadow-sm group-hover:border-[#4A90E2]/30 transition-colors duration-300">
                <img :src="session.avatar" class="w-full h-full object-cover" />
              </div>
            </div>

            <!-- Info -->
            <div class="flex flex-col min-w-0">
              <h3 class="font-bold text-[#2C3E50] text-[15px] leading-snug mb-1 line-clamp-2 transition-colors duration-300 group-hover:text-[#4A90E2]">
                {{ session.title }}
              </h3>
              
              <div class="flex flex-col gap-0.5">
                <p class="text-[13px] text-slate-500 font-medium hover:text-[#2C3E50] transition-colors truncate">
                  {{ session.tutor }}
                </p>
                <div class="flex items-center text-[12px] text-slate-400 font-medium">
                  <span>{{ session.students }} views</span>
                  <span class="mx-1">•</span>
                  <span>{{ session.date }}</span>
                </div>
              </div>

              <!-- Tags (YouTube style subtle) -->
              <div class="flex flex-wrap gap-1 mt-2">
                <span v-for="tag in session.tags" :key="tag" class="text-[11px] text-[#4A90E2] font-semibold hover:underline">
                  #{{ tag }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </transition-group>

      <!-- Beautiful Empty State for No Filter Results -->
      <div v-if="filteredSessions.length === 0" class="mt-12 bg-white/60 backdrop-blur-md rounded-[32px] p-20 border border-white/80 shadow-sm text-center animate-pulse-slow">
        <div class="w-24 h-24 bg-blue-50 rounded-full flex items-center justify-center text-5xl mx-auto mb-6 shadow-inner">🔍</div>
        <h3 class="text-2xl font-extrabold text-[#2C3E50] mb-2 tracking-tight">No sessions found for "{{ searchQuery }}"</h3>
        <p class="text-slate-500 font-medium text-lg">Try adjusting your keywords or switching filters to find what you're looking for!</p>
        <button @click="searchQuery = ''; selectedFilter = 'All'" class="mt-8 bg-[#4A90E2] hover:bg-blue-600 text-white font-bold py-3 px-8 rounded-2xl transition-all shadow-md active:scale-95">Clear Filters</button>
      </div>

      <!-- No Results -->
      <div v-if="filteredSessions.length === 0" class="text-center py-16 fade-up">
        <div class="text-5xl mb-4">🔍</div>
        <h3 class="text-[#2C3E50] font-bold text-lg mb-2">No sessions found</h3>
        <p class="text-slate-400 text-[14px]">Try adjusting your search or filter to find sessions.</p>
      </div>

      <!-- CTA Banner -->
      <div class="mt-14 cta-banner bg-gradient-to-r from-[#2C3E50] via-[#34495e] to-[#2C3E50] rounded-[24px] p-10 flex flex-col md:flex-row items-center justify-between gap-8 border border-slate-600/30 relative overflow-hidden animate-fade-in-up delay-300">
        <div class="absolute -right-10 -top-10 w-40 h-40 bg-yellow-500/15 blur-2xl rounded-full"></div>
        <div class="absolute -left-10 -bottom-10 w-36 h-36 bg-[#4A90E2]/10 blur-2xl rounded-full"></div>
        <div class="relative z-10">
          <h3 class="text-white text-2xl font-extrabold mb-2">Want to become a Peer Tutor? 🏆</h3>
          <p class="text-slate-300 text-[14px] max-w-[420px] leading-relaxed">Register as a student and opt-in as a Kuppi Teacher to schedule your own sessions and help your batchmates excel.</p>
        </div>
        <RouterLink to="/register" class="cta-btn bg-[#A8E6CF] hover:bg-[#8fd4b8] text-[#2C3E50] font-bold py-3.5 px-10 rounded-2xl text-[15px] transition-all duration-300 shadow-lg hover:shadow-[0_6px_20px_rgba(168,230,207,0.4)] relative z-10 whitespace-nowrap hover:scale-105">
          Register Now →
        </RouterLink>
      </div>
    </div>
    </main>
  </div>
</template>

<style scoped>
/* Page Load Animations */
@keyframes fadeInDown {
  0% { opacity: 0; transform: translateY(-30px); }
  100% { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(30px); }
  100% { opacity: 1; transform: translateY(0); }
}

.animate-fade-in-down {
  animation: fadeInDown 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.animate-fade-in-up {
  opacity: 0;
  animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.delay-100 { animation-delay: 100ms; }
.delay-200 { animation-delay: 200ms; }
.delay-300 { animation-delay: 300ms; }

/* Grid Transition Group */
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px) scale(0.95);
}
.list-leave-active {
  position: absolute;
}

/* Animated Background Orbs */
.orb {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
}
.orb-1 {
  width: 350px; height: 350px;
  top: -80px; right: -60px;
  background: radial-gradient(circle, rgba(74,144,226,0.25) 0%, transparent 70%);
  animation: float 8s ease-in-out infinite;
}
.orb-2 {
  width: 250px; height: 250px;
  bottom: -50px; left: -30px;
  background: radial-gradient(circle, rgba(168,230,207,0.2) 0%, transparent 70%);
  animation: float 10s ease-in-out infinite reverse;
}
.orb-3 {
  width: 150px; height: 150px;
  top: 40%; left: 50%;
  background: radial-gradient(circle, rgba(99,179,237,0.12) 0%, transparent 70%);
  animation: float 6s ease-in-out infinite 2s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-25px) scale(1.05); }
}

/* Hero Text Enter */
.hero-text-enter {
  animation: slideUp 0.7s ease-out both;
}
.hero-stats-enter {
  animation: slideUp 0.7s ease-out 0.3s both;
}

/* Fade Up Animation for Grid Items */
.fade-up {
  animation: fadeUp 0.5s ease-out both;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px);}
  to { opacity: 1; transform: translateY(0);}
}
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Video Card Effects */
.video-card {
  transition: all 0.3s ease;
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Hero Section Refinement */
.orb-1 {
  background: radial-gradient(circle, rgba(74,144,226,0.15) 0%, transparent 70%);
}

/* Hide scrollbar for recommendation carousel */
.vid-scroll-hide::-webkit-scrollbar { display: none; }
.vid-scroll-hide { -ms-overflow-style: none; scrollbar-width: none; }
</style>
