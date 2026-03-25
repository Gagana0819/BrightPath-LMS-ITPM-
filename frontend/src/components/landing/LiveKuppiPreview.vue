<script setup></script>

<template>
  <section class="relative min-h-screen flex items-center overflow-hidden py-24 bg-white">
    <!-- Background diagonal layout -->
    <div
      class="absolute top-0 -left-[5%] w-[55%] h-full bg-[#e0e7ff] -skew-x-[15deg] -z-10 hidden lg:block"
    ></div>

    <div
      class="max-w-[1600px] mx-auto px-4 lg:px-6 w-full z-10 flex flex-col lg:flex-row items-stretch justify-between gap-16 pt-12 lg:pt-0"
    >
      <!-- Left Content -->
      <div class="flex-1 max-w-[600px] py-0 lg:py-16 relative flex flex-col justify-center">
        <h2
          class="text-[3.5rem] lg:text-[4.5rem] leading-[1.2] text-[#333333] font-normal mb-10 tracking-tight"
        >
          Live Kuppi &<br />
          <span class="text-[#5D6DFF] font-bold relative inline-block pb-2">
            Virtual Classrooms
            <span class="absolute bottom-0 left-0 w-full h-[3px] bg-[#5D6DFF]"></span>
          </span>
        </h2>

        <div class="border-l-[3px] border-[#5D6DFF] pl-6 mb-12 relative z-10">
          <p
            class="text-[1.15rem] lg:text-[1.25rem] text-[#333333] font-medium leading-relaxed max-w-[500px]"
          >
            Sync your sessions automatically via our Google Classroom API integration. Connect with
            top-tier educators through interactive 'Kuppi' sessions and discussion videos.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
          <!-- Profile Highlight -->
          <div
            class="bg-white p-6 rounded-2xl shadow-lg border border-slate-100 flex items-start gap-4 hover:-translate-y-1 transition-transform"
          >
            <div
              class="w-12 h-12 rounded-full bg-indigo-100 flex items-center justify-center text-xl"
            >
              👨‍🏫
            </div>
            <div>
              <h3 class="font-bold text-[#333333]">Prof. Perera</h3>
              <p class="text-sm text-slate-500">SE Expert • 4.9⭐</p>
            </div>
          </div>
          <div
            class="bg-white p-6 rounded-2xl shadow-lg border border-slate-100 flex items-start gap-4 hover:-translate-y-1 transition-transform"
          >
            <div
              class="w-12 h-12 rounded-full bg-rose-100 flex items-center justify-center text-xl"
            >
              👩‍💻
            </div>
            <div>
              <h3 class="font-bold text-[#333333]">Dr. Silva</h3>
              <p class="text-sm text-slate-500">DSA Pro • 5.0⭐</p>
            </div>
          </div>
        </div>

        <div class="flex items-center relative z-10">
          <RouterLink
            to="/dashboard"
            class="inline-flex items-center justify-center px-8 py-3.5 rounded-lg font-bold text-[1.1rem] text-white bg-[#5D6DFF] hover:bg-[#4a58e6] transition-all shadow-md hover:shadow-lg hover:-translate-y-0.5"
          >
            View Live Schedule
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

      <!-- Right Visual (Calendar Mockup) -->
      <div class="flex-1 relative flex items-center justify-center">
        <!-- Main Mockup Container -->
        <div
          class="relative w-full max-w-lg bg-white rounded-3xl overflow-hidden shadow-[0_20px_50px_-12px_rgba(93,109,255,0.3)] border border-slate-100 p-6 z-10"
        >
          <div class="flex items-center justify-between border-b border-slate-100 pb-4 mb-6">
            <div>
              <h3 class="font-bold text-[#333333] text-lg">Upcoming Sessions</h3>
              <p class="text-sm text-slate-500">Synced via Google Classroom</p>
            </div>
            <div
              class="w-10 h-10 bg-[#e0e7ff] rounded-xl flex items-center justify-center text-[#5D6DFF]"
            >
              📅
            </div>
          </div>

          <div class="space-y-4">
            <!-- Event 1 -->
            <div
              class="bg-slate-50 rounded-xl p-4 border border-slate-100 border-l-4 border-l-[#5D6DFF]"
            >
              <div class="flex justify-between items-start mb-2">
                <h4 class="font-bold text-[#333333]">Data Structures Kuppi</h4>
                <span
                  class="bg-red-100 text-red-600 text-xs font-bold px-2 py-1 rounded-full animate-pulse"
                  >LIVE NOW</span
                >
              </div>
              <div class="flex items-center gap-4 text-sm text-slate-500 mb-3">
                <span class="flex items-center gap-1">🕒 10:00 AM</span>
                <span class="flex items-center gap-1">👤 Dr. Silva</span>
              </div>
              <div class="flex gap-2">
                <button
                  class="flex-1 bg-[#5D6DFF] text-white font-bold text-sm py-2 rounded-lg hover:bg-[#4a58e6] transition-colors"
                >
                  Join Meeting
                </button>
              </div>
            </div>

            <!-- Event 2 -->
            <div
              class="bg-slate-50 rounded-xl p-4 border border-slate-100 border-l-4 border-l-emerald-400"
            >
              <div class="flex justify-between items-start mb-2">
                <h4 class="font-bold text-[#333333]">ITPM Past Paper Discussion</h4>
                <span class="bg-slate-200 text-slate-600 text-xs font-bold px-2 py-1 rounded-full"
                  >TODAY</span
                >
              </div>
              <div class="flex items-center gap-4 text-sm text-slate-500 mb-3">
                <span class="flex items-center gap-1">🕒 2:00 PM</span>
                <span class="flex items-center gap-1">👤 Prof. Perera</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Decorative Elements -->
        <div
          class="absolute -right-10 -bottom-10 w-48 h-48 bg-[#5D6DFF] rounded-full mix-blend-multiply filter blur-[60px] opacity-20 z-0 animate-pulse"
        ></div>
        <div
          class="absolute -left-10 -top-10 w-48 h-48 bg-rose-400 rounded-full mix-blend-multiply filter blur-[60px] opacity-10 z-0"
        ></div>
      </div>
    </div>
  </section>
</template>

<style scoped></style>
