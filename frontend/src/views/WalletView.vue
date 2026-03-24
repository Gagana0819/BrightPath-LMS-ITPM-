<script setup>
import { ref } from 'vue'

// Points wallet data
const walletData = ref({
  totalPoints: 3450,
  tier: 'Gold',
  tierProgress: 85,
  pointsToNext: 150,
  recentActivity: [
    { action: 'Downloaded', doc: 'ITPM Midterm Paper', points: -20, time: '2h ago' },
    { action: 'Uploaded', doc: 'OOP Notes', points: +50, time: '1d ago' },
    { action: 'Review Bonus', doc: 'SQL Joins Summary', points: +15, time: '2d ago' },
  ]
})
</script>

<template>
  <div class="wallet-view p-6 lg:p-10 animate-fade-in">
    <div class="max-w-[1200px] mx-auto">
      <header class="mb-10 text-center lg:text-left">
        <h1 class="text-3xl font-extrabold text-[#2C3E50] tracking-tight mb-2 uppercase tracking-[0.2em]">My Gamified Wallet</h1>
        <div class="h-1 w-20 bg-[#4A90E2] mx-auto lg:mx-0 mb-4 rounded-full"></div>
        <p class="text-slate-500 font-medium">Track your contributions, earn points, and climb the leadership ranks.</p>
      </header>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Main Wallet Column -->
        <div class="lg:col-span-2 space-y-8 order-2 lg:order-1">
          <!-- Points Wallet Card -->
          <div class="bg-gradient-to-br from-[#2C3E50] to-[#1a2636] rounded-3xl p-8 text-white shadow-2xl relative overflow-hidden group border border-[#4A90E2]/20">
            <!-- Decorative background overlay for premium feel -->
            <div class="absolute inset-0 bg-[url('/hero BG.png')] opacity-20 mix-blend-overlay pointer-events-none"></div>
            <div class="absolute -top-12 -right-12 w-64 h-64 bg-[#4A90E2]/20 rounded-full blur-3xl group-hover:bg-[#4A90E2]/30 transition-colors duration-500"></div>
            <div class="absolute -bottom-16 -left-16 w-48 h-48 bg-[#A8E6CF]/15 rounded-full blur-2xl"></div>

            <div class="relative z-10">
              <div class="flex items-center justify-between mb-12">
                <h3 class="text-slate-300 font-bold tracking-widest text-sm uppercase">BrightPath Points Balance</h3>
                <div class="bg-[#4A90E2]/20 p-3 rounded-2xl border border-[#4A90E2]/30 backdrop-blur-md">
                  <svg class="w-6 h-6 text-[#4A90E2]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
              </div>

              <div class="flex items-end gap-4 mb-8">
                <span class="text-7xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-white via-white to-slate-400">
                  {{ walletData.totalPoints.toLocaleString() }}
                </span>
                <span class="text-[#4A90E2] text-2xl font-black pb-3 flex items-center gap-1">
                  <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                  </svg>
                  BP
                </span>
              </div>

              <!-- Tier Progress -->
              <div class="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-md mb-8 ring-1 ring-white/10">
                <div class="flex justify-between items-center mb-4">
                  <div class="flex flex-col">
                    <span class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Current Tier</span>
                    <span class="text-lg font-black text-[#FFB800] uppercase tracking-wider flex items-center gap-2">
                      🏆 {{ walletData.tier }} Member
                    </span>
                  </div>
                  <div class="text-right">
                    <span class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1 block">Next Goal</span>
                    <span class="text-sm font-bold text-white">Platinum Tier</span>
                  </div>
                </div>
                <!-- Premium Progress Bar -->
                <div class="w-full bg-slate-900/50 rounded-full h-4 mb-3 overflow-hidden p-[3px] border border-white/10">
                  <div class="bg-gradient-to-r from-[#4A90E2] via-[#4A90E2] to-[#FFB800] h-full rounded-full transition-all duration-1000 shadow-[0_0_15px_rgba(74,144,226,0.5)] relative overflow-hidden" :style="{ width: walletData.tierProgress + '%' }">
                    <!-- Shimmer effect -->
                    <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent skew-x-[45deg] -translate-x-full animate-shimmer"></div>
                  </div>
                </div>
                <div class="flex justify-between items-center">
                  <p class="text-xs font-medium text-slate-400 italic">"Keep contributing to earn more rewards"</p>
                  <p class="text-xs font-bold text-slate-300">{{ walletData.pointsToNext }} BP remaining</p>
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <button class="py-4 bg-[#4A90E2] text-white rounded-2xl font-black hover:bg-[#3A7BC8] transition-all text-sm shadow-xl hover:shadow-[#4A90E2]/30 active:scale-95 flex items-center justify-center gap-2 group">
                  <span>Redeem Rewards</span>
                  <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
                    <path d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </button>
                <button class="py-4 bg-white/10 text-white border border-white/10 rounded-2xl font-black hover:bg-white/20 transition-all text-sm backdrop-blur-sm active:scale-95 flex items-center justify-center gap-2">
                  <span>View Benefits</span>
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                    <path d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <!-- Activity History -->
          <div class="bg-white rounded-3xl p-8 shadow-sm border border-slate-100 animate-fade-in-up delay-100">
            <div class="flex items-center justify-between mb-8">
               <h3 class="text-lg font-extrabold text-[#2C3E50] flex items-center gap-2">
                <svg class="w-5 h-5 text-[#4A90E2]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Recent Activity
              </h3>
              <button class="text-xs font-bold text-[#4A90E2] hover:underline uppercase tracking-wider">Download Statement</button>
            </div>
            
            <div class="space-y-0 text-slate-600">
              <div
                v-for="(activity, i) in walletData.recentActivity"
                :key="i"
                class="flex items-center justify-between py-5 border-b border-slate-50 last:border-0 hover:bg-slate-50/50 px-4 -mx-4 rounded-xl transition-all cursor-default group"
              >
                <div class="flex items-center gap-4">
                  <div class="w-12 h-12 rounded-2xl bg-[#F4F7F9] flex items-center justify-center shrink-0 group-hover:bg-white group-hover:shadow-sm border border-transparent group-hover:border-slate-100 transition-all">
                    <svg v-if="activity.points > 0" class="w-6 h-6 text-[#A8E6CF]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18" />
                    </svg>
                    <svg v-else class="w-6 h-6 text-red-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                    </svg>
                  </div>
                  <div>
                    <p class="font-bold text-[#2C3E50] text-[0.95rem] group-hover:text-[#4A90E2] transition-colors">{{ activity.action }}</p>
                    <p class="text-xs text-slate-400 font-medium uppercase tracking-tighter">{{ activity.doc }} · {{ activity.time }}</p>
                  </div>
                </div>
                <div class="flex flex-col items-end">
                  <span class="text-base font-black tabular-nums" :class="activity.points > 0 ? 'text-[#2e7d32]' : 'text-slate-500'">
                    {{ activity.points > 0 ? '+' : '' }}{{ activity.points }} BP
                  </span>
                  <span class="text-[10px] text-slate-400 font-bold uppercase">Points Status</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Side Stats -->
        <div class="space-y-8 animate-fade-in-up delay-200 order-1 lg:order-2">
          <!-- Library Stats -->
          <div class="bg-white rounded-3xl p-8 shadow-sm border border-slate-100 group/stats overflow-hidden relative">
            <div class="absolute -right-4 -top-4 w-20 h-20 bg-[#4A90E2]/5 rounded-full scale-0 group-hover/stats:scale-100 transition-transform duration-500"></div>
            <h3 class="font-black text-[#2C3E50] mb-6 uppercase tracking-[0.2em] text-[10px] opacity-60">Global Impact</h3>
            <div class="grid grid-cols-2 gap-4">
              <div class="bg-[#F4F7F9] rounded-2xl p-5 border border-slate-100 hover:border-[#4A90E2]/30 transition-all hover:bg-white hover:shadow-md">
                <span class="block text-3xl font-black text-[#4A90E2] mb-1">5k+</span>
                <span class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">Resources</span>
              </div>
              <div class="bg-[#F4F7F9] rounded-2xl p-5 border border-slate-100 hover:border-[#4A90E2]/30 transition-all hover:bg-white hover:shadow-md">
                <span class="block text-3xl font-black text-[#2C3E50] mb-1">1.2k</span>
                <span class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">Students</span>
              </div>
              <div class="bg-[#F4F7F9] rounded-2xl p-5 border border-slate-100 hover:border-[#4A90E2]/30 transition-all hover:bg-white hover:shadow-md">
                <span class="block text-3xl font-black text-[#FFB800] mb-1">892</span>
                <span class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">Gold Ranked</span>
              </div>
              <div class="bg-[#A8E6CF]/10 rounded-2xl p-5 border border-[#A8E6CF]/20 hover:border-[#4A90E2]/30 transition-all hover:bg-white hover:shadow-md">
                <span class="block text-3xl font-black text-[#2C3E50] mb-1">50+</span>
                <span class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">Lecturers</span>
              </div>
            </div>
          </div>

          <!-- Top Contributors -->
          <div class="bg-white rounded-3xl p-8 shadow-sm border border-slate-100 relative overflow-hidden group/contri">
             <div class="absolute -left-12 -bottom-12 w-32 h-32 bg-[#FFB800]/5 rounded-full scale-0 group-hover/contri:scale-100 transition-transform duration-500"></div>
            <h3 class="font-black text-[#2C3E50] mb-8 uppercase tracking-[0.2em] text-[10px] opacity-60">Community Stars</h3>
            <div class="space-y-6 relative z-10">
              <div class="flex items-center gap-4 group cursor-default">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#FFB800] to-amber-200 flex items-center justify-center text-white font-black text-lg shadow-lg shadow-amber-200/50 group-hover:scale-110 transition-transform">1</div>
                <div class="flex-1">
                  <p class="font-bold text-[#2C3E50] group-hover:text-[#4A90E2] transition-colors">Kasun Silva</p>
                  <div class="flex items-center gap-2">
                    <span class="text-[10px] font-bold text-slate-400 uppercase tracking-tighter">42 uploads</span>
                    <span class="w-1 h-1 rounded-full bg-slate-200"></span>
                    <span class="text-[10px] font-black text-[#FFB800] uppercase">🏆 Gold</span>
                  </div>
                </div>
                <span class="font-black text-[#4A90E2] group-hover:scale-110 transition-transform">8.2k</span>
              </div>
              <div class="flex items-center gap-4 group cursor-default">
                <div class="w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center text-slate-400 font-black text-lg group-hover:bg-[#4A90E2]/10 group-hover:text-[#4A90E2] transition-all">2</div>
                <div class="flex-1">
                  <p class="font-bold text-[#2C3E50] group-hover:text-[#4A90E2] transition-colors">Sanduni M.</p>
                  <div class="flex items-center gap-2">
                    <span class="text-[10px] font-bold text-slate-400 uppercase tracking-tighter">38 uploads</span>
                    <span class="w-1 h-1 rounded-full bg-slate-200"></span>
                    <span class="text-[10px] font-black text-[#FFB800] uppercase">🏆 Gold</span>
                  </div>
                </div>
                <span class="font-black text-slate-400">7.6k</span>
              </div>
              <div class="flex items-center gap-4 group cursor-default">
                <div class="w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center text-slate-400 font-black text-lg group-hover:bg-[#4A90E2]/10 group-hover:text-[#4A90E2] transition-all">3</div>
                <div class="flex-1">
                  <p class="font-bold text-[#2C3E50] group-hover:text-[#4A90E2] transition-colors">Nuwan P.</p>
                  <div class="flex items-center gap-2">
                    <span class="text-[10px] font-bold text-slate-400 uppercase tracking-tighter">29 uploads</span>
                    <span class="w-1 h-1 rounded-full bg-slate-200"></span>
                    <span class="text-[10px] font-black text-slate-500 uppercase">🥈 Silver</span>
                  </div>
                </div>
                <span class="font-black text-slate-400">5.4k</span>
              </div>
            </div>
            <button class="w-full mt-8 py-3.5 bg-slate-50 hover:bg-[#2C3E50] hover:text-hero-highlight text-slate-500 rounded-xl text-[10px] font-black transition-all uppercase tracking-[0.2em] border border-slate-100 shadow-sm active:scale-95">
              View Leaderboard
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes shimmer {
  0% { transform: translateX(-100%) skewX(-45deg); }
  100% { transform: translateX(200%) skewX(-45deg); }
}

.animate-fade-in {
  animation: fadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.animate-fade-in-up {
  opacity: 0;
  animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.animate-shimmer {
  animation: shimmer 2s infinite ease-in-out;
}

.delay-100 { animation-delay: 0.2s; }
.delay-200 { animation-delay: 0.4s; }

.wallet-view {
  width: 100%;
  color-scheme: light;
}
</style>
