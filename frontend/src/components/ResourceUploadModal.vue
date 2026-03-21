<script setup>
import { ref } from 'vue'
import { useContentStore } from '../stores/contentStore'

const emits = defineEmits(['close'])
const contentStore = useContentStore()

const title = ref('')
const description = ref('')
const category = ref('videos')
const selectedFile = ref(null)

const handleFileUpload = (event) => {
  selectedFile.value = event.target.files[0]
}

const submitForm = async () => {
  if (!title.value || !category.value || !selectedFile.value) {
    alert('Please fill all required fields and select a file.')
    return
  }

  const resourceData = {
    title: title.value,
    description: description.value,
    category: category.value,
  }

  await contentStore.uploadResource(resourceData, selectedFile.value)
  emits('close')
}
</script>

<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 font-sans">
    <div class="bg-base rounded-lg shadow-xl w-11/12 md:max-w-lg p-6 relative">
      <button @click="$emit('close')" class="absolute top-4 right-4 text-content hover:text-red-500">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <h2 class="text-2xl font-semibold mb-6 text-content">Upload New Resource</h2>

      <form @submit.prevent="submitForm" class="space-y-4">
        <!-- Title -->
        <div>
          <label class="block text-sm font-medium text-content mb-1">Title *</label>
          <input type="text" v-model="title" required class="w-full px-4 py-2 border rounded focus:ring focus:ring-blue-200 outline-none text-black" placeholder="Enter resource title">
        </div>

        <!-- Description -->
        <div>
          <label class="block text-sm font-medium text-content mb-1">Description</label>
          <textarea v-model="description" rows="3" class="w-full px-4 py-2 border rounded focus:ring focus:ring-blue-200 outline-none text-black" placeholder="Enter resource details"></textarea>
        </div>

        <!-- Category -->
        <div>
          <label class="block text-sm font-medium text-content mb-1">Category *</label>
          <select v-model="category" required class="w-full px-4 py-2 border rounded focus:ring focus:ring-blue-200 outline-none text-black bg-white">
            <option value="videos">Lecture Video</option>
            <option value="notes">Notes</option>
            <option value="past_papers">Past Paper</option>
          </select>
        </div>

        <!-- File Upload -->
        <div>
          <label class="block text-sm font-medium text-content mb-1">File *</label>
          <input type="file" @change="handleFileUpload" required class="w-full text-sm text-content file:space-x-4 file:py-2 file:px-4 file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100">
        </div>

        <div class="flex justify-end space-x-3 mt-6">
          <button type="button" @click="$emit('close')" class="px-4 py-2 rounded text-gray-600 hover:bg-gray-100 transition">Cancel</button>
          <button type="submit" :disabled="contentStore.isLoading" class="px-6 py-2 rounded bg-blue-600 text-white font-medium hover:bg-blue-700 transition disabled:opacity-50">
            {{ contentStore.isLoading ? 'Uploading...' : 'Upload' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
