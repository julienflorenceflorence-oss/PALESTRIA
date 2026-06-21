import os
import re

output_path = 'RDM_ULTRA_PRESTIGE_40P.html'
blocks_dir = '03-chapitres/RDM_A150_FINAL'
background_image = 'Ext-015 ©Anne Lanta.jpg'
rocket_logo = '03-chapitres/rocket logo 2.png'
hh_logo = '03-chapitres/image Happy House.png'

# V17 ROBUST PRINT ENGINE
LUXURY_V17_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600;700&display=swap');

    :root {
        --bg: #0F1115;
        --gold: #D4AF37;
        --border-color: rgba(212, 175, 55, 0.2);
        --text-dim: #E0E0E0;
    }

    @media print {
        @page { 
            size: A4; 
            margin: 0mm; 
        }
        body { 
            background-color: var(--bg) !important; 
            -webkit-print-color-adjust: exact; 
            print-color-adjust: exact;
            color: #FFFFFF !important;
        }
        
        /* Removing overlapping fixed elements in multi-page print */
        .page-frame { display: none; }
        
        .page-footer {
            position: relative;
            display: flex;
            justify-content: space-between;
            border-top: 1px solid var(--gold);
            padding-top: 5mm;
            margin-top: 20mm;
            font-family: 'Cinzel', serif;
            font-size: 8pt;
            color: var(--gold);
            opacity: 0.8;
            page-break-after: always;
        }

        h1, h2, h3 { break-after: avoid; }
        .main-body > h1 { break-before: page; margin-top: 0; padding-top: 20mm; }
        table, tr, img { break-inside: avoid; }
        p, li { break-inside: auto; }
    }

    body { 
        margin: 0; 
        padding: 0; 
        background: #222; 
        font-family: 'Montserrat', sans-serif; 
        color: #FFFFFF;
        line-height: 1.6;
    }

    .printable-content {
        background: var(--bg);
        width: 210mm;
        margin: 0 auto;
        position: relative;
    }

    .cover-page {
        width: 210mm; height: 297mm;
        background: linear-gradient(rgba(15,17,21,0.4), rgba(15,17,21,0.8)), url('""" + background_image + """') no-repeat center center;
        background-size: cover;
        display: flex; flex-direction: column; align-items: center;
        padding: 30mm 20mm; box-sizing: border-box; position: relative;
        page-break-after: always;
    }
    
    .logo-container {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 40mm;
    }
    .logo-box-main { 
        background: rgba(255,255,255,0.05); 
        padding: 10px 20px; 
        border-radius: 4px;
        height: 20mm;
        display: flex; align-items: center;
    }
    .logo-box-main img { height: 100%; width: auto; object-fit: contain; }

    .cover-title-group { text-align: center; margin-top: 10mm; }
    .cover-school { font-size: 12pt; letter-spacing: 10px; color: var(--gold); margin-bottom: 10mm; text-transform: uppercase; font-weight: 400; }
    .cover-title { font-family: 'Cinzel'; font-size: 32pt; color: #FFFFFF; font-weight: 900; line-height: 1.2; margin-bottom: 5mm; }
    .cover-subtitle { font-family: serif; font-style: italic; font-size: 18pt; color: var(--gold); margin-bottom: 30mm; opacity: 0.9; }
    
    .cover-quote {
        background: rgba(212, 175, 55, 0.1); border-left: 3px solid var(--gold);
        padding: 20px 30px; text-align: left; width: 80%; margin-bottom: 30mm;
    }
    .cover-quote p { font-size: 11pt; line-height: 1.5; color: #FFFFFF; margin: 0; font-weight: 300; font-style: italic; }

    .cover-footer { position: absolute; bottom: 25mm; width: 85%; display: flex; justify-content: space-between; align-items: flex-end; }
    .author-info { text-align: left; }
    .author-name { font-size: 20pt; font-weight: 700; letter-spacing: 1px; color: #FFF; }
    .author-role { font-family: 'Cinzel'; font-size: 8pt; color: var(--gold); letter-spacing: 3px; margin-top: 5px; }

    .main-body {
        padding: 30mm 30mm 10mm 30mm; 
        box-sizing: border-box;
    }

    h1 { font-family: 'Cinzel'; color: var(--gold); font-size: 24pt; margin: 60mm 0 40px 0; text-transform: uppercase; letter-spacing: 3px; border-bottom: 1px solid var(--gold); padding-bottom: 10px; break-before: page; }
    h2 { font-family: 'Cinzel'; color: #FFFFFF; border-left: 5px solid var(--gold); padding-left: 20px; margin: 50px 0 25px 0; font-size: 16pt; text-transform: uppercase; letter-spacing: 1px; }
    h3 { font-family: 'Cinzel'; color: var(--gold); margin: 35px 0 15px 0; font-size: 13pt; font-weight: 700; }
    
    p, li { font-size: 11.5pt; line-height: 1.75; color: var(--text-dim); margin-bottom: 18px; text-align: justify; }
    strong { color: #FFFFFF; font-weight: 700; }

    .status-tag { display: inline-block; padding: 4px 12px; border-radius: 2px; font-size: 7.5pt; font-weight: 800; text-transform: uppercase; margin-right: 8px; border: 1px solid currentColor; vertical-align: middle; }
    
    table { width: 100%; border-collapse: collapse; margin: 30px 0; background: rgba(255,255,255,0.02); table-layout: fixed; }
    th, td { border: 1px solid var(--border-color); padding: 15px; font-size: 10.5pt; word-wrap: break-word; }
    th { background: rgba(212, 175, 55, 0.15); color: #FFFFFF; font-family: 'Cinzel'; text-align: left; font-weight: 700; }
    
    .page-footer {
        padding: 5mm 30mm 15mm 30mm;
        display: flex; justify-content: space-between;
        font-family: 'Cinzel'; font-size: 8pt; color: var(--gold);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
</style>
"""

def md_to_html(text):
    # Split by blocks to inject footers
    sections = text.split('\n# ')
    html_out = ""
    
    for i, section in enumerate(sections):
        if not section.strip(): continue
        prefix = "# " if i > 0 or text.startswith('# ') else ""
        content = prefix + section
        
        lines = content.split('\n')
        in_table = False
        section_html = ""
        for line in lines:
            line = line.strip()
            if not line: continue
            if line.startswith('|'):
                if not in_table: section_html += '<table>'; in_table = True
                if '---' in line: continue
                cells = [c.strip() for c in line.split('|') if c.strip()]
                tag = 'th' if any(k in line for k in ['Indicateur', 'Variable', 'Source', 'Métrique', 'MÉTRIQUE']) else 'td'
                section_html += '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>'
            else:
                if in_table: section_html += '</table>'; in_table = False
                if line.startswith('# '): line = f'<h1>{line[2:]}</h1>'
                elif line.startswith('## '): line = f'<h2>{line[3:]}</h2>'
                elif line.startswith('### '): line = f'<h3>{line[4:]}</h3>'
                elif line.startswith('#### '): line = f'<h4>{line[5:]}</h4>'
                
                line = line.replace('[VERT]', '<span class="status-tag" style="color: #2ECC71;">SÉCURISÉ</span>')
                line = line.replace('[ROUGE]', '<span class="status-tag" style="color: #E74C3C;">CRITIQUE</span>')
                line = line.replace('[BLEU]', '<span class="status-tag" style="color: #3498DB;">ANALYSE</span>')
                line = line.replace('[OR]', '<span class="status-tag" style="color: var(--gold);">PRESTIGE</span>')
                
                line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
                
                if line.startswith('- '): line = f'<li>{line[2:]}</li>'
                elif not line.startswith('<'): line = f'<p>{line}</p>'
                section_html += line + "\n"
        if in_table: section_html += '</table>'
        
        # Inject footer after each main H1 section
        footer = f"""
        <div class="page-footer">
            <div>JULIEN FLORENCE | MÉMOIRE STRATÉGIQUE</div>
            <div>PROMO 2026 | ROCKET SCHOOL</div>
        </div>
        """
        html_out += section_html + footer
        
    return html_out

block_files = sorted([f for f in os.listdir(blocks_dir) if f.endswith('.md')])
all_html = ""
for bf in block_files:
    with open(os.path.join(blocks_dir, bf), 'r', encoding='utf-8') as f:
        all_html += md_to_html(f.read())

final_html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>RDM PRESTIGE - JULIEN FLORENCE</title>
    {LUXURY_V17_CSS}
</head>
<body>
    <div class="printable-content">
        <div class="cover-page">
            <div class="logo-container">
                <div class="logo-box-main"><img src="{rocket_logo}" alt="Rocket School"></div>
                <div class="logo-box-main"><img src="{hh_logo}" alt="Happy House"></div>
            </div>
            
            <div class="cover-title-group">
                <div class="cover-school">ROCKET SCHOOL TOULOUSE</div>
                <div class="cover-title">STRATÉGIE DE DÉVELOPPEMENT<br>OPÉRATIONNEL</div>
                <div class="cover-subtitle">Optimisation des leviers d'acquisition et structuration réseau</div>
            </div>

            <div class="cover-quote">
                <p>« Analyse de la modélisation des processus de croissance et de la structuration d'un réseau d'hébergements indépendants dans un contexte de mutation sectorielle. »</p>
            </div>

            <div class="cover-footer">
                <div class="author-info">
                    <div class="author-name">JULIEN FLORENCE</div>
                    <div class="author-role">DIRECTION DU DÉVELOPPEMENT OPÉRATIONNEL</div>
                </div>
                <div style="font-family: 'Cinzel'; font-size: 10pt; color: var(--gold); letter-spacing: 2px;">
                    SESSION 2026
                </div>
            </div>
        </div>

        <div class="main-body">
            {all_html}
        </div>
    </div>
</body>
</html>
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("V17 ROBUST ENGINE: Multi-page overlapping fixed. Ready for clean PDF export.")
