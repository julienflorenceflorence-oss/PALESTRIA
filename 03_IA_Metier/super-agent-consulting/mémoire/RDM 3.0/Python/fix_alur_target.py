import codecs

with open('mémoire/RDM 3.0/build_rdm_v6_ultra.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Page 11
old_p11 = """<div class="analytic-content">L'algorithme a scanné les <span class="analytic-highlight">126 000 lignes prospects</span>. L'analyse révèle une répartition stricte : <span class="analytic-highlight">70% de particuliers/amateurs</span> (88 200 lignes) face à 30% de professionnels (37 800 lignes). Au sein de cette cohorte Pro, la pyramide Premium a été isolée : 55% de 3★ (20 790 lieux), 35% de 4★ (13 230), et 10% de 5★/Palaces (3 780).</div>"""
new_p11 = """<div class="analytic-content">L'algorithme a scanné les <span class="analytic-highlight">126 000 lignes prospects</span>. L'analyse révèle une répartition stricte : <span class="analytic-highlight">70% de particuliers indépendants</span> (88 200 lignes) face à 30% de professionnels déjà structurés (37 800 lignes). L'enjeu stratégique n'est pas de cibler les 30% déjà équipés, mais de filtrer parmi ces 70% de particuliers ceux disposant d'un potentiel Premium (3★ à 5★) et d'une capacité viable (moins de 10 chambres).</div>"""
c = c.replace(old_p11, new_p11)

# 2. Page 12 - Contexte
old_p12_contexte = """<div class="analytic-content">Le filtrage par étoiles ne suffit pas, il faut projeter le cadre légal. La Loi ALUR (loi anti-Airbnb) a drastiquement resserré l'étau répressif en France (numéro d'enregistrement obligatoire en mairie, limite stricte de 120 jours de location pour les résidences principales, fiscalité dissuasive, obligation de compensation). Sous la pression de l'État, les opportunistes amateurs vont être décimés, tandis que les professionnels structurés vont rafler la mise. Ce croisement Data permet d'écarter immédiatement la masse exponentielle des 88 200 loueurs amateurs.</div>"""
new_p12_contexte = """<div class="analytic-content">Le filtrage par standing ne suffit pas, il faut y greffer l'urgence légale. La Loi ALUR a drastiquement resserré l'étau répressif en France (numéro d'enregistrement obligatoire, limite stricte de 120 jours, fiscalité dissuasive). Sous la pression de l'État, les particuliers indépendants sont menacés de fermeture. Contrairement à l'intuition, ces 88 200 particuliers ne sont pas un "déchet" à écarter : c'est notre cœur de cible. Ils ont un besoin vital et urgent de structuration pour survivre.</div>"""
c = c.replace(old_p12_contexte, new_p12_contexte)

# 3. Page 12 - Maladie
old_p12_maladie = """<div class="analytic-content">Si notre force de vente s'appuie sur le fichier complet pour signer des clients "à tout prix", elle risque d'onboarder des acteurs amateurs qui seront immanquablement fermés administrativement dans les 12 mois par la Loi ALUR (ou interdits de location par le DPE). Cela créerait une illusion de croissance, suivie d'une explosion de notre Churn due à la faillite de nos propres clients.</div>"""
new_p12_maladie = """<div class="analytic-content">Le "Mur des Charges" et la disparition de l'indépendant. Laissés à eux-mêmes dans ce flou, ces particuliers subiront de plein fouet l'inflation des coûts (énergie, conciergerie) et les sanctions de la Loi ALUR. La maladie n'est pas leur statut de particulier, mais leur absence d'outils professionnels pour rentabiliser leur bien (pas de centrale d'achats, pas de stratégie de réservation directe).</div>"""
c = c.replace(old_p12_maladie, new_p12_maladie)

# 4. Page 12 - Remède
old_p12_remede = """<div class="analytic-content">Le fichier de 126k contacts devient un moteur de <em>Scoring B2B</em>. Ce croisement des données permet d'écarter immédiatement les 88 200 amateurs. Seuls les prospects démontrant une conformité ALUR avérée, une capacité viable (80% des cibles ont moins de 10 chambres) et un standing (3★ à 5★) gagnent le statut de "Lead Qualifié". La Data agit comme un bouclier juridique protégeant la survie du réseau.</div>"""
new_p12_remede = """<div class="analytic-content">Le fichier de 126k contacts devient un outil de <em>Ciblage d'Urgence</em>. L'approche commerciale consiste à proposer à ces particuliers la <strong>professionnalisation</strong> de leur lieu comme unique solution de survie : "Grâce à notre centrale Entegra, vos charges baissent, compensant la perte de jours de location imposée par la loi ALUR". La Data sert à repérer ceux qui ont le plus besoin de ce bouclier.</div>"""
c = c.replace(old_p12_remede, new_p12_remede)

# 5. Page 12 - Arbitrage
old_p12_arbitrage = """<strong>Solution retenue : L'Épuration Algorithmique (Loi ALUR).</strong> Utiliser la puissance de calcul (scripts) pour croiser la base avec les registres d'état et supprimer d'un clic les 70% de déchets, livrant à l'équipe de vente une liste d'élite garantie "anti-churn légal"."""
new_p12_arbitrage = """<strong>Solution retenue : L'Identification des Profils à Fort Potentiel.</strong> Utiliser la puissance de calcul pour cibler précisément ces particuliers qui subissent la Loi ALUR, afin de leur proposer la professionnalisation Happy House comme bouclier vital et pragmatique pour la durée de vie de leur établissement."""
c = c.replace(old_p12_arbitrage, new_p12_arbitrage)

# 6. Page 13 - Intro Chapitre 5
old_p13_intro = """<p>Maintenant que la cible d'élite est isolée (les 30% de professionnels Premium conformes à la loi ALUR), la question centrale émerge : comment les acquérir de manière rentable ? L'audit du "Cold Calling" historique (prospection téléphonique à froid) révèle un désastre industriel.</p>"""
new_p13_intro = """<p>Maintenant que la cible prioritaire est identifiée (les particuliers disposant d'un potentiel Premium et nécessitant une professionnalisation d'urgence face à la loi ALUR), la question centrale émerge : comment les acquérir de manière rentable ? L'audit du "Cold Calling" historique révèle un désastre industriel.</p>"""
c = c.replace(old_p13_intro, new_p13_intro)

# 7. Page 24 - Conformité IA
c = c.replace("l'épuration légale des 126k prospects", "le ciblage analytique des 126k prospects")

# 8. Page 25 - Annexe 1 PESTEL
old_pestel = """<em style="color: var(--gold);">Impact Stratégique : L'État détruit la couche basse du marché. Cela justifie absolument notre filtrage algorithmique de la base de 126k prospects pour n'isoler que les 30% de professionnels viables, et nous protéger financièrement du Churn Réglementaire.</em>"""
new_pestel = """<em style="color: var(--gold);">Impact Stratégique : L'État menace les indépendants. Cela justifie notre stratégie de ciblage : approcher cette manne de particuliers (70% de notre base) pour leur proposer la professionnalisation comme unique solution pragmatique de survie face à la loi ALUR.</em>"""
c = c.replace(old_pestel, new_pestel)

# 9. Page 26 - Annexe 2 SWOT
old_swot_data = """Base de données d'acquisition propriétaire gigantesque de 126 000 contacts, purifiée analytiquement à 30% de professionnels via le filtre de conformité Loi ALUR."""
new_swot_data = """Base de données propriétaire de 126 000 contacts, offrant un gisement inépuisable de propriétaires particuliers nécessitant une professionnalisation face aux contraintes légales (ALUR/DPE)."""
c = c.replace(old_swot_data, new_swot_data)

old_swot_opp = """<span style="color: #2ECC71; font-weight: bold;">La Purge Légale :</span> L'élimination mécanique des loueurs amateurs (Spéculateurs Airbnb) via la loi ALUR et le DPE libère "de l'air" (des parts de marché) pour les véritables professionnels de l'hospitalité."""
new_swot_opp = """<span style="color: #2ECC71; font-weight: bold;">L'Urgence de la Professionnalisation :</span> L'étau de la loi ALUR et du DPE oblige les loueurs particuliers (70% de notre base) à se structurer professionnellement sous peine de fermeture, créant un immense marché captif pour nos solutions pragmatiques."""
c = c.replace(old_swot_opp, new_swot_opp)

with open('mémoire/RDM 3.0/build_rdm_v6_ultra.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Modification stratégique Loi ALUR & Particuliers appliquée avec succès.")
