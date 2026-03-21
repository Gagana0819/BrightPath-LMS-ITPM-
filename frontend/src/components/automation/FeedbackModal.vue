<script setup>
import { ref } from 'vue'

const props = defineProps({
  isOpen: Boolean,
  resourceName: {
    type: String,
    default: 'Object-Oriented Programming Notes'
  }
})

const emit = defineEmits(['close'])

const rating = ref(0)
const feedback = ref('')

const setRating = (val) => {
  rating.value = val
}

const submitFeedback = () => {
  // Logic
  emit('close')
}
</script>

<template>
  <div v-if="isOpen" class="fixed inset-0 z-[100] flex items-center justify-center p-4">
    <!-- Backdrop -->
    <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" @click="emit('close')"></div>
    
    <!-- Modal Content -->
    <div class="bg-white w-full max-w-md rounded-3xl shadow-2xl z-10 overflow-hidden animate-in zoom-in-95 duration-200">
      
      <!-- Graphic Header -->
      <div class="h-32 bg-gradient-to-br from-hero-bg-shape1 to-blue-100 relative flex items-center justify-center border-b border-blue-50">
        <button @click="emit('close')" class="absolute top-4 right-4 w-8 h-8 bg-white/50 hover:bg-white rounded-full flex items-center justify-center text-slate-500 transition-colors">
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        
        <div class="w-16 h-16 bg-white rounded-2xl shadow-sm rotate-3 flex items-center justify-center">
          <span class="text-3xl">⭐</span>
        </div>
      </div>

      <div class="p-8">
        <div class="text-center mb-6">
          <h2 class="text-2xl font-bold text-content tracking-tight mb-2">How was this resource?</h2>
          <p class="text-sm text-slate-500 font-medium">You just finished reading <span class="text-hero-highlight font-bold">{{ resourceName }}</span></p>
        </div>

        <!-- Star Rating -->
        <div class="flex items-center justify-center gap-2 mb-6 cursor-pointer">
          <svg 
            v-for="star in 5" 
            :key="star"
            @click="setRating(star)"
            class="w-10 h-10 transition-all hover:scale-110"
            :class="star <= rating ? 'text-[#FFB800]' : 'text-slate-200'"
            viewBox="0 0 24 24" 
            fill="currentColor"
          >
            <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
          </svg>
        </div>

        <div class="space-y-3 mb-6">
          <label class="text-sm font-bold text-slate-700">Any specific feedback? (Optional)</label>
          <textarea 
            v-model="feedback"
            rows="3" 
            class="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight text-sm text-content resize-none transition-all"
            placeholder="E.g., The examples on page 4 were really helpful!"
          ></textarea>
        </div>

        <button 
          @click="submitFeedback" 
          class="w-full py-3.5 bg-hero-highlight text-white rounded-xl font-bold shadow-md hover:-translate-y-0.5 hover:shadow-lg transition-all"
          :class="rating === 0 ? 'opacity-50 cursor-not-allowed hover:translate-y-0 hover:shadow-md' : ''"
          :disabled="rating === 0"
        >
          Submit Review
        </button>
      </div>
    </div>
  </div>
</template>
