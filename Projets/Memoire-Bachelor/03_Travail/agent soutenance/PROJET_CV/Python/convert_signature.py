import os
import sys
from PIL import Image

def convert_signature_to_gold(input_path, output_path, gold_color=(212, 175, 55)):
    """
    Isole une signature manuscrite noire sur fond blanc,
    la colore en or (#D4AF37) et la rend transparente (PNG).
    """
    if not os.path.exists(input_path):
        print(f"Erreur : L'image source {input_path} n'existe pas.")
        return False
        
    try:
        # Ouvrir la signature d'origine
        img = Image.open(input_path).convert("L")  # Conversion en niveaux de gris
        
        # Créer une image RGBA transparente
        gold_img = Image.new("RGBA", img.size)
        
        # Récupérer les données des pixels
        pixels = img.load()
        gold_pixels = gold_img.load()
        
        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                gray = pixels[x, y]
                # Plus la valeur est proche de 0 (noir), plus le tracé est fort.
                # Seuil à 220 pour nettoyer les impuretés du fond blanc
                if gray < 220:
                    # Rendre l'opacité proportionnelle au tracé d'origine
                    alpha = 255 - gray
                    # Coloration en or avec l'opacité calculée
                    gold_pixels[x, y] = (gold_color[0], gold_color[1], gold_color[2], alpha)
                else:
                    gold_pixels[x, y] = (0, 0, 0, 0) # Fond transparent
                    
        # Sauvegarder en PNG
        gold_img.save(output_path, "PNG")
        print(f"[OK] Signature en or générée : {output_path}")
        return True
    except Exception as e:
        print(f"[X] Une erreur est survenue lors de la conversion : {str(e)}")
        return False

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    # On teste les différentes sources de signatures possibles
    input_file = os.path.normpath(os.path.join(base_path, "..", "signature julien V2.jpg"))
    if not os.path.exists(input_file):
        input_file = os.path.normpath(os.path.join(base_path, "..", "signature julien.jpeg"))
        
    output_file = os.path.normpath(os.path.join(base_path, "..", "signature_or.png"))
    
    convert_signature_to_gold(input_file, output_file)
