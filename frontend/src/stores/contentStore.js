import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useContentStore = defineStore('content', () => {
  const resources = ref([])
  const liveSessions = ref([])
  const isLoading = ref(false)
  const error = ref(null)

  // Fetch resources based on category (videos, notes, past_papers)
  const fetchResources = async (category) => {
    isLoading.value = true
    error.value = null
    try {
      // TODO: Replace with actual backend API call
      // const response = await fetch(`/api/resources?category=${category}`)
      // resources.value = await response.json()
      
      // Mock data for UI development
      setTimeout(() => {
        resources.value = [
          { id: 1, title: 'Introduction to Vue 3', description: 'Basics of Composition API', category: 'videos', url: 'https://example.com/video1.mp4' },
          { id: 2, title: 'Chapter 1 Notes', description: 'Key points from chapter 1', category: 'notes', url: 'https://example.com/notes1.pdf' },
          { id: 3, title: '2022 Past Paper', description: 'Final exam 2022', category: 'past_papers', url: 'https://example.com/pastpaper.pdf' }
        ].filter(r => r.category === category)
        isLoading.value = false
      }, 500)
    } catch (err) {
      error.value = err.message
      isLoading.value = false
    }
  }

  // Upload a new resource
  const uploadResource = async (resourceData, file) => {
    isLoading.value = true
    error.value = null
    try {
      // TODO: Replace with actual upload API call (e.g., Multipart Form Data)
      console.log('Uploading resource:', resourceData, file)
      setTimeout(() => {
        const newResource = {
          id: Date.now(),
          ...resourceData,
          url: URL.createObjectURL(file)
        }
        resources.value.push(newResource)
        isLoading.value = false
      }, 1000)
    } catch (err) {
      error.value = err.message
      isLoading.value = false
    }
  }

  // Fetch live sessions
  const fetchLiveSessions = async () => {
    isLoading.value = true
    error.value = null
    try {
      // TODO: Replace with actual backend API call
      setTimeout(() => {
        liveSessions.value = [
          { id: 1, title: 'Advanced Vue Concepts', scheduled_time: new Date(Date.now() + 86400000).toISOString(), join_link: 'https://meet.google.com/abc-xyz' },
          { id: 2, title: 'Tailwind CSS Workshop', scheduled_time: new Date(Date.now() + 172800000).toISOString(), join_link: 'https://meet.google.com/def-uvw' }
        ]
        isLoading.value = false
      }, 500)
    } catch (err) {
      error.value = err.message
      isLoading.value = false
    }
  }

  // Sync with Google Classroom
  const syncWithGoogleClassroom = async () => {
    isLoading.value = true
    error.value = null
    try {
      // TODO: Replace with actual trigger for backend sync API
      console.log('Syncing with Google Classroom...')
      setTimeout(() => {
        alert('Successfully synced with Google Classroom!')
        fetchLiveSessions() // Refresh sessions after sync
      }, 1500)
    } catch (err) {
      error.value = err.message
      isLoading.value = false
    }
  }

  return {
    resources,
    liveSessions,
    isLoading,
    error,
    fetchResources,
    uploadResource,
    fetchLiveSessions,
    syncWithGoogleClassroom
  }
})
