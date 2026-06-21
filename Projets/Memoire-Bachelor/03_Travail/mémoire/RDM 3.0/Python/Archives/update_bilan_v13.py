import codecs

with open('mémoire/RDM 3.0/build_rdm_v12_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

old_paragraph = """<p>Mon expertise technique initiale (le Web-Scraping intensif, la structuration et la gestion de bases de 126 000 lignes de données, la maîtrise des API et des agents IA type Gemini) m'a d'abord poussé, par pur réflexe de "Tech", vers une première recommandation "technocentrée" de Cold Emailing de masse. La confrontation de cette hypothèse avec le "véto identitaire" de la direction (le refus de se compromettre avec des méthodes perçues comme agressives) a été le moment le plus formateur de cette alternance.</p>"""

new_paragraph = """<p>Les compétences technologiques et le nouveau paradigme digital développés grâce à l'exigence du cursus Rocket School (Web-Scraping intensif, structuration de bases massives, maîtrise des agents IA) m'ont d'abord poussé, par pur enthousiasme analytique, vers une première recommandation ultra-technocentrée de Cold Emailing de masse. La confrontation de cette hypothèse avec le "véto identitaire" de la direction a été le moment le plus formateur de cette alternance. Ce refus justifié m'a forcé à ajuster ma matrice d'analyse pour concevoir un modèle hybride. Au terme de cette expérience, je peux l'affirmer : <strong>l'humain sans la technologie est sa propre limite de croissance, mais la technologie sans l'humain manque d'efficience. Plus une approche s'appuie sur des solutions Tech, plus la notion de réassurance par le contact humain devient une priorité.</strong></p>"""

c = c.replace(old_paragraph, new_paragraph)

# Version Upgrades
c = c.replace("RAPPORT_DE_MISSION_V12_SOUTENANCE.html", "RAPPORT_DE_MISSION_V13_SOUTENANCE.html")
c = c.replace("V12 SOUTENANCE", "V13 SOUTENANCE")
c = c.replace("ÉDITION V12 SOUTENANCE", "ÉDITION V13 SOUTENANCE")

with open('mémoire/RDM 3.0/build_rdm_v13_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("V13 builder script created with updated hybrid philosophy.")
