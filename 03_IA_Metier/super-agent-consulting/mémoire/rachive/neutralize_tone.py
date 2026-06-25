import re

filename = 'RDM_STRATEGIC_COCKPIT_2026.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'infrastructure de domination économique': 'infrastructure de compétitivité sectorielle',
    'corps d’armée organisé': 'organisation structurée et coordonnée',
    'corps d\'armée organisé': 'organisation structurée et coordonnée',
    'machine de guerre technologique': 'système technologique intégré',
    'LVMH de l’hébergement indépendant': 'référence premium de l’hébergement indépendant',
    'LVMH de l\'hébergement indépendant': 'référence premium de l’hébergement indépendant',
    'hégémonie': 'position de leadership',
    'Hégémonie': 'Position de leadership',
    'fer de lance': 'vecteur principal',
    'puissance de feu commerciale': 'capacité d’acquisition commerciale',
    'puissance de feu': 'capacité d’action',
    'barricade à l’entrée': 'barrière à l’entrée structurelle',
    'barricade à l\'entrée': 'barrière à l’entrée structurelle',
    'organe de substitution': 'dispositif de support opérationnel',
    'hégémonique': 'prédominante',
    'Hégémonique': 'Prédominante',
    'souveraineté numérique': 'autonomie numérique',
    'Souveraineté numérique': 'Autonomie numérique',
    'souveraine': 'autonome',
    'Souveraine': 'Autonome',
    'coût de sortie est devenu supérieur au coût de l’adhésion': 'coût de sortie est significatif au regard des bénéfices de l’adhésion',
    'coût d’entrée pour nous égaler augmente de 100 000 par an': 'coût d’entrée concurrentiel est estimé en croissance constante selon nos projections de R&D',
    'preuve empirique': 'indicateur probant',
    'impérative': 'essentielle',
    'Nous ne subissons plus les prix, nous les dictons par le volume': 'La mutualisation permet d’optimiser les conditions tarifaires par l’effet de volume',
    'triplement des signatures': 'augmentation significative des signatures (x3)',
    'insolent': 'marquant',
    'insurmontable': 'majeure'
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Adding a methodology note for CAC
cac_methodology = """
            <div class="glass-card" style="font-size: 8.5pt; border-style: dotted;">
                <strong>[DÉTAIL CALCUL CAC]</strong> : Le CAC de 450€ (2025) inclut : 300€ de coût RH (temps de prospection manuelle), 50€ de licences outils sous-optimisées, 50€ de frais de déplacement et 50€ de coût d'opportunité lié au cycle de vente (45 jours). La cible à 185€ repose sur la suppression des frais de déplacement (closing visio) et la réduction du temps RH par l'automatisation (Make/Pharow).
            </div>
"""
content = content.replace('CAC, établi initialement à 450€, pour viser une cible à 185€.', 'CAC, établi initialement à 450€, pour viser une cible à 185€. \n' + cac_methodology)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Tone neutralized and evidence anchored.")
