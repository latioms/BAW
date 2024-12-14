# Utilisation de l'image officielle de Python
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement le fichier requirements.txt pour une meilleure mise en cache Docker
COPY requirements.txt requirements.txt

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Exposer le port utilisé par Flask
EXPOSE 5000

# Commande pour démarrer l'application (mode production)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]