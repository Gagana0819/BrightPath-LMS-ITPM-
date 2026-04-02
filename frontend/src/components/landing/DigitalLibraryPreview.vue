<script setup></script>

<template>
  <section class="relative py-24 bg-[#97C4C4] overflow-hidden">
    <div class="max-w-[1600px] mx-auto px-4 lg:px-6 w-full z-10">
      <!-- Top Content & Filter -->
      <div class="flex flex-col lg:flex-row justify-between items-end mb-16 gap-8">
        <div class="max-w-[700px]">
          <h2
            class="text-[3.5rem] lg:text-[4.5rem] leading-[1.2] text-[#333333] font-normal mb-8 tracking-tight"
          >
            Discover The<br />
            <span class="text-white font-bold relative inline-block pb-2">
              Digital Library
              <span class="absolute bottom-0 left-0 w-full h-[3px] bg-white"></span>
            </span>
          </h2>

          <div class="border-l-[3px] border-white pl-6">
            <p class="text-[1.15rem] lg:text-[1.25rem] text-[#333333] font-medium leading-relaxed">
              Access thousands of peer-reviewed study materials, PDFs, and Past Papers. Every
              document is ranked by the community for maximum quality and relevance.
            </p>
          </div>
        </div>

        <!-- Interactive Sort Filter -->
        <div
          class="flex flex-col sm:flex-row items-center gap-4 bg-white/40 backdrop-blur-md p-3 rounded-2xl border border-white/60 shadow-md"
        >
          <span class="text-[#333333] font-bold px-2 whitespace-nowrap">Sort Library By:</span>
          <select
            class="bg-white text-[#5D6DFF] font-bold text-lg px-6 py-3 rounded-xl outline-none border-2 border-transparent focus:border-[#5D6DFF] cursor-pointer shadow-sm w-full sm:w-auto appearance-none pr-10 relative"
          >
            <option>Quality Rank (Highest)</option>
            <option>Most Points Awarded</option>
            <option>Recently Uploaded</option>
          </select>
          <!-- Custom arrow for select -->
          <div class="absolute right-6 pointer-events-none text-[#5D6DFF]">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <path
                d="M6 9L12 15L18 9"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
        </div>
      </div>

      <!-- Horizontal Grid of Mockup Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 relative z-10">
        <!-- Card 1 -->
        <div
          class="bg-white rounded-2xl p-6 shadow-xl hover:-translate-y-2 hover:shadow-2xl transition-all duration-300 border border-white/50 flex flex-col h-full"
        >
          <div class="flex justify-between items-start mb-6">
            <div
              class="w-14 h-14 rounded-2xl bg-red-100 flex items-center justify-center text-red-500 font-bold text-lg shadow-inner"
            >
              PDF
            </div>
            <div
              class="flex items-center gap-1 bg-[#5D6DFF] text-white px-3 py-1.5 rounded-full text-sm font-bold shadow-sm"
            >
              <span class="text-yellow-300">★</span> 4.9 Rank
            </div>
          </div>
          <h3 class="font-bold text-[#333333] text-xl mb-3 line-clamp-2 leading-snug">
            2024 Semester 1 IT Project Management Past Paper
          </h3>
          <p class="text-slate-500 text-sm flex-1">
            Uploaded by <span class="font-semibold text-[#5D6DFF]">Student 01</span>
          </p>

          <div class="flex items-center justify-between border-t-2 border-slate-100 mt-6 pt-5">
            <div class="flex flex-col">
              <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider mb-1"
                >Reward Value</span
              >
              <div class="flex items-center gap-1.5 text-emerald-600 font-black text-lg">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                +350 Pts
              </div>
            </div>
            <button
              class="w-10 h-10 rounded-full bg-slate-50 border border-slate-200 flex items-center justify-center text-[#5D6DFF] hover:bg-[#5D6DFF] hover:text-white transition-colors"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path
                  d="M5 12H19M19 12L12 5M19 12L12 19"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </button>
          </div>
        </div>

        <!-- Card 2 -->
        <div
          class="bg-white rounded-2xl p-6 shadow-xl hover:-translate-y-2 hover:shadow-2xl transition-all duration-300 border border-white/50 flex flex-col h-full"
        >
          <div class="flex justify-between items-start mb-6">
            <div
              class="w-14 h-14 rounded-2xl bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-lg shadow-inner"
            >
              DOC
            </div>
            <div
              class="flex items-center gap-1 bg-[#5D6DFF] text-white px-3 py-1.5 rounded-full text-sm font-bold shadow-sm"
            >
              <span class="text-yellow-300">★</span> 4.7 Rank
            </div>
          </div>
          <h3 class="font-bold text-[#333333] text-xl mb-3 line-clamp-2 leading-snug">
            Software Engineering Comprehensive Lecture Notes
          </h3>
          <p class="text-slate-500 text-sm flex-1">
            Uploaded by <span class="font-semibold text-[#5D6DFF]">Alice S.</span>
          </p>

          <div class="flex items-center justify-between border-t-2 border-slate-100 mt-6 pt-5">
            <div class="flex flex-col">
              <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider mb-1"
                >Reward Value</span
              >
              <div class="flex items-center gap-1.5 text-emerald-600 font-black text-lg">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                +210 Pts
              </div>
            </div>
            <button
              class="w-10 h-10 rounded-full bg-slate-50 border border-slate-200 flex items-center justify-center text-[#5D6DFF] hover:bg-[#5D6DFF] hover:text-white transition-colors"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path
                  d="M5 12H19M19 12L12 5M19 12L12 19"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </button>
          </div>
        </div>

        <!-- Card 3 -->
        <div
          class="bg-white rounded-2xl p-6 shadow-xl hover:-translate-y-2 hover:shadow-2xl transition-all duration-300 border border-white/50 flex flex-col h-full"
        >
          <div class="flex justify-between items-start mb-6">
            <div
              class="w-14 h-14 rounded-2xl bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-lg shadow-inner"
            >
              PPT
            </div>
            <div
              class="flex items-center gap-1 bg-slate-100 text-[#333333] px-3 py-1.5 rounded-full text-sm font-bold border border-slate-200"
            >
              <span class="text-slate-400">★</span> New
            </div>
          </div>
          <h3 class="font-bold text-[#333333] text-xl mb-3 line-clamp-2 leading-snug">
            Database Architecture Slides (Week 4-7)
          </h3>
          <p class="text-slate-500 text-sm flex-1">
            Uploaded by <span class="font-semibold text-[#5D6DFF]">Michael B.</span>
          </p>

          <div class="flex items-center justify-between border-t-2 border-slate-100 mt-6 pt-5">
            <div class="flex flex-col">
              <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider mb-1"
                >Reward Value</span
              >
              <div class="flex items-center gap-1.5 text-emerald-600 font-black text-lg">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                +150 Pts
              </div>
            </div>
            <button
              class="w-10 h-10 rounded-full bg-slate-50 border border-slate-200 flex items-center justify-center text-[#5D6DFF] hover:bg-[#5D6DFF] hover:text-white transition-colors"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path
                  d="M5 12H19M19 12L12 5M19 12L12 19"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </button>
          </div>
        </div>

        <!-- Card 4 -->
        <div
          class="bg-white rounded-2xl p-6 shadow-xl hover:-translate-y-2 hover:shadow-2xl transition-all duration-300 border border-white/50 flex flex-col h-full"
        >
          <div class="flex justify-between items-start mb-6">
            <div
              class="w-14 h-14 rounded-2xl bg-emerald-100 flex items-center justify-center text-emerald-600 font-bold text-lg shadow-inner"
            >
              ZIP
            </div>
            <div
              class="flex items-center gap-1 bg-[#5D6DFF] text-white px-3 py-1.5 rounded-full text-sm font-bold shadow-sm"
            >
              <span class="text-yellow-300">★</span> 4.6 Rank
            </div>
          </div>
          <h3 class="font-bold text-[#333333] text-xl mb-3 line-clamp-2 leading-snug">
            Data Structures Assignment Code Template
          </h3>
          <p class="text-slate-500 text-sm flex-1">
            Uploaded by <span class="font-semibold text-[#5D6DFF]">Sarah K.</span>
          </p>

          <div class="flex items-center justify-between border-t-2 border-slate-100 mt-6 pt-5">
            <div class="flex flex-col">
              <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider mb-1"
                >Reward Value</span
              >
              <div class="flex items-center gap-1.5 text-emerald-600 font-black text-lg">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                +420 Pts
              </div>
            </div>
            <button
              class="w-10 h-10 rounded-full bg-slate-50 border border-slate-200 flex items-center justify-center text-[#5D6DFF] hover:bg-[#5D6DFF] hover:text-white transition-colors"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path
                  d="M5 12H19M19 12L12 5M19 12L12 19"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Call to Action button (bottom center) -->
      <div class="mt-16 flex justify-center">
        <RouterLink
          to="/library"
          class="inline-flex items-center justify-center px-10 py-4 rounded-xl font-bold text-[1.1rem] text-[#5D6DFF] bg-white hover:bg-slate-50 transition-all shadow-lg hover:shadow-xl hover:-translate-y-1"
        >
          Explore All Verified Documents
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" class="ml-2">
            <path
              d="M5 12H19M19 12L12 5M19 12L12 19"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </RouterLink>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Scoped styles */
select {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}
</style>
