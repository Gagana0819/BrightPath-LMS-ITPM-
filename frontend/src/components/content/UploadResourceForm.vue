<script setup>
import { ref, computed } from 'vue'
import { useContentStore } from '@/stores/contentStore'

const contentStore = useContentStore()

const isClassroomSync = ref(false)
const title = ref('')
const moduleCode = ref('')
const resourceType = ref('LECTURE_NOTES')
const selectedFile = ref(null)
const uploadSuccess = ref(false)
const errorMessage = ref('')

const moduleCodeError = ref('Required — 2 letters + 4 numbers')
const moduleCodeTouched = ref(false)

const resourceTypeChoices = [
  { value: 'LECTURE_NOTES', label: 'Lecture Notes' },
  { value: 'PAST_PAPER', label: 'Past Papers' },
  { value: 'TUTORIAL_ANSWER', label: 'Tutorial Answers' },
  { value: 'SHORT_NOTE', label: 'Short Notes' }
]

const handleModuleCodeInput = (e) => {
  moduleCodeTouched.value = true
  let raw = e.target.value.toUpperCase()

  let filtered = ''
  for (let i = 0; i < raw.length && filtered.length < 6; i++) {
    const ch = raw[i]
    if (filtered.length < 2) {
      if (/[A-Z]/.test(ch)) filtered += ch
    } else {
      if (/\d/.test(ch)) filtered += ch
    }
  }

  moduleCode.value = filtered
  e.target.value = filtered 

  if (filtered.length === 0) {
    moduleCodeError.value = 'Required — 2 letters + 4 numbers'
  } else if (filtered.length < 2) {
    moduleCodeError.value = `Need ${2 - filtered.length} more letter(s)`
  } else if (filtered.length < 6) {
    moduleCodeError.value = `Need ${6 - filtered.length} more number(s)`
  } else {
    moduleCodeError.value = ''
  }
}

const isModuleCodeValid = () => moduleCode.value.length === 6 && /^[A-Z]{2}\d{4}$/.test(moduleCode.value)

const onFileChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    selectedFile.value = file
  }
}

const handlePublish = async () => {
  if (!isModuleCodeValid() || !selectedFile.value || !title.value) {
    errorMessage.value = 'Please fill in all fields and select a file.'
    return
  }

  try {
    uploadSuccess.value = false
    errorMessage.value = ''
    
    await contentStore.uploadResource({
      title: title.value,
      module_code: moduleCode.value,
      resource_type: resourceType.value
    }, selectedFile.value)

    uploadSuccess.value = true
    // Reset form
    title.value = ''
    moduleCode.value = ''
    selectedFile.value = null
    moduleCodeTouched.value = false
  } catch (err) {
    console.error('Upload failed:', err)
    errorMessage.value = typeof err === 'object' ? JSON.stringify(err) : err
  }
}

const toggleSync = () => {
  isClassroomSync.value = !isClassroomSync.value
}
</script>

<template>
  <div class="w-full max-w-2xl mx-auto bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
    <div class="mb-6">
      <h2 class="text-2xl font-bold text-content mb-1">Upload Study Resource</h2>
      <p class="text-slate-500 text-sm">Share your notes, presentations, or past papers with the community.</p>
    </div>

    <!-- Feedback Messages -->
    <div v-if="uploadSuccess" class="mb-6 p-4 bg-green-50 border border-green-200 text-green-700 rounded-xl flex items-center gap-3">
      <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
      <span class="font-medium">Resource uploaded successfully to Supabase Storage!</span>
    </div>

    <div v-if="errorMessage" class="mb-6 p-4 bg-red-50 border border-red-200 text-red-700 rounded-xl flex items-center gap-3">
      <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
      <span class="text-sm">{{ errorMessage }}</span>
    </div>

    <div class="space-y-6">
      
      <!-- General Form -->
      <div class="space-y-4">
        <div class="space-y-1.5">
          <label class="text-sm font-semibold text-slate-700">Resource Title</label>
          <input 
            v-model="title"
            type="text" 
            class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none" 
            placeholder="e.g. ITPM Lecture Notes - Chapter 5" 
          />
        </div>
        
        <div class="grid md:grid-cols-2 gap-4">
          <div class="space-y-1.5 flex-1">
            <label class="text-sm font-semibold text-slate-700">Module Code</label>
            <div class="relative">
              <input 
                :value="moduleCode"
                @input="handleModuleCodeInput"
                type="text" 
                maxlength="6"
                required
                class="w-full px-4 py-3 bg-slate-50 border rounded-xl focus:ring-2 focus:ring-hero-highlight/20 transition-all outline-none uppercase tracking-normal text-sm font-medium" 
                :class="moduleCodeError && moduleCodeTouched && moduleCode.length > 0 ? 'border-red-400 focus:border-red-400 bg-red-50/30' : !moduleCodeError && moduleCode ? 'border-green-400 focus:border-green-400 bg-green-50/20' : 'border-slate-200 focus:border-hero-highlight'"
                placeholder="SE3040" 
              />
              <span v-if="!moduleCodeError && moduleCode" class="absolute right-3 top-1/2 -translate-y-1/2 text-green-500">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" /></svg>
              </span>
            </div>
            <div class="h-4 overflow-hidden">
              <p v-if="moduleCodeError && moduleCodeTouched && moduleCode.length > 0" class="text-[10px] font-medium text-red-400 tracking-tight">
                {{ moduleCodeError }}
              </p>
              <p v-else-if="!moduleCodeTouched || moduleCode.length === 0" class="text-[10px] font-medium text-slate-400 tracking-tight">
                Format: 2 letters + 4 numbers (e.g. SE3040)
              </p>
            </div>
          </div>
          <div class="space-y-1.5">
            <label class="text-sm font-semibold text-slate-700">Resource Type</label>
            <select 
              v-model="resourceType"
              class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-hero-highlight/20 focus:border-hero-highlight transition-all outline-none text-slate-700"
            >
              <option v-for="type in resourceTypeChoices" :key="type.value" :value="type.value">
                {{ type.label }}
              </option>
            </select>
          </div>
        </div>
      </div>

      <!-- File Upload Zone -->
      <div 
        @click="$refs.fileInput.click()"
        class="border-2 border-dashed border-slate-300 rounded-2xl p-8 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-50 hover:border-hero-highlight transition-all group relative overflow-hidden"
        :class="selectedFile ? 'border-hero-highlight bg-blue-50/30' : ''"
      >
        <input 
          type="file" 
          ref="fileInput" 
          class="hidden" 
          accept=".pdf,.doc,.docx,.txt"
          @change="onFileChange"
        />
        <div class="w-16 h-16 bg-blue-50 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:bg-blue-100 transition-colors">
          <svg v-if="!selectedFile" class="w-8 h-8 text-hero-highlight" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
          <svg v-else class="w-8 h-8 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <span class="font-bold text-content block text-lg mb-1">
          {{ selectedFile ? selectedFile.name : 'Drag and drop your files here' }}
        </span>
        <span class="text-sm text-slate-500 font-medium">
          {{ selectedFile ? (selectedFile.size / 1024 / 1024).toFixed(2) + ' MB' : 'Or browse files from your computer' }}
        </span>
        <span class="text-xs text-slate-400 mt-3 font-medium text-center">
          Supported formats: PDF, DOC, DOCX, TXT (max 25MB)
        </span>
      </div>

      <hr class="border-slate-100" />

      <!-- Integrations Area -->
      <div class="flex items-center justify-between p-4 bg-slate-50 rounded-xl border border-slate-200">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-white rounded-lg shadow-sm border border-slate-200 flex items-center justify-center p-2 text-green-600">
            <svg class="w-full h-full" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 4c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm0 14c-2.03 0-4.43-.82-6.14-2.88C7.55 15.8 9.68 15 12 15s4.45.8 6.14 2.12C16.43 19.18 14.03 20 12 20z"/>
            </svg>
          </div>
          <div>
            <span class="block font-bold text-slate-800 text-sm">Google Classroom Sync</span>
            <span class="block text-xs text-slate-500 font-medium tracking-wide">Automatically post a link to your configured class modules.</span>
          </div>
        </div>

        <button 
          @click="toggleSync" 
          class="w-12 h-6 rounded-full relative transition-colors duration-300 focus:outline-none"
          :class="isClassroomSync ? 'bg-green-500' : 'bg-slate-300'"
        >
          <div 
            class="absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow transition-transform duration-300"
            :class="isClassroomSync ? 'translate-x-6' : 'translate-x-0'"
          ></div>
        </button>
      </div>

      <!-- Submit Row -->
      <div class="pt-2 flex justify-end">
        <button 
          @click="handlePublish"
          :disabled="!isModuleCodeValid() || !selectedFile || !title || contentStore.isLoading"
          class="px-8 py-3 bg-hero-highlight text-white rounded-xl font-bold tracking-wide transition-all shadow-md active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-lg hover:-translate-y-0.5"
        >
          <span v-if="contentStore.isLoading" class="flex items-center gap-2">
            <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Uploading...
          </span>
          <span v-else>Publish Resource</span>
        </button>
      </div>
    </div>
  </div>
</template>
