<template>
  <div class="app-container">
    <header>
      <div class="logo-area">
        <h1>Busca Operadoras</h1>
        <span class="tag">ANS</span>
      </div>
      <p>Pesquise na base de dados oficial da Agência Nacional de Saúde.</p>
    </header>

    <main>
      <div class="search-wrapper">
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Digite o nome, razão social ou fantasia..."
          class="search-input"
        />
        </div>

      <div class="results-area">
        <div class="status-msg">
          <p class="success">
            Operadoras
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
import OperadoraCard from './components/OperadoraCard.vue'

const searchQuery = ref('')

const operadoras = ref([
  {
    registro_ans: "123456",
    cnpj: "00.000.000/0001-99",
    razao_social: "UNIMED EXEMPLO LTDA",
    modalidade: "Cooperativa Médica",
    cidade: "Xique-Xique",
    uf: "BA",
    telefone: "(11) 9999-9999",
    email: "contato@exemplo.com"
  },
  {
    registro_ans: "654321",
    cnpj: "11.111.111/0001-11",
    razao_social: "BRADESCO SAÚDE TESTE",
    modalidade: "Seguradora",
    cidade: "Rio de Janeiro",
    uf: "RJ",
    telefone: "(21) 8888-8888",
    email: "sac@teste.com"
  },
  {
    registro_ans: "789012",
    cnpj: "22.222.222/0001-22",
    razao_social: "ODONTO PREV S.A.",
    modalidade: "Odontologia",
    cidade: "Curitiba",
    uf: "PR",
    telefone: "(41) 3333-3333",
    email: ""
  }
])
</script>

<style scoped>
.app-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 20px;
  font-family: 'Segoe UI', sans-serif;
  color: #2c3e50;
}

header {
  text-align: center;
  margin-bottom: 50px;
}

.logo-area {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

h1 {
  font-size: 2.2rem;
  font-weight: 700;
  margin: 0;
  color: #2d3748;
}

.tag {
  background: #42b983;
  color: white;
  padding: 4px 8px;
  border-radius: 6px;
  font-weight: bold;
  font-size: 0.9rem;
  letter-spacing: 0.5px;
}

header p {
  color: #718096;
  font-size: 1.1rem;
  margin-top: 8px;
}

.search-wrapper {
  position: relative;
  margin-bottom: 40px;
}

.search-input {
  width: 100%;
  padding: 18px 24px;
  font-size: 1.1rem;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  outline: none;
  transition: all 0.3s;
  box-shadow: 0 4px 6px rgba(0,0,0,0.01);
  box-sizing: border-box;
}

.search-input:focus {
  border-color: #42b983;
  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.2);
}

.status-msg {
  text-align: center;
  margin-bottom: 24px;
  color: #718096;
  font-size: 0.95rem;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

/* Responsividade */
@media (max-width: 640px) {
  .cards-grid { grid-template-columns: 1fr; }
  h1 { font-size: 1.8rem; }
  .app-container { padding: 20px 16px; }
}
</style>