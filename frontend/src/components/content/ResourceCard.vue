<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useContentStore } from '@/stores/contentStore'

const props = defineProps({
  doc: {
    type: Object,
    required: true
  },
  allowActions: {
    type: Boolean,
    default: false
  }
})

const router = useRouter()
const emit = defineEmits(['preview', 'edit', 'delete'])
const contentStore = useContentStore()

const isOwner = computed(() => {
  const currentUserId = localStorage.getItem('user_id')
  return currentUserId && String(props.doc.user) === String(currentUserId)
})

const handleEdit = (e) => {
  e.stopPropagation()
  emit('edit', props.doc)
}

const handleDelete = (e) => {
  e.stopPropagation()
  if (confirm(`Are you sure you want to delete "${props.doc.title}"?`)) {
    emit('delete', props.doc.id)
  }
}

const handleDownload = (e) => {
  const isLoggedIn = !!localStorage.getItem('access_token')
  if (!isLoggedIn) {
    e.preventDefault()
    router.push('/login')
    return
  }
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
  const text = (doc.title + ' ' + (doc.module_code || '')).toLowerCase();
  
  if (text.includes('database') || text.includes('sql') || text.includes('dbms') || text.includes('it3020')) return '/database_thumbnail.png';
  if (text.includes('machine learning') || text.includes('ml') || text.includes('ai')) return '/ml_thumbnail.png';
  if (text.includes('itpm') || text.includes('project management') || text.includes('it3030')) return '/itpm_thumbnail.png';
  if (text.includes('oop') || text.includes('java') || text.includes('object oriented')) return '/oop_thumbnail.png';
  if (text.includes('cloud') || text.includes('aws') || text.includes('azure')) return '/cloud_thumbnail.png';
  if (text.includes('data structure') || text.includes('algorithm') || text.includes('it3040')) return '/data_structures_thumbnail.png';
  
  if (doc.resource_type === 'PAST_PAPER') return '/itpm_thumbnail.png';
  if (doc.resource_type === 'SHORT_NOTE') return '/oop_thumbnail.png';
  return '/database-ai-thumbnail.png'; // Distinctive fallback
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString()
}
</script>

<template>
  <div 
    class="bg-white rounded-[24px] overflow-hidden border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group cursor-pointer flex flex-col w-full h-full"
    @click="emit('preview', doc)"
  >
    <!-- Thumbnail Cover -->
    <div class="relative h-[180px] overflow-hidden shrink-0">
      <img :src="getResourceImage(doc)" :alt="doc.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
      
      <!-- Bottom-Left Type Badge -->
      <div class="absolute bottom-4 left-4">
        <span class="bg-[#5C6BC0] text-white text-[11px] font-black px-3 py-1.5 rounded-lg uppercase tracking-wider shadow-lg">
          {{ getFileTypeLabel(doc.resource_type) }}
        </span>
      </div>
      
      <!-- Top-Right Actions (Owner Only + Allowed Context) -->
      <div v-if="isOwner && allowActions" class="absolute top-4 left-4 flex gap-2 z-10">
        <button @click.stop="handleEdit" class="w-9 h-9 bg-white/90 backdrop-blur-md rounded-xl flex items-center justify-center text-slate-700 hover:text-hero-highlight transition-all shadow-md border border-white/30">
          <svg class="w-4 h-4 text-hero-highlight" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
          </svg>
        </button>
        <button @click.stop="handleDelete" class="w-9 h-9 bg-red-500/90 backdrop-blur-md rounded-xl flex items-center justify-center text-white hover:bg-red-600 transition-all shadow-md border border-white/10">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </button>
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
      <div class="flex items-start justify-between mb-1">
        <h3 class="font-bold text-[#1E293B] text-[1.1rem] leading-tight line-clamp-2 group-hover:text-[#5C6BC0] transition-colors">
          {{ doc.title }}
        </h3>
        <span v-if="doc.module_code" class="text-[10px] font-bold text-[#5C6BC0] bg-[#5C6BC0]/10 px-2.5 py-1 rounded-md uppercase shrink-0 ml-3">
          {{ doc.module_code }}
        </span>
      </div>

      <!-- Rating Badges -->
      <div v-if="doc.total_ratings > 0" class="flex items-center gap-1.5 mb-3">
        <div class="flex text-amber-500 text-xs">
          <span>★</span>
        </div>
        <span class="text-[11px] font-bold text-[#1E293B]">{{ (doc.average_rating || 0).toFixed(1) }}</span>
        <span class="text-[10px] font-medium text-slate-400">({{ doc.total_ratings }})</span>
      </div>
      <div v-else class="flex items-center gap-1.5 mb-3 text-[10px] font-medium text-slate-300 italic">
        No ratings yet
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
