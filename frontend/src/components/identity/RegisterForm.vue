<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const step = ref(1)

const formData = ref({
  firstName: '',
  lastName: '',
  email: '',
  studentId: '',
  nicFile: null
})

const nextStep = () => {
  if (step.value < 2) step.value++
}

const prevStep = () => {
  if (step.value > 1) step.value--
}

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    formData.value.nicFile = file
  }
}

const triggerFileInput = () => {
  document.getElementById('nic-upload').click()
}

const submitForm = () => {
  // Mock API call then routing to dashboard
  setTimeout(() => {
    router.push('/dashboard')
  }, 1000)
}
</script>

<template>
  <div class="w-full max-w-lg mx-auto bg-white rounded-2xl shadow-xl border border-slate-100 p-8">
    <div class="mb-8 text-center">
      <h2 class="text-3xl font-bold text-content mb-2 tracking-tight">Join BrightPath</h2>
      <p class="text-slate-500">Step {{ step }} of 2: {{ step === 1 ? 'Personal Details' : 'Identity Verification' }}</p>
    </div>

    <!-- Progress Bar -->
    <div class="w-full bg-slate-100 h-2 rounded-full mb-8 overflow-hidden">
      <div 
        class="h-full bg-hero-highlight transition-all duration-500 ease-in-out"
        :style="{ width: step === 1 ? '50%' : '100%' }"
      ></div>
    </div>

    <!-- Step 1: Details -->
    <div v-if="step === 1" class="space-y-5 animate-in fade-in slide-in-from-right-4 duration-300">
      <div class="grid grid-cols-2 gap-4">
        <div class="space-y-1.5">
          <label class="text-sm font-medium text-slate-700">First Name</label>
          <input v-model="formData.firstName" type="text" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none" placeholder="Kasun" />
        </div>
        <div class="space-y-1.5">
          <label class="text-sm font-medium text-slate-700">Last Name</label>
          <input v-model="formData.lastName" type="text" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none" placeholder="Silva" />
        </div>
      </div>
      <div class="space-y-1.5">
        <label class="text-sm font-medium text-slate-700">University Email</label>
        <input v-model="formData.email" type="email" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none" placeholder="kasun.s@university.edu" />
      </div>
      <div class="space-y-1.5">
        <label class="text-sm font-medium text-slate-700">Student ID Number</label>
        <input v-model="formData.studentId" type="text" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none" placeholder="SE/2026/045" />
      </div>

      <button @click="nextStep" class="w-full mt-6 py-3.5 px-4 bg-hero-highlight text-white rounded-xl font-bold tracking-wide hover:opacity-90 transition-all shadow-md hover:shadow-lg hover:-translate-y-0.5">
        Continue to Verification
      </button>
    </div>

    <!-- Step 2: Verification Upload -->
    <div v-if="step === 2" class="space-y-6 animate-in fade-in slide-in-from-right-4 duration-300">
      
      <div class="bg-blue-50 border border-blue-100 rounded-xl p-4 flex gap-3 text-blue-800">
        <svg class="w-6 h-6 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <p class="text-sm">Please upload a clear, legible photo of your Student ID or National Identity Card (NIC).</p>
      </div>

      <div 
        @click="triggerFileInput"
        class="border-2 border-dashed border-slate-300 rounded-2xl p-8 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-50 hover:border-hero-highlight transition-all group"
      >
        <input id="nic-upload" type="file" class="hidden" @change="handleFileUpload" accept="image/*,.pdf" />
        
        <div v-if="!formData.nicFile" class="text-center">
          <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:bg-blue-200 transition-colors">
            <svg class="w-8 h-8 text-hero-highlight" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
            </svg>
          </div>
          <span class="font-semibold text-content block text-lg">Click to Upload Document</span>
          <span class="text-sm text-slate-500 mt-1">SVG, PNG, JPG or PDF (max. 5MB)</span>
        </div>

        <div v-else class="text-center">
          <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg class="w-8 h-8 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <span class="font-semibold text-content block text-lg">{{ formData.nicFile.name }}</span>
          <span class="text-sm text-hero-highlight font-medium mt-1 cursor-pointer">Click to change file</span>
        </div>
      </div>

      <div class="flex gap-4 pt-2">
        <button @click="prevStep" class="px-6 py-3.5 rounded-xl font-bold text-slate-500 bg-slate-100 hover:bg-slate-200 transition-all">
          Back
        </button>
        <button @click="submitForm" class="flex-1 py-3.5 px-4 bg-hero-highlight text-white rounded-xl font-bold tracking-wide hover:opacity-90 transition-all shadow-md hover:shadow-lg hover:-translate-y-0.5">
          Submit Registration
        </button>
      </div>
    </div>
  </div>
</template>
