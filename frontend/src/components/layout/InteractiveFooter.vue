<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <footer class="bg-white border-t border-slate-200">
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
            <li><RouterLink to="/digital-library" class="text-slate-500 font-medium hover:text-brand transition-colors">Digital Library</RouterLink></li>
            <li><RouterLink to="/sessions" class="text-slate-500 font-medium hover:text-brand transition-colors">Kuppi Sessions</RouterLink></li>
            <li><RouterLink to="/dashboard" class="text-slate-500 font-medium hover:text-brand transition-colors">Student Dashboard</RouterLink></li>
          </ul>
        </div>

        <!-- Support Section -->
        <div>
          <h4 class="font-bold text-slate-800 uppercase tracking-wider mb-6">Support</h4>
          <ul class="space-y-4">
            <li><RouterLink to="/about" class="text-slate-500 font-medium hover:text-brand transition-colors">About Us</RouterLink></li>
            <li><RouterLink to="/" class="text-slate-500 font-medium hover:text-brand transition-colors">Contact Support</RouterLink></li>
            <li><RouterLink to="/" class="text-slate-500 font-medium hover:text-brand transition-colors">FAQ</RouterLink></li>
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
          <RouterLink to="/" class="text-slate-400 font-medium text-sm hover:text-brand transition-colors">Privacy Policy</RouterLink>
          <RouterLink to="/" class="text-slate-400 font-medium text-sm hover:text-brand transition-colors">Terms of Service</RouterLink>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
</style>
