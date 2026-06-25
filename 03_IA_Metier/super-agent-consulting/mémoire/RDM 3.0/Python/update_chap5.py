import codecs

with open('mémoire/RDM 3.0/build_rdm.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Enriching Chapter 5
old_chap5_intro = """        <h1>Chapitre 5 — Choix d'acquisition et pivot stratégique</h1>
        <p>Face à l'inefficience avérée de la prospection téléphonique de masse (détaillée au chapitre précédent), une révision de la stratégie d'acquisition s'imposait. Ce chapitre expose la tentative de rationalisation par l'automatisation, les arbitrages de gouvernance rencontrés, et la réorientation vers un modèle événementiel Inbound.</p>

        <h2>L'hypothèse d'optimisation : l'automatisation de la donnée</h2>
        <p>Face au CAC insoutenable (1 823 €), l'hypothèse de travail initiale consistait à rationaliser l'effort de prospection en s'appuyant sur un flux d'automatisation. L'objectif du prototype était de pré-qualifier la base de 126 000 contacts par l'enrichissement de données (vérification d'activité via API SIRET) et de séquences d'emailing informatives. Le modèle prévoyait que la force de vente n'intervienne qu'auprès de prospects ayant manifesté un signal d'intérêt digital, réduisant la friction du Cold Calling.</p>"""

new_chap5_intro = """        <h1>Chapitre 5 — Choix d'acquisition et pivot stratégique</h1>
        <p>Face à l'inefficience avérée de la prospection téléphonique de masse (CAC de 1 823 €), une révision de la stratégie d'acquisition s'imposait. Ce chapitre expose comment l'analyse des pressions du marché a conduit à redéfinir la stratégie vers un modèle événementiel Inbound, en abandonnant les hypothèses initiales d'automatisation de masse.</p>

        <h2>L'étouffement du marché : la justification du pivot</h2>
        <p>L'écoute terrain (Chapitre 4) avait mis en évidence un rejet massif des sollicitations numériques ("fatigue"). Pour objectiver ce phénomène et écarter toute solution d'acquisition basée sur le volume (Cold Emailing), il convenait d'auditer la pression commerciale réelle pesant sur les exploitants. L'analyse des données d'évolution des intermédiaires sur les dix dernières années confirme un harcèlement institutionnel :</p>
        
        <ul>
            <li><strong>La pression des OTAs :</strong> La part de marché des agences en ligne en Europe est passée de 19,7% en 2013 à 29,6% en 2023. Sur ce segment, Booking Holdings maintient une hégémonie écrasante avec 71% des parts de marché. L'hébergeur est donc quotidiennement sollicité par de nouveaux intermédiaires technologiques promettant de désintermédier Booking.</li>
            <li><strong>L'inflation des Labels et Certifications :</strong> La refonte légale du secteur engendre une multiplication des sollicitations pour de nouveaux labels (ex: transition du label historique "Qualité Tourisme", qui disparaît en 2026, vers "Destination d'Excellence"). L'engouement écologique a également saturé l'espace de communication : le label "Clef Verte" a vu le nombre de ses établissements exploser de 855 en 2022 à 2 428 en 2025 (+184% en 3 ans).</li>
        </ul>
        
        <p>Le marché est donc saturé de propositions pour intégrer de nouvelles plateformes ou adhérer à de nouveaux labels complexes. Toute approche d'acquisition Outbound supplémentaire (appels ou emails à froid de masse) est perçue par l'hôte comme une charge mentale additionnelle, vouée à un échec statistique, indépendamment de la qualité du produit Happy House.</p>

        <h2>L'arbitrage de gouvernance : Le refus de l'automatisation</h2>
        <p>Malgré ce contexte de saturation, une première hypothèse d'acquisition automatisée (pré-qualification des 126 000 contacts via l'outil n8n et séquences d'emailing) avait été proposée pour abaisser le CAC. Bien que ce scénario présentât une rationalisation mathématique du temps, son déploiement a été logiquement invalidé par la direction. La gouvernance a estimé que l'utilisation de campagnes d'emailing automatisées présentait un risque majeur de détérioration du positionnement "Premium", renforçant l'assimilation du réseau au bruit ambiant et au "harcèlement" décrit ci-dessus.</p>"""

c = c.replace(old_chap5_intro, new_chap5_intro)

# Remove the duplicated governance section since I integrated it above
old_chap5_gov = """        <h2>L'arbitrage de gouvernance : Le refus de l'Outbound</h2>
        <p>Bien que ce scénario d'automatisation présentât une rationalisation mathématique du temps de prospection, son déploiement a été invalidé par la direction. La gouvernance a estimé que l'utilisation de campagnes d'emailing automatisées présentait un risque majeur pour le positionnement de la marque (assimilation au démarchage de masse). Ce refus s'alignait d'ailleurs de manière empirique avec les constats de "fatigue numérique" relevés lors de notre étude terrain.</p>
    """
c = c.replace(old_chap5_gov, "")


with open('mémoire/RDM 3.0/build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Chapitre 5 mis à jour avec les chiffres macro.")
