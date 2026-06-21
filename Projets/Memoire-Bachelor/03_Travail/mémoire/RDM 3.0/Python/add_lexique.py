import codecs

with open('mémoire/RDM 3.0/build_rdm_v7_mastodonte.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add Lexique page
lexique_page = """
# --- PAGE 3.5 : LEXIQUE ---
pages.append({
    "section": "LEXIQUE & ACRONYMES",
    "content": \"\"\"
        <h1>Lexique et Acronymes</h1>
        
        <h2>Sigles et Vocabulaire Stratégique</h2>
        <p style="font-size: 10.5pt; text-align: justify; margin-bottom: 20px;">Ce rapport de mission s'appuie sur une terminologie technique propre au conseil en stratégie, au Growth Hacking et au secteur de l'hospitalité. Voici les définitions clés pour fluidifier la lecture :</p>

        <ul style="font-size: 10pt; line-height: 1.8;">
            <li><strong>ARPU (Average Revenue Per User) :</strong> Revenu moyen annuel généré par un hébergeur membre du réseau Happy House.</li>
            <li><strong>B2B (Business to Business) :</strong> Modèle économique où l'entreprise (Happy House) vend ses services à d'autres professionnels (les hébergeurs).</li>
            <li><strong>CAC (Coût d'Acquisition Client) :</strong> Montant total (budget marketing + masse salariale chargée) dépensé pour réussir à acquérir un nouveau client.</li>
            <li><strong>Churn (Taux d'Attrition) :</strong> Proportion de clients perdus (désabonnements ou perte totale de contact/silence radio) sur une période donnée.</li>
            <li><strong>CPA (Coût Par Acquisition) :</strong> Coût d'acquisition ramené à une action ou un canal spécifique (ex: le coût pour signer un client lors d'un Afterwork).</li>
            <li><strong>CRM (Customer Relationship Management) :</strong> Outil informatique ou base de données servant à gérer la relation avec les clients et les prospects (Suivi de l'onboarding, tags de statut).</li>
            <li><strong>DISC (Dominant, Influent, Stable, Conforme) :</strong> Méthode d'analyse comportementale utilisée par la force de vente pour cerner le profil psychologique du prospect et adapter le discours.</li>
            <li><strong>DPE (Diagnostic de Performance Énergétique) :</strong> Évaluation légale de la consommation énergétique d'un bâtiment, dont les mauvaises notes (F, G) entraînent désormais l'interdiction de location.</li>
            <li><strong>Inbound / Outbound :</strong> L'Outbound désigne la prospection "sortante" à froid (le commercial va chercher le client via appels ou emails). L'Inbound désigne la stratégie "entrante" (attirer le client à soi via des événements, des webinaires ou de la création de contenu).</li>
            <li><strong>LTV (Lifetime Value) :</strong> Revenu global généré par un membre sur la totalité de sa durée de vie (de sa signature à sa résiliation) au sein du réseau.</li>
            <li><strong>n8n :</strong> Outil de développement (Workflow Automation) permettant de connecter des APIs et d'automatiser des flux de données complexes sans nécessairement coder.</li>
            <li><strong>OTA (Online Travel Agency) :</strong> Agences de voyages monopolistes opérant sur internet (Booking.com, Airbnb, Expedia) qui prélèvent de fortes commissions sur les réservations.</li>
            <li><strong>POC (Proof of Concept) :</strong> "Preuve de Concept". Réalisation expérimentale ou maquette (ex: Le Dashboard ROI) visant à démontrer la faisabilité et la valeur d'un modèle avant son déploiement à grande échelle.</li>
            <li><strong>SDR (Sales Development Representative) :</strong> Commercial sédentaire spécialisé dans le premier contact et la pré-qualification des prospects avant la vente.</li>
        </ul>
    \"\"\"
})
"""

# Insert the lexique page right after the methodology page
# Looking for `# PAGE 4` or the introduction of Chapter 1
c = c.replace('# PAGE 5', lexique_page + '\n# PAGE 5')

# Update the TOC
old_toc = """chapitres = [
    ("PRÉAMBULE : LE RÉFÉRENTIEL D'ARBITRAGE", 3),
    ("I. L'ENTREPRISE & LA PROBLÉMATIQUE", 5),"""

new_toc = """chapitres = [
    ("PRÉAMBULE : LE RÉFÉRENTIEL D'ARBITRAGE", 3),
    ("LEXIQUE & ACRONYMES", 5),
    ("I. L'ENTREPRISE & LA PROBLÉMATIQUE", 6),"""

# Note: Adding a page shifts all subsequent pages by 1 in the TOC
# Let's dynamically shift the page numbers in the TOC for chapters after Lexique.
# It's better to just manually update the whole TOC list.
old_toc_full = """chapitres = [
    ("PRÉAMBULE : LE RÉFÉRENTIEL D'ARBITRAGE", 3),
    ("I. L'ENTREPRISE & LA PROBLÉMATIQUE", 5),
    ("II. LE MARCHÉ : LA FATIGUE NUMÉRIQUE", 8),
    ("III. AUDIT INTERNE : L'ÉQUATION DU NAUFRAGE", 11),
    ("IV. AUDIT DATA : LE FILTRE ALUR (126k LEADS)", 14),
    ("V. AUDIT ACQUISITION : L'IMPASSE OUTBOUND", 17),
    ("VI. LE PIVOT STRATÉGIQUE : L'INBOUND", 20),
    ("VII. LA RÉTENTION : LE DASHBOARD R.O.I", 23),
    ("VIII. LE PLAN D'ACTION & LE PILOTAGE COPIL", 26),
    ("IX. CV DIGITAL & BILAN PERSONNEL", 30),
    ("X. DÉCLARATION DE CONFORMITÉ IA", 32),
    ("XI. ANNEXES PHYSIQUES & MATRICES", 33),
    ("XII. DOSSIER DES PREUVES CLOUD", 43)
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
    ("XII. DOSSIER DES PREUVES CLOUD", 44)
]"""
c = c.replace(old_toc_full, new_toc_full)

with open('mémoire/RDM 3.0/build_rdm_v7_mastodonte.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Lexique & Acronymes page added and TOC updated.")
