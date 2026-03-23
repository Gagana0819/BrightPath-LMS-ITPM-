<script setup>
<<<<<<< HEAD
import StatsBanner from './StatsBanner.vue'
</script>

<template>
  <section class="hero-section relative w-full overflow-hidden">
    <!-- Background Image Layer -->
    <div class="absolute inset-0 w-full h-full z-0">
      <img
        src="/hero BG.png"
        alt="Hero background"
        class="w-full h-full object-cover"
      />
    </div>

    <!-- Main Content Area -->
    <div class="relative z-10 max-w-[1400px] mx-auto px-4 lg:px-8 w-full h-full">
      <div class="flex items-end justify-center lg:justify-end w-full hero-content-area">
        <!-- Right Visual: BG Asset (circles) behind the girl image -->
        <div class="relative flex items-end justify-center">
          <!-- BG Asset (abstract circles) - positioned behind the girl -->
          <img
            src="/BG asset.png"
            alt="Background decorative circles"
            class="absolute z-0 bg-asset-img"
          />

          <!-- Girl with books (digital library) - foreground -->
          <img
            src="/digital library.png"
            alt="Student with digital library"
            class="relative z-10 girl-img"
          />
        </div>
      </div>
    </div>

    <!-- Stats Banner overlapping the bottom of the hero image -->
    <div class="absolute bottom-20 left-0 right-0 z-20 w-full">
      <StatsBanner />
    </div>
=======
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
      await new Promise(r => setTimeout(r, 130)) // typing speed
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
      class="absolute top-0 -right-[10%] w-[55%] h-[105%] bg-hero-bg-right -skew-x-[20deg] z-0 hidden lg:block shadow-inner"
    ></div>

    <div
      class="max-w-[1800px] mx-auto px-4 lg:px-6 w-full z-10 flex flex-col lg:flex-row items-center justify-between gap-12 pt-12 lg:pt-0"
    >
      <!-- Left Content -->
      <div class="flex-1 w-full max-w-[650px] py-10 lg:py-16 relative flex flex-col justify-center">
        <!-- Floating shapes: Top Right -->
        <div class="absolute -top-6 right-[15%] opacity-90 hidden md:block">
          <div class="w-10 h-10 rounded-xl bg-hero-bg-shape1 absolute top-2 right-2"></div>
          <div
            class="w-10 h-10 rounded-xl border border-hero-highlight bg-transparent absolute top-0 right-0"
          ></div>
        </div>

        <div class="w-full relative min-h-[300px]">
          <h1
            class="text-[3.5rem] lg:text-[4.5rem] leading-[1.2] text-content font-normal mb-10 relative z-10 tracking-tight min-h-[160px]"
          >
            <span class="text-hero-highlight font-bold relative inline-block pb-2">
              {{ displayedText.highlight1 }}
              <span v-show="displayedText.highlight1" class="absolute bottom-0 left-0 w-[110%] h-[3px] bg-hero-highlight"></span>
              <span v-if="typingField === 'highlight1'" class="typing-cursor">|</span>
            </span>
            {{ displayedText.line1 ? ' ' + displayedText.line1 : '' }}
            <span v-if="typingField === 'line1'" class="typing-cursor">|</span>
            <br v-if="displayedText.line1 || typingField === 'line2' || displayedText.line2" />
            {{ displayedText.line2 }}
            <span v-if="typingField === 'line2'" class="typing-cursor">|</span>
            {{ displayedText.highlight2 || typingField === 'highlight2' ? ' ' : '' }}
            <span class="text-hero-highlight font-bold relative inline-block pb-2" v-show="displayedText.highlight2 || typingField === 'highlight2'">
              {{ displayedText.highlight2 }}
              <span v-show="displayedText.highlight2" class="absolute bottom-0 left-0 w-full h-[3px] bg-hero-highlight"></span>
              <span v-if="typingField === 'highlight2'" class="typing-cursor">|</span>
            </span>
          </h1>

          <div class="border-l-[3px] border-hero-highlight pl-6 mb-12 relative z-10 min-h-[100px]">
            <p
              class="text-[1.15rem] lg:text-[1.25rem] text-content font-medium leading-relaxed max-w-[600px]"
            >
              {{ displayedText.description }}<span v-if="typingField === 'description' || typingField === 'done'" class="typing-cursor">|</span>
            </p>
          </div>
        </div>

        <!-- Floating shapes: Bottom Left -->
        <div class="absolute bottom-[2%] left-[25%] hidden md:block">
          <div class="absolute w-10 h-10 bg-hero-bg-shape1 rounded-xl -top-2 -right-2"></div>
          <div class="absolute w-10 h-10 bg-hero-highlight rounded-xl"></div>
        </div>

        <!-- Floating shapes: Circle -->
        <div
          class="absolute bottom-[20%] right-[5%] w-10 h-10 rounded-full border-[3px] border-hero-highlight opacity-70 hidden md:block"
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
>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
  </section>
</template>

<style scoped>
<<<<<<< HEAD
.hero-section {
  min-height: 600px;
  padding-bottom: 0;
}

.hero-content-area {
  min-height: 500px;
  padding-top: 80px;
  padding-bottom: 40px;
}

.girl-img {
  max-height: 480px;
  width: auto;
  object-fit: contain;
  object-position: bottom;
}

.bg-asset-img {
  width: 120%;
  max-width: 700px;
  top: -10%;
  left: 50%;
  transform: translateX(-50%);
  object-fit: contain;
  pointer-events: none;
}

/* Responsive adjustments */
@media (min-width: 1024px) {
  .hero-section {
    min-height: 700px;
  }

  .hero-content-area {
    min-height: 600px;
    padding-top: 100px;
    padding-bottom: 50px;
  }

  .girl-img {
    max-height: 560px;
  }

  .bg-asset-img {
    width: 140%;
    max-width: 850px;
    top: -15%;
  }
}

@media (min-width: 1280px) {
  .hero-content-area {
    padding-top: 80px;
  }

  .girl-img {
    max-height: 600px;
  }
=======
.hero-gradient {
  background: linear-gradient(
    -130deg,
    theme('colors.hero.bg.left') 0%,
    theme('colors.hero.bg.left') 60%,
    theme('colors.hero.bg.pill') 60%,
    theme('colors.hero.bg.pill') 80%,
    theme('colors.hero.bg.shape2') 80%,
    theme('colors.hero.bg.shape2') 100%
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
  color: theme('colors.hero.highlight');
  margin-left: 2px;
  vertical-align: text-bottom;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
}
</style>
