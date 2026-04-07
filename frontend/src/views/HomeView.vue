<script setup>
import { onMounted } from 'vue'
import { useContentStore } from '../stores/contentStore'
import HeroSection from '../components/landing/HeroSection.vue'
import TrendingResources from '../components/landing/TrendingResources.vue'
import ModernFeatures from '../components/landing/ModernFeatures.vue'
import RecommendedSessions from '../components/landing/RecommendedSessions.vue'

const contentStore = useContentStore()

onMounted(() => {
  contentStore.fetchRecommendations()
  contentStore.fetchKuppiRecommendations()
})
</script>

<template>
  <main class="home-view bg-base ">
    <HeroSection />
    <TrendingResources />
    <RecommendedSessions />
    <ModernFeatures />
  </main>
</template>

<style scoped>
.home-view {
  width: 100%;
}
</style>
