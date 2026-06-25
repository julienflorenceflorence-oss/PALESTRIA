import csv
import re
import urllib.request
import urllib.error
import ssl
import concurrent.futures

input_csv = 'Fichier_Prospection_Unifie.csv'
output_csv = 'Fichier_Prospection_Unifie.csv'
output_html = 'CRM_Prospection_Standard.html'

def fetch_email_from_website(url):
    try:
        # Ignore SSL errors for scraping
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=5, context=ctx) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Priorité aux liens mailto:
            emails = re.findall(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', html)
            if emails:
                return emails[0]
                
            # Fallback sur une regex générale d'email
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)
            
            # Filtrer les faux positifs (extensions d'images, domaines génériques, etc.)
            invalid_endings = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.css', '.js')
            invalid_domains = ['w3.org', 'sentry.io', 'example.com', 'schema.org']
            
            valid_emails = []
            for e in emails:
                e_lower = e.lower()
                if not e_lower.endswith(invalid_endings) and not any(domain in e_lower for domain in invalid_domains):
                    valid_emails.append(e)
                    
            if valid_emails:
                return valid_emails[0]
    except Exception:
        pass
    return ""

def process_row(row):
    if row.get('Site_Web') and not row.get('Email'):
        email = fetch_email_from_website(row['Site_Web'])
        if email:
            row['Email'] = email
            print(f"Trouvé : {email} sur {row['Site_Web']}")
    return row

if __name__ == '__main__':
    leads = []
    with open(input_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        leads = list(reader)

    missing_emails_count = len([r for r in leads if r.get('Site_Web') and not r.get('Email')])
    print(f"Scraping de {missing_emails_count} sites web pour trouver des e-mails manquants...")

    # Scraping multithreadé pour aller vite
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        updated_leads = list(executor.map(process_row, leads))

    # Sauvegarde CSV
    with open(output_csv, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=updated_leads[0].keys())
        writer.writeheader()
        writer.writerows(updated_leads)

    # Regénération HTML
    cards_html = ""
    for r in updated_leads:
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

    new_emails_count = len([r for r in updated_leads if r.get('Email')]) - (len(leads) - missing_emails_count)
    print(f"Scraping terminé. {new_emails_count} nouveaux e-mails ajoutés avec succès.")
