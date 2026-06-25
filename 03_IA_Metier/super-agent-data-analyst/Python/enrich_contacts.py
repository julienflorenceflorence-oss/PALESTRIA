import csv
import re

input_file = 'Gites_5_Etoiles_Grand_Est.csv'
output_file = 'Gites_Prestige_Contacts.csv'

# Patterns Regex
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}'

def extract_contacts(text):
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    # Nettoyage des téléphones (enlever espaces, points, tirets)
    phones = ["".join(filter(str.isdigit, p)) for p in phones]
    # Formatage propre : 0X XX XX XX XX
    phones = [" ".join([p[i:i+2] for i in range(0, len(p), 2)]) for p in phones if len(p) == 10]
    return list(set(emails)), list(set(phones))

results = []

print(f"Extraction des contacts depuis {input_file}...")

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ['Emails', 'Telephones']
    
    for row in reader:
        # On cherche dans Contacts_du_POI et Description
        search_text = f"{row['Contacts_du_POI']} {row['Description']}"
        emails, phones = extract_contacts(search_text)
        
        row['Emails'] = ", ".join(emails)
        row['Telephones'] = ", ".join(phones)
        results.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Succès : Fichier enrichi sauvegardé dans {output_file}.")
