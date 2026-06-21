import csv
import re

input_file = 'Prospection_Segmentee_Affinée.csv'
output_file = 'CRM_Prospection_Affinée.html'

def get_stars_html(classement):
    if "5" in classement: return "⭐⭐⭐⭐⭐"
    if "4" in classement: return "⭐⭐⭐⭐"
    if "3" in classement: return "⭐⭐⭐"
    return "⭐⭐"

def get_status_color(statut):
    colors = {
        'NRP': '#6c757d',
        'REFUS CATÉGORIQUE': '#dc3545',
        'REFUS ARGUMENTÉ': '#ffc107',
        'SUIVI NÉGO': '#28a745',
        'À CONTACTER': '#17a2b8'
    }
    return colors.get(statut, '#D4AF37')

cards_html = ""
departments = set()

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)
    for row in data:
        cp_match = re.search(r'(\d{2})\d{3}', row['Code_postal_et_commune'])
        dept = cp_match.group(1) if cp_match else "Unknown"
        departments.add(dept)
        
        type_client = row['Type_Client']
        type_color = "#28a745" if type_client == "PROFESSIONNEL" else "#fd7e14"
        
        statut = row['Statut_Prospection']
        statut_color = get_status_color(statut)
        commentaire = row['Dernier_Commentaire']
        
        stars = get_stars_html(row['Classements_du_POI'])
        phone = row['Telephone_Final']
        
        cards_html += f"""
        <div class="card" data-dept="{dept}" data-type="{type_client}" style="border-left: 5px solid {statut_color};">
            <div class="badge-type" style="background: {type_color};">{type_client}</div>
            <div class="card-title">{row['Nom_du_POI']}</div>
            <div class="stars">{stars} <span style="font-size:0.7rem; opacity:0.5;">(Dept: {dept})</span></div>
            <div class="card-content">
                <p><strong>📍 Ville :</strong> {row['Code_postal_et_commune']}</p>
                <p style="font-size: 1.1rem; color: #D4AF37; margin: 5px 0;"><strong>📞 {phone}</strong></p>
                <div style="background: rgba(0,0,0,0.2); padding: 8px; border-radius: 4px; margin-top: 10px; font-size: 0.75rem;">
                    <strong style="color: {statut_color};">● {statut} :</strong><br>
                    {commentaire}
                </div>
            </div>
            <div style="margin-top:15px;">
                <a href="tel:{phone.replace(' ', '')}" class="btn-prestige">Appeler</a>
            </div>
        </div>
        """

sorted_depts = sorted(list(departments))
dept_options = "".join([f'<option value="{d}">Dept {d}</option>' for d in sorted_depts])

html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRM Prospection Affinée - 300 Leads</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0F1115;
            --accent: #D4AF37;
            --text: #F4F4F4;
            --card-bg: #1A1E26;
            --radius: 8px;
        }}

        body {{ font-family: 'Montserrat', sans-serif; background-color: var(--bg); color: var(--text); margin: 0; padding: 20px; }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        header {{ border-bottom: 2px solid var(--accent); padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; }}
        h1 {{ font-family: 'Cinzel'; color: var(--accent); font-size: 1.6rem; margin: 0; }}
        
        .filters {{ display: flex; gap: 15px; }}
        .filter-box {{ background: var(--card-bg); border: 1px solid var(--accent); color: white; padding: 10px; border-radius: 4px; font-family: 'Montserrat'; cursor: pointer; }}

        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
        
        .card {{ 
            background: var(--card-bg); 
            border: 1px solid rgba(212, 175, 55, 0.2); 
            padding: 20px; 
            border-radius: var(--radius); 
            transition: 0.3s;
            position: relative;
        }}
        .card:hover {{ border-color: var(--accent); transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0,0,0,0.5); }}
        
        .badge-type {{ position: absolute; top: -10px; right: 10px; font-size: 0.6rem; font-weight: bold; padding: 3px 12px; border-radius: 10px; color: white; box-shadow: 0 2px 5px rgba(0,0,0,0.3); }}

        .card-title {{ font-family: 'Cinzel'; color: var(--accent); font-size: 0.95rem; height: 2.5rem; overflow: hidden; padding-right: 50px; }}
        .stars {{ color: var(--accent); margin: 10px 0; }}
        
        .btn-prestige {{
            display: block; width: 100%; padding: 12px; text-align: center; background: var(--accent);
            color: var(--bg); text-decoration: none; font-family: 'Cinzel'; font-size: 0.8rem;
            font-weight: bold; border-radius: 4px; transition: 0.3s;
        }}
        .btn-prestige:hover {{ filter: brightness(1.2); box-shadow: 0 0 10px var(--accent); }}
        
        .hidden {{ display: none !important; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div>
                <h1>CRM : STRATÉGIE DE PROSPECTION AFFINÉE</h1>
                <p style="opacity: 0.6; margin-top: 5px;">Modélisation des freins : NRP (Particuliers) & Barrages (Pros Grand Est)</p>
            </div>
            <div class="filters">
                <select id="typeFilter" class="filter-box" onchange="applyFilters()">
                    <option value="all">Tous les types</option>
                    <option value="PROFESSIONNEL">Professionnels uniquement</option>
                    <option value="PARTICULIER">Particuliers uniquement</option>
                </select>
                <select id="deptFilter" class="filter-box" onchange="applyFilters()">
                    <option value="all">Tous départements</option>
                    {dept_options}
                </select>
            </div>
        </header>

        <div class="grid" id="leadsGrid">
            {cards_html}
        </div>
    </div>

    <script>
        function applyFilters() {{
            const selectedType = document.getElementById('typeFilter').value;
            const selectedDept = document.getElementById('deptFilter').value;
            const cards = document.querySelectorAll('.card');
            
            cards.forEach(card => {{
                const cardType = card.getAttribute('data-type');
                const cardDept = card.getAttribute('data-dept');
                
                const typeMatch = (selectedType === 'all' || cardType === selectedType);
                const deptMatch = (selectedDept === 'all' || cardDept === selectedDept);
                
                if (typeMatch && deptMatch) {{
                    card.classList.remove('hidden');
                }} else {{
                    card.classList.add('hidden');
                }}
            }});
        }}
    </script>
</body>
</html>
"""

with open(output_file, mode='w', encoding='utf-8') as f:
    f.write(html_template)

print(f"CRM Téléphonique généré : {output_file}")
