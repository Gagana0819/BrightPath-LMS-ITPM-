<script setup>
import { ref, watch } from 'vue'
import { useContentStore } from '@/stores/contentStore'

const props = defineProps({
  show: Boolean,
  resource: Object
})

const emit = defineEmits(['close', 'updated'])
const contentStore = useContentStore()

const formData = ref({
  title: '',
  module_code: '',
  resource_type: '',
  faculty: '',
  academic_stream: '',
  academic_year: ''
})

const isSubmitting = ref(false)
const errorMessage = ref('')

// Watch for resource changes to prepopulate form
watch(() => props.resource, (newRes) => {
  if (newRes) {
    formData.value = {
      title: newRes.title || '',
      module_code: newRes.module_code || '',
      resource_type: newRes.resource_type || '',
      faculty: newRes.faculty || '',
      academic_stream: newRes.academic_stream || '',
      academic_year: newRes.academic_year || ''
    }
  }
}, { immediate: true })

const handleSubmit = async () => {
  isSubmitting.value = true
  errorMessage.value = ''
  try {
    await contentStore.updateResource(props.resource.id, formData.value)
    emit('updated')
    emit('close')
  } catch (err) {
    errorMessage.value = typeof err === 'string' ? err : 'Failed to update resource'
  } finally {
    isSubmitting.value = false
  }
}

const resourceTypes = [
  { value: 'LECTURE_NOTES', label: 'Lecture Notes' },
  { value: 'PAST_PAPER', label: 'Past Paper' },
  { value: 'TUTORIAL_ANSWER', label: 'Tutorial Answer' },
  { value: 'SHORT_NOTE', label: 'Short Note' }
]

const faculties = ['Computing', 'Business', 'Engineering', 'Humanities & Sciences']
const streams = ['Information Technology', 'Software Engineering', 'Data Science', 'Interactive Media']
const years = ['Year 1/1', 'Year 1/2', 'Year 2/1', 'Year 2/2', 'Year 3/1', 'Year 3/2', 'Year 4/1', 'Year 4/2']

</script>

<template>
  <div v-if="show" class="fixed inset-0 z-[100] flex items-center justify-center p-4">
    <!-- Backdrop -->
    <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm animate-in fade-in duration-300" @click="emit('close')"></div>
    
    <!-- Modal Content -->
    <div class="bg-white rounded-[2.5rem] w-full max-w-xl overflow-hidden shadow-2xl relative z-10 animate-in zoom-in-95 duration-300 border border-slate-100">
      <div class="p-8 md:p-10">
        <!-- Header -->
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-3xl font-extrabold text-slate-800 tracking-tight">Edit Resource</h2>
            <p class="text-slate-500 font-medium mt-1">Update your material details</p>
          </div>
          <button @click="emit('close')" class="p-2 hover:bg-slate-100 rounded-full transition-colors text-slate-400 hover:text-slate-600">
            <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        <!-- Form -->
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Error Alert -->
          <div v-if="errorMessage" class="bg-red-50 border border-red-100 text-red-600 p-4 rounded-2xl text-sm font-bold flex items-center gap-3">
             <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
             {{ errorMessage }}
          </div>

          <!-- Title -->
          <div>
            <label class="block text-sm font-black text-slate-700 uppercase tracking-wider mb-2 ml-1">Document Title</label>
            <input v-model="formData.title" type="text" placeholder="Enter resource title" required
                   class="w-full bg-slate-50 border-2 border-slate-100 rounded-[1.25rem] px-5 py-3.5 outline-none focus:border-hero-highlight focus:ring-4 focus:ring-hero-highlight/10 transition-all font-medium text-slate-800" />
          </div>

          <div class="grid grid-cols-2 gap-4">
            <!-- Module Code -->
            <div>
              <label class="block text-sm font-black text-slate-700 uppercase tracking-wider mb-2 ml-1">Module Code</label>
              <input v-model="formData.module_code" type="text" placeholder="e.g. IT3040" required
                     class="w-full bg-slate-50 border-2 border-slate-100 rounded-[1.25rem] px-5 py-3.5 outline-none focus:border-hero-highlight focus:ring-4 focus:ring-hero-highlight/10 transition-all font-medium text-slate-800 uppercase" />
            </div>

            <!-- Resource Type -->
            <div>
              <label class="block text-sm font-black text-slate-700 uppercase tracking-wider mb-2 ml-1">Category</label>
              <select v-model="formData.resource_type" required
                      class="w-full bg-slate-50 border-2 border-slate-100 rounded-[1.25rem] px-5 py-3.5 outline-none focus:border-hero-highlight focus:ring-4 focus:ring-hero-highlight/10 transition-all font-bold text-slate-800 appearance-none">
                <option value="" disabled>Select Type</option>
                <option v-for="type in resourceTypes" :key="type.value" :value="type.value">{{ type.label }}</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <!-- Faculty -->
            <div>
              <label class="block text-sm font-black text-slate-700 uppercase tracking-wider mb-2 ml-1">Faculty</label>
              <select v-model="formData.faculty"
                      class="w-full bg-slate-50 border-2 border-slate-100 rounded-[1.25rem] px-5 py-3.5 outline-none focus:border-hero-highlight focus:ring-4 focus:ring-hero-highlight/10 transition-all font-medium text-slate-800 appearance-none">
                <option v-for="f in faculties" :key="f" :value="f">{{ f }}</option>
              </select>
            </div>

            <!-- Year -->
            <div>
              <label class="block text-sm font-black text-slate-700 uppercase tracking-wider mb-2 ml-1">Academic Year</label>
              <select v-model="formData.academic_year"
                      class="w-full bg-slate-50 border-2 border-slate-100 rounded-[1.25rem] px-5 py-3.5 outline-none focus:border-hero-highlight focus:ring-4 focus:ring-hero-highlight/10 transition-all font-medium text-slate-800 appearance-none">
                <option v-for="y in years" :key="y" :value="y">{{ y }}</option>
              </select>
            </div>
          </div>

          <!-- Stream -->
          <div>
            <label class="block text-sm font-black text-slate-700 uppercase tracking-wider mb-2 ml-1">Academic Stream</label>
            <select v-model="formData.academic_stream"
                    class="w-full bg-slate-50 border-2 border-slate-100 rounded-[1.25rem] px-5 py-3.5 outline-none focus:border-hero-highlight focus:ring-4 focus:ring-hero-highlight/10 transition-all font-medium text-slate-800 appearance-none">
              <option v-for="s in streams" :key="s" :value="s">{{ s }}</option>
            </select>
          </div>

          <!-- Actions -->
          <div class="flex flex-col gap-3 pt-4">
            <button type="submit" :disabled="isSubmitting"
                    class="w-full bg-hero-highlight text-white font-black py-4 rounded-[1.25rem] shadow-xl shadow-hero-highlight/20 hover:-translate-y-1 active:translate-y-0.5 transition-all flex items-center justify-center gap-2 disabled:opacity-70 disabled:cursor-not-allowed">
              <svg v-if="isSubmitting" class="animate-spin h-5 w-5 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" /></svg>
              {{ isSubmitting ? 'SAVING CHANGES...' : 'SAVE CHANGES' }}
            </button>
            <button type="button" @click="emit('close')"
                    class="w-full bg-slate-50 text-slate-500 font-bold py-4 rounded-[1.25rem] hover:bg-slate-100 transition-all">
              Discard Changes
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
