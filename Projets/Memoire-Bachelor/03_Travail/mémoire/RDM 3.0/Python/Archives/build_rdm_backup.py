import os

html_head = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAPPORT DE MISSION 2026 - JULIEN FLORENCE - ÉDITION PRESTIGE</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #DDA83E;
            --gold-light: #BCBFD0;
            --deep-blue: #0F163D;
            --bg-dark: #0A0C1A;
            --glass: rgba(255, 255, 255, 0.03);
            --border-glass: rgba(221, 168, 62, 0.2);
            --text-main: rgba(255, 255, 255, 0.92);
        }

        @page { size: A4; margin: 0; }
        * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }

        body {
            margin: 0; padding: 0;
            background-color: #1a1a1a;
            color: var(--text-main);
            font-family: 'Arial', sans-serif;
            font-size: 11.5pt; line-height: 1.5;
            text-align: justify;
        }

        .page {
            width: 210mm; height: 297mm;
            margin: 20px auto; background-color: var(--bg-dark);
            position: relative; overflow: hidden;
            display: flex; flex-direction: column;
            box-shadow: 0 0 50px rgba(0,0,0,0.5);
            page-break-after: always;
        }

        @media print {
            body { background: none; }
            .page { margin: 0; box-shadow: none; }
        }

        .page::before {
            content: ''; position: absolute;
            top: 10mm; left: 10mm; right: 10mm; bottom: 10mm;
            border: 1px solid var(--border-glass);
            pointer-events: none; z-index: 1;
        }

        .corner { position: absolute; width: 15mm; height: 15mm; border: 2px solid var(--gold); z-index: 2; }
        .top-left { top: 8mm; left: 8mm; border-right: none; border-bottom: none; }
        .top-right { top: 8mm; right: 8mm; border-left: none; border-bottom: none; }
        .bottom-left { bottom: 8mm; left: 8mm; border-right: none; border-top: none; }
        .bottom-right { bottom: 8mm; right: 8mm; border-left: none; border-top: none; }

        .content { padding: 25mm 20mm; position: relative; z-index: 10; flex-grow: 1; }

        h1 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 24pt; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 25px; text-align: center; font-weight: 900; }
        h2 { font-family: 'Cinzel', serif; color: var(--gold-light); font-size: 16pt; border-left: 4px solid var(--gold); padding-left: 15px; margin: 30px 0 15px 0; text-transform: uppercase; letter-spacing: 2px; }
        h3 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 13pt; margin: 20px 0 10px 0; }
        p { margin-bottom: 15px; }

        .glass-card { background: var(--glass); backdrop-filter: blur(10px); border: 1px solid var(--border-glass); padding: 20px; border-radius: 4px; margin: 20px 0; position: relative; }
        .glass-card::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, var(--gold), transparent); }

        .footer { position: absolute; bottom: 10mm; left: 20mm; right: 20mm; display: flex; justify-content: space-between; align-items: center; font-family: 'Cinzel', serif; font-size: 7.5pt; color: var(--gold); letter-spacing: 2px; z-index: 100; }
        .page-number { font-weight: 700; }

        .cover { justify-content: center; align-items: center; text-align: center; background-color: #0A0C1A; position: relative; }
        .cover-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; background-image: url('charte graphique/cover_vignoble.jpg'); background-size: cover; background-position: center; opacity: 0.25; filter: grayscale(50%); }
        .cover-content { position: relative; z-index: 10; width: 100%; height: 100%; padding: 25mm 20mm; display: flex; flex-direction: column; justify-content: space-between; }
        .tagline { font-family: 'Cinzel', serif; font-size: 12pt; color: var(--gold); letter-spacing: 8px; margin-bottom: 10px; }
        .main-title { font-size: 36pt; line-height: 1.1; margin: 20px 0; }
        .author-box { margin-top: 60px; font-family: 'Cinzel', serif; }
        .author-name { font-size: 22pt; font-weight: 900; letter-spacing: 4px; color: #FFFFFF; }
        .author-role { color: var(--gold); font-size: 10pt; text-transform: uppercase; letter-spacing: 2px; }

        table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 9pt; }
        th { background: rgba(221, 168, 62, 0.1); color: var(--gold); font-family: 'Cinzel', serif; padding: 10px; border: 1px solid var(--border-glass); text-align: left; }
        td { padding: 10px; border: 1px solid var(--border-glass); background: rgba(255,255,255,0.01); color: #fff; vertical-align: top;}

        .expert-note { border-left: 4px solid var(--gold); background: rgba(221, 168, 62, 0.05); padding: 15px; margin: 15px 0; font-style: italic; color: var(--gold-light); }
        .expert-note strong { display: block; font-family: 'Cinzel', serif; font-style: normal; color: var(--gold); margin-bottom: 5px; font-size: 9pt; }

        a { text-decoration: none; color: #DDA83E; display: block; }
        a.inline-link { display: inline; border-bottom: 1px dotted #DDA83E; }
        
        .btn-nav { display: inline-block; padding: 10px 20px; border: 2px solid #DDA83E; color: #DDA83E; font-family: 'Cinzel', serif; font-size: 10pt; letter-spacing: 2px; background: #0A0C1A; cursor: pointer; text-align: center; }

        .toc-link { width: 100%; padding: 8px 0; border-bottom: 1px solid #222; color: #FFFFFF; font-size: 10pt;}
        .toc-link:hover { color: #DDA83E; }
        
        ul { padding-left: 20px; margin-top: 5px; margin-bottom: 15px;}
        li { margin-bottom: 6px; }

        /* Visuels in-text */
        .visual-block { background: #05060A; border: 1px solid var(--border-glass); border-radius: 4px; padding: 15px; font-family: 'Courier New', Courier, monospace; font-size: 8pt; color: #DDA83E; overflow-x: hidden; margin: 20px 0; position: relative;}
        .visual-block::before { content: '/// ROCKET SCHOOL DATA VIEW ///'; position: absolute; top: 0; right: 0; background: rgba(221, 168, 62, 0.1); padding: 2px 10px; font-size: 6pt; color: var(--gold); font-family: 'Cinzel';}
        .visual-title { color: #FFFFFF; font-family: 'Cinzel', serif; font-size: 10pt; margin-bottom: 15px; border-bottom: 1px solid var(--border-glass); padding-bottom: 5px; display: inline-block; letter-spacing: 1px;}
        .gantt-table th { font-size: 7pt; text-align: center; padding: 5px; border: 1px solid #333; }
        .gantt-table td { font-size: 7.5pt; padding: 5px; border: 1px solid #333;}
        .gantt-active { background: rgba(221, 168, 62, 0.7) !important; color: #000; text-align: center; font-weight: bold; }
        .gantt-semi { background: rgba(221, 168, 62, 0.3) !important; }
        
        .code-line { display: block; margin-bottom: 4px; color: #A9B7C6; }
        .code-keyword { color: #E74C3C; font-weight: bold;}
        .code-string { color: #2ECC71; }
        .code-comment { color: #666; font-style: italic;}
    </style>
</head>
<body>
"""

pages = []

# --- PAGE 1 : COVER ---
pages.append({
    "section": "COUVERTURE",
    "content": """
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 40px;">
            <img src="charte graphique/image Happy House.png" alt="Logo Happy House" style="height: 60px;">
            <img src="charte graphique/rocket logo 2.png" alt="Logo Rocket School" style="height: 50px;">
        </div>

        <div class="tagline" style="color: #DDA83E; text-align: center;">CONSULTING STRATÉGIQUE</div>
        <h1 class="main-title" style="color: #DDA83E; text-align: center; margin-bottom: 10px;">RAPPORT DE MISSION<br>STRATÉGIQUE 2026</h1>
        <div style="width: 100px; height: 3px; background: #DDA83E; margin: 20px auto 30px auto;"></div>

        <div class="author-box" style="text-align: center; margin-top: 20px;">
            <div class="author-name" style="color: #FFFFFF;">JULIEN FLORENCE</div>
            <div class="author-role" style="color: #DDA83E;">Directeur du Développement Stratégique</div>
            <div style="margin-top: 15px; font-size: 9pt; color: #888;">PROMOTION A150 — ANNÉE 2025-2026</div>
        </div>
    """,
    "is_cover": True
})

# --- PAGE 2 : SOMMAIRE ---
sommaire_html = """
    <h1 style="color: #DDA83E; text-align: center;">Sommaire Stratégique</h1>
    <div style="margin-top: 30px;">
"""
chapitres = [
    ("REMERCIEMENTS", 4),
    ("LEXIQUE, ACRONYMES ET SOURCES", 5),
    ("I. VISION STRATÉGIQUE (Chapitre 1)", 7),
    ("II. DIAGNOSTIC EXTERNE (Chapitre 2)", 10),
    ("III. AUDIT INTERNE & ATTRITION (Chapitre 3)", 13),
    ("IV. CHOIX D'ACQUISITION & PIVOT (Chapitre 4)", 16),
    ("V. CONFRONTATION AU TERRAIN (Chapitre 5)", 20),
    ("VI. RÉTENTION & PREUVE DE VALEUR (Chapitre 6)", 23),
    ("VII. PLAN D'ACTION & BILAN (Chapitre 7)", 26),
    ("VIII. CONFORMITÉ IA (Chapitre 8)", 30),
    ("IX. INDEX DES ANNEXES", 31)
]
for titre, page_cible in chapitres:
    sommaire_html += f"""
        <a href="#page-{page_cible}" class="toc-link">
            <table style="width: 100%; border: none; margin: 0;"><tr>
                <td style="border: none; padding: 0; color: #FFFFFF;">{titre}</td>
                <td style="border: none; padding: 0; text-align: right; color: #DDA83E;">{page_cible:02d}</td>
            </tr></table>
        </a>
    """
sommaire_html += """
    </div>
"""
pages.append({"section": "SOMMAIRE", "content": sommaire_html})
pages.append({"section": "NOTE DE LECTURE", "content": "<h1 style='color:#DDA83E; text-align:center;'>Note de Lecture</h1><p>Ce document a été optimisé pour une lecture numérique (interactivité des liens) et pour l'impression A4. Les annexes volumineuses ont été déportées sur des espaces sécurisés (Cloud) accessibles via les hyperliens fournis en fin de document.</p>"})


# --- PAGE 4 : REMERCIEMENTS ---
pages.append({
    "section": "REMERCIEMENTS",
    "content": """
        <h1>Remerciements</h1>
        <p>Je tiens en premier lieu à remercier sincèrement l'équipe pédagogique et le corps professoral de <strong>Rocket School</strong>. La qualité des enseignements, la pertinence des modules de Growth Hacking et la rigueur de l'accompagnement m'ont permis de transformer une expérience de terrain en une véritable posture de Responsable Stratégique.</p>
        <p>Mes remerciements s'adressent également à la direction et aux équipes de <strong>Happy House</strong>. Je remercie particulièrement Patrice Kermarrec de m'avoir accordé sa confiance. Ce terrain de jeu entrepreneurial a été une opportunité inestimable d'être confronté à la réalité d'une entreprise : devoir composer entre l'ambition d'innovation et les contraintes inhérentes à la gouvernance d'une organisation.</p>
        <p>Enfin, je souhaite exprimer ma reconnaissance envers <strong>Ruddy</strong>, avec qui nous avons éprouvé et prototypé l'infrastructure de données, ainsi qu'envers <strong>Younes</strong>, le SDR avec qui la collaboration a été aussi formatrice sur le plan managérial que décisive sur le plan commercial.</p>
    """
})

# --- PAGE 5-6 : LEXIQUE ---
pages.append({
    "section": "LEXIQUE & SOURCES",
    "content": """
        <h1>Lexique et Sources</h1>
        <h2>Sigles et Acronymes</h2>
        <ul>
            <li><strong>AE (Account Executive) :</strong> Commercial en charge de la finalisation de la vente et de la signature des contrats.</li>
            <li><strong>B2B (Business to Business) :</strong> Vente adressée aux professionnels (les hébergeurs).</li>
            <li><strong>CAC (Coût d'Acquisition Client) :</strong> Montant total moyen dépensé pour acquérir un nouveau membre.</li>
            <li><strong>Churn (Taux d'attrition) :</strong> Proportion de clients perdus sur une période donnée.</li>
            <li><strong>POC (Proof of Concept) :</strong> Maquette ou réalisation expérimentale visant à prouver la faisabilité d'un modèle.</li>
            <li><strong>LTV (Lifetime Value) :</strong> Revenu total généré par un membre sur sa durée de vie au sein du réseau.</li>
            <li><strong>OTA (Online Travel Agency) :</strong> Agence de voyage en ligne (ex: Booking.com, Airbnb) agissant comme intermédiaire.</li>
            <li><strong>SDR (Sales Development Representative) :</strong> Commercial spécialisé dans la pré-qualification des prospects.</li>
        </ul>
    """
})
pages.append({
    "section": "LEXIQUE & SOURCES (SUITE)",
    "content": """
        <h2>Sources de Données et Références</h2>
        <p>L'ensemble du rapport repose sur des données empiriques récoltées sur le terrain, croisées avec des données de marché pour assurer la robustesse du diagnostic.</p>
        <ul>
            <li><strong>Sources Internes :</strong> Historique du parc réseau (150 hébergeurs), bilans comptables liés à la centrale d'achat Entegra, comptabilité analytique de cas d'usage (ex: Durentie).</li>
            <li><strong>Notes Méthodologiques :</strong> Face aux contraintes d'accès pour des audits automatisés, les données internes (comme le taux de Churn) ont été reconstruites à partir de la base de facturation historique, garantissant un ancrage factuel tout en tenant compte de marges d'erreur inhérentes à l'extrapolation manuelle.</li>
            <li><strong>Sources Externes :</strong> Rapports de la DGE (Direction Générale des Entreprises) sur la réglementation des Hôtels de Tourisme, analyses sectorielles MKG Consulting, et données macro-économiques de la Banque des Territoires.</li>
        </ul>
    """
})

# --- CHAPITRE 1 : INTRODUCTION ---
pages.append({
    "section": "CHAPITRE 1 : INTRODUCTION",
    "content": """
        <h1>Chapitre 1 — Introduction et problématique</h1>
        <p>Le secteur de l’hébergement indépendant haut de gamme connaît une transformation profonde, marquée à la fois par l’évolution des attentes des clients, le renforcement des exigences réglementaires et la montée en puissance des outils digitaux. Dans ce contexte, les établissements doivent préserver leur singularité tout en structurant davantage leur organisation, leur distribution et leur performance commerciale.</p>
        <p>C’est dans cet environnement que s’inscrit la mission réalisée au sein de Happy House, un réseau spécialisé dans l’accompagnement d’établissements indépendants positionnés sur le segment premium et de charme. L’entreprise intervient sur plusieurs leviers : optimisation de la distribution, acquisition commerciale, performance opérationnelle et amélioration de l’expérience client.</p>

        <h2>Tension observée</h2>
        <p>Au cours de cette alternance, une tension centrale est apparue entre, d’une part, un mode de fonctionnement historique fondé sur la proximité relationnelle et, d’autre part, la nécessité de structurer davantage les processus commerciaux et le pilotage de la performance. Cette tension ne renvoie pas seulement à un manque d’outils, mais à un besoin plus large de formalisation, de mesure et de fidélisation.</p>
    """
})
pages.append({
    "section": "CHAPITRE 1 : INTRODUCTION",
    "content": """
        <h2>Problématique</h2>
        <div class="glass-card" style="border: 2px solid var(--gold);">
            <p style="font-size: 12pt; font-weight: 600; color: var(--gold); text-align: justify; line-height: 1.5; margin:0;">
                Comment Happy House peut-elle améliorer la rétention de ses membres et renforcer la rentabilité de son réseau tout en adaptant sa stratégie d’acquisition aux contraintes internes et à son positionnement premium ?
            </p>
        </div>
        <p>Cette problématique a été choisie car elle relie directement les enjeux de croissance, de fidélisation et de rentabilité, tout en restant ancrée dans les réalités de l’entreprise. Elle permet également d’articuler une analyse externe du marché avec un diagnostic interne des forces et des limites du réseau.</p>

        <h2>Démarche adoptée</h2>
        <p>L’hypothèse de départ était qu’une automatisation technologique forte pouvait réduire le coût d’acquisition et améliorer l’efficacité commerciale. Toutefois, les contraintes rencontrées en interne ont conduit à faire évoluer cette hypothèse vers une approche plus réaliste, combinant des outils de preuve de valeur, une stratégie d’acquisition plus qualitative et un renforcement de la rétention.</p>
        <p>Cette évolution de la démarche montre que la valeur d’une analyse stratégique ne réside pas uniquement dans la qualité de ses outils, mais aussi dans la capacité à adapter les recommandations au contexte réel de l’entreprise.</p>
    """
})
pages.append({
    "section": "CHAPITRE 1 : INTRODUCTION",
    "content": """
        <div class="expert-note">
            <strong>Transition vers le chapitre 2</strong><br>
            Afin de mieux comprendre les leviers d’action disponibles, il convient d’abord d’analyser l’environnement externe de l’entreprise. Cette lecture du marché permettra d’identifier les tendances, les contraintes et les opportunités susceptibles d’influencer la stratégie de Happy House.
        </div>
    """
})

# --- CHAPITRE 2 : DIAGNOSTIC EXTERNE ---
pages.append({
    "section": "CHAPITRE 2 : DIAGNOSTIC EXTERNE",
    "content": """
        <h1>Chapitre 2 — Diagnostic externe</h1>
        <p>L’analyse de l’environnement externe permet d’identifier les forces macro-économiques qui influencent directement l’activité de Happy House. Dans le cas d’un réseau positionné sur l’hébergement indépendant premium, cette lecture objectivée par les données est indispensable pour comprendre les opportunités à saisir et les contraintes qui pèsent sur les exploitants.</p>

        <h2>Un marché sous domination numérique</h2>
        <p>Le marché de l’hébergement indépendant est caractérisé par une hégémonie croissante des intermédiaires digitaux. Les OTAs (Online Travel Agencies telles que Booking.com ou Airbnb) se sont imposées comme le canal de distribution par défaut. Selon les données sectorielles de 2024, <strong>les OTAs captent 71 % des nuitées en meublés de tourisme</strong>, ne laissant que 29 % aux réservations directes. De plus, un acteur comme Booking.com centralise à lui seul près de 70 % des réservations hôtelières en ligne en France.</p>
        <p>Pour Happy House, cet environnement de quasi-monopole constitue à la fois un risque (compression des marges due aux commissions de 15 % à 25 %) et une opportunité majeure : proposer aux indépendants une architecture de reconquête de leur souveraineté commerciale (objectif de ramener le mix OTA sous les 35 %).</p>
    """
})
pages.append({
    "section": "CHAPITRE 2 : DIAGNOSTIC EXTERNE",
    "content": """
        <h2>Pression réglementaire : L'effet de purge du DPE</h2>
        <p>L’environnement légal évolue drastiquement avec l'application de la "Loi anti-Airbnb". Depuis le 1er janvier 2025, la location de logements classés G au DPE (Diagnostic de Performance Énergétique) est interdite, une mesure qui s'étendra aux logements classés F en 2028 (sous peine de 5 000 € d'amende).</p>
        
        <p>L'analyse stratégique de cette contrainte indique qu'<strong>environ 20 % à 25 % des loueurs amateurs pourraient être contraints de quitter le marché</strong> à moyen terme (selon la représentativité des passoires thermiques dans le parc immobilier français). Cette "purge" réglementaire réduit la concurrence déloyale pour notre cible (les hébergeurs professionnels premium), mais exige de ces derniers une capacité d'investissement et d'adaptation accrue, renforçant leur besoin d'accompagnement réseau <em>(Cf. Annexe 1 : Matrice PESTEL)</em>.</p>

        <h2>L'inflation opérationnelle : L'urgence de la mutualisation</h2>
        <p>Le dernier facteur macro-économique critique concerne la structure des coûts. En 2024, le secteur hôtelier a subi une <strong>hausse brutale de 15 % de ses factures d'électricité</strong>, cumulée à une inflation globale du secteur hébergement-restauration de +3,1 %. Face à cette érosion des marges, la promesse d'une centrale d'achats mutualisée n'est plus un simple "bonus", mais un impératif de survie.</p>
    """
})
pages.append({
    "section": "CHAPITRE 2 : DIAGNOSTIC EXTERNE",
    "content": """
        <h2>Conclusion du diagnostic externe</h2>
        <p>Au final, le marché offre des opportunités historiques à Happy House. L'inflation des coûts pousse vers la mutualisation, et la complexité réglementaire comme technologique force l'indépendant à chercher un encadrement. L’enjeu n’est donc pas uniquement externe : il dépend de la capacité interne de l’entreprise à capter et à traduire ces signaux de marché en une offre d'accompagnement lisible.</p>

        <div class="expert-note">
            <strong>Transition vers le chapitre 3</strong><br>
            Après avoir objectivé l’environnement de marché par ces données sectorielles, il est nécessaire d’analyser les ressources et les limites propres à Happy House. Cette étape permettra de confronter ces opportunités (souveraineté, mutualisation) à la réalité interne du réseau et de comprendre pourquoi, historiquement, l'entreprise a peiné à fidéliser ses membres malgré un produit pertinent.
        </div>
    """
})

# --- CHAPITRE 3 : DIAGNOSTIC INTERNE & CHURN ---
pages.append({
    "section": "CHAPITRE 3 : AUDIT INTERNE",
    "content": """
        <h1>Chapitre 3 — Audit interne et analyse de l'attrition</h1>
        <p>L’analyse interne a pour objectif d’évaluer la capacité opérationnelle de Happy House à répondre aux enjeux de son marché. Il s'agit d'identifier les actifs stratégiques de l’entreprise tout en mesurant avec objectivité ses fragilités, notamment en matière de fidélisation de la clientèle.</p>

        <h2>Identification des ressources stratégiques</h2>
        <p>Happy House s’appuie sur plusieurs forces notables. La première réside dans son expertise sectorielle et son positionnement d’accompagnateur de proximité. La seconde est d'ordre financier : le partenariat avec la centrale d’achat Entegra, qui offre aux membres un levier puissant d'optimisation des coûts (gains moyens de marge opérationnelle mesurés entre 15 % et 25 % sur les postes liés à l'exploitation).</p>
        <p>Enfin, l'entreprise dispose d'un actif informationnel significatif : une base de prospection de 126 000 contacts qualifiés, structurée en interne. Cet actif représente un potentiel d'acquisition important, à condition de déployer les processus adéquats pour l'exploiter rationnellement.</p>
    """
})
pages.append({
    "section": "CHAPITRE 3 : AUDIT INTERNE",
    "content": """
        <h2>Analyse de l'attrition (Churn) et limites de la méthode</h2>
        <p>Si la capacité d'acquisition est soutenue par l'actif de données, l'audit interne a souligné une difficulté majeure dans la rétention des membres. L'évaluation de ce taux d'attrition a nécessité une approche méthodologique prudente.</p>
        
        <p>En l'absence de processus automatisé de sondage des anciens clients — une démarche d'audit non validée par la direction à ce stade —, les données ont été reconstruites à partir d'un fichier historique de la gouvernance et de la base de facturation de l'entreprise. Sur un parc de 150 hébergeurs, le contact a été perdu avec environ 80 % d'entre eux. Bien que ce chiffre brut intègre probablement des cessations d'activité (liées à la conjoncture ou aux contraintes réglementaires) et ne puisse être attribué exclusivement à une insatisfaction de service, il traduit de manière globale un défaut systémique de suivi relationnel dans la durée.</p>
        
        <div class="visual-block">
            <div class="visual-title">NOTE MÉTHODOLOGIQUE : MESURE DU CHURN</div>
            <div class="code-line">L'analyse repose sur le croisement de la base de facturation historique.</div>
            <div class="code-line">- Échantillon global étudié : 150 comptes historiques.</div>
            <div class="code-line">- Taux d'attrition brut (perte de contact) : ~80% (120 domaines).</div>
            <div class="code-line">- Limite de l'analyse : Impossibilité de distinguer précisément les fermetures d'établissements des désabonnements volontaires, justifiant une approche de projection prudente sur la frange active.</div>
        </div>
    """
})
pages.append({
    "section": "CHAPITRE 3 : AUDIT INTERNE",
    "content": """
        <h2>Interprétation des données d'attrition</h2>
        <p>L'analyse des retours qualitatifs recueillis auprès d'un échantillon actif et d'anciens membres suggère que la cause principale de départ n'est pas l'insatisfaction liée au service technique, mais un manque de lisibilité du retour sur investissement (ROI). L’absence de suivi régulier et de tableaux de bord objectivant les économies réalisées limite la perception de la valeur par l'adhérent, rendant le renouvellement de la cotisation incertain.</p>

        <h2>Conclusion de l'audit interne</h2>
        <p>Le diagnostic interne met en évidence que le principal frein à la croissance durable du réseau ne se situe pas dans le modèle économique lui-même, mais dans la transmission et la mesure de sa valeur. L'acquisition de nouveaux membres doit impérativement s'accompagner d'une structuration forte de la post-acquisition.</p>

        <div class="expert-note">
            <strong>Transition vers le chapitre 4</strong><br>
            Le diagnostic interne révèle que la difficulté principale ne réside pas seulement dans l’acquisition, mais aussi dans la capacité de l’entreprise à traduire sa valeur en bénéfices visibles pour ses membres. Dans ce contexte, il devient nécessaire d’évaluer les solutions initialement envisagées, puis d’expliquer pourquoi un ajustement stratégique s’impose face aux contraintes réelles de l’organisation.
        </div>
    """
})

# --- CHAPITRE 4 : LE PIVOT ---
pages.append({
    "section": "CHAPITRE 4 : CHOIX D'ACQUISITION",
    "content": """
        <h1>Chapitre 4 — Choix d'acquisition et pivot stratégique</h1>
        <p>Face à la nécessité de réduire le coût d'acquisition client (CAC) et d'améliorer l'efficience commerciale, une première réflexion a été menée autour de l'automatisation des processus. Ce chapitre expose cette démarche initiale, les arbitrages qui ont suivi, et la réorientation de la stratégie vers un modèle de sélection premium, adapté aux exigences de la direction.</p>

        <h2>L'hypothèse initiale : l'automatisation par la donnée</h2>
        <p>L'analyse des méthodes d'acquisition historiques a montré que la prospection téléphonique à froid (Cold Calling) mobilisait un temps considérable pour des résultats limités, générant un coût d'acquisition pénalisant la rentabilité de la première année d'adhésion. L'hypothèse de travail initiale consistait donc à rationaliser cet effort en s'appuyant sur l'outil d'automatisation n8n.</p>
        
        <p>L'objectif de ce prototype était de pré-qualifier la base de 126 000 contacts. Le flux technique prévoyait un filtrage des coordonnées, un enrichissement via des bases de données publiques, suivi de campagnes d'emailing informatives. Le modèle prévoyait que la force de vente n'intervienne qu'auprès de prospects ayant manifesté un premier signal d'intérêt (ouvertures répétées d'emails), réduisant ainsi la friction de la prise de contact initiale.</p>
    """
})
pages.append({
    "section": "CHAPITRE 4 : CHOIX D'ACQUISITION",
    "content": """
        <h2>Le blocage interne et l'ajustement nécessaire</h2>
        <p>Bien que ce scénario d'automatisation présentât un intérêt financier théorique en rationalisant le temps de prospection, son déploiement a été invalidé par la direction lors de sa présentation. La gouvernance de Happy House a estimé que l'utilisation de campagnes d'emailing sortantes (Cold Emailing) présentait un risque pour le positionnement de la marque, craignant une assimilation à du démarchage automatisé de masse, incompatible avec l'image "premium" recherchée.</p>
        
        <p>Cette décision constitue un élément structurant de la mission de conseil : la pertinence d'une solution technique doit toujours être évaluée et ajustée à l'aune de la culture de l'entreprise cliente et de sa politique de marque.</p>

        <h2>Le pivot : vers une acquisition événementielle</h2>
        <p>L’hypothèse initiale d’automatisation sortante a donc été abandonnée. Ce blocage a conduit à redéfinir la stratégie d'acquisition vers un modèle "Inbound" et événementiel. L'effort d'acquisition a été réalloué vers la création de points de rencontre plus qualitatifs.</p>
    """
})
pages.append({
    "section": "CHAPITRE 4 : CHOIX D'ACQUISITION",
    "content": """
        <p>La nouvelle stratégie repose sur un cycle de vente qualifié de "sélection", articulé autour de webinaires thématiques (répondant aux problématiques réglementaires) et d'Afterworks régionaux. Cette approche vise à réunir des prospects ciblés dans un environnement valorisant, souvent au sein d'un établissement déjà membre, permettant de s'appuyer sur la preuve sociale et l'échange entre pairs plutôt que sur une démarche commerciale directe.</p>

        <div class="visual-block">
            <div class="visual-title">SYNTHÈSE DE L'ARBITRAGE STRATÉGIQUE</div>
            <div class="code-line"><strong>Modèle A (Proposé) :</strong> Outbound Massif (Automatisation + Cold Email).</div>
            <div class="code-line">-> <em>Invalidé par la direction (Risque perçu sur l'image de marque).</em></div>
            <div class="code-line"><strong>Modèle B (Retenu) :</strong> Inbound & Événementiel Premium (Réseautage qualifié).</div>
            <div class="code-line">-> <em>Implication : Le budget d'acquisition se déplace de l'outil technique vers l'organisation et la logistique d'événements physiques.</em></div>
        </div>

        <div class="expert-note">
            <strong>Transition vers le chapitre 5</strong><br>
            Au-delà du diagnostic interne et de ce pivot stratégique vers l'événementiel, il est important de confronter ces orientations à la réalité du terrain et aux retours des membres. Cette confrontation permet de vérifier si ce modèle qualitatif répond véritablement aux attentes, aux usages et aux freins exprimés par la cible.
        </div>
    """
})

# --- CHAPITRE 5 : RECHERCHE TERRAIN ---
pages.append({
    "section": "CHAPITRE 5 : RECHERCHE TERRAIN",
    "content": """
        <h1>Chapitre 5 — Confrontation au terrain et analyse des usages</h1>
        <p>Pour s'assurer de l'adéquation de la nouvelle stratégie d'acquisition et de la nécessité de structurer la fidélisation, une phase d'écoute terrain a été conduite. L'objectif est d'identifier formellement les leviers d'adhésion et les points de friction opérationnels des exploitants indépendants au quotidien.</p>

        <h2>Méthodologie de la collecte d'informations</h2>
        <p>Les retours terrain proviennent d’échanges non directifs répétés avec un panel de plus de 30 hôtes et prospects, menés lors d’appels téléphoniques, d'interactions post-webinaires et de visites sur site. La récurrence des thématiques abordées permet de dégager des signaux faibles solides, représentatifs des préoccupations du segment de l'hébergement de charme.</p>
        
        <div class="visual-block" style="border-color: #DDA83E;">
            <div class="visual-title">NOTE MÉTHODOLOGIQUE : LIMITES ET BIAIS DE L'ÉCHANTILLON</div>
            <div class="code-line">- <strong>Volume :</strong> Panel qualitatif de ~30 acteurs de l'hébergement indépendant premium.</div>
            <div class="code-line">- <strong>Biais d'auto-sélection :</strong> Les interlocuteurs ayant accepté l'échange présentaient déjà une réceptivité aux enjeux de distribution. Les résultats reflètent donc les attentes d'exploitants en phase de "prise de conscience", justifiant une interprétation prudente quant à leur généralisation à l'ensemble du marché passif.</div>
        </div>
    """
})
pages.append({
    "section": "CHAPITRE 5 : RECHERCHE TERRAIN",
    "content": """
        <h2>Identification des préoccupations dominantes</h2>
        <p>L'analyse des retours d'usage met en lumière deux thématiques structurelles :</p>
        
        <ul>
            <li><strong>Le besoin d'accompagnement managérial :</strong> Les exploitants expriment fréquemment le sentiment d'isolement décisionnel. Devoir gérer simultanément les problématiques opérationnelles et les enjeux de stratégie de distribution génère une charge mentale importante. Cette observation conforte la pertinence d'un réseau offrant un cadre d'échange entre pairs et un rôle de conseil externe.</li>
            <li><strong>La saturation face aux sollicitations numériques :</strong> Un grand nombre d'interlocuteurs témoignent d'une fatigue face au volume de démarchage commercial et à la complexité des solutions logicielles qui leur sont proposées. Une solution perçue comme ajoutant un niveau de complexité dans leur gestion quotidienne engendre un rejet, indépendamment de ses bénéfices théoriques.</li>
        </ul>
        <p><em>[Pour le détail de l'intégration de cette psychologie dans le discours commercial, consulter l'Annexe 6 : Script Cold Calling et Profilage].</em></p>
    """
})
pages.append({
    "section": "CHAPITRE 5 : RECHERCHE TERRAIN",
    "content": """
        <h2>Conséquences sur l'offre de valeur</h2>
        <p>Ces observations empiriques corroborent la pertinence du pivot stratégique abordé au chapitre précédent. La lassitude déclarée face aux sollicitations directes confirme a posteriori que le choix d'abandonner l'outbound de masse était une décision alignée avec la sensibilité de la cible. Par ailleurs, la crainte de la complexité technique souligne qu'il est impératif de simplifier au maximum la lecture des bénéfices apportés par Happy House.</p>
        
        <p>La proposition de valeur du réseau ne doit pas être perçue comme un fardeau administratif supplémentaire, mais comme un facilitateur dont les résultats sont évidents et facilement mesurables par le dirigeant.</p>

        <div class="expert-note">
            <strong>Transition vers le chapitre 6</strong><br>
            Les signaux recueillis sur le terrain confirment que la valeur perçue doit être rendue plus lisible et plus concrète pour lever les freins à l'engagement durable. Cette nécessité justifie la conception d’un outil de preuve de valeur, pensé pour soutenir la rétention en matérialisant très simplement le retour sur investissement généré par l'adhésion.
        </div>
    """
})

# --- CHAPITRE 6 : RÉTENTION & DASHBOARD ---
pages.append({
    "section": "CHAPITRE 6 : RÉTENTION & PREUVE DE VALEUR",
    "content": """
        <h1>Chapitre 6 — Rétention et matérialisation de la preuve de valeur</h1>
        <p>Les constats précédents ont établi que le défaut de perception du Retour sur Investissement (ROI) constituait un frein majeur à la fidélisation. Pour pallier cette faiblesse et ancrer la relation client dans la durée, une réflexion a été engagée sur la conception d'un support de restitution financière visant à objectiver la valeur globale créée par l'appartenance au réseau.</p>

        <h2>Le concept du tableau de bord (Dashboard) de performance</h2>
        <p>L’objectif de cette démarche de conception est de fournir un tableau de bord pensé comme un support de dialogue stratégique. Ce document synthétique permet de visualiser rapidement les économies réalisées (notamment grâce à la centrale d’achats) et le chiffre d'affaires incrémental généré par les interactions avec d'autres membres. Cet outil a pour vocation de remplacer les perceptions subjectives par des données comptables tangibles.</p>

        <p>Dans un processus opérationnel stabilisé, cet outil est conçu pour être utilisé comme support principal lors de revues trimestrielles menées en visioconférence avec l'adhérent. Cette approche de conseil personnalisé permet de maintenir un point de contact qualitatif, de mesurer l'impact de la stratégie d'achat, et d'ajuster les leviers de distribution si nécessaire, réaffirmant ainsi la valeur de l'accompagnement de Happy House.</p>
    """
})
pages.append({
    "section": "CHAPITRE 6 : RÉTENTION & PREUVE DE VALEUR",
    "content": """
        <h2>Prototypage : Preuve de concept (POC)</h2>
        <p>Le déploiement systématique de ce type de reporting impliquant un accès aux données de gestion des membres, un prototype (Proof of Concept) a été élaboré afin de démontrer sa faisabilité et sa valeur d'usage. Ce POC s'appuie sur la mise en exergue de deux indicateurs de performance fondamentaux : l'optimisation des coûts de structure et l'apport d'affaires inter-réseau.</p>

        <div class="visual-block" style="border-color: #DDA83E;">
            <div class="visual-title">VUE CONCEPTUELLE DU REPORTING ROI (POC)</div>
            <table class="gantt-table" style="width: 100%; color: #FFF; margin-top: 10px;">
                <tr style="background: rgba(221, 168, 62, 0.2);">
                    <th style="text-align: left;">AXE DE PERFORMANCE</th>
                    <th style="text-align: right;">IMPACT MESURÉ</th>
                </tr>
                <tr>
                    <td>Optimisation Achats (Centrale Entegra)</td>
                    <td style="text-align: right; color: #2ECC71;">Baisse en % sur factures cibles</td>
                </tr>
                <tr>
                    <td>Apport d'affaires inter-réseau</td>
                    <td style="text-align: right; color: #2ECC71;">Volume de CA incrémental B2B</td>
                </tr>
                <tr style="border-top: 1px solid var(--gold);">
                    <td style="text-align: right; font-weight: bold; color: var(--gold);">FINALITÉ DU SUPPORT :</td>
                    <td style="text-align: right; font-weight: bold; font-size: 9pt;">Matérialiser le bénéfice net global</td>
                </tr>
            </table>
        </div>

        <p>Au-delà de son rôle dans la fidélisation, ce type de livrable chiffré, une fois anonymisé, s'intègre naturellement à la nouvelle stratégie d'acquisition événementielle détaillée au chapitre précédent. Il constitue une base argumentaire objective lors des événements de présentation pour répondre avec transparence aux interrogations relatives au coût de la cotisation.</p>
    """
})
pages.append({
    "section": "CHAPITRE 6 : RÉTENTION & PREUVE DE VALEUR",
    "content": """
        <div class="expert-note">
            <strong>Transition vers le chapitre 7</strong><br>
            Une fois le besoin de preuve de valeur identifié et conceptualisé, il convient de transformer l'ensemble de cette réflexion en actions opérationnelles et planifiables. Le plan d’action proposé doit articuler le pivot événementiel, la mise en place des outils de rétention, et l'analyse d'un cas pratique permettant d'évaluer la rentabilité concrète du modèle pour un adhérent.
        </div>
    """
})

# --- CHAPITRE 7 : PLAN D'ACTION & BILAN ---
pages.append({
    "section": "CHAPITRE 7 : PLAN D'ACTION & BILAN",
    "content": """
        <h1>Chapitre 7 — Plan d'action, pilotage et bilan</h1>
        <p>L’analyse stratégique doit se traduire par un plan de mise en œuvre structuré et pilotable. Ce chapitre présente le déploiement opérationnel des recommandations au travers d'un calendrier d'actions (Gantt), intègre une matrice de gestion des risques, détaille les méthodes de calcul des indicateurs de performance, et analyse la rentabilité du réseau sur un cas pratique avéré.</p>

        <h2>Plan d'action opérationnel (Mois 1 à 12)</h2>
        <p>Le plan de déploiement est structuré sur un cycle de préparation (M1-M6) et d'exécution événementielle (M7-M12), intégrant le pivot stratégique (abandon de l'outbound de masse) abordé au Chapitre 5.</p>

        <div class="visual-block" style="padding: 10px;">
            <div class="visual-title">TABLEAU DE BORD OPÉRATIONNEL : GANTT ET RESSOURCES</div>
            <table class="gantt-table" style="width: 100%; border-collapse: collapse; color: #FFF; margin-top: 5px;">
                <tr style="background: rgba(221,168,62,0.1);">
                    <th style="width: 25%; text-align: left;">Action</th>
                    <th style="width: 20%;">Resp. & Budget</th>
                    <th style="width: 15%;">M1 - M3</th>
                    <th style="width: 15%;">M4 - M6</th>
                    <th style="width: 25%;">M7 - M12</th>
                </tr>
                <tr>
                    <td>1. Prototypage POC Dashboard</td>
                    <td>J. Florence (0€)</td>
                    <td class="gantt-active">Conception</td>
                    <td>Validation interne</td>
                    <td>Déploiement cible</td>
                </tr>
                <tr>
                    <td>2. Lancement Webinaires</td>
                    <td>P. Kermarrec (0€)</td>
                    <td></td>
                    <td class="gantt-active">1 / mois</td>
                    <td class="gantt-active">1 / mois</td>
                </tr>
                <tr>
                    <td>3. Afterworks Régionaux</td>
                    <td>J.F. (~500 €/evt)</td>
                    <td></td>
                    <td>Préparation logistique</td>
                    <td class="gantt-active">1 evt / trimestre</td>
                </tr>
            </table>
        </div>
    """
})
pages.append({
    "section": "CHAPITRE 7 : PLAN D'ACTION & BILAN",
    "content": """
        <h2>Matrice de pilotage : KPI et gestion des risques</h2>
        <p>Pour assurer la viabilité de ce plan d'action, des indicateurs de performance (KPI) stricts et des mesures d'atténuation des risques ont été définis en amont du déploiement :</p>

        <div class="visual-block" style="border-color: #E74C3C;">
            <div class="visual-title" style="color: #E74C3C;">ANALYSE DES RISQUES ET MÉTRIQUES DE SUIVI</div>
            <table class="gantt-table" style="width: 100%; border-collapse: collapse; color: #FFF; margin-top: 5px;">
                <tr style="background: rgba(231,76,60,0.1);">
                    <th style="width: 30%; text-align: left;">Risque Opérationnel</th>
                    <th style="width: 40%; text-align: left;">Stratégie d'Atténuation</th>
                    <th style="width: 30%; text-align: left;">Indicateur Clé (KPI)</th>
                </tr>
                <tr>
                    <td>Faible participation aux Afterworks</td>
                    <td>Sourcing amont par Younes via méthodologie DISC. Focus qualitatif plutôt que quantitatif.</td>
                    <td>Taux de présence (Cible: > 50% des inscrits confirmés)</td>
                </tr>
                <tr>
                    <td>Non-appropriation du Dashboard</td>
                    <td>Intégration du document dans une "Revue de Performance Trimestrielle" en visioconférence.</td>
                    <td>Taux d'ouverture post-envoi (Cible: > 60%)</td>
                </tr>
                <tr>
                    <td>Dérive des coûts d'acquisition</td>
                    <td>Suivi rigoureux du CPA. Arrêt si seuil limite dépassé sur 3 événements consécutifs.</td>
                    <td>Coût Par Acquisition (Cible: < 200€)</td>
                </tr>
            </table>
        </div>
    """
})
pages.append({
    "section": "CHAPITRE 7 : PLAN D'ACTION & BILAN",
    "content": """
        <h2>Méthodologie de calcul des indicateurs (KPIs)</h2>
        <p>Le pilotage de la stratégie événementielle repose sur deux indicateurs principaux, dont les méthodes de calcul sont formalisées afin de garantir un suivi objectif <em>(Cf. Annexe 8 : Note de Cadrage)</em>.</p>
        
        <h3>1. Le Taux de Présence</h3>
        <p>Cet indicateur mesure l'engagement réel des prospects. Il est calculé en divisant le nombre de participants physiques par le nombre d'inscrits ayant confirmé leur présence à J-2. Cette confirmation à J-2 permet d'isoler l'engagement réel des "no-shows" habituels en événementiel. L'objectif fixé est supérieur à 50%.</p>

        <h3>2. Le Coût Par Acquisition (CPA)</h3>
        <p>Le CPA évalue la rentabilité directe des événements (Afterworks). Il est obtenu en divisant le coût total de l'événement (organisation et marketing) par le nombre de nouveaux membres acquis. Le CPA maximal de rentabilité est défini par la différence entre la marge brute générée par un membre et les coûts opérationnels de son suivi.</p>

        <h2>Suivi post-déploiement : Le Comité de Pilotage (COPIL)</h2>
        <p>Pour analyser les écarts entre les objectifs et les résultats réels, un Comité de Pilotage (COPIL) mensuel est instauré avec la direction. D'une durée d'une à deux heures, ce comité évalue les performances (Taux de présence, CPA, ROI) et formalise les décisions selon des seuils d'échec stricts :</p>
        <ul>
            <li><strong>Seuil d'alerte (No-Go financier) :</strong> Un CPA supérieur à 200 € sur trois événements consécutifs entraîne l'arrêt ou la refonte complète du format Afterwork.</li>
        </ul>
    """
})
pages.append({
    "section": "CHAPITRE 7 : PLAN D'ACTION & BILAN",
    "content": """
        <h2>Étude de la performance : Le cas Durentie</h2>
        <p>L'efficacité du modèle réseau (mutualisation des achats et synergies commerciales) s'illustre factuellement par l'analyse du cas d'un membre Premium (Domaine de la Durentie). Ce cas d'usage sert de référence pour illustrer la valeur objectivée recherchée par le prototype de reporting.</p>
        
        <p>Le cycle initial de conversion de ce prospect a été d'environ cinq mois, témoignant de la difficulté d'engagement sans preuve de valeur préalable. À la suite de l'adhésion (impliquant une cotisation de 360 € TTC), l'utilisation des accords de la centrale d'achats a généré une économie mesurable de l'ordre de 4 120 € sur les postes de coûts opérationnels de l'établissement <em>(Cf. Annexe 10 : Évaluation de rentabilité)</em>.</p>
        
        <p>De plus, l'appartenance au réseau a favorisé une recommandation qualifiée : un autre membre affichant un taux d'occupation plein a réorienté gracieusement une clientèle vers le domaine, générant une transaction directe de 11 000 €. Ces données comptables valident que la rentabilité pour un membre actif dépasse largement le montant de l'adhésion, confirmant la viabilité économique du modèle.</p>
    """
})
pages.append({
    "section": "CHAPITRE 7 : PLAN D'ACTION & BILAN",
    "content": """
        <h2>Bilan de la mission et prise de recul</h2>
        <p>Cette mission d'alternance a constitué un environnement d'apprentissage particulièrement exigeant, imposant de concilier des recommandations stratégiques avec la réalité de la gouvernance d'entreprise. L'abandon forcé des processus d'automatisation (Outbound) a représenté un point d'inflexion : il a fallu accepter l'échec d'un modèle technique pertinent sur le papier pour construire une solution de contournement (l'événementiel) acceptable par la direction.</p>
        
        <p>Ce changement de paradigme a favorisé une évolution significative de ma posture professionnelle. Au-delà des compétences techniques initialement visées (Scraping, outils No-Code), la mission a nécessité le développement de compétences transversales : accompagnement au changement, formation d'un collaborateur (SDR) aux techniques de qualification, et capacité à argumenter des arbitrages face à une direction.</p>
        
        <p>En définitive, cette expérience valide une transition d'une logique d'exécution commerciale vers une fonction de pilotage du développement, où la maîtrise des données (mesure du ROI, suivi du CPA, analyse du Churn) sert avant tout à sécuriser la prise de décision stratégique.</p>

        <div class="expert-note">
            <strong>Transition vers le chapitre 8</strong><br>
            Enfin, pour clore ce document dans le respect des directives académiques, il convient de présenter de manière transparente la méthodologie de rédaction employée, et plus particulièrement le cadre d'utilisation des outils technologiques d'assistance à la rédaction.
        </div>
    """
})

# --- CHAPITRE 8 : IA ---
pages.append({
    "section": "CHAPITRE 8 : CONFORMITÉ IA",
    "content": """
        <h1>Chapitre 8 — Conformité et déclaration d'usage de l'IA</h1>
        
        <h2>Cadre de rédaction et transparence</h2>
        <p>Afin de répondre avec rigueur aux exigences de transparence stipulées dans le guide méthodologique (Section "Usage de l'IA"), cette section documente la manière dont les outils d'Intelligence Artificielle ont été intégrés dans le processus de formalisation de ce rapport de mission.</p>
        
        <p>L'IA a été employée exclusivement comme un outil d’assistance à la structuration formelle et au rendu visuel. Les contenus bruts ont ensuite été systématiquement relus, vérifiés et contextualisés personnellement afin de garantir l'authenticité de la démarche intellectuelle et l'exactitude des faits rapportés au sein de l'entreprise.</p>

        <div class="glass-card" style="border-left: 4px solid var(--gold);">
            <ul style="margin:0; padding-left: 15px;">
                <li><strong>Outil technologique mobilisé :</strong> Modèle de langage Gemini (via interface en ligne de commande locale).</li>
                <li><strong>Périmètre strict d'intervention :</strong> Aide à la reformulation syntaxique pour répondre aux standards académiques, et génération du code informatique (HTML/CSS/Python) nécessaire à la mise en page avancée du document PDF final.</li>
                <li><strong>Responsabilité exclusive de l'auteur :</strong> L'intégralité du diagnostic de l'entreprise, des choix de matrice d'analyse (PESTEL, SWOT), de la compréhension des blocages stratégiques (le pivot), de la conception du plan d'action, ainsi que des données chiffrées relatives à l'activité (indicateurs de churn, métriques du cas Durentie) constitue un travail d'analyse rigoureusement personnel et factuel. L'outil n'a produit aucun concept métier autonome.</li>
            </ul>
        </div>
    """
})

# --- ANNEXES ---
pages.append({
    "section": "ANNEXES : INDEX RÉPERTOIRE",
    "content": """
        <h1>Index des Annexes (Registre numérisé)</h1>
        <div class="expert-note">
            <strong>CONSULTATION DES LIVRABLES</strong>
            Afin de préserver la lisibilité de ce rapport de synthèse, les documents d'analyse exhaustifs, les tableaux de données et les preuves opérationnelles sont référencés ci-dessous et accessibles via un registre documentaire sécurisé en ligne.
        </div>

        <h2>Annexes de diagnostic et stratégie</h2>
        <ul>
            <li><strong>Annexe 1 : Matrice PESTEL détaillée</strong><br><a href="https://docs.google.com/document/d/1Yj4T12y6xtjj0OovCVUuuz70k-gqNvqwGKgHXW4ypWI/edit?usp=sharing" target="_blank" class="inline-link">Consulter l'analyse macro-environnementale ➔</a></li>
            <li><strong>Annexe 2 : Matrice SWOT complète</strong><br><a href="https://docs.google.com/document/d/1cODXz35hWuD4Ul_QJznqq29sbjeZZxCi9-4X7sztBBE/edit?usp=sharing" target="_blank" class="inline-link">Consulter le diagnostic interne/externe ➔</a></li>
            <li><strong>Annexe 3 : Analyse des forces de Porter</strong><br><a href="https://docs.google.com/document/d/1IDylUnSmjhGw9LoI7xI00ZjJISwBPqWOlvlnmsveD2w/edit?usp=sharing" target="_blank" class="inline-link">Consulter l'étude sectorielle ➔</a></li>
        </ul>

        <h2 style="margin-top: 30px;">Annexes financières et de performance</h2>
        <ul>
            <li><strong>Annexe 4 : Comparatif de performance d'acquisition</strong><br><a href="https://docs.google.com/document/d/1FTc__nwL3GdpaVOmY8W6-qnU7nHr9QYw5HPMF7d37pU/edit?usp=sharing" target="_blank" class="inline-link">Consulter le document ➔</a></li>
            <li><strong>Annexe 5 : Modélisation d'attrition (Churn)</strong><br><a href="https://docs.google.com/document/d/1VCUcwDRPigbblBWIv4Xl_pmXIc_UzeIREN6M3aKTty0/edit?usp=sharing" target="_blank" class="inline-link">Consulter la projection financière ➔</a></li>
            <li><strong>Annexe 10 : Évaluation de rentabilité de la centrale d'achats</strong><br><a href="https://docs.google.com/document/d/1_BWGT2HkVC9Q8mFkxtq33ClZ-guhxT7AHQkZjm3W_vI/edit?usp=sharing" target="_blank" class="inline-link">Consulter les simulations ➔</a></li>
        </ul>
    """
})

pages.append({
    "section": "ANNEXES : INDEX RÉPERTOIRE (SUITE)",
    "content": """
        <h2>Annexes méthodologiques et managériales</h2>
        <ul>
            <li><strong>Annexe 6 : Document de support au profilage qualitatif</strong><br><a href="https://docs.google.com/document/d/1VuTpPuFtGQIGZml0UKWOtm1tSNE0UJso4cQN1zBRSrE/edit?usp=sharing" target="_blank" class="inline-link">Consulter la méthodologie ➔</a></li>
            <li><strong>Annexe 7 : Trame de qualification pré-rendez-vous</strong><br><a href="https://docs.google.com/document/d/1quiGY0-cKDjFy-QrXMADToaMYqsx_JhzRp4iw5Bt7co/edit?usp=sharing" target="_blank" class="inline-link">Consulter la trame ➔</a></li>
            <li><strong>Annexe 8 : Synthèse de cadrage opérationnel</strong><br><a href="https://docs.google.com/document/d/1qsVUmIVUoutCg8Bd8d2f5p-irb17boQ1j9d06AX8Hfw/edit?usp=sharing" target="_blank" class="inline-link">Consulter la note de cadrage ➔</a></li>
        </ul>

        <h2 style="margin-top: 30px;">Preuves opérationnelles et supports complémentaires</h2>
        <ul>
            <li><strong>Éléments de communication et identité de marque :</strong> <a href="https://drive.google.com/file/d/1OoDtqvV-s1TELt1J17h7HyKzHJqrdiIQ/view?usp=drive_link" target="_blank" class="inline-link">Accéder au dossier ➔</a></li>
            <li><strong>Exemples contractuels :</strong> <a href="https://drive.google.com/file/d/1FAJt6nb93-iX32-AgZAJ_28MJDK2YDJ9/view?usp=drive_link" target="_blank" class="inline-link">Accéder au dossier ➔</a></li>
            <li><strong>Tableaux de suivi de performance :</strong> <a href="https://drive.google.com/file/d/1KHVaDgWzgNSpym-UeFSKzoDM5abVMJj2/view?usp=drive_link" target="_blank" class="inline-link">Accéder au dossier ➔</a></li>
        </ul>

        <div class="glass-card" style="margin-top: 50px; text-align: center; border: 1px solid #DDA83E;">
            <p style="font-family: 'Cinzel', serif; font-size: 12pt; color: #DDA83E; margin: 0; font-weight: bold;">
                FIN DU RAPPORT DE MISSION
            </p>
            <p style="font-size: 9pt; color: #888; margin-top: 10px;">
                Candidat : Julien Florence (Promotion A150).
            </p>
        </div>
    """
})

def make_page(content, page_num, section_title):
    html = f"""
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
"""
    return html

# Assembly
final_html = html_head
page_number = 1

for p in pages:
    if p.get("is_cover", False):
        final_html += f"""
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
"""
    else:
        final_html += make_page(p["content"], page_number, p["section"])
    page_number += 1

final_html += "</body></html>"

base_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(base_path, "RAPPORT_DE_MISSION_ULTRA_PRESTIGE.html")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"[✓] HTML académique généré avec succès ({page_number-1} pages estimées).")
