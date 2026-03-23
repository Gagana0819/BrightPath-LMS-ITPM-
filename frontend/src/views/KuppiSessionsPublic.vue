<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const upcomingSessions = [
  { id: 1, title: 'Object Oriented Programming — Past Papers', tutor: 'Kasun Bandara', year: 'Year 4', date: 'Oct 25, 2026', time: '6:00 PM', students: 45, stream: 'Information Technology', tags: ['OOP', 'Past Papers', 'Exam Prep'] },
  { id: 2, title: 'Database Optimization Techniques', tutor: 'Nimesha Perera', year: 'Year 3', date: 'Oct 27, 2026', time: '4:00 PM', students: 32, stream: 'Software Engineering', tags: ['SQL', 'Indexing', 'Performance'] },
  { id: 3, title: 'React Context API Deep Dive', tutor: 'Malithi Fernando', year: 'Year 3', date: 'Oct 28, 2026', time: '5:30 PM', students: 28, stream: 'Information Technology', tags: ['React', 'Hooks', 'Frontend'] },
  { id: 4, title: 'Network Security Fundamentals', tutor: 'Tharindu Silva', year: 'Year 4', date: 'Oct 30, 2026', time: '7:00 PM', students: 19, stream: 'Cyber Security', tags: ['Firewalls', 'VPN', 'Encryption'] },
  { id: 5, title: 'Spring Boot Microservices', tutor: 'Sandun Dimantha', year: 'Year 3', date: 'Nov 01, 2026', time: '6:00 PM', students: 55, stream: 'Software Engineering', tags: ['Java', 'Spring', 'REST API'] },
  { id: 6, title: 'Machine Learning with Python', tutor: 'Amaya Jayasinghe', year: 'Year 4', date: 'Nov 03, 2026', time: '4:30 PM', students: 38, stream: 'Data Science', tags: ['ML', 'Pandas', 'Scikit-Learn'] },
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
      s.tags.some(t => t.toLowerCase().includes(q))
    )
  }

  filteredSessions.value = results
}

const applyFilter = (filter) => {
  selectedFilter.value = filter
  runFilter()
}

const onSearch = () => {
  runFilter()
}

const joinSession = (session) => {
  const isLoggedIn = !!localStorage.getItem('access_token')
  if (isLoggedIn) {
    router.push('/dashboard/kuppi')
  } else {
    router.push({ path: '/login', query: { redirect: '/dashboard/kuppi' } })
  }
}
</script>

<template>
  <div class="kuppi-public min-h-screen bg-[#F4F7F9] font-sans pt-[90px] pb-16">
    
    <!-- Hero Banner -->
    <div class="relative bg-gradient-to-br from-[#2C3E50] via-[#1a2a3a] to-[#0f1c2e] text-white py-20 px-4 mb-10 overflow-hidden">
      <!-- Animated Orbs -->
      <div class="orb orb-1"></div>
      <div class="orb orb-2"></div>
      <div class="orb orb-3"></div>
      
      <div class="max-w-[1200px] mx-auto relative z-10">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-8">
          <div class="hero-text-enter">
            <div class="flex items-center gap-3 mb-5">
              <span class="bg-white/10 backdrop-blur-md border border-white/20 text-white text-[11px] font-bold px-4 py-1.5 rounded-full uppercase tracking-widest">Peer Tutoring</span>
              <!-- Live Pulse -->
              <span class="flex items-center gap-1.5 bg-emerald-500/20 backdrop-blur-md border border-emerald-400/30 text-emerald-300 text-[11px] font-bold px-3 py-1.5 rounded-full">
                <span class="relative flex h-2 w-2">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-400"></span>
                </span>
                Live Now
              </span>
            </div>
            <h1 class="text-4xl md:text-[3.5rem] font-extrabold tracking-tight mb-4 leading-[1.1]">
              Kuppi <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#4A90E2] to-[#63B3ED]">Sessions</span> 💡
            </h1>
            <p class="text-slate-300 text-lg max-w-[520px] leading-relaxed">
              Learn from your peers! Join live student-led tutoring sessions, discuss past papers, and ace your exams together.
            </p>
          </div>
          
          <!-- Stats Cards -->
          <div class="flex gap-4 hero-stats-enter">
            <div class="stat-card bg-white/10 backdrop-blur-md border border-white/10 rounded-2xl p-5 text-center min-w-[120px]">
              <p class="text-3xl font-extrabold text-[#A8E6CF]">{{ upcomingSessions.length }}</p>
              <p class="text-slate-400 text-[12px] font-medium mt-1">Sessions</p>
            </div>
            <div class="stat-card bg-white/10 backdrop-blur-md border border-white/10 rounded-2xl p-5 text-center min-w-[120px]">
              <p class="text-3xl font-extrabold text-[#4A90E2]">217</p>
              <p class="text-slate-400 text-[12px] font-medium mt-1">Students</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="max-w-[1200px] mx-auto px-4">

      <!-- Search Bar (Glassmorphism) -->
      <div class="mb-6 fade-up" style="animation-delay: 0.1s">
        <div class="relative max-w-[520px]">
          <svg class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-[#4A90E2] pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          <input
            v-model="searchQuery"
            @input="onSearch"
            type="text"
            placeholder="Search by session title, tutor, or topic..."
            class="search-input w-full pl-12 pr-4 py-4 rounded-2xl border border-slate-200 bg-white/80 backdrop-blur-sm text-[14px] text-[#2C3E50] placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-[#4A90E2]/40 focus:border-[#4A90E2] shadow-[0_2px_16px_rgba(74,144,226,0.06)] transition-all duration-300"
          />
        </div>
      </div>

      <!-- Stream Filters -->
      <div class="flex flex-wrap gap-2 mb-8 fade-up" style="animation-delay: 0.2s">
        <button 
          v-for="filter in filters"
          :key="filter"
          @click="applyFilter(filter)"
          class="filter-pill px-5 py-2.5 rounded-full text-[13px] font-bold border transition-all duration-300"
          :class="selectedFilter === filter 
            ? 'bg-[#4A90E2] text-white border-[#4A90E2] shadow-[0_4px_14px_rgba(74,144,226,0.35)] scale-[1.03]' 
            : 'bg-white text-[#2C3E50] border-slate-200 hover:border-[#4A90E2] hover:text-[#4A90E2] hover:shadow-md'"
        >
          {{ filter }}
        </button>
      </div>

      <!-- Sessions Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="(session, index) in filteredSessions" 
          :key="session.id"
          class="session-card bg-white rounded-[20px] p-6 border border-slate-200/80 shadow-sm hover:shadow-xl transition-all duration-300 group cursor-pointer relative overflow-hidden fade-up"
          :style="{ animationDelay: (0.3 + index * 0.08) + 's' }"
          @click="joinSession(session)"
        >
          <!-- Hover Gradient Glow -->
          <div class="absolute inset-0 bg-gradient-to-br from-[#4A90E2]/0 to-[#A8E6CF]/0 group-hover:from-[#4A90E2]/[0.03] group-hover:to-[#A8E6CF]/[0.05] transition-all duration-500 pointer-events-none rounded-[20px]"></div>
          
          <!-- Stream Badge -->
          <div class="flex items-center justify-between mb-4 relative z-10">
            <span class="bg-[#4A90E2]/10 text-[#4A90E2] text-[11px] font-bold px-2.5 py-1 rounded-lg border border-[#4A90E2]/10">{{ session.stream }}</span>
            <div class="flex items-center gap-1.5 text-[12px] text-slate-500 font-medium">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
              {{ session.students }} joined
            </div>
          </div>
          
          <!-- Title -->
          <h3 class="font-bold text-[#2C3E50] text-[16px] leading-tight mb-3 group-hover:text-[#4A90E2] transition-colors duration-300 relative z-10">{{ session.title }}</h3>
          
          <!-- Tutor Info -->
          <div class="flex items-center gap-3 mb-4 relative z-10">
            <div class="w-9 h-9 rounded-full bg-gradient-to-br from-[#4A90E2]/20 to-indigo-100 flex items-center justify-center text-[#4A90E2] font-bold text-[11px] border border-[#4A90E2]/20 shrink-0 group-hover:scale-110 transition-transform duration-300">
              {{ session.tutor.split(' ').map(n => n[0]).join('') }}
            </div>
            <div>
              <p class="text-[13px] font-bold text-[#2C3E50]">{{ session.tutor }}</p>
              <p class="text-[11px] text-slate-400">{{ session.year }} Student</p>
            </div>
          </div>
          
          <!-- Tags -->
          <div class="flex flex-wrap gap-1.5 mb-4 relative z-10">
            <span v-for="tag in session.tags" :key="tag" class="bg-slate-50 text-slate-600 text-[10px] font-bold px-2.5 py-1 rounded-lg border border-slate-100 flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-[#4A90E2]/40"></span>
              {{ tag }}
            </span>
          </div>
          
          <!-- Date & Join -->
          <div class="flex items-center justify-between pt-4 border-t border-slate-100 relative z-10">
            <div class="flex items-center gap-2 text-[12px] text-slate-500 font-medium">
              <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              {{ session.date }} • {{ session.time }}
            </div>
            <button class="join-btn bg-[#4A90E2] hover:bg-[#3a7bc8] text-white text-[12px] font-bold py-2 px-5 rounded-xl transition-all duration-300 shadow-sm hover:shadow-[0_4px_14px_rgba(74,144,226,0.4)] flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path></svg>
              Join
            </button>
          </div>
        </div>
      </div>

      <!-- No Results -->
      <div v-if="filteredSessions.length === 0" class="text-center py-16 fade-up">
        <div class="text-5xl mb-4">🔍</div>
        <h3 class="text-[#2C3E50] font-bold text-lg mb-2">No sessions found</h3>
        <p class="text-slate-400 text-[14px]">Try adjusting your search or filter to find sessions.</p>
      </div>

      <!-- CTA Banner -->
      <div class="mt-14 cta-banner bg-gradient-to-r from-[#2C3E50] via-[#34495e] to-[#2C3E50] rounded-[24px] p-10 flex flex-col md:flex-row items-center justify-between gap-8 border border-slate-600/30 relative overflow-hidden fade-up" style="animation-delay: 0.6s">
        <div class="absolute -right-16 -top-16 w-52 h-52 bg-yellow-500/10 blur-3xl rounded-full"></div>
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
  </div>
</template>

<style scoped>
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

/* Session Card Effects */
.session-card {
  transform: translateY(0);
  will-change: transform, box-shadow;
}
.session-card:hover {
  transform: translateY(-4px);
  border-color: rgba(74, 144, 226, 0.25);
}

/* Search Input Focus Effect */
.search-input:focus {
  box-shadow: 0 4px 20px rgba(74, 144, 226, 0.12);
  background: rgba(255,255,255, 0.95);
}

/* Filter Pill Active Micro-animation */
.filter-pill {
  will-change: transform;
}
.filter-pill:active {
  transform: scale(0.96);
}

/* Join Button Pulse on Hover */
.join-btn:hover {
  animation: subtlePulse 1.5s ease-in-out infinite;
}
@keyframes subtlePulse {
  0%, 100% { box-shadow: 0 4px 14px rgba(74,144,226,0.4); }
  50% { box-shadow: 0 4px 20px rgba(74,144,226,0.6); }
}

/* CTA Banner Shimmer */
.cta-banner {
  background-size: 200% 100%;
  animation: shimmer 6s ease-in-out infinite;
}
@keyframes shimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

/* Stat Card Hover */
.stat-card {
  transition: all 0.3s ease;
}
.stat-card:hover {
  transform: translateY(-2px);
  border-color: rgba(255,255,255,0.2);
  background: rgba(255,255,255,0.15);
}
</style>
