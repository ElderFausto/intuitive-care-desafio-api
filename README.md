# 🏥 Intuitive Care - Desafio API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-High_Performance-009688?style=for-the-badge&logo=fastapi)
![Vue.js](https://img.shields.io/badge/Vue.js-3.0-4FC08D?style=for-the-badge&logo=vue.js)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)

> Desafio API para busca inteligente de operadoras de planos de saúde ativas na ANS.

---

## 📸 Preview
<img width="998" height="753" alt="image" src="https://github.com/user-attachments/assets/1131522a-bfb9-439c-8192-4471db10f0ce" />
<img width="998" height="753" alt="image" src="https://github.com/user-attachments/assets/c1118b04-0d23-498e-b92e-89b201e4454d" />
<img width="998" height="753" alt="image" src="https://github.com/user-attachments/assets/8f8d51b6-266b-4423-bdc1-c2b5be0c17ac" />
<img width="998" height="753" alt="image" src="https://github.com/user-attachments/assets/35ce2b77-5fce-4c3b-b63f-fbd280574477" />
<img width="998" height="753" alt="image" src="https://github.com/user-attachments/assets/9f86a2f5-5664-4de4-b392-5fa922f1a2a5" />
<img width="998" height="753" alt="image" src="https://github.com/user-attachments/assets/bf429a4e-72ff-4eea-8d04-41ee1c579abc" />
<img width="998" height="753" alt="image" src="https://github.com/user-attachments/assets/7bd533b8-de61-4bee-90c1-a6575e945ad2" />




---

## 🚀 Sobre o Projeto

Este projeto foi desenvolvido como parte do teste técnico para a vaga de desenvolvedor na **Intuitive Care**. O objetivo principal era criar uma aplicação Web (Frontend + Backend) capaz de realizar buscas textuais numa base de dados CSV da ANS.

Fui além dos requisitos básicos, focando em **Performance**, **UX (Experiência do Utilizador)**, **Arquitetura Limpa** e **DevOps**.

### ✨ Diferenciais Implementados

* **🔍 Busca Híbrida Inteligente:** O sistema deteta automaticamente a intenção do utilizador.
    * **Números** Busca exata por **CNPJ** (com ou sem pontuação).
    * **Texto** Busca Fuzzy (aproximada) por **Razão Social**, tolerando erros de digitação e correspondência parcial.
    * **Filtro:** Opção de filtrar operadoras por Estado (UF) para refinar os resultados.
* **⚡ Performance Otimizada:**
    * Uso do padrão **Singleton** para carregar o CSV em memória apenas uma vez na inicialização.
    * Utilização da biblioteca **RapidFuzz** (baseada em C++) para processamento de texto ultrarrápido.
    * Implementação de **Debounce** no Frontend para evitar sobrecarga de requisições enquanto o utilizador digita.
* **🎨 UX Refinada:**
    * **Design Responsivo:** Layout fluido que se adapta de 3 colunas (Desktop) para 1 coluna (Mobile).
    * **Interatividade:** Cópia de CNPJ ao clicar e badges coloridas dinamicamente conforme a modalidade.
* **🐳 Cloud Ready:** Aplicação 100% em container com **Docker** e orquestrada via **Docker Compose**.
* **🧪 Qualidade de Código:** Cobertura de testes unitários e de integração no Backend utilizando `pytest`.

---

## 🏗️ Arquitetura e Tecnologias

O projeto segue uma arquitetura de **Monorepo**, separando claramente as responsabilidades entre Cliente (Frontend) e Servidor (Backend).

### 🟢 Backend (API)
* **FastAPI:** Framework moderno, assíncrono e de alta performance. Geração automática de documentação (Swagger/OpenAPI).
* **Pandas:** Leitura e manipulação eficiente de dados tabulares (CSV).
* **RapidFuzz:** Algoritmo `partial_token_sort_ratio` para encontrar a melhor correspondência textual.
* **Pydantic:** Validação rigorosa de dados e schemas de entrada/saída.
* **Pytest:** Framework de testes para garantir a estabilidade da API.

### 🔵 Frontend (SPA)
* **Vue.js 3 (Composition API):** Framework reativo moderno e leve.
* **Vite:** Build tool de última geração para desenvolvimento rápido.
* **Axios:** Cliente HTTP para comunicação com a API.
* **CSS Scoped:** Estilização modular utilizando unidades relativas (`rem`) para acessibilidade e CSS Grid para layouts complexos.

---

## ⚙️ Pré-requisitos

Para rodar este projeto, é necessário ter instalado:

* **Git**
* **Docker** e **Docker Compose** (Altamente Recomendado)

*Caso opte por rodar sem Docker de forma manual:*
* Python 3.10+
* Node.js 18+ ou 20+

---

## 📦 Como Rodar (Docker - Recomendado)

A maneira mais simples e garantida de rodar a aplicação, sem se preocupar com versões de ambiente ou dependências.

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/intuitive-care-desafio-api.git](https://github.com/SEU-USUARIO/intuitive-care-desafio-api.git)
    cd intuitive-care-desafio-api
    ```

2.  **Subir os containers:**
    Este comando irá construir as imagens do Python e Node.js e iniciar os serviços.
    ```bash
    docker compose up --build
    ```

3.  **Acessar à aplicação:**
    * 📱 **Frontend (Aplicação):** [http://localhost:5173](http://localhost:5173)
    * 📄 **Backend (Documentação API):** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔧 Como Rodar (Manual)

Caso prefira rodar os ambientes separadamente de forma local:

### 1. Configurar o Backend

```bash
cd backend

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente (Linux/Mac)
source venv/bin/activate
# Ativar ambiente (Windows)
# .\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
uvicorn app.main:app --reload

O Backend ficará disponível em http://localhost:8000
```

### 2. Configurar o Frontend

```bash

cd frontend

# Instalar dependências
npm install

# Rodar projeto
npm run dev

O Frontend ficará disponível em http://localhost:5173
```

## ✅ Executar os Testes

Para garantir a integridade da aplicação e validar a lógica de busca:

```bash

cd backend
# Certifica-te de que o venv está ativo (se for manual) ou entra no contentor
pytest

Saída esperada: 7 passed (Todos os testes aprovados com sucesso).
```

## 📂 Estrutura de Pastas
<img width="638" height="383" alt="image" src="https://github.com/user-attachments/assets/58269113-a173-48f3-ac15-1b8ad54190e3" />
