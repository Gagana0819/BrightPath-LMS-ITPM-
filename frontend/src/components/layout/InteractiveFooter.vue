<<<<<<< HEAD
<template>
  <footer class="bg-white border-t border-slate-200">
    <!-- CTA Banner -->
    <div class="bg-gradient-to-r from-brand to-[#6BAAEE] py-16 px-4">
      <div class="max-w-[1200px] mx-auto text-center text-white">
        <h2 class="text-[2.2rem] font-bold mb-4">Ready to join the community?</h2>
        <p class="text-white/90 text-lg mb-8 max-w-[600px] mx-auto">
          Sign up today and get instant access to thousands of resources, real-time sessions, and peer support.
        </p>
        <RouterLink to="/register" class="inline-flex items-center justify-center px-8 py-3.5 rounded-md font-bold text-[1.1rem] text-brand bg-white hover:bg-slate-50 transition-all shadow-md">
          Get Started Now
        </RouterLink>
      </div>
    </div>

    <!-- Main Footer -->
    <div class="max-w-[1400px] mx-auto px-4 lg:px-6 py-16">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8">
        
        <!-- Brand Section -->
        <div>
          <h3 class="font-bold text-2xl text-brand mb-4">The Academic Curator</h3>
          <p class="text-slate-500 font-medium leading-relaxed mb-6">
            The comprehensive web-based LMS designed exclusively for university students. Master your curriculum with a curated community of experts and peers.
          </p>
        </div>

        <!-- Resources Section -->
        <div>
          <h4 class="font-bold text-slate-800 uppercase tracking-wider mb-6">Resources</h4>
          <ul class="space-y-4">
            <li><RouterLink to="/library" class="text-slate-500 font-medium hover:text-brand transition-colors">Digital Library</RouterLink></li>
            <li><RouterLink to="/dashboard/kuppi" class="text-slate-500 font-medium hover:text-brand transition-colors">Kuppi Sessions</RouterLink></li>
            <li><RouterLink to="/dashboard" class="text-slate-500 font-medium hover:text-brand transition-colors">Student Dashboard</RouterLink></li>
          </ul>
        </div>

        <!-- Support Section -->
        <div>
          <h4 class="font-bold text-slate-800 uppercase tracking-wider mb-6">Support</h4>
          <ul class="space-y-4">
            <li><RouterLink to="/about" class="text-slate-500 font-medium hover:text-brand transition-colors">About Us</RouterLink></li>
            <li><RouterLink to="/contact" class="text-slate-500 font-medium hover:text-brand transition-colors">Contact Support</RouterLink></li>
            <li><RouterLink to="/faq" class="text-slate-500 font-medium hover:text-brand transition-colors">FAQ</RouterLink></li>
          </ul>
        </div>

        <!-- Connect Section -->
        <div>
          <h4 class="font-bold text-slate-800 uppercase tracking-wider mb-6">Connect</h4>
          <ul class="space-y-4">
            <li><a href="#" class="text-slate-500 font-medium hover:text-brand transition-colors">Twitter</a></li>
            <li><a href="#" class="text-slate-500 font-medium hover:text-brand transition-colors">LinkedIn</a></li>
            <li><a href="#" class="text-slate-500 font-medium hover:text-brand transition-colors">Facebook</a></li>
          </ul>
        </div>

      </div>

      <div class="border-t border-slate-100 mt-12 pt-8 text-center md:flex md:justify-between md:text-left">
        <p class="text-slate-400 font-medium text-sm">&copy; 2026 The Academic Curator. All rights reserved.</p>
        <div class="flex space-x-6 justify-center mt-4 md:mt-0">
          <RouterLink to="/privacy" class="text-slate-400 font-medium text-sm hover:text-brand transition-colors">Privacy Policy</RouterLink>
          <RouterLink to="/terms" class="text-slate-400 font-medium text-sm hover:text-brand transition-colors">Terms of Service</RouterLink>
        </div>
=======
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
>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
      </div>
    </div>
  </footer>
</template>

<<<<<<< HEAD
<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
=======
<style scoped></style>
>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
