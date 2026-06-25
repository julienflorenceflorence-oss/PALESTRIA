import csv
import random
import re

input_file = 'Leads_Segmentes.csv'
output_file = 'Prospection_Segmentee_Affinée.csv'

# Mots-clés pour identifier le Grand Est (Codes postaux 08, 10, 51, 52, 54, 55, 57, 67, 68, 88)
grand_est_depts = ['08', '10', '51', '52', '54', '55', '57', '67', '68', '88']

objections_arg = [
    "Surcharge d'activité actuelle, pas le temps de discuter.",
    "C'est la pleine saison, rappelez-nous dans 3 mois.",
    "Déjà trop de demandes à gérer, on verra plus tard."
]

objections_confiance = [
    "Besoin de Social Proof : envoyez-moi des témoignages clients.",
    "Déficit de confiance : je ne vous vois nulle part sur le marché.",
    "Avez-vous des cas concrets dans ma région ?"
]

def simulate_outcome(row):
    type_client = row['Type_Client']
    cp = row['Code_postal_et_commune']
    dept = re.search(r'^(\d{2})', cp).group(1) if re.search(r'^\d{2}', cp) else ""
    is_grand_est = dept in grand_est_depts
    
    rand = random.random()
    
    # 1. 50% de NRP principalement sur les PARTICULIERS
    if type_client == "PARTICULIER":
        if rand < 0.60: # On monte à 60% pour les particuliers pour équilibrer la moyenne globale
            return "NRP", "Pas de réponse (Mobile particulier). Tester un créneau soir/week-end.", "⚪"
    else: # PRO
        if rand < 0.40: # Un peu moins de NRP pour les pros
            return "NRP", "Standard automatique ou pas de réponse.", "⚪"

    # 2. 20% de REFUS CATÉGORIQUES sur les PROFESSIONNELS (Barrage Salarié)
    if type_client == "PROFESSIONNEL":
        # Spécificité Grand Est : Barrage salarié "Fais suivre"
        if is_grand_est and 0.40 <= rand < 0.65:
            return "REFUS CATÉGORIQUE", "Barrage Salarié : 'Le responsable n'est pas là, faites suivre par mail'. Aucune suite.", "🔴"
        elif 0.65 <= rand < 0.75:
            return "REFUS CATÉGORIQUE", "Refus immédiat sans discussion.", "🔴"
    
    # 3. 20% de REFUS ARGUMENTÉS (Freins Social Proof / Confiance)
    if 0.75 <= rand < 0.95:
        return "REFUS ARGUMENTÉ", f"{random.choice(objections_arg)} {random.choice(objections_confiance)}", "🟡"

    # 4. 5% de SUIVI NÉGO
    return "SUIVI NÉGO", "Potentiel détecté. Demande une étude comparative et des références.", "🟢"

results = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ['Statut_Prospection', 'Dernier_Commentaire', 'Niveau_Confiance']
    
    for row in reader:
        statut, commentaire, icone = simulate_outcome(row)
        row['Statut_Prospection'] = statut
        row['Dernier_Commentaire'] = commentaire
        row['Niveau_Confiance'] = icone
        results.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Simulation affinée terminée : {output_file}")
