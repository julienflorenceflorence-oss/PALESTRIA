import csv
import re
import unicodedata

def normalize(s):
    if not isinstance(s, str): return ""
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.lower().replace('-', ' ').replace('_', ' ')
    s = re.sub(r'[^a-z0-9\s]', '', s)
    return " ".join(s.split())

def generate_final_repaired():
    # File paths
    v2_path = 'CSV client HH/CLIENTS_Triage_Enrichi_V2.csv'
    prospect_path = 'prompt générato/prospection_hebergement.csv'
    output_path = 'CLIENTS_Triage_Enrichi_V3_FINAL_REPAIRED.csv'

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

    # 1. First, LOAD EVERYTHING from V2 (The most complete file for emails/phones)
    try:
        with open(v2_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("Nom de l'établissement")
                if name:
                    norm_name = normalize(name)
                    # Ensure we don't have empty rows
                    clean_row = {f: row.get(f, '') for f in target_fieldnames}
                    # Fix empty emails if they were N/D
                    for k in ["Téléphone Extrait", "Email 1 Extrait", "Email 2 Extrait"]:
                        if not clean_row[k]: clean_row[k] = 'N/D'
                    
                    seen_names[norm_name] = clean_row
                    final_data.append(clean_row)
    except Exception as e:
        print(f"Error loading V2: {e}")

    # 2. Add NEW names from Prospect Sheet and update Status
    try:
        with open(prospect_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for s_row in reader:
                if len(s_row) > 4:
                    s_name = s_row[4]
                    norm_s_name = normalize(s_name)
                    
                    # Extract Status from cells
                    statut_found = None
                    for cell in s_row:
                        if any(kw in cell for kw in ['Publié', 'A décider', 'A supprimer', 'NO GO', 'A venir', 'A créer']):
                            statut_found = cell
                            break
                    
                    if norm_s_name in seen_names:
                        # Existing: Just Update Status if found
                        if statut_found:
                            seen_names[norm_s_name]['Statut'] = statut_found
                    else:
                        # New: Create entry
                        new_row = {f: "" for f in target_fieldnames}
                        new_row["Nom de l'établissement"] = s_name
                        new_row['Statut'] = statut_found if statut_found else 'Non contacte'
                        new_row['Photos'] = '0'
                        new_row['SITE WEB HH'] = 'NON'
                        new_row['DROPBOX'] = 'NON'
                        new_row['APPLICATION HH'] = 'NON'
                        new_row['Statut closing'] = 'En cours'
                        new_row['Téléphone Extrait'] = 'N/D'
                        new_row['Email 1 Extrait'] = 'N/D'
                        new_row['Email 2 Extrait'] = 'N/D'
                        
                        seen_names[norm_s_name] = new_row
                        final_data.append(new_row)
    except Exception as e:
        print(f"Error loading Prospect Sheet: {e}")

    # 3. Final Re-index and Formulas
    for idx, row in enumerate(final_data, 1):
        row["N°"] = idx
        row_idx = idx + 1
        row['Priorite'] = f'=IF(OR(E{row_idx}<5, H{row_idx}="NON", I{row_idx}="NON", J{row_idx}="NON"), "HAUTE", "MOYENNE")'
        row['Alerte Complétude'] = f'=IF(AND(H{row_idx}="OUI", I{row_idx}="OUI", J{row_idx}="OUI"), "✅ COMPLET", "⚠️ À OPTIMISER")'

    # 4. Save to final file
    with open(output_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=target_fieldnames)
        writer.writeheader()
        writer.writerows(final_data)
    
    print(f"DONE: {len(final_data)} rows. Check {output_path}")

if __name__ == "__main__":
    generate_final_repaired()
