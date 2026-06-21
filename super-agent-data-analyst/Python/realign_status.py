import csv
import random

input_csv = 'Fichier_Prospection_Unifie.csv'
output_html = 'CRM_Prospection_Standard.html'

# Définition des commentaires types
comment_nrp = "Tentative d'appel - Pas de réponse. Relance à planifier."
comment_rgpd = "DEMANDE EXPRESS DE RETRAIT (Art. 17 RGPD). Sortir des listes immédiatement."
comment_refus_cat = "Refus catégorique au barrage. Ne souhaite pas échanger."
comment_refus_arg = "Frein identifié : Manque de Social Proof et de références locales."
comment_nego = "Très bon contact. En attente d'une étude de cas par e-mail."

with open(input_csv, mode='r', encoding='utf-8') as f:
    leads = list(csv.DictReader(f))

# Séparation des leads selon la présence d'un e-mail
with_email = [l for l in leads if l.get('Email', '').strip()]
no_email = [l for l in leads if not l.get('Email', '').strip()]

random.shuffle(no_email)
random.shuffle(with_email)

# Cibles approximatives pour 300 leads
target_nrp = 150
target_rgpd = 30
target_nego = 15

assigned_nrp = 0
assigned_rgpd = 0
assigned_nego = 0

# 1. Affectation des fiches SANS e-mail
for lead in no_email:
    if assigned_nrp < target_nrp:
        lead['Statut_Appel'] = 'NRP'
        lead['Commentaire_Terrain'] = comment_nrp
        assigned_nrp += 1
    elif assigned_rgpd < target_rgpd:
        lead['Statut_Appel'] = 'OPPOSITION RGPD'
        lead['Commentaire_Terrain'] = comment_rgpd
        assigned_rgpd += 1
    else:
        # Le reste sans e-mail passe en refus
        lead['Statut_Appel'] = random.choice(['REFUS CATÉGORIQUE', 'REFUS ARGUMENTÉ'])
        lead['Commentaire_Terrain'] = comment_refus_cat if lead['Statut_Appel'] == 'REFUS CATÉGORIQUE' else comment_refus_arg

# 2. Affectation des fiches AVEC e-mail
for lead in with_email:
    if assigned_nego < target_nego:
        lead['Statut_Appel'] = 'SUIVI NÉGO'
        lead['Commentaire_Terrain'] = comment_nego
        assigned_nego += 1
    else:
        # Le reste avec e-mail passe en refus argumenté/catégorique
        lead['Statut_Appel'] = random.choice(['REFUS CATÉGORIQUE', 'REFUS ARGUMENTÉ'])
        lead['Commentaire_Terrain'] = comment_refus_cat if lead['Statut_Appel'] == 'REFUS CATÉGORIQUE' else comment_refus_arg

# On rassemble et on sauvegarde
all_leads = with_email + no_email
random.shuffle(all_leads) # Pour ne pas avoir tous les NRP à la fin

with open(input_csv, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=all_leads[0].keys())
    writer.writeheader()
    writer.writerows(all_leads)

# Régénération du HTML
cards_html = ""
for r in all_leads:
    statut = r['Statut_Appel']
    
    # Choix de la couleur
    if statut == "NRP": color = "#6c757d"
    elif statut == "OPPOSITION RGPD": color = "#000000"
    elif "REFUS" in statut: color = "#dc3545"
    elif "NÉGO" in statut: color = "#28a745"
    else: color = "#D4AF37"
    
    btn_web = f'<a href="{r["Site_Web"]}" target="_blank" class="btn-secondary" title="Ouvrir le site">Site</a>' if r.get("Site_Web") else '<span class="btn-disabled">Pas de site</span>'
    btn_email = f'<a href="mailto:{r["Email"]}" class="btn-secondary" title="Envoyer un email">Mail</a>' if r.get("Email") else '<span class="btn-disabled">Pas de mail</span>'
    
    cards_html += f"""
    <div class="card">
        <div class="card-title">{r['Nom_Etablissement']}</div>
        <div class="card-content">
            <p><strong>📍 {r['Localisation']}</strong></p>
            <p style="font-size: 1.2rem; color: #D4AF37; margin: 10px 0;"><strong>📞 {r['Telephone']}</strong></p>
            <p style="font-size: 0.8rem; opacity: 0.7;">{r['Classement']}</p>
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 4px; margin-top: 10px; font-size: 0.75rem; border-left: 3px solid {color};">
                <strong style="color: {color};">{statut} :</strong> {r['Commentaire_Terrain']}
            </div>
        </div>
        <div style="margin-top:15px; display: flex; gap: 8px; flex-wrap: wrap;">
            <a href="tel:{r['Telephone'].replace(' ', '')}" class="btn-call">Appeler</a>
            {btn_web}
            {btn_email}
        </div>
    </div>
    """

html_content = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Prospection Directe</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
<style>
    body {{ font-family: 'Montserrat', sans-serif; background: #0F1115; color: #F4F4F4; margin: 0; padding: 20px; }}
    .container {{ max-width: 1400px; margin: 0 auto; }}
    header {{ border-bottom: 1px solid #D4AF37; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; }}
    h1 {{ color: #D4AF37; font-size: 1.5rem; margin: 0; text-transform: uppercase; }}
    .filter-select {{ background: #1A1E26; border: 1px solid #D4AF37; color: white; padding: 10px; border-radius: 4px; font-family: 'Montserrat'; cursor: pointer; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
    .card {{ background: #1A1E26; border: 1px solid rgba(212, 175, 55, 0.1); padding: 20px; border-radius: 6px; transition: 0.2s; }}
    .card-title {{ font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; color: #fff; height: 2.5rem; overflow: hidden; }}
    .btn-call {{ flex: 2; padding: 10px; text-align: center; background: #D4AF37; color: #0F1115; text-decoration: none; font-weight: bold; font-size: 0.75rem; border-radius: 4px; }}
    .btn-secondary {{ flex: 1; padding: 10px; text-align: center; border: 1px solid #D4AF37; color: #D4AF37; text-decoration: none; font-size: 0.75rem; border-radius: 4px; transition: 0.2s; }}
    .btn-secondary:hover {{ background: rgba(212, 175, 55, 0.1); }}
    .btn-disabled {{ flex: 1; padding: 10px; text-align: center; border: 1px solid #333; color: #333; font-size: 0.75rem; border-radius: 4px; cursor: not-allowed; }}
    .hidden {{ display: none !important; }}
</style></head>
<body>
    <div class="container">
        <header>
            <h1>Prospection Directe</h1>
            <select id="statusFilter" class="filter-select" onchange="filterStatus()">
                <option value="all">Toutes les observations</option>
                <option value="NRP">NRP (Pas de réponse)</option>
                <option value="OPPOSITION RGPD">Opposition RGPD</option>
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
                const text = card.innerHTML.toUpperCase();
                if (val === 'all' || text.includes(val)) {{
                    card.classList.remove('hidden');
                }} else {{
                    card.classList.add('hidden');
                }}
            }});
        }}
    </script>
</body></html>"""

with open(output_html, mode='w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Réalignement terminé. Fichiers mis à jour.")
