import os

def generate_text(page_num, topic):
    base_text = f"""
    <h2>Chapitre {page_num} : {topic}</h2>
    <p>
    L'analyse approfondie de {topic} révèle des enjeux cruciaux pour le développement de la stratégie Happy House dans le secteur de l'hôtellerie de prestige. 
    Il est impératif de comprendre que le marché actuel ne se contente plus de standards préétablis, mais exige une personnalisation extrême. 
    La convergence entre le digital et l'humain devient le pivot central de toute opération visant l'excellence opérationnelle. 
    En examinant les données recueillies lors des derniers audits, nous observons une tendance marquée vers l'authenticité et la quête de sens. 
    Les clients ne recherchent plus seulement un lieu de séjour, mais une expérience transformative qui résonne avec leurs valeurs personnelles. 
    Cela implique une refonte totale des processus d'accueil et de suivi, intégrant des technologies prédictives sans sacrifier la chaleur du contact humain. 
    L'optimisation des flux de revenus passe désormais par une compréhension fine des micro-segments de marché, permettant une tarification dynamique et contextuelle.
    </p>
    <p>
    La gestion opérationnelle de {topic} nécessite une rigueur exemplaire. Chaque détail compte, de la sélection des matériaux à la fluidité des interactions numériques. 
    Nous avons identifié plusieurs leviers de croissance organique qui pourraient être activés par une meilleure coordination entre les départements marketing et opérationnels. 
    La formation continue des équipes est le garant de la pérennité de cette vision. Investir dans le capital humain n'est plus une option mais une nécessité stratégique pour maintenir un avantage compétitif durable. 
    Les indicateurs de performance clés (KPI) doivent être réévalués pour inclure des mesures de satisfaction émotionnelle et de fidélité à long terme. 
    Le rapport souligne l'importance de l'agilité organisationnelle face aux fluctuations imprévues du marché mondial. 
    La résilience du modèle économique repose sur sa capacité à s'adapter rapidement aux nouvelles normes sanitaires et environnementales tout en préservant l'aura d'exclusivité propre au luxe.
    </p>
    <p>
    En outre, l'aspect technologique de {topic} ne doit pas être négligé. L'implémentation de systèmes ERP de nouvelle génération permet une synchronisation parfaite entre les réservations et les services sur site. 
    L'utilisation de la blockchain pour garantir la transparence de la chaîne d'approvisionnement des produits de luxe est une piste que nous explorons activement. 
    La cybersécurité est également au cœur de nos préoccupations, car la protection des données personnelles de nos clients VIP est primordiale. 
    Chaque interaction numérique laisse une empreinte qui, si elle est correctement analysée, peut conduire à une amélioration significative du service anticipatif. 
    Les algorithmes d'intelligence artificielle que nous déployons sont conçus pour apprendre des préférences individuelles, créant ainsi un "profil de bonheur" unique pour chaque membre du club Happy House.
    </p>
    <p>
    En conclusion de cette section sur {topic}, il apparaît clairement que l'innovation doit être au service de l'émotion. 
    L'intégration de solutions logicielles avancées permet une gestion proactive des attentes, minimisant les frictions et maximisant les moments de plaisir. 
    L'audit démontre que les établissements qui réussissent le mieux sont ceux qui parviennent à créer un lien affectif fort avec leurs hôtes. 
    Ce lien se construit à travers une multitude de micro-services souvent invisibles mais dont l'absence serait immédiatement ressentie. 
    La stratégie Happy House doit donc se concentrer sur la maîtrise de cet invisible, sur l'art de l'anticipation et sur la célébration constante de l'art de vivre. 
    Les prochaines étapes de la mission porteront sur l'implémentation concrète de ces recommandations à l'échelle du groupe, avec un calendrier de déploiement strict et des audits de suivi réguliers. 
    La vision à long terme est celle d'un leadership incontesté, fondé sur une expertise technique irréprochable et une sensibilité artistique unique dans le paysage hôtelier international.
    </p>
    """
    return base_text

topics = [
    "Introduction à l'Audit de Prestige", "Analyse des Tendances du Marché", "Comportement du Consommateur de Luxe",
    "Stratégie de Différenciation", "Optimisation de l'Expérience Client", "Gestion du Capital Humain",
    "Digitalisation et Haute Technologie", "Développement Durable et RSE", "Marketing d'Influence et Réputation",
    "Ingénierie Financière en Hôtellerie", "Design et Architecture d'Intérieur", "Gastronomie et Art de la Table",
    "Wellness et Spa de Luxe", "Conciergerie et Services sur Mesure", "Gestion de Crise et Résilience",
    "Expansion Internationale et Localisation", "Programmes de Fidélité Elite", "Sécurité et Confidentialité",
    "Logistique et Chaîne d'Approvisionnement", "Intelligence Artificielle et Prédictivité", "Événementiel et MICE de Prestige",
    "Analyse de la Concurrence", "Gouvernance et Éthique des Affaires", "Transformation Digitale des Processus",
    "Psychologie du Luxe", "Art de Recevoir et Étiquette", "Gestion des Actifs Immobiliers",
    "Innovation et Recherche de Concept", "Partenariats Stratégiques", "Branding et Identité Visuelle",
    "Data Analytics et Big Data", "Cyber-sécurité des Données Clients", "Rituels de Service Exceptionnels",
    "Analyse de la Valeur Vie Client", "Marketing Sensoriel", "Management de l'Excellence",
    "Prospection et Développement Commercial", "Audit des Coûts Opérationnels", "Stratégies de Yield Management",
    "Impact de la Globalisation", "Tourisme Régénératif", "Hôtellerie de Demain",
    "Expérience Immersion Culturelle", "Gestion de la Qualité Totale", "Leadership et Vision Stratégique",
    "Conclusion de l'Audit Phase 1", "Recommandations Prioritaires", "Plan d'Action 2025-2026"
]

html_start = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RDM MASTER 50P - Happy House</title>
    <style>
        :root {
            --bg: #000000;
            --accent: #D4AF37;
            --text: #FFFFFF;
            --page-w: 210mm;
            --page-h: 297mm;
        }
        @media print {
            @page { size: A4; margin: 0; }
            body { background: var(--bg) !important; }
            .page { margin: 0 !important; border: none !important; box-shadow: none !important; }
        }
        body { background: #111; color: var(--text); font-family: Arial, sans-serif; font-size: 12pt; margin: 0; counter-reset: page; line-height: 1.5; }
        .page {
            width: var(--page-w);
            height: var(--page-h);
            background: var(--bg);
            margin: 40px auto;
            position: relative;
            padding: 25mm 20mm;
            box-sizing: border-box;
            box-shadow: 0 0 30px rgba(0,0,0,0.8);
            page-break-after: always;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        .inner-border {
            position: absolute; top: 10mm; left: 10mm; right: 10mm; bottom: 10mm;
            border: 2px solid var(--accent); pointer-events: none;
        }
        h1 { font-size: 3rem; color: var(--accent); text-align: center; margin-top: 50mm; margin-bottom: 20mm; text-transform: uppercase; border-bottom: 2px solid var(--accent); padding-bottom: 10px; }
        h2 { color: var(--accent); border-left: 10px solid var(--accent); padding-left: 20px; margin: 30px 0; font-size: 1.8rem; text-transform: uppercase; }
        .content { flex-grow: 1; text-align: justify; }
        .footer {
            border-top: 1px solid var(--accent); padding-top: 5mm;
            display: flex; justify-content: space-between; font-size: 10pt; color: var(--accent);
        }
        .page-num::after { counter-increment: page; content: "Page " counter(page); }
        .sommaire { font-size: 1.2rem; }
        .sommaire-item { display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px dotted var(--accent); }
    </style>
</head>
<body>
"""

pages_html = []

# Page 1: Garde
pages_html.append(f"""
<div class="page" id="p01">
    <div class="inner-border"></div>
    <div style="text-align:center; margin-top:20mm; font-size:1.5rem; color:var(--accent);">MISSION DE CONSEIL STRATÉGIQUE</div>
    <h1>RAPPORT DE MISSION MASTER</h1>
    <div style="text-align:center; font-size:2rem; margin-top:10mm;">HAPPY HOUSE</div>
    <div style="text-align:center; margin-top:50mm; font-size:1.2rem;">
        <p>Présenté par : Julien FLORENCE</p>
        <p>Date : Novembre 2025</p>
        <p>Version : 5.0 - ULTRA PRESTIGE</p>
    </div>
    <div class="footer" style="margin-top:auto;">
        <div>HAPPY HOUSE CONSULTING</div>
        <div class="page-num"></div>
    </div>
</div>
""")

# Page 2: Sommaire
sommaire_items = "".join([f'<div class="sommaire-item"><span>{t}</span><span>P.{i+3:02d}</span></div>' for i, t in enumerate(topics)])
pages_html.append(f"""
<div class="page" id="p02">
    <div class="inner-border"></div>
    <h2 style="text-align:center; border-left:none;">SOMMAIRE GÉNÉRAL</h2>
    <div class="content sommaire">
        {sommaire_items}
    </div>
    <div class="footer">
        <div>CONFIDENTIEL - HAPPY HOUSE</div>
        <div class="page-num"></div>
    </div>
</div>
""")

# Pages 3-50: Content
for i, topic in enumerate(topics):
    page_content = generate_text(i + 1, topic)
    pages_html.append(f"""
<div class="page" id="p{i+3:02d}">
    <div class="inner-border"></div>
    <div class="content">
        {page_content}
    </div>
    <div class="footer">
        <div>RAPPORT DE MISSION MASTER - HAPPY HOUSE</div>
        <div class="page-num"></div>
    </div>
</div>
""")

html_end = """
</body>
</html>
"""

with open("RDM_MASTER_50P.html", "w", encoding="utf-8") as f:
    f.write(html_start)
    for p in pages_html:
        f.write(p)
    f.write(html_end)

print(f"File generated: {os.path.getsize('RDM_MASTER_50P.html')} bytes")
