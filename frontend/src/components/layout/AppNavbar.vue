<script setup>
</script>

<template>
  <header class="navbar">
    <div class="navbar-container">
      <div class="brand">
        <RouterLink to="/" class="brand-link">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" class="brand-icon">
            <path d="M4 19V5C4 3.89543 4.89543 3 6 3H19V19C19 20.1046 18.1046 21 17 21H6C4.89543 21 4 20.1046 4 19Z" stroke="#6c7cf2" stroke-width="2"/>
            <path d="M4 15L15 3" stroke="#6c7cf2" stroke-width="2"/>
            <path d="M10 12L10 21" stroke="#6c7cf2" stroke-width="1" stroke-dasharray="2 2"/>
            <path d="M14 12L14 21" stroke="#6c7cf2" stroke-width="1" stroke-dasharray="2 2"/>
          </svg>
          BrightPath
        </RouterLink>
      </div>
      
      <nav class="nav-links">
        <RouterLink to="/" class="nav-link" active-class="active">HOME</RouterLink>
        <RouterLink to="/library" class="nav-link" active-class="active">LIBRARY</RouterLink>
        <RouterLink to="/dashboard" class="nav-link" active-class="active">KUPPI</RouterLink>
        <RouterLink to="/login" class="nav-link" active-class="active">LOGIN</RouterLink>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.navbar {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
  padding: var(--spacing-md) 0;
}

.navbar-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--spacing-2xl);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-link {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--color-primary);
  text-decoration: none;
  letter-spacing: -0.5px;
}

.nav-links {
  display: flex;
  gap: var(--spacing-2xl);
}

.nav-link {
  color: var(--color-primary);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  letter-spacing: 0.5px;
  position: relative;
  padding-bottom: 4px;
}

.nav-link:hover {
  color: var(--color-accent);
}

.nav-link.active {
  color: var(--color-primary);
}

.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--color-primary);
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
}
</style>
