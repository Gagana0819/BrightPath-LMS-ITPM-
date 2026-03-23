<script setup>
import HeroSection from '../components/landing/HeroSection.vue'
import TrendingResources from '../components/landing/TrendingResources.vue'
import ModernFeatures from '../components/landing/ModernFeatures.vue'
</script>

<template>
  <main class="home-view bg-base ">
    <HeroSection />
    <TrendingResources />
    <ModernFeatures />
  </main>
</template>

<style scoped>
.home-view {
  width: 100%;
}
</style>
