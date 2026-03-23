<script setup></script>

<template>
  <footer class="bg-[#1e293b] text-white py-16 mt-auto">
    <div class="max-w-[1600px] mx-auto px-4 lg:px-6 w-full">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">
        <!-- Brand Info -->
        <div class="lg:col-span-2">
          <h3 class="flex items-center gap-2 text-2xl font-bold text-white tracking-tight mb-4">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" class="text-brand">
              <path
                d="M4 19V5C4 3.89543 4.89543 3 6 3H19V19C19 20.1046 18.1046 21 17 21H6C4.89543 21 4 20.1046 4 19Z"
                stroke="currentColor"
                stroke-width="2"
              />
              <path d="M4 15L15 3" stroke="currentColor" stroke-width="2" />
              <path
                d="M10 12L10 21"
                stroke="currentColor"
                stroke-width="1"
                stroke-dasharray="2 2"
              />
              <path
                d="M14 12L14 21"
                stroke="currentColor"
                stroke-width="1"
                stroke-dasharray="2 2"
              />
            </svg>
            BrightPath
          </h3>
          <p class="text-slate-400 leading-relaxed max-w-[400px]">
            The centralized peer-to-peer LMS for University Students. Share, access, and rank
            resources for collaborative success.
          </p>
        </div>

        <!-- Links -->
        <div>
          <h4 class="font-bold text-lg mb-6 text-white">Quick Links</h4>
          <ul class="space-y-3 flex flex-col">
            <li>
              <RouterLink to="/" class="text-slate-400 hover:text-brand transition-colors"
                >Home</RouterLink
              >
            </li>
            <li>
              <RouterLink
                to="/library"
                class="text-slate-400 hover:text-brand transition-colors"
                >Digital Library</RouterLink
              >
            </li>
            <li>
              <RouterLink
                to="/dashboard"
                class="text-slate-400 hover:text-brand transition-colors"
                >Kuppi Sessions</RouterLink
              >
            </li>
            <li>
              <RouterLink to="/login" class="text-slate-400 hover:text-brand transition-colors"
                >Login / Verification</RouterLink
              >
            </li>
          </ul>
        </div>

        <!-- Platform Stats -->
        <div>
          <h4 class="font-bold text-lg mb-6 text-white">Platform Stats</h4>
          <div class="flex flex-col gap-5">
            <div>
              <span class="block text-2xl font-bold text-brand leading-none mb-1">5k+</span>
              <span class="text-sm text-slate-400">Total Resources</span>
            </div>
            <div>
              <span class="block text-2xl font-bold text-brand leading-none mb-1">1.2k</span>
              <span class="text-sm text-slate-400">Active Students</span>
            </div>
            <div>
              <span class="block text-2xl font-bold text-brand leading-none mb-1">50+</span>
              <span class="text-sm text-slate-400">Verified Teachers</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer Bottom -->
      <div class="border-t border-slate-700 pt-8 mt-12 text-center flex flex-col items-center">
        <p class="text-slate-500 text-sm">&copy; 2026 BrightPath LMS. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<style scoped></style>
