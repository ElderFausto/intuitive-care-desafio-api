<template>
  <div class="app-container">
    <header>
      <div class="logo-container">
        <img src="./assets/logo.png" alt="Intuitive Care logo" />
      </div>
      <p class="subtitle">Busca oficial de operadoras ativas na ANS</p>
    </header>

    <main>
      <div class="search-wrapper">
        <div class="input-group">
          <span class="search-icon">🔍</span>
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Digite o nome, razão social ou CNPJ..."
            @input="handleInput"
            class="search-input"
          />
          <div v-if="loading" class="spinner"></div>
        </div>
      </div>

      <div class="results-area">
        <div v-if="hasSearched && !loading" class="status-msg">
          <p v-if="operadoras.length > 0" class="success">
            Encontramos <strong>{{ operadoras.length }}</strong> operadoras
            relevantes.
          </p>
          <p v-else class="empty">Nenhum resultado para "{{ searchQuery }}".</p>
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
import { ref } from "vue";
import axios from "axios";
import debounce from "lodash/debounce";
import OperadoraCard from "./components/OperadoraCard.vue";

const searchQuery = ref("");
const operadoras = ref([]);
const loading = ref(false);
const hasSearched = ref(false);
const API_URL = "http://127.0.0.1:8000/operadoras/search";

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
    const response = await axios.get(API_URL, { params: { q: query } });
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
  max-width: 62.5rem; /* 1000px */
  margin: 0 auto;
  padding: 0 1.25rem 3.75rem 1.25rem; /* 0 20px 60px 20px */
  font-family: "Inter", sans-serif;
  color: #1c2b4b;
}

header {
  padding: 3.125rem 1.25rem 5.625rem 1.25rem;
  margin: 0 -1.25rem 0 -1.25rem;
  display: flex;
  flex-direction: column;
  align-items: center; /* Centraliza horizontalmente o container da logo e o texto */
  position: relative;
  text-align: center; /* Garante que textos quebrem centralizados */
}

/* LOGO CENTRALIZADA */
.logo-container {
  width: 100%;
  max-width: 17.5rem; /* 280px Desktop */
  margin-bottom: 0.75rem;
  transition: max-width 0.3s ease;
  
  /* CENTRALIZAÇÃO: */
  display: flex; 
  justify-content: center; /* Centraliza a imagem DENTRO do container */
  margin-left: auto;      /* Garante margens iguais */
  margin-right: auto;
}

.brand-logo {
  width: 100%;
  height: auto;
  display: block;
}

.subtitle {
  color: #a0aec0;
  font-size: 1rem;
  margin: 0;
  font-weight: 300;
  letter-spacing: 0.031rem;
  text-align: center;
  padding: 0 0.625rem;
}

/* BARRA DE PESQUISA */
.search-wrapper {
  margin-top: -2.81rem; 
  margin-bottom: 2.5rem;
  max-width: 31.25rem;
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

.search-icon {
  font-size: 1.2rem;
  padding-left: 0.93rem;
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

.search-input::placeholder {
  color: #a0aec0;
}

.spinner {
  width: 1.25rem;
  height: 1.25rem;
  border: 0.125rem solid #f3f3f3;
  border-top: 0.125rem solid #ff4081;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-right: 0.93rem;
  flex-shrink: 0;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.status-msg {
  text-align: center;
  margin-bottom: 1.875rem;
  color: #7a869a;
}

.success { color: #2d3748; }
.empty {
  background: #fff5f5;
  color: #c53030;
  padding: 0.625rem 1.25rem;
  border-radius: 0.5rem;
  display: inline-block;
  font-size: 0.9rem;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
  gap: 1.5rem;
}

/* Mobile*/
@media (max-width: 40rem) {
  header {
    padding: 1.875rem 1.25rem 4.375rem 1.25rem;
    align-items: center;
    text-align: center;
  }

  .logo-container {
    max-width: 11.25rem;
    margin-left: auto; 
    margin-right: auto;
    display: flex;
    justify-content: center;
  }
  
  .brand-logo {
    margin: 0 auto;
  }

  .subtitle {
    font-size: 0.9rem;
    padding: 0 1rem;
  }

  .search-wrapper {
    margin-top: -2.18rem;
    padding: 0;
  }

  .search-input {
    padding: 0.875rem 0.75rem;
    font-size: 1rem;
  }

  .search-icon {
    padding-left: 0.75rem;
    font-size: 1rem;
  }

  .cards-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .app-container {
    padding-bottom: 2.5rem;
  }
}
</style>