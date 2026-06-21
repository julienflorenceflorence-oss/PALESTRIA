import codecs

with open('mémoire/RDM 3.0/build_rdm_v8_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update the Annexe 11 Text
old_annexe_text = """Conformément aux standards académiques interdisant l'usage exclusif de liens Cloud externes pour les preuves, cette section présente un extrait synthétique des livrables opérationnels produits. <strong>Les documents complets, natifs et exhaustifs sont joints au format physique dans le dossier cartonné officiel remis au jury.</strong>"""

new_annexe_text = """Cette section présente un extrait synthétique des livrables opérationnels produits afin d'en faciliter la lecture directe. <strong>La restitution de ce rapport s'opérant sous un format PDF dématérialisé, l'intégralité des documents natifs et interactifs (tableaux de bord complets, matrices de calculs, contrats) est tenue à la stricte disposition du jury via un Espace Cloud Sécurisé (Drive).</strong>
        </p>
        <div style="text-align: center; margin-bottom: 30px;">
            <a href="#" style="display: inline-block; background: var(--gold); color: #000; padding: 12px 25px; text-decoration: none; font-weight: bold; font-family: 'Cinzel', serif; letter-spacing: 1px; border-radius: 3px;">📥 ACCÉDER AU DOSSIER DRIVE SÉCURISÉ</a>
        </div>
        <p style="display:none;">""" # Hidden p tag to close the opened one from the original string replacement logic if needed, but let's do a cleaner replace.

old_full_p = """<p style="font-size: 10.5pt; text-align: center; margin-bottom: 30px; line-height: 1.6; color: var(--text-muted);">
            Conformément aux standards académiques interdisant l'usage exclusif de liens Cloud externes pour les preuves, cette section présente un extrait synthétique des livrables opérationnels produits. <strong>Les documents complets, natifs et exhaustifs sont joints au format physique dans le dossier cartonné officiel remis au jury.</strong>
        </p>"""

new_full_p = """<p style="font-size: 10.5pt; text-align: center; margin-bottom: 20px; line-height: 1.6; color: var(--text-muted);">
            Cette section présente un extrait synthétique des livrables opérationnels produits afin d'en faciliter la lecture directe. <strong>La restitution de ce rapport s'opérant sous format PDF dématérialisé, l'intégralité des documents natifs et interactifs (tableaux de bord complets, matrices de calculs, contrats) est tenue à la stricte disposition du jury via un Espace Cloud Sécurisé (Drive).</strong>
        </p>
        <div style="text-align: center; margin-bottom: 35px;">
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA" target="_blank" style="display: inline-block; background: var(--gold); color: #000; padding: 10px 20px; text-decoration: none; font-weight: bold; font-family: 'Arial', sans-serif; font-size: 9pt; letter-spacing: 1px; border-radius: 3px;">📥 ACCÉDER AU DOSSIER DRIVE SÉCURISÉ</a>
        </div>"""

c = c.replace(old_full_p, new_full_p)

# 2. Update TOC to say "EXTRAITS & DOSSIER DRIVE"
old_toc_line = '("XII. EXTRAITS DES PIÈCES JUSTIFICATIVES", 45)'
new_toc_line = '("XII. EXTRAITS & DOSSIER DRIVE SÉCURISÉ", 45)'
c = c.replace(old_toc_line, new_toc_line)

with open('mémoire/RDM 3.0/build_rdm_v8_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Drive Link restored and phrasing adapted for digital submission.")
