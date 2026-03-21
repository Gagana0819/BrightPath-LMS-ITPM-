<script setup>
import HeroSection from '../components/landing/HeroSection.vue'
import DigitalLibraryPreview from '../components/landing/DigitalLibraryPreview.vue'
import LiveKuppiPreview from '../components/landing/LiveKuppiPreview.vue'
import VerificationWorks from '../components/landing/VerificationWorks.vue'
import SmartNotificationsPreview from '../components/landing/SmartNotificationsPreview.vue'
</script>

<template>
  <main class="home-view bg-base">
    <HeroSection />
    <DigitalLibraryPreview />
    <LiveKuppiPreview />
    <VerificationWorks />
    <SmartNotificationsPreview />
  </main>
</template>

<style scoped>
.home-view {
  width: 100%;
}
</style>
