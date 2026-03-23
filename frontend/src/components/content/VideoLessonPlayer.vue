<script setup>
import { ref } from 'vue'

const isPlaying = ref(false)
const progress = ref(35) // mock progress
const volume = ref(80) 

const togglePlay = () => {
  isPlaying.value = !isPlaying.value
}
</script>

<template>
  <div class="w-full max-w-5xl mx-auto flex flex-col gap-4 animate-in fade-in slide-in-from-bottom-4 duration-500">
    
    <!-- Player Container -->
    <div class="relative w-full aspect-video bg-black rounded-2xl overflow-hidden shadow-xl group border border-slate-800">
      
      <!-- Mock Video Thumbnail / Content -->
      <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Lesson Thumbnail" class="absolute inset-0 w-full h-full object-cover opacity-60" />

      <!-- Center Play Button (Large) -->
      <button v-if="!isPlaying" @click="togglePlay" class="absolute inset-0 flex items-center justify-center bg-black/20 group-hover:bg-black/40 transition-all z-10 text-white">
        <div class="w-20 h-20 bg-hero-highlight/90 backdrop-blur rounded-full flex items-center justify-center shadow-lg hover:scale-110 transition-transform">
          <svg class="w-10 h-10 ml-1" fill="currentColor" viewBox="0 0 24 24">
            <path d="M8 5v14l11-7z" />
          </svg>
        </div>
      </button>

      <!-- Bottom Controls Bar -->
      <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black/80 to-transparent p-4 md:p-6 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end z-20">
        
        <!-- Progress Bar -->
        <div class="w-full h-1.5 bg-white/30 rounded-full mb-4 cursor-pointer relative">
          <div class="absolute top-0 left-0 h-full bg-hero-highlight rounded-full relative" :style="`width: ${progress}%`">
            <div class="absolute right-0 top-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full shadow translate-x-1.5 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </div>
        </div>

        <!-- Controls -->
        <div class="flex items-center justify-between text-white">
          <div class="flex items-center gap-4 md:gap-6">
            <button @click="togglePlay" class="hover:text-hero-highlight transition-colors">
              <svg v-if="isPlaying" class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24">
                <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z" />
              </svg>
              <svg v-else class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8 5v14l11-7z" />
              </svg>
            </button>
            <button class="hover:text-hero-highlight transition-colors hidden sm:block">
              <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
              </svg>
            </button>
            <span class="text-sm font-medium tracking-wide">14:05 / 45:30</span>
          </div>

          <div class="flex items-center gap-4 md:gap-6">
            <button class="hover:text-hero-highlight transition-colors flex items-center gap-1 font-semibold text-sm">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              <span class="hidden md:block">1080p</span>
            </button>
            <button class="hover:text-hero-highlight transition-colors">
              <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Metadata Section -->
    <div class="px-2 pt-2">
      <div class="flex items-start justify-between">
        <div>
          <h1 class="text-2xl font-bold text-content tracking-tight mb-2">Advanced Database Architecture - Lecture 04</h1>
          <div class="flex items-center gap-3 text-slate-500 text-sm">
            <span class="inline-flex items-center gap-1.5 font-medium text-hero-highlight bg-hero-highlight/10 px-2.5 py-1 rounded-md">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Updated 2 days ago
            </span>
            <span>•</span>
            <span class="font-medium">Module: IT3040</span>
          </div>
        </div>
        <button class="hidden md:flex items-center gap-2 px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-lg transition-colors">
          <svg class="w-5 h-5 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
          </svg>
          Save
        </button>
      </div>
    </div>
  </div>
</template>
