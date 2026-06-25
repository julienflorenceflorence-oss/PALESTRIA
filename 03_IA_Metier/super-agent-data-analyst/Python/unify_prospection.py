import csv
import re

input_file = 'Prospection_Segmentee_Affinée.csv'
output_csv = 'Fichier_Prospection_Unifie.csv'
output_html = 'CRM_Prospection_Standard.html'

results = []

# Lecture et préparation des données unifiées
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # On ne garde que les colonnes utiles pour un fichier classique
        unified_row = {
            'Nom_Etablissement': row['Nom_du_POI'],
            'Telephone': row['Telephone_Final'],
            'Localisation': row['Code_postal_et_commune'],
            'Classement': row['Classements_du_POI'],
            'Statut_Appel': row['Statut_Prospection'],
            'Commentaire_Terrain': row['Dernier_Commentaire']
        }
        results.append(unified_row)

# Sauvegarde en CSV Classique
with open(output_csv, mode='w', encoding='utf-8', newline='') as f:
    fieldnames = ['Nom_Etablissement', 'Telephone', 'Localisation', 'Classement', 'Statut_Appel', 'Commentaire_Terrain']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# Génération du CRM Visuel Standard (sans filtres pro/part)
cards_html = ""
for r in results:
    statut = r['Statut_Appel']
    # Couleurs de statut standard
    color = "#6c757d" if statut == "NRP" else "#dc3545" if "REFUS" in statut else "#28a745" if "NÉGO" in statut else "#D4AF37"
    
    cards_html += f"""
    <div class="card">
        <div class="card-title">{r['Nom_Etablissement']}</div>
        <div class="card-content">
            <p><strong>📍 {r['Localisation']}</strong></p>
            <p style="font-size: 1.2rem; color: #D4AF37; margin: 10px 0;"><strong>📞 {r['Telephone']}</strong></p>
            <p style="font-size: 0.8rem; opacity: 0.7;">{r['Classement']}</p>
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 4px; margin-top: 10px; font-size: 0.75rem; border-left: 3px solid {color};">
                <strong>{statut} :</strong> {r['Commentaire_Terrain']}
            </div>
        </div>
        <div style="margin-top:15px;">
            <a href="tel:{r['Telephone'].replace(' ', '')}" class="btn-call">Appeler</a>
        </div>
    </div>
    """

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Fichier de Prospection</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Montserrat', sans-serif; background: #0F1115; color: #F4F4F4; margin: 0; padding: 20px; }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        header {{ border-bottom: 1px solid #D4AF37; padding-bottom: 20px; margin-bottom: 30px; }}
        h1 {{ color: #D4AF37; font-size: 1.5rem; margin: 0; text-transform: uppercase; letter-spacing: 2px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
        .card {{ background: #1A1E26; border: 1px solid rgba(212, 175, 55, 0.1); padding: 20px; border-radius: 6px; transition: 0.2s; }}
        .card:hover {{ border-color: #D4AF37; }}
        .card-title {{ font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; color: #fff; height: 2.5rem; overflow: hidden; }}
        .btn-call {{ display: block; width: 100%; padding: 10px; text-align: center; background: #D4AF37; color: #0F1115; text-decoration: none; font-weight: bold; font-size: 0.8rem; border-radius: 4px; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Fichier de Prospection - 300 Leads</h1>
        </header>
        <div class="grid">
            {cards_html}
        </div>
    </div>
</body>
</html>
"""

with open(output_html, mode='w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Fichiers unifiés générés : {output_csv} et {output_html}")
