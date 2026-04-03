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
  // Since ResourceList is used in the personal Content Dashboard, we only fetch user's resources
  contentStore.fetchResources({ userOnly: true, category: props.category })
}

const handleDelete = (id) => {
  if (confirm('Are you sure you want to delete this resource?')) {
    contentStore.deleteResource(id)
  }
}

const handleEdit = (resource) => {
  const newTitle = prompt('Enter new title:', resource.title)
  if (newTitle) {
    contentStore.updateResource(resource.id, { title: newTitle })
  }
}

onMounted(() => {
  loadResources()
})

watch(() => props.category, () => {
  loadResources()
})
</script>

<template>
  <div class="resource-list w-full animate-in fade-in duration-700">
    <div v-if="contentStore.isLoading" class="flex flex-col items-center justify-center p-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
      <p class="text-blue-600 font-medium animate-pulse">Loading resources...</p>
    </div>

    <div v-else-if="contentStore.resources.length === 0" class="text-center p-12 bg-white rounded-2xl shadow-sm border border-gray-100">
      <div class="w-16 h-16 bg-gray-50 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
        </svg>
      </div>
      <p class="text-gray-500 text-lg font-medium">No resources found for this category.</p>
      <p class="text-gray-400 text-sm mt-1">Upload your first resource to get started.</p>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div v-for="resource in contentStore.resources" :key="resource.id" 
        class="group flex flex-col bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 overflow-hidden border border-gray-100 hover:-translate-y-1">
        
        <!-- Preview Section -->
        <div class="relative">
          <!-- Video Viewer -->
          <div v-if="resource.category === 'videos'" class="aspect-video bg-slate-900 overflow-hidden">
            <video v-if="resource.url" controls class="w-full h-full object-cover">
              <source :src="resource.url" type="video/mp4">
            </video>
            <div v-else class="flex items-center justify-center h-full text-white/50 flex-col">
              <svg class="h-12 w-12 mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span class="text-xs uppercase tracking-widest font-bold">Video Clip</span>
            </div>
          </div>

          <!-- Notes/Papers Placeholder -->
          <div v-else class="h-40 bg-gradient-to-br from-blue-50 to-indigo-50 flex items-center justify-center relative overflow-hidden">
             <div class="absolute -right-4 -bottom-4 w-24 h-24 bg-blue-100/50 rounded-full blur-2xl"></div>
             <svg v-if="resource.category === 'notes'" xmlns="http://www.w3.org/2000/svg" class="h-20 w-20 text-blue-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-20 w-20 text-indigo-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
            </svg>
            <div class="absolute top-3 right-3">
              <span class="bg-white/80 backdrop-blur-sm text-[10px] font-bold px-2 py-1 rounded-lg border border-white uppercase text-blue-600 shadow-sm">
                {{ resource.category === 'notes' ? 'Notes' : 'Exam PDF' }}
              </span>
            </div>
          </div>

          <!-- CRUD Actions Overlay (Quick access) -->
          <div class="absolute top-3 left-3 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
            <button @click="handleEdit(resource)" class="p-2 bg-white/90 backdrop-blur rounded-lg shadow-sm hover:bg-blue-600 hover:text-white transition-all text-gray-600">
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg>
            </button>
            <button @click="handleDelete(resource.id)" class="p-2 bg-white/90 backdrop-blur rounded-lg shadow-sm hover:bg-red-600 hover:text-white transition-all text-gray-600">
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
            </button>
          </div>
        </div>

        <div class="p-6 flex flex-col flex-1">
          <h3 class="font-bold text-lg text-gray-800 mb-2 leading-tight">{{ resource.title }}</h3>
          <p class="text-sm text-gray-500 mb-6 flex-1 line-clamp-2">{{ resource.description || 'Access and master the core concepts with this structured resource.' }}</p>
          
          <div class="mt-auto pt-4 border-t border-gray-50 flex items-center justify-between">
             <div class="flex items-center text-xs text-gray-400 font-medium">
               <svg class="h-3.5 w-3.5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3" /></svg>
               Added Just Now
             </div>
             <a v-if="resource.category !== 'videos'" :href="resource.url" target="_blank" 
                class="bg-blue-50 text-blue-700 hover:bg-blue-600 hover:text-white px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 shadow-sm border border-blue-100/50">
               <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
               Download
             </a>
             <button v-else class="bg-indigo-50 text-indigo-700 hover:bg-indigo-600 hover:text-white px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 shadow-sm border border-indigo-100/50">
               <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" /></svg>
               Watch
             </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
