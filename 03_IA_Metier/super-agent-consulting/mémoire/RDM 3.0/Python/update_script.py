import codecs

with open('build_rdm.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Make sure chap 7 is dense with KPIs
c = c.replace('L\'objectif fixé est supérieur à 50%.', 'L\'objectif fixé est supérieur à 50%.')
c = c.replace('garantir un suivi objectif <em>(Cf. Annexe 8 : Note de Cadrage)</em>.', 'garantir un suivi objectif <em>(Cf. Annexe 8 : Note de Cadrage Force de Vente)</em>.')

old_durentie = "de l'ordre de 4 120 € sur les postes de coûts opérationnels de l'établissement <em>(Cf. Annexe 10 : Évaluation de rentabilité)</em>.</p>"
new_durentie = "de l'ordre de 4 120 € sur les postes de coûts opérationnels de l'établissement.</p>\n        \n        <p>La décomposition exacte de ces économies générées, ventilée par postes de dépenses (F&B, Blanchisserie, Énergie), est intégralement documentée dans l'Annexe 10 <em>(Cf. Annexe 10 : Simulations Rentabilité Achats)</em>.</p>"

c = c.replace(old_durentie, new_durentie)

with open('build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated successfully")
