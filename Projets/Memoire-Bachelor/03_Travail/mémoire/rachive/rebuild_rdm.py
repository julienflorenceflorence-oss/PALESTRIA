import os
import re

header = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MÉMOIRE STRATÉGIQUE - JULIEN FLORENCE</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@0,400;1,400&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #D4AF37;
            --bg: #0F1115;
            --text: rgba(255, 255, 255, 0.98);
        }

        /* RESET & PRINT ENGINE HD PRO */
        * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }

        html, body {
            margin: 0;
            padding: 0;
            background-color: #050505 !important;
            color: #FFFFFF !important;
            font-family: 'Montserrat', sans-serif;
            text-rendering: optimizeLegibility;
            height: auto !important;
        }

        /* LIENS EN BLANC */
        a, a:visited, .toc-link { 
            color: #FFFFFF !important; 
            text-decoration: none !important; 
        }
        a:hover { color: var(--gold) !important; }

        /* STRUCTURE DES PAGES - BLOCK STRICT POUR PDF */
        .page { 
            width: 210mm; 
            height: 297mm; 
            background-color: #0F1115 !important; 
            margin: 40px auto; 
            position: relative; 
            padding: 45mm 35mm; 
            display: block; 
            overflow: hidden;
            break-after: page;
            page-break-after: always;
            border: 1.5px solid #1a1a1a;
            box-shadow: 0 0 50px rgba(0,0,0,0.8);
        }

        @media print {
            @page { size: A4; margin: 0 !important; }
            .page { 
                margin: 0 !important; 
                border: none !important; 
                box-shadow: none !important;
                width: 210mm !important;
                height: 297mm !important;
                min-height: 297mm !important;
                max-height: 297mm !important;
                padding: 45mm 35mm !important;
            }
            .footer {
                position: absolute !important;
                bottom: 15mm !important;
                left: 35mm !important;
                right: 35mm !important;
                border-top: 2px solid #D4AF37 !important;
            }
            .back-to-toc-icon { display: none !important; }
        }

        .inner-border { 
            position: absolute; 
            top: 12mm; left: 12mm; right: 12mm; bottom: 12mm; 
            border: 2px solid rgba(212, 175, 55, 0.45) !important; 
            pointer-events: none; z-index: 1; 
        }

        h1 { font-family: 'Cinzel', serif; color: var(--gold) !important; text-align: center; border-bottom: 3px solid var(--gold); padding-bottom: 15px; margin-bottom: 40px; text-transform: uppercase; font-size: 24pt; position: relative; z-index: 2; }
        h2 { font-family: 'Cinzel', serif; color: var(--gold) !important; border-left: 6px solid var(--gold); padding-left: 25px; margin: 40px 0; font-size: 18pt; text-transform: uppercase; position: relative; z-index: 2; }
        h3 { font-family: 'Cinzel', serif; color: var(--gold) !important; margin: 30px 0; font-size: 14pt; position: relative; z-index: 2; }
        
        p, li { font-size: 12pt; line-height: 1.8; color: var(--text) !important; text-align: justify; margin-bottom: 20px; position: relative; z-index: 2; }

        .footer { 
            position: absolute;
            bottom: 12mm;
            left: 35mm;
            right: 35mm;
            border-top: 2.5px solid rgba(212, 175, 55, 0.85); 
            padding-top: 6mm; 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
            font-family: 'Cinzel', serif; 
            font-size: 10.5pt; 
            color: var(--gold) !important; 
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 2px;
        }

        .page-num::after { counter-increment: page; content: "PAGE " counter(page, decimal-leading-zero); font-weight: 900; }

        .verbatim { 
            font-family: 'Playfair Display', serif; font-style: italic; color: var(--gold) !important; 
            border-left: 5px solid var(--gold); padding-left: 35px; margin: 50px 0; font-size: 15pt; 
            position: relative; z-index: 2; line-height: 1.6;
        }

        .kpi-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 35px; margin: 40px 0; position: relative; z-index: 2; }
        .kpi-card { background: rgba(255,255,255,0.06); border: 2px solid rgba(212,175,55,0.35); padding: 35px; text-align: center; }
        .kpi-value { font-family: 'Cinzel'; font-size: 30pt; color: var(--gold); margin-bottom: 15px; font-weight: 900; }
        
        .back-to-toc-icon { 
            position: absolute; bottom: 15mm; right: 15mm; width: 10mm; height: 10mm; 
            display: flex; align-items: center; justify-content: center; 
            border: 2px solid var(--gold); border-radius: 50%; color: var(--gold) !important; 
            font-size: 16pt; z-index: 100; background-color: rgba(15, 17, 21, 0.95); 
        }
    </style>
</head>
<body>
"""

def get_content(filename):
    if not os.path.exists(filename): return ""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        # If batch contains <body>, extract it. Otherwise take everything.
        match = re.search('(?s)<body.*?>(.*?)</body>', content)
        if match: return match.group(1)
        # Remove head/html tags if present
        content = re.sub('(?s)<head>.*?</head>', '', content)
        content = re.sub('(?s)<html>', '', content)
        content = re.sub('(?s)</html>', '', content)
        content = re.sub('(?s)<!DOCTYPE.*?>', '', content)
        return content

# Page de garde
garde = """
    <div class="page" id="p01">
        <div class="inner-border"></div>
        <div style="text-align: center; margin-top: 100px;">
            <div style="font-family: 'Cinzel'; color: #D4AF37; letter-spacing: 7px; font-size: 1.6rem;">Rocket School Toulouse</div>
            <h1 style="border:none; font-size: 4.5rem; margin: 60px 0;">RAPPORT DE MISSION<br>STRATÉGIQUE</h1>
            <div class="verbatim" style="border:none; text-align:center; padding:0; font-size: 2rem; margin: 60px 0;">"Industrialiser le prestige : la métamorphose numérique d'un réseau d'exception."</div>
            <div style="font-size: 3rem; font-weight: 600; letter-spacing: 5px;">JULIEN FLORENCE</div>
            <div style="font-family: 'Cinzel'; color: #D4AF37; letter-spacing: 4px; font-size: 1.4rem; margin-top: 20px;">Directeur du Développement Opérationnel</div>
            <div style="margin-top: 100px; font-family: 'Cinzel'; font-size: 1.3rem; letter-spacing: 3px;">Tuteur : Patrice Kermarrec<br>(Hébergeur & Fondateur)</div>
            <div style="margin-top: 50px; font-family: 'Cinzel'; font-size: 1.1rem; letter-spacing: 3px;">SESSION 2026 | HAPPY HOUSE</div>
        </div>
    </div>
"""

# Sommaire
sommaire = """
    <div class="page" id="toc">
        <div class="inner-border"></div>
        <h1>Sommaire Interactif</h1>
        <div class="content" style="margin-top: 50px; font-size: 14pt; padding: 0 40px;">
            <p><a href="#p03">I. Introduction & Vision Stratégique .............................. 03</a></p>
            <p><a href="#p10">II. Présentation de Happy House .................................. 10</a></p>
            <p><a href="#p18">III. Diagnostics Stratégiques (PESTEL/SWOT) ....................... 18</a></p>
            <p><a href="#p26">IV. Ingénierie Commerciale & Sales Machine ........................ 26</a></p>
            <p><a href="#p33">V. Recherche Terrain & Interviews (6) ............................. 33</a></p>
            <p><a href="#p41">VI. Plan de Rétention : La "Double Détente" ....................... 41</a></p>
            <p><a href="#p43">VII. Onboarding Technologique (NFC/QR) ............................ 43</a></p>
            <p><a href="#p46">VIII. Bilan ROI & Perspectives 2027 ................................. 46</a></p>
            <p><a href="#p50">IX. Conclusion & Bilan Personnel .................................. 50</a></p>
            <p><a href="#p51">X. Annexes Documentaires (Playbook) ............................... 51</a></p>
        </div>
        <div class="footer"><div>JULIEN FLORENCE | MÉMOIRE STRATÉGIQUE</div><div class="page-num"></div></div>
    </div>
"""

with open('RDM_FINAL_MASTER_JULIEN_FLORENCE.html', 'w', encoding='utf-8') as f:
    f.write(header)
    f.write(garde)
    f.write(sommaire)
    f.write(get_content('batch1.html'))
    f.write(get_content('batch2.html'))
    f.write(get_content('batch3.html'))
    f.write(get_content('batch4.html'))
    f.write(get_content('annexes.html'))
    f.write("</body></html>")

print("RDM Rebuilt properly.")
