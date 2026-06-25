import re
from bs4 import BeautifulSoup

def transform():
    with open('RDM_STRATEGIC_COCKPIT_2026.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. TONE REPLACEMENT
    replacements = {
        "Wahou": "Optimisation",
        "Hégémonie": "Souveraineté numérique",
        "hégémonique": "souverain numérique",
        "génial": "efficient",
        "incroyable": "performant",
        "massif": "industriel",
        "Wahou": "Optimisation",
        "Machine": "Système de Gestion",
    }
    
    # We'll do a simple string replacement in the whole body text later
    # but first let's handle the specific sections.

    # 2. DASHBOARD (Page 2)
    p02 = soup.find('div', id='p02')
    if p02:
        tiles = p02.find_all('div', class_='dashboard-tile')
        for tile in tiles:
            onclick = tile.get('onclick')
            if onclick:
                target = onclick.split("'")[1]
                # Wrap content in <a>
                new_a = soup.new_tag('a', href=target, style="text-decoration:none; color:inherit; display:block;")
                tile.wrap(new_a)
                del tile['onclick']

    # 3. BACK BUTTONS (Footer)
    footers = soup.find_all('div', class_='footer')
    for footer in footers:
        back_btn = footer.find('a', class_='back-btn')
        if back_btn:
            back_btn['href'] = '#p02' # Systematic back to TOC
            back_btn.string = "◈ RETOUR SOMMAIRE"

    # 4. ADD [ANALYSE DU CONSULTANT] on each page
    pages = soup.find_all('div', class_='page')
    for i, page in enumerate(pages):
        content_body = page.find('div', class_='content-body')
        if content_body:
            # Check if it already has a consultant note or similar
            if not content_body.find('div', class_='consultant-analysis'):
                analysis_div = soup.new_tag('div', class_='glass-card', style="border-left: 4px solid var(--gold); margin-top: 20px; font-size: 9pt;")
                analysis_div['class'] = ['consultant-analysis', 'glass-card']
                analysis_title = soup.new_tag('strong')
                analysis_title.string = "[ANALYSE DU CONSULTANT]"
                analysis_div.append(analysis_title)
                
                analysis_text = soup.new_tag('p', style="margin-top: 5px; font-style: italic; opacity: 0.9;")
                
                # Vary text based on page index
                if i < 10:
                    analysis_text.string = "La cohérence entre la vision de prestige et les outils industriels est le point critique. Une déviation de 10% dans l'expérience utilisateur peut entraîner un désengagement total de la cible premium."
                elif i < 20:
                    analysis_text.string = "L'analyse PESTEL confirme une fenêtre d'opportunité étroite. La souveraineté numérique n'est plus un luxe mais une barrière de protection contre l'érosion inéluctable des marges B2C."
                elif i < 30:
                    analysis_text.string = "L'efficience du Système de Gestion repose sur la qualité du sourcing. Un lead mal qualifié en amont détruit le ROI du SDR. La surveillance du scoring AAA est l'indicateur maître de ce module."
                elif i < 40:
                    analysis_text.string = "Le terrain révèle une solitude opérationnelle profonde. Notre posture de 'Consultant Partenaire' est le seul levier capable de briser la résistance culturelle à l'automatisation."
                elif i < 50:
                    analysis_text.string = "Le passage au NFC doit être traité comme un déploiement de mobilier de luxe, pas comme une installation informatique. L'esthétique du support est le garant de l'adoption par le voyageur."
                else:
                    analysis_text.string = "La capitalisation sur la data souveraine est l'unique chemin vers une valorisation durable de l'écosystème. La conformité RGPD doit être vue comme un avantage concurrentiel éthique."
                
                analysis_div.append(analysis_text)
                content_body.append(analysis_div)

    # 5. PAGE 25 (CAC Table)
    p25 = soup.find('div', id='p25')
    if p25:
        content_body = p25.find('div', class_='content-body')
        if content_body:
            # Replace existing card or add new one
            card = content_body.find('div', class_='glass-card')
            if card:
                card.clear()
                table = """
                <strong style="display:block; margin-bottom:10px;">[DÉTAIL DU CAC EXPERT - 2026]</strong>
                <table style="width:100%; font-size:9pt; border-collapse: collapse;">
                    <thead>
                        <tr style="border-bottom: 2px solid var(--gold);">
                            <th style="text-align:left; padding:5px;">Poste de Coût</th>
                            <th style="text-align:right; padding:5px;">Détail</th>
                            <th style="text-align:right; padding:5px;">Montant HT</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td style="padding:5px;">Ressources Humaines (SDR)</td><td style="text-align:right;">Qualification & Outreach</td><td style="text-align:right;">85,00 €</td></tr>
                        <tr><td style="padding:5px;">Infrastructures SaaS</td><td style="text-align:right;">Pharow, Instantly, Make</td><td style="text-align:right;">35,00 €</td></tr>
                        <tr><td style="padding:5px;">Logistique & Déplacements</td><td style="text-align:right;">Visites Closing (Amorti)</td><td style="text-align:right;">45,00 €</td></tr>
                        <tr><td style="padding:5px;">Data & Enrichissement</td><td style="text-align:right;">Verification & Validation</td><td style="text-align:right;">20,00 €</td></tr>
                        <tr style="border-top: 1px solid var(--gold); font-weight:bold;">
                            <td colspan="2" style="padding:5px;">TOTAL CAC CIBLE</td>
                            <td style="text-align:right; color:var(--gold);">185,00 €</td>
                        </tr>
                    </tbody>
                </table>
                """
                card.append(BeautifulSoup(table, 'html.parser'))

    # 6. PAGE 33 (Methodology)
    p33 = soup.find('div', id='p33')
    if p33:
        content_body = p33.find('div', class_='content-body')
        if content_body:
            method_div = soup.new_tag('div', class_='glass-card', style="border: 1px dashed var(--gold); font-size: 9.5pt;")
            method_content = """
            <strong>[MÉTHODOLOGIE DE RECHERCHE QUALITATIVE]</strong>
            <p>Étude fondée sur N=6 entretiens semi-directifs approfondis (durée moyenne : 75 min). 
            Le guide d'entretien s'est articulé autour de 4 axes : 
            1. Perceptions de la transition numérique. 
            2. Analyse des freins à l'automatisation. 
            3. Besoins en souveraineté de données. 
            4. Projection de valeur du groupement.</p>
            <p style="font-size:8pt; opacity:0.8;">Cible : Propriétaires de domaines de prestige (CA > 500k€). Période : Octobre 2025 - Janvier 2026.</p>
            """
            method_div.append(BeautifulSoup(method_content, 'html.parser'))
            content_body.insert(2, method_div)

    # 7. Restructure Action Plans (Sales Machine, Afterworks, NFC)
    
    # Sales Machine (Page 26)
    p26 = soup.find('div', id='p26')
    if p26:
        content_body = p26.find('div', class_='content-body')
        if content_body:
            content_body.clear()
            header = soup.new_tag('h1')
            header.string = "VIII. Sales Engine : L'Ingénierie"
            content_body.append(header)
            
            h2 = soup.new_tag('h2')
            h2.string = "8.1 Architecture de la Sales Système de Gestion"
            content_body.append(h2)
            
            structure = """
            <div class="glass-card">
                <p><strong>PROBLÈME :</strong> Le goulot d'étranglement de la croissance réside dans la gestion artisanale du recrutement (CAC élevé à 450€, temps SDR saturé).</p>
                <p><strong>ARBITRAGE :</strong> Développement d'une stack hybride (Pharow/Instantly/Make) plutôt qu'un recrutement massif. Choix de l'efficience technologique pour sanctuariser le temps de closing humain.</p>
                <p><strong>PILOTAGE :</strong> Mesure hebdomadaire du CAC, taux de conversion des leads AAA (>70) et monitoring de la délivrabilité email (objectif >95%).</p>
            </div>
            <p>Cette architecture permet de traiter 1200 leads/mois sans surcoût RH, garantissant une scalabilité industrielle du réseau.</p>
            """
            content_body.append(BeautifulSoup(structure, 'html.parser'))

    # Afterworks (Page 41)
    p41 = soup.find('div', id='p41')
    if p41:
        content_body = p41.find('div', class_='content-body')
        if content_body:
            content_body.clear()
            header = soup.new_tag('h1')
            header.string = "XI. Plan de Rétention"
            content_body.append(header)
            
            h2 = soup.new_tag('h2')
            h2.string = "11.2 Stratégie 'Double Détente' & Preuve Sociale"
            content_body.append(h2)
            
            structure = """
            <div class="glass-card">
                <p><strong>PROBLÈME :</strong> L'isolement opérationnel des hôtes entraîne un churn structurel (45% de départ par manque de ROI perçu).</p>
                <p><strong>ARBITRAGE :</strong> Création d'un cycle hybride Afterwork (physique) + Webinaire (digital). Le physique recrée le lien de confiance, le digital maintient l'autorité technique.</p>
                <p><strong>PILOTAGE :</strong> Suivi du taux d'attrition post-événement (objectif <5%) et calcul du NPS (Net Promoter Score) communautaire.</p>
            </div>
            <p>En transformant les membres performants en ambassadeurs, nous réduisons le besoin de réassurance commerciale directe.</p>
            """
            content_body.append(BeautifulSoup(structure, 'html.parser'))

    # NFC (Page 43)
    p43 = soup.find('div', id='p43')
    if p43:
        content_body = p43.find('div', class_='content-body')
        if content_body:
            content_body.clear()
            header = soup.new_tag('h1')
            header.string = "XII. Innovation Phygitale"
            content_body.append(header)
            
            h2 = soup.new_tag('h2')
            h2.string = "12.1 Justification NFC : Au-delà du Papier"
            content_body.append(h2)
            
            structure = """
            <div class="glass-card">
                <p><strong>PROBLÈME :</strong> Obsolescence immédiate des supports papier et perte totale de data sur le comportement voyageur on-site.</p>
                <p><strong>ARBITRAGE :</strong> Déploiement de supports NFC en bois noble (Chêne) plutôt que de simples QR codes ou applications mobiles lourdes. Le NFC est perçu comme un objet de luxe discret.</p>
                <p><strong>PILOTAGE :</strong> Tracking du taux d'engagement par chambre (scans/nuitée) et mesure de la vente additionnelle (upselling) via le Welcome Book digital.</p>
            </div>
            <p>Le NFC devient la sonde marketing invisible qui permet de profiler les centres d'intérêt réels du client premium.</p>
            """
            content_body.append(BeautifulSoup(structure, 'html.parser'))

    # Final string replacements for tone
    final_html = str(soup)
    for old, new in replacements.items():
        final_html = final_html.replace(old, new)

    # Title update
    final_html = final_html.replace("STRATEGIC COCKPIT 2026", "RAPPORT D'EXPERTISE STRATÉGIQUE 2026")
    final_html = final_html.replace("STRATEGIC<br>COCKPIT 2026", "RDM EXPERT<br>FINAL 2026")

    with open('RDM_EXPERT_FINAL_2026.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == "__main__":
    transform()
