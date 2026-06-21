import codecs

with open('mémoire/RDM 3.0/build_rdm.py', 'r', encoding='utf-8') as f:
    c = f.read()

old_outbound = """<h2>Analyse quantitative de l'effort (Outbound)</h2>
        <p>Cette inefficacité est confirmée par l'audit des métriques d'appels. Sur un exercice de 48 semaines, avec un volume de 300 numéros composés par jour, les retours démontrent une friction majeure :</p>"""

new_outbound = """<h2>Analyse quantitative de l'effort (Outbound)</h2>
        <p>Cette inefficacité est confirmée par l'audit des métriques d'appels. Sur un exercice de 11 mois (48 semaines), le SDR a ciblé un volume massif de <strong>5 850 prospects</strong> (à raison d'une moyenne de 300 numéros composés par semaine/jour de session). Cette volumétrie donne une valeur statistique irréfutable aux taux de rejet constatés :</p>"""

c = c.replace(old_outbound, new_outbound)

with open('mémoire/RDM 3.0/build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(c)
print("Data updated.")
