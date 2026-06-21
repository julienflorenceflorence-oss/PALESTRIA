import codecs

with open('build_rdm_v5_expert.py', 'r', encoding='utf-8') as f:
    c = f.read()

# PERSONAS IN CHAP 6 (Le Pivot)
new_personas = """
# PAGE 17.5 : PERSONAS
pages.append({
    "section": "CHAPITRE 6 : L'ANATOMIE DU PIVOT (LES PERSONAS)",
    "content": \"\"\"
        <a id="chapitre-6-personas"></a>
        <h2>L'Anatomie du Pivot : La Création des Personas</h2>
        <p>L'abandon de l'Outbound de masse ne suffit pas ; il fallait structurer le ciblage de l'événementiel Inbound. L'extraction et l'analyse croisée de notre base de 126 000 contacts avec les observations terrain nous ont permis de modéliser avec une précision clinique les 3 avatars psychologiques (Personas) qui constituent notre cœur de cible. Sans cette modélisation, le taux de conversion lors des Afterworks chuterait.</p>

        <div class="analytic-point">1. Le Persona "Dominant" : Jean-Marc, 55 ans</div>
        <div class="analytic-content">
            <strong>Typologie :</strong> Propriétaire de 3 Gros Gîtes Premium.<br>
            <strong>La Maladie :</strong> L'obsession de la rentabilité. Il voit ses marges fondre face à l'inflation énergétique et à la commission de Booking.<br>
            <strong>Le Remède Happy House :</strong> L'approche Cost-Killing. L'invitation à l'Afterwork ne parlera jamais de "réseau" ou de "convivialité", mais exclusivement d'une méthode chiffrée pour réduire ses frais F&B de 20% via Entegra.
        </div>

        <div class="analytic-point">2. Le Persona "Influent" : Sophie, 40 ans</div>
        <div class="analytic-content">
            <strong>Typologie :</strong> Ancienne cadre en reconversion, propriétaire d'une maison d'hôtes de charme.<br>
            <strong>La Maladie :</strong> L'isolement entrepreneurial. La charge mentale de la gestion opérationnelle la coupe de toute réflexion stratégique.<br>
            <strong>Le Remède Happy House :</strong> L'approche Communautaire. L'invitation à l'Afterwork mettra en avant la rencontre physique avec ses pairs de la région pour échanger sur les bonnes pratiques et rompre la solitude.
        </div>

        <div class="analytic-point">3. La Persona "Néo-Entrante" (Cible ALUR) : Delphine, 36 ans</div>
        <div class="analytic-content">
            <strong>Typologie :</strong> Vient d'hériter d'une maison familiale et se lance dans l'activité de gîte en parallèle de son poste de salariée.<br>
            <strong>La Maladie :</strong> La terreur administrative. Elle est la cible directe du couperet de la Loi ALUR (120 jours max) et du DPE. Sans aide, elle abandonnera le marché.<br>
            <strong>Le Remède Happy House :</strong> La Professionnalisation comme bouclier de survie. L'Afterwork sera présenté comme une consultation d'urgence pour la mettre aux normes d'exploitation et pérenniser son patrimoine.
        </div>
    \"\"\"
})
"""

# Insert personas right before Chapter 7
c = c.replace('# PAGE 18\npages.append({', new_personas + '\n# PAGE 18\npages.append({')


# AUDIT N8N IN CHAP 4
old_data_audit = """<div class="analytic-point">3. Les Preuves Chiffrées (Le Tri de l'Algorithme)</div>
        <div class="analytic-content">Le scan exhaustif de l'algorithme sur les <span class="analytic-highlight">126 000 lignes prospects</span> livre une répartition implacable"""

new_data_audit = """<div class="analytic-point">3. Les Preuves Chiffrées (L'Architecture de Filtrage via n8n)</div>
        <div class="analytic-content">Le tri n'est pas manuel, il est technologique. L'agent IA que j'ai configuré via l'outil <strong>n8n</strong> s'est branché sur l'API de <em>societe.fr</em> pour opérer une première scission automatisée : séparer les Hébergeurs Professionnels des Particuliers. Une seconde automatisation a évalué les critères de confort (3 à 5 étoiles), les prestations annexes (ventes additionnelles) et le volume d'avis clients. Ce scan exhaustif sur les <span class="analytic-highlight">126 000 lignes prospects</span> livre une répartition implacable"""
c = c.replace(old_data_audit, new_data_audit)

old_data_alur = """<div class="analytic-content">Le fichier de 126k contacts devient un outil de <em>Ciblage d'Urgence</em>."""

new_data_alur = """<div class="analytic-content">Le fichier de 126k contacts devient un outil de <em>Ciblage d'Urgence</em>. Une fois la sélection algorithmique terminée, n8n a orchestré la mise en relation automatisée avec les Offices du Tourisme locaux (prise de contact avec les responsables hébergement) couplée à l'envoi d'une série d'emails de chauffe ("Nurturing") pour préparer le terrain avant l'appel du SDR. """
c = c.replace(old_data_alur, new_data_alur)


# PRICING
pricing_page = """
# PAGE 18.5 : PRICING
pages.append({
    "section": "CHAPITRE 6 : L'AUDIT FINANCIER (PRICING)",
    "content": \"\"\"
        <a id="chapitre-6-pricing"></a>
        <h2>L'Audit Financier Étendu : La Grille Tarifaire</h2>
        
        <p>L'analyse du Ratio LTV/CAC catastrophique (0.16) imposait de disséquer le revenu généré par notre cible. Le diagnostic de l'ARPU (Revenu Moyen par Utilisateur fixé à 226€) est issu de notre grille d'abonnement interne, structurée en 4 formules d'adhésion.</p>

        <div class="visual-block" style="border-color: var(--gold);">
            <div class="visual-title" style="color: var(--gold);">GRILLE TARIFAIRE HAPPY HOUSE (VILLAS & GÎTES)</div>
            <table class="gantt-table" style="width: 100%; border-collapse: collapse; color: #FFF; margin-top: 5px;">
                <tr style="background: rgba(221,168,62,0.1);">
                    <th style="width: 25%; text-align: left;">Formule</th>
                    <th style="width: 15%;">Prix HT/an</th>
                    <th style="width: 60%; text-align: left;">Services Inclus et Cible privilégiée</th>
                </tr>
                <tr>
                    <td style="color: #BCBFD0; font-weight: bold;">1. VISIBILITÉ</td>
                    <td style="text-align: center;">150 €</td>
                    <td>La porte d'entrée. Annonce sur le portail, Réservation Directe (sans commission), Label Happy House, Centrale d'achat Entegra, Service HTA à 8%.<br><em>Cible : Les petites structures et les particuliers néo-entrants (Delphine).</em></td>
                </tr>
                <tr>
                    <td style="color: #BCBFD0; font-weight: bold;">2. PREMIUM</td>
                    <td style="text-align: center;">240 €</td>
                    <td>Intègre la Version Premium de la Guest App (Relation clients et ventes additionnelles), Service HTA réduit à 5%.<br><em>Cible : Les hôtes en phase de professionnalisation (Sophie).</em></td>
                </tr>
                <tr style="background: rgba(221,168,62,0.05);">
                    <td style="color: var(--gold); font-weight: bold;">3. PRESTIGE</td>
                    <td style="text-align: center; color: var(--gold); font-weight: bold;">360 €</td>
                    <td>Ajoute la Promotion Boostée sur réseau qualifié, Expertise personnalisée annuelle, Accès partenaires réseau. Service HTA à 2%.<br><em>Cible : Les pros cherchant l'optimisation des marges (Le standard de vente).</em></td>
                </tr>
                <tr>
                    <td style="color: #BCBFD0; font-weight: bold;">4. WAOUH</td>
                    <td style="text-align: center;">540 €</td>
                    <td>L'offre faîtière. Service HTA gratuit (0% commission). Pack Human Travel Agency complet.<br><em>Cible : Les domaines de haut standing et les profils dominants (Jean-Marc).</em></td>
                </tr>
            </table>
        </div>
        
        <p style="font-size: 10pt; color: var(--text-muted); margin-top: 15px;">L'ARPU consolidé à 226€ (tel que défini dans le mémo stratégique d'alignement avec R. Marie-Luce) résulte du mix de souscription pondéré sur ces 4 offres. C'est ce plafond de revenu annuel qui condamne de facto toute tentative d'acquisition téléphonique de masse dépassant les 200€ de CPA.</p>
    \"\"\"
})
"""

# Insert pricing right after the Personas block (or before Chap 7 Retention)
c = c.replace('# PAGE 18\npages.append({', pricing_page + '\n# PAGE 18\npages.append({')


# AFTERWORK GUIDE
guide_page = """
# PAGE 21.5 : GUIDE LOGISTIQUE
pages.append({
    "section": "CHAPITRE 8 : LE GUIDE DE L'INBOUND",
    "content": \"\"\"
        <a id="chapitre-8-guide"></a>
        <h2>Le Guide Logistique de l'Afterwork Régional</h2>
        
        <p>L'Afterwork Inbound étant le "Remède" absolu à l'échec de la prospection, sa rentabilité (CPA < 200€) dépend d'une exécution logistique militaire. Voici le Manuel d'Opérations (SOP) standardisé validé pour maximiser le closing sur site.</p>

        <div class="analytic-point">Chronologie de Conversion (Le Timeline)</div>
        <div class="analytic-content" style="border-left: 2px solid #2ECC71;">
            <ul style="list-style-type: none; padding-left: 0; font-size: 10pt; line-height: 1.6;">
                <li><strong style="color: var(--gold);">19h00 : L'Accueil Réassurance.</strong> Prise en charge par l'hôte membre et l'équipe Happy House. Boissons fraîches. Désamorçage immédiat du stress commercial.</li>
                <li><strong style="color: var(--gold);">19h30 : Le Pitch d'Autorité (20 min).</strong> Présentation de l'écosystème Happy House centrée exclusivement sur les économies réalisées (Centralisation des achats Entegra).</li>
                <li><strong style="color: var(--gold);">19h50 : La Preuve Sociale (Social Proof).</strong> Le moment clé. Prise de parole de l'hôte hébergeur pour une démonstration physique de la valeur du réseau. C'est l'indépendant qui parle à l'indépendant.</li>
                <li><strong style="color: var(--gold);">20h00 : Le Networking Ciblé.</strong> Échanges libres et ciblés autour des leviers de la centrale d'achat.</li>
                <li><strong style="color: var(--gold);">20h10 : Q&A et Transparence.</strong> Session de Questions/Réponses sans filtre.</li>
                <li><strong style="color: var(--gold); font-size: 9pt;">20h20 : Le Cautionnement Local.</strong> Prise de parole des commerçants/fournisseurs partenaires de la soirée (ancrage territorial).</li>
                <li><strong style="color: var(--gold); font-size: 9pt;">20h25 : L'Art de Vivre.</strong> Intervention du vigneron (ou de moi-même en tant qu'ancien sommelier) pour la présentation des vins. Le networking de clôture s'ouvre.</li>
            </ul>
        </div>
        
        <div class="analytic-point">La Mécanique de Closing (FOMO et Remises)</div>
        <div class="analytic-content">
            Pendant l'échange convivial de fin de soirée, j'assure le passage individuel auprès des prospects pour capter les retours à chaud, identifier les derniers doutes et enclencher la phase de signature <em>in situ</em>. Pour forcer l'urgence de la décision (Biais FOMO) :
            <ul style="margin-top: 5px; font-size: 10pt;">
                <li><strong>Signature sur place :</strong> La formule "Waouh" (540€) est exceptionnellement concédée au tarif de la formule "Prestige" (360€).</li>
                <li><strong>Signature à J+7 :</strong> Maintien d'une remise de 20% sur les formules Waouh et Prestige, couplée au tirage au sort d'une Plaque Google Avis offerte.</li>
            </ul>
            <em>C'est cette ingénierie logistique ultra-paramétrée qui permet de garantir l'objectif stratégique de 3 signatures fermes par événement, sécurisant ainsi le CPA cible de 166€.</em>
        </div>
    \"\"\"
})
"""

# Insert Guide right before Chap 9 (Bilan)
c = c.replace('# PAGE 24\npages.append({', guide_page + '\n# PAGE 24\npages.append({')

with open('build_rdm_v7_mastodonte.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("V7 (Mastodonte) generated.")
