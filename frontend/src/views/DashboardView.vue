<script setup>
import { computed, ref } from 'vue'

// Mock fetching user details (in a real app, this comes from Pinia/API)
const fullName = computed(() => localStorage.getItem('full_name') || 'Sandun Dimantha')
const role = computed(() => localStorage.getItem('user_role') || 'STUDENT')
const academicStream = computed(() => 'Information Technology') // Using static for demo of Innovation spec
const academicYear = computed(() => 'Year 3')
const isPeerTutor = computed(() => true) // Set to true to show the requested badge

// Core Innovation: Stream-Based Logic
const suggestedCourses = computed(() => {
  if (academicStream.value.includes('Information Technology') || academicStream.value.includes('Software')) {
    return [
      { id: 1, title: 'DevOps Engineering', desc: 'Master CI/CD pipelines and Docker containerization.', icon: '🚀', color: 'bg-blue-50 text-blue-600' },
      { id: 2, title: 'Microservices Architecture', desc: 'Build scalable distributed systems.', icon: '🧩', color: 'bg-purple-50 text-purple-600' },
      { id: 3, title: 'Advanced Java', desc: 'Deep dive into Spring Boot and Hibernate.', icon: '☕', color: 'bg-orange-50 text-orange-600' }
    ]
  } else if (academicStream.value.includes('Cyber Security')) {
    return [
      { id: 4, title: 'Network Security', desc: 'Secure enterprise networks against intrusions.', icon: '🛡️', color: 'bg-red-50 text-red-600' },
      { id: 5, title: 'Ethical Hacking', desc: 'Learn penetration testing methodologies.', icon: '🕵️', color: 'bg-slate-800 text-green-400' }
    ]
  }
  return [] // Default empty
})
</script>

<template>
  <div class="animate-in fade-in slide-in-from-bottom-4 duration-500 pb-12 font-sans bg-[#F8FAFC] min-h-screen px-4 md:px-8 py-8">
    
    <!-- 1. Personalized Welcome Header & Peer Tutor Badge -->
    <div class="mb-8 bg-white p-6 md:p-8 rounded-[24px] shadow-sm border border-slate-200">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 class="text-3xl font-extrabold text-[#111827] tracking-tight mb-2">
            Welcome, {{ fullName }}! 👋
          </h1>
          <p class="text-[16px] text-[#4B5563] font-medium flex items-center gap-2">
            — <span class="text-[#2563EB] bg-[#EFF6FF] px-3 py-1 rounded-full text-sm font-bold">{{ academicStream }} Student</span>
          </p>
        </div>
        
        <!-- Peer Tutor Badge (Conditional) -->
        <div v-if="isPeerTutor" class="flex items-center gap-3 bg-gradient-to-r from-[#FFFBEB] to-[#FEF3C7] border border-[#FDE68A] px-5 py-3 rounded-2xl shadow-sm hover:shadow-md transition-all cursor-pointer group">
          <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm text-xl border border-[#FDE68A] group-hover:rotate-12 transition-transform">🌟</div>
          <div>
            <h3 class="text-[#92400E] font-bold text-[14px]">Certified Peer Tutor</h3>
            <p class="text-[#B45309] text-[12px] font-medium">Access Kuppi Dashboard &rarr;</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Dashboard Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
      
      <!-- LEFT COLUMN (Span 8) -->
      <div class="lg:col-span-8 space-y-8">
        
        <!-- 2. Enrolled Modules Grid (Cards with Progress Bars) -->
        <div>
          <div class="flex items-center justify-between mb-5">
            <h2 class="text-[20px] font-bold text-[#111827] flex items-center gap-2">
              <svg class="w-6 h-6 text-[#2563EB]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
              My Enrolled Modules
            </h2>
            <button class="text-[#2563EB] text-sm font-bold hover:underline">View All</button>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <!-- Module Card 1 -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-[0_2px_10px_rgba(0,0,0,0.02)] hover:shadow-md transition-shadow relative overflow-hidden group">
              <div class="w-12 h-12 bg-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">💻</div>
              <h3 class="font-bold text-[#111827] text-[16px] mb-1">Information Technology Project</h3>
              <p class="text-[13px] text-[#6B7280] mb-5">IT3040 • 4 Credits</p>
              
              <!-- Progress Bar -->
              <div>
                <div class="flex justify-between text-[12px] font-bold text-[#4B5563] mb-2">
                  <span>Progress</span>
                  <span class="text-[#2563EB]">75% Completed</span>
                </div>
                <div class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden">
                  <div class="bg-[#2563EB] h-2.5 rounded-full w-[75%] transition-all duration-1000"></div>
                </div>
              </div>
            </div>

            <!-- Module Card 2 -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-[0_2px_10px_rgba(0,0,0,0.02)] hover:shadow-md transition-shadow relative overflow-hidden group">
              <div class="w-12 h-12 bg-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">📱</div>
              <h3 class="font-bold text-[#111827] text-[16px] mb-1">Mobile Application Dev</h3>
              <p class="text-[13px] text-[#6B7280] mb-5">IT3030 • 3 Credits</p>
              
              <!-- Progress Bar -->
              <div>
                <div class="flex justify-between text-[12px] font-bold text-[#4B5563] mb-2">
                  <span>Progress</span>
                  <span class="text-emerald-600">40% Completed</span>
                </div>
                <div class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden">
                  <div class="bg-emerald-500 h-2.5 rounded-full w-[40%] transition-all duration-1000"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Core Innovation: "Suggested for You" (Stream-Based) -->
        <div class="bg-gradient-to-br from-[#1E293B] to-[#0F172A] rounded-3xl p-8 relative overflow-hidden border border-slate-700/50 shadow-xl">
          <div class="absolute -right-20 -top-20 w-64 h-64 bg-blue-500/20 blur-3xl rounded-full pointer-events-none"></div>
          
          <div class="flex items-center gap-3 mb-6 relative z-10">
            <div class="p-2 bg-white/10 rounded-xl backdrop-blur-sm border border-white/10">✨</div>
            <div>
              <h2 class="text-xl font-bold text-white tracking-tight">Suggested for You</h2>
              <p class="text-slate-400 text-sm mt-1">AI-curated modules based on your <strong>{{ academicStream }}</strong> stream</p>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 relative z-10">
            <div v-for="course in suggestedCourses" :key="course.id" 
                 class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-2xl p-5 backdrop-blur-md transition-all cursor-pointer group">
              <div :class="[course.color, 'w-10 h-10 rounded-xl flex items-center justify-center text-xl mb-4 group-hover:scale-110 transition-transform shadow-sm']">
                {{ course.icon }}
              </div>
              <h3 class="font-bold text-white text-[15px] mb-2">{{ course.title }}</h3>
              <p class="text-slate-400 text-[12px] leading-relaxed">{{ course.desc }}</p>
            </div>
          </div>
        </div>

      </div>

      <!-- RIGHT COLUMN (Span 4) -->
      <div class="lg:col-span-4 space-y-8 flex flex-col">
        
        <!-- 6. Academic Year Summary -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm relative overflow-hidden">
          <div class="absolute top-0 left-0 w-1.5 h-full bg-[#2563EB]"></div>
          <h3 class="font-bold text-[#111827] text-[16px] mb-1">Academic Status</h3>
          <p class="text-[13px] text-[#6B7280] mb-5">{{ academicYear }} Summary</p>
          
          <div class="flex items-center justify-between bg-slate-50 p-4 rounded-xl mb-3">
            <div class="flex items-center gap-3">
              <div class="text-xl">📚</div>
              <div>
                <p class="text-[12px] font-medium text-[#6B7280]">Compulsory Modules</p>
                <p class="font-bold text-[#111827]">5 / 6 Registered</p>
              </div>
            </div>
          </div>
          
          <div class="flex items-center justify-between bg-slate-50 p-4 rounded-xl">
            <div class="flex items-center gap-3">
              <div class="text-xl">🎓</div>
              <div>
                <p class="text-[12px] font-medium text-[#6B7280]">Total Credits</p>
                <p class="font-bold text-[#111827]">15 Credits Secured</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 4. Upcoming Deadlines & Tasks -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm flex-1">
          <h3 class="font-bold text-[#111827] text-[16px] mb-5 flex items-center gap-2">
            <svg class="w-5 h-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            Urgent Deadlines
          </h3>
          
          <div class="space-y-4">
            <div class="flex gap-4 items-start p-3 bg-red-50 border border-red-100 rounded-xl">
              <div class="bg-white text-red-600 font-bold rounded-lg border border-red-200 w-12 h-12 flex flex-col items-center justify-center shrink-0 shadow-sm">
                <span class="text-[10px] uppercase">Apr</span>
                <span class="text-[16px] leading-none">27</span>
              </div>
              <div>
                <h4 class="font-bold text-[#111827] text-[14px]">PAF Assignment Submission</h4>
                <p class="text-[12px] text-[#6B7280] mt-1">IT3040 Project • Due at 11:59 PM</p>
              </div>
            </div>

            <div class="flex gap-4 items-start p-3 hover:bg-slate-50 rounded-xl transition-colors">
              <div class="bg-slate-100 text-slate-600 font-bold rounded-lg w-12 h-12 flex flex-col items-center justify-center shrink-0">
                <span class="text-[10px] uppercase">May</span>
                <span class="text-[16px] leading-none">02</span>
              </div>
              <div>
                <h4 class="font-bold text-[#111827] text-[14px]">React Component Quiz</h4>
                <p class="text-[12px] text-[#6B7280] mt-1">IT3030 Mobile App • Due at 10:00 AM</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 7. Notification Panel -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm">
          <h3 class="font-bold text-[#111827] text-[16px] mb-5 flex items-center gap-2">
            <svg class="w-5 h-5 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
            Recent Alerts
          </h3>
          
          <div class="space-y-4 relative before:absolute before:inset-0 before:ml-2 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-slate-200 before:to-transparent">
            
            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
              <div class="flex items-center justify-center w-6 h-6 rounded-full border-2 border-white bg-green-500 text-white shadow shrink-0 z-10">
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
