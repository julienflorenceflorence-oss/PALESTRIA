import os
from pypdf import PdfReader, PdfWriter

folder_path = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-startup\vins\PDF analyse marchet du vin en france"

files_to_clean = [
    "Observatoire National de la Viticulture 2026.pdf",
    "Rapport de Précision Viticole 2026.pdf",
    "Synthèse Stratégique Viticole 2026.pdf"
]

def clean_pdf_borders():
    for filename in files_to_clean:
        full_path = os.path.join(folder_path, filename)
        if not os.path.exists(full_path):
            print(f"Fichier non trouvé : {full_path}")
            continue
            
        reader = PdfReader(full_path)
        writer = PdfWriter()
        
        for page in reader.pages:
            # Récupère les dimensions de la page
            lower_left = page.cropbox.lower_left
            upper_right = page.cropbox.upper_right
            
            # Recadre ~40-50 points en bas (supprime l'URL / chemin et numéro de page)
            # Recadre ~40-50 points en haut (supprime la date et le titre d'en-tête)
            new_lower_left = (lower_left[0], lower_left[1] + 45)
            new_upper_right = (upper_right[0], upper_right[1] - 45)
            
            page.cropbox.lower_left = new_lower_left
            page.cropbox.upper_right = new_upper_right
            
            writer.add_page(page)
            
        # Nom du nouveau fichier propre
        new_filename = filename.replace(".pdf", " - SansBordures.pdf")
        new_full_path = os.path.join(folder_path, new_filename)
        with open(new_full_path, "wb") as f:
            writer.write(f)
            
        print(f"✅ Nettoyé avec succès : '{new_filename}'")

if __name__ == "__main__":
    clean_pdf_borders()
