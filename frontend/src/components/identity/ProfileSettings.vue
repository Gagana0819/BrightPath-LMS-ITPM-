<script setup>
import { ref } from 'vue'

const user = ref({
  firstName: 'Kasun',
  lastName: 'Silva',
  email: 'kasun.s@university.edu',
  studentId: 'SE/2026/045',
  verified: true
})
</script>

<template>
  <div class="w-full max-w-4xl mx-auto space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
    
    <!-- Header -->
    <div>
      <h1 class="text-3xl font-bold tracking-tight text-content mb-2">Profile Settings</h1>
      <p class="text-slate-500">Manage your identity verified status and personal details.</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      
      <!-- Left Column: Avatar & Status -->
      <div class="lg:col-span-1 space-y-6">
        <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 flex flex-col items-center text-center">
          <div class="relative mb-4">
            <img 
              src="https://api.dicebear.com/7.x/notionists/svg?seed=Kasun&backgroundColor=e4f8f6" 
              alt="Profile Avatar" 
              class="w-32 h-32 rounded-full border-4 border-white shadow-md object-cover"
            />
            <button class="absolute bottom-0 right-2 bg-hero-highlight text-white p-2 rounded-full shadow-md hover:bg-blue-700 transition">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
              </svg>
            </button>
          </div>
          <h2 class="text-xl font-bold text-content">{{ user.firstName }} {{ user.lastName }}</h2>
          <p class="text-sm text-slate-500 mb-4">{{ user.studentId }}</p>
          
          <div v-if="user.verified" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-green-50 text-green-700 rounded-full font-medium text-sm border border-green-200">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            ID Verified
          </div>
        </div>
      </div>

      <!-- Right Column: Settings Form -->
      <div class="lg:col-span-2">
        <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
          <h3 class="text-lg font-bold text-content mb-6">Personal Information</h3>
          
          <div class="space-y-5">
            <div class="grid grid-cols-2 gap-5">
              <div class="space-y-1.5">
                <label class="text-sm font-medium text-slate-700">First Name</label>
                <input v-model="user.firstName" type="text" class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-hero-highlight/20 focus:outline-none" />
              </div>
              <div class="space-y-1.5">
                <label class="text-sm font-medium text-slate-700">Last Name</label>
                <input v-model="user.lastName" type="text" class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-hero-highlight/20 focus:outline-none" />
              </div>
            </div>

            <div class="space-y-1.5">
              <label class="text-sm font-medium text-slate-700">University Email Address</label>
              <input v-model="user.email" type="email" disabled class="w-full px-4 py-2.5 bg-slate-100 border border-slate-200 rounded-xl text-slate-500 cursor-not-allowed" />
              <p class="text-xs text-slate-400 mt-1">Contact admin to change your primary academic email.</p>
            </div>

            <div class="pt-4 flex justify-end">
              <button class="px-6 py-2.5 bg-hero-highlight text-white rounded-xl font-bold tracking-wide hover:opacity-90 transition-all shadow-sm">
                Save Changes
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
