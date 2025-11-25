# Usa uma imagem leve do Node.js
FROM node:22-alpine

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia o restante do código
COPY . .

# Expõe a porta do Vite
EXPOSE 5173

# Roda o servidor de desenvolvimento
# --host é necessário para liberar o acesso externo ao container
CMD ["npm", "run", "dev", "--", "--host"]