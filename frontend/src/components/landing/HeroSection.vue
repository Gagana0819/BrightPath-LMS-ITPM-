<script setup>
import StatsBanner from './StatsBanner.vue'
</script>

<template>
  <section class="hero-section relative w-full overflow-hidden">
    <!-- Background Image Layer -->
    <div class="absolute inset-0 w-full h-full z-0">
      <img
        src="/hero BG.png"
        alt="Hero background"
        class="w-full h-full object-cover"
      />
    </div>

    <!-- Main Content Area -->
    <div class="relative z-10 max-w-[1400px] mx-auto px-4 lg:px-8 w-full h-full">
      <div class="flex items-end justify-center lg:justify-end w-full hero-content-area">
        <!-- Right Visual: BG Asset (circles) behind the girl image -->
        <div class="relative flex items-end justify-center">
          <!-- BG Asset (abstract circles) - positioned behind the girl -->
          <img
            src="/BG asset.png"
            alt="Background decorative circles"
            class="absolute z-0 bg-asset-img"
          />

          <!-- Girl with books (digital library) - foreground -->
          <img
            src="/digital library.png"
            alt="Student with digital library"
            class="relative z-10 girl-img"
          />
        </div>
      </div>
    </div>

    <!-- Stats Banner overlapping the bottom of the hero image -->
    <div class="absolute bottom-20 left-0 right-0 z-20 w-full">
      <StatsBanner />
    </div>
  </section>
</template>

<style scoped>
.hero-section {
  min-height: 600px;
  padding-bottom: 0;
}

.hero-content-area {
  min-height: 500px;
  padding-top: 80px;
  padding-bottom: 40px;
}

.girl-img {
  max-height: 480px;
  width: auto;
  object-fit: contain;
  object-position: bottom;
}

.bg-asset-img {
  width: 120%;
  max-width: 700px;
  top: -10%;
  left: 50%;
  transform: translateX(-50%);
  object-fit: contain;
  pointer-events: none;
}

/* Responsive adjustments */
@media (min-width: 1024px) {
  .hero-section {
    min-height: 700px;
  }

  .hero-content-area {
    min-height: 600px;
    padding-top: 100px;
    padding-bottom: 50px;
  }

  .girl-img {
    max-height: 560px;
  }

  .bg-asset-img {
    width: 140%;
    max-width: 850px;
    top: -15%;
  }
}

@media (min-width: 1280px) {
  .hero-content-area {
    padding-top: 80px;
  }

  .girl-img {
    max-height: 600px;
  }
}
</style>
