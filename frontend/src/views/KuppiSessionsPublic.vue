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
const filters = ['All', 'Information Technology', 'Software Engineering', 'Cyber Security', 'Data Science']

const filteredSessions = ref(upcomingSessions)

const applyFilter = (filter) => {
  selectedFilter.value = filter
  if (filter === 'All') {
    filteredSessions.value = upcomingSessions
  } else {
    filteredSessions.value = upcomingSessions.filter(s => s.stream === filter)
  }
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
  <div class="min-h-screen bg-[#F4F7F9] font-sans pt-[90px] pb-16 relative overflow-hidden">
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
        <div class="relative bg-gradient-to-br from-[#2C3E50] to-[#1a252f] text-white py-16 px-8 md:px-12 overflow-hidden shadow-2xl rounded-3xl border border-slate-700/50">
          <div class="absolute inset-0 w-full h-full z-0 opacity-40 mix-blend-overlay">
            <img src="/hero BG.png" class="w-full h-full object-cover" />
          </div>
          <div class="absolute top-1/2 right-0 -translate-y-1/2 translate-x-1/4 w-[600px] z-0 opacity-60 mix-blend-screen pointer-events-none">
            <img src="/BG asset.png" class="w-full h-auto" />
          </div>
          <div class="absolute -right-20 -top-20 w-80 h-80 bg-[#4A90E2]/30 blur-3xl rounded-full z-0"></div>
          <div class="absolute -left-10 -bottom-10 w-60 h-60 bg-[#A8E6CF]/20 blur-3xl rounded-full z-0"></div>
          
          <div class="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
            <div class="max-w-[600px]">
              <div class="flex items-center gap-2 mb-4">
                <span class="bg-white/10 backdrop-blur-md border border-white/20 text-white text-[11px] font-bold px-3 py-1.5 rounded-full uppercase tracking-widest shadow-sm">Peer Tutoring</span>
              </div>
              <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-4">
                Kuppi <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#A8E6CF] to-[#4A90E2]">Sessions</span> 💡
              </h1>
              <p class="text-slate-300 text-lg leading-relaxed">
                Learn from your peers! Join live student-led tutoring sessions, discuss past papers, and ace your exams together.
              </p>
            </div>
            
            <div class="flex flex-col items-end gap-2 text-right shrink-0">
              <div class="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-6 text-center shadow-lg">
                <p class="text-4xl font-extrabold text-[#A8E6CF]">{{ upcomingSessions.length }}</p>
                <p class="text-slate-300 text-sm font-medium mt-1">Sessions Available</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    <div class="max-w-[1200px] mx-auto px-4">

      <!-- Stream Filters -->
      <div class="flex flex-wrap gap-2 mb-8 animate-fade-in-up delay-100">
        <button 
          v-for="filter in filters"
          :key="filter"
          @click="applyFilter(filter)"
          class="px-4 py-2 rounded-full text-[13px] font-bold border transition-all"
          :class="selectedFilter === filter 
            ? 'bg-[#4A90E2] text-white border-[#4A90E2] shadow-md' 
            : 'bg-white text-[#2C3E50] border-slate-200 hover:border-[#4A90E2] hover:text-[#4A90E2]'"
        >
          {{ filter }}
        </button>
      </div>

      <!-- Sessions Grid -->
      <transition-group name="list" tag="div" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 animate-fade-in-up delay-200 relative">
        <div 
          v-for="session in filteredSessions" 
          :key="session.id"
          class="bg-white rounded-[20px] p-6 border border-slate-200 shadow-sm hover:shadow-lg hover:border-[#4A90E2]/30 transition-all group cursor-pointer relative overflow-hidden"
          @click="joinSession(session)"
        >
          <!-- Stream Badge -->
          <div class="flex items-center justify-between mb-4">
            <span class="bg-[#4A90E2]/10 text-[#4A90E2] text-[11px] font-bold px-2.5 py-1 rounded-lg">{{ session.stream }}</span>
            <div class="flex items-center gap-1 text-[12px] text-slate-500 font-medium">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5V4H2v16h5m4-4h2"></path></svg>
              {{ session.students }} joined
            </div>
          </div>
          
          <!-- Title -->
          <h3 class="font-bold text-[#2C3E50] text-[16px] leading-tight mb-3 group-hover:text-[#4A90E2] transition-colors">{{ session.title }}</h3>
          
          <!-- Tutor Info -->
          <div class="flex items-center gap-3 mb-4">
            <div class="w-8 h-8 rounded-full bg-gradient-to-br from-blue-100 to-indigo-100 flex items-center justify-center text-indigo-800 font-bold text-[11px] border border-indigo-200 shrink-0">
              {{ session.tutor.split(' ').map(n => n[0]).join('') }}
            </div>
            <div>
              <p class="text-[13px] font-bold text-[#2C3E50]">{{ session.tutor }}</p>
              <p class="text-[11px] text-slate-500">{{ session.year }} Student</p>
            </div>
          </div>
          
          <!-- Tags -->
          <div class="flex flex-wrap gap-1.5 mb-4">
            <span v-for="tag in session.tags" :key="tag" class="bg-slate-100 text-slate-600 text-[10px] font-bold px-2 py-0.5 rounded-md">{{ tag }}</span>
          </div>
          
          <!-- Date & Join -->
          <div class="flex items-center justify-between pt-4 border-t border-slate-100">
            <div class="flex items-center gap-2 text-[12px] text-slate-500 font-medium">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              {{ session.date }} • {{ session.time }}
            </div>
            <button class="bg-[#4A90E2] hover:bg-blue-600 text-white text-[12px] font-bold py-1.5 px-4 rounded-lg transition-colors shadow-sm">
              Join
            </button>
          </div>
        </div>
      </transition-group>

      <!-- CTA Banner -->
      <div class="mt-12 bg-gradient-to-r from-[#2C3E50] to-[#34495e] rounded-[20px] p-8 flex flex-col md:flex-row items-center justify-between gap-6 border border-slate-700/50 relative overflow-hidden animate-fade-in-up delay-300">
        <div class="absolute -right-10 -top-10 w-40 h-40 bg-yellow-500/15 blur-2xl rounded-full"></div>
        <div class="relative z-10">
          <h3 class="text-white text-xl font-extrabold mb-2">Want to become a Peer Tutor? 🏆</h3>
          <p class="text-slate-300 text-[14px] max-w-[400px]">Register as a student and opt-in as a Kuppi Teacher to schedule your own sessions and help your batchmates excel.</p>
        </div>
        <RouterLink to="/register" class="bg-[#A8E6CF] hover:bg-[#8fd4b8] text-[#2C3E50] font-bold py-3 px-8 rounded-xl text-[14px] transition-colors shadow-md relative z-10 whitespace-nowrap">
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
</style>
