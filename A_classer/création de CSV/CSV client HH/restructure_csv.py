import csv

def restructure():
    input_file = 'CLIENTS_Triage_Enrichi_V2.csv'
    output_file = 'CLIENTS_Triage_Enrichi_V2_restructured.csv'
    
    # Define the exact order of the 14 columns + enrichment
    target_fieldnames = [
        'N°',
        'Nom de l'établissement',
        'Ville',
        'Pays',
        'Photos',
        'Date de création',
        'SITE WEB HH',
        'DROPBOX',
        'APPLICATION HH',
        'Conseillés par Happy house',
        'Écran connecté',
        'Lien Backoffice',
        'Lien Dropbox',
        'Site_Perso',
        'Téléphone Extrait',
        'Email 1 Extrait',
        'Email 2 Extrait'
    ]
    
    rows = []
    with open(input_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            new_row = {}
            for field in target_fieldnames:
                # Copy existing data or initialize new columns with empty string
                new_row[field] = row.get(field, '')
            rows.append(new_row)
            
    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=target_fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    restructure()
    print("Restructuring complete.")
