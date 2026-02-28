<script setup>
</script>

<template>
  <section class="hero">
    <div class="hero-container">
      <div class="hero-content">
        <div class="badge glass-panel">
          <span class="badge-dot"></span> Next-Gen Learning
        </div>
        <h1 class="hero-title">Your Academic Journey, <span class="text-gradient">Optimized</span></h1>
        <p class="hero-subtitle">
          Join BrightPath and experience the future of university collaboration. 
          Share resources, join live sessions, and climb the leaderboard.
        </p>
        <div class="hero-actions">
          <RouterLink to="/login" class="btn btn-primary">Start Learning</RouterLink>
          <div class="trust-indicator">
            <div class="avatars">
              <span class="avatar">👨‍🎓</span>
              <span class="avatar">👩‍🔬</span>
              <span class="avatar">🧑‍💻</span>
            </div>
            <span class="trust-text">Join 1.2k+ Peers</span>
          </div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="image-container animate-float">
          <div class="glow-effect"></div>
          <img src="/hero_image.png" alt="3D Isometric University Book" class="hero-image" />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: 85vh;
  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.hero-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: var(--spacing-4xl) var(--spacing-xl);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-4xl);
  z-index: 10;
}

.hero-content {
  flex: 1;
  max-width: 650px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: 0.4rem 1rem;
  border-radius: var(--radius-full);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--color-success);
  margin-bottom: var(--spacing-xl);
}

.badge-dot {
  width: 8px;
  height: 8px;
  background-color: var(--color-success);
  border-radius: 50%;
  box-shadow: 0 0 10px var(--color-success);
}

.hero-title {
  font-size: 4.5rem;
  line-height: 1.1;
  margin-bottom: var(--spacing-lg);
  font-weight: 800;
  letter-spacing: -1px;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--color-text-secondary);
  line-height: 1.7;
  margin-bottom: var(--spacing-2xl);
  max-width: 550px;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-2xl);
}

.btn-primary {
  display: inline-block;
  background-color: var(--color-accent);
  color: white;
  padding: 1rem 2.5rem;
  border-radius: var(--radius-full);
  font-weight: 600;
  font-size: 1.125rem;
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
}

.btn-primary:hover {
  background-color: var(--color-accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(255, 107, 53, 0.5);
}

.trust-indicator {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}

.avatars {
  display: flex;
}

.avatar {
  background: var(--color-primary-lighter);
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  border: 2px solid var(--color-bg-main);
  margin-left: -10px;
}

.avatar:first-child {
  margin-left: 0;
}

.trust-text {
  color: var(--color-text-secondary);
  font-size: 0.9rem;
  font-weight: 500;
}

.hero-visual {
  flex: 1;
  position: relative;
  display: flex;
  justify-content: center;
}

.image-container {
  position: relative;
  width: 100%;
  max-width: 600px;
}

.glow-effect {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  height: 80%;
  background: radial-gradient(circle, rgba(16, 185, 129, 0.2) 0%, transparent 70%);
  filter: blur(40px);
  z-index: -1;
}

.hero-image {
  width: 100%;
  height: auto;
  object-fit: contain;
  filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));
}

@media (max-width: 1024px) {
  .hero-container {
    flex-direction: column;
    text-align: center;
    padding-top: var(--spacing-2xl);
  }
  
  .hero-content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .hero-title {
    font-size: 3.5rem;
  }
  
  .hero-actions {
    flex-direction: column;
    gap: var(--spacing-lg);
  }
}
</style>
