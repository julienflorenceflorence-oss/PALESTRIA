import codecs

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# --- CORRECTION ZONE B : La vraie cause du Churn (La résistance au changement) ---
old_chap3 = """<div class="analytic-content">L'asymétrie de l'information. La mécanique même de notre avantage concurrentiel crée un angle mort : les 15% à 25% d'économies générées par Entegra sont appliquées directement à la source, sur les factures du grossiste alimentaire ou du fournisseur d'énergie. Le client ne voit jamais de chèque estampillé "Happy House". En revanche, à la date anniversaire, il reçoit une facture sèche de 360€ pour sa cotisation réseau. Isolée de son contexte, cette facture crée une dissonance cognitive : l'hébergeur, le nez dans le guidon de son exploitation quotidienne, ne fait plus le calcul croisé. Ne percevant psychologiquement qu'une dépense, il s'emmure dans le silence.</div>"""

new_chap3 = """<div class="analytic-content">L'inertie comportementale et la résistance au changement. Contrairement à l'idée reçue, le client ne se contente pas "d'oublier" ses économies : bien souvent, il ne les réalise même pas. Le diagnostic révèle que l'indépendant, la tête dans l'opérationnel, refuse spontanément de changer ses fournisseurs habituels ou de paramétrer la <em>Guest App</em>. Sans un protocole d'accompagnement humain fort (Onboarding) pour forcer cette bascule des habitudes d'achat vers la centrale Entegra, l'outil n'est pas utilisé. L'absence d'usage entraîne une absence de R.O.I. À la date anniversaire, la cotisation de 360€ apparaît comme une charge sèche et inutile. L'hébergeur s'emmure alors dans le "Silence Radio".</div>"""
c = c.replace(old_chap3, new_chap3)

# --- CORRECTION ZONE B (Suite) : Le remède adapté (L'onboarding forcé via le Dashboard) ---
old_remede3 = """<div class="analytic-content">Création urgente d'un protocole chiffré de "Preuve de Valeur" (Reporting ROI) pour sauver la base. C'est l'action de Rétention.</div>"""

new_remede3 = """<div class="analytic-content">Création urgente d'un "Proof of Concept" (POC) d'accompagnement chiffré : le Dashboard R.O.I. L'objectif n'est pas seulement de prouver la valeur, mais de créer des rendez-vous imposés pour forcer l'usage (le changement d'habitudes) et sauver la base. C'est l'action de Rétention.</div>"""
c = c.replace(old_remede3, new_remede3)

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Chapitre 3 : Cause of churn updated to behavior/resistance.")
