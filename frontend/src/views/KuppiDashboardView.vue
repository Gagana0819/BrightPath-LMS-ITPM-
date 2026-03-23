<script setup>
import { computed } from 'vue'

const tutorName = computed(() => localStorage.getItem('full_name') || 'Sandun Dimantha')
const tutorRating = 4.8 // Mock rating
const googleSyncActive = true

const activeSessions = [
  { id: 1, title: 'Object Oriented Programming - Past Papers', date: 'Oct 25', time: '6:00 PM', students: 45, link: 'meet.google.com/xyz' },
  { id: 2, title: 'Database Optimization Techniques', date: 'Oct 27', time: '4:00 PM', students: 32, link: 'meet.google.com/abc' }
]

const pendingRequests = [
  { id: 1, student: 'Malithi Perera', topic: 'Help with React Context API', votes: 12 },
  { id: 2, student: 'Kamal Silva', topic: 'SQL Joins & Group By', votes: 8 }
]

const recentAttendees = [
  { id: 1, name: 'Sunil Shantha', present: true },
  { id: 2, name: 'Ama Fernando', present: true },
  { id: 3, name: 'Pasindu Kumara', present: false }
]
</script>

<template>
  <div class="animate-in fade-in slide-in-from-bottom-4 duration-500 pb-12 font-sans bg-[#F4F7F9] min-h-screen px-4 md:px-8 py-8">
    
    <!-- 1 & 6 & 7. Header + Badge + Integration Status -->
    <div class="mb-8 bg-white p-6 md:p-8 rounded-[24px] shadow-sm border border-slate-200">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 class="text-[28px] font-extrabold text-[#2C3E50] tracking-tight mb-2">
            Kuppi Tutor Dashboard
          </h1>
          <p class="text-[15px] text-[#4B5563] font-medium flex items-center gap-3">
            Welcome back, <span class="font-bold text-[#2C3E50]">{{ tutorName }}</span>!
            
            <!-- Integration Status -->
            <span v-if="googleSyncActive" class="flex items-center gap-1.5 text-[12px] bg-emerald-50 text-emerald-700 px-3 py-1 rounded-full border border-emerald-100 font-bold shadow-sm">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-[#A8E6CF]"></span>
              </span>
              Google Sync: Active
            </span>
          </p>
        </div>
        
        <!-- Tutor Performance Badge -->
        <div class="flex items-center gap-4 bg-gradient-to-r from-[#1E293B] to-[#0F172A] border border-slate-700 px-6 py-3.5 rounded-[20px] shadow-lg relative overflow-hidden group">
          <div class="absolute -right-4 -top-4 w-16 h-16 bg-yellow-500/20 blur-xl rounded-full"></div>
          <div class="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center shadow-inner text-2xl border border-white/5 backdrop-blur-md group-hover:scale-110 transition-transform">🏆</div>
          <div>
            <h3 class="text-white font-bold text-[14px]">Top Rated Tutor</h3>
            <div class="flex items-center gap-1 mt-0.5">
              <span class="text-yellow-400 text-[14px]">★★★★★</span>
              <span class="text-slate-300 text-[12px] font-bold ml-1">{{ tutorRating }} / 5.0</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Dashboard Grid -->
    <div class="grid grid-cols-1 xl:grid-cols-3 gap-8">
      
      <!-- LEFT COLUMN -->
      <div class="xl:col-span-2 space-y-8">
        
        <!-- 2. Active Sessions Overview -->
        <div class="bg-white rounded-[24px] p-6 md:p-8 border border-slate-200 shadow-sm">
          <div class="flex items-center justify-between mb-6">
            <h2 class="text-[18px] font-bold text-[#2C3E50] flex items-center gap-2">
              <span class="text-xl">🎙️</span> Active "Kuppi" Sessions
            </h2>
            <button class="bg-[#4A90E2] hover:bg-blue-700 text-white text-[13px] font-bold py-2 px-4 rounded-xl shadow-sm transition-colors flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
              New Session
            </button>
          </div>
          
          <div class="space-y-4">
            <div v-for="session in activeSessions" :key="session.id" class="flex flex-col sm:flex-row justify-between p-5 bg-slate-50 border border-slate-100 rounded-[16px] hover:border-blue-200 transition-colors group">
              <div>
                <div class="flex items-center gap-3 mb-2">
                  <span class="bg-blue-100 text-blue-700 text-[12px] font-bold px-2.5 py-0.5 rounded-lg border border-blue-200">{{ session.date }} &bull; {{ session.time }}</span>
                  <span class="text-[12px] text-slate-500 font-bold flex items-center gap-1">
                    <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5V4H2v16h5m4-4h2"></path></svg>
                    {{ session.students }} Registered
                  </span>
                </div>
                <h3 class="font-bold text-[#2C3E50] text-[16px] leading-tight group-hover:text-[#4A90E2] transition-colors">{{ session.title }}</h3>
              </div>
              <div class="mt-4 sm:mt-0 flex gap-2 sm:self-center">
                <button class="bg-white border border-slate-300 hover:bg-slate-100 text-slate-700 font-bold py-2 px-4 rounded-xl text-[13px] transition-colors shadow-sm">
                  Edit
                </button>
                <button class="bg-[#A8E6CF] hover:bg-emerald-600 text-white font-bold py-2 px-5 rounded-xl text-[13px] transition-colors shadow-sm flex items-center gap-2">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  Join
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Resource Upload Center -->
        <div class="bg-white rounded-[24px] p-6 md:p-8 border border-slate-200 shadow-sm">
          <h2 class="text-[18px] font-bold text-[#2C3E50] flex items-center gap-2 mb-2">
            <span class="text-xl">📁</span> Resource Upload Center
          </h2>
          <p class="text-[13px] text-slate-500 mb-6">Upload lecture notes and past papers for your sessions securely.</p>
          
          <div class="border-2 border-dashed border-slate-300 rounded-[20px] p-10 flex flex-col items-center justify-center bg-slate-50 hover:bg-blue-50/50 hover:border-blue-400 transition-colors cursor-pointer group">
            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-sm mb-4 group-hover:scale-110 transition-transform">
              <svg class="w-8 h-8 text-[#4A90E2]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"></path></svg>
            </div>
            <h3 class="text-[#2C3E50] font-bold text-[15px] mb-1">Click to upload or drag and drop</h3>
            <p class="text-[12px] text-slate-500">PDF, PPTX, or ZIP (Max 50MB)</p>
          </div>
        </div>

      </div>

      <!-- RIGHT COLUMN -->
      <div class="xl:col-span-1 space-y-8 flex flex-col">

        <!-- 1. Session Scheduler (Mini Calendar Mock) -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm relative overflow-hidden">
          <div class="absolute top-0 right-0 w-32 h-32 bg-blue-500/5 blur-2xl rounded-full pointer-events-none"></div>
          <h3 class="font-bold text-[#2C3E50] text-[16px] mb-5 flex items-center gap-2">
            <svg class="w-5 h-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
            Session Scheduler
          </h3>
          
          <!-- Mock Calendar Grid -->
          <div class="bg-slate-50 border border-slate-100 rounded-xl p-4">
            <div class="flex justify-between items-center text-[13px] font-bold text-[#2C3E50] mb-4">
              <button class="p-1 hover:bg-slate-200 rounded">&lt;</button>
              October 2026
              <button class="p-1 hover:bg-slate-200 rounded">&gt;</button>
            </div>
            <div class="grid grid-cols-7 gap-1 text-center text-[11px] font-bold text-slate-400 mb-2">
              <div>S</div><div>M</div><div>T</div><div>W</div><div>T</div><div>F</div><div>S</div>
            </div>
            <div class="grid grid-cols-7 gap-1 text-center text-[12px] font-medium text-slate-700">
              <!-- Placeholder Days -->
              <div class="p-1.5 text-slate-300">27</div><div class="p-1.5 text-slate-300">28</div><div class="p-1.5 text-slate-300">29</div><div class="p-1.5 text-slate-300">30</div>
              <div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">1</div><div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">2</div><div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">3</div>
              <div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">4</div><div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">5</div><div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">6</div><div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">7</div>
              <!-- Active Day -->
              <div class="p-1.5 bg-[#4A90E2] text-white font-bold rounded cursor-pointer shadow-sm shadow-blue-200">8</div>
              <div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">9</div><div class="p-1.5 hover:bg-slate-200 rounded cursor-pointer">10</div>
            </div>
            <button class="w-full mt-4 border border-blue-200 text-blue-700 bg-blue-50 hover:bg-blue-100 font-bold py-2 rounded-xl text-[12px] transition-colors">Open Google Calendar</button>
          </div>
        </div>

        <!-- 5. Request Inbox -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm flex-1">
          <h3 class="font-bold text-[#2C3E50] text-[16px] mb-5 flex items-center justify-between">
            <div class="flex items-center gap-2">
              <svg class="w-5 h-5 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
              Request Inbox
            </div>
            <span class="bg-amber-100 text-amber-800 text-[11px] px-2 py-0.5 rounded-full">+{{ pendingRequests.length }} New</span>
          </h3>
          
          <div class="space-y-3">
            <div v-for="req in pendingRequests" :key="req.id" class="p-3 bg-amber-50/50 border border-amber-100 rounded-xl">
              <div class="flex justify-between items-start mb-1">
                <h4 class="font-bold text-[#2C3E50] text-[13px] leading-tight">{{ req.topic }}</h4>
                <span class="text-[11px] font-bold text-amber-600 bg-amber-100 px-1.5 rounded flex items-center gap-1"><span class="text-[10px]">▲</span> {{ req.votes }}</span>
              </div>
              <p class="text-[11px] text-slate-500 mb-3">Requested by {{ req.student }}</p>
              <div class="flex gap-2">
                <button class="flex-1 bg-amber-500 hover:bg-amber-600 text-white text-[11px] font-bold py-1.5 rounded-lg transition-colors">Accept Topic</button>
                <button class="px-3 bg-white border border-slate-300 hover:bg-slate-100 text-slate-600 text-[11px] font-bold rounded-lg transition-colors">Dismiss</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 4. Student Attendance Tracker -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm">
          <h3 class="font-bold text-[#2C3E50] text-[16px] mb-4 flex items-center gap-2">
            <svg class="w-5 h-5 text-purple-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
            Recent Attendance
          </h3>
          
          <ul class="space-y-2">
            <li v-for="attendee in recentAttendees" :key="attendee.id" class="flex items-center justify-between p-2 rounded-lg hover:bg-slate-50 transition-colors">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center text-slate-600 text-[10px] font-bold">
                  {{ attendee.name.substring(0, 2).toUpperCase() }}
                </div>
                <span class="text-[13px] font-medium text-[#2C3E50]">{{ attendee.name }}</span>
              </div>
              <div :class="attendee.present ? 'bg-[#A8E6CF] text-green-700' : 'bg-red-100 text-red-700'" class="text-[10px] font-bold px-2 py-0.5 rounded-full">
                {{ attendee.present ? 'Present' : 'Absent' }}
              </div>
            </li>
          </ul>
          <button class="w-full mt-3 text-purple-600 text-[12px] font-bold hover:underline text-center">View Full Log</button>
        </div>

      </div>
    </div>
  </div>
</template>
