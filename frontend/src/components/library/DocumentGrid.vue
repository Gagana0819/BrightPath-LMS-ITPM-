<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  searchQuery: {
    type: String,
    default: ''
  }
})

const documents = ref([
  { id: 1, title: 'Object-Oriented Programming Notes', uploader: 'Dr. Amanda', rank: 'Gold', score: 98, type: 'PDF', image: 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', date: '2026-03-24T10:00:00Z' },
  { id: 2, title: 'Database Systems SQL Joins', uploader: 'Kasun S.', rank: 'Silver', score: 85, type: 'DOCX', image: 'https://images.unsplash.com/photo-1606326608606-aa0b62935f2b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', date: '2026-03-23T15:30:00Z' },
  { id: 3, title: 'ITPM Midterm Review 2026', uploader: 'Prof. Wijesekera', rank: 'Gold', score: 95, type: 'PDF', image: 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', date: '2026-03-22T09:15:00Z' },
  { id: 4, title: 'Data Structures Tree Algorithms', uploader: 'Nuwan S.', rank: 'Bronze', score: 65, type: 'PDF', image: 'https://images.unsplash.com/photo-1517842645767-c639042777db?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', date: '2026-03-21T18:45:00Z' },
  { id: 5, title: 'UI/UX Design Wireframes', uploader: 'Sanduni S.', rank: 'Gold', score: 92, type: 'PDF', image: '/assets/ui_ux_wireframes.png', date: '2026-03-20T14:20:00Z' },
  { id: 6, title: 'Machine Learning Basics', uploader: 'Dr. Fernando', rank: 'Silver', score: 78, type: 'PDF', image: 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80', date: '2026-03-19T11:05:00Z' }
])

const sortBy = ref('rating') // default to highest rated

const getRankColor = (rank) => {
  if (rank === 'Gold') return 'text-[#FFB800] bg-[#FFB800]/10 border-[#FFB800]'
  if (rank === 'Silver') return 'text-slate-500 bg-slate-100 border-slate-300'
  if (rank === 'Bronze') return 'text-amber-700 bg-amber-50 border-amber-200'
  return 'text-slate-500 bg-slate-100 border-slate-200'
}

const filteredDocuments = computed(() => {
  const q = props.searchQuery.toLowerCase().trim()
  let result = documents.value

  if (q) {
    result = result.filter(doc =>
      doc.title.toLowerCase().includes(q) ||
      doc.uploader.toLowerCase().includes(q) ||
      doc.type.toLowerCase().includes(q)
    )
  }

  // Sorting logic
  if (sortBy.value === 'rating') {
    result.sort((a, b) => b.score - a.score)
  } else if (sortBy.value === 'recent') {
    result.sort((a, b) => new Date(b.date) - new Date(a.date))
  }

  return result
})
</script>

<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <h2 class="text-2xl font-bold text-content">Community Resources</h2>
      <div class="flex gap-2">
        <select 
          v-model="sortBy"
          class="bg-white border border-slate-200 text-sm rounded-lg px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-hero-highlight/20 font-medium cursor-pointer"
        >
          <option value="rating">Highest Rated (Gold)</option>
          <option value="recent">Most Recent</option>
          <option value="dept">My Department</option>
        </select>
      </div>
    </div>

    <!-- Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      
      <div 
        v-for="doc in filteredDocuments" 
        :key="doc.id"
        class="bg-white rounded-2xl overflow-hidden border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group cursor-pointer flex flex-col"
      >
        <!-- Thumbnail Cover -->
        <div class="relative h-[160px] bg-slate-100 overflow-hidden shrink-0">
          <img :src="doc.image" :alt="doc.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          
          <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-90"></div>
          
          <div class="absolute bottom-3 left-3 text-white font-semibold text-sm tracking-wide bg-black/40 backdrop-blur px-2.5 py-1 rounded-md">
            {{ doc.type }}
          </div>
          
          <button class="absolute top-3 right-3 w-8 h-8 bg-white/20 hover:bg-white/40 backdrop-blur rounded-full flex items-center justify-center text-white transition-colors">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
            </svg>
          </button>
        </div>

        <!-- Meta -->
        <div class="p-5 flex flex-col flex-1">
          <h3 class="font-bold text-content text-[1.05rem] leading-tight mb-2 line-clamp-2 group-hover:text-hero-highlight transition-colors">{{ doc.title }}</h3>
          
          <p class="text-sm font-medium text-slate-500 mb-4">By {{ doc.uploader }}</p>

          <div class="mt-auto flex items-center justify-between">
            <!-- Quality Badge -->
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border" :class="getRankColor(doc.rank)">
              <svg v-if="doc.rank === 'Gold'" class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
              </svg>
              {{ doc.rank }} Rank
            </div>

            <div class="flex items-center gap-1 font-bold text-slate-700 text-sm">
              <span :class="doc.rank === 'Gold' ? 'text-[#FFB800]' : ''">{{ doc.score }}%</span>
              <svg class="w-4 h-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
              </svg>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
