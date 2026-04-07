<script setup>
import { computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import PointsWallet from '@/components/library/PointsWallet.vue'
import { useWalletStore } from '@/stores/walletStore'

const walletStore = useWalletStore()

onMounted(() => {
  walletStore.fetchWalletData()
})

const academicStream = computed(() => 'Information Technology')

// Mock Data for the Hub
const availableCourses = [
  { id: 1, code: 'IT3050', title: 'Data Science Fundamentals', credit: 4, type: 'Elective', rating: '4.8', students: 120 },
  { id: 2, code: 'IT3060', title: 'Cloud Computing Architecture', credit: 3, type: 'Elective', rating: '4.9', students: 85 },
  { id: 3, code: 'IT3070', title: 'Machine Learning Concepts', credit: 4, type: 'Elective', rating: '4.7', students: 150 },
]

const lecturers = [
  { id: 1, name: 'Dr. Nuwan Perera', title: 'Senior Lecturer - Software Eng', avatar: 'NP', isAvailable: true },
  { id: 2, name: 'Ms. Sanduni Fernando', title: 'Lecturer - Data Science', avatar: 'SF', isAvailable: false },
  { id: 3, name: 'Prof. Kamal Silva', title: 'Head of IT Department', avatar: 'KS', isAvailable: true },
]

const kuppiSessions = [
  { id: 1, title: 'Exam Prep: Microservices', tutor: 'Kasun Bandara (Year 4)', time: 'Today, 6:00 PM', location: 'Zoom Link' },
  { id: 2, title: 'Java Past Paper Discussion', tutor: 'Nimesha Perera (Year 3)', time: 'Tomorrow, 4:00 PM', location: 'Study Room 02' },
]

const resources = [
  { id: 1, title: 'ITPM Project Guidelines v2.pdf', type: 'PDF', size: '2.4 MB' },
  { id: 2, title: 'Spring Boot Cheat Sheet', type: 'DOCX', size: '1.1 MB' },
  { id: 3, title: 'Cloud Architecture Diagrams', type: 'ZIP', size: '15.6 MB' },
]
</script>

<template>
  <div class="animate-in fade-in slide-in-from-bottom-4 duration-500 pb-12 font-sans bg-[#F4F7F9] min-h-screen px-4 md:px-8 py-8">
    
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-extrabold text-[#2C3E50] tracking-tight mb-2">Academic Hub</h1>
      <p class="text-[16px] text-[#4B5563] font-medium">
        Discover courses, resources, and peers in <span class="text-[#4A90E2] font-bold">{{ academicStream }}</span>.
      </p>
    </div>

    <!-- Main Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
      
      <!-- LEFT COLUMN -->
      <div class="lg:col-span-8 space-y-8">
        
        <!-- Courses to Follow -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm">
          <div class="flex items-center justify-between mb-5">
            <h2 class="text-[18px] font-bold text-[#2C3E50] flex items-center gap-2">
              <span class="text-2xl">📚</span> Courses You Can Follow
            </h2>
            <button class="text-[#4A90E2] text-sm font-bold hover:underline">Browse All</button>
          </div>
          
          <div class="space-y-4">
            <div v-for="course in availableCourses" :key="course.id" class="flex flex-col sm:flex-row sm:items-center justify-between p-4 bg-slate-50 border border-slate-100 rounded-2xl hover:border-[#4A90E2]/30 transition-colors group cursor-pointer">
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <span class="bg-indigo-100 text-indigo-700 text-[11px] font-bold px-2 py-0.5 rounded-md">{{ course.code }}</span>
                  <span class="bg-slate-200 text-slate-700 text-[11px] font-bold px-2 py-0.5 rounded-md">{{ course.type }}</span>
                </div>
                <h3 class="font-bold text-[#2C3E50] text-[15px] group-hover:text-[#4A90E2] transition-colors">{{ course.title }}</h3>
                <p class="text-[12px] text-slate-500 mt-1">{{ course.credit }} Credits • ⭐ {{ course.rating }} ({{ course.students }} Students)</p>
              </div>
              <button class="mt-3 sm:mt-0 bg-white border border-[#4A90E2] text-[#4A90E2] hover:bg-[#4A90E2] hover:text-white font-bold py-2 px-5 rounded-xl text-[13px] transition-colors shadow-sm w-full sm:w-auto">
                Enroll
              </button>
            </div>
          </div>
        </div>

        <!-- Lecturers in My Stream -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm">
          <h2 class="text-[18px] font-bold text-[#2C3E50] flex items-center gap-2 mb-5">
            <span class="text-2xl">👨‍🏫</span> Lecturers in Your Stream
          </h2>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div v-for="lecturer in lecturers" :key="lecturer.id" class="border border-slate-100 p-4 rounded-2xl flex items-center gap-4 hover:shadow-md transition-shadow bg-white relative">
              <div class="absolute top-2 right-2 w-2.5 h-2.5 rounded-full" :class="lecturer.isAvailable ? 'bg-green-500' : 'bg-red-500'"></div>
              <div class="w-12 h-12 rounded-full bg-gradient-to-br from-blue-100 to-indigo-100 flex items-center justify-center text-indigo-800 font-bold text-lg border border-indigo-200 shrink-0">
                {{ lecturer.avatar }}
              </div>
              <div>
                <h3 class="font-bold text-[#2C3E50] text-[14px] leading-tight mb-1">{{ lecturer.name }}</h3>
                <p class="text-[11px] text-slate-500 leading-tight">{{ lecturer.title }}</p>
                <button class="mt-2 text-[#4A90E2] text-[12px] font-bold hover:underline">Message</button>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- RIGHT COLUMN -->
      <div class="lg:col-span-4 space-y-8">

        <!-- Points Wallet -->
        <PointsWallet />

        <!-- Kuppi Sessions -->
        <div class="bg-gradient-to-br from-[#1E293B] to-[#0F172A] rounded-[24px] p-6 border border-slate-700/50 shadow-lg relative overflow-hidden">
          <div class="absolute top-0 right-0 w-32 h-32 bg-yellow-500/10 blur-2xl rounded-full"></div>
          <h2 class="text-[18px] font-bold text-white flex items-center gap-2 mb-5 relative z-10">
            <span class="text-2xl">💡</span> Peer Tutor (Kuppi)
          </h2>
          
          <div class="space-y-4 relative z-10">
            <div v-for="kuppi in kuppiSessions" :key="kuppi.id" class="bg-white/10 backdrop-blur-md border border-white/10 p-4 rounded-xl">
              <div class="flex justify-between items-start mb-2">
                <h3 class="font-bold text-white text-[14px]">{{ kuppi.title }}</h3>
              </div>
              <p class="text-[12px] text-yellow-400 font-medium mb-1">By {{ kuppi.tutor }}</p>
              <div class="flex items-center gap-3 text-[11px] text-slate-300">
                <span class="flex items-center gap-1"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> {{ kuppi.time }}</span>
                <span class="flex items-center gap-1"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg> {{ kuppi.location }}</span>
              </div>
              <button class="mt-3 w-full bg-white/10 hover:bg-white/20 text-white text-[12px] font-bold py-1.5 rounded-lg transition-colors border border-white/10">RSVP / Join</button>
            </div>
          </div>
        </div>

        <!-- Resources to Refer -->
        <div class="bg-white rounded-[24px] p-6 border border-slate-200 shadow-sm">
          <h2 class="text-[18px] font-bold text-[#2C3E50] flex items-center gap-2 mb-5">
            <span class="text-2xl">📁</span> Recommended Materials
          </h2>
          
          <div class="space-y-3">
            <div v-for="res in resources" :key="res.id" class="flex items-center justify-between p-3 bg-slate-50 hover:bg-slate-100 rounded-xl transition-colors cursor-pointer border border-transparent hover:border-slate-200">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-white shadow-sm border border-slate-100 rounded-lg flex items-center justify-center text-[10px] font-bold text-slate-500 shrink-0">
                  {{ res.type }}
                </div>
                <div>
                  <h4 class="font-bold text-[#2C3E50] text-[13px] leading-tight">{{ res.title }}</h4>
                  <p class="text-[11px] text-slate-400 mt-0.5">{{ res.size }}</p>
                </div>
              </div>
              <button class="text-[#4A90E2] hover:bg-blue-50 p-2 rounded-lg transition-colors">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
              </button>
            </div>
          </div>
          <RouterLink 
            to="/dashboard/library" 
            class="w-full mt-4 block py-2.5 bg-slate-50 border border-slate-200 text-[#4A90E2] text-[13px] font-bold rounded-xl hover:bg-[#4A90E2] hover:text-white transition-all text-center"
          >
            Open Digital Library
          </RouterLink>
        </div>

      </div>
    </div>
  </div>
</template>
