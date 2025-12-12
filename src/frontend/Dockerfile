FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --prefer-offline --no-audit --progress=false
COPY . .
RUN npm run build
CMD ["npm", "run", "preview"]
