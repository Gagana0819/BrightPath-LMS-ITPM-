<script setup>
import { ref, onMounted } from 'vue';

const isVisible = ref(false);

onMounted(() => {
  // Simple intersection observer for scroll animations
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      isVisible.value = true;
    }
  }, { threshold: 0.1 });
  
  const section = document.querySelector('.library-carousel');
  if (section) observer.observe(section);
});
</script>

<template>
  <section class="library-carousel" :class="{ 'is-visible': isVisible }">
    <div class="section-header">
      <h2 class="text-gradient">The Smart Library</h2>
      <p>Access high-quality, peer-reviewed resources ranked by the community.</p>
    </div>
    
    <div class="carousel-track">
      <!-- Card 1 -->
      <div class="document-card glass-panel card-1">
        <div class="icon-3d pdf-icon">📄</div>
        <div class="card-content">
          <h3>Advanced algorithms.pdf</h3>
          <p class="author">By Student 01</p>
          <div class="metrics">
            <span class="quality-score"><span class="dot"></span> 98% Match</span>
            <span class="points">+50 pts</span>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="document-card glass-panel card-2">
        <div class="icon-3d doc-icon">📝</div>
        <div class="card-content">
          <h3>SE Past Paper 2025</h3>
          <p class="author">By Alice S.</p>
          <div class="metrics">
            <span class="quality-score"><span class="dot"></span> 95% Match</span>
            <span class="points">+45 pts</span>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="document-card glass-panel card-3">
        <div class="icon-3d slide-icon">📊</div>
        <div class="card-content">
          <h3>Database Normalization</h3>
          <p class="author">By John Doe</p>
          <div class="metrics">
            <span class="quality-score"><span class="dot"></span> 92% Match</span>
            <span class="points">+40 pts</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.library-carousel {
  padding: var(--spacing-4xl) var(--spacing-xl);
  max-width: 1400px;
  margin: 0 auto;
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.library-carousel.is-visible {
  opacity: 1;
  transform: translateY(0);
}

.section-header {
  text-align: center;
  margin-bottom: var(--spacing-3xl);
}

.section-header h2 {
  font-size: 3rem;
  margin-bottom: var(--spacing-sm);
  font-weight: 800;
}

.section-header p {
  font-size: 1.125rem;
  color: var(--color-text-secondary);
}

.carousel-track {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: var(--spacing-xl);
  perspective: 1000px;
}

.document-card {
  padding: var(--spacing-xl);
  display: flex;
  align-items: flex-start;
  gap: var(--spacing-lg);
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
  background: rgba(17, 34, 64, 0.5); /* Slightly darker glass */
}

.document-card:hover {
  transform: translateY(-10px) scale(1.02);
  background: rgba(17, 34, 64, 0.8);
  border-color: rgba(255, 255, 255, 0.2);
}

/* Stagger animations for cards */
.is-visible .card-1 { animation: slideUp 0.6s 0.1s both; }
.is-visible .card-2 { animation: slideUp 0.6s 0.2s both; }
.is-visible .card-3 { animation: slideUp 0.6s 0.3s both; }

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.icon-3d {
  font-size: 3rem;
  filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3));
  background: linear-gradient(135deg, var(--color-primary-lighter), var(--color-primary-light));
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 16px;
  border: 1px solid rgba(255,255,255,0.05);
}

.card-content {
  flex: 1;
}

.card-content h3 {
  font-size: 1.25rem;
  color: var(--color-text-primary);
  margin-bottom: var(--spacing-xs);
  font-weight: 600;
}

.author {
  color: var(--color-text-secondary);
  font-size: 0.9rem;
  margin-bottom: var(--spacing-md);
}

.metrics {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: var(--spacing-sm);
  border-top: 1px solid rgba(255,255,255,0.05);
}

.quality-score {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  color: var(--color-success);
  font-weight: 600;
  font-size: 0.875rem;
}

.dot {
  width: 6px;
  height: 6px;
  background-color: var(--color-success);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--color-success);
}

.points {
  background: rgba(255, 107, 53, 0.1);
  color: var(--color-accent);
  padding: 0.2rem 0.6rem;
  border-radius: var(--radius-full);
  font-size: 0.8rem;
  font-weight: bold;
}
</style>
