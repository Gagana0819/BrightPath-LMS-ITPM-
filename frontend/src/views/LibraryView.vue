<script setup>
import { ref } from 'vue'
import DocumentGrid from '../components/library/DocumentGrid.vue'
import PointsWallet from '../components/library/PointsWallet.vue'
import UploadResourceForm from '../components/content/UploadResourceForm.vue'

const searchQuery = ref('')
</script>

<template>
  <div class="flex flex-col lg:flex-row gap-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
    <!-- Main Library Content -->
    <div class="flex-1 space-y-8">
      
      <!-- Search / Filters Header -->
      <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 flex flex-col md:flex-row gap-4 items-center">
        <div class="relative flex-1 w-full">
          <svg class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input v-model="searchQuery" type="text" placeholder="Search digital library by title, module, or tags..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-12 pr-4 py-3 outline-none focus:border-hero-highlight focus:ring-2 focus:ring-hero-highlight/20 transition-all font-medium" />
        </div>
        <button class="w-full md:w-auto px-8 py-3 bg-hero-highlight text-white rounded-xl font-bold shadow-md hover:-translate-y-0.5 transition-all">
          Search
        </button>
      </div>

      <!-- Member 03: The Library Grid -->
      <DocumentGrid :searchQuery="searchQuery" />
    </div>

    <!-- Right Sidebar Modules -->
    <aside class="w-full lg:w-[380px] shrink-0 space-y-8">
      
      <!-- Member 03: Gamification Module -->
      <PointsWallet />
      
      <!-- Member 02: Upload Module (Scaled to fit sidebar nicely) -->
      <div class="bg-white rounded-2xl shadow-sm border border-slate-100 overflow-hidden pb-4">
        <div class="p-4 bg-slate-50 border-b border-slate-100 flex items-center justify-between">
          <h3 class="font-bold text-content">Quick Upload</h3>
          <span class="text-xs font-bold text-hero-highlight bg-blue-50 px-2 py-1 rounded-md mb-0">Earn +50 BP</span>
        </div>
        <!-- We use the Resource form here but normally you might place it on its own page depending on the exact UX -->
        <UploadResourceForm class="shadow-none border-none p-4 !max-w-full" />
      </div>

    </aside>
  </div>
</template>
