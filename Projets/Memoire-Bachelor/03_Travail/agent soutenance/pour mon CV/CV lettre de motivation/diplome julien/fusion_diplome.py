import os
from PIL import Image, ImageDraw

# Chemins des fichiers
cert_path = 'diplome tch/Certificat digital marketing.png'
# On utilise l'image qu'on a déjà générée comme base de cadre si l'originale est perdue
# OU on tente de retrouver le cadre original s'il a été renommé.
frame_path = 'MON_DIPLOME_PRESTIGE.png' 
output_path = 'DIPLOME_GOOGLE_PRESTIGE_FINAL.png'

def main():
    if not os.path.exists(cert_path):
        print(f"Erreur : Le fichier {cert_path} est introuvable.")
        return
    if not os.path.exists(frame_path):
        # Si on ne trouve pas l'image générée, on cherche le fichier cadre original
        print(f"Erreur : Le fichier {frame_path} est introuvable.")
        return

    # 1. Charger les images
    cert = Image.open(cert_path).convert("RGBA")
    # On repart de notre base MON_DIPLOME_PRESTIGE qui contient déjà le cadre bien recadré
    base = Image.open(frame_path).convert("RGBA")
    bw, bh = base.size

    # 2. Détecter la zone d'insertion dans notre base
    # (On cherche le rectangle blanc central)
    gray = base.convert("L")
    # On cherche le blanc
    bw_map = gray.point(lambda x: 255 if x > 240 else 0)
    bbox = bw_map.getbbox()
    
    if not bbox:
        print("Erreur de détection de la zone interne.")
        return

    left, top, right, bottom = bbox
    target_w = right - left
    target_h = bottom - top

    # 3. NETTOYAGE : On vide l'intérieur du cadre
    draw = ImageDraw.Draw(base)
    draw.rectangle([left, top, right, bottom], fill=(255, 255, 255, 255))

    # 4. PRÉPARATION DU DIPLÔME
    cw, ch = cert.size
    # On retire le haut (logos/liens) pour masquer sous le cadre
    # On garde les félicitations (qui sont un peu plus bas)
    cert_useful = cert.crop((0, int(ch*0.09), cw, ch))
    
    # Redimensionnement pour centrage parfait
    # On veut que le texte soit bien lisible, donc on remplit la largeur
    aspect_ratio = cert_useful.size[1] / cert_useful.size[0]
    new_w = target_w
    new_h = int(new_w * aspect_ratio)
    cert_resized = cert_useful.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # 5. ASSEMBLAGE
    # Centrage horizontal parfait
    x_pos = left
    # Centrage vertical avec un petit décalage vers le haut pour cacher le bord
    y_pos = top - 10 
    
    # On colle le diplôme
    base.paste(cert_resized, (x_pos, y_pos), cert_resized)

    # 6. PROTECTION DES BORDS
    # On redessine une bordure blanche très fine pour nettoyer les pixels de bordure
    draw.rectangle([left, top, right, bottom], outline=(255, 255, 255, 255), width=2)

    # Sauvegarde
    base.save(output_path, "PNG", optimize=True)
    print(f"Succès : Le diplôme Google a été inséré proprement.")
    print(f"Fichier : '{output_path}'")

if __name__ == "__main__":
    main()
