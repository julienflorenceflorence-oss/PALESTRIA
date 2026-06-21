import re

filename = 'RDM_STRATEGIC_COCKPIT_2026.html'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# On retire le bouton BACK TO CENTER spécifiquement dans les sections p01 et p02
# Le bouton a été inséré au début du footer : <div class="footer"><a href="#toc" class="back-btn">◈ BACK TO CENTER</a>

# Nettoyage Page 01
content = re.sub(r'(?s)(<div class="page" id="p01">.*?)<a href="#toc" class="back-btn">◈ BACK TO CENTER</a>', r'\1', content)

# Nettoyage Page 02
content = re.sub(r'(?s)(<div class="page" id="p02">.*?)<a href="#toc" class="back-btn">◈ BACK TO CENTER</a>', r'\1', content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Boutons supprimés sur P1 et P2.")
