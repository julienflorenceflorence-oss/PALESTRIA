import csv

input_file = 'DATAs/datatourisme-reg-gde.csv'
output_file = 'Gites_5_Etoiles_Grand_Est.csv'

# Critères de filtrage
# Les catégories peuvent varier, on va chercher "SelfCateringAccommodation" ou "Gite"
# Le classement doit contenir "5 étoiles" ou "5 épis"
target_category = "SelfCateringAccommodation"
target_5_stars = ["5 étoiles", "5 épis"]
target_4_stars = ["4 étoiles", "4 épis"]

results_5 = []
results_4 = []

print(f"Filtrage en cours sur {input_file}...")

try:
    with open(input_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            categories = row['Categories_de_POI']
            classement = row['Classements_du_POI']
            
            # Vérification de la catégorie (Gîte)
            is_gite = "SelfCateringAccommodation" in categories or "Gite" in categories
            
            if is_gite:
                # Vérification 5 étoiles
                if any(s in classement for s in target_5_stars):
                    results_5.append(row)
                # Vérification 4 étoiles
                elif any(s in classement for s in target_4_stars):
                    results_4.append(row)
            
            # Si on a déjà assez de 5 étoiles (peu probable vu le fichier)
            if len(results_5) >= 300:
                results = results_5[:300]
                break
        else:
            # On complète avec les 4 étoiles pour atteindre 300
            results = results_5 + results_4
            results = results[:300]

    if results:
        # On garde les mêmes colonnes que l'original
        fieldnames = results[0].keys()
        with open(output_file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"Succès : {len(results)} gîtes trouvés et sauvegardés dans {output_file}.")
    else:
        print("Aucun gîte 5 étoiles trouvé avec ces critères.")

except Exception as e:
    print(f"Erreur lors du traitement : {e}")
