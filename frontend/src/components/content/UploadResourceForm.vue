<script setup>
import { ref } from 'vue'

const isClassroomSync = ref(true)
const fileRef = ref(null)

const toggleSync = () => {
  isClassroomSync.value = !isClassroomSync.value
}
</script>

<template>
  <div class="w-full max-w-2xl mx-auto bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
    <div class="mb-6">
      <h2 class="text-2xl font-bold text-content mb-1">Upload Study Resource</h2>
      <p class="text-slate-500 text-sm">Share your notes, presentations, or past papers with the community.</p>
    </div>

    <div class="space-y-6">
      
      <!-- General Form -->
      <div class="space-y-4">
        <div class="space-y-1.5">
          <label class="text-sm font-semibold text-slate-700">Resource Title</label>
          <input type="text" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none" placeholder="e.g. ITPM Lecture Notes - Chapter 5" />
        </div>
        
        <div class="grid md:grid-cols-2 gap-4">
          <div class="space-y-1.5">
            <label class="text-sm font-semibold text-slate-700">Module Code</label>
            <input type="text" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none" placeholder="SE3040" />
          </div>
          <div class="space-y-1.5">
            <label class="text-sm font-semibold text-slate-700">Resource Type</label>
            <select class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none text-slate-700">
              <option>Lecture Notes</option>
              <option>Past Papers</option>
              <option>Tutorial Answers</option>
              <option>Cheat Sheet</option>
            </select>
          </div>
        </div>
      </div>

      <!-- File Upload Zone -->
      <div class="border-2 border-dashed border-slate-300 rounded-2xl p-8 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-50 hover:border-hero-highlight transition-all group relative overflow-hidden">
        <div class="w-16 h-16 bg-blue-50 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:bg-blue-100 transition-colors">
          <svg class="w-8 h-8 text-hero-highlight" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
        </div>
        <span class="font-bold text-content block text-lg mb-1">Drag and drop your files here</span>
        <span class="text-sm text-slate-500 font-medium">Or <span class="text-hero-highlight">browse files</span> from your computer</span>
        <span class="text-xs text-slate-400 mt-3 font-medium">Supported formats: PDF, DOCX, PPTX (max 25MB)</span>
      </div>

      <hr class="border-slate-100" />

      <!-- Integrations Area -->
      <div class="flex items-center justify-between p-4 bg-slate-50 rounded-xl border border-slate-200">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-white rounded-lg shadow-sm border border-slate-200 flex items-center justify-center p-2">
            <!-- Simple GClassroom Icon placeholder -->
            <svg class="w-full h-full text-green-600" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 4c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm0 14c-2.03 0-4.43-.82-6.14-2.88C7.55 15.8 9.68 15 12 15s4.45.8 6.14 2.12C16.43 19.18 14.03 20 12 20z"/>
            </svg>
          </div>
          <div>
            <span class="block font-bold text-slate-800 text-sm">Google Classroom Sync</span>
            <span class="block text-xs text-slate-500 font-medium tracking-wide">Automatically post a link to your configured class modules.</span>
          </div>
        </div>

        <!-- Toggle Switch -->
        <button 
          @click="toggleSync" 
          class="w-12 h-6 rounded-full relative transition-colors duration-300 focus:outline-none"
          :class="isClassroomSync ? 'bg-green-500' : 'bg-slate-300'"
        >
          <div 
            class="absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow transition-transform duration-300"
            :class="isClassroomSync ? 'translate-x-6' : 'translate-x-0'"
          ></div>
        </button>
      </div>

      <!-- Submit Row -->
      <div class="pt-2 flex justify-end">
        <button class="px-8 py-3 bg-hero-highlight text-white rounded-xl font-bold tracking-wide hover:opacity-90 transition-all shadow-md hover:shadow-lg hover:-translate-y-0.5">
          Publish Resource
        </button>
      </div>
    </div>
  </div>
</template>
