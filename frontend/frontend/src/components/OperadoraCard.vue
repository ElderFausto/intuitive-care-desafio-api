<template>
  <div class="card">
    <div class="card-header">
      <h3>{{ operadora.razao_social }}</h3>
      <span class="badge">{{ operadora.modalidade }}</span>
    </div>
    
    <div class="card-body">
      <div class="info-row">
        <span class="label">CNPJ:</span>
        <span class="value cnpj">{{ operadora.cnpj }}</span>
      </div>
      
      <div class="info-row">
        <span class="label">Registro ANS:</span>
        <span class="value">{{ operadora.registro_ans }}</span>
      </div>

      <div class="divider"></div>

      <p v-if="operadora.telefone" class="contact">
        📞 {{ operadora.telefone }}
      </p>
      
      <p class="location">
        📍 {{ operadora.cidade }} - {{ operadora.uf }}
      </p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  operadora: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 16px;
  transition: transform 0.2s, box-shadow 0.2s;
  background: #fff;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  border-color: #cbd5e0;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
  gap: 8px;
}

h3 {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  color: #2d3748;
  line-height: 1.4;
}

.badge {
  background-color: #c6f6d5;
  color: #22543d;
  font-size: 0.75rem;
  padding: 2px 8px;
  border-radius: 9999px;
  white-space: nowrap;
  font-weight: 600;
}

.info-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 4px;
  font-size: 0.875rem;
}

.label {
  color: #718096;
}

.value {
  font-weight: 500;
  color: #4a5568;
}

.cnpj {
  font-family: monospace;
}

.divider {
  height: 1px;
  background-color: #edf2f7;
  margin: 12px 0;
}

.contact {
  font-size: 0.875rem;
  color: #4a5568;
  margin: 4px 0;
}

.location {
  font-size: 0.8rem;
  color: #718096;
  margin-top: 8px;
  font-style: italic;
  text-align: right;
}
</style>