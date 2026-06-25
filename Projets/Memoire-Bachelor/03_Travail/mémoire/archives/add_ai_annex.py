import re
import os

filename = 'RDM_STRATEGIC_COCKPIT_2026.html'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Add AI Annex at the end
ai_annex = """
    <div class="page" id="p71">
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body">
            <h1>ANNEXE IA : TRANSPARENCE</h1>
            <h2>Déclaration d'Usage (Conformité Guide Méthodologique)</h2>
            <div class="glass-card" style="font-size: 10pt;">
                <strong>1. IA UTILISÉES :</strong> Gemini 1.5 Pro via l'interface CLI, Python pour le traitement de données textuelles.
            </div>
            <p><strong>Parties concernées :</strong> L'IA a été sollicitée pour la reformulation stylistique, la structuration sémantique et la mise en page HD du présent document. Elle a également servi d'outil de synthèse pour condenser les 24 500 mots initiaux vers le format cible de 14 500 mots, tout en préservant l'intégrité des données stratégiques.</p>
            <p><strong>Prompts utilisés :</strong> Les instructions portaient sur l'adoption d'un ton de "Directeur Commercial Senior", la suppression des répétitions narratives et l'intégration systématique de sections de "Recul Critique" et d'"Arbitrages Stratégiques".</p>
            <p><strong>Rôle de l'IA :</strong> L'IA a agi comme un assistant d'édition et un moteur de rendu. Elle n'a pas généré les concepts stratégiques (Double Détente, CAC Elite, Audit des 100 anciens) qui sont le fruit de mon travail de terrain et de mon analyse personnelle au sein de Happy House.</p>
            <p><strong>Apport personnel :</strong> J'ai supervisé chaque itération, corrigé les biais de langage et injecté l'intégralité des preuves chiffrées issues du CRM Maison sur Google Sheets. Je demeure l'unique architecte de la réflexion stratégique présentée.</p>
            
            <div class="director-note">
                <strong>Réflexion Critique sur l'Usage de l'IA</strong>
                L'intégration de l'IA dans la rédaction de ce mémoire est en soi une démonstration de ma problématique : industrialiser une tâche complexe pour gagner en efficience sans perdre en valeur ajoutée humaine. Ce document est la preuve que la technologie, bien pilotée, devient le multiplicateur de force de l'expertise métier.
            </div>
        </div>
        <div class="footer"><a href="#p02" class="back-btn">◈ BACK TO CENTER</a><div>ANNEXE OBLIGATOIRE</div><div class="page-num">71</div></div>
    </div>
"""

# Append before </body>
content = content.replace('</body>', f"{ai_annex}\n</body>")

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("AI Annex added.")
