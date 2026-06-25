import codecs
import re

with open('mémoire/RDM 3.0/build_rdm_v6_ultra.py', 'r', encoding='utf-8') as f:
    c = f.read()

old_arbitrage_block = """<div class="arbitrage-box" style="margin-top: 30px;">
            <div class="arbitrage-title">MATRICE D'ARBITRAGE : GESTION DES 126K LEADS</div>
            <div class="arbitrage-rejected">
                <strong>Solution écartée A : Acheter un fichier "Propre" externe.</strong> Abandonner notre fichier pour acheter une base qualifiée chez un broker de données. <em>Pourquoi c'est inadapté : Coût d'achat prohibitif (dizaines de milliers d'euros) pour des données souvent obsolètes, sans l'avantage de la qualification par étoiles dont nous disposons déjà en interne.</em>
            </div>
            <div class="arbitrage-rejected">
                <strong>Solution écartée B : Qualification manuelle par le SDR.</strong> Demander aux commerciaux d'appeler chaque numéro pour vérifier si c'est un pro ou un amateur. <em>Pourquoi c'est inadapté : Pur gaspillage du temps humain. Le SDR mettrait des années à épuiser la liste, détruisant la rentabilité commerciale de l'équipe.</em>
            </div>
            <div class="arbitrage-accepted">
                <strong>Solution retenue : L'Identification des Profils à Fort Potentiel.</strong> Utiliser la puissance de calcul pour cibler précisément ces particuliers qui subissent la Loi ALUR, afin de leur proposer la professionnalisation Happy House comme bouclier vital et pragmatique pour la durée de vie de leur établissement.
            </div>
        </div>"""

new_arbitrage_block = """<div class="arbitrage-box" style="margin-top: 30px;">
            <div class="arbitrage-title">MATRICE D'ARBITRAGE : LE CHOIX DE LA CIBLE (DATA)</div>
            <div class="arbitrage-rejected">
                <strong>Solution écartée A : Le ciblage exclusif des "Pros" hyper-structurés.</strong> Se concentrer uniquement sur les 30% d'acteurs institutionnels. <em>Pourquoi c'est inadapté : L'océan rouge. Ces acteurs sont déjà sur-armés en outils et engagés avec des centrales d'achats concurrentes. Le cycle de vente est long et la guerre se fait sur les prix, détruisant nos marges.</em>
            </div>
            <div class="arbitrage-rejected">
                <strong>Solution écartée B : Le ciblage "Masse / Micro-amateurs".</strong> Cibler la totalité des 88 200 particuliers sans distinction. <em>Pourquoi c'est inadapté : Cela inclurait des micro-structures (ex: petits studios urbains) qui n'ont ni le volume d'achat nécessaire pour rentabiliser notre centrale Entegra, ni l'ADN "Premium" du réseau.</em>
            </div>
            <div class="arbitrage-accepted">
                <strong>Solution retenue : L'Indépendant à fort potentiel (Gros Gîtes & Domaines).</strong> Utiliser l'algorithme pour filtrer les particuliers exploitant de belles capacités (Gros gîtes) subissant la Loi ALUR. Ils ont les volumes pour rentabiliser nos services, mais manquent cruellement d'outils professionnels. Avec eux, nous ne remplaçons pas un outil concurrent : nous comblons un vide vital pour leur survie.
            </div>
        </div>"""

c = c.replace(old_arbitrage_block, new_arbitrage_block)

with open('mémoire/RDM 3.0/build_rdm_v6_ultra.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Matrice d'arbitrage de la cible mise à jour avec succès.")
