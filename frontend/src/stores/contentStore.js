import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '../api/axios'

export const useContentStore = defineStore('content', () => {
  const resources = ref([])
  const liveSessions = ref([])
  const isLoading = ref(false)
  const isSyncing = ref(false)
  const error = ref(null)

  const fetchResources = async (params = {}) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await api.get('core/resources/', { params })
      resources.value = response.data
    } catch (err) {
      error.value = err.response?.data || err.message
    } finally {
      isLoading.value = false
    }
  }

  const uploadResource = async (resourceData, file) => {
    isLoading.value = true
    error.value = null
    try {
      const formData = new FormData()
      Object.keys(resourceData).forEach(key => {
        formData.append(key, resourceData[key])
      })
      formData.append('file', file)
      
      const response = await api.post('core/resources/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      resources.value.unshift(response.data)
      return response.data
    } catch (err) {
      error.value = err.response?.data || err.message
      throw error.value
    } finally {
      isLoading.value = false
    }
  }

  const deleteResource = async (id) => {
    isLoading.value = true
    error.value = null
    try {
      await api.delete(`core/resources/${id}/`)
      resources.value = resources.value.filter(r => r.id !== id)
    } catch (err) {
      error.value = err.response?.data || err.message
    } finally {
      isLoading.value = false
    }
  }

  const updateResource = async (id, resourceData) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await api.put(`core/resources/${id}/`, resourceData)
      const index = resources.value.findIndex(r => r.id === id)
      if (index !== -1) {
        resources.value[index] = response.data
      }
      return response.data
    } catch (err) {
      error.value = err.response?.data || err.message
    } finally {
      isLoading.value = false
    }
  }

  const fetchLiveSessions = async (params = {}) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await api.get('core/kuppi/sessions/', { params })
      liveSessions.value = response.data
    } catch (err) {
      error.value = err.response?.data || err.message
    } finally {
      isLoading.value = false
    }
  }

  const createLiveSession = async (sessionData) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await api.post('core/kuppi/sessions/', sessionData)
      liveSessions.value.unshift(response.data)
      return response.data
    } catch (err) {
      error.value = err.response?.data || err.message
      throw error.value
    } finally {
      isLoading.value = false
    }
  }

  const updateLiveSession = async (id, sessionData) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await api.put(`core/kuppi/sessions/${id}/`, sessionData)
      const index = liveSessions.value.findIndex(s => s.id === id)
      if (index !== -1) {
        liveSessions.value[index] = response.data
      }
      return response.data
    } catch (err) {
      error.value = err.response?.data || err.message
      throw error.value
    } finally {
      isLoading.value = false
    }
  }

  const deleteLiveSession = async (id) => {
    isLoading.value = true
    error.value = null
    try {
      await api.delete(`core/kuppi/sessions/${id}/`)
      liveSessions.value = liveSessions.value.filter(s => s.id !== id)
    } catch (err) {
      error.value = err.response?.data || err.message
      throw error.value
    } finally {
      isLoading.value = false
    }
  }

  const uploadSessionVideo = async (id, file) => {
    isLoading.value = true
    error.value = null
    try {
      const formData = new FormData()
      formData.append('file', file)
      const response = await api.post(`core/kuppi/sessions/${id}/upload-video/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      
      const index = liveSessions.value.findIndex(s => s.id === id)
      if (index !== -1) {
        liveSessions.value[index].video_url = response.data.video_url
        if (response.data.thumbnail) {
          liveSessions.value[index].thumbnail = response.data.thumbnail
        }
      }
      return response.data
    } catch (err) {
      error.value = err.response?.data || err.message
      throw error.value
    } finally {
      isLoading.value = false
    }
  }

  const uploadSessionThumbnail = async (id, file) => {
    isLoading.value = true
    error.value = null
    try {
      const formData = new FormData()
      formData.append('file', file)
      const response = await api.post(`core/kuppi/sessions/${id}/upload-thumbnail/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      
      const index = liveSessions.value.findIndex(s => s.id === id)
      if (index !== -1) {
        liveSessions.value[index].thumbnail = response.data.thumbnail
      }
      return response.data
    } catch (err) {
      error.value = err.response?.data || err.message
      throw error.value
    } finally {
      isLoading.value = false
    }
  }

  const incrementSessionViews = async (id) => {
    try {
      const response = await api.post(`core/kuppi/sessions/${id}/increment-views/`)
      const index = liveSessions.value.findIndex(s => s.id === id)
      if (index !== -1) {
        liveSessions.value[index].view_count = response.data.view_count
      }
    } catch (err) {
      console.error('Failed to increment views', err)
    }
  }

  const syncWithGoogleClassroom = async () => {
    isSyncing.value = true
    error.value = null
    try {
      console.log('Syncing with Google Classroom (simulated)...')
      return new Promise((resolve) => {
        setTimeout(() => {
          fetchLiveSessions({ userOnly: true })
          isSyncing.value = false
          resolve(true)
        }, 1500)
      })
    } catch (err) {
      error.value = err.message
      isSyncing.value = false
    }
  }

  const recordResourceDownload = async (resourceId) => {
    console.log(`DEBUG: Calling recordResourceDownload for resource ID: ${resourceId}`);
    try {
      const response = await api.post(`core/resources/${resourceId}/record-download/`)
      console.log('DEBUG: recordResourceDownload response:', response.data.message);
    } catch (err) {
      console.error('Failed to record download', err)
    }
  }

  const fetchResourceStats = async (resourceId) => {
    try {
      const response = await api.get(`core/resources/${resourceId}/stats/`)
      return response.data
    } catch (err) {
      console.error('Failed to fetch resource stats', err)
      return null
    }
  }

  const fetchResourceReviews = async (resourceId) => {
    try {
      const response = await api.get(`core/resources/${resourceId}/reviews/`)
      return response.data
    } catch (err) {
      console.error('Failed to fetch resource reviews', err)
      return []
    }
  }

  const submitResourceReview = async (resourceId, reviewData) => {
    isLoading.value = true
    error.value = null
    try {
      // Body needs to include the resource ID
      const data = { ...reviewData, resource: resourceId }
      const response = await api.post('core/resources/reviews/add/', data)
      return response.data
    } catch (err) {
      error.value = err.response?.data || err.message
      throw error.value
    } finally {
      isLoading.value = false
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
    createLiveSession,
    updateLiveSession,
    deleteLiveSession,
    uploadSessionVideo,
    uploadSessionThumbnail,
    incrementSessionViews,
    recordResourceDownload,
    recordResourceDownload,
    submitResourceReview,
    fetchResourceStats,
    fetchResourceReviews,
    syncWithGoogleClassroom
  }
})
