<script setup>
import { ref, computed, onMounted } from 'vue'
import { useContentStore } from '@/stores/contentStore'
import ResourceCard from '@/components/content/ResourceCard.vue'

const props = defineProps({
  searchQuery: {
    type: String,
    default: ''
  },
  userOnly: {
    type: Boolean,
    default: false
  }
})

const contentStore = useContentStore()

onMounted(() => {
  // DocumentGrid is used in both the public Digital Library (userOnly=false) and Dashboard (userOnly=true)
  contentStore.fetchResources({ userOnly: props.userOnly })
})

const sortBy = ref('recent') 

const filteredDocuments = computed(() => {
  const q = props.searchQuery.toLowerCase().trim()
  // Combine real resources with some mock ones if store is empty (optional, but better to just use real)
  let result = [...contentStore.resources]

  if (q) {
    result = result.filter(doc =>
      doc.title.toLowerCase().includes(q) ||
      doc.module_code.toLowerCase().includes(q) ||
      doc.resource_type.toLowerCase().includes(q)
    )
  }

  // Sorting logic
  if (sortBy.value === 'recent') {
    result.sort((a, b) => new Date(b.uploaded_at) - new Date(a.uploaded_at))
  }

  return result
})
</script>

<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between w-full">
      <h2 class="text-3xl font-extrabold text-content pl-16">Community Resources</h2>
      <div class="flex gap-2">
        <select 
          v-model="sortBy"
          class="bg-white border border-slate-200 text-sm rounded-lg px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-hero-highlight/20 font-medium cursor-pointer"
        >
          <option value="recent">Most Recent</option>
          <option value="rating">Highest Rated</option>
        </select>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="contentStore.isLoading" class="flex flex-col items-center justify-center py-20 animate-pulse">
      <div class="w-12 h-12 border-4 border-hero-highlight border-t-transparent rounded-full animate-spin mb-4"></div>
      <p class="text-slate-500 font-medium font-outfit uppercase tracking-widest text-sm">Fetching real resources...</p>
    </div>

    <!-- Empty State -->
    <div v-else-if="filteredDocuments.length === 0" class="text-center py-20 bg-slate-50 rounded-3xl border border-dashed border-slate-200">
      <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mx-auto mb-4 shadow-sm">
        <svg class="w-10 h-10 text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
      </div>
      <h3 class="text-lg font-bold text-slate-700">No resources found</h3>
      <p class="text-slate-500 px-10">Try a different search query or be the first to upload a resource for this module!</p>
    </div>

    <!-- Grid -->
    <div v-else class="flex flex-wrap justify-start gap-6 pl-16">
      
      <div 
        v-for="doc in filteredDocuments" 
        :key="doc.id"
        class="w-full md:w-[calc(33.33%-16px)] min-w-[280px]"
      >
        <ResourceCard :doc="doc" />
      </div>

    </div>
  </div>
</template>
