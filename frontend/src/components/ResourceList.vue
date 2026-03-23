<script setup>
import { onMounted, watch } from 'vue'
import { useContentStore } from '../stores/contentStore'

const props = defineProps({
  category: {
    type: String,
    required: true
  }
})

const contentStore = useContentStore()

const loadResources = () => {
  contentStore.fetchResources(props.category)
}

onMounted(() => {
  loadResources()
})

watch(() => props.category, () => {
  loadResources()
})
</script>

<template>
  <div class="resource-list w-full">
    <div v-if="contentStore.isLoading" class="flex justify-center p-8">
      <div class="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600"></div>
    </div>

    <div v-else-if="contentStore.resources.length === 0" class="text-center p-8 text-gray-500 bg-white rounded-lg shadow-sm">
      <p>No resources found for this category. Click 'Upload Resource' to add some.</p>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="resource in contentStore.resources" :key="resource.id" class="flex flex-col bg-white rounded-lg shadow hover:shadow-md transition overflow-hidden">
        
        <!-- Video Viewer -->
        <div v-if="resource.category === 'videos'" class="aspect-video bg-gray-900 border-b relative">
          <!-- Using a simple video tag for this mockup. Real app might use an embedded player for S3/YouTube -->
          <video v-if="resource.url" controls class="w-full h-full object-cover">
            <source :src="resource.url" type="video/mp4">
            Your browser does not support the video tag.
          </video>
          <div v-else class="flex items-center justify-center h-full text-white pb-2 flex-col">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-2 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>Video Placeholder</span>
          </div>
        </div>

        <!-- Document Viewer (Notes / Past Papers) -->
        <div v-else class="h-32 bg-gray-100 border-b flex items-center justify-center text-gray-400">
           <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
        </div>

        <div class="p-4 flex flex-col flex-1">
          <h3 class="font-bold text-lg text-gray-800 mb-1 truncate">{{ resource.title }}</h3>
          <p class="text-sm text-gray-500 mb-4 flex-1">{{ resource.description || 'No description provided.' }}</p>
          
          <div class="mt-auto pt-3 border-t flex justify-end">
            <!-- Download / View Button -->
             <a v-if="resource.category !== 'videos'" :href="resource.url" target="_blank" class="text-blue-600 hover:text-blue-800 text-sm font-medium flex items-center transition">
               <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
               Download / View
             </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
