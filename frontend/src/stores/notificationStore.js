import { defineStore } from 'pinia'
import api from '../api/axios'

export const useNotificationStore = defineStore('notification', {
  state: () => ({
    notifications: [],
    loading: false,
    error: null,
    pollingInterval: null
  }),

  getters: {
    unreadNotifications: (state) => state.notifications.filter(n => !n.is_read),
    unreadCount: (state) => state.notifications.filter(n => !n.is_read).length,
    latestNotifications: (state) => state.notifications.slice(0, 5)
  },

  actions: {
    async fetchNotifications() {
      if (!localStorage.getItem('access_token')) return
      
      this.loading = true
      try {
        const response = await api.get('core/notifications/')
        this.notifications = response.data
      } catch (err) {
        console.error('Failed to fetch notifications:', err)
        this.error = err.message
      } finally {
        this.loading = false
      }
    },

    async markAsRead(id) {
      try {
        await api.patch(`core/notifications/${id}/mark_read/`)
        const notification = this.notifications.find(n => n.id === id)
        if (notification) notification.is_read = true
      } catch (err) {
        console.error('Failed to mark notification as read:', err)
      }
    },

    async markAllRead() {
      try {
        await api.post('core/notifications/mark_all_read/')
        this.notifications.forEach(n => n.is_read = true)
      } catch (err) {
        console.error('Failed to mark all as read:', err)
      }
    },

    startPolling(intervalMs = 30000) {
      if (this.pollingInterval) return
      this.fetchNotifications()
      this.pollingInterval = setInterval(() => {
        this.fetchNotifications()
      }, intervalMs)
    },

    stopPolling() {
      if (this.pollingInterval) {
        clearInterval(this.pollingInterval)
        this.pollingInterval = null
      }
    }
  }
})
