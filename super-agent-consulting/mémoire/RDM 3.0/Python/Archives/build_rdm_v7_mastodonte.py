import os

html_head = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAPPORT DE MISSION 2026 - JULIEN FLORENCE - ÉDITION EXPERT V5</title>
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
            --text-muted: #A9B7C6;
        }

        @page { size: A4; margin: 0; }
        * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }

        body {
            margin: 0; padding: 0;
            background-color: #1a1a1a;
            color: var(--text-main);
            font-family: 'Arial', sans-serif;
            font-size: 11.5pt; line-height: 1.6;
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

        h1 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 20pt; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 25px; text-align: center; font-weight: 900; border-bottom: 1px solid var(--border-glass); padding-bottom: 15px;}
        h2 { font-family: 'Cinzel', serif; color: var(--gold-light); font-size: 14pt; border-left: 4px solid var(--gold); padding-left: 15px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 2px; }
        h3 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 12pt; margin: 20px 0 10px 0; }
        p { margin-bottom: 15px; }

        .glass-card { background: var(--glass); backdrop-filter: blur(10px); border: 1px solid var(--border-glass); padding: 20px; border-radius: 4px; margin: 25px 0; position: relative; }
        
        .analytic-point { font-family: 'Cinzel', serif; color: var(--gold); font-size: 11pt; margin-top: 20px; margin-bottom: 5px;}
        .analytic-content { padding-left: 15px; border-left: 2px solid rgba(221, 168, 62, 0.3); margin-bottom: 20px; color: #FFFFFF; font-size: 10.5pt;}
        .analytic-highlight { color: #FFF; font-weight: bold; }

        .btn-annexe { display: inline-block; background: rgba(221, 168, 62, 0.15); color: var(--gold); border: 1px solid var(--gold); padding: 4px 10px; font-size: 8.5pt; font-weight: bold; text-decoration: none; border-radius: 3px; font-family: 'Arial', sans-serif; letter-spacing: 1px; vertical-align: middle; margin: 0 4px;}
        .btn-annexe:hover { background: var(--gold); color: #000; }

        .footer { position: absolute; bottom: 10mm; left: 20mm; right: 20mm; display: flex; justify-content: space-between; align-items: center; font-family: 'Cinzel', serif; font-size: 7.5pt; color: var(--gold); letter-spacing: 2px; z-index: 100; }
        .page-number { font-weight: 700; }

        .cover { justify-content: center; align-items: center; text-align: center; background-color: #0A0C1A; position: relative; }
        .cover-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; background-image: url('charte graphique/cover_vignoble.jpg'); background-size: cover; background-position: center; opacity: 0.25; filter: grayscale(50%); }
        .cover-content { position: relative; z-index: 10; width: 100%; height: 100%; padding: 25mm 20mm; display: flex; flex-direction: column; justify-content: space-between; }
        .tagline { font-family: 'Cinzel', serif; font-size: 14pt; color: var(--gold); letter-spacing: 8px; margin-bottom: 10px; }
        .main-title { font-size: 32pt; line-height: 1.1; margin: 25px 0; }
        .author-box { margin-top: 60px; font-family: 'Cinzel', serif; }
        .author-name { font-size: 22pt; font-weight: 900; letter-spacing: 4px; color: #FFFFFF; }
        .author-role { color: var(--gold); font-size: 10pt; text-transform: uppercase; letter-spacing: 2px; }

        table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 9.5pt; }
        th { background: rgba(221, 168, 62, 0.1); color: var(--gold); font-family: 'Cinzel', serif; padding: 12px; border: 1px solid var(--border-glass); text-align: left; }
        td { padding: 12px; border: 1px solid var(--border-glass); background: rgba(255,255,255,0.01); color: #fff; vertical-align: top;}

        .expert-note { border-left: 4px solid var(--gold); background: rgba(221, 168, 62, 0.05); padding: 15px; margin: 20px 0; font-style: italic; color: var(--gold-light); font-size: 10pt;}
        .expert-note strong { display: block; font-family: 'Cinzel', serif; font-style: normal; color: var(--gold); margin-bottom: 8px; font-size: 10pt; }

        a { text-decoration: none; color: #DDA83E; display: block; }
        a.inline-link { display: inline; border-bottom: 1px dotted #DDA83E; }
        
        .btn-nav { display: inline-block; padding: 12px 25px; border: 2px solid #DDA83E; color: #DDA83E; font-family: 'Cinzel', serif; font-size: 10pt; letter-spacing: 2px; background: #0A0C1A; cursor: pointer; text-align: center; }

        .toc-link { width: 100%; padding: 10px 0; border-bottom: 1px solid #222; color: #FFFFFF; font-size: 11pt;}
        .toc-link:hover { color: #DDA83E; }
        
        ul { padding-left: 20px; margin-top: 5px; margin-bottom: 15px;}
        li { margin-bottom: 6px; }

        .visual-block { background: #05060A; border: 1px solid var(--border-glass); border-radius: 4px; padding: 15px; font-family: 'Courier New', Courier, monospace; font-size: 9pt; color: #DDA83E; overflow-x: hidden; margin: 20px 0; position: relative;}
        .visual-block::before { content: '/// ROCKET SCHOOL DATA VIEW ///'; position: absolute; top: 0; right: 0; background: rgba(221, 168, 62, 0.1); padding: 2px 10px; font-size: 6pt; color: var(--gold); font-family: 'Cinzel';}
        .visual-title { color: #FFFFFF; font-family: 'Cinzel', serif; font-size: 10pt; margin-bottom: 12px; border-bottom: 1px solid var(--border-glass); padding-bottom: 5px; display: inline-block; letter-spacing: 1px;}
        .code-line { display: block; margin-bottom: 6px; color: #A9B7C6; }
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
    <h1 style="color: #DDA83E; text-align: center;">Sommaire Analytique</h1>
    <div style="margin-top: 30px;">
"""
chapitres = [
    ("REMERCIEMENTS & MÉTHODOLOGIE", 3),
    ("I. L'ENTREPRISE & LA PROBLÉMATIQUE STRATÉGIQUE", 5),
    ("II. LE DIAGNOSTIC EXTERNE : LA FATIGUE NUMÉRIQUE", 7),
    ("III. L'AUDIT INTERNE : L'ÉQUATION DU NAUFRAGE", 9),
    ("IV. AUDIT DATA : LE FILTRE LÉGAL (LOI ALUR)", 12),
    ("V. AUDIT ACQUISITION : L'IMPASSE OUTBOUND", 14),
    ("VI. LE PIVOT STRATÉGIQUE : L'INBOUND", 16),
    ("VII. LA RÉTENTION : LE DASHBOARD R.O.I", 18),
    ("VIII. LE PLAN D'ACTION & LE PILOTAGE COPIL", 20),
    ("IX. CV DIGITAL & BILAN PERSONNEL", 23),
    ("X. DÉCLARATION DE CONFORMITÉ IA", 25),
    ("XI. ANNEXES PHYSIQUES & MATRICES", 26),
    ("XII. DOSSIER DES PREUVES CLOUD", 33)
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

# --- PAGE 3 : REMERCIEMENTS & MÉTHODOLOGIE ---
pages.append({
    "section": "INTRODUCTION",
    "content": """
        <h1>Remerciements & Cadre Analytique</h1>
        <p>Je tiens en premier lieu à remercier l'équipe pédagogique de <strong>Rocket School</strong>. L'exigence de ce cursus m'a permis d'opérer une véritable transition intellectuelle : passer d'une logique d'exécution opérationnelle (issue de l'hospitalité et de la sommellerie de luxe) à une posture de Direction Stratégique orientée Data & Growth.</p>
        <p>Mes remerciements s'adressent à la gouvernance de <strong>Happy House</strong>, et particulièrement à Patrice Kermarrec. Ce terrain d'entreprise a été le théâtre d'un apprentissage fondamental : devoir composer en temps réel entre l'ambition technologique et les limites identitaires et financières imposées par la marque.</p>
        <p>Je salue enfin <strong>Younes</strong> (SDR), avec qui la restructuration des discours commerciaux fut aussi formatrice sur le plan managérial que vitale pour la réussite de la mission, ainsi que mon binôme <strong>Ruddy Marie-Luce</strong> avec qui le croisement de l'analyse Data a permis de poser le diagnostic financier final de l'entreprise.</p>
    """
})

# PAGE 4
pages.append({
    "section": "MÉTHODOLOGIE ANALYTIQUE",
    "content": """
        <h2>Structure de la démonstration (Les 6 temps)</h2>
        <p>Afin de répondre aux standards les plus élevés du conseil en stratégie, ce rapport rompt avec la narration descriptive pour adopter une posture de "preuve". Aucune recommandation n'est avancée sans être soumise au crible de l'entonnoir suivant :</p>
        
        <ul style="font-size: 10.5pt; color: var(--text-muted); line-height: 1.8;">
            <li><strong>Le Point :</strong> L'observation directe du terrain ou du marché de l'hébergement.</li>
            <li><strong>La Justification :</strong> L'explication de pourquoi ce point est un pivot stratégique (Life or Death).</li>
            <li><strong>La Preuve Chiffrée :</strong> L'extraction mathématique vérifiable issue de nos systèmes internes (CRM).</li>
            <li><strong>Le Contexte d'Analyse :</strong> La mise en perspective de ce chiffre.</li>
            <li><strong>La Cause Racine (La Maladie) :</strong> L'identification du problème structurel sous-jacent.</li>
            <li><strong>Le Plan d'Action (Le Remède) :</strong> La solution opérationnelle déployée pour corriger la trajectoire.</li>
        </ul>

        <h2>La règle d'alignement Data</h2>
        <p>Chaque choix stratégique (le Pivot, la Rétention) est strictement corrélé à l'analyse de nos deux bases maîtresses : le fichier prospect brut (126 000 contacts) et le CRM d'onboarding (146 adhésions validées). Par ailleurs, les chiffres de rentabilité globale et de LTV sont rigoureusement alignés sur l'audit mené conjointement avec Ruddy Marie-Luce pour garantir une lecture comptable unifiée du réseau.</p>
    """
})

# --- CHAPITRE 1 : ENTREPRISE ---
pages.append({
    "section": "CHAPITRE 1 : L'ENTREPRISE",
    "content": """
        <a id="chapitre-1"></a>
        <h1>Chapitre 1 — L'Entreprise & La Problématique</h1>
        
        <h2>L'Écosystème Happy House</h2>
        <p>Fondée en 2017, la startup Happy House s'est positionnée sur un marché de niche à forte valeur ajoutée : l'accompagnement des hébergeurs indépendants sur le segment Premium et "Hébergement de charme". L'entreprise déploie un écosystème de services globaux :</p>
        
        <ul style="font-size: 10.5pt; line-height: 1.6;">
            <li><strong>1. L'Optimisation des Achats :</strong> Accès exclusif à la puissance de la centrale d'achats <em>Entegra</em> (générant de 15% à 25% de marge additionnelle sur les postes F&B et énergie).</li>
            <li><strong>2. La Connectivité (Tech) :</strong> Déploiement d'un écosystème logiciel (Une "Guest App" dédiée à l'expérience du voyageur et un outil CRM complet pour la gestion quotidienne de l'hébergeur).</li>
            <li><strong>3. La Visibilité Digitale :</strong> Création de sites web optimisés pour la conversion et la réservation directe (pour contourner les OTAs).</li>
            <li><strong>4. La Synergie de Réseau :</strong> Apport d'affaires inter-membres et partenariats locaux.</li>
        </ul>
    """
})

# PAGE 6
pages.append({
    "section": "CHAPITRE 1 : LA PROBLÉMATIQUE",
    "content": """
        <h2>Le Plafond de Verre : Analyse de la Tension</h2>
        
        <p>Appliquons notre grille de lecture stratégique à la structure de Happy House.</p>

        <div class="analytic-point">Le Point Initial</div>
        <div class="analytic-content">La structure historique de l'entreprise, fondée sur le management relationnel, atteint ses limites opérationnelles.</div>
        
        <div class="analytic-point">Pourquoi ce choix</div>
        <div class="analytic-content">C'est le postulat de base. On ne peut résoudre un problème de scalabilité si l'on ne comprend pas l'asymétrie béante entre la taille restreinte de l'équipe et le volume d'affaires.</div>
        
        <div class="analytic-point">La Preuve Chiffrée</div>
        <div class="analytic-content">Un parc de <span class="analytic-highlight">170 membres historiques</span> gérés par une équipe de seulement 4 personnes (Le CEO et 3 alternants couvrant la Data, les Sales et la Tech).</div>
        
        <div class="analytic-point">L'Analyse de Contexte</div>
        <div class="analytic-content">Les exigences de l'hébergement haut de gamme réclament une disponibilité et une réassurance de niveau "Senior". La structure actuelle, bien qu'agile, ne peut pas absorber une croissance exponentielle sans imploser.</div>
        
        <div class="analytic-point">La Maladie (Cause Racine)</div>
        <div class="analytic-content">L'absence de processus automatisés et de formalisation comptable des preuves de valeur bloque la fidélisation. C'est le syndrome du "seau percé" : on tente de remplir le réseau par l'acquisition, mais on perd les clients par le fond (Churn) faute de structuration.</div>
        
        <div class="analytic-point">Le Remède</div>
        <div class="analytic-content">Formuler une problématique d'audit stricte qui lie indissociablement l'acquisition et la rétention.</div>

        <div class="glass-card" style="border: 2px solid var(--gold); margin-top: 25px;">
            <div class="visual-title" style="color: var(--gold);">PROBLÉMATIQUE STRATÉGIQUE</div>
            <p style="font-size: 13pt; font-weight: 600; color: #FFF; text-align: justify; line-height: 1.5; margin:0;">
                Comment Happy House peut-elle réduire drastiquement son taux d'attrition (Churn) tout en structurant une stratégie d'acquisition rentable, adaptée à son positionnement Premium et aux contraintes de sa gouvernance interne ?
            </p>
        </div>
    """
})

# PAGE 7
pages.append({
    "section": "CHAPITRE 2 : LE MARCHÉ",
    "content": """
        <a id="chapitre-2"></a>
        <h1>Chapitre 2 — Le Diagnostic Externe : La Pression Numérique</h1>
        
        <p>Afin de structurer l'acquisition (répondre à la problématique), il faut comprendre la cible. L’analyse macro-économique démontre que l'hébergeur indépendant évolue dans un environnement d'une violence institutionnelle et technologique inouïe. <a href="#annexe-1" class="btn-annexe">VOIR MATRICE PESTEL (ANNEXE 1)</a></p>

        <h2>La Saturation par les Monopoles et les Normes</h2>
        
        <div class="analytic-point">L'Observation du Marché</div>
        <div class="analytic-content">L'hébergeur souffre d'une "Fatigue Numérique" systémique en raison d'un harcèlement technologique et réglementaire continu.</div>
        
        <div class="analytic-point">Pourquoi ce choix stratégique</div>
        <div class="analytic-content">Il est impératif de prouver mathématiquement que la prospection de masse classique (Cold Call) est devenue sociologiquement inopérante sur cette cible avant de proposer un pivot d'acquisition.</div>
        
        <div class="analytic-point">Les Preuves Chiffrées</div>
        <div class="analytic-content"><span class="analytic-highlight">71%</span> : C'est la part de marché écrasante détenue par Booking.com en Europe. En parallèle, le label environnemental "Clef Verte" a connu une inflation de <span class="analytic-highlight">+184%</span> en 3 ans. <a href="#annexe-9" class="btn-annexe">VOIR DATA MACRO (ANNEXE 9)</a></div>
    """
})

# PAGE 8
pages.append({
    "section": "CHAPITRE 2 : LE MARCHÉ (SUITE)",
    "content": """
        <h2>Analyse de la Pression Numérique (Suite)</h2>

        <div class="analytic-point">Le Contexte d'Étouffement</div>
        <div class="analytic-content">L'hébergeur Premium est écartelé. D'un côté, les OTAs l'asphyxient financièrement en prélevant jusqu'à 25% de commission. De l'autre, l'injonction écologique gouvernementale (loi DPE) et la fin brutale du label d'État "Qualité Tourisme" l'étouffent administrativement. En outre, il subit une inflation opérationnelle de +15% sur ses coûts énergétiques en 2024.</div>
        
        <div class="analytic-point">La Maladie du Marché</div>
        <div class="analytic-content">Le rejet pavlovien. Submergé par les emails promettant des "logiciels miracles" ou de "nouvelles certifications", l'hôte indépendant a dressé un mur. Il considère désormais toute sollicitation téléphonique entrante comme une charge mentale additionnelle, et non comme une opportunité.</div>
        
        <div class="analytic-point">Le Remède Stratégique</div>
        <div class="analytic-content">Un changement radical de posture commerciale. Happy House ne doit plus se présenter en prospection comme un "outil technologique de plus", mais comme un "facilitateur humain". L'angle d'attaque ne doit plus être le digital, mais la réassurance physique et la mutualisation défensive des coûts (l'argument Entegra).</div>
    """
})

# PAGE 9
pages.append({
    "section": "CHAPITRE 3 : AUDIT INTERNE",
    "content": """
        <a id="chapitre-3"></a>
        <h1>Chapitre 3 — Audit Interne : L'Équation du Naufrage</h1>
        
        <p>Si le contexte macro-économique valide l'urgence de nos services <a href="#annexe-2" class="btn-annexe">VOIR SWOT (ANNEXE 2)</a>, l'audit interne (mené conjointement avec la Direction Data, R. Marie-Luce) révèle une hémorragie comptable et commerciale sur l'acquisition récente.</p>

        <h2>Le Diagnostic du Churn (Taux d'Attrition) et de la LTV</h2>
        
        <div class="analytic-point">L'Observation du Terrain Interne</div>
        <div class="analytic-content">L'effondrement de la fidélisation des membres acquis à froid détruit mathématiquement la rentabilité de l'entreprise.</div>
        
        <div class="analytic-point">Pourquoi isoler ce point</div>
        <div class="analytic-content">Acquérir à froid coûte très cher. Si la Lifetime Value (LTV) du client est inférieure au Coût d'Acquisition Client (CAC), le modèle est une pyramide de Ponzi.</div>
        
        <div class="analytic-point">La Preuve Chiffrée (Extraction CRM Validée)</div>
        <div class="analytic-content">L'étude de la cohorte des <span class="analytic-highlight">146 adhésions formelles</span> (2022-2025) générées en Outbound donne des chiffres glaciaux. Bien que les sorties officielles (tag "NO GO") ne soient que de 18%, nous constatons en réalité une déperdition d'environ <span class="analytic-highlight">80% du parc</span> (Perte de suivi, hébergeurs qui ne paient plus sans être tagués). Le revenu moyen par hébergeur (ARPU) est estimé à 226 €/an, limitant la LTV moyenne à seulement <span class="analytic-highlight">290 €</span>. <a href="#annexe-5" class="btn-annexe">VOIR DATA CRM (ANNEXE 5)</a></div>
    """
})

# PAGE 10
pages.append({
    "section": "CHAPITRE 3 : AUDIT INTERNE (SUITE)",
    "content": """
        <h2>Modélisation des causes de l'attrition</h2>

        <div class="analytic-point">L'Analyse du Biais (Contexte)</div>
        <div class="analytic-content">Le réseau historique de 170 membres reste stable grâce au bouche-à-oreille naturel. L'hémorragie de 80% frappe spécifiquement les cohortes acquises par démarchage (Outbound). Attention, ce "Churn" ne représente pas uniquement des sorties volontaires : il s'agit majoritairement d'une "perte de contact". Les appels de notre équipe restent sans réponse. L'hébergeur s'emmure dans le silence.</div>
        
        <div class="analytic-point">La Maladie Interne</div>
        <div class="analytic-content">L'asymétrie de l'information. Nous possédons une arme financière puissante (les 15% à 25% d'économies générées par Entegra). Le problème n'est pas le produit, mais la <em>perte de valeur perçue</em> au fil des mois. L'hébergeur Premium, sur-sollicité (cf. Chapitre 2), oublie qu'il fait des économies avec nous. Ne voyant plus l'utilité directe de l'interaction, il cesse de nous répondre. Ce "mur du silence" est la forme la plus insidieuse de l'attrition.</div>
        
        <div class="analytic-point">Le Remède Structurel</div>
        <div class="analytic-content">Une répartition des urgences : la survie exige la création d'un protocole chiffré de "Preuve de Valeur" (Reporting ROI) pour sauver la base. C'est l'objet de mon action de Rétention. En parallèle, l'acquisition Inbound pure (trafic voyageur) sera confiée à mon collaborateur Ruddy.</div>
    """
})

# PAGE 11
pages.append({
    "section": "CHAPITRE 4 : AUDIT DATA & LOI ALUR",
    "content": """
        <a id="chapitre-4"></a>
        <h1>Chapitre 4 — L'Audit Data : Le Filtre Légal (Loi ALUR)</h1>
        
        <p>Afin de relancer l'acquisition, il convient d'auditer notre actif principal (le fichier prospect brut de 126 000 contacts) via le même cadre analytique.</p>

        <h2>L'Épuration de la Base de Données</h2>

        <div class="analytic-point">Le Point Initial (L'Observation)</div>
        <div class="analytic-content">La possession d'un fichier brut de 126 000 contacts n'est pas un actif commercial exploitable en l'état ; c'est un gisement non qualifié qu'il faut filtrer juridiquement.</div>
        
        <div class="analytic-point">Pourquoi appliquer notre méthodologie ici</div>
        <div class="analytic-content">Prospecter à l'aveugle une telle base expose l'entreprise à un double risque fatal : un gouffre financier (appels inutiles) et le danger d'associer la marque Happy House à des loueurs non conformes. L'analyse Data doit précéder l'action commerciale.</div>
        
        <div class="analytic-point">Les Preuves Chiffrées (Le Tri Data)</div>
        <div class="analytic-content">L'algorithme a scanné les <span class="analytic-highlight">126 000 lignes prospects</span>. L'analyse révèle une répartition stricte : <span class="analytic-highlight">70% de particuliers/amateurs</span> (88 200 lignes) face à 30% de professionnels (37 800 lignes). Au sein de cette cohorte Pro, la pyramide Premium a été isolée : 55% de 3★ (20 790 lieux), 35% de 4★ (13 230), et 10% de 5★/Palaces (3 780).</div>
    """
})

# PAGE 12
pages.append({
    "section": "CHAPITRE 4 : AUDIT DATA (SUITE)",
    "content": """
        <h2>La Conformité comme Arme de Qualification</h2>

        <div class="analytic-point">L'Analyse de Contexte (La Loi ALUR)</div>
        <div class="analytic-content">Le filtrage par étoiles ne suffit pas, il faut appliquer la loi. La Loi ALUR a drastiquement resserré l'étau sur la location courte durée (numéro d'enregistrement obligatoire, limite stricte de 120 jours pour les résidences principales). Le marché se scinde : les opportunistes reculent sous la pression de l'État, tandis que les professionnels restent. Ce croisement Data permet d'écarter immédiatement la masse exponentielle des 88 200 loueurs amateurs.</div>
        
        <div class="analytic-point">La Maladie (Le Churn Réglementaire)</div>
        <div class="analytic-content">Le risque de "Faux Positifs". Si notre force de vente appelle cette liste de haut en bas, elle risque d'onboarder des acteurs amateurs qui seront contraints à la fermeture administrative dans les 12 mois par la Loi ALUR ou le DPE. Cela générerait une illusion de croissance, immédiatement suivie d'une explosion mathématique de notre Taux d'Attrition (Churn).</div>
        
        <div class="analytic-point">Le Remède (Scoring Légal)</div>
        <div class="analytic-content">Le fichier n'est plus un annuaire, c'est un moteur de <em>Scoring B2B</em>. Seuls les prospects démontrant une conformité ALUR avérée, une capacité viable (80% des cibles isolées ont moins de 10 chambres) et un standing certifié (3★ à 5★) gagnent le statut de "Lead Qualifié" et le droit de recevoir l'invitation à un Afterwork. La Data devient un bouclier juridique protégeant la LTV du réseau.</div>
    """
})

# PAGE 13
pages.append({
    "section": "CHAPITRE 5 : AUDIT ACQUISITION",
    "content": """
        <a id="chapitre-5"></a>
        <h1>Chapitre 5 — Audit d'Acquisition : L'Impasse Outbound</h1>
        
        <p>Maintenant que la cible saine est isolée (les 30% de pros Premium), comment les acquérir ? L'audit du "Cold Calling" historique a révélé une impasse absolue.</p>

        <h2>Les Mathématiques du Désastre Financier</h2>
        
        <div class="analytic-point">L'Observation Commerciale</div>
        <div class="analytic-content">Le modèle d'acquisition par démarchage téléphonique direct (Outbound pur) est financièrement insoutenable et statistiquement inopérant.</div>
        
        <div class="analytic-point">Pourquoi modéliser cette inefficacité</div>
        <div class="analytic-content">L'intuition ne suffit pas face à la direction. Il faut "tuer" l'ancienne méthode de manière irréfutable en calculant son Coût d'Acquisition Client (CAC) et le Ratio LTV/CAC. <a href="#annexe-4" class="btn-annexe">VOIR CALCULS CAC (ANNEXE 4)</a></div>
    """
})

# PAGE 14
pages.append({
    "section": "CHAPITRE 5 : AUDIT ACQUISITION (SUITE)",
    "content": """
        <h2>Le Ratio Mortel : LTV / CAC</h2>

        <div class="analytic-point">Les Preuves Chiffrées (Tunnel d'Acquisition)</div>
        <div class="analytic-content">L'audit conjoint des métriques SDR sur 48 semaines d'exercice donne le vertige :
            <ul style="margin-top: 5px;">
                <li>Volume d'effort : <span class="analytic-highlight">14 500 appels</span> (moyenne de 300 appels/semaine).</li>
                <li>Le taux de Non-Réponse (NRP) immédiat s'élève à <strong>50%</strong>.</li>
                <li>Les refus catégoriques frappent <strong>40%</strong> de la cohorte.</li>
                <li>Le <strong>CAC historique (Outbound) s'élève à 1 823 €</strong> (salaire SMIC SDR rapporté à 1 signature mensuelle).</li>
                <li><strong>Ratio Stratégique :</strong> La LTV moyenne étant de 290€, le ratio <span class="analytic-highlight">LTV/CAC est de 0,16</span>. L'acquisition Outbound récupère à peine 16% de son coût.</li>
            </ul>
        </div>
        
        <div class="analytic-point">Le Contexte d'Analyse</div>
        <div class="analytic-content">L'effort herculéen de 14 500 appels pour générer un CAC de 1 823 € face à un ARPU (Revenu Moyen) de 226 €/an démontre que ce modèle est "mathématiquement condamné". L'Outbound est 6 à 8 fois trop cher.</div>
        
        <div class="analytic-point">La Maladie du Canal</div>
        <div class="analytic-content">L'observation du terrain démontre que la cible est angoissée par le cadre réglementaire (Loi ALUR, DPE) et harcelée par les logiciels (Chapitre 2). Le "Cold Calling", par essence interruptif et agressif, déclenche un rejet pavlovien chez un indépendant terrifié et sur la défensive.</div>
        
        <div class="analytic-point">Le Remède Opérationnel</div>
        <div class="analytic-content">Arrêt immédiat de l'Outbound de masse. Il faut basculer sur un canal quasi-gratuit (Demande organique) et sur de l'Inbound qualitatif.</div>
    """
})

# PAGE 15
pages.append({
    "section": "CHAPITRE 6 : LE PIVOT STRATÉGIQUE",
    "content": """
        <a id="chapitre-6"></a>
        <h1>Chapitre 6 — Le Pivot Stratégique : L'Inbound</h1>
        
        <p>Face à ce Ratio LTV/CAC de 0.16, ma mission imposait de proposer une révision totale de l'acquisition. Ce chapitre expose la tentative de rationalisation par l'algorithme, les arbitrages de gouvernance rencontrés, et l'émergence d'une solution humaine.</p>

        <h2>De l'Hypothèse Algorithmique à l'Événementiel</h2>
        
        <div class="analytic-point">L'Observation et l'Hypothèse</div>
        <div class="analytic-content">Le rejet d'une solution technique d'automatisation (n8n) au profit d'un pivot événementiel humain (Inbound).</div>
        
        <div class="analytic-point">Pourquoi faire l'autopsie de ce choix</div>
        <div class="analytic-content">Le rôle d'un Directeur Stratégique n'est pas d'imposer un outil informatique de force, mais de fournir une solution business qui reste compatible avec l'identité de marque et les lignes rouges fixées par la direction.</div>
    """
})

# PAGE 16
pages.append({
    "section": "CHAPITRE 6 : LE PIVOT STRATÉGIQUE (SUITE)",
    "content": """
        <h2>La Gouvernance face à l'Automatisation</h2>

        <div class="analytic-point">Le Contexte (Le véto de la Direction)</div>
        <div class="analytic-content">J'ai initialement proposé d'exploiter la base des Leads via l'outil <strong>n8n</strong> pour automatiser le Cold Emailing. L'idée était d'envoyer des séquences automatisées, pour que le SDR n'appelle que les clics positifs, faisant chuter le CAC. La gouvernance a opposé un <strong>veto formel et définitif</strong>. La peur de l'assimilation au SPAM était jugée incompatible avec le positionnement Premium (4★ et 5★) que Happy House souhaite incarner.</div>
        
        <div class="analytic-point">La Maladie (Identitaire)</div>
        <div class="analytic-content">Le risque de "Brand Damage" (dégradation de la marque). Automatiser l'acquisition dans un marché déjà saturé de bruit, c'est prendre le risque d'aligner le réseau sur les pratiques des vendeurs de logiciels décriés.</div>
        
        <div class="analytic-point">Le Remède (Le Pivot Inbound & Social Proof)</div>
        <div class="analytic-content">J'ai intégré cette contrainte pour créer la "Stratégie d'Afterwork Régional". La Data du CRM n'est plus utilisée pour du tir de barrage, mais uniquement pour qualifier des listes de 30 invités ultra-locaux (déjà triées ALUR). L'acquisition se fait en rencontre physique, in-situ, hébergée par un membre existant (Social Proof). Le discours du SDR (Younes) change radicalement : on ne vend plus rien au téléphone, on qualifie les "Douleurs" de l'hôte via la méthode DISC (Dominant/Influent) pour l'inviter à l'Afterwork. <a href="#annexe-6" class="btn-annexe">VOIR SCRIPT SDR (ANNEXE 6)</a></div>
    """
})

# PAGE 17
pages.append({
    "section": "CHAPITRE 7 : LA RÉTENTION",
    "content": """
        <a id="chapitre-7"></a>
        <h1>Chapitre 7 — La Rétention : Le Dashboard R.O.I</h1>
        
        <p>Le pivot vers l'événementiel (Afterworks) règle la qualité de l'acquisition. Mais avec une LTV de 290€, il faut impérativement allonger la durée de vie du client en corrigeant le "Silence Radio" identifié au Chapitre 3.</p>

        <h2>Matérialiser l'invisible pour fidéliser</h2>
        
        <div class="analytic-point">Le Concept Déployé</div>
        <div class="analytic-content">La conception opérationnelle d'un "Proof of Concept" (POC) de Reporting Financier (Dashboard) à fréquence trimestrielle pour chaque adhérent.</div>
        
        <div class="analytic-point">Pourquoi ce choix fonctionnel</div>
        <div class="analytic-content">Dans le B2B Premium, la fidélité n'est pas liée à la sympathie, mais à la mathématique stricte de l'exploitation. Il faut objectiver les gains apportés par le réseau (les tarifs négociés Entegra). Si le membre ne voit pas le chiffre net, il résilie la cotisation à 360€.</div>
    """
})


# PAGE 17.5 : PERSONAS
pages.append({
    "section": "CHAPITRE 6 : L'ANATOMIE DU PIVOT (LES PERSONAS)",
    "content": """
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
    """
})


# PAGE 18.5 : PRICING
pages.append({
    "section": "CHAPITRE 6 : L'AUDIT FINANCIER (PRICING)",
    "content": """
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
    """
})

# PAGE 18
pages.append({
    "section": "CHAPITRE 7 : LA RÉTENTION (SUITE)",
    "content": """
        <h2>L'Ingénierie de la Preuve</h2>

        <div class="analytic-point">Le Chiffre (Coût d'exécution)</div>
        <div class="analytic-content">Une conception technologique "Low-Code" nécessitant <span class="analytic-highlight">moins de 1 heure de gestion</span> mensuelle par client pour l'équipe interne, assurant un coût de maintien quasi nul.</div>
        
        <div class="analytic-point">Le Contexte Technologique</div>
        <div class="analytic-content">La gouvernance n'avait ni le budget d'investissement pour un SaaS sur-mesure, ni le temps humain. L'utilisation stratégique de l'infrastructure n8n a permis de relier les données de facturation (via Entegra) à une interface lisible sans nécessiter de développeur.</div>
        
        <div class="analytic-point">La Maladie du Client</div>
        <div class="analytic-content">La volatilité de la mémoire comptable. L'hébergeur paie sa cotisation annuelle Happy House mais oublie au quotidien qu'il bénéficie en coulisse de tarifs préférentiels. Au moment de renouveler son abonnement, son cerveau ne voit qu'une charge sèche, déconnectée de ses économies globales.</div>
        
        <div class="analytic-point">Le Remède Opérationnel</div>
        <div class="analytic-content">Imposer un rendez-vous (Customer Success) trimestriel en visioconférence. Le Dashboard devient l'outil central et indiscutable de l'Account Manager pour asséner la preuve de valeur : <em>"Votre cotisation coûte 360€, nous vous avons fait économiser 4120€"</em>. Cet outil anonymisé servira en outre d'arme de réassurance massive lors des Afterworks Inbound pour lever le doute des prospects.</div>
    """
})

# PAGE 19
pages.append({
    "section": "CHAPITRE 8 : LE PLAN D'ACTION",
    "content": """
        <a id="chapitre-8"></a>
        <h1>Chapitre 8 — Plan d'Action & Pilotage COPIL</h1>
        
        <p>L'exécution combinée du double remède (Le pivot Afterworks pour l'acquisition + Le Dashboard ROI pour la rétention) nécessite une doctrine de contrôle de gestion stricte. Une stratégie sans KPI de gestion de l'échec n'a aucune valeur.</p>

        <h2>1. Objectiver la promesse comptable (Preuve Terrain)</h2>
        
        <div class="analytic-point">L'Étape Fondatrice</div>
        <div class="analytic-content">La validation mathématique du modèle de rentabilité sur un Cas Pratique réel et avéré de l'entreprise.</div>
        
        <div class="analytic-point">Pourquoi valider avant de déployer</div>
        <div class="analytic-content">Il faut démontrer que la promesse inscrite dans le futur Dashboard repose sur des flux monétaires réels et non sur des projections marketing. C'est le prérequis à tout déblocage de budget pour les Afterworks.</div>
    """
})

# PAGE 20
pages.append({
    "section": "CHAPITRE 8 : LE PLAN D'ACTION (SUITE)",
    "content": """
        <h2>Le Crash-Test de Rentabilité : Le Cas Durentie</h2>

        <div class="analytic-point">Les Preuves Chiffrées (Dossier CRM)</div>
        <div class="analytic-content">L'analyse du domaine Premium "La Durentie" révèle une équation magistrale : Un investissement initial de <span class="analytic-highlight">360 €</span> a généré <span class="analytic-highlight">4 120 € de bénéfice net d'exploitation</span> factuel, couplé à une génération de <span class="analytic-highlight">11 000 € de CA additionnel</span> inter-réseau. <a href="#annexe-10" class="btn-annexe">VOIR BILAN COMPTABLE (ANNEXE 10)</a></div>
        
        <div class="analytic-point">Le Contexte Client</div>
        <div class="analytic-content">Après un cycle de prospection long, l'intégration de ce membre a généré des baisses massives et documentées sur la Blanchisserie (910€), le F&B (2150€) et l'Énergie (1420€) via l'application de nos contrats cadres Entegra.</div>
        
        <div class="analytic-point">La Maladie du Prospect</div>
        <div class="analytic-content">Le doute systématique lors des rencontres (Afterworks). Sur un marché saturé de marchands de rêves (OTAs/Logiciels), le paiement d'une cotisation initiale est toujours un frein psychologique "viscéral".</div>
        
        <div class="analytic-point">Le Remède Déployé</div>
        <div class="analytic-content">L'impression et l'utilisation physique de ces données Durentie comme "socle de conviction" central lors des événements régionaux. La peur de la dépense est annulée par l'objectivité de l'économie réalisée par un pair.</div>
    """
})

# PAGE 21
pages.append({
    "section": "CHAPITRE 8 : LE PLAN D'ACTION (SUITE)",
    "content": """
        <h2>2. La Doctrine de Pilotage (Le COPIL)</h2>
        
        <p>L'organisation d'un Afterwork Inbound nécessite un budget moyen évalué à 500 € (Traiteur, Logistique). Face à un ARPU de 226€, ce budget doit être verrouillé. Un protocole d'engagement a été acté avec la direction via un Comité de Pilotage (COPIL) mensuel d'analyse des écarts.</p>

        <div class="visual-block" style="border-color: #E74C3C; padding: 25px;">
            <div class="visual-title" style="color: #E74C3C; font-size: 11pt;">GESTION DU RISQUE ET MATRICE D'ESCALADE</div>
            
            <div class="code-line" style="margin-top: 15px;"><strong>[1] Les KPI Cibles (Condition de Maintien) :</strong></div>
            <div class="code-line">- Un Taux de Présence > 50% (Mesuré sur les inscrits confirmés à J-2 pour neutraliser les no-shows).</div>
            <div class="code-line">- Un CPA (Coût Par Acquisition) plafonné fermement à <strong>200 €</strong>, garantissant un seuil de rentabilité dès la 1ère année.</div>
            
            <div class="code-line" style="margin-top: 20px;"><strong>[2] Gestion de l'Écart Initial (Le 1er Échec) :</strong></div>
            <div class="code-line">- Si un événement échoue (CPA > 200€), une analyse causale immédiate est imposée au COPIL : Heure inadaptée ? Mauvais profilage DISC de l'invité par le SDR ? Un correctif est voté pour l'itération N+1.</div>
            
            <div class="code-line" style="margin-top: 20px;"><strong>[3] Gestion de l'Écart Persistant (La Réingénierie) :</strong></div>
            <div class="code-line">- Au 2ème échec consécutif, le format est <strong>downgradé financièrement</strong>. Plutôt qu'une annulation sèche destructrice d'image, l'événement est transformé en "Atelier de réflexion collective". Les frais externes (Traiteur lourd) sont coupés. L'acquisition est mise en pause au profit exclusif de la Rétention (animation du réseau existant à coût logistique quasi-nul).</div>
        </div>
    """
})

# PAGE 22
pages.append({
    "section": "CHAPITRE 8 : LE PLAN D'ACTION (SUITE)",
    "content": """
        <h2>3. Objectifs à M12 et Déploiement Opérationnel</h2>

        <p>Le déploiement de ce plan d'action hybride (Acquisition Inbound + Rétention par la Preuve) doit permettre l'atteinte d'objectifs de fin d'exercice clairs pour l'entreprise :</p>
        
        <ul style="font-size: 10.5pt; line-height: 1.8;">
            <li><strong>Métrique d'Acquisition :</strong> Atteindre un rythme de croisière cible de 3 adhésions fermes par événement (CPA projeté de 166 €).</li>
            <li><strong>Métrique de Rétention :</strong> Casser la courbe d'attrition et prolonger la LTV (actuellement bloquée à 290€) pour viser une stabilisation du parc actif grâce au choc de la "Preuve de Valeur" trimestrielle.</li>
            <li><strong>Impact Organisationnel Fort :</strong> Ce plan dépasse le cadre commercial. Il acte une montée en maturité psychologique de la force de vente (qui passe de "téléprospecteur à froid" à "sélectionneur de réseau").</li>
        </ul>

        <div class="expert-note" style="margin-top: 40px; font-size: 10.5pt;">
            <strong>Transition vers le Bilan Personnel (Chapitre 9)</strong><br>
            L'analyse du marché (Loi ALUR, OTAs), la conception du pivot d'acquisition et le plan de pilotage financier (CPA, LTV/CAC) étant formellement établis, il convient de dresser le bilan réflexif de cette immersion stratégique et de l'évolution de mes compétences face à cette complexité "Big Data".
        </div>
    """
})

# PAGE 23
pages.append({
    "section": "CHAPITRE 9 : BILAN & PROFIL",
    "content": """
        <a id="chapitre-9"></a>
        <h1>Chapitre 9 — Bilan Personnel & CV Digital</h1>
        
        <h2>Prise de recul sur la complexité de la mission</h2>
        
        <p>Ce parcours de consulting intégré au sein de la gouvernance de Happy House a constitué un point d'inflexion majeur dans mon évolution professionnelle. J'y ai appris une leçon d'humilité stratégique : <strong>la Data et les algorithmes de croissance ne sont rien s'ils se heurtent au mur de la gouvernance ou à la réalité sociologique d'un marché saturé (La fatigue numérique et légale de la cible).</strong></p>
        
        <p>Mon expertise technique initiale (le Web-Scraping intensif, la gestion de bases de 126 000 lignes, la maîtrise des flux d'automatisation via n8n) m'a poussé vers une première recommandation "technocentrée" de Cold Emailing. La confrontation de cette hypothèse avec le "véto identitaire" de la direction a été le moment le plus formateur de cette alternance.</p>
        
        <p>La validation du pivot stratégique final (l'abandon de mon propre modèle d'automatisation logicielle pour concevoir de toutes pièces une stratégie Inbound événementielle, beaucoup plus "organique") témoigne de l'acquisition d'une compétence fondamentale visée par Rocket School : <strong>la maturité politique en entreprise.</strong></p>
        
        <p>Un bon "Directeur du Développement" ne cherche pas à vendre l'outil technologique le plus moderne à sa direction. Il écoute les peurs de son marché (ALUR), il intègre l'ADN de sa marque (Premium), et il pilote le risque financier (Ratio LTV/CAC) tout en s'assurant de l'adhésion humaine de son équipe (Méthodologie DISC avec Younes).</p>
    """
})


# PAGE 21.5 : GUIDE LOGISTIQUE
pages.append({
    "section": "CHAPITRE 8 : LE GUIDE DE L'INBOUND",
    "content": """
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
    """
})

# PAGE 24
pages.append({
    "section": "CHAPITRE 9 : CV DIGITAL",
    "content": """
        <h2>Positionnement et Projection (Le Profil Hybride)</h2>

        <div class="glass-card" style="border: 1px solid var(--gold); padding: 30px;">
            <div class="visual-title" style="color: var(--gold); font-size: 14pt; margin-bottom: 20px;">JULIEN FLORENCE</div>
            <p style="font-size: 11pt; line-height: 1.6; text-align: center; color: var(--gold-light); margin-bottom: 30px;">
                <em>"De l'Excellence Opérationnelle de l'Hospitalité au Pilotage Stratégique Data-Driven"</em>
            </p>
            
            <p style="font-size: 10pt; line-height: 1.6;">
                Fort d'un ADN exigeant forgé dans les standards de l'Hospitalité de luxe et de la Sommellerie internationale (où la rigueur du <strong>"Service Client Extrême"</strong> et la création de <strong>"l'Effet Waouh"</strong> sont des impératifs quotidiens), j'ai opéré une reconversion totale vers le pilotage stratégique de la croissance (Growth Hacking, Data Analysis, Workflow Automation).<br><br>
                
                <strong>Ma Valeur Ajoutée (Le Profil Hybride) :</strong><br>
                Ma singularité réside dans la fusion de ces deux univers : la capacité à concevoir et coder des architectures d'acquisition numériques complexes (Manipulation Data, Automatisation), sans jamais perdre de vue que la finalité d'un business Premium repose toujours sur l'interaction humaine qualitative et la rétention par la preuve mathématique (ROI).<br><br>
                
                <strong>Soft Skills Majeurs :</strong><br>
                • Leadership transversal (Conduite du changement auprès de la force de vente).<br>
                • Résilience et Agilité (Acceptation de l'échec d'une hypothèse pour pivoter).<br>
                • Capacité d'arbitrage financier (Maîtrise des ratios CAC / LTV / CPA).<br>
                • Écoute terrain et profilage cognitif (Méthode DISC / Analyse Comportementale).<br><br>
                
                <strong>Projection à Court Terme :</strong><br>
                Accéder à des fonctions de Direction du Développement et de la Stratégie (Secteur Hospitalité / Hospitality Tech / Solutions B2B Premium).
            </p>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="https://www.linkedin.com/in/julien-florence-2536a083" target="_blank" class="btn-nav" style="background: var(--gold); color: #000; font-weight: bold; width: 100%; max-width: 400px; padding: 15px;">
                    🔗 CONSULTER MON PROFIL LINKEDIN (CV)
                </a>
            </div>
        </div>
    """
})

# PAGE 25
pages.append({
    "section": "CHAPITRE 10 : CONFORMITÉ IA",
    "content": """
        <a id="chapitre-10"></a>
        <h1>Chapitre 10 — Déclaration de Conformité IA</h1>
        
        <h2>Cadre de rédaction et exigence de transparence</h2>
        <p>Afin de répondre avec la plus grande rigueur aux exigences académiques de transparence stipulées dans le guide méthodologique, cette page documente explicitement la manière dont les outils d'Intelligence Artificielle générative ont été intégrés dans le processus de formalisation de ce rapport.</p>
        
        <p>L'IA a été employée <strong>exclusivement</strong> comme un outil technologique d’assistance à la structuration formelle de haut niveau et au rendu visuel interactif. Les contenus bruts fournis ont ensuite été systématiquement relus, vérifiés et contextualisés personnellement afin de garantir l'absolue authenticité de la démarche intellectuelle et l'exactitude des faits rapportés au sein du réseau Happy House.</p>

        <div class="glass-card" style="border-left: 4px solid var(--gold); margin-top: 30px; padding: 25px;">
            <ul style="margin:0; padding-left: 15px; font-size: 10.5pt; line-height: 1.8;">
                <li><strong>Outil technologique mobilisé :</strong> Modèle de langage Gemini (via interface CLI en environnement local).</li>
                <li><strong>Périmètre strict d'intervention de l'algorithme :</strong> Aide à la reformulation syntaxique (pour aligner le texte sur le ton "Consulting Expert" des standards académiques), et génération intégrale du code informatique (HTML/CSS embarqué via un script d'assemblage Python) nécessaire à la mise en page avancée du document PDF final.</li>
                <li><strong>Responsabilité exclusive de l'auteur (Déclaration sur l'honneur) :</strong> L'intégralité du diagnostic analytique de l'entreprise, les choix d'évaluation de la matrice d'analyse (PESTEL, SWOT, Porter), la compréhension et l'explication des blocages stratégiques (Loi ALUR, le veto et le pivot Inbound), la conception du plan d'action (le Dashboard), ainsi que 100% des données chiffrées relatives à l'activité (ARPU à 226€, Ratio LTV/CAC catastrophique, métriques du cas Durentie, l'audit des 14500 appels et 126k prospects) constituent un travail d'audit rigoureusement personnel, factuel et sourcé conjointement avec la Direction Data (R. Marie-Luce).</li>
            </ul>
        </div>
        
        <p style="text-align: center; margin-top: 30px; color: var(--gold); font-style: italic;">
            "L'outil algorithmique n'a produit aucun concept métier ni aucune réflexion analytique autonome, agissant uniquement comme un ouvrier de structuration formelle sous ma direction stratégique."
        </p>
    """
})

# --- ANNEXES PHYSIQUES ---

# PAGE 26
pages.append({
    "section": "ANNEXE 1 : MATRICE PESTEL",
    "content": """
        <a id="annexe-1"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXE 1 : L'Analyse Macro (PESTEL)</h1>
        
        <p style="font-size: 10.5pt; text-align: justify; margin-bottom: 30px;">
            Cet outil d'analyse macro-environnementale justifie empiriquement le "moment de marché". Il démontre pourquoi les services de Happy House (Cost-Killing et Accompagnement de l'Indépendant) répondent à une urgence structurelle du secteur de l'hébergement en 2024-2026.
        </p>

        <table style='width: 100%; border-collapse: collapse; font-size: 10pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 25%; padding: 15px;'>Dimension Macro</th><th style='padding: 15px;'>Analyse des Forces et Impact Direct sur le Réseau Happy House</th></tr>
            <tr>
                <td style='padding: 15px;'><strong>P — Politique & Légal</strong></td>
                <td style='padding: 15px;'>Déploiement implacable de la <strong>Loi anti-Airbnb et Loi ALUR</strong> (interdiction de louer des passoires thermiques classées DPE G dès 2025, obligation d'enregistrement, quota de 120 jours). Purge mécanique estimée à 20-25% des acteurs amateurs du marché. <br><br><em style="color: var(--gold);">Impact Stratégique : Justifie notre filtrage de la base de 126k prospects pour isoler les 30% de professionnels et nous protéger du Churn Réglementaire.</em></td>
            </tr>
            <tr>
                <td style='padding: 15px;'><strong>E — Économique</strong></td>
                <td style='padding: 15px;'>Hyper-inflation des coûts opérationnels incompressibles (+15% d'augmentation sur les factures d'énergie constatée en 2024). <br><br><em style="color: var(--gold);">Impact Stratégique : Fort levier d'acquisition via notre centrale d'achat (Entegra). Le ROI devient un argument vital face au "Mur du Silence".</em></td>
            </tr>
            <tr>
                <td style='padding: 15px;'><strong>S — Socioculturel</strong></td>
                <td style='padding: 15px;'>Mutation des attentes B2C vers la recherche d'expériences "authentiques, locales et de caractère" (Le mouvement du Slow Tourism post-Covid). <br><br><em style="color: var(--gold);">Impact Stratégique : Validation absolue de la pertinence de notre ciblage focalisé sur le "Premium & Charme".</em></td>
            </tr>
            <tr>
                <td style='padding: 15px;'><strong>T — Technologique</strong></td>
                <td style='padding: 15px;'>Renforcement du quasi-monopole des grandes OTAs (Booking, Airbnb) qui captent jusqu'à 71% des nuitées en ligne en Europe. <br><br><em style="color: var(--gold);">Impact Stratégique : L'hébergeur est harcelé. Cela invalide la prospection Outbound de masse et impose notre pivot Inbound.</em></td>
            </tr>
            <tr>
                <td style='padding: 15px;'><strong>E — Écologique</strong></td>
                <td style='padding: 15px;'>Forte pression normative pour l'intégration de processus de développement durable dans l'hospitalité (Explosion des certifications type Clef Verte à +184%). <br><br><em style="color: var(--gold);">Impact Stratégique : Source de "fatigue administrative" qui nécessite notre réassurance physique lors des Afterworks.</em></td>
            </tr>
        </table>
    """
})

# PAGE 27
pages.append({
    "section": "ANNEXE 2 : MATRICE SWOT",
    "content": """
        <a id="annexe-2"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXE 2 : Le Diagnostic Croisé (SWOT)</h1>
        
        <p style="font-size: 10.5pt; text-align: justify; margin-bottom: 30px;">
            La matrice SWOT confronte les observations du marché (PESTEL) aux réalités comptables et opérationnelles du réseau Happy House. C'est cette matrice qui a mis en lumière l'équation du naufrage (Ratio LTV/CAC) et imposé la répartition des missions (Rétention / Acquisition Inbound).
        </p>

        <table style='width: 100%; border-collapse: collapse; font-size: 10pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'>
                <th style='width: 50%; text-align: center; padding: 20px; font-size: 12pt;'>FORCES (Capacités Internes)</th>
                <th style='width: 50%; text-align: center; padding: 20px; font-size: 12pt; color: #E74C3C;'>FAIBLESSES (Failles Internes)</th>
            </tr>
            <tr>
                <td style='height: 180px; padding: 25px; line-height: 1.8;'>
                    <span style="color: var(--gold); font-weight: bold;">Le Produit :</span> Partenariat exclusif validé avec la centrale d'achats Entegra (Générateur avéré d'économies nettes, cf. Cas Durentie).<br><br>
                    <span style="color: var(--gold); font-weight: bold;">L'Actif Data :</span> Base de données d'acquisition propriétaire de 126 000 contacts, purifiée à 30% de pros via le filtre Loi ALUR.<br><br>
                    <span style="color: var(--gold); font-weight: bold;">La Marque :</span> Positionnement d'expert "Premium & Charme" reconnu par le cœur de réseau historique (170 membres).<br><br>
                </td>
                <td style='padding: 25px; line-height: 1.8;'>
                    <span style="color: #E74C3C; font-weight: bold;">Le Gouffre de l'Acquisition :</span> Stratégie de prospection (Cold Calling) intenable. CAC évalué à 1823€ face à un ARPU de 226€ (Ratio LTV/CAC effondré à 0,16).<br><br>
                    <span style="color: #E74C3C; font-weight: bold;">L'Hémorragie de l'Attrition :</span> Taux de Churn sévère ("Silence Radio") sur la cohorte d'acquisition Outbound (80% d'attrition sur les 146 dossiers démarchés à froid entre 2022 et 2025).<br><br>
                    <span style="color: #E74C3C; font-weight: bold;">Le Management de la Valeur :</span> Défaut systémique de formalisation du ROI. Le client ne "voit" pas les économies qu'il réalise (absence historique de Dashboard).
                </td>
            </tr>
            <tr style='background: rgba(221, 168, 62, 0.2);'>
                <th style='text-align: center; padding: 20px; font-size: 12pt; color: #2ECC71;'>OPPORTUNITÉS (Leviers Externes)</th>
                <th style='text-align: center; padding: 20px; font-size: 12pt; color: #E74C3C;'>MENACES (Risques Externes)</th>
            </tr>
            <tr>
                <td style='height: 160px; padding: 25px; line-height: 1.8;'>
                    <span style="color: #2ECC71; font-weight: bold;">La Purge Légale :</span> L'élimination des loueurs amateurs (Airbnb) via la loi ALUR et le DPE libère de l'air pour les professionnels.<br><br>
                    <span style="color: #2ECC71; font-weight: bold;">L'Urgence Financière :</span> Le besoin vital d'accompagnement (cost-killing) pour faire face à la flambée de l'inflation (énergie, blanchisserie).
                </td>
                <td style='padding: 25px; line-height: 1.8;'>
                    <span style="color: #E74C3C; font-weight: bold;">Le Monopole Tech :</span> L'hégémonie prédatrice des OTAs, où le leader Booking contrôle à lui seul 71% des flux en Europe.<br><br>
                    <span style="color: #E74C3C; font-weight: bold;">Le Rejet de la Cible :</span> La "Fatigue Numérique" des prospects, qui entraîne un rejet pavlovien du démarchage de masse (le "Brand Damage" empêchant d'utiliser l'automatisation n8n).
                </td>
            </tr>
        </table>
    """
})

# PAGE 28
pages.append({
    "section": "ANNEXE 3 : FORCES DE PORTER",
    "content": """
        <a id="annexe-3"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXE 3 : Les 5 Forces de Porter</h1>
        
        <p style="font-size: 10.5pt; text-align: justify; margin-bottom: 30px;">
            L'analyse structurelle des 5 Forces de Porter modélise le rapport de force (Intensité Concurrentielle) que subit Happy House sur son marché d'évolution.
        </p>

        <table style='width: 100%; border-collapse: collapse; font-size: 10.5pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 30%; padding: 15px;'>Axe de la Force Concurrentielle</th><th style='width: 20%; padding: 15px;'>Évaluation de l'Intensité</th><th style='padding: 15px;'>Justification Analytique (Impact)</th></tr>
            <tr>
                <td style='padding: 15px;'><strong>Intensité Concurrentielle Interne</strong> (Entre acteurs du conseil et de la Tech hôtelière)</td>
                <td style="color: #E74C3C; font-weight: bold; font-size: 12pt; text-align: center;">Forte<br>(4/5)</td>
                <td style='padding: 15px; line-height: 1.6;'>L'espace concurrentiel est saturé (vendeurs de PMS, experts en Yield Management). L'hébergeur Premium est sur-sollicité, ce qui détruit l'attention accordée au démarchage.</td>
            </tr>
            <tr>
                <td style='padding: 15px;'><strong>Menace Nouveaux Entrants</strong> (Risque de nouveaux concurrents pour Happy House)</td>
                <td style="color: #2ECC71; font-weight: bold; font-size: 12pt; text-align: center;">Faible<br>(2/5)</td>
                <td style='padding: 15px; line-height: 1.6;'>Cibler le segment "Premium" requiert une expertise métier et des actifs data difficiles à répliquer. Le ticket d'entrée intellectuel et le réseau établi sont une forte barrière de protection.</td>
            </tr>
            <tr>
                <td style='padding: 15px;'><strong>Pouvoir Négociation (Clients/OTAs)</strong></td>
                <td style="color: #E74C3C; font-weight: bold; font-size: 12pt; text-align: center;">Très Fort<br>(5/5)</td>
                <td style='padding: 15px; line-height: 1.6;'>Les géants technologiques (Booking, Expedia) imposent unilatéralement leurs commissions. Les hébergeurs sont sous perfusion de leur visibilité algorithmique.</td>
            </tr>
            <tr>
                <td style='padding: 15px;'><strong>Pouvoir Négociation (Fournisseurs)</strong> (Énergie, F&B, Équipementiers)</td>
                <td style="color: #F1C40F; font-weight: bold; font-size: 12pt; text-align: center;">Moyen à Fort<br>(3,5/5)</td>
                <td style='padding: 15px; line-height: 1.6;'>Les fournisseurs d'énergie et de denrées sont en position de force absolue face à l'inflation globale. <em>C'est la justification du modèle de massification des achats via Entegra.</em></td>
            </tr>
            <tr>
                <td style='padding: 15px;'><strong>Menace des Substituts</strong> (Pour le voyageur)</td>
                <td style="color: #F1C40F; font-weight: bold; font-size: 12pt; text-align: center;">Moyenne<br>(3/5)</td>
                <td style='padding: 15px; line-height: 1.6;'>L'hôtellerie de chaîne standardisée s'oppose au concept d'hébergement "de charme", forçant nos membres à justifier sans cesse leur positionnement Premium.</td>
            </tr>
        </table>
    """
})

# PAGE 29
pages.append({
    "section": "ANNEXE 4 : COMPARATIF D'ACQUISITION",
    "content": """
        <a id="annexe-4"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXE 4 : La Condamnation de l'Outbound</h1>
        
        <p style="font-size: 10.5pt; text-align: justify; margin-bottom: 30px;">
            Modélisation comptable stricte (Alignement de données) démontrant que la stratégie Outbound initiale est "mathématiquement condamnée" face à la rentabilité projetée du pivot stratégique Inbound.
        </p>

        <div class="visual-block" style="border-color: #E74C3C; padding: 25px; margin-bottom: 30px;">
            <div class="visual-title" style="color: #E74C3C; font-size: 12pt;">1. L'IMPÉRATIF D'ABANDON : L'OUTBOUND DE MASSE (Cold Calling)</div>
            
            <p style="color: #FFF; font-size: 10pt; margin-top: 15px; margin-bottom: 10px;"><strong>Audit du Tunnel d'Acquisition (SDR) :</strong></p>
            <div class="code-line" style="font-size: 10pt;">- <strong>Coût Salarial SDR :</strong> 1 823 € nets / mois (SMIC apprenti >26 ans). L'effort d'appels à froid occupe 100% de la bande passante.</div>
            <div class="code-line" style="font-size: 10pt; margin-top: 8px;">- <strong>Effort Métrique Brut :</strong> <strong>14 500 appels</strong> générés sur une cohorte d'analyse de 48 semaines (moyenne stricte de 300 appels/semaine). Taux de non-réponse de 50%, et 40% de refus francs.</div>
            <div class="code-line" style="font-size: 10pt; margin-top: 8px;">- <strong>Résultat du Tunnel (Conversion) :</strong> Le taux de closing avéré ne s'élève qu'à <strong>1 signature formelle / mois</strong>.</div>
            
            <div style="background: rgba(231, 76, 60, 0.15); padding: 15px; margin-top: 25px; border-left: 4px solid #E74C3C;">
                <div class="code-line" style="color: #E74C3C; font-weight: bold; font-size: 14pt;">=> Coût d'Acquisition Client (CAC) : 1 823 € par Membre.</div>
                <div class="code-line" style="color: #FFF; font-size: 10pt; margin-top: 10px;"><em>Conclusion Stratégique : Avec un Revenu Moyen par Utilisateur (ARPU) estimé à 226€/an, et une LTV bloquée à 290€ à cause du Churn, le Ratio LTV/CAC s'effondre à 0,16. L'acquisition Outbound est 6 à 8 fois trop chère. Le modèle est condamné.</em></div>
            </div>
        </div>

        <div class="visual-block" style="border-color: #2ECC71; padding: 25px;">
            <div class="visual-title" style="color: #2ECC71; font-size: 12pt;">2. LE MODÈLE DE SAUVETAGE : INBOUND (Afterworks Régionaux)</div>
            
            <p style="color: #FFF; font-size: 10pt; margin-top: 15px; margin-bottom: 10px;"><strong>Les variables de modélisation (Le Crash-Test) :</strong></p>
            <div class="code-line" style="font-size: 10pt;">- <strong>Budget d'exécution :</strong> Une enveloppe fermée d'organisation (Traiteur, Logistique) évaluée à <strong>~500 € par événement régional</strong>. L'invitation est réservée à 30 prospects hyper-qualifiés extraits du fichier Data initial.</div>
            <div class="code-line" style="font-size: 10pt; margin-top: 8px;">- <strong>Objectif de clôture plancher :</strong> Fixation d'une conversion de 10% des présents, soit <strong>3 signatures par événement</strong>.</div>
            
            <div style="background: rgba(46, 204, 113, 0.15); padding: 15px; margin-top: 25px; border-left: 4px solid #2ECC71;">
                <div class="code-line" style="color: #2ECC71; font-weight: bold; font-size: 14pt;">=> Coût Par Acquisition (CPA) Projeté Cible : 166 € par Membre.</div>
                <div class="code-line" style="color: #FFF; font-size: 10pt; margin-top: 10px;"><em>Conclusion Stratégique : Le CPA descend en dessous de l'ARPU (226€). C'est la seule arithmétique compatible avec les prix de vente de l'entreprise.</em></div>
            </div>
        </div>
    """
})

# PAGE 30
pages.append({
    "section": "ANNEXE 5 & 10 : CHURN & DURENTIE",
    "content": """
        <a id="annexe-5"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXE 5 & 10 : Attrition & Rentabilité Nette</h1>
        
        <h2 style='font-size: 14pt; color: #E74C3C; margin-bottom: 15px;'>Annexe 5 : Le Bilan du Churn Outbound</h2>
        <p style='font-size: 10.5pt; text-align: justify; line-height: 1.6;'>L'audit du portefeuille historique a révélé un <strong>"Silence Radio" de 80% sur la cohorte d'acquisition Outbound (146 dossiers démarchés à froid entre 2022 et 2025)</strong>. Ce Churn massif détruit la Lifetime Value (LTV), figée à 290€. Ce contraste avec la stabilité du réseau historique (170 membres acquis organiquement par bouche-à-oreille) prouve définitivement que l'Outbound génère une base de clientèle infidèle. La mise en place du Dashboard ROI (Piloté par J. Florence) et de la Demande Organique Inbound (Pilotée par R. Marie-Luce) est la réponse conjuguée à cet effondrement.</p>

        <a id="annexe-10"></a>
        <h2 style='font-size: 14pt; color: #2ECC71; margin-top: 40px; margin-bottom: 15px;'>Annexe 10 : La Validation Comptable (Cas Durentie)</h2>
        <p style='font-size: 10.5pt; text-align: justify; line-height: 1.6;'>Simulation comptable extraite du dossier d'un domaine Premium suite à son adhésion (Application des remises de la centrale d'achats Entegra). C'est la Master Data du futur Dashboard.</p>

        <table style='width: 100%; border-collapse: collapse; font-size: 11pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 60%; padding: 15px;'>Poste Financier Analysé</th><th style='padding: 15px;'>Impact Comptable Mesuré (€)</th></tr>
            <tr><td style='padding: 15px;'><strong>Investissement Initial</strong><br><span style='font-size: 9pt; color: #888;'>Cotisation d'adhésion au réseau Happy House</span></td><td style="color: #E74C3C; font-weight: bold; padding: 15px; font-size: 12pt;">- 360,00 €</td></tr>
            
            <tr><td style='padding: 15px;'><strong>Économies F&B (Alimentation & Boissons)</strong><br><span style='font-size: 9pt; color: #888;'>Remises exclusives appliquées sur les volumes via Entegra</span></td><td style="color: #2ECC71; padding: 15px;">+ 2 150,00 €</td></tr>
            
            <tr><td style='padding: 15px;'><strong>Économies Énergie</strong><br><span style='font-size: 9pt; color: #888;'>Bouclier tarifaire sur factures (électricité/gaz)</span></td><td style="color: #2ECC71; padding: 15px;">+ 1 420,00 €</td></tr>
            
            <tr><td style='padding: 15px;'><strong>Économies Blanchisserie / Équipement</strong><br><span style='font-size: 9pt; color: #888;'>Renégociation des contrats d'entretien</span></td><td style="color: #2ECC71; padding: 15px;">+ 910,00 €</td></tr>
            
            <tr style='border-top: 2px solid var(--gold); background: rgba(255,255,255,0.05);'>
                <td style='padding: 15px;'><strong>BÉNÉFICE NET STRICTEMENT OPÉRATIONNEL</strong><br><span style='font-size: 9pt; color: #888;'>Économies passives nettes déduction faite de la cotisation</span></td>
                <td style="color: var(--gold); font-weight: bold; padding: 15px; font-size: 13pt;">+ 4 120,00 €</td>
            </tr>
            
            <tr><td style='padding: 15px;'><strong>Chiffre d'Affaires Actif Généré</strong><br><span style='font-size: 9pt; color: #888;'>Apport de clientèle qualifiée d'un membre à un autre</span></td><td style="color: #2ECC71; padding: 15px;">+ 11 000,00 €</td></tr>
            
            <tr style='background: rgba(46, 204, 113, 0.1); border-top: 3px solid #2ECC71;'>
                <td style='padding: 20px; font-size: 12pt;'><strong>IMPACT GLOBAL SUR LA TRÉSORERIE</strong></td>
                <td style='padding: 20px;'><strong style="color: #2ECC71; font-size: 16pt;">+ 15 120,00 €</strong></td>
            </tr>
        </table>
    """
})

# PAGE 31
pages.append({
    "section": "ANNEXE 6 & 7 : SCRIPT & MÉTHODE",
    "content": """
        <a id="annexe-6"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXE 6 & 7 : Le Pivot du Script SDR</h1>
        
        <p style="font-size: 10.5pt; text-align: justify; margin-bottom: 25px; line-height: 1.6;">La révision stratégique de l'acquisition a imposé d'abandonner le "Tir de barrage" (le pitch de vente direct qui générait 40% de refus francs par angoisse de la cible). Le SDR (Younes) a dû être reformé pour basculer sur une méthodologie de <strong>"Sélection Inbound"</strong> (On ne vend rien, on offre une invitation VIP issue d'un profilage des 126k contacts).</p>

        <div class='glass-card' style='font-size: 10.5pt; padding: 30px;'>
            <div class="visual-title" style="color: var(--gold); font-size: 13pt; margin-bottom: 20px;">LA NOUVELLE TRAME DE QUALIFICATION (Extrait)</div>
            
            <p style='margin-top: 15px; color: #FFF; font-size: 11pt;'><strong>ÉTAPE 1 : L'ACCROCHE (Désamorcer le bouclier commercial)</strong><br>
            <span style='color: #FFFFFF; font-size: 10.5pt; line-height: 1.5;'><br>L'objectif des 5 premières secondes est de créer un choc de statut (On vous a remarqué).<br>
            <em style='color: #A9B7C6; display: block; background: rgba(0,0,0,0.3); padding: 15px; margin-top: 10px; border-left: 3px solid #A9B7C6;'>« Bonjour [Prénom de l'exploitant], c’est Younes, en charge de la sélection pour le réseau Happy House. Je vous appelle directement aujourd'hui car nous organisons un événement privé à huis clos pour les meilleurs hébergeurs premium de [Région] le [Date]. Vu la réputation de votre domaine, votre profil correspond à notre filtre d'invités. »</em></span></p>
            
            <p style='margin-top: 30px; color: #FFF; font-size: 11pt;'><strong>ÉTAPE 2 : LA QUALIFICATION PSYCHOLOGIQUE (Méthode DISC)</strong><br>
            <span style='color: #FFFFFF; font-size: 10.5pt; line-height: 1.5;'><br>Le SDR doit identifier la "douleur" de l'interlocuteur dans les secondes qui suivent.<br><br>
            <strong>Scénario A : Le profil "Dominant" (D) / Rationnel</strong> (Angoissé par ses marges).<br>
            <em style='color: #A9B7C6; display: block; background: rgba(0,0,0,0.3); padding: 15px; margin-top: 10px; border-left: 3px solid #E74C3C;'>« L'objectif sera d'aborder avec des chiffres réels les leviers qui permettent aujourd'hui de contrer l'inflation et d'abaisser les charges d'un établissement comme le vôtre via le modèle de la centrale Entegra. »</em><br><br>
            <strong>Scénario B : Le profil "Influent" (I) / Relationnel</strong> (Souffrant de l'isolement).<br>
            <em style='color: #A9B7C6; display: block; background: rgba(0,0,0,0.3); padding: 15px; margin-top: 10px; border-left: 3px solid #2ECC71;'>« Ce format en petit comité sera l'occasion d'échanger en toute transparence avec vos pairs de la région sur la complexité commune à tous : gérer la distribution face à Booking. »</em></span></p>
            
            <p style='margin-top: 30px; color: #FFF; font-size: 11pt;'><strong>ÉTAPE 3 : LA CLÔTURE (Imposer le principe d'exclusivité)</strong><br>
            <span style='color: #FFFFFF; font-size: 10.5pt; line-height: 1.5;'><br>Ne pas chercher l'accord forcé, créer la notion de privilège ("Fear Of Missing Out").<br>
            <em style='color: #A9B7C6; display: block; background: rgba(0,0,0,0.3); padding: 15px; margin-top: 10px; border-left: 3px solid var(--gold);'>« Je vous rassure, l'accès à la rencontre est strictement sur invitation et gratuit. Si cela fait sens pour vous, je vous fais parvenir le lien d'inscription privé. Vous pourrez y croiser physiquement [Nom d'un domaine membre] qui sera présent. On bloque votre nom ? »</em></span></p>
        </div>
    """
})


# PAGE 32.5
pages.append({
    "section": "ANNEXE 8 : OUTILS D'ACQUISITION (CRM & NURTURING)",
    "content": """
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
    """
})

# PAGE 32
pages.append({
    "section": "ANNEXE 9 : DATA MACRO",
    "content": """
        <a id="annexe-9"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXE 9 : La Pression Commerciale Externe</h1>
        
        <p style="font-size: 10.5pt; text-align: justify; margin-bottom: 30px; line-height: 1.6;">
            Cette annexe justifie objectivement "l'étouffement" numérique de la cible Premium, expliquant le rejet massif constaté en prospection lors de nos 14 500 appels Outbound.
        </p>

        <h2 style='font-size: 13pt; margin-top: 20px; color: var(--gold-light);'>1. L'Hégémonie Absolue des OTAs (Marché Européen)</h2>
        <table style='width: 100%; border-collapse: collapse; font-size: 10.5pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 15%; padding: 15px;'>Échéance</th><th style='width: 60%; padding: 15px;'>Indicateur de Mesure Sectoriel</th><th style='width: 25%; padding: 15px;'>Valeur Monitorée</th></tr>
            <tr><td style='padding: 15px;'>2013</td><td style='padding: 15px;'>Part de marché globale des Agences en Ligne (OTAs)</td><td style='padding: 15px;'>19,7 %</td></tr>
            <tr style="background: rgba(255,255,255,0.05);"><td style='padding: 15px; font-weight: bold;'>2023</td><td style='padding: 15px; font-weight: bold;'>Part de marché globale des Agences en Ligne</td><td style='padding: 15px;'><strong style="color: #E74C3C; font-size: 12pt;">29,6 %</strong></td></tr>
            
            <tr><td style='padding: 15px;'>2024</td><td style='padding: 15px;'>Poids de l'acteur hégémonique : <strong>Booking.com</strong></td><td style='padding: 15px;'><strong style="color: #E74C3C; font-size: 12pt;">69,3 %</strong> (du flux OTA)</td></tr>
            <tr><td style='padding: 15px;'>2024</td><td style='padding: 15px;'>Poids du challenger nord-américain : <strong>Expedia</strong></td><td style='padding: 15px;'>11,5 % (du flux OTA)</td></tr>
        </table>
        
        <h2 style='font-size: 13pt; margin-top: 40px; color: var(--gold-light);'>2. L'Inflation des Certifications & L'Anxiété Écologique</h2>
        <table style='width: 100%; border-collapse: collapse; font-size: 10.5pt; margin-top: 20px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 15%; padding: 15px;'>Échéance</th><th style='width: 60%; padding: 15px;'>Indicateur Sectoriel (Données Marché France)</th><th style='width: 25%; padding: 15px;'>Volume (État)</th></tr>
            <tr><td style='padding: 15px;'>2022</td><td style='padding: 15px;'>Volume d'établissements détenant le label "Clef Verte"</td><td style='padding: 15px;'>855 établissements</td></tr>
            <tr style="background: rgba(255,255,255,0.05);"><td style='padding: 15px; font-weight: bold;'>2025</td><td style='padding: 15px; font-weight: bold;'>Projection établissements "Clef Verte"</td><td style='padding: 15px;'><strong style="color: var(--gold); font-size: 12pt;">2 428 (+184%)</strong></td></tr>
            <tr><td style='padding: 15px;'>2024</td><td style='padding: 15px;'>Fin du Label historique "Qualité Tourisme"</td><td style='padding: 15px;'>5 000 établissements</td></tr>
            <tr><td style='padding: 15px; font-weight: bold;'>2026</td><td style='padding: 15px; font-weight: bold;'>Label d'État "Qualité Tourisme"</td><td style='padding: 15px;'><strong style="color: #E74C3C;">Disparition Actée</strong></td></tr>
        </table>
        
        <div class="expert-note" style="margin-top: 30px; padding: 25px;">
            <strong>Analyse : Le Mythe de "L'Outil Supplémentaire"</strong><br><br>
            Côté distribution, l'hébergeur est écrasé, réduit au statut de figurant face à la toute-puissance punitive des algorithmes mondialisés (Booking à 70%). Côté administratif, il est noyé sous la complexité des certifications mouvantes et de la loi ALUR.<br><br>
            Dans un écosystème en telle surchauffe, l'hébergeur Premium devient hermétique aux promesses d'acquisition téléphonique. <strong>Il a un besoin viscéral d'un partenaire physique, d'un pair, et d'un climat de confiance.</strong> Ce contexte verrouille et prouve la nécessité indiscutable du pivot stratégique : seule la Rencontre Physique (Les Afterworks Inbound in situ) peut percer la carapace du prospect.
        </div>
    """
})

# PAGE 33
pages.append({
    "section": "DOSSIER DES PREUVES CLOUD",
    "content": """
        <a id="annexe-links"></a>
        <h1 style='color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px;'>ANNEXES : DOSSIER DES PREUVES EXTERNES</h1>
        
        <p style="font-size: 10.5pt; text-align: center; margin-bottom: 40px; line-height: 1.6; color: var(--text-muted);">
            Les documents opérationnels bruts, les livrables contractuels (non floutés) et les tableaux de pilotage de type "Big Data" (incompatibles avec le format A4) ont été sécurisés, chiffrés et stockés sur une infrastructure Cloud dédiée. <br>Vous pouvez ordonner leur ouverture dans un navigateur externe en un clic via le panneau de commande centralisé ci-dessous.
        </p>

        <div style="display: flex; flex-direction: column; gap: 15px; align-items: center;">
            <h2 style='font-size: 12pt; color: var(--gold-light); margin-bottom: 10px; margin-top: 0;'>A. LIVRABLES CLIENTS & MATRICES FINANCIÈRES</h2>
            
            <a href="https://drive.google.com/file/d/1OoDtqvV-s1TELt1J17h7HyKzHJqrdiIQ/view?usp=drive_link" target="_blank" class="btn-nav" style="width: 85%; font-size: 10.5pt; text-align: left; padding-left: 30px;">
                <span style="display: inline-block; width: 30px;">📄</span> <strong>[Archive 1]</strong> Pack Communication & Identité de Marque
            </a>
            
            <a href="https://drive.google.com/file/d/1kE7TUcKFbJkPhW6H4-cSR-xk0HBUzmy5/view?usp=drive_link" target="_blank" class="btn-nav" style="width: 85%; font-size: 10.5pt; text-align: left; padding-left: 30px;">
                <span style="display: inline-block; width: 30px;">🏢</span> <strong>[Archive 2]</strong> Justificatif d'Activité Légal / Extraction Fichiers
            </a>
            
            <a href="https://drive.google.com/file/d/1v9lRZvhTwE4CF3Dq4kPeR9IB8QzR9geY/view?usp=drive_link" target="_blank" class="btn-nav" style="width: 85%; font-size: 10.5pt; text-align: left; padding-left: 30px;">
                <span style="display: inline-block; width: 30px;">📦</span> <strong>[Archive 3]</strong> Livrable Mission (Reporting Analytique)
            </a>
            
            <a href="https://drive.google.com/file/d/1KHVaDgWzgNSpym-UeFSKzoDM5abVMJj2/view?usp=drive_link" target="_blank" class="btn-nav" style="width: 85%; font-size: 10.5pt; text-align: left; padding-left: 30px;">
                <span style="display: inline-block; width: 30px;">📊</span> <strong>[Archive 4]</strong> Relevés de Performance & Stats Brutes (Excel)
            </a>

            <h2 style='font-size: 12pt; color: var(--gold-light); margin-bottom: 10px; margin-top: 35px;'>B. EXPERTISE SOCIAL SELLING (LINKEDIN)</h2>
            <p style="font-size: 9.5pt; text-align: center; margin-top: 0; margin-bottom: 15px; color: var(--text-muted);">Preuves de la capacité à rayonner et influencer la cible sur les réseaux professionnels B2B.</p>
            
            <a href="https://www.linkedin.com/posts/julien-florence-2536a083_oenotourisme-artdevivre-vignobles-activity-7421884268253057024-Ofgh?utm_source=share&utm_medium=member_desktop&rcm=ACoAABG4o18BLawDZS3rFCCggwVoWwgws6scy_U" target="_blank" class="btn-nav" style="width: 85%; font-size: 10.5pt; text-align: left; padding-left: 30px;">
                <span style="display: inline-block; width: 30px;">🍇</span> <strong>[Post Analytique]</strong> L'Œnotourisme & l'Art de Vivre
            </a>
            
            <a href="https://www.linkedin.com/posts/julien-florence-2536a083_serviceclient-excellence-sommelier-activity-7418976158194552832-DbgX?utm_source=share&utm_medium=member_desktop&rcm=ACoAABG4o18BLawDZS3rFCCggwVoWwgws6scy_U" target="_blank" class="btn-nav" style="width: 85%; font-size: 10.5pt; text-align: left; padding-left: 30px;">
                <span style="display: inline-block; width: 30px;">🍷</span> <strong>[Réflexion]</strong> Excellence & Service Client (L'Héritage Sommelier)
            </a>
            
            <a href="https://www.linkedin.com/posts/julien-florence-2536a083_effetwaouh-hospitalitaez-happyhouse-activity-7417883359349022720-amMw?utm_source=share&utm_medium=member_desktop&rcm=ACoAABG4o18BLawDZS3rFCCggwVoWwgws6scy_U" target="_blank" class="btn-nav" style="width: 85%; font-size: 10.5pt; text-align: left; padding-left: 30px;">
                <span style="display: inline-block; width: 30px;">✨</span> <strong>[Marque]</strong> L'Effet Waouh en Hospitalité (L'expérience Client)
            </a>
            
            <a href="https://www.linkedin.com/posts/julien-florence-2536a083_happyhouse-ecotourisme-toulouse-activity-7415346621812645890-4xin?utm_source=share&utm_medium=member_desktop&rcm=ACoAABG4o18BLawDZS3rFCCggwVoWwgws6scy_U" target="_blank" class="btn-nav" style="width: 85%; font-size: 10.5pt; text-align: left; padding-left: 30px;">
                <span style="display: inline-block; width: 30px;">🌿</span> <strong>[Réseau]</strong> Écotourisme & Engagement Régional Happy House
            </a>
        </div>
        
        <div class="glass-card" style="margin-top: 50px; text-align: center; border: 1px solid #DDA83E; padding: 25px;">
            <p style="font-family: 'Cinzel', serif; font-size: 14pt; color: #DDA83E; margin: 0; font-weight: bold; letter-spacing: 2px;">
                FIN DU RAPPORT DE MISSION EXPERT
            </p>
            <div style="width: 50px; height: 1px; background: #DDA83E; margin: 15px auto;"></div>
            <p style="font-size: 10pt; color: #888; margin-top: 10px; font-style: italic;">
                Dossier conçu, audité et certifié par Julien Florence (Promotion A150 — Année 2026).
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
            <a href="#page-2" style="color: #DDA83E; border: 1px solid #DDA83E; padding: 5px 10px; display: inline-block; font-size: 7pt; transition: all 0.3s;" onmouseover="this.style.background='#DDA83E'; this.style.color='#000';" onmouseout="this.style.background='transparent'; this.style.color='#DDA83E';">◈ RETOUR SOMMAIRE</a>
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
output_path = os.path.join(base_path, "RAPPORT_DE_MISSION_V7_MASTODONTE.html")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"[✓] HTML ULTIME généré avec succès ({page_number-1} pages).")
