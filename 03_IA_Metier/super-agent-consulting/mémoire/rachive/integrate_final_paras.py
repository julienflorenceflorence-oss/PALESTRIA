import re

filename = 'RDM_STRATEGIC_COCKPIT_2026.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

paras = {
    'p03': "La réflexion stratégique impose ici une lecture transversale des enjeux de souveraineté numérique. L'indépendance des hébergeurs de prestige ne peut se limiter à une simple réduction des coûts de commission ; elle doit s'incarner dans une réappropriation totale de la donnée client et de l'identité de marque. En reprenant le contrôle sur le canal de distribution, l'établissement ne sauve pas seulement sa marge, il sécurise son héritage immatériel face à la standardisation algorithmique. Cette démarche requiert une agilité technologique couplée à une excellence opérationnelle sans faille, transformant ainsi la contrainte digitale en un levier d'exclusivité et de différenciation durable sur un marché mondialisé de plus en plus saturé et impersonnel.",
    'p18': "L'analyse de la concurrence révèle une faille structurelle dans le modèle dominant des OTA : l'incapacité à transmettre l'âme d'un domaine d'exception. La stratégie de Happy House repose sur cette exploitation fine du 'génie du lieu', là où les plateformes massifiées échouent par nature. Il est impératif de comprendre que le luxe de demain se définit par l'authenticité et la relation directe, deux piliers que la technologie doit servir sans jamais les occulter. Cette approche stratégique permet de transformer chaque visiteur en un ambassadeur, court-circuitant ainsi les cycles de vente traditionnels pour instaurer un cercle vertueux de fidélisation ultra-personnalisée, indispensable à la pérennité économique des structures indépendantes haut de gamme.",
    'p26': "Le déploiement commercial doit impérativement s'adosser à une rigueur analytique constante. La 'Sales Machine' n'est pas qu'un outil de prospection, c'est un organe vital de détection d'opportunités sous-exploitées dans des segments de niche à haute valeur ajoutée. L'intelligence commerciale réside dans la capacité à corréler les données de flux avec l'expérience émotionnelle vécue par l'hôte. En structurant ainsi la force de vente autour d'une promesse de valeur claire et mesurable, Happy House assure une montée en puissance progressive mais solide de son réseau. Cette croissance maîtrisée est la clé pour maintenir un standard de qualité irréprochable tout en augmentant la force de négociation globale du groupement face aux fournisseurs.",
    'p41': "L'optimisation des processus opérationnels constitue le socle invisible de la promesse client. Une réflexion stratégique sur l'intégration des flux et la centralisation des achats démontre que l'efficacité ne nuit pas à l'exceptionnel ; au contraire, elle le libère des lourdeurs administratives. En automatisant les tâches à faible valeur ajoutée, nous redonnons au personnel le temps précieux nécessaire à l'accueil et au soin du détail. Cette ingénierie de service permet de stabiliser les coûts fixes tout en améliorant significativement le Net Promoter Score. À terme, cette maîtrise opérationnelle devient un actif stratégique majeur, facilitant la scalabilité du modèle sans dilution de la qualité intrinsèque qui définit l'ADN de Happy House.",
    'p50': "En conclusion, la trajectoire de Happy House s'inscrit dans une vision de long terme où l'innovation technologique et l'humain coexistent pour réinventer l'hospitalité de luxe. La réflexion stratégique finale souligne l'importance de rester agile face aux évolutions géopolitiques et environnementales qui redéfinissent déjà les habitudes de voyage. Le succès de cette transformation repose sur notre capacité à maintenir cette tension créative entre tradition patrimoniale et modernité digitale. En bâtissant un écosystème résilient, solidaire et souverain, nous ne nous contentons pas de survivre à la mutation du marché ; nous définissons les nouveaux standards d'une hôtellerie de prestige consciente, rentable et profondément connectée à son territoire."
}

for pid, text in paras.items():
    # Insert at the end of the content-body
    pattern = rf'(?s)(<div class="page" id="{pid}">.*?<div class="content-body">.*?)(</div>)'
    new_text = f'<p style="font-style:italic; opacity:0.8; margin-top:20px;">{text}</p>'
    content = re.sub(pattern, rf'\1{new_text}\2', content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final strategic paragraphs integrated.")
