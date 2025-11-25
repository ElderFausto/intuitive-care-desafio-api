<template>
  <div class="card">
    
    <div class="card-header">
      <h3>{{ operadora.razao_social }}</h3>
      
      <span class="badge" :class="getBadgeClass(operadora.modalidade)">
        {{ operadora.modalidade }}
      </span>
    </div>
    
    <div class="card-body">
      <div class="info-row">
        <span class="label">CNPJ:</span>
        <span 
          class="value cnpj clickable" 
          @click="copyCnpj(operadora.cnpj)"
          title="Clique para copiar"
        >
          {{ operadora.cnpj }}
          <span v-if="copied" class="copy-feedback">Copiado!</span>
        </span>
      </div>
      
      <div class="info-row">
        <span class="label">Registro ANS:</span>
        <span class="value">{{ operadora.registro_ans }}</span>
      </div>

      <div class="contact-info">
        <div v-if="operadora.telefone" class="contact-item">
          📞 {{ operadora.telefone }}
        </div>
        <div v-if="operadora.email" class="contact-item">
          ✉️ {{ operadora.email }}
        </div>
      </div>
      
      <p class="location">
        📍 {{ operadora.cidade }} - {{ operadora.uf }}
      </p>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  operadora: {
    type: Object,
    required: true
  }
})

const copied = ref(false);

const copyCnpj = (cnpj) => {
  if (!cnpj) return;
  navigator.clipboard.writeText(cnpj);
  copied.value = true;
  setTimeout(() => { copied.value = false; }, 2000);
}

const getBadgeClass = (modalidade) => {
  if (!modalidade) return 'badge-default';
  const text = String(modalidade).toLowerCase();
  
  if (text.includes('odont')) return 'badge-odonto';
  if (text.includes('medic') || text.includes('médic')) return 'badge-medica';
  if (text.includes('administradora') || text.includes('admin')) return 'badge-admin';
  if (text.includes('seguradora')) return 'badge-seguradora';
  if (text.includes('filantropia')) return 'badge-filantropia';
  
  return 'badge-default';
}
</script>

<style scoped>
.card {
  background: white;
  border: 0;
  border-radius: 0.75rem;
  padding: 1rem;
  
  box-shadow: 0 0.25rem 0.75rem rgba(28, 43, 75, 0.08);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  
  display: flex;
  flex-direction: column;
  height: 100%;
}

.card::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 0.25rem;
  background: linear-gradient(180deg, #8E2DE2, #4A00E0);
  opacity: 0;
  transition: opacity 0.3s;
}

.card:hover {
  transform: translateY(-0.35rem);
  box-shadow: 0 1rem 2rem rgba(28, 43, 75, 0.15);
}

.card:hover::before { opacity: 1; }

.card-header {
  margin-bottom: 1.5rem;
  text-align: center;
  display: flex;
  flex-direction: column; /* Empilha Título e Badge */
  align-items: center;
  gap: 0.75rem; /* Espaço entre Título e Badge */
}

h3 {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 700;
  color: #1C2B4B;
  line-height: 1.4;
  overflow-wrap: break-word; 
  word-wrap: break-word;
}

.badge {
  background-color: #F1F5F9;
  color: #475569;
  padding: 0.25rem 0.75rem;
  border-radius: 1.25rem;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.05rem;
  text-transform: uppercase;
  text-align: center;
  display: inline-block;
}

.card-body {
  border-top: 0.0625rem solid #F0F2F5;
  padding-top: 1rem;
  flex-grow: 1; 
}

.info-row {
  display: flex;
  align-items: baseline;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.label {
  color: #7A869A;
  font-weight: 600;
  flex-shrink: 0;
}

.value {
  font-weight: 500;
  color: #42526E;
  word-break: break-word;
}

.clickable {
  cursor: pointer;
  position: relative;
  transition: all 0.2s;
}
.clickable:hover {
  background-color: #e2e8f0;
  color: #1C2B4B;
}

.copy-feedback {
  position: absolute;
  top: -1.8rem;
  left: 50%;
  transform: translateX(-50%);
  background: #1C2B4B;
  color: white;
  font-size: 0.7rem;
  padding: 2px 6px;
  border-radius: 4px;
  animation: fadeIn 0.3s;
  pointer-events: none;
  white-space: nowrap;
}
@keyframes fadeIn { from { opacity: 0; top: -1rem; } to { opacity: 1; top: -1.8rem; } }

.cnpj {
  font-family: 'Consolas', monospace;
  background: #F4F5F7;
  padding: 0.125rem 0.375rem;
  border-radius: 0.25rem;
  color: #1C2B4B;
  display: inline-block;
}

.contact-info {
  margin-top: 1rem;
  padding-top: 0.75rem;
  border-top: 0.0625rem dashed #E0E4E8;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.375rem;
  color: #42526E;
  font-size: 0.9rem;
}

.location {
  margin-top: 0.75rem;
  font-size: 0.85rem;
  color: #7A869A;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

/* CORES BADGES */
.badge-odonto { background-color: #E3F2FD !important; color: #1565C0 !important; } 
.badge-medica { background-color: #E8F5E9 !important; color: #2E7D32 !important; } 
.badge-admin { background-color: #F3E5F5 !important; color: #7B1FA2 !important; }
.badge-seguradora { background-color: #FFF3E0 !important; color: #E65100 !important; }
.badge-filantropia { background-color: #FCE4EC !important; color: #880E4F !important; }
.badge-default { background-color: #F1F5F9 !important; color: #64748B !important; }

@media (max-width: 40rem) {
  .card { padding: 1rem; }
}
</style>