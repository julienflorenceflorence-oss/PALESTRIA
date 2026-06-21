import codecs

with open('build_rdm_v5_expert.py', 'r', encoding='utf-8') as f:
    c = f.read()

new_page = """
# PAGE 15.5
pages.append({
    "section": "CHAPITRE 5 : AUDIT DATA & LOI ALUR",
    "content": \"\"\"
        <h2>L'Épuration de la Base de Données (Filtre Légal ALUR)</h2>
        
        <p>Afin de maintenir l'exigence intellectuelle qui régit ce rapport, l'analyse de notre actif principal (le fichier prospect) doit être soumise au même cadre analytique rigoureux.</p>

        <div class="analytic-point">Le Point Initial (L'Observation)</div>
        <div class="analytic-content">La possession d'un fichier brut de 126 000 contacts n'est pas un actif commercial exploitable en l'état ; c'est un gisement non qualifié qu'il faut filtrer juridiquement, notamment via le prisme de la Loi ALUR.</div>
        
        <div class="analytic-point">Pourquoi appliquer notre méthodologie ici</div>
        <div class="analytic-content">Parce que prospecter à l'aveugle une base de cette taille expose l'entreprise à un double risque fatal : un gouffre financier (perte de temps) et le danger d'associer la marque Premium de Happy House à des loueurs non conformes. L'analyse Data doit précéder l'action commerciale.</div>
        
        <div class="analytic-point">Les Preuves Chiffrées (Le Tri Data)</div>
        <div class="analytic-content">L'algorithme d'audit a scanné les <span class="analytic-highlight">126 000 lignes prospects</span>. Le filtrage qualitatif a d'abord isolé la pyramide Premium : <span class="analytic-highlight">55% de 3★, 35% de 4★, et 10% de 5★/Palaces</span>. Surtout, le croisement des données permet d'écarter la masse exponentielle des loueurs amateurs.</div>
        
        <div class="analytic-point">L'Analyse de Contexte (La Loi ALUR)</div>
        <div class="analytic-content">La Loi ALUR a drastiquement resserré l'étau sur la location de courte durée en France (numéro d'enregistrement obligatoire, limite stricte de 120 jours pour les résidences principales, lourdes procédures de changement d'usage dans les zones tendues). Le marché se scinde : les opportunistes immobiliers reculent sous la pression de l'État, tandis que les véritables professionnels du "Charme" restent. Or, un fichier de scraping massif de 126k contacts intègre historiquement des dizaines de milliers de ces "amateurs" en sursis.</div>
        
        <div class="analytic-point">La Maladie (Le Churn Réglementaire)</div>
        <div class="analytic-content">Le risque de "Faux Positifs". Si notre force de vente (le SDR) appelle cette liste de haut en bas sans discernement, il risque d'onboarder des acteurs amateurs qui seront contraints à la fermeture administrative dans les 12 mois par la Loi ALUR (ou le DPE, cf. Chapitre 2). Cela générerait une illusion de croissance comptable, immédiatement suivie d'une explosion mathématique de notre Taux d'Attrition.</div>
        
        <div class="analytic-point">Le Remède (Scoring Légal & Invitation)</div>
        <div class="analytic-content">Le fichier de prospection n'est plus utilisé comme un "annuaire téléphonique", mais comme un moteur de <em>Scoring B2B</em>. Seuls les prospects démontrant une structure juridique pérenne (Conformité ALUR avérée) et un standing validé (3★ à 5★) gagnent le statut de "Lead Qualifié". Ce n'est qu'à l'issue de ce filtre que l'invitation exclusive pour les Afterworks Inbound est générée. La Data devient un bouclier juridique protégeant la Lifetime Value (LTV) du réseau.</div>
    \"\"\"
})
"""

if "CHAPITRE 5 : AUDIT DATA & LOI ALUR" not in c:
    c = c.replace('# PAGE 16\n', new_page + '\n# PAGE 16\n')
    with open('build_rdm_v5_expert.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Page ALUR ajoutée.")
else:
    print("Page ALUR déjà présente.")
