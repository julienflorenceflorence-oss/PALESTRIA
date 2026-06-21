import codecs

with open('mémoire/RDM 3.0/build_rdm.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the current Annex 9 block with a split version
old_annexe9 = """# --- ANNEXE 9 : DONNÉES MARCHÉ ---
pages.append({
    "section": "ANNEXE 9 : ÉVOLUTION DU MARCHÉ",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 9 : Pression Commerciale (OTAs & Labels)</h1>
        
        <p style="font-size: 9pt;">Extrait de la base de données sectorielle : Évolution de la domination des plateformes et prolifération des certifications environnementales imposant une forte charge mentale aux exploitants (2013-2026).</p>

        <h2 style='font-size: 11pt; margin-top: 15px;'>1. L'Hégémonie des OTAs (Online Travel Agencies) en Europe</h2>
        <table style='width: 100%; border-collapse: collapse; font-size: 8pt; margin-top: 10px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 15%;'>Année</th><th style='width: 60%;'>Indicateur Sectoriel</th><th style='width: 25%;'>Valeur</th></tr>
            <tr><td>2013</td><td>Part de marché globale des OTAs</td><td>19,7 %</td></tr>
            <tr><td>2019</td><td>Part de marché globale des OTAs</td><td>29,2 %</td></tr>
            <tr><td>2023</td><td>Part de marché globale des OTAs</td><td><strong>29,6 %</strong></td></tr>
            <tr><td>2024</td><td>Part de marché spécifique : <strong>Booking.com</strong></td><td><strong>69,3 %</strong> (du marché OTA)</td></tr>
            <tr><td>2024</td><td>Part de marché spécifique : <strong>Expedia</strong></td><td>11,5 % (du marché OTA)</td></tr>
            <tr><td>2024</td><td>Poids économique mondial du marché OTA</td><td>253,2 Milliards $</td></tr>
        </table>
        <p style="font-size: 8pt; color: #888; font-style: italic; margin-top: 5px;">* Sources : Statistiques DGE, MKG Consulting, Rapports institutionnels.</p>

        <h2 style='font-size: 11pt; margin-top: 20px;'>2. L'Inflation des Certifications & Labels (Marché Français)</h2>
        <table style='width: 100%; border-collapse: collapse; font-size: 8pt; margin-top: 10px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 15%;'>Année</th><th style='width: 60%;'>Indicateur Sectoriel</th><th style='width: 25%;'>Valeur</th></tr>
            <tr><td>2022</td><td>Nombre d'établissements labelisés "Clef Verte"</td><td>855 établissements</td></tr>
            <tr><td>2024</td><td>Nombre d'établissements labelisés "Clef Verte"</td><td>1 564 établissements</td></tr>
            <tr><td>2025</td><td>Projection établissements "Clef Verte"</td><td><strong>2 428 établissements</strong> (+184% en 3 ans)</td></tr>
            <tr><td>2024</td><td>Label "Qualité Tourisme" (Arrêt des attributions)</td><td>5 000 établissements</td></tr>
            <tr><td>2024</td><td>Nouveau label "Destination Excellence"</td><td>203 premiers labellisés</td></tr>
            <tr><td>2026</td><td>Label "Qualité Tourisme"</td><td><strong>Disparition totale</strong> annoncée</td></tr>
        </table>
        
        <div class="expert-note" style="margin-top: 15px;">
            <strong>Analyse Stratégique : La "Fatigue Numérique"</strong><br>
            Ces données factuelles valident l'impasse d'une prospection Outbound pour Happy House. L'hébergeur Premium est saturé par deux forces majeures : le monopole écrasant de Booking (qu'il cherche à fuir mais qui capte 70% des flux) et l'instabilité des normes écologiques (la disparition d'un label historique au profit de nouveaux). Toute sollicitation numérique ou téléphonique de masse est instantanément assimilée à ce bruit ambiant.
        </div>
    \"\"\"
})"""

new_annexe9 = """# --- ANNEXE 9 : DONNÉES MARCHÉ ---
pages.append({
    "section": "ANNEXE 9 : ÉVOLUTION DU MARCHÉ",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 9 : Pression Commerciale (1/2)</h1>
        
        <p style="font-size: 9pt;">Extrait de la base de données sectorielle : Évolution de la domination des plateformes et prolifération des certifications environnementales imposant une forte charge mentale aux exploitants (2013-2026).</p>

        <h2 style='font-size: 11pt; margin-top: 15px;'>1. L'Hégémonie des OTAs (Online Travel Agencies) en Europe</h2>
        <table style='width: 100%; border-collapse: collapse; font-size: 9pt; margin-top: 10px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 15%;'>Année</th><th style='width: 60%;'>Indicateur Sectoriel</th><th style='width: 25%;'>Valeur</th></tr>
            <tr><td>2013</td><td>Part de marché globale des OTAs</td><td>19,7 %</td></tr>
            <tr><td>2019</td><td>Part de marché globale des OTAs</td><td>29,2 %</td></tr>
            <tr><td>2023</td><td>Part de marché globale des OTAs</td><td><strong>29,6 %</strong></td></tr>
            <tr><td>2024</td><td>Part de marché spécifique : <strong>Booking.com</strong></td><td><strong>69,3 %</strong> (du marché OTA)</td></tr>
            <tr><td>2024</td><td>Part de marché spécifique : <strong>Expedia</strong></td><td>11,5 % (du marché OTA)</td></tr>
            <tr><td>2024</td><td>Poids économique mondial du marché OTA</td><td>253,2 Milliards $</td></tr>
        </table>
        <p style="font-size: 8pt; color: #888; font-style: italic; margin-top: 5px;">* Sources : Statistiques DGE, MKG Consulting, Rapports institutionnels.</p>
    \"\"\"
})

pages.append({
    "section": "ANNEXE 9 : ÉVOLUTION DU MARCHÉ (SUITE)",
    "content": \"\"\"
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 10px;'>ANNEXE 9 : Pression Commerciale (2/2)</h1>
        
        <h2 style='font-size: 11pt; margin-top: 20px;'>2. L'Inflation des Certifications & Labels (Marché Français)</h2>
        <table style='width: 100%; border-collapse: collapse; font-size: 9pt; margin-top: 10px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 15%;'>Année</th><th style='width: 60%;'>Indicateur Sectoriel</th><th style='width: 25%;'>Valeur</th></tr>
            <tr><td>2022</td><td>Nombre d'établissements labelisés "Clef Verte"</td><td>855 établissements</td></tr>
            <tr><td>2024</td><td>Nombre d'établissements labelisés "Clef Verte"</td><td>1 564 établissements</td></tr>
            <tr><td>2025</td><td>Projection établissements "Clef Verte"</td><td><strong>2 428 établissements</strong> (+184% en 3 ans)</td></tr>
            <tr><td>2024</td><td>Label "Qualité Tourisme" (Arrêt des attributions)</td><td>5 000 établissements</td></tr>
            <tr><td>2024</td><td>Nouveau label "Destination Excellence"</td><td>203 premiers labellisés</td></tr>
            <tr><td>2026</td><td>Label "Qualité Tourisme"</td><td><strong>Disparition totale</strong> annoncée</td></tr>
        </table>
        
        <div class="expert-note" style="margin-top: 30px;">
            <strong>Analyse Stratégique : La "Fatigue Numérique"</strong><br>
            Ces données factuelles valident l'impasse d'une prospection Outbound pour Happy House. L'hébergeur Premium est saturé par deux forces majeures : le monopole écrasant de Booking (qu'il cherche à fuir mais qui capte 70% des flux) et l'instabilité des normes écologiques (la disparition d'un label historique au profit de nouveaux). Toute sollicitation numérique ou téléphonique de masse est instantanément assimilée à ce bruit ambiant.
        </div>
    \"\"\"
})"""

c = c.replace(old_annexe9, new_annexe9)

with open('mémoire/RDM 3.0/build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(c)
print("Splitted Annex 9.")
