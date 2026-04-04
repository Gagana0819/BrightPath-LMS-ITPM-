<script setup>
import { computed } from 'vue'
import { useContentStore } from '@/stores/contentStore'

const props = defineProps({
  doc: {
    type: Object,
    required: true
  }
})

const contentStore = useContentStore()

const handleDownload = () => {
  contentStore.recordResourceDownload(props.doc.id)
}

const getFileTypeLabel = (resourceType) => {
  const types = {
    'LECTURE_NOTES': 'LECTURE NOTES',
    'PAST_PAPER': 'PAST PAPER',
    'TUTORIAL_ANSWER': 'TUTORIAL ANSWER',
    'SHORT_NOTE': 'SHORT NOTE'
  }
  return types[resourceType] || 'FILE'
}

const getResourceImage = (doc) => {
  if (doc.resource_type === 'PAST_PAPER') return 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
  if (doc.resource_type === 'LECTURE_NOTES') return 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
  if (doc.resource_type === 'SHORT_NOTE') return 'https://images.unsplash.com/photo-1517842645767-c639042777db?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
  return 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80'
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString()
}
</script>

<template>
  <div class="bg-white rounded-[24px] overflow-hidden border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group cursor-pointer flex flex-col w-full h-full">
    <!-- Thumbnail Cover -->
    <div class="relative h-[180px] overflow-hidden shrink-0">
      <img :src="getResourceImage(doc)" :alt="doc.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
      
      <!-- Bottom-Left Type Badge -->
      <div class="absolute bottom-4 left-4">
        <span class="bg-[#5C6BC0] text-white text-[11px] font-black px-3 py-1.5 rounded-lg uppercase tracking-wider shadow-lg">
          {{ getFileTypeLabel(doc.resource_type) }}
        </span>
      </div>
      
      <!-- Top-Right Download Button -->
      <a :href="doc.file" target="_blank" @click.stop="handleDownload" class="absolute top-4 right-4 w-11 h-11 bg-white/20 hover:bg-white/90 backdrop-blur-md rounded-full flex items-center justify-center text-white hover:text-[#5C6BC0] transition-all shadow-lg border border-white/30">
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
      </a>
      
      <!-- Bottom Overlay Gradient (to make text readable) -->
      <div class="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-black/40 to-transparent pointer-events-none"></div>
    </div>

    <!-- Meta Details -->
    <div class="p-6 flex flex-col flex-1">
      <div class="flex items-start justify-between mb-3">
        <h3 class="font-bold text-[#1E293B] text-[1.1rem] leading-tight line-clamp-2 group-hover:text-[#5C6BC0] transition-colors">
          {{ doc.title }}
        </h3>
        <span v-if="doc.module_code" class="text-[10px] font-bold text-[#5C6BC0] bg-[#5C6BC0]/10 px-2.5 py-1 rounded-md uppercase shrink-0 ml-3">
          {{ doc.module_code }}
        </span>
      </div>

      <!-- Faculty and Year Badges -->
      <div v-if="doc.faculty || doc.academic_year || doc.academic_stream" class="flex flex-wrap gap-2 mb-4">
        <span v-if="doc.faculty" class="text-[9px] font-black text-blue-600 bg-blue-50 px-2 py-1 rounded uppercase tracking-tighter border border-blue-100">
          {{ doc.faculty }}
        </span>
        <span v-if="doc.academic_stream" class="text-[9px] font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded uppercase tracking-tighter border border-emerald-100">
          {{ doc.academic_stream }}
        </span>
        <span v-if="doc.academic_year" class="text-[9px] font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded uppercase tracking-tighter border border-amber-100">
          {{ doc.academic_year }}
        </span>
      </div>
      
      <div class="flex items-center text-slate-400 text-xs font-medium mb-5">
        <svg class="w-4 h-4 mr-2 opacity-60" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
        </svg>
        Uploaded on {{ formatDate(doc.uploaded_at) }}
      </div>

      <div class="mt-auto flex items-center justify-between">
        <!-- Verified Badge -->
        <div class="inline-flex items-center px-4 py-1.5 rounded-full text-[11px] font-bold border border-slate-100 bg-[#F8FAFC] text-slate-500 shadow-sm">
          Verified Resource
        </div>

        <div class="flex items-center gap-1.5 font-bold text-slate-400 text-[11px]">
          <span>Public Access</span>
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
