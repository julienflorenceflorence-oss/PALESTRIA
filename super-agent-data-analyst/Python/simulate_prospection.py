import csv
import random

input_file = 'Gites_Prestige_Grand_Est_Web.csv'
output_file = 'Gites_Prospection_Simulee.csv'

# Statistiques cibles du texte
stats = {
    'NRP': 0.50,
    'REFUS_CAT': 0.20,
    'REFUS_ARG': 0.20,
    'NEGO': 0.05,
    'AUTRE': 0.05
}

objections_arg = [
    "Surcharge d'activité actuelle, pas le temps de discuter.",
    "C'est la pleine saison, rappelez-nous dans 3 mois.",
    "Déjà trop de demandes à gérer seul, je ne veux pas de nouveaux outils.",
    "Planning complet jusqu'à la fin de l'année.",
    "En pleine rénovation, on verra ça plus tard."
]

objections_confiance = [
    "Je ne connais pas votre société, vous avez des clients dans le coin ?",
    "Avez-vous des témoignages d'autres gîtes 5 étoiles ?",
    "Je préfère rester sur des solutions connues, c'est trop risqué pour moi.",
    "Votre site manque de références concrètes, je ne suis pas rassuré.",
    "On m'a déjà fait le coup, j'ai besoin de preuves de résultats."
]

commentaires_nego = [
    "Intéressé par le concept mais demande un cas d'étude précis.",
    "A validé le besoin, mais veut comparer avec la concurrence.",
    "Profil décideur, prêt à avancer si on prouve le ROI.",
    "Demande une démo personnalisée pour sa conciergerie.",
    "En attente d'un geste commercial pour lancer le test."
]

def generate_prospection_data():
    rand = random.random()
    if rand < 0.50:
        return "NRP", "Tentative d'appel - Pas de réponse. À rappeler sur un autre créneau."
    elif rand < 0.60:
        return "REFUS CATÉGORIQUE", "Barrage secrétaire ou refus immédiat. Ne souhaite plus être contacté."
    elif rand < 0.70:
        return "OPPOSITION RGPD", "DEMANDE EXPRESS DE RETRAIT (Art. 17 RGPD). Sortir des listes immédiatement et ne plus recontacter."
    elif rand < 0.90:
        return "REFUS ARGUMENTÉ", random.choice(objections_arg) + " Frein : " + random.choice(objections_confiance)
    elif rand < 0.95:
        return "SUIVI NÉGO", "POTENTIEL ÉLEVÉ. " + random.choice(commentaires_nego)
    else:
        return "À CONTACTER", "Nouveau lead - Priorité haute."

results = []

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ['Statut_Prospection', 'Dernier_Commentaire', 'Niveau_Confiance']
    
    for row in reader:
        statut, commentaire = generate_prospection_data()
        row['Statut_Prospection'] = statut
        row['Dernier_Commentaire'] = commentaire
        
        # Attribution d'un niveau de confiance visuel (couleur CRM)
        if statut == "SUIVI NÉGO": row['Niveau_Confiance'] = "🟢"
        elif statut == "NRP": row['Niveau_Confiance'] = "⚪"
        elif statut == "REFUS ARGUMENTÉ": row['Niveau_Confiance'] = "🟡"
        elif statut == "OPPOSITION RGPD": row['Niveau_Confiance'] = "⬛" # Noir pour "Droit à l'oubli"
        else: row['Niveau_Confiance'] = "🔴"
        
        results.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Simulation terminée : {output_file}")
