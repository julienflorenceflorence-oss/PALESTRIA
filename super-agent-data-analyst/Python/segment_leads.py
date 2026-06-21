import csv
import re

input_file = 'Leads_Telephoniques_Garantis.csv'
output_file = 'Leads_Segmentes.csv'

# Mots-clés pour identifier les professionnels
pro_keywords = [
    'HOTEL', 'RESIDENCE', 'DOMAINE', 'CHATEAU', 'SARL', 'SAS', 'SCI', 'EURL', 
    'CAMPING', 'MUSEE', 'MAIRIE', 'OFFICE DE TOURISME', 'VILLAGE DE VACANCES',
    'AUBERGE', 'RELAIS', 'ABBAYE', 'CONCIERGERIE', 'PROPRIETE', 'MANOIR'
]

# Mots-clés pour identifier les particuliers
indiv_keywords = [
    'CHEZ', 'M.', 'MME', 'MONSIEUR', 'MADAME', 'M ET MME', 'MLLE'
]

def classify_lead(name, contacts, description):
    name_upper = name.upper()
    contacts_upper = contacts.upper()
    desc_upper = description.upper()
    
    # Priorité aux indices "Professionnels"
    if any(word in name_upper for word in pro_keywords) or \
       any(word in contacts_upper for word in pro_keywords):
        return "PROFESSIONNEL"
    
    # Indices "Particuliers"
    if any(word in name_upper for word in indiv_keywords) or \
       re.search(r'^[A-Z][a-z]+\s[A-Z][a-z]+$', name): # Nom Prénom simple
        return "PARTICULIER"
    
    # Par défaut, si c'est un nom complexe sans mot-clé pro, on vérifie la structure
    # Si le nom est très court et ressemble à une entreprise, pro.
    # Sinon, par défaut on classe en "PARTICULIER" pour les gîtes.
    if len(name.split()) > 4:
        return "PARTICULIER" # Les gîtes de particuliers ont souvent des noms longs/poétiques
    
    return "PROFESSIONNEL" # Structure courte type enseigne

results = []

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ['Type_Client']
    
    for row in reader:
        type_client = classify_lead(
            row['Nom_du_POI'], 
            row['Contacts_du_POI'], 
            row['Description']
        )
        row['Type_Client'] = type_client
        results.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# Bilan rapide
counts = {"PROFESSIONNEL": 0, "PARTICULIER": 0}
for r in results:
    counts[r['Type_Client']] += 1

print(f"Classification terminée. Pros: {counts['PROFESSIONNEL']} | Particuliers: {counts['PARTICULIER']}")
