<script setup>
</script>

<template>
  <section class="gamification">
    <div class="gamification-content">
      <h2 class="text-gradient">Top 5 Contributors</h2>
      <p>Climb the leaderboard by sharing high-quality, verified study materials.</p>
    </div>

    <div class="leaderboard-widget glass-panel">
      <div class="leaderboard-header">
        <h3>🏆 Weekly Standings</h3>
        <span class="live-dot"><span class="dot"></span> Live</span>
      </div>
      
      <ul class="leaderboard-list">
        <!-- Rank 1: Gold -->
        <li class="leaderboard-item rank-1">
          <div class="rank-medal gold">🥇</div>
          <div class="user-info">
            <span class="name">Student 01</span>
            <span class="badge">Master Sharer</span>
          </div>
          <div class="score">
            <span class="points text-gradient">1,250 pts</span>
          </div>
        </li>

        <!-- Rank 2: Silver -->
        <li class="leaderboard-item rank-2">
          <div class="rank-medal silver">🥈</div>
          <div class="user-info">
            <span class="name">Alice Smith</span>
          </div>
          <div class="score">
            <span class="points">980 pts</span>
          </div>
        </li>

        <!-- Rank 3: Bronze -->
        <li class="leaderboard-item rank-3">
          <div class="rank-medal bronze">🥉</div>
          <div class="user-info">
            <span class="name">John Doe</span>
          </div>
          <div class="score">
            <span class="points">845 pts</span>
          </div>
        </li>

        <!-- Rank 4 -->
        <li class="leaderboard-item">
          <div class="rank-medal">4</div>
          <div class="user-info">
            <span class="name">Sarah K.</span>
          </div>
          <div class="score">
            <span class="points">720 pts</span>
          </div>
        </li>

        <!-- Rank 5 -->
        <li class="leaderboard-item">
          <div class="rank-medal">5</div>
          <div class="user-info">
            <span class="name">Michael T.</span>
          </div>
          <div class="score">
            <span class="points">615 pts</span>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.gamification {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--spacing-4xl) var(--spacing-xl);
  max-width: 800px;
  margin: 0 auto;
}

.gamification-content {
  text-align: center;
  margin-bottom: var(--spacing-2xl);
}

.gamification-content h2 {
  font-size: 2.75rem;
  margin-bottom: var(--spacing-sm);
  font-weight: 800;
}

.gamification-content p {
  font-size: 1.125rem;
  color: var(--color-text-secondary);
}

.leaderboard-widget {
  width: 100%;
  padding: 0;
  overflow: hidden;
  background: rgba(10, 25, 47, 0.7); /* Deep intense dark */
  border: 1px solid rgba(255, 255, 255, 0.05);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

.leaderboard-header {
  padding: var(--spacing-lg) var(--spacing-xl);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(0,0,0,0.2);
}

.leaderboard-header h3 {
  font-size: 1.1rem;
  color: var(--color-text-primary);
  margin: 0;
}

.live-dot {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  color: var(--color-success);
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.live-dot .dot {
  width: 8px;
  height: 8px;
  background: var(--color-success);
  border-radius: 50%;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
  70% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
  100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.leaderboard-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.leaderboard-item {
  display: flex;
  align-items: center;
  padding: var(--spacing-md) var(--spacing-xl);
  border-bottom: 1px solid rgba(255,255,255,0.03);
  transition: background 0.3s ease;
}

.leaderboard-item:hover {
  background: rgba(255,255,255,0.02);
}

.leaderboard-item:last-child {
  border-bottom: none;
}

.rank-medal {
  width: 40px;
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--color-text-secondary);
  text-align: center;
}

.rank-1 .rank-medal, .rank-2 .rank-medal, .rank-3 .rank-medal {
  font-size: 2rem;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
}

.user-info {
  flex: 1;
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  margin-left: var(--spacing-md);
}

.name {
  font-weight: 600;
  color: var(--color-text-primary);
  font-size: 1.1rem;
}

.badge {
  background: rgba(16, 185, 129, 0.1);
  color: var(--color-success);
  font-size: 0.75rem;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  border: 1px solid rgba(16, 185, 129, 0.3);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: bold;
}

.score {
  text-align: right;
}

.points {
  font-weight: 800;
  font-size: 1.15rem;
  color: var(--color-text-secondary);
}

.rank-1 {
  background: linear-gradient(to right, rgba(255, 215, 0, 0.05), transparent);
}
.rank-1 .points {
  font-size: 1.25rem;
}

@media (max-width: 600px) {
  .leaderboard-item {
    padding: var(--spacing-md);
  }
}
</style>
