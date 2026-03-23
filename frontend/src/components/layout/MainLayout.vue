<template>
  <div class="flex h-screen bg-[#F9FAFB] overflow-hidden">
    <!-- Sidebar -->
    <DashboardSidebar class="hidden md:flex" />
    
    <!-- Main Content Area -->
    <div class="flex-1 flex flex-col overflow-hidden relative">
      <!-- Top Navbar (Contains the circular user profile!) -->
      <DashboardNavbar />
      
      <!-- Page Content -->
      <main class="flex-1 overflow-x-hidden overflow-y-auto bg-[#F9FAFB]">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import DashboardSidebar from './DashboardSidebar.vue'
import DashboardNavbar from './DashboardNavbar.vue'
</script>

<style scoped>
</style>
