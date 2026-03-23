<script setup>
import { ref } from 'vue'
import RecommendedGrid from '../components/automation/RecommendedGrid.vue'
import VideoLessonPlayer from '../components/content/VideoLessonPlayer.vue'
import FeedbackModal from '../components/automation/FeedbackModal.vue'

const showFeedback = ref(false)

const triggerFeedback = () => {
  showFeedback.value = true
}

const closeFeedback = () => {
  showFeedback.value = false
}
</script>

<template>
  <div class="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500 pb-12">
    
    <!-- Welcome Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-content tracking-tight mb-1">Welcome back, Kasun! 👋</h1>
        <p class="text-slate-500 font-medium">Here's what's happening with your courses today.</p>
      </div>
      <!-- Test Button for Member 04 Feedback Modal Demo -->
      <button @click="triggerFeedback" class="hidden md:flex bg-white border border-slate-200 text-slate-600 px-4 py-2 rounded-lg text-sm font-bold shadow-sm hover:border-hero-highlight hover:text-hero-highlight transition-all">
        Test Feedback Modal
      </button>
    </div>

    <!-- Member 04: AI Recommendations -->
    <RecommendedGrid />

    <!-- Member 02: Content Player -->
    <div class="pt-6">
      <div class="flex items-center gap-2 mb-4">
        <svg class="w-5 h-5 text-hero-highlight" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h2 class="text-xl font-bold text-content tracking-tight">Continue Learning</h2>
      </div>
      
      <div class="bg-white p-4 lg:p-6 rounded-3xl shadow-sm border border-slate-100">
        <VideoLessonPlayer />
      </div>
    </div>

    <!-- Member 04: Feedback Modal (Hidden by default) -->
    <FeedbackModal :isOpen="showFeedback" resourceName="Advanced DB Architecture Video" @close="closeFeedback" />

  </div>
</template>
