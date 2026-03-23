<script setup></script>

<template>
  <section class="relative min-h-screen flex items-center overflow-hidden py-24 bg-base px-20">
    <!-- Background diagonal layout applied to wrapper -->
    <div
      class="absolute top-0 -left-[5%] w-[55%] h-full bg-[#6366F1]/5 -skew-x-[15deg] -z-10 hidden lg:block"
    ></div>

    <div
      class="max-w-[1600px] mx-auto px-4 lg:px-6 w-full z-10 flex flex-col lg:flex-row-reverse items-stretch justify-between gap-16 pt-12 lg:pt-0"
    >
      <!-- Right Content -->
      <div class="flex-1 max-w-[600px] py-0 lg:py-16 relative flex flex-col justify-center">
        <h2
          class="text-[3.5rem] lg:text-[4.5rem] leading-[1.2] text-content font-normal mb-10 tracking-tight"
        >
          Smart Interactions &<br />
          <span class="text-[#6366F1] font-bold relative inline-block pb-2">
            Personalized Alerts
            <span class="absolute bottom-0 left-0 w-full h-[3px] bg-[#6366F1]"></span>
          </span>
        </h2>

        <div class="border-l-[3px] border-[#6366F1] pl-6 mb-12 relative z-10">
          <p
            class="text-[1.15rem] lg:text-[1.25rem] text-content font-medium leading-relaxed max-w-[500px]"
          >
            Stay ahead of your coursework without the noise. Our intelligent engine delivers context-aware notifications, reminding you of upcoming events and suggesting resources tailored to your current modules.
          </p>
        </div>

        <div class="space-y-6 mb-10">
          <!-- Feature 1 -->
          <div
            class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-start gap-4 hover:border-[#6366F1]/50 transition-colors"
          >
            <div
              class="w-12 h-12 rounded-xl bg-[#6366F1]/10 text-[#6366F1] flex items-center justify-center text-2xl shrink-0"
            >
              🔔
            </div>
            <div>
              <h3 class="font-bold text-content text-lg mb-1">Intelligent Feedback Loop</h3>
              <p class="text-slate-600 leading-relaxed text-sm">
                After consuming content, the system triggers subtle alerts prompting you to rate and review, ensuring high-quality resources organically bubble to the top.
              </p>
            </div>
          </div>

          <!-- Feature 2 -->
          <div
            class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-start gap-4 hover:border-[#6366F1]/50 transition-colors"
          >
            <div
              class="w-12 h-12 rounded-xl bg-[#6366F1]/10 text-[#6366F1] flex items-center justify-center text-2xl shrink-0"
            >
              🧠
            </div>
            <div>
              <h3 class="font-bold text-content text-lg mb-1">Module-Aware Suggestions</h3>
              <p class="text-slate-600 leading-relaxed text-sm">
                Recommendations adapt dynamically based on your current semester—whether you’re tackling Cloud Computing or Data Science.
              </p>
            </div>
          </div>
        </div>

        <div class="flex items-center relative z-10">
          <RouterLink
            to="/login"
            class="inline-flex items-center justify-center px-8 py-3.5 rounded-lg font-bold text-[1.1rem] text-white bg-[#6366F1] hover:bg-[#4f46e5] transition-all shadow-md hover:shadow-lg hover:-translate-y-0.5"
          >
            Set Up Alerts
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

      <!-- Left Visual (Notifications Mockup) -->
      <div class="flex-1 relative flex items-center justify-center">
        <!-- Mockup Device Frame -->
        <div
          class="relative w-full max-w-sm bg-white rounded-[2.5rem] overflow-hidden shadow-[0_25px_50px_-12px_rgba(99,102,241,0.25)] border-8 border-slate-100 p-2 z-10 aspect-[0.5] flex flex-col"
        >
          <!-- Notch -->
          <div
            class="w-1/3 h-6 bg-slate-100 absolute top-0 left-1/2 -translate-x-1/2 rounded-b-2xl z-20"
          ></div>

          <!-- Screen Content -->
          <div
            class="flex-1 bg-base rounded-[2rem] overflow-hidden relative pt-12 p-4 flex flex-col gap-4"
          >
            <!-- Real-time Gmail Mockup -->
            <div
              class="bg-white p-4 rounded-2xl shadow-sm border border-slate-100 transform transition-transform hover:scale-[1.02] cursor-pointer"
            >
              <div class="flex justify-between items-start mb-2">
                <div class="flex items-center gap-2">
                  <div
                    class="w-6 h-6 rounded bg-amber-500 flex items-center justify-center text-white text-[10px] font-bold"
                  >
                    M
                  </div>
                  <span class="text-xs font-bold text-slate-500">Gmail · now</span>
                </div>
              </div>
              <h4 class="font-bold text-content text-sm mb-1 leading-tight">
                Recommended for You: Week 5 IT PM Slides
              </h4>
              <p class="text-xs text-slate-500 line-clamp-2">
                Since you're enrolled in IT PM, check out this highly-rated summary guide uploaded by Kasun.
              </p>
            </div>

            <!-- App push notification mockup -->
            <div
              class="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-sm border border-slate-100 transform transition-transform hover:scale-[1.02] cursor-pointer border-l-4 border-l-[#6366F1]"
            >
              <div class="flex justify-between items-start mb-2">
                <div class="flex items-center gap-2">
                  <div
                    class="w-6 h-6 rounded bg-[#6366F1] flex items-center justify-center text-white text-[10px] font-bold"
                  >
                    BP
                  </div>
                  <span class="text-xs font-bold text-slate-500">BrightPath · 2m</span>
                </div>
              </div>
              <h4 class="font-bold text-content text-sm mb-1 leading-tight">Review Request ⭐️</h4>
              <p class="text-xs text-slate-500 line-clamp-2">
                You recently downloaded "Data Structures Array PDF". Help your peers by rating its
                quality!
              </p>
            </div>

            <!-- App push notification mockup 2 -->
            <div
              class="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-sm border border-slate-100 transform transition-transform hover:scale-[1.02] cursor-pointer"
            >
              <div class="flex justify-between items-start mb-2">
                <div class="flex items-center gap-2">
                  <div
                    class="w-6 h-6 rounded bg-[#6366F1] flex items-center justify-center text-white text-[10px] font-bold"
                  >
                    BP
                  </div>
                  <span class="text-xs font-bold text-slate-500">BrightPath · 1h</span>
                </div>
              </div>
              <h4 class="font-bold text-content text-sm mb-1 leading-tight">
                Live Kuppi Starting Soon
              </h4>
              <p class="text-xs text-slate-500 line-clamp-2">
                Prof. Kumara Perera is starting "DSA Trees Discussion" in 10 minutes. Click to join securely.
              </p>
            </div>
          </div>
        </div>

        <!-- Decorative Background Blur -->
        <div
          class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-[80%] bg-[#6366F1] rounded-full mix-blend-multiply filter blur-[100px] opacity-10 -z-10 animate-pulse"
        ></div>
      </div>
    </div>
  </section>
</template>

<style scoped></style>
