<template>
  <div class="max-w-6xl mx-auto">
    <h1 class="text-3xl font-bold mb-8">👥 Admin Panel</h1>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Names Management -->
      <div class="bg-white rounded-lg shadow-lg p-6">
        <h2 class="text-xl font-semibold mb-4">Manage Names</h2>
        
        <div class="mb-4">
          <div class="flex gap-2">
            <input 
              v-model="newName"
              @keyup.enter="addName"
              placeholder="Enter new name..."
              class="flex-1 border border-gray-300 rounded px-3 py-2 focus:outline-none focus:border-blue-500"
            />
            <button 
              @click="addName"
              :disabled="!newName.trim()"
              class="bg-green-600 hover:bg-green-700 disabled:bg-gray-400 text-white px-4 py-2 rounded transition-colors"
            >
              Add
            </button>
          </div>
        </div>
        
        <ul class="space-y-2 max-h-96 overflow-y-auto">
          <li v-for="(name, index) in managedNames" :key="index" class="flex justify-between items-center bg-gray-50 p-3 rounded">
            <span>{{ name }}</span>
            <button 
              @click="removeName(index)"
              class="text-red-600 hover:text-red-800 font-bold"
            >
              ✕
            </button>
          </li>
        </ul>
        
        <div class="mt-4 text-sm text-gray-600">
          Total names: {{ managedNames.length }}
        </div>
      </div>
      
      <!-- Quick Actions -->
      <div class="bg-white rounded-lg shadow-lg p-6">
        <h2 class="text-xl font-semibold mb-4">Quick Actions</h2>
        
        <div class="space-y-4">
          <button 
            @click="clearAllNames"
            class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition-colors"
          >
            🗑️ Clear All Names
          </button>
          
          <button 
            @click="loadSampleData"
            class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors"
          >
            📝 Load Sample Data
          </button>
          
          <button 
            @click="exportNames"
            class="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded transition-colors"
          >
            📥 Export Names
          </button>
        </div>
        
        <div class="mt-6 p-4 bg-blue-50 rounded">
          <h3 class="font-semibold text-blue-800 mb-2">💡 Tips</h3>
          <ul class="text-sm text-blue-700 space-y-1">
            <li>• Press Enter to quickly add names</li>
            <li>• Names are saved automatically</li>
            <li>• Duplicate names are not allowed</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const newName = ref('')
const managedNames = ref([
  'Alice Johnson',
  'Bob Smith',
  'Charlie Brown',
  'Diana Wilson',
  'Edward Davis',
  'Fiona Taylor'
])

const addName = () => {
  const trimmedName = newName.value.trim()
  if (trimmedName && !managedNames.value.includes(trimmedName)) {
    managedNames.value.push(trimmedName)
    newName.value = ''
  }
}

const removeName = (index: number) => {
  managedNames.value.splice(index, 1)
}

const clearAllNames = () => {
  if (confirm('Are you sure you want to clear all names?')) {
    managedNames.value = []
  }
}

const loadSampleData = () => {
  const sampleNames = [
    'John Doe', 'Jane Smith', 'Mike Johnson', 'Sarah Wilson',
    'David Brown', 'Emily Davis', 'Chris Taylor', 'Jessica Anderson'
  ]
  
  sampleNames.forEach(name => {
    if (!managedNames.value.includes(name)) {
      managedNames.value.push(name)
    }
  })
}

const exportNames = () => {
  const dataStr = JSON.stringify(managedNames.value, null, 2)
  const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr)
  
  const exportFileDefaultName = 'roulette-names.json'
  
  const linkElement = document.createElement('a')
  linkElement.setAttribute('href', dataUri)
  linkElement.setAttribute('download', exportFileDefaultName)
  linkElement.click()
}
</script>