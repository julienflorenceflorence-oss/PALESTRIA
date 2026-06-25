import re

with open('mémoire/RDM 3.0/build_rdm.py', 'r', encoding='utf-8') as f:
    content = f.read()

# I will find the blocks for Chapter 4 and Chapter 5 and swap them, renaming the chapter numbers.
# We also need to update the TOC.

# Let's just do a big text replacement for the TOC part first:
toc_old = """    ("IV. CHOIX D'ACQUISITION & PIVOT (Chapitre 4)", 16),
    ("V. CONFRONTATION AU TERRAIN (Chapitre 5)", 20),"""

toc_new = """    ("IV. CONFRONTATION AU TERRAIN (Chapitre 4)", 16),
    ("V. CHOIX D'ACQUISITION & PIVOT (Chapitre 5)", 19),"""

content = content.replace(toc_old, toc_new)

# Now swap Chapter 4 and 5 in the body.
# Let's find where they start and end.
# Chapitre 4 starts at "# --- CHAPITRE 4 : LE PIVOT ---"
# Chapitre 5 starts at "# --- CHAPITRE 5 : RECHERCHE TERRAIN ---"
# Chapitre 6 starts at "# --- CHAPITRE 6 : RÉTENTION & DASHBOARD ---"

part_chap4 = content.split("# --- CHAPITRE 4 : LE PIVOT ---")[1].split("# --- CHAPITRE 5 : RECHERCHE TERRAIN ---")[0]
part_chap5 = content.split("# --- CHAPITRE 5 : RECHERCHE TERRAIN ---")[1].split("# --- CHAPITRE 6 : RÉTENTION & DASHBOARD ---")[0]

# Modify the strings inside part_chap4 to say Chapter 5
part_chap4_mod = part_chap4.replace("Chapitre 4 — Choix", "Chapitre 5 — Choix")
part_chap4_mod = part_chap4_mod.replace("chapitre précédent", "chapitre 4") # fixing references
part_chap4_mod = part_chap4_mod.replace("Transition vers le chapitre 5", "Transition vers le chapitre 6")
part_chap4_mod = part_chap4_mod.replace("CHAPITRE 4 : CHOIX D'ACQUISITION", "CHAPITRE 5 : CHOIX D'ACQUISITION")
part_chap4_mod = part_chap4_mod.replace("Le pivot stratégique abordé au Chapitre 4", "Le pivot stratégique abordé au Chapitre 5")

# Modify strings inside part_chap5 to say Chapter 4
part_chap5_mod = part_chap5.replace("Chapitre 5 — Confrontation", "Chapitre 4 — Confrontation")
part_chap5_mod = part_chap5_mod.replace("Transition vers le chapitre 6", "Transition vers le chapitre 5")
part_chap5_mod = part_chap5_mod.replace("CHAPITRE 5 : RECHERCHE TERRAIN", "CHAPITRE 4 : RECHERCHE TERRAIN")
part_chap5_mod = part_chap5_mod.replace("abordé au chapitre précédent", "abordé au chapitre 5")

# Now reassemble
before = content.split("# --- CHAPITRE 4 : LE PIVOT ---")[0]
after = "# --- CHAPITRE 6 : RÉTENTION & DASHBOARD ---" + content.split("# --- CHAPITRE 6 : RÉTENTION & DASHBOARD ---")[1]

# But wait, in Chapter 3 transition it says:
before = before.replace("Transition vers le chapitre 4</strong><br>\n            Le diagnostic interne révèle que la difficulté principale ne réside pas seulement dans l’acquisition, mais aussi dans la capacité de l’entreprise à traduire sa valeur en bénéfices visibles pour ses membres. Dans ce contexte, il devient nécessaire d’évaluer les solutions initialement envisagées, puis d’expliquer pourquoi un ajustement stratégique s’impose face aux contraintes réelles de l’organisation.", "Transition vers le chapitre 4</strong><br>\n            Le diagnostic interne révèle une difficulté de transmission de la valeur. Avant de proposer une nouvelle mécanique d'acquisition pour remplacer les départs, il est impératif d'interroger directement la cible (les hébergeurs) pour comprendre leurs véritables attentes et freins face aux solutions du marché.")

new_content = before + "# --- CHAPITRE 4 : RECHERCHE TERRAIN ---\n" + part_chap5_mod + "# --- CHAPITRE 5 : LE PIVOT ---\n" + part_chap4_mod + after

# Also fix the reference in Chapitre 6
new_content = new_content.replace("la nouvelle stratégie d'acquisition événementielle détaillée au chapitre précédent", "la nouvelle stratégie d'acquisition événementielle détaillée au chapitre 5")
new_content = new_content.replace("intégrant le pivot stratégique (abandon de l'outbound de masse) abordé au Chapitre 4.", "intégrant le pivot stratégique (abandon de l'outbound de masse) abordé au Chapitre 5.")

with open('mémoire/RDM 3.0/build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done")
