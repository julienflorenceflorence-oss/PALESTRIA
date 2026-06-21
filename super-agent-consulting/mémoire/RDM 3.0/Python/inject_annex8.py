import codecs

with open('build_rdm_v7_mastodonte.py', 'r', encoding='utf-8') as f:
    c = f.read()

# ADD ANNEX 8: CRM & NURTURING
annexe_crm_nurturing = """
# PAGE 32.5
pages.append({
    "section": "ANNEXE 8 : OUTILS D'ACQUISITION (CRM & NURTURING)",
    "content": \"\"\"
        <a id="annexe-8"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXE 8 : Preuves Opérationnelles (CRM & Nurturing)</h1>
        
        <p style="font-size: 10.5pt; text-align: justify; margin-bottom: 20px; line-height: 1.6;">Cette annexe matérialise l'ingénierie opérationnelle développée pour soutenir le pivot stratégique : la qualification des leads (Scoring) et la préparation du terrain avant l'appel (Nurturing).</p>

        <h2 style='font-size: 13pt; margin-top: 20px; color: var(--gold-light);'>1. Le Scoring CRM (L'Interface de Pilotage SDR)</h2>
        <p style="font-size: 9.5pt; margin-bottom: 15px; color: var(--text-muted);">L'interface CRM développée spécifiquement pour le SDR permet de classer les leads issus du fichier de 126k contacts, après le filtre Loi ALUR. Elle met en évidence la séparation stratégique entre "PRO" et "PARTICULIER".</p>

        <div class="visual-block" style="border-color: #2ECC71; padding: 20px;">
            <div class="visual-title" style="color: #2ECC71; font-size: 11pt;">EXTRAIT INTERFACE CRM (QUALIFICATION & TAGS)</div>
            
            <table style="width: 100%; border-collapse: collapse; font-size: 9pt; margin-top: 10px;">
                <tr style="background: rgba(255,255,255,0.05);">
                    <th style="padding: 8px;">Statut ALUR</th>
                    <th style="padding: 8px;">Nom du Domaine</th>
                    <th style="padding: 8px;">Standing</th>
                    <th style="padding: 8px;">Dép.</th>
                    <th style="padding: 8px;">Tag de Suivi (Qualification)</th>
                </tr>
                <tr>
                    <td style="color: #fd7e14; font-weight: bold;">PARTICULIER</td>
                    <td>Les Caudalies</td>
                    <td>⭐⭐⭐</td>
                    <td>39</td>
                    <td style="color: #28a745;">SUIVI NÉGO (Potentiel détecté, demande comparatif)</td>
                </tr>
                <tr>
                    <td style="color: #28a745; font-weight: bold;">PROFESSIONNEL</td>
                    <td>Hostellerie de Bretonnière</td>
                    <td>⭐⭐⭐</td>
                    <td>21</td>
                    <td style="color: #28a745;">SUIVI NÉGO (Potentiel détecté)</td>
                </tr>
                <tr>
                    <td style="color: #fd7e14; font-weight: bold;">PARTICULIER</td>
                    <td>Chalet adossé à la forêt</td>
                    <td>⭐⭐⭐</td>
                    <td>25</td>
                    <td style="color: #ffc107;">REFUS ARGUMENTÉ (Surcharge, besoin de Social Proof)</td>
                </tr>
                <tr>
                    <td style="color: #28a745; font-weight: bold;">PROFESSIONNEL</td>
                    <td>Annexe du 11 C</td>
                    <td>⭐⭐⭐</td>
                    <td>25</td>
                    <td style="color: #dc3545;">REFUS CATÉGORIQUE (Refus immédiat, typique Outbound)</td>
                </tr>
                <tr>
                    <td style="color: #fd7e14; font-weight: bold;">PARTICULIER</td>
                    <td>Chalets des Chemins Verts</td>
                    <td>⭐⭐⭐⭐</td>
                    <td>39</td>
                    <td style="color: #6c757d;">NRP (Non-Réponse, relance soir/week-end requise)</td>
                </tr>
            </table>
            <p style="font-size: 8.5pt; color: var(--text-muted); margin-top: 10px; font-style: italic;">* Note analytique : L'identification précise des "Particuliers Premium" (3 à 5 étoiles) est le socle de l'invitation VIP aux Afterworks.</p>
        </div>

        <h2 style='font-size: 13pt; margin-top: 30px; color: var(--gold-light);'>2. Le Nurturing (L'Échauffement du Lead)</h2>
        <p style="font-size: 9.5pt; margin-bottom: 15px; color: var(--text-muted);">Pour briser la glace (le "Mur du Silence") et contourner la fatigue numérique, des séquences d'emails sont orchestrées vers les institutionnels locaux (Offices du Tourisme) pour préparer le terrain de l'Afterwork avant l'appel.</p>

        <div class="glass-card" style="padding: 20px; font-size: 9.5pt;">
            <div class="visual-title" style="color: var(--gold); font-size: 11pt; margin-bottom: 15px;">TEMPLATE PROSPECTION : LEVIER INSTITUTIONNEL</div>
            <p style="color: var(--text-muted); line-height: 1.5;"><strong>Objet :</strong> Partenariat Excellence Locale - Événement Happy House [Région]<br>
            <strong>Cible :</strong> Responsable Hébergement (Office du Tourisme)</p>
            <p style="color: #FFF; line-height: 1.5; font-style: italic; border-left: 2px solid var(--gold); padding-left: 10px; margin-top: 10px;">
                "Bonjour [Prénom],<br><br>
                Dans le cadre du développement de notre réseau de domaines de charme (3 à 5 étoiles), nous organisons prochainement un événement privé (Afterwork) dédié aux exploitants indépendants de la région [Région].<br><br>
                Face à la complexité des nouvelles normes (Loi ALUR, DPE) et à l'inflation des coûts, notre objectif est d'offrir à vos acteurs locaux des solutions pragmatiques de professionnalisation (Cost-Killing via notre centrale d'achat, optimisation de la distribution directe).<br><br>
                Afin de garantir un niveau d'échange Premium, nous souhaiterions échanger avec vous pour identifier les propriétaires de votre territoire qui bénéficieraient le plus de cette invitation exclusive. Seriez-vous disponible pour un court échange téléphonique ce [Jour] ?"
            </p>
        </div>
    \"\"\"
})
"""

# INSERT INTO CODE
c = c.replace('# PAGE 32\npages.append({', annexe_crm_nurturing + '\n# PAGE 32\npages.append({')

# Update TOC to reflect Annex 8
old_toc_full = """chapitres = [
    ("PRÉAMBULE : LE RÉFÉRENTIEL D'ARBITRAGE", 3),
    ("LEXIQUE & ACRONYMES", 5),
    ("I. L'ENTREPRISE & LA PROBLÉMATIQUE", 6),
    ("II. LE MARCHÉ : LA FATIGUE NUMÉRIQUE", 9),
    ("III. AUDIT INTERNE : L'ÉQUATION DU NAUFRAGE", 12),
    ("IV. AUDIT DATA : LE FILTRE ALUR (126k LEADS)", 15),
    ("V. AUDIT ACQUISITION : L'IMPASSE OUTBOUND", 18),
    ("VI. LE PIVOT STRATÉGIQUE : L'INBOUND", 21),
    ("VII. LA RÉTENTION : LE DASHBOARD R.O.I", 24),
    ("VIII. LE PLAN D'ACTION & LE PILOTAGE COPIL", 27),
    ("IX. CV DIGITAL & BILAN PERSONNEL", 31),
    ("X. DÉCLARATION DE CONFORMITÉ IA", 33),
    ("XI. ANNEXES PHYSIQUES & MATRICES", 34),
    ("XII. DOSSIER DES PREUVES CLOUD", 44)
]"""

new_toc_full = """chapitres = [
    ("PRÉAMBULE : LE RÉFÉRENTIEL D'ARBITRAGE", 3),
    ("LEXIQUE & ACRONYMES", 5),
    ("I. L'ENTREPRISE & LA PROBLÉMATIQUE", 6),
    ("II. LE MARCHÉ : LA FATIGUE NUMÉRIQUE", 9),
    ("III. AUDIT INTERNE : L'ÉQUATION DU NAUFRAGE", 12),
    ("IV. AUDIT DATA : LE FILTRE ALUR (126k LEADS)", 15),
    ("V. AUDIT ACQUISITION : L'IMPASSE OUTBOUND", 18),
    ("VI. LE PIVOT STRATÉGIQUE : L'INBOUND", 21),
    ("VII. LA RÉTENTION : LE DASHBOARD R.O.I", 24),
    ("VIII. LE PLAN D'ACTION & LE PILOTAGE COPIL", 27),
    ("IX. CV DIGITAL & BILAN PERSONNEL", 31),
    ("X. DÉCLARATION DE CONFORMITÉ IA", 33),
    ("XI. ANNEXES PHYSIQUES & MATRICES", 34),
    ("XII. DOSSIER DES PREUVES CLOUD", 45)
]"""

c = c.replace(old_toc_full, new_toc_full)

with open('build_rdm_v7_mastodonte.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Annex 8 injected (CRM & Templates).")