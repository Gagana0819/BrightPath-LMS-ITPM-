<script setup>
import { ref } from 'vue'

const recommendations = ref([
  { id: 1, title: 'Machine Learning Masterclass', author: 'Dr. Fernando', tag: 'AI & Data', match: '98%', image: 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80' },
  { id: 2, title: 'Advanced React Patterns', author: 'Nuwan S.', tag: 'Web Dev', match: '92%', image: 'https://images.unsplash.com/photo-1633356122544-f134324a6cee?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80' },
  { id: 3, title: 'Project Management Essentials', author: 'Prof. Wijesekera', tag: 'IT PM', match: '85%', image: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80' }
])
</script>

<template>
  <div class="space-y-4">
    <div class="flex items-center justify-between mb-2">
      <div class="flex items-center gap-2">
        <svg class="w-5 h-5 text-hero-highlight" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
        </svg>
        <h2 class="text-xl font-bold text-content tracking-tight">AI Recommended For You</h2>
      </div>
      <a href="#" class="text-sm font-bold text-hero-highlight hover:underline">View Engine</a>
    </div>

    <!-- Horizontal Scrollable Grid -->
    <div class="flex gap-4 overflow-x-auto pb-4 snap-x hide-scrollbars">
      
      <div 
        v-for="course in recommendations" 
        :key="course.id"
        class="min-w-[280px] md:min-w-[320px] bg-white border border-slate-100 rounded-2xl p-4 shadow-sm hover:shadow-lg transition-all duration-300 group cursor-pointer snap-start relative overflow-hidden"
      >
        <!-- The Match Highlight -->
        <div class="absolute top-0 right-0 bg-green-500 text-white text-[0.7rem] font-bold px-3 py-1 rounded-bl-xl z-10 shadow-sm border-b border-l border-green-600">
          {{ course.match }} Match
        </div>

        <div class="w-full h-32 bg-slate-100 rounded-xl overflow-hidden mb-4 relative">
          <img :src="course.image" :alt="course.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors"></div>
        </div>

        <span class="inline-block px-2.5 py-1 bg-slate-100 text-slate-600 rounded-lg text-xs font-bold tracking-wide mb-2 uppercase">{{ course.tag }}</span>
        
        <h3 class="font-bold text-content leading-snug mb-1 group-hover:text-hero-highlight transition-colors">{{ course.title }}</h3>
        <p class="text-sm text-slate-500 font-medium mb-4">By {{ course.author }}</p>

        <button class="w-full py-2 bg-slate-50 border border-slate-200 text-hero-highlight font-bold rounded-xl group-hover:bg-hero-highlight group-hover:text-white transition-all overflow-hidden flex items-center justify-center gap-2">
          Start Module
          <svg class="w-4 h-4 translate-x-0 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3" />
          </svg>
        </button>
      </div>

    </div>
  </div>
</template>

<style scoped>
.hide-scrollbars::-webkit-scrollbar {
  display: none;
}
.hide-scrollbars {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
