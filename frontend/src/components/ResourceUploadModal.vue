<script setup>
import { ref } from 'vue'
import { useContentStore } from '../stores/contentStore'

const emits = defineEmits(['close'])
const contentStore = useContentStore()

const title = ref('')
const description = ref('')
const category = ref('videos')
const selectedFile = ref(null)
const isDragging = ref(false)
const uploadProgress = ref(0)
const isUploading = ref(false)
const isSuccess = ref(false)

const handleFileUpload = (event) => {
  selectedFile.value = event.target.files[0]
}

const onDrop = (event) => {
  isDragging.value = false
  selectedFile.value = event.dataTransfer.files[0]
}

const submitForm = async () => {
  if (!title.value || !category.value || !selectedFile.value) {
    return
  }

  isUploading.value = true
  uploadProgress.value = 0

  // Simulate S3 Upload Progress
  const interval = setInterval(() => {
    if (uploadProgress.value < 90) {
      uploadProgress.value += Math.floor(Math.random() * 15)
    } else {
      clearInterval(interval)
    }
  }, 200)

  const resourceData = {
    title: title.value,
    description: description.value,
    category: category.value,
  }

  await contentStore.uploadResource(resourceData, selectedFile.value)
  
  uploadProgress.value = 100
  isUploading.value = false
  isSuccess.value = true

  setTimeout(() => {
    emits('close')
  }, 1500)
}
</script>

<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm font-sans px-4">
    <div class="bg-white rounded-[32px] shadow-2xl w-full max-w-xl p-8 relative overflow-hidden animate-in zoom-in duration-300">
      
      <!-- Decorative Background -->
      <div class="absolute -top-24 -right-24 w-48 h-48 bg-blue-50 rounded-full blur-3xl opacity-50"></div>
      
      <button @click="$emit('close')" class="absolute top-6 right-6 text-slate-400 hover:text-slate-600 transition-colors p-2 hover:bg-slate-50 rounded-full">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <div v-if="!isSuccess">
        <div class="mb-8">
          <h2 class="text-3xl font-extrabold text-[#1E293B] tracking-tight mb-2">Upload Resource</h2>
          <p class="text-slate-500 text-sm font-medium">Add new content to your <span class="text-blue-600">AWS S3 Cloud</span> storage.</p>
        </div>

        <form @submit.prevent="submitForm" class="space-y-5">
          <!-- Dropzone -->
          <div 
            @dragover.prevent="isDragging = true"
            @dragleave.prevent="isDragging = false"
            @drop.prevent="onDrop"
            :class="[
              'relative border-2 border-dashed rounded-[24px] p-8 transition-all duration-300 flex flex-col items-center justify-center group cursor-pointer',
              isDragging ? 'bg-blue-50 border-blue-400' : 'bg-slate-50 border-slate-200 hover:border-blue-300 hover:bg-white'
            ]"
          >
            <input type="file" @change="handleFileUpload" class="absolute inset-0 opacity-0 cursor-pointer" id="file-input">
            
            <div :class="['w-16 h-16 rounded-2xl flex items-center justify-center shadow-sm mb-4 transition-transform duration-300 group-hover:scale-110', selectedFile ? 'bg-emerald-100' : 'bg-white']">
              <svg v-if="!selectedFile" class="w-8 h-8 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <svg v-else class="w-8 h-8 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </div>

            <p v-if="!selectedFile" class="text-slate-600 font-bold text-center">
              Drag & drop or <span class="text-blue-600 underline">browse</span>
            </p>
            <p v-else class="text-emerald-700 font-bold text-center truncate max-w-full px-4">
              {{ selectedFile.name }}
            </p>
            <p class="text-[11px] text-slate-400 font-medium mt-1 uppercase tracking-wider">Supports PDF, Video, DOCX (Max 100MB)</p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Title -->
            <div class="col-span-full">
              <label class="block text-[13px] font-bold text-slate-700 mb-1.5 ml-1">Resource Title *</label>
              <input type="text" v-model="title" required class="w-full px-5 py-3.5 bg-slate-50 border border-slate-200 rounded-[16px] focus:ring-4 focus:ring-blue-100 focus:border-blue-500 outline-none transition-all font-medium" placeholder="E.g. Computer Science Past Paper 2024">
            </div>

            <!-- Category -->
            <div class="col-span-full">
              <label class="block text-[13px] font-bold text-slate-700 mb-1.5 ml-1">Delivery Format *</label>
              <div class="grid grid-cols-3 gap-3">
                <button type="button" @click="category = 'videos'" :class="['py-3 px-2 rounded-xl border font-bold text-[12px] transition-all', category === 'videos' ? 'bg-blue-600 text-white border-blue-600 shadow-md transform scale-[1.02]' : 'bg-white text-slate-500 border-slate-200 hover:border-blue-200']">Lecture Video</button>
                <button type="button" @click="category = 'notes'" :class="['py-3 px-2 rounded-xl border font-bold text-[12px] transition-all', category === 'notes' ? 'bg-blue-600 text-white border-blue-600 shadow-md transform scale-[1.02]' : 'bg-white text-slate-500 border-slate-200 hover:border-blue-200']">Study Notes</button>
                <button type="button" @click="category = 'past_papers'" :class="['py-3 px-2 rounded-xl border font-bold text-[12px] transition-all', category === 'past_papers' ? 'bg-blue-600 text-white border-blue-600 shadow-md transform scale-[1.02]' : 'bg-white text-slate-500 border-slate-200 hover:border-blue-200']">Past Paper</button>
              </div>
            </div>
          </div>

          <!-- Progress Bar (Simulation) -->
          <div v-if="isUploading" class="pt-4 animate-in slide-in-from-top-2">
            <div class="flex justify-between items-center mb-2">
              <span class="text-[12px] font-bold text-blue-600 flex items-center gap-2">
                <svg class="animate-spin h-3 w-3" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                Syncing to AWS S3...
              </span>
              <span class="text-[12px] font-bold text-slate-400">{{ uploadProgress }}%</span>
            </div>
            <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
              <div class="bg-blue-600 h-full transition-all duration-300 ease-out" :style="{ width: uploadProgress + '%' }"></div>
            </div>
          </div>

          <div class="flex gap-3 pt-4">
            <button type="button" @click="$emit('close')" class="flex-1 py-4 px-6 rounded-[18px] text-slate-500 font-bold hover:bg-slate-50 transition-colors border border-transparent">Cancel</button>
            <button type="submit" :disabled="isUploading || !selectedFile" class="flex-[2] py-4 px-6 rounded-[18px] bg-[#1E293B] hover:bg-[#0F172A] text-white font-bold shadow-lg shadow-slate-200 transition-all active:scale-95 disabled:opacity-50 disabled:active:scale-100 flex items-center justify-center gap-2">
              {{ isUploading ? 'Finalizing Sync...' : 'Publish to Cloud' }}
              <svg v-if="!isUploading" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
            </button>
          </div>
        </form>
      </div>

      <!-- Success State -->
      <div v-else class="py-12 flex flex-col items-center justify-center text-center animate-in zoom-in duration-500">
        <div class="w-24 h-24 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mb-6 shadow-inner animate-bounce">
          <svg class="w-12 h-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <h2 class="text-3xl font-extrabold text-slate-800 mb-2">Upload Successful!</h2>
        <p class="text-slate-500 font-medium">Your resource is now live and <br> securely stored on AWS S3.</p>
      </div>
      
    </div>
  </div>
</template>
