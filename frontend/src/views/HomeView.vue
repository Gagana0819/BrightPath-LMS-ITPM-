<script setup>
import HeroSection from '../components/landing/HeroSection.vue'
import SmartLibraryCarousel from '../components/landing/SmartLibraryCarousel.vue'
import LiveKuppiSync from '../components/landing/LiveKuppiSync.vue'
import LeaderboardWidget from '../components/landing/LeaderboardWidget.vue'
import VerificationTrust from '../components/landing/VerificationTrust.vue'
</script>

<template>
  <main class="home-view">
    <HeroSection />
    <VerificationTrust />
    <SmartLibraryCarousel />
    <LiveKuppiSync />
    <LeaderboardWidget />
  </main>
</template>

<style scoped>
.home-view {
  width: 100%;
}
</style>
