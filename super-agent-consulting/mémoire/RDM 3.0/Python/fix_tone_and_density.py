import codecs

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# --- 1. AÉRATION VISUELLE (CSS) ---
old_body_css = """        body {
            margin: 0; padding: 0;
            background-color: #1a1a1a;
            color: var(--text-main);
            font-family: 'Arial', sans-serif;
            font-size: 11pt; line-height: 1.55;
            text-align: justify;
        }"""
new_body_css = """        body {
            margin: 0; padding: 0;
            background-color: #1a1a1a;
            color: var(--text-main);
            font-family: 'Arial', sans-serif;
            font-size: 10.5pt; line-height: 1.65;
            text-align: justify;
        }"""
c = c.replace(old_body_css, new_body_css)

c = c.replace("p { margin-bottom: 12px; }", "p { margin-bottom: 16px; }")

# --- 2. LISSAGE LEXICAL (NEUTRALISATION DU TON) ---
replacements = {
    "desserrer l'étau des OTAs": "réduire la dépendance aux OTAs",
    "l'arsenal répressif": "le cadre réglementaire",
    "la panique": "l'inquiétude",
    "en détresse": "en difficulté",
    "l'effondrement": "la dégradation",
    "violence institutionnelle et technologique inouïe": "complexité institutionnelle et technologique croissante",
    "une extrême hostilité": "une forte réticence",
    "se sent harcelé": "se sent sur-sollicité",
    "l'asphyxie financièrement": "pèse sur sa rentabilité",
    "l'étouffent administrativement": "complexifient sa gestion",
    "Le rejet pavlovien": "Le rejet systématique",
    "agression": "sollicitation intrusive",
    "la survie de la base": "la pérennité de la base",
    "équation de survie": "équation de pérennité",
    "resserré l'étau répressif": "renforcé le cadre normatif",
    "menacés de fermeture": "exposés à des risques d'exploitation",
    "Ciblage d'Urgence": "Ciblage Prioritaire",
    "bouclier de survie": "levier de pérennisation",
    "manquent cruellement": "manquent souvent",
    "terreur administrative": "lourdeur administrative",
    "du couperet": "de la contrainte",
    "mécanique implacable": "mécanique structurelle",
    "pilote d'une main de fer": "pilote rigoureusement",
    "La dictature du Ratio LTV/CAC": "L'exigence du Ratio LTV/CAC",
    "Déploiement implacable": "Mise en application stricte",
    "Purge mécanique": "Réduction structurelle",
    "quasi-monopole dictatorial": "quasi-monopole",
    "harcelé technologiquement": "fortement dépendant technologiquement",
    "missions de survie": "missions critiques",
    "L'étau de la loi ALUR": "Le cadre de la loi ALUR",
    "C'est l'étau autour du cou de notre cible.": "C'est la forte pression concurrentielle que subit notre cible.",
    "Face à cet abattage": "Face à ce volume de traitement",
    "stricte et épuisante": "intensive",
    "réels et implacables": "réels et objectifs",
    "l'étau de Booking": "la dépendance à Booking",
    "contexte d'asphyxie": "contexte de forte contrainte",
    "survie financière absolue": "nécessité financière vitale",
    "un désastre": "un déficit",
    "mortifère": "non-viable"
}

for old, new in replacements.items():
    c = c.replace(old, new)

# Update version numbers
c = c.replace("RAPPORT_DE_MISSION_V9_SOUTENANCE.html", "RAPPORT_DE_MISSION_V10_SOUTENANCE.html")
c = c.replace("V9 SOUTENANCE", "V10 SOUTENANCE")
c = c.replace("ÉDITION V9 SOUTENANCE", "ÉDITION V10 SOUTENANCE")

with open('mémoire/RDM 3.0/build_rdm_v10_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Tone neutralized and CSS adjusted for V10.")
