import re
import os

output_html = 'RDM_SOBRE_PRINT_READY.html'
blocks_dir = '03-chapitres/RDM_A150_FINAL'
rocket_logo = '03-chapitres/rocket logo 2.png'
hh_logo = '03-chapitres/image Happy House.png'
bg_image = 'Ext-015 ©Anne Lanta.jpg'

CLEAN_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600;700&display=swap');

    :root {
        --text-main: #333333;
        --text-light: #555555;
        --accent-dark: #0B132B;
        --accent-gold: #D4AF37;
        --border-light: #E0E0E0;
    }

    @media print {
        @page { size: A4; margin: 0; }
        body { background: #FFFFFF !important; color: #000 !important; }
        .page-frame { display: none; }
        .no-print { display: none; }
        h1 { break-before: page; margin-top: 25mm !important; }
        h2, h3 { break-after: avoid; }
        table, tr, img { break-inside: avoid; }
    }

    body { margin: 0; padding: 0; background: #EEE; font-family: 'Montserrat', sans-serif; color: var(--text-main); line-height: 1.6; }

    .paper-container {
        width: 210mm;
        margin: 0 auto;
        background: #FFFFFF;
        box-shadow: 0 0 20px rgba(0,0,0,0.2);
        position: relative;
    }

    .cover-page {
        width: 210mm; height: 297mm;
        background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.95)), url('Ext-015 ©Anne Lanta.jpg') no-repeat center center;
        background-size: cover;
        display: flex; flex-direction: column; align-items: center; text-align: center;
        padding: 40mm 20mm; box-sizing: border-box;
        page-break-after: always;
    }

    .main-body { padding: 30mm 25mm; box-sizing: border-box; }

    h1 { font-family: 'Cinzel'; color: var(--accent-dark); font-size: 24pt; margin: 40px 0 30px 0; text-transform: uppercase; border-bottom: 2pt solid var(--accent-gold); padding-bottom: 10px; }
    h2 { font-family: 'Cinzel'; color: var(--accent-dark); border-left: 5pt solid var(--accent-gold); padding-left: 15px; margin: 35px 0 15px 0; font-size: 16pt; text-transform: uppercase; }
    h3 { font-family: 'Cinzel'; color: var(--accent-dark); margin: 25px 0 10px 0; font-size: 12pt; border-bottom: 1px solid #CCC; display: inline-block; padding-bottom: 4px; }
    
    p, li { font-size: 11pt; line-height: 1.8; margin-bottom: 15px; text-align: justify; }
    strong { color: #000; font-weight: 700; }

    .status-tag { display: inline-block; padding: 3px 10px; border-radius: 2px; font-size: 8pt; font-weight: 800; text-transform: uppercase; margin-right: 8px; border: 1px solid currentColor; vertical-align: middle; }
    
    table { width: 100%; border-collapse: collapse; margin: 30px 0; table-layout: fixed; }
    th, td { border: 1px solid #DDD; padding: 12px; font-size: 10pt; text-align: left; }
    th { background: #F4F4F4; font-family: 'Cinzel'; font-weight: 700; }

    .page-footer {
        padding: 5mm 25mm;
        display: flex; justify-content: space-between;
        font-family: 'Cinzel'; font-size: 8pt; color: #999;
        border-top: 1px solid #EEE;
    }
</style>
"""

def md_to_html(text):
    lines = text.split('\n')
    in_table = False
    html_lines = []
    for line in lines:
        line = line.strip()
        if not line: continue
        if line.startswith('|'):
            if not in_table: html_lines.append('<table>'); in_table = True
            if '---' in line: continue
            cells = [c.strip() for c in line.split('|') if c.strip()]
            tag = 'th' if any(k in line for k in ['Indicateur', 'Variable', 'Source', 'Métrique', 'MÉTRIQUE', 'Catégorie', 'Acteur', 'Dimension', 'Force', 'ID', 'Phase']) else 'td'
            html_lines.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
        else:
            if in_table: html_lines.append('</table>'); in_table = False
            if line.startswith('# '): line = f'<h1>{line[2:]}</h1>'
            elif line.startswith('## '): line = f'<h2>{line[3:]}</h2>'
            elif line.startswith('### '): line = f'<h3>{line[4:]}</h3>'
            elif line.startswith('#### '): line = f'<h4>{line[5:]}</h4>'
            
            line = line.replace('[VERT]', '<span class="status-tag" style="color: #27AE60;">VALIDE</span>')
            line = line.replace('[ROUGE]', '<span class="status-tag" style="color: #C0392B;">CRITIQUE</span>')
            line = line.replace('[BLEU]', '<span class="status-tag" style="color: #2980B9;">ANALYSE</span>')
            line = line.replace('[OR]', '<span class="status-tag" style="color: #D4AF37;">STRATÉGIE</span>')
            
            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            
            if line.startswith('- '): line = f'<li>{line[2:]}</li>'
            elif line[0:3].isdigit() and line[3] == '.': line = f'<li>{line[3:]}</li>'
            elif not line.startswith('<'): line = f'<p>{line}</p>'
            html_lines.append(line)
    if in_table: html_lines.append('</table>')
    return "\n".join(html_lines)

# FETCH ALL BLOCKS
block_files = sorted([f for f in os.listdir(blocks_dir) if f.endswith('.md')])
all_html_content = ""
for bf in block_files:
    with open(os.path.join(blocks_dir, bf), 'r', encoding='utf-8') as f:
        all_html_content += md_to_html(f.read())

final_html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>RDM SOBRE - JULIEN FLORENCE</title>
    {CLEAN_CSS}
</head>
<body>
    <div class="paper-container">
        <div class="cover-page">
            <div style="width: 100%; display: flex; justify-content: space-between; margin-bottom: 40mm;">
                <img src="../{rocket_logo}" alt="Rocket School" style="height: 60px;">
                <img src="../{hh_logo}" alt="Happy House" style="height: 60px;">
            </div>
            <div style="font-family: 'Cinzel'; color: var(--accent-dark); letter-spacing: 5px; margin-bottom: 10mm;">ROCKET SCHOOL TOULOUSE</div>
            <h1 style="border:none; font-size: 36pt; line-height: 1.1; margin-bottom: 5mm; page-break-before: auto;">INDUSTRIALISATION DE LA CROISSANCE :<br>L'ARSENAL HAPPY HOUSE</h1>
            <div style="font-size: 16pt; font-style: italic; color: #666; margin-bottom: 30mm;">Mémoire de Mission Professionnelle</div>
            
            <div style="border-left: 4px solid var(--accent-gold); padding: 20px; text-align: left; width: 85%; background: #F9F9F9; margin-bottom: auto;">
                <strong>Problématique :</strong><br>
                « Comment concilier l'industrialisation des processus d'acquisition numérique et la promesse d'exclusivité "Waouh" pour piloter le passage à l'échelle d'un réseau d'hébergements indépendants ? »
            </div>

            <div style="width: 100%; display: flex; justify-content: space-between; align-items: flex-end; text-align: left; margin-top: 40px;">
                <div>
                    <div style="font-size: 18pt; font-weight: 700; color: #000;">JULIEN FLORENCE</div>
                    <div style="font-family: 'Cinzel'; font-size: 10pt; color: var(--accent-gold); letter-spacing: 2px;">DIRECTION DU DÉVELOPPEMENT OPÉRATIONNEL</div>
                </div>
                <div style="text-align: right; font-size: 10pt; color: #666;">
                    <strong>Session 2026</strong><br>
                    Tuteur : Patrice Kermarrec
                </div>
            </div>
        </div>

        <div class="main-body">
            {all_html_content}
        </div>

        <div class="page-footer">
            <div>JULIEN FLORENCE | RDM 2026</div>
            <div>ROCKET SCHOOL TOULOUSE</div>
        </div>
    </div>
</body>
</html>
"""

with open(output_html, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("V18 FULL CONTENT ENGINE: High-density sober document generated.")
