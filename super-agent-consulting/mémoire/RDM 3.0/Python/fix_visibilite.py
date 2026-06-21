import codecs

with open('mémoire/RDM 3.0/build_rdm_v7_mastodonte.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the wrong "Visibilité Digitale" definition in Chapter 1
old_visibilite = """<li><strong>3. La Visibilité Digitale :</strong> Création de sites web transactionnels, spécifiquement optimisés pour la réservation directe afin de desserrer l'étau des géants du web.</li>"""

new_visibilite = """<li><strong>3. La Visibilité Digitale :</strong> Publication d'annonces optimisées pour la réservation directe (sans commission) sur le portail propriétaire du réseau (<em>my-happyhouse.com</em>) ainsi que sur le site partenaire haut de gamme <em>Charme et Caractère</em>, afin de desserrer l'étau des OTAs.</li>"""

c = c.replace(old_visibilite, new_visibilite)

with open('mémoire/RDM 3.0/build_rdm_v7_mastodonte.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Visibilité Digitale definition updated.")
