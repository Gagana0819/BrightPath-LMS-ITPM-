import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '../api/axios'

export const useWalletStore = defineStore('wallet', () => {
    const balance = ref(0)
    const lifetimePoints = ref(0)
    const tier = ref('BRONZE')
    const recentActivity = ref([])
    const leaderboard = ref([])
    const globalStats = ref({
        total_resources: 0,
        total_students: 0,
        gold_ranked: 0,
        total_lecturers: 0
    })
    const isLoading = ref(false)
    const error = ref(null)

    const fetchWalletData = async () => {
        isLoading.value = true
        error.value = null
        try {
            const response = await api.get('core/wallet/')
            balance.value = response.data.balance || 0
            lifetimePoints.value = response.data.lifetime_points || 0
            tier.value = response.data.tier || 'BRONZE'
            recentActivity.value = response.data.recent_activity || []
        } catch (err) {
            error.value = err.response?.data || err.message
        } finally {
            isLoading.value = false
        }
    }

    const fetchLeaderboard = async () => {
        try {
            const response = await api.get('core/wallet/leaderboard/')
            leaderboard.value = response.data
        } catch (err) {
            console.error('Leaderboard error:', err)
        }
    }

    const fetchGlobalStats = async () => {
        try {
            const response = await api.get('core/wallet/global_stats/')
            globalStats.value = response.data
        } catch (err) {
            console.error('Global stats error:', err)
        }
    }

    const downloadStatement = async () => {
        try {
            const response = await api.get('core/wallet/download_statement/', {
                responseType: 'blob'
            })
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a')
            link.href = url
            link.setAttribute('download', `BrightPath_Statement.pdf`)
            document.body.appendChild(link)
            link.click()
            link.remove()
        } catch (err) {
            console.error('Download error:', err)
        }
    }

    return {
        balance,
        lifetimePoints,
        tier,
        recentActivity,
        leaderboard,
        globalStats,
        isLoading,
        error,
        fetchWalletData,
        fetchLeaderboard,
        fetchGlobalStats,
        downloadStatement
    }
})
