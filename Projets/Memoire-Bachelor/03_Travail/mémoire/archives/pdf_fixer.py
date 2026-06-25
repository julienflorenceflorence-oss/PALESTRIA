import os

header = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RDM MASTER PRESTIGE - JULIEN FLORENCE</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:ital,wght@0,300;0,400;0,600;1,400&display=swap" rel="stylesheet">
    <style>
        /* CRITICAL PDF FIXES */
        :root {
            --bg: #0F1115;
            --accent: #D4AF37;
            --text: #FFFFFF;
            --dim: rgba(255, 255, 255, 0.8);
        }

        * { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }

        @page {
            size: A4;
            margin: 0; /* We handle margins inside the .page div */
        }

        body { 
            background-color: #050505; 
            margin: 0; 
            padding: 0;
            counter-reset: page;
        }

        .page {
            width: 210mm;
            height: 297mm;
            background-color: var(--bg) !important;
            color: var(--text) !important;
            margin: 0 auto;
            position: relative;
            padding: 30mm 25mm 25mm 25mm;
            page-break-after: always;
            overflow: hidden; /* Strict container */
            display: flex;
            flex-direction: column;
            font-family: Arial, sans-serif;
            border: none;
        }

        /* Border Decoration */
        .inner-border {
            position: absolute;
            top: 10mm; left: 10mm; right: 10mm; bottom: 10mm;
            border: 0.5pt solid rgba(212, 175, 55, 0.2);
            pointer-events: none;
        }

        h1, h2, h3 { font-family: 'Cinzel', serif; color: var(--accent) !important; text-transform: uppercase; margin-top: 0; }
        h1 { font-size: 20pt; border-bottom: 1pt solid var(--accent); padding-bottom: 5mm; margin-bottom: 20mm; text-align: center; letter-spacing: 2px; }
        h2 { font-size: 14pt; border-left: 3pt solid var(--accent); padding-left: 15px; margin-bottom: 15mm; }
        
        p, li { 
            font-size: 12pt; 
            line-height: 1.5; 
            color: var(--dim) !important; 
            text-align: justify; 
            margin-bottom: 4mm;
            orphans: 3;
            widows: 3;
        }

        .content {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }

        .footer {
            height: 15mm;
            border-top: 0.5pt solid rgba(212, 175, 55, 0.4);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Cinzel', serif;
            font-size: 8pt;
            color: var(--accent) !important;
            margin-top: auto;
        }

        .page-num::after { counter-increment: page; content: "PAGE " counter(page, decimal-leading-zero); }

        .back-to-toc-icon {
            position: absolute; bottom: 12mm; right: 12mm; width: 8mm; height: 8mm;
            display: flex; align-items: center; justify-content: center;
            border: 0.5pt solid var(--accent); border-radius: 50%; color: var(--accent);
            text-decoration: none; font-size: 14pt; z-index: 100;
            background-color: rgba(15, 17, 21, 0.8);
        }

        .verbatim {
            font-family: 'Montserrat', sans-serif; font-style: italic; color: var(--accent) !important;
            border-left: 2pt solid var(--accent); padding-left: 15px; margin: 5mm 0; font-size: 11pt;
        }

        .kpi-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; margin-bottom: 5mm; }
        .kpi-card { background: rgba(255,255,255,0.05); border: 0.5pt solid rgba(212, 175, 55, 0.3); padding: 4mm; text-align: center; }
        .kpi-value { font-size: 16pt; font-weight: bold; color: var(--accent); }

        .cover { justify-content: center; text-align: center; padding-top: 0; }
        .cover h1 { border: none; font-size: 32pt; }
        
        a { color: inherit; text-decoration: none; }

        @media print {
            body { background: none; }
            .back-to-toc-icon { display: none; }
            .page { margin: 0; box-shadow: none; }
        }
    </style>
</head>
<body id="toc-anchor">
"""

garde = """
    <div class="page cover">
        <div class="inner-border"></div>
        <div style="font-family: 'Cinzel'; color: var(--accent); letter-spacing: 5px; font-size: 1.5rem;">Rocket School Toulouse</div>
        <div style="margin-top: 40mm;">
            <h1>RAPPORT DE MISSION<br>STRATÉGIQUE</h1>
            <div class="verbatim" style="border:none; text-align:center; padding:0; font-size: 1.3rem;">"Industrialiser le prestige : la métamorphose numérique d'un réseau d'exception."</div>
            <div style="font-size: 2.2rem; font-weight: 600; letter-spacing: 3px; margin-top: 20mm;">JULIEN FLORENCE</div>
            <div style="font-family: 'Cinzel'; color: var(--accent); letter-spacing: 3px; font-size: 1rem; margin-top: 5mm;">Directeur du Développement Opérationnel</div>
            <div style="margin-top: 50mm; font-family: 'Cinzel'; font-size: 0.9rem; letter-spacing: 2px;">Tuteur : Patrice Kermarrec<br>(Hébergeur & Fondateur)</div>
            <div style="margin-top: 15mm; font-family: 'Cinzel'; font-size: 0.8rem; letter-spacing: 2px;">SESSION 2026 | HAPPY HOUSE</div>
        </div>
    </div>
"""

sommaire = """
    <div class="page" id="toc">
        <div class="inner-border"></div>
        <h1>Sommaire Interactif</h1>
        <div class="content" style="padding-top: 10mm;">
            <p><a href="#p03">I. Introduction & Vision Stratégique ................................. 03</a></p>
            <p><a href="#p10">II. Présentation de Happy House ................................... 10</a></p>
            <p><a href="#p18">III. Diagnostics Stratégiques (PESTEL/SWOT) ................ 18</a></p>
            <p><a href="#p26">IV. Ingénierie de l'Acquisition (Sales Machine) ................ 26</a></p>
            <p><a href="#p33">V. Recherche Terrain & Interviews (6) ............................ 33</a></p>
            <p><a href="#p41">VI. Expérience Onboarding Phygital ................................ 41</a></p>
            <p><a href="#p46">VII. Bilan ROI & Perspectives 2027 ................................ 46</a></p>
            <p><a href="#p50">VIII. Conclusion & Bilan Personnel ................................. 50</a></p>
            <p><a href="#annexe-start">IX. Annexes Documentaires (7 Blocs) .............................. 51</a></p>
        </div>
        <div class="footer"><div>JULIEN FLORENCE | MÉMOIRE STRATÉGIQUE</div><div class="page-num"></div></div>
    </div>
"""

def clean_content(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
        # Find start of pages
        start = c.find('<div class="page"')
        end = c.rfind('</div>') + 6
        if start != -1:
            body = c[start:end]
            # Replace id="toc" if it exists in batch to avoid duplicate
            body = body.replace('id="toc"', 'id="old-toc"')
            # Fix links back to toc
            body = body.replace('href="#toc"', 'href="#toc-anchor"')
            return body
    return ""

with open('RDM_MASTER_PDF_ULTRA_CLEAN.html', 'w', encoding='utf-8') as f:
    f.write(header)
    f.write(garde)
    f.write(sommaire)
    f.write(clean_content('batch1.html'))
    f.write(clean_content('batch2.html'))
    f.write(clean_content('batch3.html'))
    f.write(clean_content('batch4.html'))
    f.write('<div id="annexe-start"></div>')
    f.write(clean_content('annexes.html'))
    f.write("</body></html>")
