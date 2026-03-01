<script setup>
</script>

<template>
  <section class="hero-wrapper">
    <!-- Decorative background elements -->
    <div class="bg-shape-large text-gradient"></div>
    <div class="bg-dot-grid"></div>
    
    <div class="hero-container">
      <div class="hero-content">
        <h1 class="hero-title">
          YOUR PARTNER<br/>
          IN LEARNING FOR<br/>
          <span class="text-gradient">COLLABORATIVE<br/>SUCCESS</span>
        </h1>
        <p class="hero-subtitle">
          BrightPath: The centralized peer-to-peer LMS for University Students. Share, access, and rank resources for collaborative success.
        </p>
        
        <div class="hero-actions">
          <RouterLink to="/login" class="btn btn-primary">BUY NOW</RouterLink>
          <RouterLink to="/library" class="btn btn-secondary">View Demo</RouterLink>
        </div>
        
        <!-- Small decorative floating shapes -->
        <div class="floating-shape square"></div>
        <div class="floating-shape circle"></div>
      </div>
      
      <div class="hero-visual">
        <div class="image-frame">
          <div class="teal-accent-bg"></div>
          <img src="/student_laptop.png" alt="University student using BrightPath LMS" class="hero-image" />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-wrapper {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  overflow: hidden;
  padding-top: 80px; /* Offset for absolute navbar */
}

/* Background diagonal layout approximation */
.hero-wrapper::before {
  content: '';
  position: absolute;
  top: 0;
  right: -5%;
  width: 55%;
  height: 100%;
  background-color: #8daea5; /* Teal section behind image */
  transform: skewX(-15deg);
  z-index: -1;
}

.hero-wrapper::after {
  content: '';
  position: absolute;
  top: 0;
  right: -5%;
  width: 55%;
  height: 50%;
  background-color: #63938b; /* Darker teal top */
  transform: skewX(-15deg);
  z-index: -2;
}

.hero-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--spacing-2xl);
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  width: 100%;
  z-index: 10;
}

.hero-content {
  flex: 1;
  max-width: 600px;
  padding: var(--spacing-3xl) 0;
  position: relative;
}

.hero-title {
  font-size: 3.5rem;
  line-height: 1.1;
  color: var(--color-primary);
  margin-bottom: var(--spacing-md);
  font-weight: 800;
  text-transform: uppercase;
}

.text-gradient {
  color: var(--color-accent); /* Make it plain bright blue as per image */
}

.hero-subtitle {
  font-size: 1.1rem;
  color: var(--color-text-secondary);
  line-height: 1.6;
  margin-bottom: var(--spacing-2xl);
  max-width: 500px;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-xl);
}

.btn {
  display: inline-block;
  padding: 0.8rem 2.5rem;
  border-radius: var(--radius-full);
  font-weight: 600;
  font-size: 1rem;
  text-decoration: none;
  transition: all 0.3s ease;
}

.btn-primary {
  background-color: var(--color-accent);
  color: white;
  box-shadow: 0 4px 14px rgba(108, 124, 242, 0.4);
}

.btn-primary:hover {
  background-color: var(--color-accent-hover);
  transform: translateY(-2px);
}

.btn-secondary {
  background-color: transparent;
  color: var(--color-primary);
}

.btn-secondary:hover {
  text-decoration: underline;
}

.hero-visual {
  flex: 1;
  position: relative;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}

.image-frame {
  position: relative;
  width: 120%;
  height: 90%;
  margin-right: -20%;
  margin-bottom: -5%;
  z-index: 5;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  clip-path: polygon(15% 0, 100% 0, 100% 100%, 0% 100%);
  border-radius: var(--radius-lg);
  box-shadow: rgba(0,0,0,0.2) 0px 20px 40px;
}

/* Decorative elements */
.floating-shape {
  position: absolute;
  background-color: var(--color-accent);
  opacity: 0.8;
}

.square {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  bottom: 0;
  left: 30%;
  box-shadow: 4px 4px 0px rgba(108, 124, 242, 0.3);
}

.circle {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: 4px solid var(--color-accent);
  background-color: transparent;
  bottom: 20%;
  right: 10%;
}

.bg-dot-grid {
  position: absolute;
  bottom: 10%;
  left: 5%;
  width: 100px;
  height: 100px;
  background-image: radial-gradient(#cbd5e1 2px, transparent 2px);
  background-size: 15px 15px;
  opacity: 0.6;
}

@media (max-width: 1024px) {
  .hero-wrapper::before, .hero-wrapper::after {
    display: none;
  }
  .hero-container {
    flex-direction: column;
    padding-top: var(--spacing-2xl);
  }
  .image-frame {
    width: 100%;
    margin-right: 0;
    margin-top: var(--spacing-xl);
  }
  .hero-image {
    clip-path: none;
    border-radius: var(--radius-lg);
  }
}
</style>
