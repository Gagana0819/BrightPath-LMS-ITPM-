import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/api/axios'

export const useContentStore = defineStore('content', () => {
  const resources = ref([])
  const liveSessions = ref([])
  const isLoading = ref(false)
  const isSyncing = ref(false)
  const error = ref(null)

  // Fetch resources (optionally filtered by module_code or user_only)
  const fetchResources = async (options = {}) => {
    const { moduleCode = null, userOnly = false, category = null } = options
    isLoading.value = true
    error.value = null
    try {
      const params = {}
      if (moduleCode) params.module_code = moduleCode
      if (userOnly) params.user_only = 'true'
      if (category) params.category = category // If backend supports category filtering later

      const response = await api.get('core/resources/', { params })
      resources.value = response.data
    } catch (err) {
      error.value = err.response?.data?.detail || err.message
    } finally {
      isLoading.value = false
    }
  }

  // Upload a new resource
  const uploadResource = async (resourceData, file) => {
    isLoading.value = true
    error.value = null
    try {
      const formData = new FormData()
      formData.append('title', resourceData.title)
      formData.append('module_code', resourceData.module_code)
      formData.append('resource_type', resourceData.resource_type)
      formData.append('file', file)

      const response = await api.post('core/resources/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      
      resources.value.unshift(response.data)
      return response.data
    } catch (err) {
      error.value = err.response?.data || { message: err.message }
      throw error.value
    } finally {
      isLoading.value = false
    }
  }
// ... rest of the functions (delete, update, fetchLiveSessions, syncWithGoogleClassroom remains similar but can be updated later if needed)
  // Delete a resource
  const deleteResource = async (id) => {
    // To be implemented in backend
    resources.value = resources.value.filter(r => r.id !== id)
  }

  // Update a resource
  const updateResource = async (id, updatedData) => {
    // To be implemented in backend
    const index = resources.value.findIndex(r => r.id === id)
    if (index !== -1) {
      resources.value[index] = { ...resources.value[index], ...updatedData }
    }
  }

  // Fetch live sessions (still mocked for now as per Kuppi sessions request)
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
