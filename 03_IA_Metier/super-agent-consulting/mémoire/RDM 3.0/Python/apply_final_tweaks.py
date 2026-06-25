import codecs

with open('mémoire/RDM 3.0/build_rdm.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update Chapter 7 Copil
old_copil = """        <ul>
            <li><strong>Seuil d'alerte (No-Go financier) :</strong> Un CPA supérieur à 200 € sur trois événements consécutifs entraîne l'arrêt ou la refonte complète du format Afterwork.</li>
        </ul>"""
new_copil = """        <p>Le traitement des écarts de performance fait l'objet d'un protocole itératif strict :</p>
        <ul>
            <li><strong>Écart initial (1er échec d'événement) :</strong> Si les KPIs (ex: CPA > 200 €) ne sont pas atteints, une analyse causale est déclenchée (diagnostic du ciblage, volume d'inscrits, pertinence du lieu). Des actions correctives sont appliquées pour l'itération suivante.</li>
            <li><strong>Écart persistant (2ème échec) :</strong> Le format subit une réingénierie financière. Plutôt qu'une annulation qui pénaliserait la dynamique locale, le budget logistique (frais de traiteur) est drastiquement réduit et l'événement est transformé en "Atelier de réflexion collective". Cela permet de maintenir l'interaction avec les membres, de démontrer une dynamique d'entraide (facteur de rétention), tout en limitant l'exposition au risque financier.</li>
        </ul>"""
c = c.replace(old_copil, new_copil)

# 2. Integration of Annexes actively
old_pestel = "renforçant leur besoin d'accompagnement réseau <em>(Cf. Annexe 1 : Matrice PESTEL détaillée)</em>.</p>"
new_pestel = "renforçant leur besoin d'accompagnement réseau. La Matrice PESTEL <em>(Cf. Annexe 1)</em> vient d'ailleurs objectiver la manière dont ce risque légal peut être converti en barrière à l'entrée favorable pour notre positionnement premium.</p>"
c = c.replace(old_pestel, new_pestel)

old_swot = "limite la perception de la valeur par l'adhérent <em>(Cf. Annexe 2 : Matrice SWOT complète)</em>.</p>"
new_swot = "limite la perception de la valeur par l'adhérent. Cette asymétrie entre valeur créée et valeur perçue est formellement identifiée comme la faiblesse centrale dans la Matrice SWOT du réseau <em>(Cf. Annexe 2)</em>.</p>"
c = c.replace(old_swot, new_swot)

old_script = "simplification <em>(Cf. Annexe 6 : Document de support au profilage qualitatif)</em>.</p>"
new_script = "simplification. Cette analyse comportementale a d'ailleurs servi de socle à la conception du profilage prospect <em>(détaillé en Annexe 6)</em>.</p>"
c = c.replace(old_script, new_script)

old_younes = "à une méthode de qualification psychologique <em>(Cf. Annexe 7 : Script de Vente Younes - SDR Version)</em>.</p>"
new_younes = "à une méthode de qualification psychologique. L'application concrète de ce pivot conversationnel est documentée dans le Script de Vente du SDR <em>(Cf. Annexe 7)</em>.</p>"
c = c.replace(old_younes, new_younes)

# 3. Tone cooling
c = c.replace("une arme de rétention massive", "un levier de rétention structurant")
c = c.replace("détruit instantanément les objections", "permet de rationaliser le traitement des objections")
c = c.replace("un sans-faute absolu", "une base opérationnelle validée")
c = c.replace("foudroyant", "significatif")

with open('mémoire/RDM 3.0/build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Text and KPIs updated successfully.")
