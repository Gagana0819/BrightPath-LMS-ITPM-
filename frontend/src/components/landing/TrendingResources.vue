<script setup>
import { ref, computed, reactive, watch } from 'vue'
import { useContentStore } from '@/stores/contentStore'
import ResourceCard from '../content/ResourceCard.vue'

const contentStore = useContentStore()
const isLoggedIn = computed(() => !!localStorage.getItem('access_token'))

// Filter Logic
const showFilters = ref(false)
const filterErrors = reactive({ module_code: '' })
const filters = reactive({
  module_code: '',
  year: ''
})

const yearOptions = [
  'year 1/1', 'year 1/2', 
  'year 2/1', 'year 2/2', 
  'year 3/1', 'year 3/2', 
  'year 4/1', 'year 4/2'
]

const validateModuleId = (val) => {
  if (!val) {
    filterErrors.module_code = ''
    return true
  }
  const regex = /^[A-Za-z]{2}\d{4}$/
  if (!regex.test(val)) {
    filterErrors.module_code = 'ID must be 2 letters + 4 numbers (e.g. IT3050)'
    return false
  }
  filterErrors.module_code = ''
  return true
}

const applyFilters = () => {
  if (validateModuleId(filters.module_code)) {
    contentStore.fetchRecommendations({
      module_code: filters.module_code,
      year: filters.year
    })
  }
}

const clearFilters = () => {
  filters.module_code = ''
  filters.year = ''
  filterErrors.module_code = ''
  contentStore.fetchRecommendations()
}

// Auto-apply filters on change
let debounceTimer = null
watch(filters, (newVal) => {
  if (debounceTimer) clearTimeout(debounceTimer)
  
  // For year, apply immediately
  // For module_code, apply only if valid after a short debounce
  debounceTimer = setTimeout(() => {
    if (validateModuleId(newVal.module_code)) {
      applyFilters()
    }
  }, 500)
}, { deep: true })

// Scroll Logic
const resScrollRef = ref(null)
const resCanScrollLeft = ref(false)
const resCanScrollRight = ref(true)

const updateResScroll = () => {
  const el = resScrollRef.value
  if (!el) return
  resCanScrollLeft.value = el.scrollLeft > 10
  resCanScrollRight.value = el.scrollLeft < el.scrollWidth - el.clientWidth - 10
}

const scrollRes = (dir) => {
  const el = resScrollRef.value
  if (!el) return
  el.scrollBy({ left: dir === 'left' ? -350 : 350, behavior: 'smooth' })
  setTimeout(updateResScroll, 350)
}
</script>

<template>
  <section v-if="isLoggedIn" class="py-24 bg-slate-50 relative overflow-hidden px-4 sm:px-8 lg:px-20 border-y border-slate-100">
    <!-- Abstract Decoration -->
    <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-blue-50/50 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/2 -z-0"></div>
    <div class="absolute bottom-0 left-0 w-[400px] h-[400px] bg-indigo-50/50 rounded-full blur-[100px] translate-y-1/2 -translate-x-1/2 -z-0"></div>

    <div class="max-w-[1200px] mx-auto w-full z-10 relative">
      <!-- Header -->
      <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
        <div class="space-y-4">
          <div class="inline-flex items-center gap-2 px-3 py-1 bg-blue-600/10 text-blue-600 rounded-full text-[10px] font-black uppercase tracking-widest border border-blue-600/20">
            For You
          </div>
          <div class="flex items-center gap-4">
            <h2 class="text-3xl md:text-5xl font-black text-[#2C3E50] tracking-tighter">Recommended <span class="text-[#4A90E2]">Resources</span></h2>
            
            <!-- Dynamic Filter Trigger -->
            <button 
              @click="showFilters = !showFilters" 
              :class="[
                'p-3 rounded-2xl border-2 transition-all flex items-center gap-2 group',
                showFilters ? 'bg-[#4A90E2] border-[#4A90E2] text-white shadow-lg' : 'bg-white border-slate-100 text-slate-400 hover:border-[#4A90E2] hover:text-[#4A90E2]'
              ]"
            >
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
              </svg>
              <span class="text-xs font-black uppercase tracking-widest hidden sm:inline">Filter</span>
            </button>
          </div>
          <p class="text-slate-500 font-medium text-lg max-w-[600px] leading-relaxed">
            Personalized learning materials curated precisely for your academic stream and current year.
          </p>
        </div>
        
        <div class="flex items-center gap-4">
          <!-- Scroll Buttons -->
          <div class="flex items-center gap-2 mr-4">
            <button @click="scrollRes('left')" :disabled="!resCanScrollLeft" class="w-10 h-10 rounded-full bg-white border border-slate-100 flex items-center justify-center text-slate-400 hover:text-[#4A90E2] hover:border-[#4A90E2] hover:shadow-lg transition-all shadow-sm disabled:opacity-20 disabled:scale-95">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
            </button>
            <button @click="scrollRes('right')" :disabled="!resCanScrollRight" class="w-10 h-10 rounded-full bg-white border border-slate-100 flex items-center justify-center text-slate-400 hover:text-[#4A90E2] hover:border-[#4A90E2] hover:shadow-lg transition-all shadow-sm disabled:opacity-20 disabled:scale-95">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" /></svg>
            </button>
          </div>

          <router-link to="/digital-library" class="group relative px-6 py-3 bg-white text-[#2C3E50] rounded-xl font-bold text-sm border border-slate-200 shadow-sm transition-all hover:shadow-xl hover:-translate-y-1 flex items-center gap-2 overflow-hidden">
            <span class="relative z-10 flex items-center gap-2">
              Explore All 
              <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </span>
          </router-link>
        </div>
      </div>

      <!-- Expandable Filter Bar -->
      <transition 
        enter-active-class="transition duration-300 ease-out" 
        enter-from-class="transform -translate-y-4 opacity-0" 
        enter-to-class="transform translate-y-0 opacity-100" 
        leave-active-class="transition duration-200 ease-in" 
        leave-from-class="transform translate-y-0 opacity-100" 
        leave-to-class="transform -translate-y-4 opacity-0"
      >
        <div v-if="showFilters" class="mb-10 p-6 bg-white/60 backdrop-blur-xl rounded-[2.5rem] border border-white shadow-xl grid grid-cols-1 md:grid-cols-12 gap-6 items-end">
          <div class="md:col-span-5 space-y-2">
            <label class="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] ml-2">Module ID</label>
            <div class="relative">
              <input 
                v-model="filters.module_code" 
                @input="validateModuleId(filters.module_code)"
                type="text" 
                placeholder="Ex: IT3050" 
                :class="[
                  'w-full px-6 py-4 bg-white border-2 rounded-2xl outline-none transition-all font-bold text-slate-700',
                  filterErrors.module_code ? 'border-red-200 focus:border-red-400' : 'border-transparent focus:border-[#4A90E2] shadow-sm'
                ]"
              />
              <p v-if="filterErrors.module_code" class="absolute -bottom-6 left-2 text-[10px] font-bold text-red-500 uppercase">{{ filterErrors.module_code }}</p>
            </div>
          </div>

          <div class="md:col-span-4 space-y-2">
            <label class="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] ml-2">Academic Year</label>
            <select v-model="filters.year" class="w-full px-6 py-4 bg-white border-2 border-transparent rounded-2xl outline-none focus:border-[#4A90E2] font-bold text-slate-700 shadow-sm appearance-none cursor-pointer">
              <option value="">All Years</option>
              <option v-for="year in yearOptions" :key="year" :value="year">{{ year }}</option>
            </select>
          </div>

          <div class="md:col-span-3 flex gap-3">
            <button @click="applyFilters" class="flex-1 bg-slate-900 text-white py-4 rounded-2xl font-black text-[11px] uppercase tracking-widest hover:bg-black active:scale-95 transition-all shadow-lg">Apply</button>
            <button @click="clearFilters" class="px-6 bg-white border border-slate-200 text-slate-500 py-4 rounded-2xl font-black text-[11px] uppercase tracking-widest hover:bg-slate-50 active:scale-95 transition-all shadow-sm">Reset</button>
          </div>
        </div>
      </transition>

      <!-- Recommendation Carousel -->
      <div v-if="contentStore.recommendedResources.length > 0" class="relative">
        <div 
          ref="resScrollRef" 
          @scroll="updateResScroll"
          class="flex gap-6 lg:gap-8 overflow-x-auto pb-8 scroll-smooth hide-scrollbar"
        >
          <ResourceCard 
            v-for="res in contentStore.recommendedResources" 
            :key="res.id" 
            :doc="res" 
            class="min-w-[280px] max-w-[280px] hover:shadow-2xl transition-all duration-500"
          />
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="bg-white rounded-[2rem] p-16 text-center border-2 border-dashed border-slate-200 shadow-sm">
        <div class="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center mx-auto mb-6 text-slate-300">
          <svg class="w-10 h-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 21v-8.25M15.75 21v-8.25M8.25 21v-8.25M3 9l9-6 9 6m-1.5 12V10.332A48.36 48.36 0 0012 9.75c-2.551 0-5.056.2-7.5.582V21M3 21h18M12 6.75h.008v.008H12V6.75z" />
          </svg>
        </div>
        <h3 class="text-xl font-bold text-slate-900 mb-2">No recommendations ready yet</h3>
        <p class="text-slate-500 max-w-sm mx-auto">Complete your profile or explore the library to help us find the best resources for you.</p>
      </div>

    </div>
  </section>
</template>

<style scoped>
.hide-scrollbar {
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
</style>

<style scoped>
.animate-pulse-slow {
  animation: pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.8; }
}
</style>
