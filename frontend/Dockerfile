# Imagen base
FROM node:20

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias primero (cache-friendly)
COPY package.json package-lock.json* ./

# Instalar dependencias de Node
RUN npm install

# Copiar el resto de la app
COPY . .

# Comando por defecto: iniciar el servidor de desarrollo Vite
CMD ["npm", "run", "dev", "--", "--host"]
