import codecs

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# --- CORRECTION DE L'ESPACEMENT PAGE 4 ---
old_page4_content = """<h2>La Matrice de Décision à 6 Niveaux</h2>
        
        <p>Pour garantir cette robustesse académique et opérationnelle, aucune stratégie ni aucune action corrective n'a été actée sans passer par un crible analytique absolu. Ce crible, qui servira de fil rouge à chaque chapitre, repose sur la boucle suivante :</p>

        <div class="glass-card" style="border-left: 4px solid var(--gold); padding: 15px;">
            <ul style="font-size: 10pt; color: #FFF; line-height: 1.6; margin-top: 5px; margin-bottom: 5px;">
                <li><strong>1. Le Point Initial :</strong> L'observation clinique d'un dysfonctionnement terrain ou d'une anomalie de marché.</li>
                <li><strong>2. L'Enjeu du Choix :</strong> Pourquoi l'entreprise ne peut pas ignorer ce point. Pourquoi l'isoler est vital pour la survie du modèle économique.</li>
                <li><strong>3. La Preuve Chiffrée :</strong> Le croisement obligatoire avec nos bases de données. Tout chiffre avancé est extrait soit de notre gisement de <span class="analytic-highlight">126 000 prospects</span>, soit de notre <span class="analytic-highlight">CRM "Hébergeurs 2"</span>.</li>
                <li><strong>4. Le Contexte Analytique :</strong> La mise en perspective du chiffre avec la réalité du terrain et la réglementation en vigueur (Ex: Loi ALUR).</li>
                <li><strong>5. La Maladie :</strong> L'identification de la cause racine. Ne pas soigner le symptôme, mais identifier la pathologie psychologique ou structurelle de la cible.</li>
                <li><strong>6. Le Remède :</strong> Le plan d'action déployé, justifiant des gains financiers ou d'engagement attendus.</li>
            </ul>
        </div>
        
        <h2>La Doctrine des Alternatives (Matrice d'Arbitrage)</h2>
        <p>Proposer une solution est facile ; démontrer qu'elle est la seule viable est le vrai travail de la stratégie. C'est pourquoi, chaque décision finale a été mise en compétition avec <strong>deux autres solutions alternatives</strong> qui paraissaient pertinentes sur le papier. Je détaillerai systématiquement pourquoi ces alternatives ont été factuellement démontées et écartées au profit de la solution finale.</p>"""

# J'ajoute des classes style inline pour forcer un line-height plus petit sur cette page spécifique.
new_page4_content = """<h2 style="margin-bottom: 5px;">La Matrice de Décision à 6 Niveaux</h2>
        
        <p style="line-height: 1.4; margin-bottom: 10px;">Pour garantir cette robustesse académique et opérationnelle, aucune stratégie ni aucune action corrective n'a été actée sans passer par un crible analytique absolu. Ce crible, qui servira de fil rouge à chaque chapitre, repose sur la boucle suivante :</p>

        <div class="glass-card" style="border-left: 4px solid var(--gold); padding: 10px 15px; margin: 10px 0;">
            <ul style="font-size: 10pt; color: #FFF; line-height: 1.4; margin-top: 0; margin-bottom: 0;">
                <li style="margin-bottom: 4px;"><strong>1. Le Point Initial :</strong> L'observation clinique d'un dysfonctionnement terrain ou d'une anomalie de marché.</li>
                <li style="margin-bottom: 4px;"><strong>2. L'Enjeu du Choix :</strong> Pourquoi l'entreprise ne peut pas ignorer ce point. Pourquoi l'isoler est vital pour la survie du modèle économique.</li>
                <li style="margin-bottom: 4px;"><strong>3. La Preuve Chiffrée :</strong> Le croisement obligatoire avec nos bases de données. Tout chiffre avancé est extrait soit de notre gisement de <span class="analytic-highlight">126 000 prospects</span>, soit de notre <span class="analytic-highlight">CRM "Hébergeurs 2"</span>.</li>
                <li style="margin-bottom: 4px;"><strong>4. Le Contexte Analytique :</strong> La mise en perspective du chiffre avec la réalité du terrain et la réglementation en vigueur (Ex: Loi ALUR).</li>
                <li style="margin-bottom: 4px;"><strong>5. La Maladie :</strong> L'identification de la cause racine. Ne pas soigner le symptôme, mais identifier la pathologie psychologique ou structurelle de la cible.</li>
                <li><strong>6. Le Remède :</strong> Le plan d'action déployé, justifiant des gains financiers ou d'engagement attendus.</li>
            </ul>
        </div>
        
        <h2 style="margin-top: 15px; margin-bottom: 5px;">La Doctrine des Alternatives (Matrice d'Arbitrage)</h2>
        <p style="line-height: 1.4; margin-bottom: 0;">Proposer une solution est facile ; démontrer qu'elle est la seule viable est le vrai travail de la stratégie. C'est pourquoi, chaque décision finale a été mise en compétition avec <strong>deux autres solutions alternatives</strong> qui paraissaient pertinentes sur le papier. Je détaillerai systématiquement pourquoi ces alternatives ont été factuellement démontées et écartées au profit de la solution finale.</p>"""

c = c.replace(old_page4_content, new_page4_content)

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Page 4 line-height and margins adjusted.")
