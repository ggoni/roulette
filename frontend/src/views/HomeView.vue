<template>
  <div class="max-w-4xl mx-auto">
    <h1 class="text-4xl font-bold text-center mb-8">🎰 Roulette Wheel</h1>
    
    <div class="bg-white rounded-lg shadow-lg p-6">
      <div class="text-center mb-6">
        <div class="w-64 h-64 mx-auto border-4 border-blue-500 rounded-full flex items-center justify-center bg-gradient-to-r from-blue-100 to-purple-100">
          <div v-if="!isSpinning" class="text-2xl font-bold text-gray-700">
            {{ selectedName || 'Ready to Spin!' }}
          </div>
          <div v-else class="animate-spin text-4xl">🎯</div>
        </div>
      </div>
      
      <div class="text-center mb-6">
        <button 
          @click="spin"
          :disabled="isSpinning || names.length === 0"
          class="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-bold py-3 px-8 rounded-lg text-xl transition-colors"
        >
          {{ isSpinning ? 'Spinning...' : 'Spin!' }}
        </button>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <h3 class="text-lg font-semibold mb-3">Available Names ({{ names.length }})</h3>
          <ul class="bg-gray-50 rounded p-4 max-h-64 overflow-y-auto">
            <li v-for="name in names" :key="name" class="py-1 px-2 bg-white rounded mb-1 shadow-sm">
              {{ name }}
            </li>
          </ul>
        </div>
        
        <div v-if="lastResult">
          <h3 class="text-lg font-semibold mb-3">Last Result</h3>
          <div class="bg-green-50 border border-green-200 rounded p-4">
            <p class="text-green-800 font-bold text-xl">🎉 {{ lastResult }}</p>
            <p class="text-green-600 text-sm mt-1">Congratulations!</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouletteStore } from '@/stores/roulette'

const rouletteStore = useRouletteStore()

const isSpinning = ref(false)
const selectedName = ref('')
const lastResult = ref('')

// Sample data - will be replaced with API calls
const names = ref([
  'Alice Johnson',
  'Bob Smith', 
  'Charlie Brown',
  'Diana Wilson',
  'Edward Davis',
  'Fiona Taylor'
])

const spin = async () => {
  if (names.value.length === 0) return
  
  isSpinning.value = true
  selectedName.value = ''
  
  // Simulate spinning animation
  setTimeout(() => {
    const randomIndex = Math.floor(Math.random() * names.value.length)
    const winner = names.value[randomIndex]
    selectedName.value = winner
    lastResult.value = winner
    isSpinning.value = false
  }, 2000)
}

onMounted(() => {
  // Initialize component
})
</script>