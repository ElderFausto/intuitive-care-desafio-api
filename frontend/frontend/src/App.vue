<template>
  <div class="app-container">
    <header>
      <div class="logo-area">
        <h1>Buscar Operadoras</h1>
      </div>
      <p>Encontre informações detalhadas sobre operadoras de saúde no Brasil.</p>
    </header>

    <main>
      <div class="search-wrapper">
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Digite o nome, razão social ou fantasia..."
          @input="handleInput"
          class="search-input"
        />
        <div v-if="loading" class="spinner"></div>
      </div>

      <div class="results-area">
        <div v-if="hasSearched && !loading" class="status-msg">
          <p v-if="operadoras.length > 0" class="success">
            Encontramos <strong>{{ operadoras.length }}</strong> operadoras relevantes.
          </p>
          <p v-else class="empty">
            Nenhum resultado encontrado para "{{ searchQuery }}".
          </p>
        </div>

        <div class="cards-grid">
          <OperadoraCard 
            v-for="op in operadoras" 
            :key="op.registro_ans" 
            :operadora="op" 
          />
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import debounce from 'lodash/debounce'
import OperadoraCard from './components/OperadoraCard.vue'

const searchQuery = ref('')
const operadoras = ref([])
const loading = ref(false)
const hasSearched = ref(false)

const API_URL = 'http://127.0.0.1:8000/operadoras/search'

const fetchOperadoras = async (query) => {
  if (!query || query.length < 3) {
    operadoras.value = []
    hasSearched.value = false
    loading.value = false
    return
  }

  loading.value = true
  hasSearched.value = true

  try {
    const response = await axios.get(API_URL, {
      params: { q: query }
    })
    operadoras.value = response.data
  } catch (error) {
    console.error("Erro na API:", error)
    operadoras.value = []
  } finally {
    loading.value = false
  }
}

// Debounce de 500ms
const debouncedSearch = debounce((query) => {
  fetchOperadoras(query)
}, 500)

const handleInput = () => {
  debouncedSearch(searchQuery.value)
}
</script>

<style scoped>
.app-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px 60px 20px;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #1C2B4B;
}

header {
  background: linear-gradient(135deg, #b115c5 0%, #2A4068 100%);
  color: white;
  padding: 60px 20px;
  border-radius: 0 0 30px 30px;
  margin: 0 -20px 50px -20px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(28, 43, 75, 0.2);
}

.logo-area {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

h1 {
  font-size: 2.5rem;
  font-weight: 800;
  margin: 0;
  letter-spacing: -1px;
}

.tag {
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  padding: 4px 10px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.8rem;
  backdrop-filter: blur(4px);
}

header p {
  color: rgba(255, 255, 255, 0.8);
  font-size: 1.1rem;
  font-weight: 300;
  margin-top: 8px;
}

/* BUSCA ESTILIZADA */
.search-wrapper {
  position: relative;
  margin-bottom: 40px;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  top: -30px; 
}

.search-input {
  width: 100%;
  padding: 22px 60px 22px 28px;
  font-size: 1.15rem;
  border: 0;
  border-radius: 16px;
  outline: none;
  transition: all 0.3s ease;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  box-sizing: border-box;
  background: white;
  color: #1C2B4B;
}

.search-input::placeholder {
  color: #A0AEC0;
}

.search-input:focus {
  transform: translateY(-2px);
  box-shadow: 0 15px 35px rgba(28, 43, 75, 0.12);
}

.spinner {
  position: absolute;
  right: 24px;
  top: 50%;
  transform: translateY(-50%);
  width: 24px;
  height: 24px;
  border: 3px solid #f3f3f3;
  border-top: 3px solid #FF4081;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin { 0% { transform: translateY(-50%) rotate(0deg); } 100% { transform: translateY(-50%) rotate(360deg); } }

/* MENSAGENS DE STATUS */
.status-msg {
  text-align: center;
  margin-bottom: 30px;
  color: #7A869A;
  font-size: 0.95rem;
}

.success {
  color: #1C2B4B;
}

.empty {
  background: #FFF5F5;
  color: #C53030;
  padding: 12px 24px;
  border-radius: 8px;
  display: inline-block;
  font-weight: 500;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

@media (max-width: 640px) {
  h1 { font-size: 1.8rem; }
  header { padding: 40px 20px; border-radius: 0 0 20px 20px; }
  .search-wrapper { top: -20px; padding: 0 10px; }
}
</style>