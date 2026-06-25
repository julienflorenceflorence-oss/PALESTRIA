import csv
import re
import os
import random

data_dir = 'DATAs'
input_file = 'Prospection_Segmentee_Affinée.csv'
output_csv = 'Fichier_Prospection_Unifie.csv'
output_html = 'CRM_Prospection_Standard.html'
target_count = 300

# Pattern pour les téléphones classiques (PAS 08)
phone_pattern = r'(?:(?:\+|00)33|0)\s*[1-79](?:[\s.-]*\d{2}){4}'
# Liste des fichiers régionaux
files = [f for f in os.listdir(data_dir) if f.startswith('datatourisme-reg-') and f.endswith('.csv')]

def extract_clean_phone(text):
    phones = re.findall(phone_pattern, text)
    if not phones: return ""
    p = "".join(filter(str.isdigit, phones[0]))
    if len(p) == 10 and not p.startswith('08'):
        return " ".join([p[i:i+2] for i in range(0, len(p), 2)])
    return ""

def extract_email(text):
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    return emails[0] if emails else ""

def get_simulation_data(row):
    # Logique simplifiée
    rand = random.random()
    if rand < 0.50: return "NRP", "Pas de réponse."
    if rand < 0.70: return "REFUS CATÉGORIQUE", "Refus immédiat."
    if rand < 0.90: return "REFUS ARGUMENTÉ", "Indisponible actuellement / Manque de confiance."
    return "SUIVI NÉGO", "Potentiel détecté."

# Liste d'exclusion pour ne garder que les sites "officiels"
exclude_list = ['airbnb', 'booking', 'tripadvisor', 'abritel', 'facebook', 'instagram', 'reservation', 'clevacances', 'gites-de-france', 'secureholiday', 'elloha']

def extract_website(text):
    urls = re.findall(r'https?://[^\s|#<>]+', text)
    for url in urls:
        clean_url = url.rstrip('/')
        if not any(domain in clean_url.lower() for domain in exclude_list):
            return clean_url
    return ""

final_leads = []
used_names = set()

print("Recherche de nouveaux leads avec sites web, emails et sans numéros 08...")

for file in files:
    if len(final_leads) >= target_count: break
    file_path = os.path.join(data_dir, file)
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('Nom_du_POI', '')
                if name in used_names: continue
                
                categories = row.get('Categories_de_POI', '')
                classement = row.get('Classements_du_POI', '')
                contacts = row.get('Contacts_du_POI', '')
                description = row.get('Description', '')
                
                if "Accommodation" in categories and any(s in classement for s in ["3 étoiles", "4 étoiles", "5 étoiles", "3 épis", "4 épis", "5 épis"]):
                    phone = extract_clean_phone(contacts + " " + description)
                    if phone:
                        statut, comment = get_simulation_data(row)
                        website = extract_website(contacts)
                        email = extract_email(contacts + " " + description)
                        final_leads.append({
                            'Nom_Etablissement': name,
                            'Telephone': phone,
                            'Email': email,
                            'Localisation': row.get('Code_postal_et_commune', ''),
                            'Classement': classement,
                            'Statut_Appel': statut,
                            'Commentaire_Terrain': comment,
                            'Site_Web': website
                        })
                        used_names.add(name)
                        if len(final_leads) >= target_count: break
    except: continue

# Sauvegarde CSV
with open(output_csv, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Nom_Etablissement', 'Telephone', 'Email', 'Localisation', 'Classement', 'Statut_Appel', 'Commentaire_Terrain', 'Site_Web'])
    writer.writeheader()
    writer.writerows(final_leads)

# Génération HTML
cards_html = ""
for r in final_leads:
    statut = r['Statut_Appel']
    color = "#6c757d" if statut == "NRP" else "#dc3545" if "REFUS" in statut else "#28a745" if "NÉGO" in statut else "#D4AF37"
    
    btn_web = f'<a href="{r["Site_Web"]}" target="_blank" class="btn-secondary" title="Ouvrir le site">Site</a>' if r["Site_Web"] else '<span class="btn-disabled">Pas de site</span>'
    btn_email = f'<a href="mailto:{r["Email"]}" class="btn-secondary" title="Envoyer un email">Mail</a>' if r["Email"] else '<span class="btn-disabled">Pas de mail</span>'
    
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
        <div style="margin-top:15px; display: flex; gap: 8px; flex-wrap: wrap;">
            <a href="tel:{r['Telephone'].replace(' ', '')}" class="btn-call">Appeler</a>
            {btn_web}
            {btn_email}
        </div>
    </div>
    """

with open(output_html, mode='w', encoding='utf-8') as f:
    f.write(f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Prospection Directe</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Montserrat', sans-serif; background: #0F1115; color: #F4F4F4; margin: 0; padding: 20px; }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        header {{ border-bottom: 1px solid #D4AF37; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: center; }}
        h1 {{ color: #D4AF37; font-size: 1.5rem; margin: 0; text-transform: uppercase; }}
        .filter-select {{ background: #1A1E26; border: 1px solid #D4AF37; color: white; padding: 10px; border-radius: 4px; font-family: 'Montserrat'; cursor: pointer; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
        .card {{ background: #1A1E26; border: 1px solid rgba(212, 175, 55, 0.1); padding: 20px; border-radius: 6px; transition: 0.2s; }}
        .card-title {{ font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; color: #fff; height: 2.5rem; overflow: hidden; }}
        .btn-call {{ flex: 2; padding: 10px; text-align: center; background: #D4AF37; color: #0F1115; text-decoration: none; font-weight: bold; font-size: 0.75rem; border-radius: 4px; }}
        .btn-secondary {{ flex: 1; padding: 10px; text-align: center; border: 1px solid #D4AF37; color: #D4AF37; text-decoration: none; font-size: 0.75rem; border-radius: 4px; }}
        .btn-disabled {{ flex: 1; padding: 10px; text-align: center; border: 1px solid #333; color: #333; font-size: 0.75rem; border-radius: 4px; }}
        .hidden {{ display: none !important; }}
    </style></head>
    <body>
        <div class="container">
            <header>
                <h1>Prospection Directe</h1>
                <select id="statusFilter" class="filter-select" onchange="filterStatus()">
                    <option value="all">Toutes les observations</option>
                    <option value="NRP">NRP (Pas de réponse)</option>
                    <option value="REFUS">Refus (Catégorique/Argumenté)</option>
                    <option value="NÉGO">Suivi Négo</option>
                </select>
            </header>
            <div class="grid" id="leadsGrid">{cards_html}</div>
        </div>
        <script>
            function filterStatus() {{
                const val = document.getElementById('statusFilter').value;
                const cards = document.querySelectorAll('.card');
                cards.forEach(card => {{
                    const text = card.innerText.toUpperCase();
                    if (val === 'all' || text.includes(val)) {{
                        card.classList.remove('hidden');
                    }} else {{
                        card.classList.add('hidden');
                    }}
                }});
            }}
        </script>
    </body></html>""")

print("Traitement terminé. Emails ajoutés.")
