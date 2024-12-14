from flask import Flask, request, render_template, url_for
from PIL import Image
import os

app = Flask(__name__)

# Répertoire pour stocker les images générées dans static
STATIC_FOLDER = 'static'
os.makedirs(STATIC_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def to_black_and_white():
    if 'image' not in request.files:
        return "Aucune image envoyée.", 400

    file = request.files['image']
    if file.filename == '':
        return "Nom de fichier invalide.", 400

    try:
        # Charger l'image
        image = Image.open(file)

        # Convertir en noir et blanc
        bw_image = image.convert("L")

        # Sauvegarder le fichier transformé dans le répertoire static
        output_path = os.path.join(STATIC_FOLDER, "black_and_white.png")
        bw_image.save(output_path)

        # URL pour afficher l'image transformée
        image_url = url_for('static', filename='black_and_white.png')

        # Retourner la page avec le résultat
        return render_template('index.html', image_url=image_url)

    except Exception as e:
        return f"Erreur lors du traitement : {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
