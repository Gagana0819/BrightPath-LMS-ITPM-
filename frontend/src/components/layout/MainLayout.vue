<script setup>
import DashboardSidebar from './DashboardSidebar.vue'
import DashboardNavbar from './DashboardNavbar.vue'
</script>

<template>
  <div class="flex h-screen bg-base overflow-hidden font-sans text-content">
    <!-- Sidebar (Desktop and Mobile drawer) -->
    <DashboardSidebar class="hidden md:flex" />

    <div class="flex-1 flex flex-col relative overflow-hidden">
      <!-- Top App Bar -->
      <DashboardNavbar />

      <!-- Main Scrollable Content -->
      <main class="flex-1 overflow-y-auto p-4 md:p-6 lg:p-8 bg-base">
        <!-- Render current route components -->
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>
