import codecs

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix the footer CSS to make it clearer (background, position)
old_footer_css = ".footer { position: absolute; bottom: 10mm; left: 20mm; right: 20mm; display: flex; justify-content: space-between; align-items: center; font-family: 'Cinzel', serif; font-size: 7.5pt; color: var(--gold); letter-spacing: 2px; z-index: 100; }"
new_footer_css = ".footer { position: absolute; bottom: 8.5mm; left: 15mm; right: 15mm; display: flex; justify-content: space-between; align-items: center; font-family: 'Cinzel', serif; font-size: 8.5pt; color: var(--gold); letter-spacing: 2px; z-index: 100; background: var(--bg-dark); padding: 2px 10px; font-weight: bold; border-top: 1px solid rgba(221,168,62,0.3); }"
c = c.replace(old_footer_css, new_footer_css)

# Fix the section titles for the Annexes to be perfectly clear
c = c.replace('"section": "EXTRAITS PIÈCES JUSTIFICATIVES"', '"section": "ANNEXE 11 : EXTRAITS PIÈCES JUSTIFICATIVES"')
c = c.replace('"section": "DOSSIER DES PREUVES CLOUD"', '"section": "ANNEXE 12 : DOSSIER DRIVE SÉCURISÉ"')

# Prevent content from overlapping the footer in densely packed annexes
old_content_css = ".content { padding: 25mm 20mm; position: relative; z-index: 10; flex-grow: 1; }"
new_content_css = ".content { padding: 20mm 20mm 35mm 20mm; position: relative; z-index: 10; flex-grow: 1; }"
c = c.replace(old_content_css, new_content_css)

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Footer style and Annex sections updated.")
