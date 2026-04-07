<script setup>
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { useRouter, useRoute } from 'vue-router'

import { useContentStore } from '@/stores/contentStore'
import ResourceCard from '@/components/content/ResourceCard.vue'

// Recommendation carousel
const recScrollRef = ref(null)
const canScrollLeft = ref(false)
const canScrollRight = ref(true)

const contentStore = useContentStore()
const router = useRouter()
const route = useRoute()

onMounted(async () => {
  await Promise.all([
    contentStore.fetchResources({ userOnly: false }),
    contentStore.fetchRecommendations()
  ])
  checkDeepLink()
})

const checkDeepLink = () => {
  const resourceId = route.query.review_resource
  if (resourceId && contentStore.resources.length > 0) {
    // Auth Guard: Only open deep-links for logged-in users
    const isLoggedIn = !!localStorage.getItem('access_token')
    if (!isLoggedIn) {
      // Save current path to redirect back after login
      router.push({ path: '/login', query: { redirect: route.fullPath } })
      return
    }

    // Find the resource in the loaded list
    const resource = contentStore.resources.find(r => r.id == resourceId)
    if (resource) {
      openPreview(resource)
      // Automatically open the reviews modal after a short delay for smooth animation
      setTimeout(() => {
        showReviewsModal.value = true
      }, 600)
      
      // Clean up the URL so it doesn't re-trigger on refresh
      router.replace({ query: { ...route.query, review_resource: undefined } })
    }
  }
}

const recommendedResources = computed(() => contentStore.recommendedResources)

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

const getResourceImage = (res) => {
  const text = (res.title + ' ' + (res.module_code || '')).toLowerCase();
  
  if (text.includes('database') || text.includes('sql') || text.includes('dbms') || text.includes('it3020')) return '/database_thumbnail.png';
  if (text.includes('machine learning') || text.includes('ml') || text.includes('ai')) return '/ml_thumbnail.png';
  if (text.includes('itpm') || text.includes('project management') || text.includes('it3030')) return '/itpm_thumbnail.png';
  if (text.includes('oop') || text.includes('java') || text.includes('object oriented')) return '/oop_thumbnail.png';
  if (text.includes('cloud') || text.includes('aws') || text.includes('azure')) return '/cloud_thumbnail.png';
  if (text.includes('data structure') || text.includes('algorithm') || text.includes('ds ') || text.includes('it3040')) return '/data_structures_thumbnail.png';
  
  if (res.resource_type === 'PAST_PAPER') return '/itpm_thumbnail.png';
  return '/database-ai-thumbnail.png'; // Diverse fallback
}

// Search & filter state
const searchQuery = ref('')
const selectedModule = ref('All')
const selectedType = ref('All')
const sortBy = ref('recent')
const showFilterPanel = ref(false)

// Resource Preview state
const selectedResource = ref(null)
const showPreview = ref(false)

const openPreview = (doc) => {
  selectedResource.value = doc
  showPreview.value = true
}

const handleDownload = (doc, e) => {
  const isLoggedIn = !!localStorage.getItem('access_token')
  if (!isLoggedIn) {
     if (e) e.preventDefault()
     router.push('/login')
     return
  }
  contentStore.recordResourceDownload(doc.id)
}

// Stats & Reviews
const ratingStats = ref({ average_rating: 0, total_ratings: 0, distribution: {1:0, 2:0, 3:0, 4:0, 5:0} })
const reviewsList = ref([])
const showReviewsModal = ref(false)
const showAddReviewForm = ref(false)
const userHasReviewed = ref(false)
const newReview = ref({ rating: 5, comment: '' })

watch(selectedResource, async (newVal) => {
  if (newVal) {
    const [stats, reviews] = await Promise.all([
      contentStore.fetchResourceStats(newVal.id),
      contentStore.fetchResourceReviews(newVal.id)
    ])
    if (stats) {
      ratingStats.value = stats
      userHasReviewed.value = stats.user_has_reviewed
    }
    reviewsList.value = reviews
  }
})

const submitReview = async () => {
  if (!selectedResource.value) return
  try {
    await contentStore.submitResourceReview(selectedResource.value.id, newReview.value)
    // Refresh
    if (stats) {
      ratingStats.value = stats
      userHasReviewed.value = stats.user_has_reviewed
    }
    reviewsList.value = reviews
    showAddReviewForm.value = false
    newReview.value = { rating: 5, comment: '' }
  } catch (err) {
    alert(err.detail || 'Failed to submit review')
  }
}

const activeFilterCount = computed(() => {
  let count = 0
  if (selectedModule.value !== 'All') count++
  if (selectedType.value !== 'All') count++
  if (sortBy.value !== 'recent') count++
  return count
})

const clearFilters = () => {
  selectedModule.value = 'All'
  selectedType.value = 'All'
  sortBy.value = 'recent'
}

const modules = ['All', 'IT3040', 'IT3030', 'IT Project Management', 'Object-Oriented Programming', 'Database Systems', 'Data Structures', 'UI/UX Design', 'Machine Learning', 'Cloud Computing']
const fileTypes = ['All', 'LECTURE_NOTES', 'PAST_PAPER', 'TUTORIAL_ANSWER', 'SHORT_NOTE']

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
  let result = [...contentStore.resources]

  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    result = result.filter(d =>
      d.title.toLowerCase().includes(q) ||
      (d.module_code && d.module_code.toLowerCase().includes(q))
    )
  }
  if (selectedModule.value !== 'All') {
    result = result.filter(d => d.module_code && d.module_code.includes(selectedModule.value))
  }
  if (selectedType.value !== 'All') {
    result = result.filter(d => d.resource_type === selectedType.value)
  }

  if (sortBy.value === 'recent') {
    result.sort((a, b) => new Date(b.uploaded_at) - new Date(a.uploaded_at))
  }

  return result
})
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
        <div v-if="recommendedResources.length > 0" class="mb-10 animate-fade-in-up delay-100">
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
              @click="openPreview(rec)"
              class="min-w-[280px] max-w-[280px] bg-white rounded-2xl border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-pointer group overflow-hidden flex flex-col shrink-0"
            >
              <!-- Thumbnail -->
              <div class="relative h-[150px] overflow-hidden">
                <img :src="getResourceImage(rec)" class="absolute inset-0 w-full h-full object-cover opacity-90 transition-transform duration-500 group-hover:scale-110" />
                <div class="absolute inset-0 flex items-center justify-center">
                  <div v-if="rec.resource_type === 'PAST_PAPER'" class="w-16 h-20 bg-white/20 backdrop-blur-sm rounded-lg border border-white/30 flex flex-col items-center justify-center gap-1">
                    <svg class="w-7 h-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" /></svg>
                    <span class="text-[9px] text-white font-bold uppercase">PDF</span>
                  </div>
                  <div v-else class="w-16 h-20 bg-white/20 backdrop-blur-sm rounded-lg border border-white/30 flex flex-col items-center justify-center gap-1">
                    <svg class="w-7 h-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25" /></svg>
                    <span class="text-[9px] text-white font-bold uppercase">Notes</span>
                  </div>
                </div>
                <!-- Tag badge -->
                <span class="absolute top-3 left-3 bg-black/40 backdrop-blur-md text-white text-[10px] font-bold px-2.5 py-1 rounded-lg border border-white/10">
                   {{ rec.average_rating > 4 ? 'Top Rated' : (rec.download_count > 10 ? 'Trending' : 'New Content') }}
                </span>
                <!-- Type badge -->
                <span class="absolute bottom-3 right-3 text-white text-[10px] font-extrabold px-2.5 py-1 rounded-lg" :class="rec.resource_type === 'PAST_PAPER' ? 'bg-red-500/80 backdrop-blur-sm' : 'bg-[#4A90E2]/80 backdrop-blur-sm'">
                  {{ rec.resource_type.replace('_', ' ') }}
                </span>
              </div>
              <!-- Content -->
              <div class="p-4 flex flex-col flex-1">
                <p class="text-[11px] text-slate-400 font-bold uppercase tracking-wider mb-1.5">{{ rec.module_code || 'General' }}</p>
                <h4 class="text-[14px] font-bold text-[#2C3E50] leading-snug mb-3 line-clamp-2 group-hover:text-[#4A90E2] transition-colors">{{ rec.title }}</h4>
                <div class="mt-auto flex items-center gap-2">
                  <div class="w-6 h-6 rounded-full bg-[#4A90E2]/10 flex items-center justify-center text-[#4A90E2] text-[9px] font-bold">
                    {{ (rec.uploader_name || 'U').split(' ').map(n => n[0]).join('').substring(0, 2) }}
                  </div>
                  <span class="text-xs text-slate-500 font-medium">{{ rec.uploader_name }}</span>
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
                      <div class="flex flex-col gap-2">
                        <button
                          v-for="m in modules"
                          :key="m"
                          @click="selectedModule = m"
                          class="px-4 py-3 rounded-xl text-sm font-semibold transition-all border text-left"
                          :class="selectedModule === m ? 'bg-[#4A90E2] text-white border-[#4A90E2] shadow-md' : 'bg-[#F4F7F9] text-[#2C3E50] border-slate-200 hover:border-[#4A90E2]/40 bg-white hover:bg-slate-50'"
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
                class="w-full md:w-[calc(33.33%-16px)] min-w-[280px]"
              >
                <ResourceCard :doc="doc" @preview="openPreview" />
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


    <!-- Resource Preview Slide-Over Panel -->
    <Teleport to="body">
      <Transition name="overlay">
        <div v-if="showPreview" class="fixed inset-0 bg-black/40 backdrop-blur-sm z-[110]" @click="showPreview = false"></div>
      </Transition>
      <Transition name="slide">
        <div v-if="showPreview && selectedResource" class="fixed top-0 right-0 h-full w-[500px] max-w-[95vw] bg-white z-[111] shadow-2xl flex flex-col">
          <!-- Panel Header -->
          <div class="flex items-center justify-between p-6 border-b border-slate-100 shrink-0">
            <div>
              <h2 class="text-xl font-bold text-[#2C3E50]">Resource Preview</h2>
              <p class="text-sm text-slate-400 mt-0.5">Details about this study material</p>
            </div>
            <button @click="showPreview = false" class="w-10 h-10 rounded-xl bg-[#F4F7F9] flex items-center justify-center text-slate-500 hover:text-red-500 hover:bg-red-50 transition-colors">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>

          <!-- Panel Body -->
          <div class="flex-1 overflow-y-auto p-6 space-y-6">
            <!-- Thumbnail -->
            <div class="aspect-video w-full rounded-2xl overflow-hidden shadow-md border border-slate-100">
               <img :src="selectedResource.image || 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'" class="w-full h-full object-cover">
            </div>

            <!-- Title & Type -->
            <div>
              <div class="flex items-center gap-2 mb-2">
                <span class="px-2.5 py-1 bg-[#4A90E2]/10 text-[#4A90E2] text-[10px] font-black uppercase rounded-lg">
                  {{ selectedResource.resource_type?.replace('_', ' ') || 'RESOURCE' }}
                </span>
                <span v-if="selectedResource.module_code" class="px-2.5 py-1 bg-slate-100 text-slate-500 text-[10px] font-black uppercase rounded-lg">
                  {{ selectedResource.module_code }}
                </span>
              </div>
              <div class="flex items-center justify-between">
                <h1 class="text-2xl font-bold text-[#2C3E50] leading-tight">{{ selectedResource.title }}</h1>
              </div>

              <!-- Rating Summary Line -->
              <div class="flex items-center gap-2 mt-2">
                <span class="text-amber-500 font-bold text-lg">{{ ratingStats.average_rating.toFixed(1) }}</span>
                <div class="flex text-amber-400">
                  <span v-for="i in 5" :key="i" class="text-lg">
                    <template v-if="i <= Math.round(ratingStats.average_rating)">★</template>
                    <template v-else>☆</template>
                  </span>
                </div>
                <button 
                  @click="showReviewsModal = true"
                  class="text-slate-400 text-sm font-medium hover:text-[#4A90E2] hover:underline transition-all cursor-pointer"
                >
                  ({{ ratingStats.total_ratings.toLocaleString() }} ratings)
                </button>
              </div>
            </div>

            <!-- Metadata Cards -->
            <div class="grid grid-cols-2 gap-4">
              <div class="p-4 bg-[#F4F7F9] rounded-2xl border border-slate-100">
                <p class="text-[10px] font-bold text-slate-400 uppercase mb-1">Faculty</p>
                <p class="text-sm font-bold text-[#2C3E50]">{{ selectedResource.faculty || 'Not Specified' }}</p>
              </div>
              <div class="p-4 bg-[#F4F7F9] rounded-2xl border border-slate-100">
                <p class="text-[10px] font-bold text-slate-400 uppercase mb-1">Academic Year</p>
                <p class="text-sm font-bold text-[#2C3E50]">{{ selectedResource.academic_year || 'Not Specified' }}</p>
              </div>
              <div class="p-4 bg-[#F4F7F9] rounded-2xl border border-slate-100">
                <p class="text-[10px] font-bold text-slate-400 uppercase mb-1">Stream</p>
                <p class="text-sm font-bold text-[#2C3E50]">{{ selectedResource.academic_stream || 'Not Specified' }}</p>
              </div>
              <div class="p-4 bg-[#F4F7F9] rounded-2xl border border-slate-100">
                <p class="text-[10px] font-bold text-slate-400 uppercase mb-1">Uploaded On</p>
                <p class="text-sm font-bold text-[#2C3E50]">{{ new Date(selectedResource.uploaded_at).toLocaleDateString() }}</p>
              </div>
            </div>

            <!-- Description / Help -->
            <div class="p-5 bg-emerald-50 rounded-2xl border border-emerald-100">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-600 shrink-0">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div>
                  <p class="text-sm font-bold text-emerald-800">Verified Resource</p>
                  <p class="text-xs text-emerald-700 mt-0.5">This resource has been verified for quality and accuracy by the BrightPath academic committee.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel Footer -->
          <div class="p-6 border-t border-slate-100 shrink-0 bg-white">
            <a 
              :href="selectedResource.file" 
              target="_blank"
              @click="handleDownload(selectedResource, $event)"
              class="w-full flex items-center justify-center gap-3 py-4 rounded-2xl bg-[#4A90E2] text-white font-bold hover:bg-[#3A7BC8] transition-all shadow-lg hover:shadow-[#4A90E2]/30 active:scale-[0.98]"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              Download Full Resource
            </a>
            <p class="text-center text-[10px] text-slate-400 mt-4 font-medium uppercase tracking-widest">
              Secured by BrightPath Storage
            </p>
          </div>
        </div>
      </Transition>
    </Teleport>

    <!-- Reviews Modal (Udemy-style) -->
    <Teleport to="body">
      <Transition name="overlay">
        <div v-if="showReviewsModal" class="fixed inset-0 z-[120] pointer-events-none">
          <!-- Dark Backdrop (Only to the left of preview) -->
          <div class="absolute inset-0 bg-black/40 backdrop-blur-sm pointer-events-auto" @click="showReviewsModal = false"></div>
          
          <!-- Modal Sidebar (Anchored to the left of the preview panel) -->
          <div 
            class="absolute top-1/2 -translate-y-1/2 right-[520px] bg-white w-full max-w-4xl max-h-[90vh] rounded-3xl shadow-2xl overflow-hidden flex flex-col pointer-events-auto border border-slate-100"
            @click.stop
          >
            <!-- Close Button -->
            <button @click="showReviewsModal = false" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center hover:bg-red-50 hover:text-red-500 transition-colors z-10">
              ✕
            </button>

            <!-- Modal Header -->
            <div class="p-8 border-b border-slate-100 shrink-0">
              <div class="flex items-center gap-3 text-amber-500 mb-1">
                <span class="text-2xl font-black">★</span>
                <h2 class="text-2xl font-bold text-[#2C3E50]">{{ ratingStats.average_rating.toFixed(1) }} resource rating • {{ ratingStats.total_ratings.toLocaleString() }} ratings</h2>
              </div>
            </div>

            <!-- Modal Body -->
            <div class="flex-1 overflow-y-auto flex flex-col md:flex-row min-h-0">
              <!-- Left: Statistics Sidebar -->
              <div class="w-full md:w-1/3 p-8 bg-slate-50/50 border-r border-slate-100 flex flex-col">
                <h3 class="font-bold text-slate-700 mb-6 uppercase text-xs tracking-widest">Rating Statistics</h3>
                <div class="space-y-4">
                  <div v-for="star in [5, 4, 3, 2, 1]" :key="star" class="flex items-center gap-3 group">
                    <div class="flex-1 h-2 bg-slate-200 rounded-full overflow-hidden">
                      <div 
                        class="h-full bg-slate-500 group-hover:bg-[#4A90E2] transition-all" 
                        :style="{ width: `${ratingStats.total_ratings > 0 ? (ratingStats.distribution[star] / ratingStats.total_ratings * 100) : 0}%` }"
                      ></div>
                    </div>
                    <div class="flex items-center gap-1 w-20 justify-end">
                      <span class="text-amber-500 font-bold text-xs">{{ star }} ★</span>
                      <span class="text-slate-400 text-[10px] font-bold">{{ ratingStats.total_ratings > 0 ? Math.round(ratingStats.distribution[star] / ratingStats.total_ratings * 100) : 0 }}%</span>
                    </div>
                  </div>
                </div>

                <!-- Add Review Action -->
                <div class="mt-auto pt-8">
                  <div v-if="userHasReviewed" class="p-4 bg-emerald-50 rounded-xl border border-emerald-100 text-center">
                    <p class="text-sm font-bold text-emerald-800">You've shared your thoughts!</p>
                    <p class="text-xs text-emerald-600 mt-1">Thank you for your valuable feedback on this resource.</p>
                  </div>
                  <button 
                    v-else
                    @click="showAddReviewForm = !showAddReviewForm"
                    class="w-full py-3 bg-white border-2 border-slate-200 rounded-xl font-bold text-slate-700 hover:border-[#4A90E2] hover:text-[#4A90E2] transition-all flex items-center justify-center gap-2"
                  >
                    {{ showAddReviewForm ? 'Cancel Review' : 'Add Review' }}
                  </button>
                </div>
              </div>

              <!-- Right: Review List & Form -->
              <div class="flex-1 p-8">
                <!-- Search Mock -->
                <div class="relative mb-8">
                   <input type="text" placeholder="Search reviews" class="w-full pl-10 pr-4 py-3 bg-[#F4F7F9] border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#4A90E2]/20 focus:border-[#4A90E2] outline-none text-sm trans">
                   <svg class="absolute left-3 top-3.5 text-slate-400" width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <circle cx="11" cy="11" r="8" stroke-width="2"/>
                      <path d="M21 21l-4.35-4.35" stroke-width="2" stroke-linecap="round"/>
                   </svg>
                </div>

                <!-- Review Form -->
                <transition enter-active-class="transition-all duration-300 overflow-hidden" enter-from-class="max-h-0 opacity-0" enter-to-class="max-h-[500px] opacity-100" leave-active-class="transition-all duration-300 overflow-hidden" leave-from-class="max-h-[500px] opacity-100" leave-to-class="max-h-0 opacity-0">
                  <div v-if="showAddReviewForm" class="mb-8 p-6 bg-[#4A90E2]/5 rounded-2xl border border-[#4A90E2]/10">
                    <h4 class="font-bold text-[#2C3E50] mb-4">Rate this resource</h4>
                    <div class="flex gap-2 mb-6">
                      <button v-for="i in 5" :key="i" @click="newReview.rating = i" class="text-3xl transition-transform active:scale-90" :class="i <= newReview.rating ? 'text-amber-400' : 'text-slate-200'">
                        ★
                      </button>
                    </div>
                    <textarea 
                      v-model="newReview.comment" 
                      placeholder="What did you think of this resource? Your feedback helps other students."
                      class="w-full p-4 bg-white border border-slate-200 rounded-xl h-32 text-sm outline-none focus:border-[#4A90E2] mb-4"
                    ></textarea>
                    <button 
                      @click="submitReview"
                      class="px-8 py-3 bg-[#4A90E2] text-white font-bold rounded-xl shadow-lg hover:bg-[#3A7BC8] transition-all"
                    >
                      Post Review
                    </button>
                  </div>
                </transition>

                <!-- Reviews Feed -->
                <div class="space-y-8">
                  <div v-if="reviewsList.length === 0" class="text-center py-12">
                     <p class="text-slate-400 font-medium italic">No reviews yet. Be the first to share your thoughts!</p>
                  </div>
                  <div v-for="review in reviewsList" :key="review.id" class="flex gap-4 border-b border-slate-100 pb-8 last:border-0">
                    <!-- User Circle -->
                    <div class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center shrink-0 font-bold text-slate-500 uppercase">
                      {{ review.user_name?.substring(0, 2) || '??' }}
                    </div>
                    <div class="flex-1">
                      <div class="flex justify-between items-start mb-2">
                        <div>
                          <p class="font-bold text-[#2C3E50] leading-none mb-1">{{ review.user_name }}</p>
                          <div class="flex items-center gap-2">
                            <div class="flex text-amber-400 text-xs">
                              <span v-for="i in 5" :key="i">{{ i <= review.rating ? '★' : '☆' }}</span>
                            </div>
                            <span class="text-[10px] font-bold text-slate-400 uppercase tracking-tighter">{{ new Date(review.created_at).toLocaleDateString() }}</span>
                          </div>
                        </div>
                      </div>
                      <p class="text-slate-600 text-[0.95rem] leading-relaxed mb-4">
                        {{ review.comment }}
                      </p>
                      <div class="flex items-center gap-4 text-xs font-bold text-slate-400">
                        <span>Helpful?</span>
                        <button class="hover:text-emerald-500 flex items-center gap-1">👍 Yes</button>
                        <button class="hover:text-red-500 flex items-center gap-1">👎 No</button>
                        <button class="ml-auto hover:text-slate-600 underline">Report</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
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
