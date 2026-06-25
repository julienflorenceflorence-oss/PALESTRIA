import codecs

with open('build_rdm.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Problématique Formulation claire
old_prob = "Comment le réseau Happy House peut-il optimiser la rétention de ses membres et structurer son acquisition tout en intégrant les contraintes de gouvernance interne et son positionnement premium ?"
new_prob = "Comment Happy House peut-elle réduire son taux d'attrition tout en structurant une stratégie d'acquisition rentable, adaptée à son positionnement premium et aux contraintes de sa gouvernance interne ?"
c = c.replace(old_prob, new_prob)

# 2. Add Missing Annexes BEFORE the Index Page
annexe_pestel = """
# --- ANNEXE 1 : PESTEL ---
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
                <td>Pression pour des hébergements durables. <br><em>Impact : Argument de valorisation de nos membres.</em></td>
            </tr>
        </table>
    \"\"\"
})
"""

annexe_swot = """
# --- ANNEXE 2 : SWOT ---
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
"""

annexe_script = """
# --- ANNEXE 6 : SCRIPT ---
pages.append({
    "section": "ANNEXE 6 & 7 : SCRIPT SDR",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 6/7 : Script de Qualification SDR (Extrait)</h1>
        <div class='glass-card' style='font-size: 9pt;'>
            <p><strong>Objectif :</strong> Passer d'une vente directe (qui générait 50% de NRP et 20% de refus catégoriques) à une approche d'invitation événementielle (Pivot Inbound).</p>
            <p style='margin-top: 15px;'><strong>ACCROCHE (Casser la friction) :</strong><br>
            <em style='color: #A9B7C6;'>« Bonjour [Prénom], c’est Younes de Happy House. Je vous appelle car nous organisons un événement privé pour les hébergeurs premium de [Région] le [Date], et votre domaine a attiré notre attention. »</em></p>
            <p style='margin-top: 15px;'><strong>QUALIFICATION (Méthode DISC) :</strong><br>
            - Si profil <strong>Dominant (D)</strong> : Axer sur la rentabilité (<em style='color: #A9B7C6;'>« On abordera comment réduire les charges F&B de 20% »</em>).<br>
            - Si profil <strong>Influent (I)</strong> : Axer sur le réseau (<em style='color: #A9B7C6;'>« Ce sera l'occasion d'échanger avec vos pairs de la région »</em>).</p>
            <p style='margin-top: 15px;'><strong>CLÔTURE :</strong><br>
            <em style='color: #A9B7C6;'>« L'accès est sur invitation, je vous fais parvenir le lien d'inscription. Vous pourrez échanger directement avec [Nom d'un membre existant] qui sera présent. »</em></p>
        </div>
    \"\"\"
})
"""

c = c.replace('# --- ANNEXES ---', annexe_pestel + '\n' + annexe_swot + '\n' + annexe_script + '\n# --- ANNEXES ---')

old_cloud_text = "Conformément aux contraintes de volume (20 pages max), les annexes complètes de ce rapport (Documents stratégiques, Matrices lourdes, Scripts de vente, Preuves financières) sont disponibles intégralement en ligne."
new_cloud_text = "Une sélection des annexes fondamentales au raisonnement (PESTEL, SWOT, Extraits de Script) a été intégrée physiquement dans les pages précédentes pour appuyer la démonstration académique. Les preuves financières additionnelles ou volumineuses restent disponibles en ligne ci-dessous."
c = c.replace(old_cloud_text, new_cloud_text)

with open('build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated Problématique and appended physical Annexes.")
