import codecs
import re

# Read V13 content
with open('mémoire/RDM 3.0/build_rdm_v13_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# --- INJECT NEW NUMBERS ---

# 1. Inject 97% stat into Outbound failure analysis (Chapter 5)
old_outbound_context = """Dans ce contexte de surmenage (et d'angoisse face à la Loi ALUR), un appel téléphonique non sollicité promettant "d'optimiser sa rentabilité" est instantanément classé mentalement parmi les dizaines de démarchages de marchands de logiciels qu'il subit chaque semaine."""
new_outbound_context = """Dans ce contexte de surmenage (et d'angoisse face à la Loi ALUR), un appel téléphonique non sollicité promettant "d'optimiser sa rentabilité" est instantanément classé mentalement parmi les dizaines de démarchages qu'il subit chaque semaine, un agacement partagé par 97% des Français."""
c = c.replace(old_outbound_context, new_outbound_context)


# 2. Inject benefits into Ecosystem presentation (Chapter 1)
# Cost-Killing
old_cost_killing = """<li><strong>1. L'Optimisation Financière :</strong> Accès exclusif à la puissance de la centrale d'achats <em>Entegra</em> (générant de 15% à 25% de marge additionnelle sur les lourds postes d'exploitation, l'énergie et la restauration). C'est le cœur de la promesse de rentabilité.</li>"""
new_cost_killing = """<li><strong>1. L'Optimisation Financière :</strong> Accès à la centrale d'achats <em>Entegra</em> pour attaquer les postes opérationnels qui pèsent jusqu'à <strong>45% des charges</strong> de l'hébergeur et viser une augmentation de <strong>10 à 20% de sa marge nette</strong>.</li>"""
c = c.replace(old_cost_killing, new_cost_killing)

# Tech
old_tech_pillar = """<li><strong>2. L'Infrastructure Tech :</strong> Déploiement d'une application dédiée à l'expérience du voyageur (Guest App) et d'un outil CRM centralisant la gestion de l'hébergeur pour professionnaliser son accueil.</li>"""
new_tech_pillar = """<li><strong>2. L'Infrastructure Tech :</strong> Déploiement d'une application (Guest App) et d'un CRM pour libérer <strong>10 à 15 heures par semaine</strong> à l'exploitant en automatisant les tâches de communication client.</li>"""
c = c.replace(old_tech_pillar, new_tech_pillar)

# --- UPDATE VERSIONING ---
c = c.replace("V13 SOUTENANCE", "V14 SOUTENANCE")
c = c.replace("RAPPORT_DE_MISSION_V13_SOUTENANCE.html", "RAPPORT_DE_MISSION_V14_SOUTENANCE.html")
c = c.replace("ÉDITION V13 SOUTENANCE", "ÉDITION V14 SOUTENANCE")


with open('mémoire/RDM 3.0/build_rdm_v14_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("V14 builder script created with new prospecting data.")
