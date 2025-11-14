<template>
  <div class="max-w-6xl mx-auto">
    <h1 class="text-3xl font-bold mb-8">📊 Analytics Dashboard</h1>
    
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
      <!-- Stats Cards -->
      <div class="bg-white rounded-lg shadow-lg p-6">
        <div class="flex items-center">
          <div class="bg-blue-100 rounded-lg p-3">
            <span class="text-2xl">🎲</span>
          </div>
          <div class="ml-4">
            <p class="text-gray-600">Total Spins</p>
            <p class="text-2xl font-bold text-blue-600">{{ stats.totalSpins }}</p>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-lg shadow-lg p-6">
        <div class="flex items-center">
          <div class="bg-green-100 rounded-lg p-3">
            <span class="text-2xl">👥</span>
          </div>
          <div class="ml-4">
            <p class="text-gray-600">Active Names</p>
            <p class="text-2xl font-bold text-green-600">{{ stats.activeNames }}</p>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-lg shadow-lg p-6">
        <div class="flex items-center">
          <div class="bg-purple-100 rounded-lg p-3">
            <span class="text-2xl">🏆</span>
          </div>
          <div class="ml-4">
            <p class="text-gray-600">Most Selected</p>
            <p class="text-lg font-bold text-purple-600">{{ stats.mostSelected }}</p>
          </div>
        </div>
      </div>
    </div>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Recent Results -->
      <div class="bg-white rounded-lg shadow-lg p-6">
        <h2 class="text-xl font-semibold mb-4">🕐 Recent Results</h2>
        
        <div class="space-y-3 max-h-96 overflow-y-auto">
          <div 
            v-for="(result, index) in recentResults" 
            :key="index"
            class="flex justify-between items-center p-3 bg-gray-50 rounded"
          >
            <div>
              <p class="font-semibold">{{ result.name }}</p>
              <p class="text-sm text-gray-600">{{ result.timestamp }}</p>
            </div>
            <span class="text-2xl">🎯</span>
          </div>
        </div>
      </div>
      
      <!-- Name Frequency -->
      <div class="bg-white rounded-lg shadow-lg p-6">
        <h2 class="text-xl font-semibold mb-4">📈 Name Frequency</h2>
        
        <div class="space-y-3">
          <div 
            v-for="(freq, index) in nameFrequency" 
            :key="index"
            class="flex items-center justify-between"
          >
            <span class="font-medium">{{ freq.name }}</span>
            <div class="flex items-center">
              <div class="w-32 bg-gray-200 rounded-full h-2 mr-3">
                <div 
                  class="bg-blue-600 h-2 rounded-full"
                  :style="{ width: freq.percentage + '%' }"
                ></div>
              </div>
              <span class="text-sm text-gray-600 w-12">{{ freq.count }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Export Section -->
    <div class="mt-8 bg-white rounded-lg shadow-lg p-6">
      <h2 class="text-xl font-semibold mb-4">💾 Export Data</h2>
      <div class="flex gap-4">
        <button 
          @click="exportResults"
          class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition-colors"
        >
          📊 Export Results CSV
        </button>
        <button 
          @click="exportStatistics"
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors"
        >
          📈 Export Statistics JSON
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// Sample data - will be replaced with API calls
const stats = ref({
  totalSpins: 156,
  activeNames: 6,
  mostSelected: 'Alice Johnson'
})

const recentResults = ref([
  { name: 'Bob Smith', timestamp: '2 minutes ago' },
  { name: 'Alice Johnson', timestamp: '5 minutes ago' },
  { name: 'Charlie Brown', timestamp: '8 minutes ago' },
  { name: 'Diana Wilson', timestamp: '12 minutes ago' },
  { name: 'Alice Johnson', timestamp: '15 minutes ago' },
  { name: 'Edward Davis', timestamp: '18 minutes ago' }
])

const nameFrequency = ref([
  { name: 'Alice Johnson', count: 12, percentage: 85 },
  { name: 'Bob Smith', count: 10, percentage: 71 },
  { name: 'Charlie Brown', count: 8, percentage: 57 },
  { name: 'Diana Wilson', count: 6, percentage: 43 },
  { name: 'Edward Davis', count: 4, percentage: 29 },
  { name: 'Fiona Taylor', count: 2, percentage: 14 }
])

const exportResults = () => {
  const csvContent = "data:text/csv;charset=utf-8," + 
    "Name,Timestamp\n" +
    recentResults.value.map(r => `"${r.name}","${r.timestamp}"`).join("\n")
  
  const encodedUri = encodeURI(csvContent)
  const link = document.createElement("a")
  link.setAttribute("href", encodedUri)
  link.setAttribute("download", "roulette-results.csv")
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

const exportStatistics = () => {
  const data = {
    stats: stats.value,
    nameFrequency: nameFrequency.value,
    exportDate: new Date().toISOString()
  }
  
  const dataStr = JSON.stringify(data, null, 2)
  const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr)
  
  const linkElement = document.createElement('a')
  linkElement.setAttribute('href', dataUri)
  linkElement.setAttribute('download', 'roulette-statistics.json')
  linkElement.click()
}
</script>