<script setup>
import { RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'
import AppNavbar from './components/layout/AppNavbar.vue'
import InteractiveFooter from './components/layout/InteractiveFooter.vue'

const route = useRoute()
const isDashboard = computed(() => route.path.startsWith('/dashboard'))
</script>

<template>
  <AppNavbar v-if="!isDashboard" />
  <RouterView />
  <InteractiveFooter v-if="!isDashboard" />
</template>

<style scoped>
/* App specific global styles can go here, but mostly handled in main.css */
</style>
