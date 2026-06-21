import codecs

with open('build_rdm.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find cutoff
cutoff_idx = 0
for i, line in enumerate(lines):
    if '# --- ANNEXE 1 : PESTEL ---' in line:
        cutoff_idx = i
        break

c = "".join(lines[:cutoff_idx])

# Update TOC
c = c.replace('("IX. INDEX DES ANNEXES", 30)', '("IX. ANNEXES STRATÉGIQUES & PREUVES", 30)')

# New Annexes
new_annexes = """
# --- ANNEXES PHYSIQUES ---

pages.append({
    "section": "ANNEXE 1 : MATRICE PESTEL",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 1 : Matrice PESTEL</h1>
        <table style='width: 100%; border-collapse: collapse; font-size: 9pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 25%;'>Dimension</th><th>Analyse et Impact sur Happy House</th></tr>
            <tr>
                <td><strong>Politique & Légal</strong></td>
                <td>Loi anti-Airbnb (interdiction des DPE G en 2025 et F en 2028). Purge de 20 à 25% des acteurs non professionnels. <br><em>Impact : Opportunité majeure de cibler les professionnels restants (Prime à la qualité).</em></td>
            </tr>
            <tr>
                <td><strong>Économique</strong></td>
                <td>Inflation des coûts opérationnels (+15% sur l'énergie en 2024). <br><em>Impact : Fort levier d'acquisition via notre centrale d'achat (Entegra). Le ROI devient un argument vital.</em></td>
            </tr>
            <tr>
                <td><strong>Socioculturel</strong></td>
                <td>Recherche d'expériences authentiques et locales par les voyageurs (Slow Tourism). <br><em>Impact : Validation de notre ciblage "Premium & Charme".</em></td>
            </tr>
            <tr>
                <td><strong>Technologique</strong></td>
                <td>Monopole des OTAs (Booking, Airbnb) captant 71% des nuitées. <br><em>Impact : Nécessité d'accompagner les indépendants vers l'indépendance numérique.</em></td>
            </tr>
            <tr>
                <td><strong>Écologique</strong></td>
                <td>Pression pour des hébergements durables (Clef Verte +184%). <br><em>Impact : Argument de valorisation de nos membres.</em></td>
            </tr>
        </table>
    \"\"\"
})

pages.append({
    "section": "ANNEXE 2 : MATRICE SWOT",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 2 : Matrice SWOT</h1>
        <table style='width: 100%; border-collapse: collapse; font-size: 9pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'>
                <th style='width: 50%; text-align: center;'>FORCES (Internes)</th>
                <th style='width: 50%; text-align: center;'>FAIBLESSES (Internes)</th>
            </tr>
            <tr>
                <td style='height: 100px;'>- Partenariat exclusif Entegra (Gains 15-25%).<br>- Base de données qualifiée (126 000 contacts).<br>- Positionnement premium reconnu.<br>- Équipe agile de 4 personnes (1 CEO, 3 alternants).</td>
                <td>- Taux de churn historique élevé (~80%).<br>- Défaut de formalisation du ROI pour les membres.<br>- Prospection téléphonique manuelle trop onéreuse (CAC à 1823€).</td>
            </tr>
            <tr style='background: rgba(221, 168, 62, 0.2);'>
                <th style='text-align: center;'>OPPORTUNITÉS (Externes)</th>
                <th style='text-align: center;'>MENACES (Externes)</th>
            </tr>
            <tr>
                <td style='height: 100px;'>- Purge des amateurs via les contraintes DPE.<br>- Besoin d'accompagnement lié à l'inflation (énergie).</td>
                <td>- Hégémonie des OTAs (71% des parts de marché).<br>- Fatigue numérique des prospects (rejet du démarchage de masse).</td>
            </tr>
        </table>
    \"\"\"
})

pages.append({
    "section": "ANNEXE 3 : FORCES DE PORTER",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 3 : Les 5 Forces de Porter</h1>
        <table style='width: 100%; border-collapse: collapse; font-size: 9pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 30%;'>Force Concurrentielle</th><th style='width: 20%;'>Intensité</th><th>Justification</th></tr>
            <tr>
                <td><strong>Intensité Concurrentielle</strong></td>
                <td style="color: #E74C3C;">Forte (4/5)</td>
                <td>Concurrence accrue sur le marché des logiciels et plateformes de distribution. Les hébergeurs sont sur-sollicités.</td>
            </tr>
            <tr>
                <td><strong>Menace Nouveaux Entrants</strong></td>
                <td style="color: #2ECC71;">Faible (2/5)</td>
                <td>Les normes DPE et les lourds investissements requis créent de fortes barrières à l'entrée. Le marché se professionnalise.</td>
            </tr>
            <tr>
                <td><strong>Pouvoir de Négociation Clients (OTAs)</strong></td>
                <td style="color: #E74C3C;">Très Fort (5/5)</td>
                <td>Booking.com et Airbnb dictent les commissions (15 à 25%). Les hébergeurs sont dépendants de cette visibilité algorithmique.</td>
            </tr>
            <tr>
                <td><strong>Pouvoir Négociation Fournisseurs</strong></td>
                <td style="color: #F1C40F;">Moyen (3/5)</td>
                <td>Fournisseurs d'énergie et équipementiers hôteliers en position de force face à l'inflation, justifiant la massification des achats.</td>
            </tr>
            <tr>
                <td><strong>Menace des Substituts</strong></td>
                <td style="color: #F1C40F;">Moyenne (3/5)</td>
                <td>Les hôtels standards ou les résidences de tourisme industrialisées face au concept d'hébergement "de charme".</td>
            </tr>
        </table>
    \"\"\"
})

pages.append({
    "section": "ANNEXE 4 : COMPARATIF DE PERFORMANCE",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 4 : Comparatif de Performance (Acquisition)</h1>
        
        <p style="font-size: 9pt;">Modélisation chiffrée démontrant l'impasse financière de la stratégie Outbound initiale face à la rentabilité de la nouvelle stratégie événementielle Inbound.</p>

        <div class="visual-block" style="border-color: #DDA83E;">
            <div class="visual-title">1. MODÈLE HISTORIQUE : OUTBOUND (Cold Calling)</div>
            <div class="code-line">- Charge mensuelle SDR (Alternant >26 ans) : 1 823 € (100% SMIC exonéré).</div>
            <div class="code-line">- Volume d'appels : ~6 000 / mois.</div>
            <div class="code-line">- Taux de conversion constaté : 1 signature / mois.</div>
            <div class="code-line" style="color: #E74C3C; font-weight: bold;">=> Coût d'Acquisition Client (CAC) : 1 823 € / membre.</div>
            <div class="code-line"><em>Conclusion : Le CAC détruit intégralement la rentabilité de la cotisation annuelle.</em></div>
        </div>

        <div class="visual-block" style="border-color: #2ECC71;">
            <div class="visual-title" style="color: #2ECC71;">2. MODÈLE PIVOT : INBOUND (Événementiel)</div>
            <div class="code-line">- Budget organisation Afterwork (Traiteur, Logistique) : ~500 € / événement.</div>
            <div class="code-line">- Objectif de conversion post-événement : 3 signatures.</div>
            <div class="code-line" style="color: #2ECC71; font-weight: bold;">=> Coût Par Acquisition (CPA) Projeté : 166 € / membre.</div>
            <div class="code-line"><em>Conclusion : Un modèle d'acquisition rentable, favorisant en outre la rétention (Preuve sociale).</em></div>
        </div>
    \"\"\"
})

pages.append({
    "section": "ANNEXE 5 & 10 : CHURN & RENTABILITÉ",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 5 & 10 : Modélisation Churn et Rentabilité (Durentie)</h1>
        
        <h2 style='font-size: 11pt;'>Modélisation de l'Attrition (Churn)</h2>
        <p style='font-size: 9pt;'>Le taux d'attrition historique évalué à 80% impacte sévèrement la <strong>Lifetime Value (LTV)</strong> du client. La mise en place du Dashboard trimestriel vise à stopper cette érosion en matérialisant instantanément le retour sur investissement de la cotisation (360 €).</p>

        <h2 style='font-size: 11pt; margin-top: 20px;'>Évaluation Rentabilité Centrale d'Achats (Cas Durentie)</h2>
        <p style='font-size: 9pt;'>Simulation extraite de la comptabilité analytique d'un domaine Premium suite à son adhésion au réseau Happy House.</p>

        <table style='width: 100%; border-collapse: collapse; font-size: 9pt; margin-top: 10px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 50%;'>Poste Financier</th><th>Montant (€)</th></tr>
            <tr><td>Investissement Initial (Cotisation Adhérent)</td><td style="color: #E74C3C;">- 360,00 €</td></tr>
            <tr><td>Économies F&B (Alimentation & Boissons) Entegra</td><td style="color: #2ECC71;">+ 2 150,00 €</td></tr>
            <tr><td>Économies Énergie</td><td style="color: #2ECC71;">+ 1 420,00 €</td></tr>
            <tr><td>Économies Blanchisserie</td><td style="color: #2ECC71;">+ 550,00 €</td></tr>
            <tr style='border-top: 1px solid var(--gold);'><td><strong>BÉNÉFICE NET OPÉRATIONNEL (A)</strong></td><td><strong>+ 4 120,00 €</strong></td></tr>
            <tr><td>CA Généré (Apport réseau membre à membre) (B)</td><td style="color: #2ECC71;">+ 11 000,00 €</td></tr>
            <tr style='background: rgba(46, 204, 113, 0.1);'><td><strong>IMPACT GLOBAL SUR L'ÉTABLISSEMENT (A+B)</strong></td><td><strong style="color: #2ECC71;">+ 15 120,00 €</strong></td></tr>
        </table>
    \"\"\"
})

pages.append({
    "section": "DOSSIER DE PREUVES",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>DOSSIER DE PREUVES COMPLÉMENTAIRES</h1>
        
        <p style="font-size: 9pt; text-align: center; margin-bottom: 30px;">
            Les documents opérationnels, livrables contractuels et tableaux de pilotage volumineux ont été sécurisés sur une infrastructure Cloud dédiée. Vous pouvez les consulter en un clic via les accès sécurisés ci-dessous.
        </p>

        <div style="display: flex; flex-direction: column; gap: 15px; align-items: center;">
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/raw/main/Justificatifs_Preuves/Pack_Communication_2_HH.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                📄 1. Pack Communication & Branding
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/raw/main/Justificatifs_Preuves/Process_d_integration_1.1.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                🤝 2. Contrats & Cadre de Confiance
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/raw/main/Justificatifs_Preuves/PMS_CONNECTES.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                🏢 3. Justificatif d'Activité n°2
            </a>
            <a href="https://htmlpreview.github.io/?https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/Justificatifs_Preuves/DATA_DEMONSTRATION_FORCE.html" target="_blank" class="btn-nav" style="width: 80%;">
                📦 4. Livrable Mission n°1
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/raw/main/Justificatifs_Preuves/Process_Commercial_KPIs_Happy_House.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                📊 5. Relevés de Performance & Stats
            </a>
            <a href="https://htmlpreview.github.io/?https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/Justificatifs_Preuves/DASHBOARD_HEBERGEURS.html" target="_blank" class="btn-nav" style="width: 80%;">
                ⚙️ 6. Archive Technique & Preuve n°3
            </a>
        </div>
    \"\"\"
})

def make_page(content, page_num, section_title):
    html = f\"\"\"
    <div class="page">
        <a id="page-{page_num}" style="display: block; height: 1px; width: 1px;">&nbsp;</a>
        <div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content">
            {content}
        </div>
        <div class="footer">
            <a href="#page-2" style="color: #DDA83E; border: 1px solid #DDA83E; padding: 5px 10px; display: inline-block; font-size: 7pt;">◈ RETOUR SOMMAIRE</a>
            <div style="color: #DDA83E; font-size: 7.5pt; text-transform: uppercase;">{section_title}</div>
            <div class="page-number" style="color: #DDA83E;">{page_num:02d}</div>
        </div>
    </div>
\"\"\"
    return html

# Assembly
final_html = html_head
page_number = 1

for p in pages:
    if p.get("is_cover", False):
        final_html += f\"\"\"
    <div class="page cover">
        <div class="cover-bg"></div>
        <a id="page-{page_number}"></a>
        <div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content cover-content">
            {p["content"]}
        </div>
        <div class="footer">
            <div style="color: #DDA83E;">HAPPY HOUSE & ROCKET SCHOOL</div>
            <div class="page-number" style="color: #DDA83E;">{page_number:02d}</div>
        </div>
    </div>
\"\"\"
    else:
        final_html += make_page(p["content"], page_number, p["section"])
    page_number += 1

final_html += "</body></html>"

base_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(base_path, "RAPPORT_DE_MISSION_ULTRA_PRESTIGE.html")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"[✓] HTML académique généré avec succès ({page_number-1} pages estimées).")
"""

with open('build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(c + new_annexes)

print("Annexes physicalized and Drive links transformed into buttons.")
