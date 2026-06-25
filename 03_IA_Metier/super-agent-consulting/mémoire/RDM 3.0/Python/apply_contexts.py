import codecs

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# --- CORRECTION ZONE A : Ratio 60/40 et la vraie tension ---
old_chap1 = """<p>Logiquement, une équipe restreinte de 4 personnes ne peut physiquement pas absorber les appels de réassurance quotidiens de 170 membres. Structurer l'automatisation de l'acquisition et de la performance financière devient alors une nécessité vitale pour éviter l'épuisement des équipes et l'effondrement du service client historique.</p>"""

new_chap1 = """<p>Logiquement, une équipe restreinte de 4 personnes peine physiquement à absorber la gestion de sa base installée de 170 membres. Si <strong>60% de ce parc historique est composé de professionnels</strong> (déjà structurés), les <strong>40% restants (les particuliers)</strong> réclament aujourd'hui un accompagnement humain intensif face à cette panique légale. Structurer l'automatisation de l'acquisition (pour aller capter et rassurer cette cible en détresse sur le marché) et de la performance financière devient alors une nécessité vitale pour éviter l'épuisement interne et l'effondrement du service client.</p>"""
c = c.replace(old_chap1, new_chap1)


# --- CORRECTION ZONE B : Contexte sur l'oubli des économies (Chapitre 3) ---
old_chap3 = """<div class="analytic-content">La volatilité de la mémoire comptable. L'hébergeur Premium paie sa cotisation annuelle à Happy House, mais oublie au quotidien qu'il bénéficie en coulisse de tarifs préférentiels vitaux sur ses commandes d'énergie ou de blanchisserie. Au moment de renouveler son abonnement à la date anniversaire, son cerveau ne perçoit qu'une charge financière sèche, totalement déconnectée de ses économies globales.</div>"""

new_chap3 = """<div class="analytic-content">L'asymétrie de l'information. La mécanique même de notre avantage concurrentiel crée un angle mort : les 15% à 25% d'économies générées par Entegra sont appliquées directement à la source, sur les factures du grossiste alimentaire ou du fournisseur d'énergie. Le client ne voit jamais de chèque estampillé "Happy House". En revanche, à la date anniversaire, il reçoit une facture sèche de 360€ pour sa cotisation réseau. Isolée de son contexte, cette facture crée une dissonance cognitive : l'hébergeur, le nez dans le guidon de son exploitation quotidienne, ne fait plus le calcul croisé. Ne percevant psychologiquement qu'une dépense, il s'emmure dans le silence.</div>"""
c = c.replace(old_chap3, new_chap3)


# --- CORRECTION ZONE C : Contexte de l'appel Outbound (Chapitre 5) ---
old_chap5 = """<div class="analytic-content">Ce n'est nullement le talent ou l'engagement du SDR qui est en cause, c'est l'inadéquation totale du canal. L'observation du terrain (soutenue par un mini-sondage de validation post-Data) démontre que la cible est angoissée par le cadre réglementaire répressif (la <strong>Loi ALUR</strong>). Harcelés par des vendeurs de logiciels et terrifiés par le risque de fermeture, ces exploitants exigent de la réassurance physique. Le "Cold Calling", par essence interruptif et agressif, déclenche un rejet pavlovien de protection.</div>"""

new_chap5 = """<div class="analytic-content">Ce n'est nullement le talent ou l'engagement du SDR qui est en cause, c'est l'inadéquation totale du canal. Le rejet pavlovien s'explique par la réalité physique de l'exploitation. Lorsqu'un commercial effectue un "Cold Call" à 14h, il interrompt un indépendant isolé, souvent en train de gérer ses check-ins, de nettoyer ses chambres ou de jongler avec sa comptabilité. Dans ce contexte de surmenage (et d'angoisse face à la Loi ALUR), un appel téléphonique non sollicité promettant "d'optimiser sa rentabilité" est instantanément classé mentalement parmi les dizaines de démarchages de marchands de logiciels qu'il subit chaque semaine. L'appel devient une charge mentale supplémentaire.</div>"""
c = c.replace(old_chap5, new_chap5)

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Zones A, B, and C contexts updated in the Python builder script.")
