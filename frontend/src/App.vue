<template>
  <div class="app-container">
    <header>
      <div class="logo-container">
        <img src="./assets/logo.png" alt="Intuitive Care logo" class="brand-logo"/>
      </div>
      <p class="subtitle">Busca oficial de operadoras ativas na ANS</p>
    </header>

    <main>
      <div class="search-wrapper">
        <div class="input-group">
          
          <div class="select-wrapper">
            <select v-model="selectedUf" @change="handleInput" class="uf-select">
              <option value="">Todos</option>
              <option v-for="uf in ufs" :key="uf" :value="uf">{{ uf }}</option>
            </select>
            <span class="select-arrow">▼</span>
          </div>
          
          <div class="divider"></div>

          <span class="search-icon">🔍</span>
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Nome, Razão Social ou CNPJ..."
            @input="handleInput"
            class="search-input"
          />
          <div v-if="loading" class="spinner"></div>
        </div>
      </div>

      <div class="results-area">
        <div v-if="hasSearched && !loading" class="status-msg">
          <p v-if="operadoras.length > 0" class="success">
            Exibindo <strong>{{ operadoras.length }}</strong> resultados
            <span v-if="selectedUf"> em <strong>{{ selectedUf }}</strong></span>.
          </p>
          <p v-else class="empty">
            Nenhum resultado para "{{ searchQuery }}"
            <span v-if="selectedUf"> em {{ selectedUf }}</span>.
          </p>
        </div>

        <div class="cards-grid">
          <template v-if="loading">
            <div v-for="n in 6" :key="n" class="skeleton">
              <div class="skeleton-title"></div>
              <div class="skeleton-text"></div>
              <div class="skeleton-text"></div>
              <div class="skeleton-text short"></div>
            </div>
          </template>

          <template v-else>
            <OperadoraCard
              v-for="op in operadoras"
              :key="op.registro_ans"
              :operadora="op"
            />
          </template>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import debounce from "lodash/debounce";
import OperadoraCard from "./components/OperadoraCard.vue";

const searchQuery = ref("");
const selectedUf = ref(""); 
const ufs = ref([]);        
const operadoras = ref([]);
const loading = ref(false);
const hasSearched = ref(false);

const API_BASE = import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL.replace('/operadoras/search', '') : "http://127.0.0.1:8000";

onMounted(async () => {
  try {
    const response = await axios.get(`${API_BASE}/operadoras/ufs`);
    ufs.value = response.data;
  } catch (error) {
    console.error("Erro ao carregar UFs:", error);
  }
});

const fetchOperadoras = async (query) => {
  if (!query || query.length < 3) {
    operadoras.value = [];
    hasSearched.value = false;
    loading.value = false;
    return;
  }
  
  loading.value = true;
  hasSearched.value = true;

  try {
    const params = { q: query, limit: 50 };
    if (selectedUf.value) {
      params.uf = selectedUf.value;
    }

    const response = await axios.get(`${API_BASE}/operadoras/search`, { params });
    operadoras.value = response.data;
    
  } catch (error) {
    console.error("Erro na API:", error);
    operadoras.value = [];
  } finally {
    loading.value = false;
  }
};

const debouncedSearch = debounce((query) => {
  fetchOperadoras(query);
}, 500);

const handleInput = () => {
  debouncedSearch(searchQuery.value);
};
</script>

<style scoped>
.app-container {
  max-width: 75rem; 
  margin: 0 auto;
  padding: 0 1.25rem 3.75rem 1.25rem;
  font-family: "Inter", sans-serif;
  color: #1c2b4b;
}

header {
  padding: 3.125rem 1.25rem 5.625rem 1.25rem;
  margin: 0 -1.25rem 0 -1.25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  text-align: center;
}

.logo-container {
  width: 100%;
  max-width: 17.5rem;
  margin-bottom: 0.75rem;
  transition: max-width 0.3s ease;
  display: flex; 
  justify-content: center;
  margin-left: auto;
  margin-right: auto;
}

.brand-logo { width: 100%; height: auto; display: block; }

.subtitle {
  color: #a0aec0;
  font-size: 1rem;
  margin: 0;
  font-weight: 300;
  letter-spacing: 0.031rem;
  text-align: center;
  padding: 0 0.625rem;
}

.search-wrapper {
  margin-top: -2.81rem; 
  margin-bottom: 2.5rem;
  max-width: 43.75rem;
  margin-left: auto;
  margin-right: auto;
  position: relative;
  z-index: 10;
  padding: 0 0.625rem;
}

.input-group {
  position: relative;
  background: white;
  border-radius: 3.125rem;
  box-shadow: 0 0.625rem 1.56rem rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  padding: 0.31rem 0.625rem;
  transition: transform 0.2s;
}

.input-group:focus-within {
  transform: translateY(-0.125rem);
  box-shadow: 0 0.93rem 2.18rem rgba(0, 0, 0, 0.15);
}

.select-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.uf-select {
  appearance: none;
  border: none;
  background: transparent;
  padding: 1rem 1.5rem 1rem 1.2rem;
  font-size: 1rem;
  color: #1c2b4b;
  font-weight: 600;
  cursor: pointer;
  outline: none;
}

.select-arrow {
  position: absolute;
  right: 0.5rem;
  font-size: 0.7rem;
  color: #a0aec0;
  pointer-events: none;
}

.divider {
  width: 1px; height: 24px; background-color: #e2e8f0; margin: 0 0.5rem;
}

.search-icon {
  font-size: 1.2rem;
  padding-left: 0.5rem;
  opacity: 0.5;
  display: flex;
  align-items: center;
}

.search-input {
  width: 100%;
  padding: 1.125rem 1rem;
  font-size: 1.1rem;
  border: none;
  background: transparent;
  outline: none;
  color: #1c2b4b;
}
.search-input::placeholder { color: #a0aec0; }

.spinner {
  width: 1.25rem; height: 1.25rem;
  border: 0.125rem solid #f3f3f3;
  border-top: 0.125rem solid #ff4081;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-right: 0.93rem;
  flex-shrink: 0;
}
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

.status-msg { text-align: center; margin-bottom: 1.875rem; color: #7a869a; }
.success { color: #2d3748; }
.empty { background: #fff5f5; color: #c53030; padding: 0.625rem 1.25rem; border-radius: 0.5rem; display: inline-block; font-size: 0.9rem; }

.cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  
  row-gap: 3rem; 
  column-gap: 2rem;
  
  padding-bottom: 3rem;
}

@keyframes shimmer { 100% { transform: translateX(100%); } }
.skeleton-title { height: 20px; background: #eee; border-radius: 4px; margin-bottom: 15px; width: 60%; }
.skeleton-text { height: 12px; background: #eee; border-radius: 4px; margin-bottom: 8px; width: 100%; }
.skeleton-text.short { width: 40%; }

@media (max-width: 56.25rem) {
  .cards-grid { 
    grid-template-columns: repeat(2, 1fr);
    row-gap: 2.5rem;
  }
}

@media (max-width: 40rem) {
  header { padding: 1.875rem 1.25rem 4.375rem 1.25rem; align-items: center; text-align: center; }
  .logo-container { max-width: 11.25rem; margin-left: auto; margin-right: auto; }
  .brand-logo { margin: 0 auto; }
  .subtitle { font-size: 0.9rem; padding: 0 1rem; }
  .search-wrapper { margin-top: -2.18rem; padding: 0; }
  .search-input { padding: 0.875rem 0.75rem; font-size: 1rem; }
  .search-icon { padding-left: 0.75rem; font-size: 1rem; }
  
  .cards-grid { 
    grid-template-columns: 1fr; 
    row-gap: 2.5rem; 
  }
  
  .app-container { padding-bottom: 4rem; }
}
</style>
