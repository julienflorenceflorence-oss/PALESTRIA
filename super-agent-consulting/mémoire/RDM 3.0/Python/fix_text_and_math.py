import codecs

with open('mémoire/RDM 3.0/build_rdm_v5_expert.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remplacer la couleur du texte analytique (gris) par le blanc pur des titres (#FFFFFF)
old_css = ".analytic-content { padding-left: 15px; border-left: 2px solid rgba(221, 168, 62, 0.3); margin-bottom: 20px; color: var(--text-muted); }"
new_css = ".analytic-content { padding-left: 15px; border-left: 2px solid rgba(221, 168, 62, 0.3); margin-bottom: 20px; color: #FFFFFF; }"
c = c.replace(old_css, new_css)

# 2. Corriger "300 appels/jour" par "300 appels/semaine"
c = c.replace("300 appels/jour", "300 appels/semaine")

# 3. Mettre à jour l'annexe 4 (Le calcul du volume d'appels mensuel)
old_annex_math = "300 appels quotidiens * 20 jours ouvrés = <strong>~6 000 appels / mois</strong>"
new_annex_math = "300 appels par semaine * 4 semaines = <strong>~1 200 appels / mois</strong>"
c = c.replace(old_annex_math, new_annex_math)

# Mettre à jour une occurrence restante potentielle
c = c.replace("300 appels quotidiens", "300 appels par semaine")

with open('mémoire/RDM 3.0/build_rdm_v5_expert.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Modifications appliquées (Couleur blanche et 300 appels/semaine).")
