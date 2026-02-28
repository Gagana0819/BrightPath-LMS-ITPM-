<script setup>
</script>

<template>
  <section class="kuppi-sync">
    <div class="sync-container glass-panel">
      <div class="sync-content">
        <h2 class="text-gradient">Live "Kuppi" Sync</h2>
        <p>Real-time collaboration synced directly with Google Classroom.</p>
        <ul class="feature-list">
          <li><span>🎙️</span> Instant Voice Channels</li>
          <li><span>💬</span> Real-time Peer Chat</li>
          <li><span>📅</span> Automatic Schedule Sync</li>
        </ul>
      </div>

      <div class="split-screen-mockup">
        <!-- Mockup Video/Classroom Area -->
        <div class="video-area">
          <div class="mockup-header">
            <div class="dots">
              <span></span><span></span><span></span>
            </div>
            <div class="title">ITPM Exam Review</div>
          </div>
          <div class="video-grid">
            <div class="video-cell presenter">Lecturer Presenting...</div>
            <div class="video-cell student">Student 01</div>
            <div class="video-cell student">Alice S.</div>
            <div class="video-cell student">John D.</div>
          </div>
        </div>

        <!-- Mockup Chat Area -->
        <div class="chat-area">
          <div class="chat-messages">
            <div class="message msg-other">
              <span class="user">Student 01</span>
              <p>Can we go over the ER diagrams again?</p>
            </div>
            <div class="message msg-self">
              <span class="user">You</span>
              <p>Yes, I just shared a PDF in the library.</p>
            </div>
          </div>
          <div class="chat-input">Type a message...</div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.kuppi-sync {
  padding: var(--spacing-4xl) var(--spacing-xl);
  max-width: 1400px;
  margin: 0 auto;
}

.sync-container {
  display: flex;
  align-items: center;
  gap: var(--spacing-4xl);
  padding: var(--spacing-3xl);
  background: linear-gradient(145deg, rgba(17,34,64,0.6), rgba(10,25,47,0.4));
  overflow: hidden;
}

.sync-content {
  flex: 1;
  max-width: 400px;
}

.sync-content h2 {
  font-size: 2.5rem;
  margin-bottom: var(--spacing-md);
  font-weight: 800;
}

.sync-content p {
  font-size: 1.125rem;
  color: var(--color-text-secondary);
  margin-bottom: var(--spacing-xl);
}

.feature-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.feature-list li {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  font-size: 1.05rem;
  color: var(--color-text-primary);
  background: rgba(255,255,255,0.03);
  padding: 0.75rem 1rem;
  border-radius: var(--radius-md);
  border: 1px solid rgba(255,255,255,0.02);
}

.split-screen-mockup {
  flex: 1.5;
  display: flex;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  border: 1px solid var(--glass-border);
  height: 400px;
}

/* Video Side */
.video-area {
  flex: 2;
  background-color: #111; /* Dark for video */
  display: flex;
  flex-direction: column;
}

.mockup-header {
  background: #2a2a2a;
  padding: 0.5rem 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  border-bottom: 1px solid #000;
}

.dots {
  display: flex;
  gap: 6px;
}

.dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #555;
}

.dots span:nth-child(1) { background: #ff5f56; }
.dots span:nth-child(2) { background: #ffbd2e; }
.dots span:nth-child(3) { background: #27c93f; }

.mockup-header .title {
  color: #ccc;
  font-size: 0.85rem;
  font-weight: 600;
}

.video-grid {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 2fr 1fr;
  gap: 4px;
  padding: 4px;
  background: #000;
}

.video-cell {
  background: #222;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #888;
  font-size: 0.8rem;
}

.presenter {
  grid-column: 1 / -1; /* Spans full width */
  font-size: 1.2rem;
  color: #eee;
  background: linear-gradient(45deg, #1a2a3a, #0a192f);
}

/* Chat Side */
.chat-area {
  flex: 1;
  background: var(--color-primary-light);
  border-left: 1px solid var(--glass-border);
  display: flex;
  flex-direction: column;
}

.chat-messages {
  flex: 1;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  overflow-y: auto;
}

.message {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  max-width: 90%;
}

.message .user {
  font-size: 0.75rem;
  color: var(--color-text-secondary);
  font-weight: bold;
}

.message p {
  padding: 0.5rem 0.75rem;
  border-radius: var(--radius-md);
  font-size: 0.85rem;
  line-height: 1.4;
}

.msg-other {
  align-self: flex-start;
}

.msg-other p {
  background: var(--color-primary-lighter);
  color: var(--color-text-primary);
  border-bottom-left-radius: 2px;
}

.msg-self {
  align-self: flex-end;
  text-align: right;
}

.msg-self p {
  background: var(--color-accent);
  color: white;
  border-bottom-right-radius: 2px;
}

.chat-input {
  padding: 1rem;
  background: rgba(0,0,0,0.2);
  color: var(--color-text-secondary);
  font-size: 0.85rem;
  border-top: 1px solid var(--glass-border);
}

@media (max-width: 1024px) {
  .sync-container {
    flex-direction: column;
  }
  .split-screen-mockup {
    width: 100%;
  }
}

@media (max-width: 600px) {
  .chat-area {
    display: none; /* Hide chat on mobile mockup */
  }
}
</style>
