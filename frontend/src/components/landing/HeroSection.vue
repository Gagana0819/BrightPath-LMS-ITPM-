<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import StatsBanner from './StatsBanner.vue'

const slides = [
  {
    image: '/digital library.png',
    title: 'Illuminate Your <br><span class="text-blue-600">Academic Path</span><br> Together.',
    description: 'The comprehensive web-based LMS designed exclusively for university students. Master your curriculum with a curated community of experts and peers.'
  },
  {
    image: '/gmail notify.png',
    title: 'Never Miss a <br><span class="text-blue-600">Critical Update</span><br> Again.',
    description: 'Get real-time notifications directly in your university inbox when new lecture notes, past papers, or exam schedules are uploaded.'
  },
  {
    image: '/kuppi session.png',
    title: 'Interactive Live <br><span class="text-blue-600">Kuppi Sessions</span>.',
    description: 'Join peer-led live tutoring sessions to clarify doubts, discuss past papers, and prepare for finals collaboratively with your batchmates.'
  }
]

const currentSlide = ref(0)
let slideInterval

onMounted(() => {
  slideInterval = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
})

onUnmounted(() => {
  clearInterval(slideInterval)
})
</script>

<template>
  <section class="hero-section relative w-full overflow-hidden bg-[#F8FAFC]">
    <!-- Background Image Layer (Subtle Gradient/Texture) -->
    <div class="absolute inset-0 w-full h-full z-0 opacity-100">
      <img src="/hero BG.png" alt="Hero background mix" class="w-full h-full object-cover" />
    </div>

    <!-- Main Content Area -->
    <div class="relative z-10 max-w-[1400px] mx-auto px-4 sm:px-8 lg:px-12 w-full h-full flex flex-col lg:flex-row items-center pt-0 lg:pt-10">
      
      <!-- Left Text Content -->
      <div class="w-full lg:w-1/2 flex flex-col justify-center relative z-20 mb-12 lg:mb-0">
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-100 text-blue-700 text-xs font-black uppercase tracking-widest w-max mb-8 shadow-sm">
          UNIVERSITY NETWORK
        </div>
         
        <div class="relative h-[200px] sm:h-[220px] lg:h-[260px] w-full">
          <transition name="fade" mode="out-in">
            <div :key="currentSlide" class="absolute inset-0 w-full flex flex-col justify-start">
              <h1 class="text-[2.8rem] sm:text-5xl lg:text-6xl font-extrabold text-slate-900 leading-[1.15] mb-6 tracking-tight" v-html="slides[currentSlide].title"></h1>
              <p class="text-lg text-slate-600 font-medium leading-relaxed max-w-[550px]">
                {{ slides[currentSlide].description }}
              </p>
            </div>
          </transition>
        </div>
         
        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4 mt-6">
          <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3.5 px-8 rounded-lg transition-all shadow-md hover:shadow-lg flex items-center gap-2 w-full sm:w-auto justify-center">
            Join for Free
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
          <button class="bg-white border-2 border-blue-100 text-blue-600 hover:border-blue-600 hover:bg-blue-50 font-bold py-3.5 px-8 rounded-lg transition-colors w-full sm:w-auto justify-center">
            Browse Resources
          </button>
        </div>
         
        <!-- Slide Indicators -->
        <div class="flex items-center gap-3 mt-12">
          <button v-for="(_, index) in slides" :key="'indicator-'+index" @click="currentSlide = index"
            class="h-2 rounded-full transition-all duration-500 ease-out"
            :class="currentSlide === index ? 'w-10 bg-blue-600' : 'w-2 bg-slate-300 hover:bg-slate-400'">
          </button>
        </div>
      </div>

      <!-- Right Visual Content -->
      <div class="w-full lg:w-1/2 relative flex items-end justify-center mt-8 lg:mt-0 h-[350px] sm:h-[450px] lg:h-[550px]">
        <!-- Rotating/Static Background Circles -->
        <img src="/BG asset.png" class="absolute z-0 w-[75%] lg:w-[100%] max-w-[900px] top-1/2 left-1/4 -translate-x-1/2 -translate-y-1/2 opacity-100 pointer-events-none mix-blend-multiply" />
         
        <!-- Animated Foreground Image -->
        <!-- Moved down to sit on the StatsBanner and removed padding-bottom -->
        <div class="absolute z-10 w-full h-[115%] flex items-end justify-center lg:justify-end bottom-0 sm:-bottom-8 lg:-bottom-12">
          <transition name="fade-image" mode="out-in">
            <img :key="'img-'+currentSlide" :src="slides[currentSlide].image" class="max-h-[100%] w-auto object-contain object-bottom drop-shadow-2xl will-change-transform" />
          </transition>
        </div>
      </div>
    </div>

    <!-- Stats Banner -->
    <div class="absolute bottom-0 left-0 right-0 z-30 w-full translate-y-1/2 lg:translate-y-1/3">
      <div class="max-w-[1340px] mx-auto px-4 relative bottom-10 z-40">
        <StatsBanner />
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-section {
  min-height: 100vh;
}

/* Text Fade Transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(15px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-15px);
}

/* Image Fade Transition (No Slide) */
.fade-image-enter-active,
.fade-image-leave-active {
  transition: opacity 0.6s ease;
}
.fade-image-enter-from,
.fade-image-leave-to {
  opacity: 0;
}
</style>
