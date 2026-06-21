import csv
import re

input_file = 'Gites_Prestige_Grand_Est_Complet.csv'
output_file = 'Gites_Prestige_Grand_Est_Web.csv'

# Liste d'exclusion pour ne garder que les sites "officiels" ou directs
exclude_list = [
    'airbnb', 'booking', 'tripadvisor', 'abritel', 'facebook', 'instagram', 
    'reservation', 'clevacances', 'gites-de-france', 'papvacances', 'leboncoin',
    'expedia', 'hotels.com', 'logishotels', 'secureholiday', 'elloha'
]

def extract_official_website(contact_text):
    # Regex pour trouver toutes les URLs
    urls = re.findall(r'https?://[^\s|#<>]+', contact_text)
    official_urls = []
    
    for url in urls:
        # Nettoyage de l'URL (enlever le slash final si présent)
        clean_url = url.rstrip('/')
        
        # Vérification si l'URL contient un mot-clé de plateforme à exclure
        if not any(domain in clean_url.lower() for domain in exclude_list):
            official_urls.append(clean_url)
    
    # Retourne la première URL trouvée ou vide
    return official_urls[0] if official_urls else ""

results = []

print(f"Extraction des sites web depuis {input_file}...")

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ['Site_Web_Officiel']
    
    for row in reader:
        # On analyse la colonne Contacts_du_POI
        website = extract_official_website(row['Contacts_du_POI'])
        row['Site_Web_Officiel'] = website
        results.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Succès : Fichier avec sites web sauvegardé dans {output_file}.")
