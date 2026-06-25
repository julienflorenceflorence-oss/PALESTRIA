import csv

input_csv = 'Fichier_Prospection_Unifie.csv'
output_html = 'Tableau_Prospection_Prestige.html'

table_rows = ""

with open(input_csv, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        statut = row['Statut_Appel']
        color = "#6c757d" if statut == "NRP" else "#000000" if "RGPD" in statut else "#dc3545" if "REFUS" in statut else "#28a745" if "NÉGO" in statut else "#D4AF37"
        
        email_display = f'<a href="mailto:{row["Email"]}" style="color:#D4AF37; text-decoration:none;">{row["Email"]}</a>' if row["Email"] else '<span style="opacity:0.3;">-</span>'
        web_display = f'<a href="{row["Site_Web"]}" target="_blank" style="color:#D4AF37; text-decoration:none;">Lien</a>' if row["Site_Web"] else '<span style="opacity:0.3;">-</span>'
        
        table_rows += f"""
        <tr>
            <td><strong>{row['Nom_Etablissement']}</strong></td>
            <td>{row['Localisation']}</td>
            <td style="color:#D4AF37; font-weight:bold;">{row['Telephone']}</td>
            <td>{email_display}</td>
            <td>{web_display}</td>
            <td><span class="badge" style="background:{color};">{statut}</span></td>
            <td style="font-size: 0.85rem; opacity:0.8;">{row['Commentaire_Terrain']}</td>
        </tr>
        """

html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tableau de Prospection - Édition Prestige</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&family=Cinzel:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Montserrat', sans-serif;
            background-color: #0F1115;
            color: #F4F4F4;
            margin: 0;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 1500px;
            margin: 0 auto;
            background: #1A1E26;
            border: 1px solid rgba(212, 175, 55, 0.3);
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        h1 {{
            font-family: 'Cinzel', serif;
            color: #D4AF37;
            text-align: center;
            letter-spacing: 3px;
            margin-top: 0;
            border-bottom: 1px solid rgba(212, 175, 55, 0.2);
            padding-bottom: 20px;
        }}
        .table-wrapper {{
            overflow-x: auto;
            margin-top: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}
        th {{
            font-family: 'Cinzel', serif;
            color: #D4AF37;
            padding: 15px;
            border-bottom: 2px solid #D4AF37;
            background: rgba(212, 175, 55, 0.05);
            text-transform: uppercase;
            font-size: 0.9rem;
        }}
        td {{
            padding: 15px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            vertical-align: middle;
        }}
        tr:hover {{
            background: rgba(212, 175, 55, 0.05);
        }}
        .badge {{
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
            color: #fff;
            white-space: nowrap;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Bilan de Prospection Qualifiée</h1>
        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th>Établissement</th>
                        <th>Localisation</th>
                        <th>Téléphone</th>
                        <th>E-mail</th>
                        <th>Site Web</th>
                        <th>Statut</th>
                        <th>Commentaire / Observation</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""

with open(output_html, mode='w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Tableau généré : {output_html}")
