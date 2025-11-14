import { defineStore } from 'pinia'
import { ref } from 'vue'

export interface Name {
  id: string
  name: string
  isActive: boolean
  weight: number
}

export interface GameResult {
  id: string
  selectedName: string
  sessionId: string
  timestamp: Date
  availableNames: string[]
}

export const useRouletteStore = defineStore('roulette', () => {
  const names = ref<Name[]>([])
  const isSpinning = ref(false)
  const lastResult = ref<GameResult | null>(null)
  const spinHistory = ref<GameResult[]>([])
  const sessionId = ref(crypto.randomUUID())
  
  const activeNames = computed(() => 
    names.value.filter(name => name.isActive)
  )
  
  const spin = async () => {
    if (activeNames.value.length === 0) {
      throw new Error('No active names available')
    }
    
    isSpinning.value = true
    
    try {
      // Simulate API call to backend
      const randomIndex = Math.floor(Math.random() * activeNames.value.length)
      const selectedName = activeNames.value[randomIndex]
      
      const result: GameResult = {
        id: crypto.randomUUID(),
        selectedName: selectedName.name,
        sessionId: sessionId.value,
        timestamp: new Date(),
        availableNames: activeNames.value.map(n => n.name)
      }
      
      lastResult.value = result
      spinHistory.value.unshift(result)
      
      return result
    } finally {
      isSpinning.value = false
    }
  }
  
  const addName = (name: string) => {
    if (!names.value.some(n => n.name === name)) {
      names.value.push({
        id: crypto.randomUUID(),
        name,
        isActive: true,
        weight: 1
      })
    }
  }
  
  const removeName = (id: string) => {
    const index = names.value.findIndex(n => n.id === id)
    if (index > -1) {
      names.value.splice(index, 1)
    }
  }
  
  const toggleNameActive = (id: string) => {
    const name = names.value.find(n => n.id === id)
    if (name) {
      name.isActive = !name.isActive
    }
  }
  
  return {
    names,
    isSpinning,
    lastResult,
    spinHistory,
    sessionId,
    activeNames,
    spin,
    addName,
    removeName,
    toggleNameActive
  }
})