<script setup>
</script>

<template>
  <div class="bg-gradient-to-br from-[#1E293B] to-[#0F172A] rounded-2xl p-6 text-white shadow-xl relative overflow-hidden group border border-[#334155]">
    
    <!-- Decorative background elements -->
    <div class="absolute -top-12 -right-12 w-40 h-40 bg-hero-highlight/20 rounded-full blur-2xl group-hover:bg-hero-highlight/30 transition-colors duration-500"></div>
    <div class="absolute -bottom-8 -left-8 w-32 h-32 bg-[#FFB800]/10 rounded-full blur-xl"></div>
    
    <div class="relative z-10">
      <div class="flex items-center justify-between mb-8">
        <h3 class="text-slate-300 font-semibold tracking-wide text-sm uppercase">Your Points Wallet</h3>
        <button class="text-hero-highlight hover:text-white transition-colors bg-hero-highlight/10 p-2 rounded-xl border border-hero-highlight/20">
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
      </div>

      <div class="flex items-end gap-3 mb-6">
        <span class="text-5xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-white to-slate-400">
          3,450
        </span>
        <span class="text-hero-highlight font-bold pb-1.5 flex items-center gap-1">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
          </svg>
          BP
        </span>
      </div>

      <!-- Tier Status -->
      <div class="bg-white/5 border border-white/10 rounded-xl p-4 backdrop-blur-sm mb-6">
        <div class="flex justify-between items-center mb-2">
          <span class="text-sm font-medium text-slate-300">Current Tier</span>
          <span class="text-sm font-bold text-[#FFB800] uppercase tracking-wider flex items-center gap-1">
            Gold Member
          </span>
        </div>
        
        <div class="w-full bg-slate-800 rounded-full h-1.5 mb-2 overflow-hidden">
          <div class="bg-gradient-to-r from-hero-highlight to-[#FFB800] h-1.5 rounded-full" style="width: 85%"></div>
        </div>
        <p class="text-xs text-slate-400 text-right">150 BP to Platinum</p>
      </div>

      <button class="w-full py-3 bg-white text-content rounded-xl font-bold hover:bg-slate-100 transition-colors text-sm shadow-[0_0_15px_rgba(255,255,255,0.1)] hover:shadow-[0_0_20px_rgba(255,255,255,0.2)]">
        Redeem Rewards
      </button>
    </div>
  </div>
</template>
