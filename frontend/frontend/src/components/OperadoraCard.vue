<template>
  <div class="card">
    <div class="card-header">
      <h3>{{ operadora.razao_social }}</h3>
      <span class="badge">{{ operadora.modalidade }}</span>
    </div>
    
    <div class="card-body">
      <p><strong>CNPJ:</strong> {{ operadora.cnpj }}</p>
      <p><strong>Registro ANS:</strong> {{ operadora.registro_ans }}</p>
      <div class="contact-info">
        <p v-if="operadora.telefone">📞 {{ operadora.telefone }}</p>
        <p v-if="operadora.email">✉️ {{ operadora.email }}</p>
      </div>
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
  border: 0;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 16px;
  /* sombra */
  box-shadow: 0 2px 10px rgba(28, 43, 75, 0.05);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

/* Detalhe colorido na esquerda do card */
.card::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: linear-gradient(180deg, #8E2DE2, #4A00E0);
  opacity: 0;
  transition: opacity 0.3s;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 20px rgba(28, 43, 75, 0.1);
}

.card:hover::before {
  opacity: 1;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
  gap: 12px;
}

h3 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 700;
  color: #1C2B4B;
  line-height: 1.4;
}

.badge {
  background-color: #E8F0FE;
  color: #1C2B4B;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.card-body {
  border-top: 1px solid #F0F2F5;
  padding-top: 16px;
}

.info-row {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
  font-size: 0.9rem;
}

.label {
  color: #7A869A;
  width: 100px;
  flex-shrink: 0;
}

.value {
  font-weight: 500;
  color: #42526E;
}

.cnpj {
  font-family: 'Consolas', monospace;
  background: #F4F5F7;
  padding: 2px 6px;
  border-radius: 4px;
  color: #1C2B4B;
}

.contact-info {
  margin-top: 16px;
  padding-top: 12px;
  border-top: 1px dashed #E0E4E8;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
  color: #42526E;
  font-size: 0.9rem;
}

.location {
  margin-top: 12px;
  font-size: 0.85rem;
  color: #7A869A;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
}
</style>