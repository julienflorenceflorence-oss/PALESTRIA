import os
import re

header = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RDM PRESTIGE - JULIEN FLORENCE - 70 PAGES</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body { background-color: #050505 !important; color: #FFFFFF !important; font-family: Arial, Helvetica, sans-serif; margin: 0; padding: 0; counter-reset: page; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        .page { width: 210mm; min-height: 296.5mm; background-color: #0F1115 !important; margin: 20px auto; position: relative; padding: 30mm 25mm; box-sizing: border-box; page-break-after: always; display: flex; flex-direction: column; border: 1px solid #1a1a1a; }
        .inner-border { position: absolute; top: 10mm; left: 10mm; right: 10mm; bottom: 10mm; border: 1px solid rgba(212, 175, 55, 0.3); pointer-events: none; z-index: 1; }
        h1 { font-family: 'Cinzel', serif; color: #D4AF37 !important; text-align: center; border-bottom: 2px solid #D4AF37; padding-bottom: 10px; margin-bottom: 30px; text-transform: uppercase; font-size: 22pt; }
        h2 { font-family: 'Cinzel', serif; color: #D4AF37 !important; border-left: 5px solid #D4AF37; padding-left: 20px; margin: 30px 0; font-size: 16pt; text-transform: uppercase; }
        h3 { font-family: 'Cinzel', serif; color: #D4AF37 !important; margin: 20px 0; font-size: 13pt; }
        p { font-size: 12pt; line-height: 1.5; color: rgba(255,255,255,0.9) !important; text-align: justify; margin-bottom: 20px; }
        li { font-size: 12pt; line-height: 1.5; color: rgba(255,255,255,0.9) !important; margin-bottom: 15px; }
        .content { flex-grow: 1; position: relative; z-index: 2; }
        .footer { border-top: 1px solid rgba(212, 175, 55, 0.5); padding-top: 5mm; margin-top: 10mm; display: flex; justify-content: space-between; font-family: 'Cinzel', serif; font-size: 9pt; color: #D4AF37 !important; z-index: 2; }
        .page-num::after { counter-increment: page; content: "PAGE " counter(page, decimal-leading-zero); }
        .back-to-toc-icon { position: absolute; bottom: 12mm; right: 12mm; width: 8mm; height: 8mm; display: flex; align-items: center; justify-content: center; border: 1px solid #D4AF37; border-radius: 50%; color: #D4AF37; text-decoration: none; font-size: 14pt; z-index: 100; background-color: rgba(15, 17, 21, 0.8); }
        .verbatim { font-family: 'Montserrat', sans-serif; font-style: italic; color: #D4AF37 !important; border-left: 3px solid #D4AF37; padding-left: 20px; margin: 30px 0; font-size: 11pt; }
        .cover { justify-content: center; text-align: center; background: linear-gradient(rgba(15,17,21,0.9), rgba(15,17,21,0.9)), url('https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80'); background-size: cover; }
        a { color: inherit; text-decoration: none; }
        @media print { .page { margin: 0; border: none; } .back-to-toc-icon { display: none; } }
    </style>
</head>
<body>
"""

garde = """
    <div class="page" id="p01">
        <div class="inner-border"></div>
        <div style="text-align: center; margin-top: 50px;">
            <div style="font-family: 'Cinzel'; color: #D4AF37; letter-spacing: 5px; font-size: 1.3rem;">Rocket School Toulouse</div>
            <h1 style="border:none; font-size: 3.5rem; margin: 40px 0;">RAPPORT DE MISSION<br>STRATÉGIQUE</h1>
            <div class="verbatim" style="border:none; text-align:center; padding:0; font-size: 1.5rem; margin: 40px 0;">"Industrialiser le prestige : la métamorphose numérique d'un réseau d'exception."</div>
            <div style="font-size: 2.5rem; font-weight: 600; letter-spacing: 3px;">JULIEN FLORENCE</div>
            <div style="font-family: 'Cinzel'; color: #D4AF37; letter-spacing: 3px; font-size: 1.2rem; margin-top: 10px;">Directeur du Développement Opérationnel</div>
            <div style="margin-top: 80px; font-family: 'Cinzel'; font-size: 1.1rem; letter-spacing: 2px;">Tuteur : Patrice Kermarrec<br>(Hébergeur & Fondateur)</div>
            <div style="margin-top: 40px; font-family: 'Cinzel'; font-size: 1rem; letter-spacing: 2px;">SESSION 2026 | HAPPY HOUSE</div>
        </div>
    </div>
"""

sommaire = """
    <div class="page" id="toc">
        <div class="inner-border"></div>
        <h1>Sommaire Interactif</h1>
        <div class="content" style="margin-top: 20px; font-size: 10pt;">
            <p><a href="#p03">I. Introduction & Vision Stratégique ............................................. 03</a></p>
            <p><a href="#p10">II. Présentation de Happy House ............................................. 10</a></p>
            <p><a href="#p18">III. Diagnostics Stratégiques (PESTEL/SWOT) .......................... 18</a></p>
            <p><a href="#p26">IV. Ingénierie de l'Acquisition (Sales Machine) .......................... 26</a></p>
            <p><a href="#p33">V. Recherche Terrain & Interviews (6) ...................................... 33</a></p>
            <p><a href="#p41">VI. Expérience Onboarding Phygital .......................................... 41</a></p>
            <p><a href="#p46">VII. Bilan ROI & Perspectives 2027 .......................................... 46</a></p>
            <p><a href="#p50">VIII. Conclusion & Bilan Personnel ........................................... 50</a></p>
            <p><a href="#p51">IX. Annexes Documentaires (7 Blocs) ........................................ 51</a></p>
        </div>
        <div class="footer"><div>JULIEN FLORENCE | MÉMOIRE STRATÉGIQUE</div><div class="page-num"></div></div>
    </div>
"""

def clean_and_inject(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
        # Extract body content
        if "<body>" in c:
            c = c[c.find("<body>")+6:c.rfind("</body>")]
        # Inject back to toc icon if not present
        pages = c.split('<div class="page"')
        new_pages = []
        for p in pages:
            if not p.strip(): continue
            p = '<div class="page"' + p
            if 'back-to-toc-icon' not in p and 'id="p01"' not in p and 'id="toc"' not in p:
                p = p.replace('</div>\n</div>', '</div><a href="#toc" class="back-to-toc-icon">◈</a></div>')
            new_pages.append(p)
        return "\n".join(new_pages)

with open('RDM_MASTER_ULTRA_70P.html', 'w', encoding='utf-8') as f:
    f.write(header)
    f.write(garde)
    f.write(sommaire)
    for b in ['batch1.html', 'batch2.html', 'batch3.html', 'batch4.html', 'annexes.html']:
        f.write(clean_and_inject(b))
    f.write("</body></html>")
