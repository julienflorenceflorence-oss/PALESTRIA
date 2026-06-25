import os
import markdown

# Configuration
CONTENT_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\contenue"
ANNEX_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\annexe\annexes .md"
COFFRE_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\annexe"
OUTPUT_FILE = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\RDM_FINAL_ASSEMBLE.html"

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

# Template HTML "Édition Prestige" A4 pour PDF
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Rapport de Mission 2026 - Julien Florence</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --gold: #DDA83E; 
            --gold-light: #BCBFD0; 
            --bg: #0A0C1A;
            --card-bg: rgba(255, 255, 255, 0.03); 
            --border: rgba(212, 175, 55, 0.3); 
            --text: rgba(255, 255, 255, 0.95);
        }}
        * {{ box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
        html, body {{ margin: 0; padding: 0; background-color: #050505; color: var(--text); font-family: 'Montserrat', sans-serif; }}
        
        .page {{
            width: 210mm; 
            background-color: #0F1115; 
            margin: 40px auto; 
            position: relative;
            padding: 20mm 15mm; 
            box-shadow: 0 0 50px rgba(0,0,0,0.8); 
        }}

        @media print {{ 
            body {{ background: none; }} 
            .page {{ margin: 0; border: none; box-shadow: none; width: 210mm; }} 
            .no-print {{ display: none !important; }}
            /* Page breaks for major sections */
            h1 {{ page-break-before: always; }}
            /* Keep tables from breaking across pages if possible */
            table {{ page-break-inside: auto; }}
            tr {{ page-break-inside: avoid; page-break-after: auto; }}
            /* Force link colors in PDF */
            a {{ color: var(--gold) !important; text-decoration: none; }}
        }}
        
        h1 {{ font-family: 'Cinzel', serif; color: var(--gold); font-size: 20pt; text-transform: uppercase; letter-spacing: 4px; margin: 40px 0 20px 0; border-bottom: 2px solid var(--gold); padding-bottom: 10px; text-align: center; }}
        h1:first-child {{ margin-top: 0; }}
        h2 {{ font-family: 'Cinzel', serif; color: var(--gold-light); font-size: 14pt; margin: 30px 0 15px 0; letter-spacing: 2px; border-left: 4px solid var(--gold); padding-left: 15px; }}
        h3 {{ font-family: 'Cinzel', serif; color: var(--gold); font-size: 11pt; margin: 20px 0 10px 0; text-transform: uppercase; }}
        
        p {{ font-size: 10pt; line-height: 1.6; text-align: justify; margin-bottom: 15px; font-weight: 300; }}
        li {{ font-size: 10pt; line-height: 1.6; margin-bottom: 8px; font-weight: 300; }}
        
        /* Table Styles for Annexes */
        table {{ width: 100%; border-collapse: collapse; margin: 25px 0; font-size: 9pt; }}
        th, td {{ border: 1px solid var(--border); padding: 12px; text-align: left; vertical-align: top; }}
        th {{ font-family: 'Cinzel', serif; color: var(--gold); background: rgba(212, 175, 55, 0.1); }}
        td {{ background: var(--card-bg); }}

        /* Blockquotes for 'director-note' styling from markdown */
        blockquote {{ border-left: 3px solid var(--gold); background: rgba(221, 168, 62, 0.05); padding: 12px 15px; margin: 20px 0; font-style: italic; }}
        
        hr {{ border: 0; border-top: 1px dashed var(--border); margin: 40px 0; }}
        
        /* Buttons / Links */
        a.btn {{ display: inline-block; padding: 10px 20px; background-color: transparent; border: 1px solid var(--gold); color: var(--gold); text-decoration: none; font-family: 'Cinzel', serif; font-size: 9pt; font-weight: bold; border-radius: 4px; }}
    </style>
</head>
<body>

<!-- PAGE DE GARDE -->
<div class="page" style="height: 297mm; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
    <div style="font-family: 'Cinzel'; font-size: 12pt; letter-spacing: 8px; color: var(--gold); margin-bottom: 40px;">CONSULTING ANALYSIS</div>
    <h1 style="font-size: 32pt; border: none; margin-top: 20px;">RAPPORT DE MISSION<br>STRATÉGIQUE 2026</h1>
    <div style="width: 60px; height: 3px; background: var(--gold); margin: 30px 0;"></div>
    <div style="font-family: 'Playfair Display'; font-style: italic; font-size: 14pt; color: var(--gold-light);">"Diagnostic, Plan d'Action et Pilotage Opérationnel : Transformer le Prestige en Performance."</div>
    <div style="margin-top: 80px; font-family: 'Cinzel'; font-size: 18pt; letter-spacing: 5px;">JULIEN FLORENCE</div>
    <div style="color: var(--gold); margin-top: 10px;">Consultant Expert en Développement Stratégique</div>
    <div style="margin-top: auto; font-size: 9pt; opacity: 0.5; font-family: 'Cinzel'; letter-spacing: 2px;">HAPPY HOUSE | ÉDITION PRESTIGE</div>
</div>

<!-- CONTENU PRINCIPAL -->
<div class="page">
    {content}
</div>

</body>
</html>
"""

# Assemblage
merged_markdown = ""
for file_path in FILES_TO_MERGE:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            # On ajoute un saut de page forcé (pour le CSS) avant chaque H1 (Chapitre)
            merged_markdown += f.read() + "\n\n---\n\n"
    else:
        print(f"ATTENTION : Fichier manquant -> {file_path}")

# Conversion Markdown -> HTML
# Les extensions 'tables' et 'attr_list' permettent de gérer les tableaux et d'injecter des classes CSS
html_content = markdown.markdown(merged_markdown, extensions=['tables', 'attr_list'])

# Injection dans le template
final_html = HTML_TEMPLATE.format(content=html_content)

# Écriture du fichier final
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Succès ! Le fichier final a été généré : {OUTPUT_FILE}")
