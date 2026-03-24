<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// Recommendation carousel
const recScrollRef = ref(null)
const canScrollLeft = ref(false)
const canScrollRight = ref(true)

const recommendedResources = ref([
  { id: 'r1', title: 'ITPM 2025 Final Exam Past Paper with Model Answers', type: 'Past Paper', module: 'IT Project Management', uploader: 'Kasun Silva', tag: 'Most Downloaded', image: '/itpm_thumbnail.png' },
  { id: 'r2', title: 'OOP Design Patterns — Complete Short Notes', type: 'Short Note', module: 'Object-Oriented Programming', uploader: 'Dr. Amanda', tag: 'Top Rated', image: '/oop_thumbnail.png' },
  { id: 'r3', title: 'Database Normalization Cheat Sheet (1NF–BCNF)', type: 'Short Note', module: 'Database Systems', uploader: 'Sanduni M.', tag: 'Trending', image: '/database_thumbnail.png' },
  { id: 'r4', title: 'Data Structures — 2024 Midterm Past Paper', type: 'Past Paper', module: 'Data Structures', uploader: 'Nuwan P.', tag: 'New', image: '/data_structures_thumbnail.png' },
  { id: 'r5', title: 'Machine Learning Key Concepts Summary', type: 'Short Note', module: 'Machine Learning', uploader: 'Dr. Fernando', tag: 'AI Trending', image: '/ml_thumbnail.png' },
  { id: 'r6', title: 'Cloud Computing — AWS Services Past Paper 2024', type: 'Past Paper', module: 'Cloud Computing', uploader: 'Prof. Kumara', tag: 'Popular', image: '/cloud_thumbnail.png' },
])

const updateRecScroll = () => {
  const el = recScrollRef.value
  if (!el) return
  canScrollLeft.value = el.scrollLeft > 10
  canScrollRight.value = el.scrollLeft < el.scrollWidth - el.clientWidth - 10
}

const scrollRec = (dir) => {
  const el = recScrollRef.value
  if (!el) return
  el.scrollBy({ left: dir === 'left' ? -320 : 320, behavior: 'smooth' })
  setTimeout(updateRecScroll, 350)
}

// Search & filter state
const searchQuery = ref('')
const selectedModule = ref('All')
const selectedType = ref('All')
const sortBy = ref('rank')
const showFilterPanel = ref(false)

const activeFilterCount = computed(() => {
  let count = 0
  if (selectedModule.value !== 'All') count++
  if (selectedType.value !== 'All') count++
  if (sortBy.value !== 'rank') count++
  return count
})

const clearFilters = () => {
  selectedModule.value = 'All'
  selectedType.value = 'All'
  sortBy.value = 'rank'
}

const modules = ['All', 'IT Project Management', 'Object-Oriented Programming', 'Database Systems', 'Data Structures', 'UI/UX Design', 'Machine Learning', 'Cloud Computing']
const fileTypes = ['All', 'PDF', 'DOCX', 'PPT', 'ZIP', 'FIG']

// Mock documents data
const documents = ref([
  { id: 1, title: 'IT Project Management - 2024 Midterm Past Paper & Answers', uploader: 'Kasun Silva', module: 'IT Project Management', rank: 'Gold', score: 98, type: 'PDF', points: 350, downloads: 1240 },
  { id: 2, title: 'Object-Oriented Programming Complete Lecture Notes', uploader: 'Dr. Amanda', module: 'Object-Oriented Programming', rank: 'Gold', score: 95, type: 'DOCX', points: 210, downloads: 890 },
  { id: 3, title: 'Database Systems - SQL Joins Summary (Week 4-7)', uploader: 'Nuwan P.', module: 'Database Systems', rank: 'Silver', score: 82, type: 'PPT', points: 150, downloads: 620 },
  { id: 4, title: 'Data Structures & Algorithms - Final Assignment Template', uploader: 'Sanduni M.', module: 'Data Structures', rank: 'Gold', score: 92, type: 'ZIP', points: 420, downloads: 1100 },
  { id: 5, title: 'UI/UX Design Wireframes & Mockup Library', uploader: 'Sanduni S.', module: 'UI/UX Design', rank: 'Gold', score: 91, type: 'FIG', points: 280, downloads: 760 },
  { id: 6, title: 'Machine Learning Basics - Neural Networks Overview', uploader: 'Dr. Fernando', module: 'Machine Learning', rank: 'Silver', score: 78, type: 'PDF', points: 190, downloads: 540 },
  { id: 7, title: 'Cloud Computing AWS Lab Guide', uploader: 'Prof. Kumara', module: 'Cloud Computing', rank: 'Bronze', score: 65, type: 'PDF', points: 120, downloads: 320 },
  { id: 8, title: 'ITPM Final Exam Revision Notes 2025', uploader: 'Dilshan K.', module: 'IT Project Management', rank: 'Silver', score: 84, type: 'PDF', points: 175, downloads: 690 },
])

// Points wallet data
const walletData = ref({
  totalPoints: 3450,
  tier: 'Gold',
  tierProgress: 85,
  pointsToNext: 150,
  recentActivity: [
    { action: 'Downloaded', doc: 'ITPM Midterm Paper', points: -20, time: '2h ago' },
    { action: 'Uploaded', doc: 'OOP Notes', points: +50, time: '1d ago' },
    { action: 'Review Bonus', doc: 'SQL Joins Summary', points: +15, time: '2d ago' },
  ]
})

// Filtered & sorted documents
const filteredDocuments = computed(() => {
  let result = documents.value

  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    result = result.filter(d =>
      d.title.toLowerCase().includes(q) ||
      d.uploader.toLowerCase().includes(q) ||
      d.module.toLowerCase().includes(q)
    )
  }
  if (selectedModule.value !== 'All') {
    result = result.filter(d => d.module === selectedModule.value)
  }
  if (selectedType.value !== 'All') {
    result = result.filter(d => d.type === selectedType.value)
  }

  if (sortBy.value === 'rank') result = [...result].sort((a, b) => b.score - a.score)
  else if (sortBy.value === 'downloads') result = [...result].sort((a, b) => b.downloads - a.downloads)
  else if (sortBy.value === 'points') result = [...result].sort((a, b) => b.points - a.points)

  return result
})

const getRankColor = (rank) => {
  if (rank === 'Gold') return 'text-[#FFB800] bg-[#FFB800]/10 border-[#FFB800]/40'
  if (rank === 'Silver') return 'text-slate-500 bg-slate-100 border-slate-300'
  if (rank === 'Bronze') return 'text-amber-700 bg-amber-50 border-amber-300'
  return 'text-slate-500 bg-slate-100 border-slate-200'
}

const getRankIcon = (rank) => {
  if (rank === 'Gold') return '🏆'
  if (rank === 'Silver') return '🥈'
  if (rank === 'Bronze') return '🥉'
  return ''
}

const getTypeColor = (type) => {
  if (type === 'PDF') return 'bg-red-50 text-red-500'
  if (type === 'DOCX') return 'bg-[#4A90E2]/10 text-[#4A90E2]'
  if (type === 'PPT') return 'bg-amber-50 text-amber-600'
  if (type === 'ZIP') return 'bg-[#A8E6CF]/30 text-[#2C3E50]'
  if (type === 'FIG') return 'bg-purple-50 text-purple-600'
  return 'bg-slate-100 text-slate-600'
}
</script>

<template>
  <div class="digital-library-page bg-[#F4F7F9] min-h-screen relative overflow-hidden">
    <main class="pt-[90px] pb-16 relative">
      <!-- Global Decorative Backgrounds -->
      <div class="absolute inset-0 w-full h-full z-0 opacity-30 fixed pointer-events-none">
        <img src="/hero BG.png" class="w-full h-full object-cover" />
      </div>
      <div class="absolute top-0 right-0 w-[80%] max-w-[800px] z-0 opacity-40 mix-blend-multiply pointer-events-none -translate-y-1/4 translate-x-1/4 fixed">
        <img src="/BG asset.png" class="w-full h-auto" />
      </div>

      <div class="relative z-10 max-w-[1600px] mx-auto px-6 lg:px-10">

        <!-- Attractive Hero Banner -->
        <div class="relative bg-slate-900 text-white py-16 lg:py-24 px-8 lg:px-12 mb-12 overflow-hidden shadow-2xl rounded-3xl border border-slate-700/50 animate-fade-in-down">
          <div class="absolute inset-0 w-full h-full z-0 opacity-40 mix-blend-overlay">
            <img src="/hero BG.png" class="w-full h-full object-cover" />
          </div>
          <div class="absolute top-1/2 right-0 -translate-y-1/2 translate-x-1/4 w-[700px] z-0 opacity-60 mix-blend-screen pointer-events-none">
            <img src="/BG asset.png" class="w-full h-auto" />
          </div>
          <div class="absolute -left-20 -bottom-20 w-96 h-96 bg-[#4A90E2]/30 blur-3xl rounded-full z-0"></div>

          <div class="relative z-10">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white text-[11px] font-bold uppercase tracking-widest w-max mb-6">
              Resource Hub
            </div>
            <h1 class="text-[3rem] lg:text-[4.5rem] leading-[1.1] font-extrabold tracking-tight mb-4">
              Digital <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-sky-300">Library</span>
            </h1>
            <p class="text-lg lg:text-xl text-slate-300 max-w-[600px] leading-relaxed">
              Search, discover, and download peer-reviewed resources. Earn points and climb the ranks by contributing to the community.
            </p>
          </div>
        </div>

        <!-- BrightPath Recommend for You -->
        <div class="mb-10 animate-fade-in-up delay-100">
          <div class="flex items-center justify-between mb-6">
            <div class="flex items-center gap-3">
              <div>
                <h2 class="text-xl font-extrabold text-[#2C3E50] tracking-tight pl-4">BrightPath Recommend for You</h2>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <button @click="scrollRec('left')" :disabled="!canScrollLeft" class="w-9 h-9 rounded-full border border-slate-200 bg-white flex items-center justify-center text-slate-400 hover:text-[#4A90E2] hover:border-[#4A90E2] transition-all disabled:opacity-30 disabled:cursor-not-allowed shadow-sm">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
              </button>
              <button @click="scrollRec('right')" :disabled="!canScrollRight" class="w-9 h-9 rounded-full border border-slate-200 bg-white flex items-center justify-center text-slate-400 hover:text-[#4A90E2] hover:border-[#4A90E2] transition-all disabled:opacity-30 disabled:cursor-not-allowed shadow-sm">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" /></svg>
              </button>
            </div>
          </div>

          <div ref="recScrollRef" @scroll="updateRecScroll" class="flex gap-5 overflow-x-auto pb-4 scroll-smooth rec-scroll-hide">
            <div
              v-for="rec in recommendedResources"
              :key="rec.id"
              class="min-w-[280px] max-w-[280px] bg-white rounded-2xl border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-pointer group overflow-hidden flex flex-col shrink-0"
            >
              <!-- Thumbnail -->
              <div class="relative h-[150px] overflow-hidden">
                <img :src="rec.image" class="absolute inset-0 w-full h-full object-cover opacity-90" />
                <div class="absolute inset-0 flex items-center justify-center">
                  <div v-if="rec.type === 'Past Paper'" class="w-16 h-20 bg-white/20 backdrop-blur-sm rounded-lg border border-white/30 flex flex-col items-center justify-center gap-1">
                    <svg class="w-7 h-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" /></svg>
                    <span class="text-[9px] text-white font-bold uppercase">PDF</span>
                  </div>
                  <div v-else class="w-16 h-20 bg-white/20 backdrop-blur-sm rounded-lg border border-white/30 flex flex-col items-center justify-center gap-1">
                    <svg class="w-7 h-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25" /></svg>
                    <span class="text-[9px] text-white font-bold uppercase">Notes</span>
                  </div>
                </div>
                <!-- Tag badge -->
                <span class="absolute top-3 left-3 bg-black/30 backdrop-blur-md text-white text-[10px] font-bold px-2.5 py-1 rounded-lg border border-white/10">{{ rec.tag }}</span>
                <!-- Type badge -->
                <span class="absolute bottom-3 right-3 text-white text-[10px] font-extrabold px-2.5 py-1 rounded-lg" :class="rec.type === 'Past Paper' ? 'bg-red-500/80 backdrop-blur-sm' : 'bg-[#4A90E2]/80 backdrop-blur-sm'">{{ rec.type }}</span>
              </div>
              <!-- Content -->
              <div class="p-4 flex flex-col flex-1">
                <p class="text-[11px] text-slate-400 font-bold uppercase tracking-wider mb-1.5">{{ rec.module }}</p>
                <h4 class="text-[14px] font-bold text-[#2C3E50] leading-snug mb-3 line-clamp-2 group-hover:text-[#4A90E2] transition-colors">{{ rec.title }}</h4>
                <div class="mt-auto flex items-center gap-2">
                  <div class="w-6 h-6 rounded-full bg-[#4A90E2]/10 flex items-center justify-center text-[#4A90E2] text-[9px] font-bold">{{ rec.uploader.split(' ').map(n => n[0]).join('').substring(0, 2) }}</div>
                  <span class="text-xs text-slate-500 font-medium">{{ rec.uploader }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="flex flex-col lg:flex-row gap-8">

          <!-- Main Content Area -->
          <div class="flex-1 space-y-6">

            <!-- Compact Search Bar -->
            <div class="bg-white rounded-2xl p-4 shadow-sm border border-[#4A90E2]/10 animate-fade-in-up delay-100">
              <div class="flex items-center gap-3">
                <!-- Search Input -->
                <div class="relative flex-1">
                  <svg class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                  </svg>
                  <input
                    v-model="searchQuery"
                    type="text"
                    placeholder="Search by title, module, or uploader..."
                    class="w-full bg-[#F4F7F9] border border-slate-200 rounded-xl pl-12 pr-4 py-3.5 outline-none focus:border-[#4A90E2] focus:ring-2 focus:ring-[#4A90E2]/20 transition-all font-medium text-[#2C3E50]"
                  />
                </div>
                <!-- Filter Button -->
                <button
                  @click="showFilterPanel = true"
                  class="relative flex items-center gap-2 px-5 py-3.5 bg-[#4A90E2] text-white rounded-xl font-bold hover:bg-[#3A7BC8] transition-all shadow-sm hover:shadow-md active:scale-[0.97] shrink-0"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
                    <path d="M22 3H2l8 9.46V19l4 2v-8.54L22 3z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Filters
                  <!-- Active filter count badge -->
                  <span
                    v-if="activeFilterCount > 0"
                    class="absolute -top-2 -right-2 w-5 h-5 bg-[#FFB800] text-[#2C3E50] rounded-full text-xs font-black flex items-center justify-center shadow-md animate-bounce"
                  >{{ activeFilterCount }}</span>
                </button>
              </div>
              <!-- Results count -->
              <div class="flex items-center justify-between mt-3 pt-3 border-t border-slate-100">
                <p class="text-sm text-slate-500 font-medium">
                  <span class="text-[#4A90E2] font-bold">{{ filteredDocuments.length }}</span> resources found
                </p>
                <!-- Active filter tags -->
                <div class="flex items-center gap-2 flex-wrap">
                  <span v-if="selectedModule !== 'All'" class="inline-flex items-center gap-1 px-2.5 py-1 bg-[#4A90E2]/10 text-[#4A90E2] text-xs font-bold rounded-lg">
                    {{ selectedModule }}
                    <button @click="selectedModule = 'All'" class="hover:text-red-500 transition-colors">✕</button>
                  </span>
                  <span v-if="selectedType !== 'All'" class="inline-flex items-center gap-1 px-2.5 py-1 bg-[#4A90E2]/10 text-[#4A90E2] text-xs font-bold rounded-lg">
                    {{ selectedType }}
                    <button @click="selectedType = 'All'" class="hover:text-red-500 transition-colors">✕</button>
                  </span>
                </div>
              </div>
            </div>

            <!-- Slide-In Filter Panel Overlay -->
            <Teleport to="body">
              <Transition name="overlay">
                <div v-if="showFilterPanel" class="fixed inset-0 bg-black/40 backdrop-blur-sm z-[100]" @click="showFilterPanel = false"></div>
              </Transition>
              <Transition name="slide">
                <div v-if="showFilterPanel" class="fixed top-0 right-0 h-full w-[400px] max-w-[90vw] bg-white z-[101] shadow-2xl flex flex-col">
                  <!-- Panel Header -->
                  <div class="flex items-center justify-between p-6 border-b border-slate-100">
                    <div>
                      <h2 class="text-xl font-bold text-[#2C3E50]">Filters & Sort</h2>
                      <p class="text-sm text-slate-400 mt-0.5">Refine your search results</p>
                    </div>
                    <button @click="showFilterPanel = false" class="w-10 h-10 rounded-xl bg-[#F4F7F9] flex items-center justify-center text-slate-500 hover:text-red-500 hover:bg-red-50 transition-colors">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                        <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </button>
                  </div>

                  <!-- Panel Body -->
                  <div class="flex-1 overflow-y-auto p-6 space-y-8">

                    <!-- Sort By Section -->
                    <div>
                      <label class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-3 block">Sort By</label>
                      <div class="space-y-2">
                        <label
                          v-for="option in [{value: 'rank', label: '🏆 Highest Ranked', desc: 'Best quality first'}, {value: 'downloads', label: '📥 Most Downloads', desc: 'Popular resources'}, {value: 'points', label: '💎 Most Points', desc: 'Highest reward value'}]"
                          :key="option.value"
                          class="flex items-center gap-3 p-3.5 rounded-xl border-2 cursor-pointer transition-all"
                          :class="sortBy === option.value ? 'border-[#4A90E2] bg-[#4A90E2]/5' : 'border-slate-100 hover:border-slate-200 bg-white'"
                          @click="sortBy = option.value"
                        >
                          <div class="w-5 h-5 rounded-full border-2 flex items-center justify-center shrink-0" :class="sortBy === option.value ? 'border-[#4A90E2]' : 'border-slate-300'">
                            <div v-if="sortBy === option.value" class="w-2.5 h-2.5 rounded-full bg-[#4A90E2]"></div>
                          </div>
                          <div>
                            <span class="font-bold text-[#2C3E50] text-sm">{{ option.label }}</span>
                            <p class="text-xs text-slate-400">{{ option.desc }}</p>
                          </div>
                        </label>
                      </div>
                    </div>

                    <!-- Module Filter Section -->
                    <div>
                      <label class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-3 block">Module</label>
                      <div class="flex flex-wrap gap-2">
                        <button
                          v-for="m in modules"
                          :key="m"
                          @click="selectedModule = m"
                          class="px-3.5 py-2 rounded-xl text-sm font-semibold transition-all border"
                          :class="selectedModule === m ? 'bg-[#4A90E2] text-white border-[#4A90E2] shadow-md' : 'bg-[#F4F7F9] text-[#2C3E50] border-slate-200 hover:border-[#4A90E2]/40'"
                        >
                          {{ m === 'All' ? '🗂 All Modules' : m }}
                        </button>
                      </div>
                    </div>

                    <!-- File Type Filter Section -->
                    <div>
                      <label class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-3 block">File Type</label>
                      <div class="grid grid-cols-3 gap-2">
                        <button
                          v-for="t in fileTypes"
                          :key="t"
                          @click="selectedType = t"
                          class="px-3 py-2.5 rounded-xl text-sm font-bold transition-all border text-center"
                          :class="selectedType === t ? 'bg-[#4A90E2] text-white border-[#4A90E2] shadow-md' : 'bg-[#F4F7F9] text-[#2C3E50] border-slate-200 hover:border-[#4A90E2]/40'"
                        >
                          {{ t === 'All' ? '📁 All' : t }}
                        </button>
                      </div>
                    </div>
                  </div>

                  <!-- Panel Footer -->
                  <div class="p-6 border-t border-slate-100 space-y-3">
                    <button
                      @click="showFilterPanel = false"
                      class="w-full py-3.5 bg-[#4A90E2] text-white rounded-xl font-bold hover:bg-[#3A7BC8] transition-all shadow-md text-sm"
                    >
                      Show {{ filteredDocuments.length }} Results
                    </button>
                    <button
                      @click="clearFilters"
                      class="w-full py-3 bg-transparent text-slate-500 rounded-xl font-semibold hover:text-red-500 hover:bg-red-50 transition-all text-sm"
                    >
                      Clear All Filters
                    </button>
                  </div>
                </div>
              </Transition>
            </Teleport>

            <!-- Document Grid with Transition -->
            <transition-group name="list" tag="div" class="flex flex-wrap justify-center gap-6 animate-fade-in-up delay-200 relative">
              <div
                v-for="doc in filteredDocuments"
                :key="doc.id"
                class="bg-white rounded-2xl overflow-hidden border border-[#4A90E2]/10 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group cursor-pointer flex flex-col w-[calc(33.333%-16px)] min-w-[280px]"
              >
                <!-- Card Header with Type Badge -->
                <div class="p-5 pb-0">
                  <div class="flex justify-between items-start mb-4">
                    <div class="w-14 h-14 rounded-2xl flex items-center justify-center font-bold text-lg shadow-inner" :class="getTypeColor(doc.type)">
                      {{ doc.type }}
                    </div>
                    <!-- Rank Badge -->
                    <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold border" :class="getRankColor(doc.rank)">
                      <span>{{ getRankIcon(doc.rank) }}</span>
                      {{ doc.rank }} Rank
                    </div>
                  </div>
                </div>

                <!-- Card Body -->
                <div class="px-5 pb-5 flex flex-col flex-1">
                  <h3 class="font-bold text-[#2C3E50] text-[1.05rem] leading-tight mb-2 line-clamp-2 group-hover:text-[#4A90E2] transition-colors">
                    {{ doc.title }}
                  </h3>

                  <p class="text-sm text-slate-500 mb-1">
                    By <span class="font-semibold text-[#4A90E2]">{{ doc.uploader }}</span>
                  </p>
                  <p class="text-xs text-slate-400 mb-4">{{ doc.module }}</p>

                  <!-- Score Bar -->
                  <div class="mb-4">
                    <div class="flex justify-between items-center mb-1">
                      <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Quality Score</span>
                      <span class="text-sm font-bold" :class="doc.score >= 90 ? 'text-[#FFB800]' : 'text-[#2C3E50]'">{{ doc.score }}%</span>
                    </div>
                    <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
                      <div
                        class="h-1.5 rounded-full transition-all duration-500"
                        :class="doc.score >= 90 ? 'bg-gradient-to-r from-[#4A90E2] to-[#FFB800]' : doc.score >= 75 ? 'bg-[#4A90E2]' : 'bg-slate-400'"
                        :style="{ width: doc.score + '%' }"
                      ></div>
                    </div>
                  </div>

                  <!-- Card Footer -->
                  <div class="mt-auto flex items-center justify-between border-t border-slate-100 pt-4">
                    <div class="flex flex-col">
                      <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider mb-0.5">Reward</span>
                      <div class="flex items-center gap-1.5 text-[#2C3E50] font-black text-base">
                        <span class="w-2 h-2 rounded-full bg-[#A8E6CF] animate-pulse"></span>
                        +{{ doc.points }} BP
                      </div>
                    </div>
                    <div class="flex items-center gap-2">
                      <span class="text-xs text-slate-400">{{ doc.downloads.toLocaleString() }} downloads</span>
                      <button class="w-10 h-10 rounded-full bg-[#F4F7F9] border border-[#4A90E2]/20 flex items-center justify-center text-[#4A90E2] hover:bg-[#4A90E2] hover:text-white transition-colors">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
                          <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </transition-group>

            <!-- Empty State -->
            <div v-if="filteredDocuments.length === 0" class="bg-white rounded-2xl p-12 text-center border border-[#4A90E2]/10">
              <div class="text-5xl mb-4">📚</div>
              <h3 class="text-xl font-bold text-[#2C3E50] mb-2">No resources found</h3>
              <p class="text-slate-500">Try adjusting your search or filters to find what you're looking for.</p>
            </div>
          </div>
        </div>
      </div>
    </main>

  </div>
</template>

<style scoped>
.digital-library-page {
  width: 100%;
}

/* Page Load Animations */
@keyframes fadeInDown {
  0% { opacity: 0; transform: translateY(-30px); }
  100% { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(30px); }
  100% { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInLeft {
  0% { opacity: 0; transform: translateX(30px); }
  100% { opacity: 1; transform: translateX(0); }
}

.animate-fade-in-down {
  animation: fadeInDown 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.animate-fade-in-up {
  opacity: 0;
  animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.animate-fade-in-left {
  opacity: 0;
  animation: fadeInLeft 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.delay-100 { animation-delay: 100ms; }
.delay-200 { animation-delay: 200ms; }
.delay-300 { animation-delay: 300ms; }

/* Grid Transition Group */
.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px) scale(0.95);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}

/* Hide scrollbar for recommendation carousel */
.rec-scroll-hide::-webkit-scrollbar { display: none; }
.rec-scroll-hide { -ms-overflow-style: none; scrollbar-width: none; }
</style>

<style>
/* Slide-in panel animation (global for Teleport) */
.slide-enter-active {
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
.slide-leave-active {
  transition: transform 0.25s cubic-bezier(0.4, 0, 1, 1);
}
.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}

/* Overlay fade animation */
.overlay-enter-active {
  transition: opacity 0.3s ease;
}
.overlay-leave-active {
  transition: opacity 0.2s ease;
}
.overlay-enter-from,
.overlay-leave-to {
  opacity: 0;
}
</style>
