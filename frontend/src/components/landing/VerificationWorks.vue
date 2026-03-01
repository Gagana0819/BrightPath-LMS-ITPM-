<script setup></script>

<template>
  <section class="relative min-h-screen flex items-center overflow-hidden py-24 bg-white">
    <!-- Background diagonal layout -->
    <div
      class="absolute top-0 -right-[5%] w-[55%] h-full bg-[#f4f7fe] -skew-x-[15deg] -z-10 hidden lg:block"
    ></div>

    <div
      class="max-w-[1600px] mx-auto px-4 lg:px-6 w-full z-10 flex flex-col lg:flex-row items-stretch justify-between gap-16 pt-12 lg:pt-0"
    >
      <!-- Left Content -->
      <div class="flex-1 max-w-[600px] py-0 lg:py-16 relative flex flex-col justify-center">
        <h2
          class="text-[3.5rem] lg:text-[4.5rem] leading-[1.2] text-[#333333] font-normal mb-10 tracking-tight"
        >
          Secure Access <br />
          <span class="text-[#5D6DFF] font-bold relative inline-block pb-2">
            How Verification Works
            <span class="absolute bottom-0 left-0 w-full h-[3px] bg-[#5D6DFF]"></span>
          </span>
        </h2>

        <div class="border-l-[3px] border-[#5D6DFF] pl-6 mb-12 relative z-10">
          <p
            class="text-[1.15rem] lg:text-[1.25rem] text-[#333333] font-medium leading-relaxed max-w-[500px]"
          >
            We maintain a high-trust environment by requiring authentic University ID or NIC
            verification for all members. Collaboration is safer when everyone is verified.
          </p>
        </div>

        <div class="space-y-6 mb-10">
          <!-- Step 1 -->
          <div class="flex items-start gap-5">
            <div
              class="w-12 h-12 rounded-full bg-[#5D6DFF]/10 text-[#5D6DFF] font-black flex items-center justify-center shrink-0 border border-[#5D6DFF]/20 text-lg"
            >
              1
            </div>
            <div class="pt-1">
              <h3 class="font-bold text-[#333333] text-lg mb-1">Upload University ID</h3>
              <p class="text-slate-600 leading-relaxed">
                Provide your official Student ID or NIC. Initiates our secure JWT-based
                authentication protocol.
              </p>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="flex items-start gap-5">
            <div
              class="w-12 h-12 rounded-full bg-[#5D6DFF]/10 text-[#5D6DFF] font-black flex items-center justify-center shrink-0 border border-[#5D6DFF]/20 text-lg"
            >
              2
            </div>
            <div class="pt-1">
              <h3 class="font-bold text-[#333333] text-lg mb-1">System Verification</h3>
              <p class="text-slate-600 leading-relaxed">
                Our backend logic validates your identity against active university enrollment
                criteria.
              </p>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="flex items-start gap-5">
            <div
              class="w-12 h-12 rounded-full bg-[#5D6DFF]/10 text-[#5D6DFF] font-black flex items-center justify-center shrink-0 border border-[#5D6DFF]/20 text-lg"
            >
              3
            </div>
            <div class="pt-1">
              <h3 class="font-bold text-[#333333] text-lg mb-1">Access Personalized Dashboard</h3>
              <p class="text-slate-600 leading-relaxed">
                Enter your hub for verified peer-to-peer collaboration, safe from unverified users.
              </p>
            </div>
          </div>
        </div>

        <div class="flex items-center relative z-10">
          <RouterLink
            to="/login"
            class="inline-flex items-center justify-center px-8 py-3.5 rounded-lg font-bold text-[1.1rem] text-white bg-[#5D6DFF] hover:bg-[#4a58e6] transition-all shadow-md hover:shadow-lg hover:-translate-y-0.5"
          >
            Verify My Account
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" class="ml-2">
              <path
                d="M5 12H19M19 12L12 5M19 12L12 19"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </RouterLink>
        </div>
      </div>

      <!-- Right Visual (Mockup ID Card) -->
      <div class="flex-1 relative flex items-center justify-center">
        <div
          class="relative w-full max-w-md aspect-[1.6] bg-gradient-to-br from-white to-slate-100 rounded-3xl overflow-hidden shadow-2xl border-4 border-white/20 p-8 z-0 transform hover:-rotate-2 transition-transform duration-500 group"
        >
          <div class="absolute top-0 right-0 w-32 h-32 bg-[#5D6DFF]/10 rounded-bl-full -z-10"></div>

          <div class="flex justify-between items-start mb-8">
            <div class="font-bold text-[#333333] text-xl tracking-tight">University ID</div>
            <div
              class="px-3 py-1 bg-green-100 text-green-700 font-bold text-xs rounded-full flex items-center gap-1"
            >
              <span class="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse"></span> VERIFIED
            </div>
          </div>

          <div class="flex gap-6 items-center">
            <div
              class="w-24 h-24 rounded-2xl bg-slate-200 border-2 border-white shadow-inner overflow-hidden flex items-center justify-center text-4xl group-hover:scale-105 transition-transform duration-500"
            >
              👨‍🎓
            </div>

            <div class="flex-1 space-y-3">
              <div class="h-4 bg-slate-200 rounded w-3/4"></div>
              <div class="h-3 bg-slate-200 rounded w-1/2"></div>
              <div class="h-3 bg-slate-200 rounded w-5/6"></div>
            </div>
          </div>

          <div class="absolute bottom-6 right-8 text-slate-300">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" class="opacity-50">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" fill="currentColor" />
            </svg>
          </div>
        </div>

        <!-- Background decorative blur -->
        <div
          class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-3/4 h-3/4 bg-[#5D6DFF] rounded-full mix-blend-multiply filter blur-[80px] opacity-20 -z-10"
        ></div>
      </div>
    </div>
  </section>
</template>
