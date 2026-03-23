<script setup>
</script>

<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h3 class="brand-name">BrightPath</h3>
          <p>Empowering Peer-to-Peer Learning.</p>
        </div>
        
        <div class="footer-links">
          <h4>Quick Links</h4>
          <ul>
            <li><RouterLink to="/library">Digital Library</RouterLink></li>
            <li><RouterLink to="/dashboard">Module Search</RouterLink></li>
            <li><a href="#">Support</a></li>
          </ul>
        </div>

        <div class="footer-stats">
          <h4>Platform Stats</h4>
          <div class="stats-grid">
            <div class="stat-item">
              <span class="stat-value">5k+</span>
              <span class="stat-label">Total Resources</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">1.2k</span>
              <span class="stat-label">Active Students</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">50+</span>
              <span class="stat-label">Verified Teachers</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>&copy; 2026 BrightPath LMS. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: var(--color-text-primary);
  color: white;
  padding: var(--spacing-4xl) 0 var(--spacing-xl);
  margin-top: auto;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-xl);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 2fr;
  gap: var(--spacing-3xl);
  margin-bottom: var(--spacing-3xl);
}

.brand-name {
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: var(--spacing-sm);
  color: var(--color-primary-light);
}

.footer-brand p {
  color: #a0aec0;
  font-size: 0.95rem;
}

.footer-links h4, .footer-stats h4 {
  font-size: 1.125rem;
  margin-bottom: var(--spacing-lg);
  color: white;
}

.footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.footer-links a {
  color: #a0aec0;
  text-decoration: none;
  transition: color 0.2s;
}

.footer-links a:hover {
  color: var(--color-primary-light);
}

.stats-grid {
  display: flex;
  gap: var(--spacing-xl);
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: var(--color-accent);
  line-height: 1;
  margin-bottom: var(--spacing-xs);
}

.stat-label {
  font-size: 0.875rem;
  color: #a0aec0;
}

.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.1);
  padding-top: var(--spacing-xl);
  text-align: center;
  color: #718096;
  font-size: 0.875rem;
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: var(--spacing-2xl);
  }
  
  .stats-grid {
    flex-direction: column;
    gap: var(--spacing-md);
  }
}
</style>
