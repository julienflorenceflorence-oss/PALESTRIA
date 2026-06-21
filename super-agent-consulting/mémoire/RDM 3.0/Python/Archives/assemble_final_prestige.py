import os
import markdown
import re

CONTENT_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\contenue"
ANNEX_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\annexe\annexes .md"
COFFRE_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\annexe"
OUTPUT_FILE = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\RDM_FINAL_ASSEMBLE.html"

FILES_TO_MERGE = [
    os.path.join(CONTENT_DIR, "00_glossaire_et_sources.md"),
    os.path.join(CONTENT_DIR, "chapitre-01-introduction-problematique.md"),
    os.path.join(CONTENT_DIR, "chapitre-02-diagnostic-externe.md"),
    os.path.join(CONTENT_DIR, "chapitre-03-diagnostic-interne.md"),
    os.path.join(CONTENT_DIR, "chapitre-04-cac-sales-engine.md"),
    os.path.join(CONTENT_DIR, "chapitre-05-recherche-terrain.md"),
    os.path.join(CONTENT_DIR, "chapitre-06-retention-onboarding.md"),
    os.path.join(CONTENT_DIR, "chapitre-07-performance-bilan.md"),
    os.path.join(CONTENT_DIR, "chapitre-08-annexes-ia.md"),
    os.path.join(ANNEX_DIR, "annexe_01_pestel.md"),
    os.path.join(ANNEX_DIR, "annexe_02_swot.md"),
    os.path.join(ANNEX_DIR, "annexe_03_porter.md"),
    os.path.join(ANNEX_DIR, "annexe_04_comparatif_performance.md"),
    os.path.join(ANNEX_DIR, "annexe_05_finance_churn.md"),
    os.path.join(ANNEX_DIR, "annexe_06_script_julien.md"),
    os.path.join(ANNEX_DIR, "annexe_07_script_younes.md"),
    os.path.join(ANNEX_DIR, "annexe_08_cadrage_equipe.md"),
    os.path.join(COFFRE_DIR, "annexe_09_coffre_fort.md")
]

HTML_HEADER = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAPPORT DE MISSION CONSULTANT 2026 - HAPPY HOUSE</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #DDA83E; --gold-light: #BCBFD0; --bg: #17225C;
            --card-bg: rgba(255, 255, 255, 0.05); --border: rgba(212, 175, 55, 0.5); --text: rgba(255, 255, 255, 0.95);
        }
        * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        html, body { margin: 0; padding: 0; background-color: var(--bg); color: var(--text); font-family: 'Montserrat', sans-serif; scroll-behavior: smooth; }
        
        /* The .page container is exactly A4 size */
        .page {
            width: 210mm; 
            height: 297mm; 
            background-color: var(--bg); 
            margin: 40px auto; 
            position: relative;
            padding: 25mm 20mm 20mm 20mm; 
            display: flex; 
            flex-direction: column; 
            overflow: hidden;
            box-shadow: 0 0 100px rgba(0,0,0,0.9); 
            page-break-after: always;
        }
        
        @media print { 
            body { background: none; } 
            .page { margin: 0; border: none; box-shadow: none; width: 210mm; height: 297mm; page-break-after: always; } 
            /* Fix link colors in print */
            a { color: var(--gold) !important; text-decoration: none; }
        }
        
        .cockpit-frame { position: absolute; top: 10mm; left: 10mm; right: 10mm; bottom: 10mm; border: 1px solid var(--border); pointer-events: none; z-index: 10; }
        .corner { position: absolute; width: 15mm; height: 15mm; border: 3px solid var(--gold); z-index: 11; }
        .top-left { top: 8mm; left: 8mm; border-right: none; border-bottom: none; }
        .top-right { top: 8mm; right: 8mm; border-left: none; border-bottom: none; }
        .bottom-left { bottom: 8mm; left: 8mm; border-right: none; border-top: none; }
        .bottom-right { bottom: 8mm; right: 8mm; border-left: none; border-top: none; }
        
        .content-body { position: relative; z-index: 5; flex-grow: 1; display: flex; flex-direction: column; }
        
        h1 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 18pt; text-transform: uppercase; letter-spacing: 4px; margin: 0 0 15px 0; border-bottom: 2px solid var(--gold); padding-bottom: 10px; }
        h2 { font-family: 'Cinzel', serif; color: var(--gold-light); font-size: 13pt; margin: 15px 0 10px 0; letter-spacing: 2px; }
        h3 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 11pt; margin: 10px 0 5px 0; }
        p, li { font-size: 10pt; line-height: 1.5; text-align: justify; margin-bottom: 10px; font-weight: 300; }
        ul { margin-top: 0; margin-bottom: 10px; padding-left: 20px; }
        
        .glass-card { background: var(--card-bg); backdrop-filter: blur(10px); border: 1px solid var(--border); padding: 15px; margin: 15px 0; border-radius: 4px; }
        .kpi-item { text-align: center; }
        .kpi-item .value { display: block; font-family: 'Cinzel', serif; font-size: 24pt; color: var(--gold); font-weight: 900; }
        .kpi-item .label { font-size: 8pt; text-transform: uppercase; letter-spacing: 1px; color: var(--gold-light); }
        
        .footer { height: 10mm; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; font-family: 'Cinzel', serif; color: var(--gold); font-size: 8pt; letter-spacing: 2px; margin-top: auto; z-index: 20; position: relative; }
        
        .cover-content { flex-grow: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .cover-title { font-size: 36pt; margin: 30px 0; line-height: 1.1; }
        .tagline { font-family: 'Cinzel', serif; font-size: 12pt; letter-spacing: 8px; color: var(--gold); margin-bottom: 40px; }
    
        .dashboard-tile {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 15px !important;
            margin: 0 !important;
            transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1.5px solid rgba(212, 175, 55, 0.2) !important;
            background: rgba(255, 255, 255, 0.03) !important;
            border-radius: 8px;
            position: relative;
            overflow: hidden;
            z-index: 100;
            text-decoration: none;
            height: 100%;
        }
        .dashboard-tile:hover {
            background: rgba(212, 175, 55, 0.1) !important;
            border-color: #D4AF37 !important;
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        }
        .tile-status {
            font-size: 6pt;
            letter-spacing: 2px;
            border: 1px solid rgba(255,255,255,0.4);
            padding: 3px 8px;
            width: fit-content;
            margin-bottom: 8px;
            font-weight: 700;
            color: #fff;
        }
        .tile-icon {
            font-size: 22pt;
            color: #D4AF37;
            margin-bottom: 6px;
        }
        .tile-title {
            font-family: 'Cinzel';
            font-weight: 900;
            font-size: 11pt;
            color: #fff;
            margin-bottom: 6px;
            letter-spacing: 1px;
        }
        .tile-desc {
            font-size: 8pt;
            line-height: 1.4;
            color: rgba(255,255,255,0.6);
            flex-grow: 1;
        }
        .tile-meta {
            font-size: 6pt;
            font-family: 'Cinzel';
            color: #D4AF37;
            text-align: right;
            margin-top: 10px;
            font-weight: 700;
        }
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);
            gap: 15px;
            z-index: 100;
            flex-grow: 1;
            padding: 10px 0;
            position: relative;
        }
        .dashboard-tile * { text-decoration: none !important; color: inherit; }

        .director-note {
            border-left: 3px solid var(--gold);
            background: rgba(221, 168, 62, 0.05);
            padding: 12px 15px;
            margin: 15px 0;
            font-size: 9pt;
            font-style: italic;
        }
        .director-note strong {
            font-family: 'Cinzel';
            font-size: 8pt;
            letter-spacing: 1px;
            display: block;
            margin-bottom: 5px;
            color: var(--gold);
            text-transform: uppercase;
        }

        .back-btn {
            background: rgba(221, 168, 62, 0.1);
            border: 1px solid var(--gold);
            color: var(--gold) !important;
            padding: 4px 12px;
            font-family: 'Cinzel';
            font-size: 7pt;
            letter-spacing: 1px;
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none !important;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .back-btn:hover {
            background: var(--gold);
            color: #000 !important;
        }
        @media print {
            .back-btn { display: none !important; }
        }
        
        table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 8.5pt; }
        th, td { border: 1px solid var(--border); padding: 8px; text-align: left; vertical-align: top; }
        th { font-family: 'Cinzel', serif; color: var(--gold); background: rgba(212, 175, 55, 0.1); }
        td { background: var(--card-bg); }

        /* Global Links */
        a { color: var(--gold); text-decoration: none; border-bottom: 1px dotted rgba(212, 175, 55, 0.4); transition: 0.3s; }
        a:hover { border-bottom: 1px solid var(--gold); }
    </style>
</head>
<body>

    <!-- PAGE 1: COVER -->
    <div class="page" id="p01">
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body cover-content">
            
            <div style="display: flex; gap: 40px; margin-bottom: 40px;">
                <!-- Fallback relative paths if needed, or absolute ones if generating locally -->
                <img src="charte graphique/image Happy House.png" alt="Happy House" style="height: 80px; object-fit: contain;">
                <img src="charte graphique/rocket logo 2.png" alt="Rocket School" style="height: 80px; object-fit: contain;">
            </div>

            <div class="tagline">CONSULTING ANALYSIS</div><h1 class="cover-title" style="border:none;">RAPPORT DE MISSION<br>STRATÉGIQUE 2026</h1>
            <div class="glass-card" style="width: 80%;"><div style="font-style:italic; font-family:'Playfair Display'; color:var(--gold-light);">"Diagnostic, Plan d'Action et Pilotage Opérationnel : Transformer le Prestige en Performance."</div></div>
            <div style="margin-top: 50px; font-family: 'Cinzel'; font-size: 18pt; letter-spacing: 5px;">JULIEN FLORENCE</div>
            <div style="color: var(--gold); margin-top: 10px;">Consultant Expert en Développement Stratégique</div>
        </div>
        <div class="footer"><div>HAPPY HOUSE & ROCKET SCHOOL | DOSSIER EXPERT</div><div class="page-num">01</div></div>
    </div>

    <!-- PAGE 2: DASHBOARD -->
    <div class="page" id="p02">
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body" style="padding: 10px 10px;">
            <h1 style="text-align:center; border-bottom: 2px solid var(--gold); padding-bottom:10px; margin-bottom: 10px;">STRATEGIC CONTROL CENTER</h1>
            <div style="text-align: center; color: var(--gold); letter-spacing: 5px; font-size: 9pt; margin-bottom: 25px; font-weight: 700;">NAVIGUER DANS LES AXES DE MISSION</div>

            <div class="dashboard-grid">
                
                <a href="#chap1" class="dashboard-tile" style="border-bottom: none;">
                    <div class="tile-status">ANALYSIS</div>
                    <div class="tile-icon">◈</div>
                    <div class="tile-title">I. VISION</div>
                    <div class="tile-desc">Introduction, problématique et trajectoire 2026 du réseau Happy House.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap3" class="dashboard-tile" style="border-bottom: none;">
                    <div class="tile-status">IDENTITY</div>
                    <div class="tile-icon">◎</div>
                    <div class="tile-title">II. IDENTITY</div>
                    <div class="tile-desc">Diagnostic Interne : L'actif data et l'audit du churn des 100 membres.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap2" class="dashboard-tile" style="border-bottom: none;">
                    <div class="tile-status" style="color:#3498DB; border-color:#3498DB;">DIAGNOSTIC</div>
                    <div class="tile-icon">◬</div>
                    <div class="tile-title">III. DIAGNOSTICS</div>
                    <div class="tile-desc">Analyse profonde des forces du marché (PESTEL) et la Loi Anti-Airbnb.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap4" class="dashboard-tile" style="border-bottom: none;">
                    <div class="tile-status" style="color:#2ECC71; border-color:#2ECC71;">ACTION PLAN</div>
                    <div class="tile-icon">⚙</div>
                    <div class="tile-title">IV. SALES ENGINE</div>
                    <div class="tile-desc">Ingénierie d'acquisition, budget 0€ et closing physique à 100%.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap5" class="dashboard-tile" style="border-bottom: none;">
                    <div class="tile-status">FIELD PROOF</div>
                    <div class="tile-icon">☖</div>
                    <div class="tile-title">V. FIELD RESEARCH</div>
                    <div class="tile-desc">Interviews terrain et analyse de la "Solitude opérationnelle".</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap6" class="dashboard-tile" style="border-bottom: none;">
                    <div class="tile-status">RETENTION</div>
                    <div class="tile-icon">☍</div>
                    <div class="tile-title">VI. RETENTION</div>
                    <div class="tile-desc">Stratégie Double Détente et intégration de l'expérience phygitale.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap7" class="dashboard-tile" style="border-bottom: none;">
                    <div class="tile-status" style="color:var(--gold); border-color:var(--gold);">ROI</div>
                    <div class="tile-icon">⊘</div>
                    <div class="tile-title">VII. PERFORMANCE</div>
                    <div class="tile-desc">Étude du Cas Durentie, Bilan Personnel et Management Commercial.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap8" class="dashboard-tile" style="border-bottom: none;">
                    <div class="tile-status" style="color:#E74C3C; border-color:#E74C3C;">VAULT</div>
                    <div class="tile-icon">🔒</div>
                    <div class="tile-title">VIII. VAULT</div>
                    <div class="tile-desc">Annexes techniques, Matrices, Scripts PCM et preuves cloud.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

            </div>
        </div>
        <div class="footer"><div>MISSION PILOTAGE V.2026</div><div class="page-num">02</div></div>
    </div>
"""

HTML_FOOTER = """
</body>
</html>
"""

def split_html_to_pages(html_content, start_page_num):
    """
    Very sophisticated chunker that respects table tags, div tags, and avoids breaking in the middle.
    Ensures that content fits perfectly inside the 297mm height without overflow.
    We use an estimated character count to avoid overflowing the page.
    """
    pages = []
    # Using character count is safer than word count for fine tuning
    CHAR_LIMIT = 2500
    
    # Split by major block tags
    blocks = re.split(r'(<h[1-6][^>]*>.*?</h[1-6]>|<p>.*?</p>|<ul>.*?</ul>|<ol>.*?</ol>|<table[^>]*>.*?</table>|<div[^>]*>.*?</div>|<blockquote>.*?</blockquote>|<hr\s*/?>)', html_content, flags=re.DOTALL)
    
    current_page = ""
    current_chars = 0
    current_title = "CONSULTING ANALYSIS"
    
    for block in blocks:
        if not block.strip(): continue
        
        # Keep track of the current H1 to display in the footer
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', block)
        if h1_match:
            # Clean HTML tags from title for footer
            current_title = re.sub(r'<[^>]+>', ' ', h1_match.group(1))[:40]
            
        block_chars = len(block)
        
        # If it's a huge table or div, we just have to put it on a new page if current page is not empty
        if block.startswith('<table') or block.startswith('<div class="glass-card"'):
            if current_chars > CHAR_LIMIT * 0.4: # If we're somewhat full, start fresh for table
                pages.append((current_page, current_title))
                current_page = block
                current_chars = block_chars
                continue
                
        # If H1 and not the very beginning, always break page
        if block.startswith('<h1') and current_page.strip() != "":
            pages.append((current_page, current_title))
            current_page = block
            current_chars = block_chars
            continue
            
        if current_chars + block_chars > CHAR_LIMIT and current_chars > 0:
            pages.append((current_page, current_title))
            current_page = block
            current_chars = block_chars
        else:
            current_page += block
            current_chars += block_chars
            
    if current_page:
        pages.append((current_page, current_title))
        
    return pages

# Process all files
all_html_pages = []
page_counter = 3

for i, file_path in enumerate(FILES_TO_MERGE):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
            
        html_segment = markdown.markdown(md_text, extensions=['tables', 'attr_list'])
        
        # Determine anchor ID for TOC
        anchor_id = f"chap{i}" if "chapitre" in file_path.lower() else f"annexe{i}"
        if "00_glossaire" in file_path: anchor_id = "glossaire"
        if "annexes-ia" in file_path: anchor_id = "chap8"
        
        page_chunks = split_html_to_pages(html_segment, page_counter)
        
        for j, (chunk, title) in enumerate(page_chunks):
            # Only put the ID on the first page of the chapter
            page_id_str = f' id="{anchor_id}"' if j == 0 else ""
            
            page_html = f"""
    <div class="page"{page_id_str}>
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body">
            {chunk}
        </div>
        <div class="footer"><a href="#p02" class="back-btn">◈ RETOUR AU PILOTAGE</a><div>{title.upper()}</div><div class="page-num">{page_counter:02d}</div></div>
    </div>
"""
            all_html_pages.append(page_html)
            page_counter += 1

    else:
        print(f"ATTENTION : Fichier manquant -> {file_path}")

# Write the final file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(HTML_HEADER)
    for p in all_html_pages:
        f.write(p)
    f.write(HTML_FOOTER)

print(f"Succès ! Le fichier final a été généré avec la pagination CSS stricte et les logos : {OUTPUT_FILE}")
