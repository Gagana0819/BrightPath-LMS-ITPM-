import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useContentStore = defineStore('content', () => {
  const resources = ref([
    { id: 1, title: 'Introduction to Vue 3', description: 'Basics of Composition API', category: 'videos', url: 'https://example.com/video1.mp4' },
    { id: 2, title: 'Chapter 1 Notes', description: 'Key points from chapter 1', category: 'notes', url: 'https://example.com/notes1.pdf' },
    { id: 3, title: '2022 Past Paper', description: 'Final exam 2022', category: 'past_papers', url: 'https://example.com/pastpaper.pdf' }
  ])
  const liveSessions = ref([])
  const isLoading = ref(false)
  const isSyncing = ref(false)
  const error = ref(null)

  // Fetch resources based on category (videos, notes, past_papers)
  const fetchResources = async (category) => {
    isLoading.value = true
    error.value = null
    try {
      // Mock data for UI development
      setTimeout(() => {
        // In a real app, this would be an API call
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
      // Simulate real delay for "Premium" feel
      return new Promise((resolve) => {
        setTimeout(() => {
          const newResource = {
            id: Date.now(),
            ...resourceData,
            url: file ? URL.createObjectURL(file) : 'https://example.com/placeholder.pdf'
          }
          resources.value.unshift(newResource)
          isLoading.value = false
          resolve(newResource)
        }, 1500)
      })
    } catch (err) {
      error.value = err.message
      isLoading.value = false
    }
  }

  // Delete a resource
  const deleteResource = async (id) => {
    isLoading.value = true
    setTimeout(() => {
      resources.value = resources.value.filter(r => r.id !== id)
      isLoading.value = false
    }, 500)
  }

  // Update a resource
  const updateResource = async (id, updatedData) => {
    isLoading.value = true
    setTimeout(() => {
      const index = resources.value.findIndex(r => r.id === id)
      if (index !== -1) {
        resources.value[index] = { ...resources.value[index], ...updatedData }
      }
      isLoading.value = false
    }, 500)
  }

  // Fetch live sessions
  const fetchLiveSessions = async () => {
    isLoading.value = true
    error.value = null
    try {
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
    isSyncing.value = true
    error.value = null
    try {
      console.log('Syncing with Google Classroom...')
      return new Promise((resolve) => {
        setTimeout(() => {
          fetchLiveSessions() // Refresh
          isSyncing.value = false
          resolve(true)
        }, 2000)
      })
    } catch (err) {
      error.value = err.message
      isSyncing.value = false
    }
  }

  return {
    resources,
    liveSessions,
    isLoading,
    isSyncing,
    error,
    fetchResources,
    uploadResource,
    deleteResource,
    updateResource,
    fetchLiveSessions,
    syncWithGoogleClassroom
  }
})
