<script setup>
import { ref } from 'vue'
import ResourceList from '../components/ResourceList.vue'
import ResourceUploadModal from '../components/ResourceUploadModal.vue'

// Tab configuration
const tabs = [
  { id: 'videos', name: 'Lecture Videos', icon: 'M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z M21 12a9 9 0 11-18 0 9 9 0 0118 0z' },
  { id: 'notes', name: 'Notes', icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
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
  <div class="content-dashboard container mx-auto px-4 py-6 font-sans text-content">
    <!-- Header Section -->
    <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
      <div>
        <h1 class="text-3xl font-bold mb-2">Content & Live Integration</h1>
        <p class="text-gray-500">Manage your learning resources and live sessions seamlessly.</p>
      </div>

      <button 
        @click="openUploadModal"
        class="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2.5 rounded-lg shadow-md transition flex items-center font-medium"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Upload Resource
      </button>
    </div>

    <!-- Navigation Tabs -->
    <div class="bg-white rounded-lg shadow-sm mb-8 border border-gray-100 overflow-x-auto">
      <nav class="flex divide-x divide-gray-100 w-full min-w-max">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="setTab(tab.id)"
          :class="[
            'flex-1 py-4 px-6 flex items-center justify-center transition-colors font-medium border-b-2 outline-none',
            activeTab === tab.id 
              ? 'bg-blue-50 text-blue-700 border-blue-600' 
              : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900 border-transparent'
          ]"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" :class="activeTab === tab.id ? 'text-blue-600' : 'text-gray-400'" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="tab.icon" />
          </svg>
          {{ tab.name }}
        </button>
      </nav>
    </div>

    <div class="content-area min-h-[400px]">
      <!-- Resource Lists -->
      <ResourceList v-if="activeTab === 'videos' || activeTab === 'notes' || activeTab === 'past_papers'" :category="activeTab" />
    </div>

    <!-- Modals -->
    <ResourceUploadModal 
      v-if="isUploadModalOpen" 
      @close="closeUploadModal" 
    />
  </div>
</template>
