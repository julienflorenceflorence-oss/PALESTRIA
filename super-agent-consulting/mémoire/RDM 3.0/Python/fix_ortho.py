import codecs

with open('mémoire/RDM 3.0/build_rdm_v10_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Contraction "à le" -> "au"
c = c.replace("confronté à le cadre réglementaire", "confronté au cadre réglementaire")

# 2. Élisions incorrectes "de l'sollicitation" -> "de la sollicitation"
c = c.replace("de l'sollicitation intrusive à l'sollicitation intrusive", "de la sollicitation intrusive à la sollicitation intrusive")

# 3. Accord du sujet "qui est" -> "qui sont"
c = c.replace("SDR qui est en cause", "SDR qui sont en cause")

# 4. Orthographe de "labelisés" -> "labellisés"
c = c.replace("labelisés", "labellisés")

# 5. Oubli de neutralisation "panique légale" -> "pression légale"
c = c.replace("panique légale", "pression légale")

with open('mémoire/RDM 3.0/build_rdm_v10_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Corrections orthographiques appliquées avec succès.")
