FROM node:20

WORKDIR /app

# Copiar archivos de dependencias
COPY package.json package-lock.json* ./

# Instalar dependencias
RUN npm install

# Copiar el resto de la aplicación
COPY . .

# Comando para iniciar Vite
CMD ["npm", "run", "dev", "--", "--host"]