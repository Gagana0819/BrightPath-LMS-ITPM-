<script setup>
import { RouterView } from 'vue-router'
import AppNavbar from './components/layout/AppNavbar.vue'
import InteractiveFooter from './components/layout/InteractiveFooter.vue'
</script>

<template>
  <AppNavbar />
  <RouterView />
  <InteractiveFooter />
</template>

<style scoped>
/* App specific global styles can go here, but mostly handled in main.css */
</style>
