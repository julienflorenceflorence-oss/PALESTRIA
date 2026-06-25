import codecs
import re

with open('mémoire/RDM 3.0/build_rdm_v8_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update the Chapter 1 Text Context and add buttons
old_chap1_text = """<p>Le secteur de l’hébergement connaît une transformation profonde, marquée par l’évolution des attentes clients vers l'hyper-personnalisation et le renforcement drastique des exigences réglementaires (RSE, DPE, Loi ALUR). Au sein de Happy House, une tension centrale est logiquement apparue entre un mode de fonctionnement historique fondé sur l'artisanat et la proximité relationnelle, et la nécessité vitale de structurer davantage le pilotage de la performance financière et de l'acquisition.</p>"""

new_chap1_text = """<p>Le secteur de l’hébergement indépendant connaît une standardisation professionnelle forcée (dictée par les exigences hôtelières post-Covid et les standards des grandes plateformes OTA). Cette mutation s'accompagne d'une pression réglementaire étouffante. Concrètement, un particulier gérant un gîte familial se retrouve soudainement confronté à l'arsenal répressif de la Loi ALUR et de la Loi Le Meur (interdiction imminente de louer si son DPE est classé G, quotas restrictifs de nuitées, complexité d'enregistrement). Face à la panique de cette cible qui réclame un accompagnement humain intensif, une tension opérationnelle est apparue chez Happy House.</p>
        
        <p>Logiquement, une équipe restreinte de 4 personnes ne peut physiquement pas absorber les appels de réassurance quotidiens de 170 membres. Structurer l'automatisation de l'acquisition et de la performance financière devient alors une nécessité vitale pour éviter l'épuisement des équipes et l'effondrement du service client historique.</p>

        <div style="margin-top: 15px; margin-bottom: 25px; display: flex; gap: 10px;">
            <a href="https://www.ecologie.gouv.fr/politiques-publiques/loi-lacces-logement-urbanisme-renove-loi-alur" target="_blank" class="btn-annexe">TEXTE LÉGISLATIF (LOI ALUR)</a>
            <a href="https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000050612711" target="_blank" class="btn-annexe">CADRE FISCAL (LOI LE MEUR)</a>
        </div>"""

c = c.replace(old_chap1_text, new_chap1_text)

# Also rename the script internally from V8 to V9 for clarity when running
c = c.replace("RAPPORT_DE_MISSION_V8_SOUTENANCE.html", "RAPPORT_DE_MISSION_V9_SOUTENANCE.html")
c = c.replace("V8 SOUTENANCE", "V9 SOUTENANCE")
c = c.replace("ÉDITION V8 SOUTENANCE", "ÉDITION V9 SOUTENANCE")

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Chapter 1 context added with legal buttons. V9 script created.")
