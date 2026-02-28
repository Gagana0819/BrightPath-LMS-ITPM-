<script setup>
</script>

<template>
  <section class="trust-banner">
    <div class="banner-container glass-panel">
      <div class="banner-text">
        <h3 class="text-gradient">Secure Access via University NIC/ID</h3>
        <p>Trusted by major universities and verified student bodies.</p>
      </div>
      <div class="university-logos">
        <!-- Mockup logos with simple CSS shapes to represent university seals -->
        <div class="logo-mockup seal-1">UoC</div>
        <div class="logo-mockup seal-2">MRT</div>
        <div class="logo-mockup seal-3">Pera</div>
        <div class="logo-mockup seal-4">UoK</div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.trust-banner {
  padding: var(--spacing-2xl) var(--spacing-xl);
  max-width: 1200px;
  margin: 0 auto;
}

.banner-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--spacing-xl) var(--spacing-3xl);
  background: rgba(17, 34, 64, 0.4);
  border: 1px solid rgba(16, 185, 129, 0.2); /* Emerald tint border */
}

.banner-text h3 {
  font-size: 1.5rem;
  margin-bottom: var(--spacing-xs);
  font-weight: 700;
}

.banner-text p {
  color: var(--color-text-secondary);
  font-size: 1rem;
}

.university-logos {
  display: flex;
  gap: var(--spacing-xl);
  align-items: center;
}

.logo-mockup {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  color: rgba(255,255,255,0.3);
  background: rgba(255,255,255,0.05);
  border: 2px solid rgba(255,255,255,0.1);
  filter: grayscale(1);
  transition: all 0.3s;
}

.logo-mockup:hover {
  filter: grayscale(0);
  color: var(--color-success);
  border-color: var(--color-success);
  background: rgba(16, 185, 129, 0.1);
}

.seal-1 { border-radius: 50%; }
.seal-2 { border-radius: 12px; transform: rotate(45deg); display: flex; align-items: center; justify-content: center; }
.seal-3 { border-radius: 50%; border-style: dashed; }
.seal-4 { border-radius: 8px; }

@media (max-width: 900px) {
  .banner-container {
    flex-direction: column;
    text-align: center;
    gap: var(--spacing-xl);
  }
}
</style>
