import csv
import re
import unicodedata

def normalize(s):
    if not isinstance(s, str): return ""
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.lower().replace('-', ' ').replace('_', ' ')
    s = re.sub(r'[^a-z0-9\s]', '', s)
    return " ".join(s.split())

def generate_full_merge():
    master_path = 'CSV client HH/CLIENTS_Triage_Enrichi_V2.csv'
    sheet_path = 'prompt générato/prospection_hebergement.csv'
    output_path = 'CLIENTS_Triage_Enrichi_V3_COMPLET.csv'

    target_fieldnames = [
        "N°", "Nom de l'établissement", "Ville (Contact)", "Pays", "Photos", 
        "Statut", "Priorite", 
        "SITE WEB HH", "DROPBOX", "APPLICATION HH", "Conseillés par Happy house", 
        "Écran connecté", "Lien Backoffice", "Lien Dropbox", "Site_Perso", 
        "Adresse", "CP", "Ville (Propriété)", "Département", "Région", 
        "Date de création", "Statut closing", 
        "Téléphone Extrait", "Email 1 Extrait", "Email 2 Extrait", "Alerte Complétude"
    ]

    final_data = []
    seen_names = {} # norm_name -> row_data

    # 1. Start with EVERYTHING from V2
    try:
        with open(master_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("Nom de l'établissement")
                if name:
                    norm_name = normalize(name)
                    # Clean the row to match target fieldnames
                    clean_row = {f: row.get(f, '') for f in target_fieldnames}
                    seen_names[norm_name] = clean_row
                    final_data.append(clean_row)
    except Exception as e:
        print(f"Error loading master: {e}")

    # 2. Add NEW names from the Sheet
    try:
        with open(sheet_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for s_row in reader:
                if len(s_row) > 4:
                    s_name = s_row[4]
                    norm_s_name = normalize(s_name)
                    
                    if norm_s_name not in seen_names:
                        # This is a new client!
                        new_row = {f: "" for f in target_fieldnames}
                        new_row["Nom de l'établissement"] = s_name
                        new_row['Photos'] = '0'
                        new_row['SITE WEB HH'] = 'NON'
                        new_row['DROPBOX'] = 'NON'
                        new_row['APPLICATION HH'] = 'NON'
                        new_row['Statut closing'] = 'En cours'
                        new_row['Téléphone Extrait'] = 'N/D'
                        new_row['Email 1 Extrait'] = 'N/D'
                        new_row['Email 2 Extrait'] = 'N/D'
                        
                        # Find Status in the row
                        statut_found = 'Non contacte'
                        for cell in s_row:
                            if any(kw in cell for kw in ['Publié', 'A décider', 'A supprimer', 'NO GO']):
                                statut_found = cell
                                break
                        new_row['Statut'] = statut_found
                        
                        seen_names[norm_s_name] = new_row
                        final_data.append(new_row)
                    else:
                        # Update status of existing client if found in sheet
                        existing_row = seen_names[norm_s_name]
                        for cell in s_row:
                            if any(kw in cell for kw in ['Publié', 'A décider', 'A supprimer', 'NO GO']):
                                existing_row['Statut'] = cell
                                break
    except Exception as e:
        print(f"Error loading sheet: {e}")

    # 3. Finalize: Re-index N° and apply Formulas
    for idx, row in enumerate(final_data, 1):
        row["N°"] = idx
        row_idx = idx + 1
        row['Priorite'] = f'=IF(OR(E{row_idx}<5, H{row_idx}="NON", I{row_idx}="NON", J{row_idx}="NON"), "HAUTE", "MOYENNE")'
        row['Alerte Complétude'] = f'=IF(AND(H{row_idx}="OUI", I{row_idx}="OUI", J{row_idx}="OUI"), "✅ COMPLET", "⚠️ À OPTIMISER")'

    # 4. Save
    with open(output_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=target_fieldnames)
        writer.writeheader()
        writer.writerows(final_data)
    
    print(f"Total rows in V3 COMPLET: {len(final_data)}")

if __name__ == "__main__":
    generate_full_merge()
