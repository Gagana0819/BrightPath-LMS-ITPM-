<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const slides = [
  {
    image: '/hero image 03.png',
    highlight1: 'Your',
    line1: 'Partner In',
    line2: 'Learning',
    highlight2: 'Success',
    description: 'Your all-in-one LMS solution with an admin panel, website, and mobile app. Perfect for mentors to teach effectively and learners to gain knowledge easily. Modern tools for modern education.'
  },
  {
    image: '/hero image 05.png',
    highlight1: 'Seamless',
    line1: 'Digital Library',
    line2: 'Access',
    highlight2: 'Anywhere',
    description: 'Access a world-class digital repository of peer-reviewed resources. Download, study, and rank materials curated for modern university students.'
  },
  {
    image: '/hero image 06.png',
    highlight1: 'Interactive',
    line1: 'Live Kuppi',
    line2: 'Sessions',
    highlight2: 'Real-time',
    description: 'Join real-time virtual classrooms seamlessly integrated with your schedule. Engage with educators and peers to clear your doubts instantly.'
  },
  {
    image: '/hero image 07.png',
    highlight1: 'Smart',
    line1: 'Notifications &',
    line2: 'Alerts',
    highlight2: 'Always',
    description: 'Never miss an important update. Get personalized recommendations and automated review requests tailored specifically to your academic stream.'
  }
]

const currentIndex = ref(0)
let intervalId

const displayedText = ref({
  highlight1: '',
  line1: '',
  line2: '',
  highlight2: '',
  description: ''
})

const typingField = ref('')
const typeVersion = ref(0)

const startTyping = async () => {
  const version = ++typeVersion.value
  const slide = slides[currentIndex.value]
  
  displayedText.value = { highlight1: '', line1: '', line2: '', highlight2: '', description: '' }
  
  const typePart = async (key, text) => {
    typingField.value = key
    for (let i = 0; i <= text.length; i++) {
      if (typeVersion.value !== version) return
      displayedText.value[key] = text.substring(0, i)
      await new Promise(r => setTimeout(r, 40)) // typing speed
    }
  }

  await typePart('highlight1', slide.highlight1)
  if (typeVersion.value !== version) return
  await typePart('line1', slide.line1)
  if (typeVersion.value !== version) return
  await typePart('line2', slide.line2)
  if (typeVersion.value !== version) return
  await typePart('highlight2', slide.highlight2)
  if (typeVersion.value !== version) return
  
  const descText = slide.description
  typingField.value = 'description'
  for (let i = 0; i <= descText.length; i++) {
    if (typeVersion.value !== version) return
    displayedText.value.description = descText.substring(0, i)
    await new Promise(r => setTimeout(r, 15)) // faster for description
  }
  
  if (typeVersion.value === version) {
    typingField.value = 'done'
  }
}

onMounted(() => {
  startTyping()
  intervalId = setInterval(() => {
    currentIndex.value = (currentIndex.value + 1) % slides.length
  }, 7500)
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
})

watch(currentIndex, () => {
  startTyping()
})
</script>

<template>
  <section class="relative min-h-screen flex items-center overflow-hidden pt-20 hero-gradient">
    <!-- Background diagonal shapes  -->
     <!-- #2C3347 / #22252C-->
    <div
      class="absolute top-0 -right-[10%] w-[55%] h-[105%] bg-[#22252C] -skew-x-[20deg] z-0 hidden lg:block shadow-inner"
    ></div>

    <div
      class="max-w-[1800px] mx-auto px-4 lg:px-6 w-full z-10 flex flex-col lg:flex-row items-center justify-between gap-12 pt-12 lg:pt-0"
    >
      <!-- Left Content -->
      <div class="flex-1 w-full max-w-[650px] py-10 lg:py-16 relative flex flex-col justify-center">
        <!-- Floating shapes: Top Right -->
        <div class="absolute -top-6 right-[15%] opacity-90 hidden md:block">
          <div class="w-10 h-10 rounded-xl bg-[#d5e2fc] absolute top-2 right-2"></div>
          <div
            class="w-10 h-10 rounded-xl border border-[#5D6DFF] bg-transparent absolute top-0 right-0"
          ></div>
        </div>

        <div class="w-full relative min-h-[300px]">
          <h1
            class="text-[3.5rem] lg:text-[4.5rem] leading-[1.2] text-[#333333] font-normal mb-10 relative z-10 tracking-tight min-h-[160px]"
          >
            <span class="text-[#5D6DFF] font-bold relative inline-block pb-2">
              {{ displayedText.highlight1 }}
              <span v-show="displayedText.highlight1" class="absolute bottom-0 left-0 w-[110%] h-[3px] bg-[#5D6DFF]"></span>
              <span v-if="typingField === 'highlight1'" class="typing-cursor">|</span>
            </span>
            {{ displayedText.line1 ? ' ' + displayedText.line1 : '' }}
            <span v-if="typingField === 'line1'" class="typing-cursor">|</span>
            <br v-if="displayedText.line1 || typingField === 'line2' || displayedText.line2" />
            {{ displayedText.line2 }}
            <span v-if="typingField === 'line2'" class="typing-cursor">|</span>
            {{ displayedText.highlight2 || typingField === 'highlight2' ? ' ' : '' }}
            <span class="text-[#5D6DFF] font-bold relative inline-block pb-2" v-show="displayedText.highlight2 || typingField === 'highlight2'">
              {{ displayedText.highlight2 }}
              <span v-show="displayedText.highlight2" class="absolute bottom-0 left-0 w-full h-[3px] bg-[#5D6DFF]"></span>
              <span v-if="typingField === 'highlight2'" class="typing-cursor">|</span>
            </span>
          </h1>

          <div class="border-l-[3px] border-[#5D6DFF] pl-6 mb-12 relative z-10 min-h-[100px]">
            <p
              class="text-[1.15rem] lg:text-[1.25rem] text-[#333333] font-medium leading-relaxed max-w-[600px]"
            >
              {{ displayedText.description }}<span v-if="typingField === 'description' || typingField === 'done'" class="typing-cursor">|</span>
            </p>
          </div>
        </div>

        <!-- Floating shapes: Bottom Left -->
        <div class="absolute bottom-[2%] left-[25%] hidden md:block">
          <div class="absolute w-10 h-10 bg-[#d5e2fc] rounded-xl -top-2 -right-2"></div>
          <div class="absolute w-10 h-10 bg-[#5D6DFF] rounded-xl"></div>
        </div>

        <!-- Floating shapes: Circle -->
        <div
          class="absolute bottom-[20%] right-[5%] w-10 h-10 rounded-full border-[3px] border-[#5D6DFF] opacity-70 hidden md:block"
        ></div>

        <!-- Dot grid -->
        <div
          class="absolute -bottom-10 -left-4 w-[120px] h-[90px] opacity-40 hidden md:block"
          style="
            background-image: radial-gradient(#94a3b8 2px, transparent 2px);
            background-size: 16px 16px;
          "
        ></div>
      </div>

      <!-- Right Visual -->
      <div
        class="flex-1 w-full relative flex items-center justify-center lg:justify-end z-10 mt-10 lg:mt-0"
      >
        <!-- Added -skew-x-[20deg] to match background, and inner skew-x-[20deg] with scale to un-skew the photo -->
        <div
          class="relative w-full lg:w-[105%] h-[600px] rounded-[2rem] overflow-hidden border-[10px] border-transparent lg:mr-8  "
        >
          <div class="w-full h-full scale-[1.35] relative">
            <transition name="carousel">
              <img
                :key="currentIndex"
                :src="slides[currentIndex].image"
                alt="University student using BrightPath LMS"
                class="absolute inset-0 w-full h-full object-cover"
              />
            </transition>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-gradient {
  background: linear-gradient(
    -130deg,
    #e6f3ff 0%,
    #e6f3ff 60%,
    #e4f8f6 60%,
    #e4f8f6 80%,
    #faefff 80%,
    #faefff 100%
  );
}

.carousel-enter-active,
.carousel-leave-active {
  transition:
    opacity 1.5s ease-in-out,
    transform 1.5s ease-in-out;
}

.carousel-enter-from {
  opacity: 0;
  transform: scale(1.05);
}

.carousel-leave-to {
  opacity: 0;
  transform: scale(0.95);
}

.typing-cursor {
  display: inline-block;
  width: 3px;
  animation: blink 1s step-end infinite;
  color: #5D6DFF;
  margin-left: 2px;
  vertical-align: text-bottom;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
</style>
