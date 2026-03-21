<script setup>
import RegisterForm from '../components/identity/RegisterForm.vue'
import AppNavbar from '../components/layout/AppNavbar.vue'
</script>

<template>
  <div class="min-h-screen bg-slate-50 flex flex-col font-sans text-content bg-[url('/bg-pattern.svg')] bg-cover">
    <AppNavbar />
    
    <main class="flex-1 flex items-center justify-center p-4 pt-24 md:pt-[100px]">
      <RegisterForm />
    </main>
  </div>
</template>
