<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible')
      }
    })
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' })

  document.querySelectorAll('.animate-on-scroll').forEach((el) => {
    observer.observe(el)
  })
})
</script>

<template>
  <main class="min-h-screen bg-slate-50 pt-24 pb-20 overflow-hidden">
    <!-- Hero Section -->
    <section class="max-w-[1200px] mx-auto px-4 lg:px-8 mb-24 relative">
      <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-blue-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 -z-10 animate-blob"></div>
      <div class="absolute top-0 left-0 w-[400px] h-[400px] bg-sky-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 -z-10 animate-blob animation-delay-2000"></div>

      <div class="text-center pt-16 pb-8 animate-on-scroll fade-up">
        <h1 class="text-[3.5rem] lg:text-[5rem] font-extrabold text-slate-900 leading-[1.1] mb-6 tracking-tight">
          Illuminate Your <br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-sky-400">
            Academic Path
          </span>
        </h1>
        <p class="text-xl text-slate-600 max-w-[800px] mx-auto leading-relaxed">
          BrightPath is a comprehensive, web-based Learning Management System specifically engineered for the university student community. We bridge the gap between academic resource availability and student accessibility through structured, peer-to-peer knowledge sharing.
        </p>
      </div>
    </section>

    <!-- Project Aims Strip -->
    <section class="bg-blue-600 py-16 mb-24">
      <div class="max-w-[1200px] mx-auto px-4 lg:px-8">
        <div class="flex flex-col md:flex-row items-center justify-between gap-12 text-white animate-on-scroll fade-up">
          <div class="flex-1">
            <h2 class="text-3xl font-bold mb-4">Our Main Objective</h2>
            <p class="text-blue-100 text-lg leading-relaxed">
              To develop a centralized, secure, and smart Peer-to-Peer Learning Management System that optimizes academic resource sharing and collaborative learning among university students everywhere.
            </p>
          </div>
          <div class="grid grid-cols-2 gap-8 flex-1">
            <div class="text-center p-6 bg-white/10 rounded-2xl backdrop-blur-sm border border-white/20">
              <div class="text-4xl font-extrabold text-yellow-300 mb-2">100%</div>
              <div class="font-medium">Peer Powered</div>
            </div>
            <div class="text-center p-6 bg-white/10 rounded-2xl backdrop-blur-sm border border-white/20">
              <div class="text-4xl font-extrabold text-yellow-300 mb-2">24/7</div>
              <div class="font-medium">Real-time Access</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Values -->
    <section class="max-w-[1200px] mx-auto px-4 lg:px-8 mb-32">
      <div class="text-center mb-16 animate-on-scroll fade-up">
        <h2 class="text-3xl lg:text-4xl font-bold text-slate-900 mb-4">Value to Students</h2>
        <p class="text-lg text-slate-500">Why BrightPath is the ultimate tool for modern education.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="bg-white p-8 rounded-3xl shadow-lg border border-slate-100 hover:-translate-y-2 transition-transform duration-300 animate-on-scroll fade-up stagger-1">
          <div class="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center mb-6">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-3">Time Saving</h3>
          <p class="text-slate-500">Quickly locate the precise notes, papers, and recordings you need without endless searching.</p>
        </div>

        <div class="bg-white p-8 rounded-3xl shadow-lg border border-slate-100 hover:-translate-y-2 transition-transform duration-300 animate-on-scroll fade-up stagger-2">
          <div class="w-14 h-14 bg-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center mb-6">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-3">Quality Content</h3>
          <p class="text-slate-500">Community-driven ranking logic ensures the best and most accurate materials stay at the top.</p>
        </div>

        <div class="bg-white p-8 rounded-3xl shadow-lg border border-slate-100 hover:-translate-y-2 transition-transform duration-300 animate-on-scroll fade-up stagger-3">
          <div class="w-14 h-14 bg-green-50 text-green-600 rounded-2xl flex items-center justify-center mb-6">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-3">Peer Learning</h3>
          <p class="text-slate-500">Collaborate directly through live "Kuppi" sessions synced instantly with Google Classroom.</p>
        </div>

        <div class="bg-white p-8 rounded-3xl shadow-lg border border-slate-100 hover:-translate-y-2 transition-transform duration-300 animate-on-scroll fade-up stagger-4">
          <div class="w-14 h-14 bg-orange-50 text-orange-600 rounded-2xl flex items-center justify-center mb-6">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-3">Personalized</h3>
          <p class="text-slate-500">A dynamic dashboard tailored perfectly to your specific academic year and course stream.</p>
        </div>
      </div>
    </section>

    <!-- Core Functions & Tech Side-by-Side -->
    <section class="max-w-[1200px] mx-auto px-4 lg:px-8 mb-24">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <div class="animate-on-scroll fade-right">
          <h2 class="text-3xl font-bold text-slate-900 mb-8">Modern Features Built for You</h2>
          
          <div class="space-y-8">
            <div class="flex gap-4">
              <div class="w-12 h-12 bg-sky-100 text-sky-600 rounded-full flex items-center justify-center shrink-0">
                <span class="font-bold">1</span>
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-900">Identity & verified Access</h4>
                <p class="text-slate-500">Implemented with secure JWT authentication and strict backend verification criteria for authorized students and staff.</p>
              </div>
            </div>

            <div class="flex gap-4">
              <div class="w-12 h-12 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center shrink-0">
                <span class="font-bold">2</span>
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-900">Library & Gamification</h4>
                <p class="text-slate-500">A robust PDF engine and point system to incentivize top contributors to share reliable lecture materials.</p>
              </div>
            </div>

            <div class="flex gap-4">
              <div class="w-12 h-12 bg-indigo-100 text-indigo-600 rounded-full flex items-center justify-center shrink-0">
                <span class="font-bold">3</span>
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-900">Automation & Intelligence</h4>
                <p class="text-slate-500">Powered by Redit & Celery for asynchronous background management, delivering real-time Gmail alerts on uploads.</p>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-slate-900 rounded-3xl p-10 text-white relative overflow-hidden animate-on-scroll fade-left">
          <!-- decorative blur -->
          <div class="absolute top-[-20%] right-[-20%] w-64 h-64 bg-blue-500 rounded-full mix-blend-screen filter blur-3xl opacity-40"></div>
          
          <h3 class="text-2xl font-bold mb-8 relative z-10">Our Technology Stack</h3>
          <div class="grid grid-cols-2 gap-6 relative z-10 font-medium">
            <div class="flex items-center gap-3">
              <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg" class="w-6 h-6" alt="Vue"> Vue.js Frontend
            </div>
            <div class="flex items-center gap-3">
              <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" class="w-6 h-6" alt="Python"> Django Backend
            </div>
            <div class="flex items-center gap-3">
              <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg" class="w-6 h-6" alt="PostgreSQL"> PostgreSQL
            </div>
            <div class="flex items-center gap-3">
              <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" class="w-8 h-6 object-contain" alt="AWS"> AWS S3 Storage
            </div>
            <div class="flex items-center gap-3 col-span-2">
              <img src="https://upload.wikimedia.org/wikipedia/commons/5/59/Google_Classroom_Logo.png" class="w-6 h-6" alt="Classroom"> Google Classroom API Integration
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Target Users -->
    <section class="max-w-[1200px] mx-auto px-4 lg:px-8 mt-16 mb-16 text-center animate-on-scroll fade-up">
      <h2 class="text-3xl font-bold text-slate-900 mb-12">Who Is It For?</h2>
      <div class="flex flex-wrap justify-center gap-6">
        <span class="px-8 py-4 bg-white shadow-sm border border-slate-200 rounded-full font-bold text-lg text-slate-700 hover:border-blue-500 hover:text-blue-600 transition-colors">🎓 University Students</span>
        <span class="px-8 py-4 bg-white shadow-sm border border-slate-200 rounded-full font-bold text-lg text-slate-700 hover:border-blue-500 hover:text-blue-600 transition-colors">👨‍🏫 Academic Staff / Teachers</span>
        <span class="px-8 py-4 bg-white shadow-sm border border-slate-200 rounded-full font-bold text-lg text-slate-700 hover:border-blue-500 hover:text-blue-600 transition-colors">⚙️ System Administrators</span>
      </div>
    </section>

  </main>
</template>

<style scoped>
/* Scroll Animation Classes */
.animate-on-scroll {
  opacity: 0;
  will-change: transform, opacity;
  transition: opacity 0.8s ease-out, transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.fade-up {
  transform: translateY(40px);
}

.fade-left {
  transform: translateX(40px);
}

.fade-right {
  transform: translateX(-40px);
}

.is-visible {
  opacity: 1;
  transform: translate(0, 0);
}

.stagger-1 { transition-delay: 100ms; }
.stagger-2 { transition-delay: 200ms; }
.stagger-3 { transition-delay: 300ms; }
.stagger-4 { transition-delay: 400ms; }

/* Blob Animation */
@keyframes blob {
  0% { transform: translate(0px, 0px) scale(1); }
  33% { transform: translate(30px, -50px) scale(1.1); }
  66% { transform: translate(-20px, 20px) scale(0.9); }
  100% { transform: translate(0px, 0px) scale(1); }
}

.animate-blob {
  animation: blob 7s infinite;
}

.animation-delay-2000 {
  animation-delay: 2s;
}
</style>
