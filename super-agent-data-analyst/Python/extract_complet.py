import csv
import re

input_file = 'DATAs/datatourisme-reg-gde.csv'
output_file = 'Gites_Prestige_Grand_Est_Complet.csv'

# Patterns Regex
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}'

def extract_contacts(text):
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    phones = ["".join(filter(str.isdigit, p)) for p in phones]
    phones = [" ".join([p[i:i+2] for i in range(0, len(p), 2)]) for p in phones if len(p) == 10]
    return list(set(emails)), list(set(phones))

results_5 = []
results_4 = []

print(f"Extraction massive depuis {input_file}...")

try:
    with open(input_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            categories = row['Categories_de_POI']
            classement = row['Classements_du_POI']
            
            is_gite = "SelfCateringAccommodation" in categories or "Gite" in categories
            
            if is_gite:
                search_text = f"{row['Contacts_du_POI']} {row['Description']}"
                emails, phones = extract_contacts(search_text)
                row['Emails'] = ", ".join(emails)
                row['Telephones'] = ", ".join(phones)
                
                if any(s in classement for s in ["5 étoiles", "5 épis"]):
                    results_5.append(row)
                elif any(s in classement for s in ["4 étoiles", "4 épis"]):
                    results_4.append(row)
                    
            if len(results_5) >= 300:
                results = results_5[:300]
                break
        else:
            results = results_5 + results_4
            results = results[:300]

    if results:
        fieldnames = list(results[0].keys())
        with open(output_file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"Succès : {len(results)} gîtes avec contacts potentiels dans {output_file}.")

except Exception as e:
    print(f"Erreur : {e}")
