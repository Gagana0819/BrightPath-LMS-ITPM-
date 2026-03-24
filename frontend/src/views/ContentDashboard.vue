<script setup>
import { ref } from 'vue'
import ResourceList from '../components/ResourceList.vue'
import ResourceUploadModal from '../components/ResourceUploadModal.vue'

// Tab configuration
const tabs = [
  { id: 'videos', name: 'Lecture Videos', icon: 'M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z M21 12a9 9 0 11-18 0 9 9 0 0118 0z' },
  { id: 'notes', name: 'Study Notes', icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
  { id: 'past_papers', name: 'Past Papers', icon: 'M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10' }
]

const activeTab = ref('videos')
const isUploadModalOpen = ref(false)

const setTab = (tabId) => {
  activeTab.value = tabId
}

const openUploadModal = () => {
  isUploadModalOpen.value = true
}

const closeUploadModal = () => {
  isUploadModalOpen.value = false
}
</script>

<template>
  <div class="content-dashboard min-h-screen bg-[#F8FAFC] font-sans text-[#1E293B] pb-20">
    <!-- Premium Header Section -->
    <div class="bg-white border-b border-slate-200 mb-8 sticky top-0 z-30 shadow-sm">
      <div class="container mx-auto px-4 py-8">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
          <div class="animate-in slide-in-from-left duration-700">
            <div class="flex items-center gap-3 mb-2">
              <span class="bg-blue-600 text-white text-[10px] font-bold px-2 py-1 rounded shadow-sm uppercase tracking-tighter">Content Hub</span>
              <span class="text-slate-300">|</span>
              <span class="text-slate-400 text-xs font-semibold">Academic Year 2026</span>
            </div>
            <h1 class="text-4xl font-[900] text-[#0F172A] tracking-tight mb-2">Content & Live <span class="text-blue-600">Integration</span></h1>
            <p class="text-slate-500 font-medium">Manage and deliver high-quality learning resources to your students.</p>
          </div>

          <button 
            @click="openUploadModal"
            class="group bg-[#1E293B] hover:bg-[#0F172A] text-white px-8 py-4 rounded-2xl shadow-xl shadow-slate-200 transition-all active:scale-95 flex items-center font-bold tracking-tight animate-in slide-in-from-right duration-700"
          >
            <div class="w-6 h-6 bg-white/10 rounded-lg flex items-center justify-center mr-3 group-hover:bg-blue-500 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4" />
              </svg>
            </div>
            Publish New Content
          </button>
        </div>

        <!-- Navigation Tabs (Integrated in Header) -->
        <div class="mt-10 overflow-x-auto scrollbar-hide">
          <nav class="flex gap-2 min-w-max pb-1">
            <button
              v-for="tab in tabs"
              :key="tab.id"
              @click="setTab(tab.id)"
              :class="[
                'px-8 py-3 rounded-xl flex items-center transition-all duration-300 font-bold text-[14px] border-2',
                activeTab === tab.id 
                  ? 'bg-white border-blue-600 text-blue-600 shadow-[0_8px_20px_rgba(37,99,235,0.1)] -translate-y-1' 
                  : 'bg-slate-50 border-transparent text-slate-500 hover:bg-white hover:border-slate-200'
              ]"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" :class="activeTab === tab.id ? 'text-blue-600' : 'text-slate-400'" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" :d="tab.icon" />
              </svg>
              {{ tab.name }}
            </button>
          </nav>
        </div>
      </div>
    </div>

    <!-- Content Area -->
    <div class="container mx-auto px-4">
      <div class="content-area min-h-[500px] animate-in fade-in slide-in-from-bottom-4 duration-1000">
        <!-- Resource Lists -->
        <ResourceList v-if="['videos', 'notes', 'past_papers'].includes(activeTab)" :category="activeTab" />
      </div>
    </div>

    <!-- Modals -->
    <ResourceUploadModal 
      v-if="isUploadModalOpen" 
      @close="closeUploadModal" 
    />
  </div>
</template>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
