<script setup>
</script>

<template>
  <header class="navbar glass-panel">
    <div class="navbar-container">
      <div class="brand">
        <RouterLink to="/" class="brand-link">BrightPath</RouterLink>
      </div>
      
      <nav class="nav-links">
        <RouterLink to="/library" class="nav-link">Library</RouterLink>
        <RouterLink to="/dashboard" class="nav-link">Dashboard</RouterLink>
      </nav>

      <div class="nav-actions">
        <RouterLink to="/login" class="btn btn-outline">Sign In</RouterLink>
        <RouterLink to="/login" class="btn btn-primary">Start Learning</RouterLink>
      </div>
    </div>
  </header>
</template>

<style scoped>
.navbar {
  position: sticky;
  top: 1rem;
  z-index: 100;
  margin: 0 var(--spacing-xl);
  border-radius: var(--radius-full);
}

.navbar-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: var(--spacing-sm) var(--spacing-2xl);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-link {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--color-text-primary);
  text-decoration: none;
  letter-spacing: -0.5px;
}

.nav-links {
  display: flex;
  gap: var(--spacing-2xl);
}

.nav-link {
  color: var(--color-text-secondary);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
  font-size: 0.95rem;
}

.nav-link:hover, .nav-link.router-link-active {
  color: var(--color-success);
}

.nav-actions {
  display: flex;
  gap: var(--spacing-md);
  align-items: center;
}

.btn {
  padding: 0.6rem 1.5rem;
  border-radius: var(--radius-full);
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.btn-outline {
  color: var(--color-text-primary);
  border: 1px solid var(--glass-border);
  background: transparent;
}

.btn-outline:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.2);
}

.btn-primary {
  background-color: var(--color-accent);
  color: white;
  border: none;
  box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
}

.btn-primary:hover {
  background-color: var(--color-accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4);
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
  .navbar {
    margin: var(--spacing-sm);
  }
  .navbar-container {
    padding: var(--spacing-sm) var(--spacing-lg);
  }
}
</style>
