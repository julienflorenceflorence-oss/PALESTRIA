import csv
import re
import unicodedata

def normalize(s):
    if not isinstance(s, str): return ""
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.lower().replace('-', ' ').replace('_', ' ')
    s = re.sub(r'[^a-z0-9\s]', '', s)
    return " ".join(s.split())

def generate_triage():
    master_path = 'CSV client HH/CLIENTS_Triage_Enrichi_V2.csv'
    sheet_path = 'prompt générato/prospection_hebergement.csv'
    output_path = 'CLIENTS_Triage_Enrichi_V3_Final.csv'

    # 1. Load Master data for enrichment
    master_data = {}
    try:
        with open(master_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("Nom de l'établissement")
                if name:
                    norm_name = normalize(name)
                    master_data[norm_name] = row
    except Exception as e:
        print(f"Error loading master: {e}")

    # 2. Load Sheet data
    sheet_rows = []
    try:
        with open(sheet_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if len(row) > 4:
                    sheet_rows.append(row)
    except Exception as e:
        print(f"Error loading sheet: {e}")

    # Target fieldnames from CLIENTS_Triage_Enrichi_V2.csv
    target_fieldnames = [
        "N°", "Nom de l'établissement", "Ville (Contact)", "Pays", "Photos", 
        "Statut", "Priorite", 
        "SITE WEB HH", "DROPBOX", "APPLICATION HH", "Conseillés par Happy house", 
        "Écran connecté", "Lien Backoffice", "Lien Dropbox", "Site_Perso", 
        "Adresse", "CP", "Ville (Propriété)", "Département", "Région", 
        "Date de création", "Statut closing", 
        "Téléphone Extrait", "Email 1 Extrait", "Email 2 Extrait", "Alerte Complétude"
    ]

    final_rows = []
    for idx, s_row in enumerate(sheet_rows, 1):
        # Mapping from prospection_hebergement.csv
        # Col 5 (index 4) is establishment name
        s_name = s_row[4]
        norm_s_name = normalize(s_name)
        
        # Try to find in master
        # We also check if s_name is contained in master name or vice versa
        match = None
        if norm_s_name in master_data:
            match = master_data[norm_s_name]
        else:
            # Fallback fuzzy match
            for m_norm, m_row in master_data.items():
                if norm_s_name and m_norm and (norm_s_name in m_norm or m_norm in norm_s_name):
                    match = m_row
                    break
        
        new_row = {f: "" for f in target_fieldnames}
        new_row["N°"] = idx
        new_row["Nom de l'établissement"] = s_name
        
        if match:
            # Transfer enriched data
            new_row["Ville (Contact)"] = match.get("Ville (Contact)", "")
            new_row["Pays"] = match.get("Pays", "")
            new_row["Photos"] = match.get("Photos", "0")
            new_row["SITE WEB HH"] = match.get("SITE WEB HH", "NON")
            new_row["DROPBOX"] = match.get("DROPBOX", "NON")
            new_row["APPLICATION HH"] = match.get("APPLICATION HH", "NON")
            new_row["Conseillés par Happy house"] = match.get("Conseillés par Happy house", "")
            new_row["Écran connecté"] = match.get("Écran connecté", "")
            new_row["Lien Backoffice"] = match.get("Lien Backoffice", "")
            new_row["Lien Dropbox"] = match.get("Lien Dropbox", "")
            new_row["Site_Perso"] = match.get("Site_Perso", "")
            new_row["Adresse"] = match.get("Adresse", "")
            new_row["CP"] = match.get("CP", "")
            new_row["Ville (Propriété)"] = match.get("Ville (Propriété)", "")
            new_row["Département"] = match.get("Département", "")
            new_row["Région"] = match.get("Région", "")
            new_row["Date de création"] = match.get("Date de création", "")
            new_row["Téléphone Extrait"] = match.get("Téléphone Extrait", "N/D")
            new_row["Email 1 Extrait"] = match.get("Email 1 Extrait", "N/D")
            new_row["Email 2 Extrait"] = match.get("Email 2 Extrait", "N/D")
        else:
            # Default for new entries
            new_row['Photos'] = '0'
            new_row['SITE WEB HH'] = 'NON'
            new_row['DROPBOX'] = 'NON'
            new_row['APPLICATION HH'] = 'NON'
            new_row['Statut closing'] = 'En cours'
            new_row['Téléphone Extrait'] = 'N/D'
            new_row['Email 1 Extrait'] = 'N/D'
            new_row['Email 2 Extrait'] = 'N/D'
            # Extract department if possible from s_row[8] (Site_Web in header, but seems to be Dept)
            dept_match = re.search(r'Département (\d+)', s_row[8])
            if dept_match:
                new_row['Département'] = dept_match.group(1)
        
        # Override with Sheet info
        # Statut_Prospection is at index 19 (if no comma issues)
        # But wait, the comma issue is real. Let's try to find "Publié" or "A décider" in the row.
        statut_found = 'Non contacte'
        for cell in s_row:
            if 'Publié' in cell or 'A décider' in cell or 'A supprimer' in cell or 'NO GO' in cell:
                statut_found = cell
                break
        new_row['Statut'] = statut_found
        
        # Formulas (as strings for Excel/Google Sheets)
        row_idx = idx + 1
        new_row['Priorite'] = f'=IF(OR(E{row_idx}<5, H{row_idx}="NON", I{row_idx}="NON", J{row_idx}="NON"), "HAUTE", "MOYENNE")'
        new_row['Alerte Complétude'] = f'=IF(AND(H{row_idx}="OUI", I{row_idx}="OUI", J{row_idx}="OUI"), "✅ COMPLET", "⚠️ À OPTIMISER")'

        final_rows.append(new_row)

    with open(output_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=target_fieldnames)
        writer.writeheader()
        writer.writerows(final_rows)
    
    print(f"Generated {len(final_rows)} rows in {output_path}")

if __name__ == "__main__":
    generate_triage()
