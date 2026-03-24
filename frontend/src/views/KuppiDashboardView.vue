<script setup>
import { computed, ref, onMounted, watch } from 'vue'
import { useContentStore } from '../stores/contentStore'
import { useRoute, useRouter } from 'vue-router'
import ResourceUploadModal from '../components/ResourceUploadModal.vue'

const contentStore = useContentStore()
const route = useRoute()
const router = useRouter()

const tutorName = computed(() => localStorage.getItem('full_name') || 'Sandun Dimantha')
const tutorRating = 4.8 

const activeSessionsList = ref([
  { 
    id: 1, 
    title: 'Object Oriented Programming - Past Papers', 
    date: 'Oct 25', 
    time: '6:00 PM', 
    students: 45, 
    link: 'https://meet.google.com/abc-xyz',
    videoUrl: 'https://www.youtube.com/embed/ScMzIvxBSi4',
    rawYoutube: 'https://www.youtube.com/watch?v=ScMzIvxBSi4'
  },
  { 
    id: 2, 
    title: 'Database Optimization Techniques', 
    date: 'Oct 27', 
    time: '4:00 PM', 
    students: 32, 
    link: 'https://meet.google.com/def-uvw',
    videoUrl: 'https://www.youtube.com/embed/668nUCeBHyY',
    rawYoutube: 'https://www.youtube.com/watch?v=668nUCeBHyY'
  }
])

const searchQuery = ref('')
const filteredSessions = computed(() => {
  if (!searchQuery.value) return activeSessionsList.value
  const q = searchQuery.value.toLowerCase()
  return activeSessionsList.value.filter(s => s.title.toLowerCase().includes(q))
})

const isUploadModalOpen = ref(false)
const isNewSessionModalOpen = ref(false)
const isEditing = ref(false)
const editingId = ref(null)

const newSession = ref({
  title: '',
  date: '',
  time: '',
  link: '',
  group: 'Information Technology'
})

const openNewSessionModal = () => {
  isEditing.value = false
  editingId.value = null
  newSession.value = { title: '', date: '', time: '', link: '', group: 'Information Technology' }
  isNewSessionModalOpen.value = true
}

const openEditModal = (session) => {
  isEditing.value = true
  editingId.value = session.id
  newSession.value = { 
    title: session.title, 
    date: session.date, 
    time: session.time, 
    link: session.link || '', 
    group: session.group || 'Information Technology' 
  }
  isNewSessionModalOpen.value = true
}

const submitSession = () => {
  if (!newSession.value.title || !newSession.value.date) return
  
  if (isEditing.value) {
    // Update existing session
    const index = activeSessionsList.value.findIndex(s => s.id === editingId.value)
    if (index !== -1) {
      activeSessionsList.value[index] = {
        ...activeSessionsList.value[index],
        ...newSession.value
      }
    }
  } else {
    // Create new session
    activeSessionsList.value.unshift({
      id: Date.now(),
      ...newSession.value,
      students: 0,
      videoUrl: '',
      rawYoutube: ''
    })
  }
  
  // Close and reset
  isNewSessionModalOpen.value = false
  isEditing.value = false
  editingId.value = null
}

// Video Player logic
const selectedVideoId = ref(null)
const selectedVideoUrl = ref('')
const selectedVideoRawUrl = ref('')
const isPlayerOpen = ref(false)
const currentVideoTitle = ref('')

const openPlayer = (id) => {
  const session = activeSessionsList.value.find(s => s.id == id) || activeSessionsList.value[0]
  currentVideoTitle.value = session.title
  selectedVideoUrl.value = session.videoUrl
  selectedVideoRawUrl.value = session.rawYoutube
  selectedVideoId.value = id
  isPlayerOpen.value = true
}

const closePlayer = () => {
  isPlayerOpen.value = false
  setTimeout(() => {
    selectedVideoId.value = null
    // Remove the play route but stay on dashboard
    router.push({ name: 'kuppi' })
  }, 300)
}

const handleSync = () => {
  contentStore.syncWithGoogleClassroom()
}

onMounted(() => {
  contentStore.fetchLiveSessions()
  
  // Check for auto-play from route
  if (route.params.id) {
    openPlayer(route.params.id)
  }
})

// Watch for route changes to trigger playback
watch(() => route.params.id, (newId) => {
  if (newId) {
    openPlayer(newId)
  } else {
    isPlayerOpen.value = false
  }
})

const pendingRequestsList = ref([
  { id: 1, student: 'Malithi Perera', topic: 'Help with React Context API', votes: 12 },
  { id: 2, student: 'Kamal Silva', topic: 'SQL Joins & Group By', votes: 8 }
])

const handleVote = (id) => {
  const req = pendingRequestsList.value.find(r => r.id === id)
  if (req) req.votes++
}

const dismissRequest = (id) => {
  pendingRequestsList.value = pendingRequestsList.value.filter(r => r.id !== id)
}
</script>

<template>
  <div class="animate-in fade-in slide-in-from-bottom-4 duration-500 pb-12 font-sans bg-[#F4F7F9] min-h-screen px-4 md:px-8 py-8">
    
    <!-- Header + Integration Status -->
    <div class="mb-8 bg-white p-6 md:p-8 rounded-[32px] shadow-sm border border-slate-200 relative overflow-hidden">
      <div class="absolute top-0 right-0 w-64 h-64 bg-blue-50/50 rounded-full blur-3xl -mr-32 -mt-32"></div>
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 relative z-10">
        <div>
          <h1 class="text-[32px] font-extrabold text-[#1E293B] tracking-tight mb-2">
            Kuppi Tutor Dashboard
          </h1>
          <div class="flex flex-wrap items-center gap-3">
            <p class="text-[15px] text-[#4B5563] font-medium">
              Welcome back, <span class="font-bold text-[#1E293B]">{{ tutorName }}</span>!
            </p>
            
            <!-- Integration Status -->
            <div @click="handleSync" class="cursor-pointer group">
              <span v-if="!contentStore.isSyncing" class="flex items-center gap-2 text-[11px] bg-emerald-50 text-emerald-700 px-4 py-1.5 rounded-full border border-emerald-100 font-bold shadow-sm hover:bg-emerald-100 transition-colors">
                <span class="flex h-2 w-2 relative">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                </span>
                Google Sync: Active
              </span>
              <span v-else class="flex items-center gap-2 text-[11px] bg-blue-50 text-blue-700 px-4 py-1.5 rounded-full border border-blue-100 font-bold shadow-sm">
                <svg class="animate-spin h-3 w-3" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                Syncing with Calendar...
              </span>
            </div>
          </div>
        </div>
        
        <!-- Tutor Performance Badge -->
        <div class="flex items-center gap-4 bg-slate-900 border border-slate-700 px-6 py-4 rounded-[24px] shadow-xl relative overflow-hidden group">
          <div class="absolute -right-4 -top-4 w-16 h-16 bg-yellow-500/20 blur-xl rounded-full"></div>
          <div class="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center shadow-inner text-2xl border border-white/5 backdrop-blur-md group-hover:scale-110 transition-transform">🎓</div>
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
        
        <!-- Active Sessions Overview -->
        <div class="bg-white rounded-[32px] p-8 border border-slate-200 shadow-sm">
          <div class="flex items-center justify-between mb-8">
            <h2 class="text-[20px] font-extrabold text-[#1E293B] flex items-center gap-3">
              <span class="w-10 h-10 bg-blue-50 rounded-xl flex items-center justify-center text-xl shadow-sm">🎙️</span> 
              Active "Kuppi" Sessions
            </h2>
            <div class="flex items-center gap-4">
              <!-- Inline Search Bar -->
              <div class="hidden md:flex items-center bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 focus-within:ring-2 focus-within:ring-blue-100 focus-within:border-blue-400 transition-all w-64">
                <svg class="w-4 h-4 text-slate-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                <input v-model="searchQuery" type="text" placeholder="Search sessions..." class="bg-transparent border-none outline-none text-[13px] text-[#1E293B] placeholder:text-slate-400 w-full font-medium" />
              </div>
              
              <button @click="openNewSessionModal" class="bg-blue-600 hover:bg-blue-700 text-white text-[13px] font-bold py-3 px-6 rounded-2xl shadow-lg shadow-blue-100 transition-all flex items-center gap-2 hover:-translate-y-0.5 active:translate-y-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"></path></svg>
                New Session
              </button>
            </div>
          </div>
          
          <div class="space-y-4">
            <!-- Empty State -->
            <div v-if="filteredSessions.length === 0" class="py-12 text-center bg-slate-50/50 rounded-3xl border border-dashed border-slate-200">
              <div class="text-4xl mb-3 opacity-40">🔍</div>
              <p class="text-slate-400 font-bold text-sm">No sessions found matching "{{ searchQuery }}"</p>
              <button @click="searchQuery = ''" class="mt-3 text-blue-600 font-extrabold text-xs hover:underline">Clear Search</button>
            </div>

            <div v-for="session in filteredSessions" :key="session.id" class="flex flex-col sm:flex-row justify-between p-6 bg-white border border-slate-100 rounded-[24px] hover:border-blue-400 hover:shadow-md transition-all group">
              <div class="flex items-start gap-4">
                 <div class="w-12 h-12 rounded-2xl bg-slate-50 flex items-center justify-center text-xl group-hover:bg-blue-50 transition-colors">👨‍💻</div>
                 <div>
                  <div class="flex items-center gap-3 mb-1">
                    <span class="bg-blue-50 text-blue-700 text-[11px] font-extrabold px-3 py-1 rounded-lg border border-blue-100 uppercase tracking-wider">{{ session.date }} @ {{ session.time }}</span>
                    <span class="text-[12px] text-slate-400 font-bold flex items-center gap-1">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5V4H2v16h5m4-4h2"></path></svg>
                      {{ session.students }} Students
                    </span>
                  </div>
                  <h3 class="font-bold text-[#1E293B] text-[17px] leading-tight group-hover:text-blue-600 transition-colors">{{ session.title }}</h3>
                </div>
              </div>
              <div class="mt-4 sm:mt-0 flex gap-2 sm:self-center">
                <button @click="openEditModal(session)" class="bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 font-bold py-2.5 px-5 rounded-xl text-[13px] transition-all">
                  Edit
                </button>
                <button @click="openPlayer(session.id)" class="bg-[#4A90E2] hover:bg-blue-600 text-white font-bold py-2.5 px-6 rounded-xl text-[13px] transition-all shadow-md flex items-center gap-2">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path></svg>
                  Watch Session
                </button>
                <a :href="session.link" target="_blank" class="bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-2.5 px-6 rounded-xl text-[13px] transition-all shadow-md flex items-center gap-2">
                  Join Live
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Resource Upload Box -->
        <div class="bg-gradient-to-br from-indigo-900 to-slate-900 rounded-[32px] p-8 text-white relative overflow-hidden shadow-2xl">
          <div class="absolute -right-10 -bottom-10 w-48 h-48 bg-blue-500/20 blur-3xl rounded-full"></div>
          <div class="relative z-10 flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="text-center md:text-left">
              <h2 class="text-[22px] font-extrabold mb-2">Resource Upload Center</h2>
              <p class="text-blue-100 text-sm opacity-80 max-w-sm">Securely upload lecture notes and past papers to <span class="text-white font-bold">AWS S3 Cloud</span> for your students.</p>
            </div>
            <button @click="isUploadModalOpen = true" class="bg-white text-slate-900 hover:bg-blue-50 px-8 py-4 rounded-[20px] font-extrabold text-[15px] shadow-lg transition-all active:scale-95 flex items-center gap-2 whitespace-nowrap">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
              Quick Upload
            </button>
          </div>
        </div>

      </div>

      <!-- RIGHT COLUMN -->
      <div class="xl:col-span-1 space-y-8">

        <!-- Session Scheduler -->
        <div class="bg-white rounded-[32px] p-8 border border-slate-200 shadow-sm relative overflow-hidden">
          <h3 class="font-extrabold text-[#1E293B] text-[18px] mb-6 flex items-center justify-between">
            <div class="flex items-center gap-3">
               <span class="w-8 h-8 bg-blue-50 rounded-lg flex items-center justify-center text-blue-600">📅</span>
               Calendar Sync
            </div>
            <button @click="handleSync" class="p-2 hover:bg-slate-50 rounded-lg transition-colors group">
               <svg :class="['w-5 h-5 text-slate-400 group-hover:text-blue-600', contentStore.isSyncing ? 'animate-spin text-blue-600' : '']" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" /></svg>
            </button>
          </h3>
          
          <div class="bg-slate-50 border border-slate-100 rounded-3xl p-6">
            <div class="flex justify-between items-center text-[14px] font-bold text-[#1E293B] mb-6">
              <button class="w-8 h-8 flex items-center justify-center hover:bg-white rounded-full transition-colors">&lt;</button>
              March 2026
              <button class="w-8 h-8 flex items-center justify-center hover:bg-white rounded-full transition-colors">&gt;</button>
            </div>
            
            <div class="grid grid-cols-7 gap-2 mb-4">
              <div v-for="d in ['S','M','T','W','T','F','S']" :key="d" class="text-center text-[11px] font-extrabold text-slate-400 uppercase tracking-widest">{{ d }}</div>
              
              <!-- Placeholder Days -->
              <div v-for="n in 5" :key="'p'+n" class="aspect-square flex items-center justify-center text-[13px] text-slate-200">2{{ n+3 }}</div>
              <div v-for="n in 25" :key="n" class="aspect-square flex items-center justify-center text-[13px] font-bold text-slate-600 hover:bg-white hover:text-blue-600 hover:shadow-sm rounded-xl cursor-pointer transition-all" :class="n === 25 ? 'bg-blue-600 text-white shadow-lg ring-4 ring-blue-100' : ''">
                {{ n }}
              </div>
            </div>
            
            <a href="https://calendar.google.com" target="_blank" class="w-full mt-4 flex items-center justify-center gap-2 border-2 border-slate-200 text-slate-700 bg-white hover:border-blue-500 hover:text-blue-600 font-extrabold py-3.5 rounded-2xl text-[13px] transition-all">
               <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Google_Calendar_icon_%282020%29.svg" class="w-5 h-5" alt="">
               Launch Google Calendar
            </a>
          </div>
        </div>

        <!-- Student Topic Requests -->
        <div class="bg-white rounded-[32px] p-8 border border-slate-200 shadow-sm relative overflow-hidden">
          <div class="absolute -right-4 -top-4 w-16 h-16 bg-blue-500/5 blur-xl rounded-full"></div>
          <h3 class="font-extrabold text-[#1E293B] text-[18px] mb-6 flex items-center justify-between">
            <div class="flex items-center gap-3">
               <span class="w-8 h-8 bg-orange-50 rounded-lg flex items-center justify-center text-orange-600 text-sm">💡</span>
               Topic Request Queue
            </div>
            <span class="text-[10px] bg-slate-100 text-slate-500 px-2 py-1 rounded-md font-bold uppercase tracking-wider">Priority</span>
          </h3>

          <div v-if="pendingRequestsList.length > 0" class="space-y-4">
            <div v-for="req in pendingRequestsList" :key="req.id" class="p-5 rounded-[20px] bg-slate-50/50 border border-slate-100 hover:border-blue-200 hover:bg-white transition-all group">
              <div class="flex justify-between items-start mb-3">
                <div class="flex items-center gap-2">
                  <img :src="'https://api.dicebear.com/7.x/notionists/svg?seed=' + req.student" class="w-6 h-6 rounded-full bg-blue-100" />
                  <span class="text-[12px] font-bold text-slate-700">{{ req.student }}</span>
                </div>
                <div class="flex items-center gap-1.5 text-blue-600">
                  <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 10.133a1.992 1.992 0 00-.8.2z" /></svg>
                  <span class="text-[12px] font-black">{{ req.votes }}</span>
                </div>
              </div>
              <p class="text-[13px] font-bold text-slate-800 mb-4 line-height-relaxed">{{ req.topic }}</p>
              <div class="flex gap-2">
                <button @click="handleVote(req.id)" class="flex-1 bg-blue-50 hover:bg-blue-100 text-blue-600 text-[11px] font-extrabold py-2 rounded-xl transition-colors">Upvote</button>
                <button @click="dismissRequest(req.id)" class="px-3 bg-slate-100 hover:bg-red-50 hover:text-red-600 text-slate-400 text-[11px] font-bold py-2 rounded-xl transition-all italic">Dismiss</button>
              </div>
            </div>
          </div>
          <div v-else class="text-center py-8">
            <div class="text-3xl mb-2 grayscale opacity-50">✨</div>
            <p class="text-slate-400 text-[12px] font-medium italic">Queue clear. Great job!</p>
          </div>

          <button class="w-full mt-6 py-3 border-2 border-dashed border-slate-200 rounded-2xl text-slate-400 text-[11px] font-bold hover:border-blue-300 hover:text-blue-500 transition-all">
             View History
          </button>
        </div>

        <!-- Attendance & Stats Group -->
        <div class="bg-white rounded-[32px] p-8 border border-slate-200 shadow-sm flex-1">
          <h3 class="font-extrabold text-[#1E293B] text-[18px] mb-6 flex items-center gap-3">
             <span class="w-8 h-8 bg-purple-50 rounded-lg flex items-center justify-center text-purple-600 text-sm">📈</span>
             Quick Analytics
          </h3>
          
          <div class="space-y-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-[12px] font-bold text-slate-400 uppercase tracking-widest mb-1">Total Attendance</p>
                <p class="text-[24px] font-extrabold text-slate-800">1.2k <span class="text-[14px] text-emerald-500 font-bold ml-1">+12%</span></p>
              </div>
              <div class="w-20 h-10 bg-emerald-50 rounded-lg flex items-center justify-center border border-emerald-100">
                <svg class="w-12 h-6 text-emerald-500" viewBox="0 0 100 30" fill="none" stroke="currentColor" stroke-width="4"><path d="M0 25 L20 15 L40 20 L60 5 L80 15 L100 0" stroke-linecap="round" /></svg>
              </div>
            </div>

            <div class="pt-6 border-t border-slate-50">
               <p class="text-[13px] font-bold text-slate-700 mb-4">Recent Students</p>
               <div class="flex -space-x-3 overflow-hidden">
                 <div v-for="n in 5" :key="n" :class="['inline-block h-10 w-10 rounded-full ring-4 ring-white shadow-sm flex items-center justify-center font-bold text-xs border border-slate-100', ['bg-blue-100 text-blue-600', 'bg-purple-100 text-purple-600', 'bg-amber-100 text-amber-600', 'bg-rose-100 text-rose-600', 'bg-indigo-100 text-indigo-600'][n-1]]">
                   {{ ['SP', 'MK', 'AF', 'PK', 'RJ'][n-1] }}
                 </div>
                 <div class="inline-block h-10 w-10 rounded-full bg-slate-900 border-2 border-white flex items-center justify-center text-white text-[10px] font-bold">+24</div>
               </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Video Player Modal -->
    <div v-if="isPlayerOpen" class="fixed inset-0 z-[100] flex items-center justify-center bg-slate-900/90 backdrop-blur-md p-4 animate-in fade-in duration-300">
      <div class="bg-[#0F172A] w-full max-w-5xl rounded-[32px] shadow-2xl overflow-hidden border border-slate-800 flex flex-col max-h-[90vh]">
        <!-- Modal Header -->
        <div class="p-6 border-b border-slate-800 flex justify-between items-center bg-slate-900/50">
          <div>
            <span class="text-blue-500 text-[10px] font-bold uppercase tracking-widest mb-1 block">Now Playing Recording</span>
            <h3 class="text-white font-extrabold text-xl">{{ currentVideoTitle }}</h3>
          </div>
          <button @click="closePlayer" class="w-10 h-10 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition-colors">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        <!-- Video Player Body -->
        <div class="flex-1 relative aspect-video bg-black flex items-center justify-center">
          <iframe 
            v-if="selectedVideoUrl"
            class="w-full h-full"
            :src="selectedVideoUrl + '?autoplay=1'" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            referrerpolicy="strict-origin-when-cross-origin" 
            allowfullscreen>
          </iframe>
          
          <!-- Fallback/Loading -->
          <div v-else class="absolute inset-0 flex items-center justify-center">
            <div class="text-center animate-pulse">
              <div class="w-20 h-20 rounded-full bg-white/10 flex items-center justify-center mb-4 mx-auto">
                <svg class="w-10 h-10 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg>
              </div>
              <p class="text-slate-500 font-bold uppercase tracking-tighter text-sm">Initializing Secure Stream...</p>
            </div>
          </div>
        </div>

        <!-- Links Section -->
        <div class="p-6 bg-slate-900 border-t border-slate-800 flex justify-between items-center">
          <p class="text-slate-400 text-sm font-medium">Recorded Feb 24, 2026 • 2.4k Views</p>
          <div class="flex gap-4">
            <a :href="selectedVideoRawUrl" target="_blank" class="text-slate-300 font-bold text-sm hover:text-white flex items-center gap-2 border border-slate-700 px-4 py-2 rounded-xl transition-all hover:bg-slate-800">
               <img src="https://upload.wikimedia.org/wikipedia/commons/e/ef/Youtube_logo.png" class="h-4" alt="YouTube" />
               Open in YouTube
            </a>
            <a href="#" class="text-emerald-500 font-bold text-sm hover:underline flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-width="2.5"/></svg>
              Google Classroom Mirror
            </a>
            <button class="bg-blue-600 px-6 py-2.5 rounded-xl text-white font-bold text-sm shadow-lg shadow-blue-900/20">Download Assets</button>
          </div>
        </div>
      </div>
    </div>

    <!-- New Session Modal -->
    <div v-if="isNewSessionModalOpen" class="fixed inset-0 z-[110] flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4 animate-in fade-in duration-300">
      <div class="bg-white w-full max-w-lg rounded-[32px] shadow-2xl overflow-hidden border border-slate-100 flex flex-col animate-in zoom-in-95 duration-300">
        <div class="p-8 border-b border-slate-50 flex justify-between items-center bg-slate-50/50">
          <div>
            <h3 class="text-[#1E293B] font-extrabold text-2xl tracking-tight">{{ isEditing ? 'Edit Session' : 'Create New Session' }}</h3>
            <p class="text-slate-500 text-sm font-medium mt-1">{{ isEditing ? 'Update your session details below.' : 'Schedule a new live peer-tutoring session.' }}</p>
          </div>
          <button @click="isNewSessionModalOpen = false" class="w-10 h-10 rounded-xl bg-white text-slate-400 hover:text-slate-600 flex items-center justify-center shadow-sm border border-slate-100 transition-colors">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        <form @submit.prevent="submitSession" class="p-8 space-y-6">
          <div class="space-y-2">
            <label class="text-[13px] font-bold text-slate-700 ml-1 uppercase tracking-wider">Session Title</label>
            <input v-model="newSession.title" type="text" placeholder="e.g. Advanced Algorithm Analysis" class="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-4 focus:ring-blue-100 focus:border-blue-500 outline-none transition-all font-medium text-slate-800" required />
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="space-y-2">
              <label class="text-[13px] font-bold text-slate-700 ml-1 uppercase tracking-wider">Date</label>
              <input v-model="newSession.date" type="text" placeholder="Oct 30" class="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-4 focus:ring-blue-100 focus:border-blue-500 outline-none transition-all font-medium text-slate-800" required />
            </div>
            <div class="space-y-2">
              <label class="text-[13px] font-bold text-slate-700 ml-1 uppercase tracking-wider">Time</label>
              <input v-model="newSession.time" type="text" placeholder="5:30 PM" class="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-4 focus:ring-blue-100 focus:border-blue-500 outline-none transition-all font-medium text-slate-800" required />
            </div>
          </div>

          <div class="space-y-2">
            <label class="text-[13px] font-bold text-slate-700 ml-1 uppercase tracking-wider">Interactive Meet Link</label>
            <input v-model="newSession.link" type="url" placeholder="https://meet.google.com/..." class="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-4 focus:ring-blue-100 focus:border-blue-500 outline-none transition-all font-medium text-slate-800" />
          </div>

          <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-extrabold py-5 rounded-[22px] shadow-xl shadow-blue-200 transition-all hover:-translate-y-1 active:scale-[0.98] mt-4 flex items-center justify-center gap-3">
             <svg v-if="!isEditing" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" /></svg>
             <svg v-else class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" /></svg>
             {{ isEditing ? 'Update Session Details' : 'Launch Session Listing' }}
          </button>
        </form>
      </div>
    </div>

    <!-- Quick Upload Modal -->
    <ResourceUploadModal 
      v-if="isUploadModalOpen" 
      @close="isUploadModalOpen = false" 
    />
  </div>
</template>
