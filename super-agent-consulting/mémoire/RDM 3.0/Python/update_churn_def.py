import codecs

with open('mémoire/RDM 3.0/build_rdm_v5_expert.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Correction of Churn Definition in Chapter 3
old_churn_def_chap3 = """Sur une cohorte d'audit isolant <span class="analytic-highlight">145 dossiers clients acquis spécifiquement par démarchage à froid</span> (entre 2022 et 2025), nous avons constaté une perte de suivi ou une sortie (tag "NO GO") d'environ <span class="analytic-highlight">80%</span>. (À noter : le cœur du réseau de 170 membres reste stable grâce à l'acquisition entrante organique historique, prouvant que c'est la méthode Outbound qui génère ce churn)."""
new_churn_def_chap3 = """Sur une cohorte d'audit isolant <span class="analytic-highlight">145 dossiers clients acquis</span> (entre 2022 et 2025), nous avons évalué notre taux de churn (attrition globale) à environ <span class="analytic-highlight">80%</span>. Attention, ce chiffre ne représente pas uniquement des sorties volontaires ou des faillites, il s'agit majoritairement d'une <strong>"perte de contact"</strong> : les appels répétés de notre équipe restent sans réponse. L'hébergeur s'emmure dans le silence."""
c = c.replace(old_churn_def_chap3, new_churn_def_chap3)

# 2. Correction of the Maladie in Chapter 3
old_maladie_chap3 = """L'asymétrie de l'information. Nous possédons une arme financière d'une efficacité rare (le partenariat Entegra, capable de générer de 15% à 25% d'économies réelles sur le F&B). Le problème n'est pas le produit. Le problème est que le client ne renouvelle pas car il n'en a pas conscience au quotidien. <em>La valeur réellement créée par l'entreprise n'est pas matérialisée en valeur perçue par le client.</em> Il paie une facture Happy House sans voir la contrepartie comptable en face."""
new_maladie_chap3 = """L'asymétrie de l'information. Nous possédons une arme financière d'une efficacité rare (le partenariat Entegra, capable de générer de 15% à 25% d'économies). Le problème n'est pas le produit, mais la <em>perte de valeur perçue</em> au fil des mois. L'hébergeur Premium, sur-sollicité (cf. Chapitre 2), oublie qu'il fait des économies avec nous. Ne voyant plus l'utilité directe de l'interaction, il cesse de nous répondre. Ce "mur du silence" est la forme la plus insidieuse de l'attrition."""
c = c.replace(old_maladie_chap3, new_maladie_chap3)

# 3. Correction in Annex 5
old_annex5_def = """L'audit du portefeuille a révélé une <strong>perte de suivi de 80% sur la cohorte spécifique des 145 dossiers acquis par démarchage téléphonique (Outbound)</strong>. Ce contraste avec la stabilité du réseau historique (170 membres acquis par bouche-à-oreille) prouve que l'Outbound génère de la mauvaise rétention."""
new_annex5_def = """L'audit du portefeuille historique a révélé un taux critique d'environ <strong>80% sur notre cohorte étudiée de 145 dossiers</strong>. Ce "Churn" intègre les sorties définitives, mais surtout une proportion majeure d'<strong>Hébergeurs Perdus de Vue (Silence Radio)</strong> malgré les relances téléphoniques. Sans matérialisation de sa rentabilité, le client B2B Premium coupe le canal de communication."""
c = c.replace(old_annex5_def, new_annex5_def)


with open('mémoire/RDM 3.0/build_rdm_v5_expert.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Churn definition updated to 'Silence Radio/Lost Contact'.")
