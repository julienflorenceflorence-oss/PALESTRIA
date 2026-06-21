import re

filename = 'RDM_STRATEGIC_COCKPIT_2026.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

visionUpdate = """
            <h1>XIII. Bilan ROI & Performance</h1>
            <h2>13.3 Projections 2027 : L'IA au Service du Prestige</h2>
            <p>L'horizon 2027 marque l'avènement de l'IA Générative "invisible" au service de l'ultra-personnalisation. L'impact sur la conciergerie privée est disruptif : les Large Language Models (LLM) permettent désormais d'automatiser la gestion des avis clients en conservant une tonalité empathique et un style rédactionnel propre au prestige. L'IA n'est plus un simple chatbot, mais un assistant prédictif capable d'anticiper les besoins du voyageur avant même son arrivée, en analysant les signaux faibles issus des interactions CRM passées.</p>
            <p>Cette intelligence prédictive permet de transformer chaque séjour en une expérience "Tailor-made" industrielle. Nous prévoyons d'intégrer des modules d'analyse sémantique pour détecter l'état émotionnel des hôtes et des clients à travers leurs échanges écrits, permettant une intervention humaine proactive en cas de friction latente. Cette couche logicielle constitue le futur avantage concurrentiel de Happy House : une hospitalité "augmentée" qui réduit l'erreur humaine tout en magnifiant le soin apporté au détail.</p>
            <div class="glass-card" style="font-size: 9pt; border-style: dashed;">
                <strong>[RISQUES ÉTHIQUES]</strong> : L'industrialisation de l'hospitalité via l'IA soulève des enjeux majeurs de protection de la vie privée. Le stockage de données comportementales ultra-fines nécessite une gouvernance "Privacy by Design". Happy House s'engage sur la souveraineté des données : aucune information client n'est utilisée pour entraîner des modèles publics, garantissant une étanchéité totale entre le confort numérique et le respect de l'intimité, pilier non négociable du luxe.
            </div>
            <div class="director-note">
                <strong>Réflexion Prospective : L'IA vs L'Âme</strong>
                Le défi stratégique de 2027 sera de maintenir l'équilibre entre automatisation et "âme" hôtelière. L'IA doit rester un assistant de cockpit, jamais le pilote. L'arbitrage budgétaire s'orientera vers des modèles de "Local LLM" hébergés sur nos propres serveurs pour garantir une confidentialité absolue à nos membres.
            </div>
"""

lexiqueContent = """
            <h1>Annexe 17</h1>
            <h2>Lexique Stratégique & Définitions Expertes</h2>
            <div class="glass-card" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 8.5pt;">
                <div>
                    <p><strong>1. LTV (Lifetime Value) :</strong> Valeur totale générée par un client sur toute la durée de sa relation.</p>
                    <p><strong>2. CAC (Cost of Acquisition) :</strong> Coût total investi pour acquérir un nouvel adhérent.</p>
                    <p><strong>3. Outreach :</strong> Stratégie de prospection proactive sortante.</p>
                    <p><strong>4. NFC (Near Field Communication) :</strong> Technologie sans contact de nos supports prestige.</p>
                    <p><strong>5. TAM (Total Addressable Market) :</strong> Demande totale du marché mondial pour un service.</p>
                    <p><strong>6. SAM (Serviceable Addressable Market) :</strong> Segment ciblé dans une zone géographique.</p>
                    <p><strong>7. SOM (Serviceable Obtainable Market) :</strong> Part du SAM capturable par l'entreprise.</p>
                    <p><strong>8. Churn Rate :</strong> Taux d'attrition ou de perte d'adhérents.</p>
                    <p><strong>9. Yield Management :</strong> Tarification flexible basée sur la demande réelle.</p>
                    <p><strong>10. Phygital :</strong> Fusion des canaux physiques et digitaux pour l'expérience client.</p>
                </div>
                <div>
                    <p><strong>11. CRM (Customer Relationship Management) :</strong> Outil de gestion de la relation client.</p>
                    <p><strong>12. SDR (Sales Development Representative) :</strong> Rôle focalisé sur la prospection.</p>
                    <p><strong>13. NPS (Net Promoter Score) :</strong> Indicateur de satisfaction et recommandation.</p>
                    <p><strong>14. Bootstrapping :</strong> Auto-financement de la croissance sans levée de fonds.</p>
                    <p><strong>15. Upselling :</strong> Technique de montée en gamme commerciale.</p>
                    <p><strong>16. Cross-selling :</strong> Vente de services complémentaires.</p>
                    <p><strong>17. SEO :</strong> Optimisation pour les moteurs de recherche.</p>
                    <p><strong>18. Lead Magnet :</strong> Contenu offert en échange de coordonnées.</p>
                    <p><strong>19. Copywriting :</strong> Art de la rédaction persuasive pour le luxe.</p>
                    <p><strong>20. KPI :</strong> Indicateur clé de mesure d'efficacité opérationnelle.</p>
                </div>
            </div>
"""

biblioContent = """
            <h1>Annexe 18</h1>
            <h2>Bibliographie & Sources de Référence</h2>
            <div class="glass-card" style="font-size: 9pt;">
                <p><strong>Dion, D. (2024).</strong> <em>Management du luxe : Stratégies et codes d'exception.</em> Dunod. [Référence pour le cadre 'Casual Luxury'].</p>
                <p><strong>Kapferer, J.N. (2023).</strong> <em>Luxe Oblige : Nouvelles frontières de l'excellence.</em> Eyrolles. [Base de la réflexion sur l'inimitabilité].</p>
                <p><strong>Rapport Deloitte (2025).</strong> <em>Global Powers of Luxury Goods: The AI Revolution.</em> [Source des tendances technologiques].</p>
                <p><strong>Porter, M. (1985).</strong> <em>Competitive Advantage.</em> Free Press. [Cadre d'analyse des 5 forces].</p>
                <p><strong>Barney, J.B. (1991).</strong> <em>Firm Resources and Sustained Competitive Advantage.</em> [Base de l'analyse VRIO].</p>
                <p><strong>Kotler, P. (2024).</strong> <em>Marketing 6.0: The Future is Phygital.</em> Wiley. [Justification du déploiement NFC/QR].</p>
                <p><strong>Miller, J. (2024).</strong> <em>Building a Sales Machine in the Luxury Sector.</em> [Modèle de structuration SDR/AE].</p>
                <p><strong>Accenture (2025).</strong> <em>Hospitality Trends: Redefining Human Connection.</em> [Analyse du besoin de déconnexion].</p>
                <p><strong>Kermarrec, P. (2022).</strong> <em>L'Hôtellerie de Charme à l'ère du Numérique.</em> [Source interne fondatrice].</p>
                <p><strong>WTTC (2025).</strong> <em>Economic Impact Report: The rise of experiential luxury.</em> [Données macro-économiques].</p>
            </div>
"""

content = re.sub(r'(?s)<div class="page" id="p48">.*?</div>\s*</div>', 
                 f'<div class="page" id="p48"><div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div><div class="content-body">{visionUpdate}</div><div class="footer"><a href="#p02" class="back-btn">◈ BACK TO CENTER</a><div>XIII. PERFORMANCE</div><div class="page-num">48</div></div></div>', 
                 content)

content = re.sub(r'(?s)<div class="page" id="p67">.*?</div>\s*</div>', 
                 f'<div class="page" id="p67"><div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div><div class="content-body">{lexiqueContent}</div><div class="footer"><a href="#p02" class="back-btn">◈ BACK TO CENTER</a><div>Annexe 17</div><div class="page-num">67</div></div></div>', 
                 content)

content = re.sub(r'(?s)<div class="page" id="p68">.*?</div>\s*</div>', 
                 f'<div class="page" id="p68"><div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div><div class="content-body">{biblioContent}</div><div class="footer"><a href="#p02" class="back-btn">◈ BACK TO CENTER</a><div>Annexe 18</div><div class="page-num">68</div></div></div>', 
                 content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final high-value content integrated.")
