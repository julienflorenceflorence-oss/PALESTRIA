import csv

input_file = 'Gites_Prospection_Simulee.csv'
output_file = 'CRM_Prospection_Prestige.html'

def get_stars(classement):
    if "5" in classement: return "⭐⭐⭐⭐⭐"
    if "4" in classement: return "⭐⭐⭐⭐"
    return "⭐⭐⭐"

def get_status_color(statut):
    colors = {
        'NRP': '#6c757d',
        'REFUS CATÉGORIQUE': '#dc3545',
        'OPPOSITION RGPD': '#000000',
        'REFUS ARGUMENTÉ': '#ffc107',
        'SUIVI NÉGO': '#28a745',
        'À CONTACTER': '#17a2b8'
    }
    return colors.get(statut, '#accent')

cards_html = ""

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stars = get_stars(row['Classements_du_POI'])
        statut = row['Statut_Prospection']
        statut_color = get_status_color(statut)
        phone = row['Telephones'] if row['Telephones'] else "Non renseigné"
        website = row['Site_Web_Officiel']
        commentaire = row['Dernier_Commentaire']
        confiance = row['Niveau_Confiance']
        
        btn_web = f'<a href="{website}" target="_blank" class="btn-prestige">Site Officiel</a>' if website else '<span class="btn-prestige" style="opacity:0.3;">Pas de site</span>'
        
        cards_html += f"""
        <div class="card" style="border-left: 4px solid {statut_color};">
            <div class="badge" style="border-color: {statut_color}; color: {statut_color};">{statut}</div>
            <div class="card-title">{row['Nom_du_POI']}</div>
            <div class="stars">{stars} <span style="font-size: 0.7rem; color: var(--text-dim); margin-left:10px;">Confiance: {confiance}</span></div>
            <div class="card-content">
                <p><strong>📍 Ville :</strong> {row['Code_postal_et_commune']}</p>
                <p><strong>📞 Tél :</strong> {phone}</p>
                <div class="comment-box">
                    <strong>💬 Dernier Retour :</strong><br>
                    {commentaire}
                </div>
            </div>
            <div style="display:flex; gap:8px; margin-top:15px;">
                {btn_web}
                <a href="tel:{phone.replace(' ', '')}" class="btn-prestige" style="opacity: 0.8;">Action</a>
            </div>
        </div>
        """

html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRM Gîtes de Prestige - Grand Est</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0F1115;
            --accent: #D4AF37;
            --text: #F4F4F4;
            --text-dim: #B0B0B0;
            --card-bg: #1A1E26;
            --radius: 8px;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Montserrat', sans-serif; background-color: var(--bg); color: var(--text); line-height: 1.6; }}

        .crm-container {{ max-width: 1400px; margin: 0 auto; padding: 40px 20px; }}
        
        header {{ margin-bottom: 40px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 20px; display: flex; justify-content: space-between; align-items: center; }}
        h1 {{ font-family: 'Cinzel'; color: var(--accent); font-size: 1.8rem; letter-spacing: 3px; }}
        .crm-stats {{ display: flex; gap: 30px; }}
        .stat-item {{ text-align: center; }}
        .stat-val {{ display: block; font-family: 'Cinzel'; color: var(--accent); font-size: 1.5rem; }}
        .stat-lbl {{ font-size: 0.7rem; text-transform: uppercase; opacity: 0.6; }}

        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 25px; }}
        
        .card {{ 
            background: var(--card-bg); 
            border: 1px solid rgba(212, 175, 55, 0.1); 
            padding: 25px; 
            border-radius: var(--radius); 
            transition: 0.3s;
            position: relative;
        }}
        .card:hover {{ border-color: var(--accent); box-shadow: 0 5px 20px rgba(0,0,0,0.6); }}
        
        .badge {{ position: absolute; top: 15px; right: 15px; font-size: 0.6rem; padding: 4px 10px; border: 1px solid var(--accent); color: var(--accent); border-radius: 20px; font-family: 'Cinzel'; }}
        
        .card-title {{ font-family: 'Cinzel'; color: var(--accent); font-size: 1.1rem; margin-bottom: 5px; padding-right: 70px; min-height: 2.4rem; }}
        .stars {{ color: var(--accent); margin-bottom: 15px; font-size: 0.9rem; }}
        .card-content {{ font-size: 0.85rem; color: var(--text-dim); }}
        .card-content p {{ margin-bottom: 5px; }}
        .comment-box {{ background: rgba(0,0,0,0.2); padding: 10px; border-radius: 4px; margin-top: 10px; border-left: 2px solid var(--accent); font-size: 0.75rem; color: #fff; }}

        .btn-prestige {{
            display: inline-block; flex: 1; padding: 10px; text-align: center; border: 1px solid var(--accent);
            color: var(--accent); text-decoration: none; font-family: 'Cinzel'; font-size: 0.7rem;
            text-transform: uppercase; letter-spacing: 1px; border-radius: 4px; transition: 0.3s;
        }}
        .btn-prestige:hover {{ background: var(--accent); color: var(--bg); font-weight: bold; }}

        .search-bar {{ width: 100%; padding: 15px; background: #161a23; border: 1px solid rgba(212, 175, 55, 0.2); border-radius: var(--radius); color: white; margin-bottom: 30px; font-family: 'Montserrat'; }}
    </style>
</head>
<body>
    <div class="crm-container">
        <header>
            <div>
                <h1>CRM PRESTIGE : Gîtes Grand Est</h1>
                <p style="font-size: 0.8rem; opacity: 0.6;">Base de données qualifiée - 300 Entrées</p>
            </div>
            <div class="crm-stats">
                <div class="stat-item"><span class="stat-val">300</span><span class="stat-lbl">Leads</span></div>
                <div class="stat-item"><span class="stat-val">110</span><span class="stat-lbl">Top 5*</span></div>
                <div class="stat-item"><span class="stat-val">192</span><span class="stat-lbl">Web Qualifié</span></div>
            </div>
        </header>

        <input type="text" class="search-bar" placeholder="Rechercher un gîte, une ville ou un département...">

        <div class="grid">
            {cards_html}
        </div>
    </div>
</body>
</html>
"""

with open(output_file, mode='w', encoding='utf-8') as f:
    f.write(html_template)

print(f"CRM Dashboard généré : {output_file}")
