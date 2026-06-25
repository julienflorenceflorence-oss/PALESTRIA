import codecs

with open('mémoire/RDM 3.0/build_rdm_v10_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

replacements = {
    # Page 4
    "<li><strong>6. Le Remède :</strong> Le plan d'action déployé, justifiant des gains financiers ou d'engagement attendus.</li>": "<li><strong>6. Le Remède Proposé :</strong> Le plan d'action préconisé, justifiant des gains financiers ou d'engagement attendus.</li>",
    
    # Page 14
    "Le Remède (Scoring Légal & Nurturing)": "La Recommandation (Scoring Légal & Nurturing)",
    "les processus d'automatisation ont orchestré": "les processus d'automatisation (POC) modélisent",
    
    # Page 18
    "Le Remède Opérationnel": "La Préconisation Opérationnelle",
    
    # Page 23
    "Le Concept Déployé (Le Point)": "Le Concept Préconisé (Le POC)",
    "La conception, le développement et le déploiement opérationnel": "La conception, le développement et la proposition de déploiement",
    
    # Page 25
    "Le Remède Opérationnel (Le Customer Success)": "La Préconisation Opérationnelle (Customer Success)",
    
    # Page 26
    "Le Remède Déployé (La Preuve Matérielle)": "La Préconisation (La Preuve Matérielle)",
    "L'impression sur papier de haute qualité de ces données": "La recommandation inclut l'impression sur papier de haute qualité de ces données",
    
    # Page 27
    "Voici le Manuel d'Opérations (SOP) standardisé validé pour maximiser le closing": "Voici le Manuel d'Opérations (SOP) standardisé proposé à la direction pour maximiser le closing",
    
    # Page 29
    "un protocole de sécurité a été acté avec la direction via l'instauration": "un protocole de sécurité strict a été modélisé et soumis à la direction, prévoyant l'instauration",
    "Un correctif opérationnel strict est voté": "Un correctif opérationnel strict doit être voté",
    "l'événement est transformé conceptuellement": "l'événement doit être transformé conceptuellement",
    
    # Page 30
    "nécessite un cadrage budgétaire strict validé par la direction :": "nécessitait un cadrage budgétaire strict, soumis ici à la validation de la direction :",
    
    # Page 31
    "La validation de mon pivot stratégique final (l'acceptation d'abandonner mon propre modèle d'automatisation logicielle parfaite pour concevoir de toutes pièces une stratégie Inbound événementielle, beaucoup plus \"organique\" et humaine) témoigne de l'acquisition d'une compétence suprême, celle visée par l'exigence de Rocket School : <strong>la maturité politique et consultative en entreprise.</strong>": "Le refus final opposé par la gouvernance au déploiement de ces recommandations (veto budgétaire sur l'événementiel et réticence au changement des process historiques) a été l'ultime leçon de cette alternance. L'abandon de mon propre modèle d'automatisation logicielle pour concevoir de toutes pièces une stratégie Inbound \"organique\" – même si elle resta au stade de proposition formelle – témoigne de l'acquisition d'une compétence suprême, celle visée par l'exigence de Rocket School : <strong>la résilience et la maturité politique en entreprise.</strong>",
    
    # Global Version updates
    "RAPPORT_DE_MISSION_V10_SOUTENANCE.html": "RAPPORT_DE_MISSION_V11_SOUTENANCE.html",
    "V10 SOUTENANCE": "V11 SOUTENANCE",
    "ÉDITION V10 SOUTENANCE": "ÉDITION V11 SOUTENANCE",
    "V10": "V11"
}

for old, new in replacements.items():
    c = c.replace(old, new)

with open('mémoire/RDM 3.0/build_rdm_v11_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("V11 builder script created with recommendation-focused tone.")
