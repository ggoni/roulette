<template>
  <div id="app">
    <nav class="bg-blue-600 text-white p-4">
      <div class="container mx-auto flex justify-between items-center">
        <router-link to="/" class="text-xl font-bold">🎰 Roulette</router-link>
        <div class="space-x-4">
          <router-link to="/" class="hover:text-blue-200">Home</router-link>
          <router-link to="/admin" class="hover:text-blue-200">Admin</router-link>
          <router-link to="/analytics" class="hover:text-blue-200">Analytics</router-link>
        </div>
      </div>
    </nav>
    
    <main class="container mx-auto py-8">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
// App component with navigation
</script>