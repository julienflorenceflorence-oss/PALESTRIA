import os
import markdown
import re

# Configuration
CONTENT_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\contenu"
OUTPUT_FILE = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\HTML\RAPPORT_DE_MISSION_JULIEN_FLORENCE_2026.html"


# Fichiers dans l'ordre exact
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
    os.path.join(CONTENT_DIR, "11_Annexe_1_PESTEL.md"),
    os.path.join(CONTENT_DIR, "12_Annexe_2_SWOT.md"),
    os.path.join(CONTENT_DIR, "13_Annexe_3_Porter.md"),
    os.path.join(CONTENT_DIR, "14_Annexe_4_Performance_ROI.md"),
    os.path.join(CONTENT_DIR, "15_Annexe_5_Churn_Finance.md"),
    os.path.join(CONTENT_DIR, "16_Annexe_6_Script_Cold_Call.md"),
    os.path.join(CONTENT_DIR, "17_Annexe_7_Script_Younes.md"),
    os.path.join(CONTENT_DIR, "18_Annexe_8_Note_Cadrage.md"),
    os.path.join(CONTENT_DIR, "19_Annexe_9_Coffre_Fort.md"),
    os.path.join(CONTENT_DIR, "20_Annexe_10_Simulations_Rentabilite.md"),
    os.path.join(CONTENT_DIR, "21_Annexe_11_Preuves_Externes.md")
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
            --gold: #DDA83E; --gold-light: #BCBFD0; --bg: #0F163D; /* Slightly darker Deep Blue for more 'Prestige' depth */
            --card-bg: rgba(255, 255, 255, 0.03); --border: rgba(221, 168, 62, 0.4); --text: rgba(255, 255, 255, 0.92);
        }
        * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        
        /* ROCKET SCHOOL RULES : Justified text + 1.5 line height */
        html, body { margin: 0; padding: 0; background-color: var(--bg); color: var(--text); font-family: 'Montserrat', sans-serif; scroll-behavior: smooth; text-align: justify; line-height: 1.6; }
        
        /* The .page container is exactly A4 size */
        .page {
            width: 210mm; 
            height: 297mm; 
            background-color: var(--bg); 
            margin: 40px auto; 
            position: relative;
            padding: 28mm 22mm 22mm 22mm; 
            display: flex; 
            flex-direction: column; 
            overflow: hidden;
            box-shadow: 0 0 80px rgba(0,0,0,0.8); 
            page-break-after: always;
            border: 1px solid rgba(221, 168, 62, 0.1);
        }
        
        @media print { 
            body { background: none; } 
            .page { margin: 0; border: none; box-shadow: none; width: 210mm; height: 297mm; page-break-after: always; } 
            a { color: var(--gold) !important; text-decoration: none; }
            .back-btn { display: none !important; }
        }
        
        .cockpit-frame { position: absolute; top: 12mm; left: 12mm; right: 12mm; bottom: 12mm; border: 1px solid var(--border); pointer-events: none; z-index: 10; opacity: 0.6; }
        .corner { position: absolute; width: 12mm; height: 12mm; border: 2px solid var(--gold); z-index: 11; }
        .top-left { top: 10mm; left: 10mm; border-right: none; border-bottom: none; }
        .top-right { top: 10mm; right: 10mm; border-left: none; border-bottom: none; }
        .bottom-left { bottom: 10mm; left: 10mm; border-right: none; border-top: none; }
        .bottom-right { bottom: 10mm; right: 10mm; border-left: none; border-top: none; }
        
        .content-body { position: relative; z-index: 5; flex-grow: 1; display: flex; flex-direction: column; }
        
        /* Typography overrides for Rocket School */
        h1 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 19pt; text-transform: uppercase; letter-spacing: 3px; margin: 0 0 18px 0; border-bottom: 1px solid var(--gold); padding-bottom: 8px; text-align: left; font-weight: 700; }
        h2 { font-family: 'Cinzel', serif; color: var(--gold-light); font-size: 14pt; margin: 20px 0 12px 0; letter-spacing: 1px; text-align: left; font-weight: 400; }
        h3 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 12pt; margin: 12px 0 6px 0; text-align: left; font-weight: 700; }
        p, li { font-size: 11.5pt; line-height: 1.5; text-align: justify; margin-bottom: 16px; font-weight: 300; }
        ul { margin-top: 0; margin-bottom: 16px; padding-left: 20px; }
        
        .glass-card { background: var(--card-bg); backdrop-filter: blur(15px); border: 1px solid var(--border); padding: 20px; margin: 20px 0; border-radius: 4px; text-align: left; }
        
        .footer { height: 10mm; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; font-family: 'Cinzel', serif; color: var(--gold); font-size: 8.5pt; letter-spacing: 2px; margin-top: auto; z-index: 20; position: relative; }
        
        .cover-content { flex-grow: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .cover-title { font-size: 38pt; margin: 35px 0; line-height: 1.1; text-align: center; border: none; color: var(--gold); font-weight: 900; }
        .tagline { font-family: 'Cinzel', serif; font-size: 13pt; letter-spacing: 10px; color: var(--gold-light); margin-bottom: 45px; }
    
        /* Dashboard styling remains unchanged */
        .dashboard-tile { display: flex; flex-direction: column; justify-content: space-between; padding: 18px !important; margin: 0 !important; transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); border: 1px solid rgba(221, 168, 62, 0.25) !important; background: rgba(255, 255, 255, 0.02) !important; border-radius: 6px; position: relative; overflow: hidden; z-index: 100; text-decoration: none; height: 100%; text-align: left; }
        .dashboard-tile:hover { background: rgba(221, 168, 62, 0.08) !important; border-color: #DDA83E !important; transform: translateY(-4px); box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        .tile-status { font-size: 6.5pt; letter-spacing: 2px; border: 1px solid rgba(255,255,255,0.3); padding: 4px 10px; width: fit-content; margin-bottom: 10px; font-weight: 700; color: #fff; text-transform: uppercase; }
        .tile-icon { font-size: 24pt; color: #DDA83E; margin-bottom: 8px; }
        .tile-title { font-family: 'Cinzel'; font-weight: 700; font-size: 11.5pt; color: #fff; margin-bottom: 8px; letter-spacing: 1.5px; text-align: left;}
        .tile-desc { font-size: 8.5pt; line-height: 1.4; color: rgba(255,255,255,0.6); flex-grow: 1; text-align: left;}
        .tile-meta { font-size: 6.5pt; font-family: 'Cinzel'; color: #DDA83E; text-align: right; margin-top: 12px; font-weight: 700; letter-spacing: 1px;}
        .dashboard-grid { display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(3, 1fr); gap: 18px; z-index: 100; flex-grow: 1; padding: 15px 0; position: relative; }
        .dashboard-tile * { text-decoration: none !important; color: inherit; }

        .director-note { border-left: 4px solid var(--gold); background: rgba(221, 168, 62, 0.04); padding: 15px 20px; margin: 18px 0; font-size: 9.5pt; font-style: italic; text-align: left;}
        .director-note strong { font-family: 'Cinzel'; font-size: 8.5pt; letter-spacing: 1.5px; display: block; margin-bottom: 6px; color: var(--gold); text-transform: uppercase; }

        .back-btn { background: rgba(221, 168, 62, 0.08); border: 1px solid var(--gold); color: var(--gold) !important; padding: 5px 14px; font-family: 'Cinzel'; font-size: 7.5pt; letter-spacing: 1.5px; cursor: pointer; transition: 0.3s; text-decoration: none !important; display: inline-flex; align-items: center; gap: 8px; }
        .back-btn:hover { background: var(--gold); color: #0F163D !important; }
        
        table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 9pt; text-align: left; }
        th, td { border: 1px solid var(--border); padding: 10px; text-align: left; vertical-align: top; }
        th { font-family: 'Cinzel', serif; color: var(--gold); background: rgba(221, 168, 62, 0.1); }
        td { background: var(--card-bg); }

        a { color: var(--gold); text-decoration: none; border-bottom: 1px dotted rgba(221, 168, 62, 0.4); transition: 0.3s; }
        a:hover { border-bottom: 1px solid var(--gold); }
    </style>
</head>
<body>

    <!-- PAGE 1: COVER -->
    <div class="page" id="p01">
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body cover-content">
            
            <div style="display: flex; gap: 50px; margin-bottom: 50px; align-items: center;">
                <img src="charte graphique/image Happy House.png" alt="Happy House" style="height: 90px; object-fit: contain;">
                <img src="charte graphique/rocket logo 2.png" alt="Rocket School" style="height: 75px; object-fit: contain;">
            </div>

            <div class="tagline">CONSULTING ANALYSIS</div><h1 class="cover-title" style="text-align: center; border:none;">RAPPORT DE MISSION<br>STRATÉGIQUE 2026</h1>
            <div class="glass-card" style="width: 85%; text-align: center; border-radius: 8px; border: 2px solid var(--gold);"><div style="font-style:italic; font-family:'Playfair Display'; color:var(--gold-light); font-size: 14pt;">"Diagnostic, Plan d'Action et Pilotage Opérationnel : Transformer le Prestige en Performance."</div></div>
            <div style="margin-top: 60px; font-family: 'Cinzel'; font-size: 20pt; letter-spacing: 6px; text-align: center; font-weight: 700;">JULIEN FLORENCE</div>
            <div style="color: var(--gold); margin-top: 15px; text-align: center; font-family: 'Montserrat'; font-weight: 400; letter-spacing: 2px;">Responsable du Développement Stratégique</div>
        </div>
        <div class="footer"><div>HAPPY HOUSE & ROCKET SCHOOL | DOSSIER FINAL</div><div class="page-num">01</div></div>
    </div>
    
    <!-- PAGE 2: REMERCIEMENTS (OBLIGATOIRE ROCKET SCHOOL) -->
    <div class="page" id="p02_remerciements">
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body">
            <h1 style="text-align:center; border: none; font-size: 28pt; margin-top: 25%; margin-bottom: 25px;">REMERCIEMENTS</h1>
            <div style="width: 80px; height: 3px; background: var(--gold); margin: 0 auto 50px auto;"></div>
            
            <p style="text-align: justify; margin-bottom: 22px;">Je tiens en premier lieu à remercier sincèrement l'équipe pédagogique et le corps professoral de <strong>Rocket School</strong>. La qualité des enseignements, la pertinence des modules de Growth Hacking et la rigueur de l'accompagnement m'ont permis de transformer une expérience de terrain en une véritable posture de Responsable Stratégique.</p>
            
            <p style="text-align: justify; margin-bottom: 22px;">Mes remerciements s'adressent également à la direction et aux équipes de <strong>Happy House</strong>. Je remercie particulièrement Patrice Kermarrec de m'avoir accordé sa confiance et de m'avoir laissé la liberté opérationnelle nécessaire pour auditer, déconstruire et rebâtir un modèle d'acquisition performant. Ce terrain de jeu entrepreneurial a été une opportunité inestimable de mettre en application la méthode "Predictable Revenue".</p>
            
            <p style="text-align: justify; margin-bottom: 22px;">Enfin, je souhaite exprimer ma reconnaissance envers <strong>Ruddy</strong>, pour son expertise technique et son travail fondamental sur l'automatisation de notre infrastructure de données, ainsi qu'envers <strong>Younes</strong>, avec qui la collaboration a été aussi formatrice sur le plan managérial que fructueuse sur le plan commercial. Le passage de l'artisanat à l'industrialisation est avant tout une aventure humaine, et leur engagement respectif a été déterminant dans le succès de cette mission.</p>
        </div>
        <div class="footer"><div>HAPPY HOUSE & ROCKET SCHOOL</div><div class="page-num">02</div></div>
    </div>

    <!-- PAGE 3: DASHBOARD -->
    <div class="page" id="p03">
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body" style="padding: 10px 10px;">
            <h1 style="text-align:center; border-bottom: 2px solid var(--gold); padding-bottom:12px; margin-bottom: 12px; font-weight: 900;">SOMMAIRE STRATÉGIQUE</h1>
            <div style="text-align: center; color: var(--gold); letter-spacing: 6px; font-size: 9.5pt; margin-bottom: 30px; font-weight: 700;">NAVIGUER DANS LES AXES DE MISSION</div>

            <div class="dashboard-grid">
                
                <a href="#chap1" class="dashboard-tile">
                    <div class="tile-status">VISION</div>
                    <div class="tile-icon">◈</div>
                    <div class="tile-title">I. VISION</div>
                    <div class="tile-desc">Introduction, problématique et trajectoire 2026 du réseau Happy House.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap3" class="dashboard-tile">
                    <div class="tile-status">AUDIT</div>
                    <div class="tile-icon">◎</div>
                    <div class="tile-title">II. IDENTITY</div>
                    <div class="tile-desc">Diagnostic Interne : L'actif data et l'audit qualitatif du churn.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap2" class="dashboard-tile">
                    <div class="tile-status" style="color:var(--gold); border-color:var(--gold);">MARKET</div>
                    <div class="tile-icon">◬</div>
                    <div class="tile-title">III. DIAGNOSTICS</div>
                    <div class="tile-desc">Analyse profonde des forces du marché et la Loi Anti-Airbnb.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap4" class="dashboard-tile">
                    <div class="tile-status" style="color:#2ECC71; border-color:#2ECC71;">ENGINE</div>
                    <div class="tile-icon">⚙</div>
                    <div class="tile-title">IV. SALES ENGINE</div>
                    <div class="tile-desc">Ingénierie d'acquisition, budget Tech 0€ et closing de phase test.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap5" class="dashboard-tile">
                    <div class="tile-status">INSIGHTS</div>
                    <div class="tile-icon">☖</div>
                    <div class="tile-title">V. FIELD RESEARCH</div>
                    <div class="tile-desc">Interviews terrain et analyse de la "Solitude opérationnelle".</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap6" class="dashboard-tile">
                    <div class="tile-status">LOYALTY</div>
                    <div class="tile-icon">☍</div>
                    <div class="tile-title">VI. RETENTION</div>
                    <div class="tile-desc">Stratégie Double Détente et intégration de l'expérience phygitale.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap7" class="dashboard-tile">
                    <div class="tile-status" style="color:var(--gold-light); border-color:var(--gold-light);">VALUE</div>
                    <div class="tile-icon">⊘</div>
                    <div class="tile-title">VII. PERFORMANCE</div>
                    <div class="tile-desc">Étude du Cas Durentie, Bilan Pro et Management Commercial.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

                <a href="#chap8" class="dashboard-tile">
                    <div class="tile-status" style="color:#E74C3C; border-color:#E74C3C;">VAULT</div>
                    <div class="tile-icon">🔒</div>
                    <div class="tile-title">VIII. VAULT</div>
                    <div class="tile-desc">Annexes techniques, Matrices, Scripts et preuves Drive.</div>
                    <div class="tile-meta">CONSULTER</div>
                </a>

            </div>
        </div>
        <div class="footer"><div>SOMMAIRE</div><div class="page-num">03</div></div>
    </div>
"""

HTML_FOOTER = """
</body>
</html>
"""

def split_html_to_pages(html_content, start_page_num):
    """
    Splits the HTML content into pages of roughly equal length.
    Now splits long lists (ul/ol) to avoid overflowing pages.
    """
    pages = []
    CHAR_LIMIT = 2400 
    
    # Pre-process lists to make them splittable: 
    # Replace <ul>...</ul> with individual list items wrapped in small <ul> for splitting
    splittable_content = html_content
    splittable_content = re.sub(r'<ul>(.*?)</ul>', lambda m: '\n'.join([f'<ul style="margin-bottom:0; padding-bottom:0;">{li}</ul>' for li in re.findall(r'<li>.*?</li>', m.group(1), re.DOTALL)]), splittable_content, flags=re.DOTALL)
    
    blocks = re.split(r'(<h[1-6][^>]*>.*?</h[1-6]>|<p>.*?</p>|<ul[^>]*>.*?</ul>|<ol[^>]*>.*?</ol>|<table[^>]*>.*?</table>|<div[^>]*>.*?</div>|<blockquote>.*?</blockquote>|<hr\s*/?>)', splittable_content, flags=re.DOTALL)
    
    current_page = ""
    current_chars = 0
    current_title = "ANALYSE STRATÉGIQUE"
    
    for block in blocks:
        if not block or not block.strip(): continue
        
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', block)
        if h1_match:
            current_title = re.sub(r'<[^>]+>', ' ', h1_match.group(1))[:40]
            
        block_chars = len(block)
        
        # Tables or big divs start a new page if we already have content
        if block.startswith('<table') or block.startswith('<div class="glass-card"'):
            if current_chars > CHAR_LIMIT * 0.2: 
                pages.append((current_page, current_title))
                current_page = block
                current_chars = block_chars
                continue
                
        # H1 always breaks page
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

# Process all Markdown files
all_html_pages = []
page_counter = 4 # Start at 4 because of Cover, Thanks, and Dashboard

for i, file_path in enumerate(FILES_TO_MERGE):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
            
        html_segment = markdown.markdown(md_text, extensions=['tables', 'attr_list'])
        
        anchor_id = f"chap{i}" if "chapitre" in file_path.lower() else f"annexe{i}"
        if "00_glossaire" in file_path: anchor_id = "glossaire"
        if "annexes-ia" in file_path: anchor_id = "chap8"
        
        page_chunks = split_html_to_pages(html_segment, page_counter)
        
        for j, (chunk, title) in enumerate(page_chunks):
            page_id_str = f' id="{anchor_id}"' if j == 0 else ""
            
            page_html = f"""
    <div class="page"{page_id_str}>
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body">
            {chunk}
        </div>
        <div class="footer"><a href="#p03" class="back-btn">◈ RETOUR AU SOMMAIRE</a><div>{title.upper()}</div><div class="page-num">{page_counter:02d}</div></div>
    </div>
"""
            all_html_pages.append(page_html)
            page_counter += 1

    else:
        print(f"ATTENTION : Fichier manquant -> {file_path}")

# The Vault annex is now merged as a regular Markdown file (19_Annexe_9_Coffre_Fort.md)
pass



# Write the final file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(HTML_HEADER)
    for p in all_html_pages:
        f.write(p)
    f.write(HTML_FOOTER)

print(f"Succès ! Le fichier final ROCKET SCHOOL a été généré : {OUTPUT_FILE}")

