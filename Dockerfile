# Étape 1: Construire l'application Angular
FROM node:18 AS build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers package.json et package-lock.json
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers de l'application
COPY . .

# Construire l'application Angular
RUN npm run build --prod

# Étape 2: Déployer avec Nginx
FROM nginx:alpine

# Copier le fichier nginx.conf personnalisé
COPY nginx.conf /etc/nginx/nginx.conf

# Copier les fichiers générés par Angular dans le répertoire Nginx
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html

# Exposer le port 80
EXPOSE 80

# Démarrer Nginx en mode de foreground
CMD ["nginx", "-g", "daemon off;"]
