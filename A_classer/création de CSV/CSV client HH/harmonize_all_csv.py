import csv
import os

def harmonize_all():
    files = ['CLIENTS _ - Triage Clients.csv', 'CLIENTS_Triage_Clients_Enrichi.csv', 'CLIENTS_Triage_Enrichi_V2.csv']
    
    fieldnames = [
        'N°', 'Nom de l'établissement', 'Ville (Contact)', 'Pays', 'Photos', 
        'Statut', 'Priorite', 
        'SITE WEB HH', 'DROPBOX', 'APPLICATION HH', 'Conseillés par Happy house', 
        'Écran connecté', 'Lien Backoffice', 'Lien Dropbox', 'Site_Perso', 
        'Adresse', 'CP', 'Ville (Propriété)', 'Département', 'Région', 
        'Date de création', 'Statut closing', 
        'Téléphone Extrait', 'Email 1 Extrait', 'Email 2 Extrait'
    ]

    for filename in files:
        if not os.path.exists(filename): continue
        
        rows = []
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                new_row = {field: '' for field in fieldnames}
                # Mapping intelligent
                new_row['N°'] = row.get('N°', '')
                new_row['Nom de l'établissement'] = row.get('Nom de l'établissement', '')
                new_row['Ville (Contact)'] = row.get('Ville', '')
                new_row['Pays'] = row.get('Pays', '')
                new_row['Photos'] = row.get('Photos', '0')
                new_row['SITE WEB HH'] = row.get('SITE WEB HH', 'NON')
                new_row['DROPBOX'] = row.get('DROPBOX', 'NON')
                new_row['APPLICATION HH'] = row.get('APPLICATION HH', 'NON')
                new_row['Statut'] = 'Non contacte'
                new_row['Statut closing'] = 'En cours'
                new_row['Téléphone Extrait'] = row.get('Téléphone Extrait', row.get('Téléphone', 'N/D'))
                new_row['Email 1 Extrait'] = row.get('Email 1 Extrait', row.get('Email 1', 'N/D'))
                
                # Auto-Priority
                try: p = float(new_row['Photos'])
                except: p = 0
                if p < 5 or new_row['SITE WEB HH'] == 'NON': new_row['Priorite'] = 'HAUTE'
                else: new_row['Priorite'] = 'MOYENNE'
                
                rows.append(new_row)
        
        # Overwrite with clean format
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

if __name__ == "__main__":
    harmonize_all()
