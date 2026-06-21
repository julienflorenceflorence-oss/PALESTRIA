import csv
import re
import os

data_dir = 'DATAs'
output_file = 'Leads_Telephoniques_Garantis.csv'
target_count = 300

# Patterns Regex
phone_pattern = r'(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}'

def extract_phone(text):
    phones = re.findall(phone_pattern, text)
    if not phones: return ""
    # Nettoyage et formatage
    p = "".join(filter(str.isdigit, phones[0]))
    if len(p) == 10:
        return " ".join([p[i:i+2] for i in range(0, len(p), 2)])
    return ""

all_leads = []

# Liste des fichiers régionaux
files = [f for f in os.listdir(data_dir) if f.startswith('datatourisme-reg-') and f.endswith('.csv')]

print("Recherche de leads avec téléphone...")

for file in files:
    if len(all_leads) >= target_count:
        break
        
    file_path = os.path.join(data_dir, file)
    print(f"Analyse de {file}...")
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                categories = row.get('Categories_de_POI', '')
                classement = row.get('Classements_du_POI', '')
                contacts = row.get('Contacts_du_POI', '')
                description = row.get('Description', '')
                
                # On cible les hébergements étoilés (3, 4, 5)
                is_accommodation = "Accommodation" in categories
                is_rated = any(s in classement for s in ["3 étoiles", "4 étoiles", "5 étoiles", "3 épis", "4 épis", "5 épis"])
                
                if is_accommodation and is_rated:
                    phone = extract_phone(contacts + " " + description)
                    if phone:
                        row['Telephone_Final'] = phone
                        all_leads.append(row)
                        if len(all_leads) >= target_count:
                            break
    except Exception as e:
        print(f"Erreur sur {file}: {e}")

if all_leads:
    fieldnames = list(all_leads[0].keys())
    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_leads)
    print(f"Succès : {len(all_leads)} leads avec téléphone extraits dans {output_file}.")
else:
    print("Aucun lead trouvé avec téléphone.")
