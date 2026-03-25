<script setup>
import { computed, ref } from 'vue'

// Mock fetching user details (in a real app, this comes from Pinia/API)
const fullName = computed(() => localStorage.getItem('full_name') || 'Sandun Dimantha')
const role = computed(() => localStorage.getItem('user_role') || 'STUDENT')
const academicStream = computed(() => 'Information Technology') // Using static for demo of Innovation spec
const academicYear = computed(() => 'Year 3')
const isPeerTutor = computed(() => true) // Set to true to show the requested badge

// Core Innovation: Stream-Based Logic
const suggestedCourses = ref([
  { id: 101, title: 'DevOps Engineering', desc: 'Master CI/CD pipelines and Docker containerization.', icon: '🚀', color: 'bg-blue-50 text-blue-600' },
  { id: 102, title: 'Microservices Architecture', desc: 'Build scalable distributed systems.', icon: '🧩', color: 'bg-purple-50 text-purple-600' },
  { id: 103, title: 'Advanced Java', desc: 'Deep dive into Spring Boot and Hibernate.', icon: '☕', color: 'bg-orange-50 text-orange-600' },
  { id: 104, title: 'Cloud Native Systems', desc: 'Serverless apps and Kubernetes orchestration.', icon: '☁️', color: 'bg-sky-50 text-sky-600' },
  { id: 105, title: 'UI/UX Design Strategy', desc: 'Mastering user-centric design principles.', icon: '🎨', color: 'bg-pink-50 text-pink-600' },
  { id: 106, title: 'Data Science Ethics', desc: 'Privacy, bias, and ethics in AI models.', icon: '⚖️', color: 'bg-slate-50 text-slate-600' }
])

const enrolledModules = ref([
  { id: 1, title: 'Information Technology Project', code: 'IT3040', credits: 4, progress: 75, icon: '💻', color: 'bg-indigo-50 text-indigo-600' },
  { id: 2, title: 'Mobile Application Dev', code: 'IT3030', credits: 3, progress: 40, icon: '📱', color: 'bg-emerald-50 text-[#A8E6CF]' }
])

const upcomingDeadlines = ref([
  { id: 1, month: 'Apr', day: '27', title: 'PAF Assignment Submission', module: 'IT3040 Project', deadline: 'Due at 11:59 PM', urgent: true },
  { id: 2, month: 'May', day: '02', title: 'React Component Quiz', module: 'IT3030 Mobile App', deadline: 'Due at 10:00 AM', urgent: false }
])

const searchQuery = ref('')
const filteredModules = computed(() => {
  if (!searchQuery.value) return enrolledModules.value
  const q = searchQuery.value.toLowerCase()
  return enrolledModules.value.filter(m => 
    m.title.toLowerCase().includes(q) || m.code.toLowerCase().includes(q)
  )
})

const notifications = ref([])
const addNotification = (message, type = 'success') => {
  const id = Date.now()
  notifications.value.push({ id, message, type })
  setTimeout(() => {
    notifications.value = notifications.value.filter(n => n.id !== id)
  }, 3000)
}

const enrollCourse = (course) => {
  if (enrolledModules.value.some(m => m.title === course.title)) {
    addNotification(`You are already enrolled in ${course.title}`, 'error')
    return
  }
  
  const newModule = {
    id: course.id, // Keep the ID for potential unenrollment unicity
    title: course.title,
    code: 'NEW-101',
    credits: 3,
    progress: 0,
    icon: course.icon,
    color: course.color,
    desc: course.desc // Keep description for when it moves back to suggestions
  }
  
  enrolledModules.value.unshift(newModule)
  suggestedCourses.value = suggestedCourses.value.filter(c => c.id !== course.id)
  addNotification(`Successfully enrolled in ${course.title}!`)
}

const unenrollCourse = (id) => {
  const module = enrolledModules.value.find(m => m.id === id)
  if (module) {
    if (confirm(`Are you sure you want to unenroll from ${module.title}?`)) {
       // Move back to suggested
       suggestedCourses.value.push({
         id: module.id,
         title: module.title,
         desc: module.desc || 'Found in your academic stream catalog.',
         icon: module.icon,
         color: module.color
       })
       enrolledModules.value = enrolledModules.value.filter(m => m.id !== id)
       addNotification(`Dropped Module: ${module.title}`, 'error')
    }
  }
}

const completeDeadline = (id) => {
  const deadline = upcomingDeadlines.value.find(d => d.id === id)
  if (deadline) {
    addNotification(`Task Completed: ${deadline.title}`)
    upcomingDeadlines.value = upcomingDeadlines.value.filter(d => d.id !== id)
  }
}

const launchModule = (module) => {
  addNotification(`Launching ${module.title}... Redirecting to LMS.`)
}
</script>

<template>
  <div class="animate-in fade-in slide-in-from-bottom-4 duration-500 pb-12 font-sans bg-[#F4F7F9] min-h-screen px-4 md:px-8 py-8 relative">
    
    <!-- Toast Notifications -->
    <div class="fixed top-8 right-8 z-[100] space-y-3 pointer-events-none">
      <transition-group 
        enter-active-class="transition duration-300 ease-out" 
        enter-from-class="transform translate-x-full opacity-0" 
        enter-to-class="transform translate-x-0 opacity-100"
        leave-active-class="transition duration-200 ease-in"
        leave-from-class="transform translate-x-0 opacity-100"
        leave-to-class="transform translate-x-full opacity-0"
      >
        <div v-for="note in notifications" :key="note.id" 
             :class="[note.type === 'success' ? 'bg-emerald-600' : 'bg-red-600', 'pointer-events-auto px-6 py-4 rounded-2xl text-white font-bold shadow-2xl flex items-center gap-3 border border-white/10 min-w-[300px]']">
          <span v-if="note.type === 'success'">✅</span>
          <span v-else>⚠️</span>
          {{ note.message }}
        </div>
      </transition-group>
    </div>
    
    <!-- 1. Personalized Welcome Header & Peer Tutor Badge -->
    <div class="mb-8 bg-white p-6 md:p-8 rounded-[24px] shadow-sm border-2 border-slate-200">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 class="text-3xl font-extrabold text-[#2C3E50] tracking-tight mb-2">
            Welcome, {{ fullName }}! 👋
          </h1>
          <p class="text-[16px] text-[#1F2937] font-medium flex items-center gap-2">
            — <span class="text-[#4A90E2] bg-[#EFF6FF] px-3 py-1 rounded-full text-sm font-bold">{{ academicStream }} Student</span>
          </p>
        </div>
        
        <!-- Peer Tutor Badge (Conditional) -->
        <router-link to="/dashboard/kuppi" v-if="isPeerTutor" class="flex items-center gap-3 bg-gradient-to-r from-[#FFFBEB] to-[#FEF3C7] border border-[#FDE68A] px-5 py-3 rounded-2xl shadow-sm hover:shadow-md transition-all cursor-pointer group">
          <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm text-xl border border-[#FDE68A] group-hover:rotate-12 transition-transform">🌟</div>
          <div>
            <h3 class="text-[#92400E] font-bold text-[14px]">Certified Peer Tutor</h3>
            <p class="text-[#B45309] text-[12px] font-medium">Access Kuppi Dashboard &rarr;</p>
          </div>
        </router-link>
      </div>
    </div>

    <!-- Main Dashboard Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
      
      <!-- LEFT COLUMN (Span 8) -->
      <div class="lg:col-span-8 space-y-8">
        
        <!-- 2. Enrolled Modules Grid (Cards with Progress Bars) -->
        <div>
          <div class="flex items-center justify-between mb-5">
            <h2 class="text-[20px] font-bold text-[#2C3E50] flex items-center gap-2">
              <svg class="w-6 h-6 text-[#4A90E2]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
              My Enrolled Modules
            </h2>
            <div class="flex items-center gap-4">
              <!-- Quick Search Bar -->
              <div class="hidden md:flex items-center bg-white border-2 border-slate-100 rounded-xl px-4 py-2 focus-within:border-[#4A90E2]/40 transition-all w-64 shadow-sm">
                <svg class="w-4 h-4 text-slate-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                <input v-model="searchQuery" type="text" placeholder="Search modules..." class="bg-transparent border-none outline-none text-[13px] text-[#2C3E50] placeholder:text-slate-400 w-full font-medium" />
              </div>
              <button class="text-[#4A90E2] text-sm font-bold hover:underline">View All</button>
            </div>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5 min-h-[140px]">
            <!-- Empty State -->
            <div v-if="filteredModules.length === 0" class="col-span-full py-12 text-center bg-white rounded-2xl border-2 border-dashed border-slate-200">
               <div class="text-3xl mb-2 grayscale opacity-30">🔍</div>
               <p class="text-slate-400 font-bold text-sm italic">No modules match your search "{{ searchQuery }}"</p>
               <button @click="searchQuery = ''" class="mt-2 text-[#4A90E2] font-extrabold text-xs hover:underline">Clear Search</button>
            </div>

            <div v-for="mod in filteredModules" :key="mod.id" class="bg-white rounded-2xl p-5 border-2 border-slate-200 shadow-[0_2px_10px_rgba(0,0,0,0.04)] hover:shadow-lg hover:border-[#4A90E2]/40 transition-all duration-300 relative overflow-hidden group">
              <div class="flex justify-between items-start mb-4">
                <div :class="[mod.color, 'w-12 h-12 rounded-2xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform shadow-sm']">{{ mod.icon }}</div>
                <div class="flex gap-2">
                  <button @click="unenrollCourse(mod.id)" class="bg-red-50 text-red-600 p-2.5 rounded-xl hover:bg-red-100 transition-all opacity-0 group-hover:opacity-100 transform translate-x-2 group-hover:translate-x-0" title="Drop Module">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                  </button>
                  <button @click="launchModule(mod)" class="bg-[#4A90E2] text-white p-2.5 rounded-xl shadow-lg shadow-blue-100 hover:bg-blue-600 transition-all opacity-0 group-hover:opacity-100 transform translate-x-2 group-hover:translate-x-0" title="Launch Module">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path></svg>
                  </button>
                </div>
              </div>
              <h3 class="font-bold text-[#2C3E50] text-[16px] mb-1">{{ mod.title }}</h3>
              <p class="text-[13px] text-[#374151] mb-5 font-medium">{{ mod.code }} • {{ mod.credits }} Credits</p>
              
              <!-- Progress Bar -->
              <div>
                <div class="flex justify-between text-[11px] font-extrabold text-[#1F2937] mb-2 uppercase tracking-wider">
                  <span>Learning Journey</span>
                  <span class="text-[#4A90E2]">{{ mod.progress }}%</span>
                </div>
                <div class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden ring-4 ring-slate-50">
                  <div class="bg-[#4A90E2] h-2.5 rounded-full transition-all duration-1000" :style="{ width: mod.progress + '%' }"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Core Innovation: "Suggested for You" (Stream-Based) -->
        <div class="bg-gradient-to-br from-[#2C3E50] to-[#1a252f] rounded-3xl p-8 relative overflow-hidden border border-slate-700/50 shadow-xl">
          <div class="absolute -right-20 -top-20 w-64 h-64 bg-[#4A90E2]/25 blur-3xl rounded-full pointer-events-none"></div>
          <div class="absolute -left-10 -bottom-10 w-48 h-48 bg-[#A8E6CF]/15 blur-3xl rounded-full pointer-events-none"></div>
          
          <div class="flex items-center gap-3 mb-6 relative z-10">
            <div class="p-2.5 bg-white/10 rounded-xl backdrop-blur-sm border border-white/10 text-xl">✨</div>
            <div>
              <h2 class="text-xl font-extrabold text-white tracking-tight">Suggested for You</h2>
              <p class="text-slate-300 text-sm font-semibold mt-1">AI-curated modules based on your <strong class="text-[#4A90E2]">{{ academicStream }}</strong> stream</p>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 relative z-10">
            <div v-for="course in suggestedCourses" :key="course.id" 
                 class="bg-white/[0.08] hover:bg-white/[0.15] border border-white/10 hover:border-[#4A90E2]/40 rounded-2xl p-5 backdrop-blur-md transition-all duration-300 cursor-pointer group hover:-translate-y-1 hover:shadow-[0_8px_25px_rgba(74,144,226,0.15)]">
              <div :class="[course.color, 'w-11 h-11 rounded-xl flex items-center justify-center text-xl mb-4 group-hover:scale-110 transition-transform duration-300 shadow-sm border border-white/10']">
                {{ course.icon }}
              </div>
              <h3 class="font-extrabold text-white text-[16px] mb-2 tracking-tight">{{ course.title }}</h3>
              <p class="text-slate-300 text-[13px] leading-relaxed font-medium">{{ course.desc }}</p>
              <button @click="enrollCourse(course)" class="mt-4 bg-[#4A90E2] hover:bg-white hover:text-[#4A90E2] text-white text-[11px] font-black px-4 py-2 rounded-lg transition-all flex items-center gap-2 shadow-lg shadow-[#4A90E2]/10">
                Enroll Now
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path></svg>
              </button>
            </div>
          </div>
        </div>

      </div>

      <!-- RIGHT COLUMN (Span 4) -->
      <div class="lg:col-span-4 space-y-8 flex flex-col">
        
        <!-- 6. Academic Year Summary -->
        <div class="bg-white rounded-[24px] p-6 border-2 border-slate-200 shadow-sm hover:shadow-md transition-all duration-300 relative overflow-hidden">
          <div class="absolute top-0 left-0 w-1.5 h-full bg-[#4A90E2]"></div>
          <h3 class="font-bold text-[#2C3E50] text-[16px] mb-1">Academic Status</h3>
          <p class="text-[13px] text-[#374151] mb-5">{{ academicYear }} Summary</p>
          
          <div class="flex items-center justify-between bg-slate-50 p-4 rounded-xl mb-3">
            <div class="flex items-center gap-3">
              <div class="text-xl">📚</div>
              <div>
                <p class="text-[12px] font-medium text-[#374151]">Compulsory Modules</p>
                <p class="font-bold text-[#2C3E50]">5 / 6 Registered</p>
              </div>
            </div>
          </div>
          
          <div class="flex items-center justify-between bg-slate-50 p-4 rounded-xl">
            <div class="flex items-center gap-3">
              <div class="text-xl">🎓</div>
              <div>
                <p class="text-[12px] font-medium text-[#374151]">Total Credits</p>
                <p class="font-bold text-[#2C3E50]">15 Credits Secured</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 4. Upcoming Deadlines & Tasks -->
        <div class="bg-white rounded-[24px] p-6 border-2 border-slate-200 shadow-sm hover:shadow-md transition-all duration-300 flex-1">
          <h3 class="font-bold text-[#2C3E50] text-[16px] mb-5 flex items-center gap-2">
            <svg class="w-5 h-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            Urgent Deadlines
          </h3>
          
          <div class="space-y-4">
            <div v-if="upcomingDeadlines.length === 0" class="py-12 text-center bg-slate-50 rounded-2xl border-2 border-dashed border-slate-200">
               <p class="text-slate-400 font-bold text-xs uppercase tracking-widest">All caught up! ✨</p>
            </div>

            <div v-for="deadline in upcomingDeadlines" :key="deadline.id" 
                 :class="['flex gap-4 items-start p-4 rounded-xl transition-all group relative', deadline.urgent ? 'bg-red-50 border border-red-100 shadow-sm' : 'hover:bg-slate-50 border border-transparent']">
              <div :class="[deadline.urgent ? 'bg-red-500 text-white' : 'bg-white text-slate-600 border border-slate-200', 'font-bold rounded-lg w-12 h-12 flex flex-col items-center justify-center shrink-0 shadow-sm']">
                <span class="text-[10px] uppercase">{{ deadline.month }}</span>
                <span class="text-[16px] leading-none">{{ deadline.day }}</span>
              </div>
              <div class="flex-1">
                <h4 class="font-bold text-[#2C3E50] text-[14px] leading-tight mb-1">{{ deadline.title }}</h4>
                <p class="text-[12px] text-[#374151] font-medium">{{ deadline.module }} • {{ deadline.deadline }}</p>
              </div>
              <button @click="completeDeadline(deadline.id)" class="bg-[#4A90E2] text-white p-1.5 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity shadow-lg shadow-blue-100 absolute top-2 right-2">
                 <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
              </button>
            </div>
          </div>
        </div>

        <!-- 7. Notification Panel -->
        <div class="bg-white rounded-[24px] p-6 border-2 border-slate-200 shadow-sm hover:shadow-md transition-all duration-300">
          <h3 class="font-bold text-[#2C3E50] text-[16px] mb-5 flex items-center gap-2">
            <svg class="w-5 h-5 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
            Recent Alerts
          </h3>
          
          <div class="space-y-4 relative before:absolute before:inset-0 before:ml-2 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-slate-200 before:to-transparent">
            
            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
              <div class="flex items-center justify-center w-6 h-6 rounded-full border-2 border-white bg-[#A8E6CF] text-white shadow shrink-0 z-10">
                <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
              </div>
              <div class="w-[calc(100%-2rem)] p-3 rounded-lg bg-green-50 border border-green-100 shadow-sm ml-4">
                <p class="text-[13px] font-bold text-green-800">Booking Approved</p>
                <p class="text-[12px] text-green-600 mt-1">Study Room 4 reserved for Apr 20.</p>
              </div>
            </div>

            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
              <div class="flex items-center justify-center w-6 h-6 rounded-full border-2 border-white bg-blue-500 text-white shadow shrink-0 z-10">
                <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
              </div>
              <div class="w-[calc(100%-2rem)] p-3 rounded-lg bg-blue-50 border border-blue-100 shadow-sm ml-4">
                <p class="text-[13px] font-bold text-blue-800">Maintenance Update</p>
                <p class="text-[12px] text-blue-600 mt-1">Ticket #1092 (AC Repair) resolved.</p>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  </div>
</template>
