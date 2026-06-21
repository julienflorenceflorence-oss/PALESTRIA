import os

header = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RDM PRESTIGE - JULIEN FLORENCE - HAPPY HOUSE</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root { --bg: #0F1115; --accent: #D4AF37; --text: #FFFFFF; --text-dim: rgba(255, 255, 255, 0.8); }
        @media print { 
            @page { size: A4; margin: 0; } 
            body { background: var(--bg) !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; } 
            .page { margin: 0 !important; border: none !important; box-shadow: none !important; } 
            .back-to-toc-icon { display: none !important; } 
        }
        body { background: #050505; color: var(--text); font-family: Arial, sans-serif; margin: 0; counter-reset: page; scroll-behavior: smooth; }
        .page { 
            width: 210mm; 
            height: 297mm; 
            background: var(--bg); 
            margin: 40px auto; 
            position: relative; 
            padding: 25mm 20mm; /* Reduced to standard but controlled */
            box-sizing: border-box; 
            box-shadow: 0 0 30px rgba(0,0,0,0.8); 
            page-break-after: always; 
            display: flex; 
            flex-direction: column; 
            overflow: hidden; 
        }
        .inner-border { position: absolute; top: 10mm; left: 10mm; right: 10mm; bottom: 10mm; border: 1px solid rgba(212, 175, 55, 0.15); pointer-events: none; }
        .back-to-toc-icon { position: absolute; bottom: 12mm; right: 15mm; width: 7mm; height: 7mm; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 50%; color: var(--accent); text-decoration: none; font-size: 10pt; z-index: 100; background: rgba(15, 17, 21, 0.8); font-family: 'Cinzel'; }
        h1 { font-family: 'Cinzel', serif; color: var(--accent); text-align: center; border-bottom: 1px solid var(--accent); padding-bottom: 5px; margin-bottom: 20px; text-transform: uppercase; font-size: 1.6rem; letter-spacing: 2px; }
        h2 { font-family: 'Cinzel', serif; color: var(--accent); border-left: 5px solid var(--accent); padding-left: 15px; margin: 20px 0; font-size: 1.3rem; text-transform: uppercase; }
        h3 { font-family: 'Cinzel', serif; color: var(--accent); margin: 15px 0; font-size: 1rem; }
        p { font-size: 12pt; line-height: 1.5; color: var(--text-dim); text-align: justify; margin-bottom: 15px; }
        li { font-size: 12pt; line-height: 1.5; color: var(--text-dim); margin-bottom: 10px; }
        .content { flex-grow: 1; overflow: hidden; margin-bottom: 5mm; }
        .footer { border-top: 1px solid rgba(212, 175, 55, 0.3); padding-top: 3mm; margin-top: auto; display: flex; justify-content: space-between; font-family: 'Cinzel'; font-size: 8pt; color: var(--accent); height: 10mm; align-items: center; }
        .page-num::after { counter-increment: page; content: "PAGE " counter(page, decimal-leading-zero); }
        .kpi-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0; }
        .kpi-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(212, 175, 55, 0.2); padding: 10px; text-align: center; }
        .kpi-value { font-size: 1.6rem; font-weight: bold; color: var(--accent); }
        .verbatim { font-family: 'Montserrat', sans-serif; font-style: italic; color: var(--accent); border-left: 3px solid var(--accent); padding-left: 15px; margin: 20px 0; font-size: 1rem; opacity: 0.9; }
        a { color: inherit; text-decoration: none; }
    </style>
</head>
<body>
"""

garde = """
    <div class="page" id="p01">
        <div class="inner-border"></div>
        <div style="text-align: center; margin-top: 50px;">
            <div style="font-family: 'Cinzel'; color: var(--accent); letter-spacing: 5px; font-size: 1.3rem;">Rocket School Toulouse</div>
            <h1 style="border:none; font-size: 3rem; margin: 40px 0;">RAPPORT DE MISSION<br>STRATÉGIQUE</h1>
            <div class="verbatim" style="border:none; text-align:center; padding:0; font-size: 1.3rem; margin: 40px 0;">"Industrialiser le prestige : la métamorphose numérique d'un réseau d'exception."</div>
            <div style="font-size: 2.2rem; font-weight: 600; letter-spacing: 3px;">JULIEN FLORENCE</div>
            <div style="font-family: 'Cinzel'; color: var(--accent); letter-spacing: 3px; font-size: 1rem; margin-top: 10px;">Directeur du Développement Opérationnel</div>
            <div style="margin-top: 80px; font-family: 'Cinzel'; font-size: 1rem; letter-spacing: 2px;">Tuteur : Patrice Kermarrec<br>(Hébergeur & Fondateur)</div>
            <div style="margin-top: 40px; font-family: 'Cinzel'; font-size: 0.8rem; letter-spacing: 2px;">SESSION 2026 | HAPPY HOUSE</div>
        </div>
    </div>
"""

sommaire = """
    <div class="page" id="toc">
        <div class="inner-border"></div>
        <h1>Sommaire Interactif</h1>
        <div style="margin-top: 10px; font-size: 10pt;">
            <p><a href="#p03">I. Introduction & Vision Stratégique ............................................. 03</a></p>
            <p><a href="#p10">II. Présentation de Happy House ............................................. 10</a></p>
            <p><a href="#p18">III. Diagnostics Stratégiques (PESTEL/SWOT) .......................... 18</a></p>
            <p><a href="#p26">IV. Ingénierie de l'Acquisition (Sales Machine) .......................... 26</a></p>
            <p><a href="#p33">V. Recherche Terrain & Interviews (6) ...................................... 33</a></p>
            <p><a href="#p41">VI. Expérience Onboarding Phygital .......................................... 41</a></p>
            <p><a href="#p46">VII. Bilan ROI & Perspectives 2027 .......................................... 46</a></p>
            <p><a href="#p50">VIII. Conclusion & Bilan Personnel ........................................... 50</a></p>
            <p><a href="#p51">IX. Annexes Documentaires ..................................................... 51</a></p>
        </div>
        <div class="footer"><div>JULIEN FLORENCE | MÉMOIRE STRATÉGIQUE</div><div class="page-num"></div></div>
    </div>
"""

with open('RDM_MASTER_FINAL_70P.html', 'w', encoding='utf-8') as f:
    f.write(header)
    f.write(garde)
    f.write(sommaire)
    for batch in ['batch1.html', 'batch2.html', 'batch3.html', 'batch4.html', 'annexes.html']:
        if os.path.exists(batch):
            with open(batch, 'r', encoding='utf-8') as b:
                content = b.read()
                # Remove extra body/html tags if present in batches
                content = content.replace('<!DOCTYPE html>', '').replace('<html>', '').replace('</html>', '').replace('<body>', '').replace('</body>', '').replace('<head>', '').replace('</head>', '')
                f.write(content)
    f.write("</body></html>")
