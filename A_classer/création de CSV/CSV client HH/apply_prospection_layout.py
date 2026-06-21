import csv

def create_prospection_file():
    input_file = 'CLIENTS_Triage_Enrichi_V2.csv'
    output_file = 'CLIENTS_Triage_Enrichi_V2.csv' # Overwriting to keep consistent name
    
    # Target structure A to Y (25 columns)
    fieldnames = [
        'N°', 'Nom de l'établissement', 'Ville (Contact)', 'Pays', 'Photos', 
        'Statut', 'Priorite', 
        'SITE WEB HH', 'DROPBOX', 'APPLICATION HH', 'Conseillés par Happy house', 
        'Écran connecté', 'Lien Backoffice', 'Lien Dropbox', 'Site_Perso', 
        'Adresse', 'CP', 'Ville (Propriété)', 'Département', 'Région', 
        'Date de création', 'Statut closing', 
        'Téléphone Extrait', 'Email 1 Extrait', 'Email 2 Extrait'
    ]
    
    rows = []
    try:
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                new_row = {field: '' for field in fieldnames}
                
                # Basic Mapping
                new_row['N°'] = row.get('N°', '')
                new_row['Nom de l'établissement'] = row.get('Nom de l'établissement', '')
                new_row['Ville (Contact)'] = row.get('Ville', '')
                new_row['Pays'] = row.get('Pays', '')
                
                photos_val = row.get('Photos', '0')
                new_row['Photos'] = photos_val
                
                new_row['SITE WEB HH'] = row.get('SITE WEB HH', 'NON')
                new_row['DROPBOX'] = row.get('DROPBOX', 'NON')
                new_row['APPLICATION HH'] = row.get('APPLICATION HH', 'NON')
                new_row['Conseillés par Happy house'] = row.get('Conseillés par Happy house', '')
                new_row['Écran connecté'] = row.get('Écran connecté', '')
                new_row['Lien Backoffice'] = row.get('Lien Backoffice', '')
                new_row['Lien Dropbox'] = row.get('Lien Dropbox', '')
                new_row['Site_Perso'] = row.get('Site_Perso', '')
                new_row['Date de création'] = row.get('Date de création', '')
                new_row['Téléphone Extrait'] = row.get('Téléphone Extrait', 'N/D')
                new_row['Email 1 Extrait'] = row.get('Email 1 Extrait', 'N/D')
                new_row['Email 2 Extrait'] = row.get('Email 2 Extrait', 'N/D')

                # Logic Business ENTJ-A
                # 1. Default Status
                new_row['Statut'] = 'Non contacte'
                new_row['Statut closing'] = 'En cours'
                
                # 2. Automated Priority Logic
                try:
                    p_count = float(photos_val) if photos_val != 'NON' else 0
                except:
                    p_count = 0
                
                if (p_count < 5 or 
                    new_row['SITE WEB HH'] == 'NON' or 
                    new_row['DROPBOX'] == 'NON' or 
                    new_row['APPLICATION HH'] == 'NON'):
                    new_row['Priorite'] = 'HAUTE'
                else:
                    new_row['Priorite'] = 'MOYENNE'
                
                # Duplicate City for Property info block
                new_row['Ville (Propriété)'] = new_row['Ville (Contact)']
                
                rows.append(new_row)
    except Exception as e:
        print(f"Error: {e}")
        return

    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    create_prospection_file()
    print("Prospection structure A-Y applied successfully.")
