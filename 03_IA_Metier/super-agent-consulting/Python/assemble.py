import os
import re

CONTENT_DIR = r'mémoire/RDM 3.0/contenu'
TEMPLATE_PATH = r'mémoire/RDM 3.0/TEMPLATE_V2.html'
OUTPUT_PATH = r'mémoire/RDM 3.0/RDM_FINAL_PRO_2026.html'

def md_to_clean_html(text):
    # Titres
    text = re.sub(r'^# (.*?)$', r'<h1 id="title-\1">\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # Listes (Lexique)
    if 'AE (Account Executive)' in text or 'LTV (Lifetime Value)' in text:
        items = re.findall(r'- \*\*(.*?)\*\* :(.*?)$', text, flags=re.MULTILINE)
        if items:
            list_html = '<ul class="lexique-list">'
            for term, desc in items:
                list_html += f'<li class="lexique-item"><span class="lexique-term">{term}</span> : {desc}</li>'
            list_html += '</ul>'
            return list_html

    # Paragraphes
    text = re.sub(r'^(?!<[hu]|<li|<ul)(.*?)$', r'<p>\1</p>', text, flags=re.MULTILINE)
    
    # Gras et Italic
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    return text

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

# Assemblage
header = template.split('<body>')[0] + '<body>'
footer = '</body></html>'

# 1. Couverture (Page 1)
cover = """
<div class="page prestige" id="p01">
    <div class="logos-container">
        <img src="charte graphique/rocket logo 2.png" class="logo-rs">
        <img src="charte graphique/image Happy House.png" class="logo-hh">
    </div>
    <div class="cover-main">
        <div style="letter-spacing: 10px; font-size: 14pt; margin-bottom: 20px;">MISSION STRATÉGIQUE</div>
        <h1 style="font-size: 42pt; line-height: 1.1; margin: 0; color: #DDA83E;">RAPPORT DE MISSION<br>CONSULTANT 2026</h1>
        <div style="width: 150px; height: 2px; background: #DDA83E; margin: 40px auto;"></div>
        <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 18pt;">"Transformer le Prestige en Performance par l'Ingénierie Digitale"</div>
        <div style="margin-top: 80px; font-size: 28pt; font-family: 'Cinzel'; font-weight: 900;">JULIEN FLORENCE</div>
        <div style="color: #DDA83E; margin-top: 15px; font-family: 'Montserrat'; letter-spacing: 3px; font-weight: 400;">Directeur du Développement</div>
    </div>
    <div class="footer"><div>HAPPY HOUSE & ROCKET SCHOOL</div><div>01</div></div>
</div>
"""

# 2. Sommaire (Pages 2-3) - On le laisse vide pour l'instant ou on l'assemble
# (L'utilisateur le veut interactif)

# 3. Corps
body = cover
files = sorted([f for f in os.listdir(CONTENT_DIR) if f.endswith('.md')])

p_num = 2
for f in files:
    with open(os.path.join(CONTENT_DIR, f), 'r', encoding='utf-8') as src:
        md = src.read()
    
    style = "prestige" if f.startswith("03") or "Chapitre" in f else "academic"
    
    page = f"""
    <div class="page {style}" id="p{p_num:02d}">
        <div class="content-body {'cover-main' if style=='prestige' else 'academic'}">
            {md_to_clean_html(md)}
        </div>
        <div class="footer">
            <div>JULIEN FLORENCE | RDM 2026</div>
            <div>{p_num:02d}</div>
        </div>
    </div>
    """
    body += page
    p_num += 1

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(header + body + footer)

print(f"RDM Assemblé : {OUTPUT_PATH}")
