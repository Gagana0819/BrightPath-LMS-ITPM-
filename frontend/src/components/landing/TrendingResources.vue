<script setup></script>

<template>
  <section class="py-24 bg-slate-50 relative overflow-hidden px-4 sm:px-8 lg:px-20">
    <div class="max-w-[1200px] mx-auto w-full z-10 relative">
      <!-- Header -->
      <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
        <div>
          <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-4">Trending Resources</h2>
          <p class="text-slate-500 font-medium text-lg max-w-[600px]">
            A curated sample of the most downloaded past papers and lecture recordings by your peers.
          </p>
        </div>
        <a href="#" class="text-blue-600 hover:text-blue-700 font-semibold text-[1.05rem] flex items-center gap-1 transition-colors whitespace-nowrap">
          View all resources 
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path d="M9 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>
      </div>

      <!-- Main Cards -->
      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 mb-6">
        
        <!-- Large Left Card -->
        <div class="md:col-span-7 lg:col-span-8 bg-slate-900 rounded-2xl overflow-hidden relative shadow-md group h-[380px] flex flex-col justify-end p-8">
          <!-- Background Image Mockup -->
          <div class="absolute inset-0 bg-gradient-to-t from-slate-900/90 via-slate-900/40 to-transparent z-10"></div>
          <!-- In real app, this would be an img tag with object-cover, but we'll use a placeholder style if image is missing -->
          <div class="absolute inset-0 bg-slate-800 bg-[url('/bg-asset.png')] bg-cover bg-center opacity-40 group-hover:scale-105 transition-transform duration-700"></div>

          <div class="relative z-20">
            <span class="inline-block bg-yellow-400 text-slate-900 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded mb-4 shadow-sm">
              Most Popular
            </span>
            <h3 class="text-3xl font-bold text-white mb-3">CS102: Algorithms & Complexity</h3>
            <p class="text-slate-200 text-lg mb-8 max-w-[500px]">
              Comprehensive past paper analysis and solved examples from the 2023 Finals.
            </p>
            <div class="flex items-center gap-6">
              <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors shadow-sm text-sm">
                Download PDF
              </button>
              <div class="flex items-center gap-2 text-slate-300 text-sm font-medium">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
                1.2k downloads
              </div>
            </div>
          </div>
        </div>

        <!-- Right Video Card -->
        <div class="md:col-span-5 lg:col-span-4 bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col p-6">
          <div class="w-10 h-10 bg-blue-50 text-blue-600 rounded-lg flex items-center justify-center mb-5">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
              <line x1="16" y1="13" x2="8" y2="13"></line>
              <line x1="16" y1="17" x2="8" y2="17"></line>
              <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-2">Engineering Mechanics</h3>
          <p class="text-slate-500 text-sm mb-6 flex-1">
            Session recording covering Vector Statics and Equilibrium by Prof. Ata.
          </p>
          
          <!-- Video Thumbnail -->
          <div class="bg-black rounded-xl mb-6 relative aspect-video flex items-center justify-center group cursor-pointer overflow-hidden">
            <div class="text-white font-mono text-xs opacity-50 text-center tracking-widest absolute inset-0 flex items-center justify-center">
              E = mc²<br/>ΣF = 0
            </div>
            <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center relative z-10 shadow-lg group-hover:scale-110 transition-transform">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="text-slate-900 ml-1">
                <polygon points="5 3 19 12 5 21 5 3"></polygon>
              </svg>
            </div>
          </div>

          <button class="w-full border-2 border-slate-200 text-blue-600 hover:border-blue-600 hover:bg-blue-50 font-bold py-2.5 rounded-lg transition-colors text-sm">
            Watch Preview
          </button>
        </div>

      </div>

      <!-- Bottom Small Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Small Card 1 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 flex items-center gap-4 hover:shadow-md transition-shadow cursor-pointer">
          <div class="w-12 h-12 bg-orange-50 text-orange-500 rounded-xl flex shrink-0 items-center justify-center">
             <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
              <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
            </svg>
          </div>
          <div>
            <h4 class="font-bold text-slate-900">Human Anatomy: Muscular System (Notes)</h4>
            <p class="text-xs text-slate-400 font-bold mt-1 tracking-wider uppercase">Medical • Shared by MedStudent9</p>
          </div>
        </div>

        <!-- Small Card 2 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 flex items-center gap-4 hover:shadow-md transition-shadow cursor-pointer">
          <div class="w-12 h-12 bg-green-50 text-green-500 rounded-xl flex shrink-0 items-center justify-center">
             <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
          </div>
          <div>
            <h4 class="font-bold text-slate-900">Macroeconomics: 2024 Mid-Term Prep</h4>
            <p class="text-xs text-slate-400 font-bold mt-1 tracking-wider uppercase">Business • Shared by Admin</p>
          </div>
        </div>

      </div>

    </div>
  </section>
</template>
