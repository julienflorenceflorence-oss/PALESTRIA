import csv
import re
import unicodedata
import os

def normalize(s):
    if not isinstance(s, str): return ""
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.lower().replace('-', ' ').replace('_', ' ')
    s = re.sub(r'[^a-z0-9\s]', '', s)
    return " ".join(s.split())

def load_source(path):
    data = []
    if not os.path.exists(path): return data
    try:
        with open(path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except:
        try:
            with open(path, mode='r', encoding='latin1') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        except: pass
    return data

def get_best_match(norm_name, knowledge_base):
    for k_norm, k_data in knowledge_base.items():
        if norm_name and k_norm and (norm_name in k_norm or k_norm in norm_name):
            return k_data
    return None

def generate_super_enriched_merge():
    master_path = 'CSV client HH/CLIENTS_Triage_Enrichi_V2.csv'
    sheet_path = 'prompt générato/prospection_hebergement.csv'
    output_path = 'CLIENTS_Triage_Enrichi_V3_SUPER_COMPLET.csv'

    sources_paths = [
        'prompt générato/extraction_donnees_adhesions_complet.csv',
        'prompt générato/extraction_donnees_adhesions_final.csv',
        'prompt générato/extraction_contrats.csv',
        'prompt générato/extraction_donnees_adhesions.csv'
    ]

    # 1. Build Knowledge Base from all sources
    knowledge_base = {} # norm_name -> {phone, email1, email2, ville, pays}
    
    for path in sources_paths:
        rows = load_source(path)
        for row in rows:
            # Try to find Name, Email, Phone in various column names
            cols = {c.lower(): c for c in row.keys() if c is not None}
            n_key = next((cols[k] for k in ['nom_entreprise', "nom de l'établissement", 'nom_etablissement', 'nom', 'entreprise'] if k in cols), None)
            e_key = next((cols[k] for k in ['email_direct', 'email_generique', 'email', 'courriel', 'email 1 extrait'] if k in cols), None)
            t_key = next((cols[k] for k in ['telephone_mobile', 'telephone_standard', 'telephone', 'tel', 'téléphone extrait'] if k in cols), None)
            v_key = next((cols[k] for k in ['ville', 'destination', 'ville (contact)'] if k in cols), None)

            if n_key and row[n_key]:
                name = row[n_key]
                norm_name = normalize(name)
                if norm_name not in knowledge_base:
                    knowledge_base[norm_name] = {'phones': set(), 'emails': set(), 'ville': '', 'pays': ''}
                
                if e_key and row[e_key] and "@" in row[e_key] and "my-happy.house" not in row[e_key]:
                    knowledge_base[norm_name]['emails'].add(row[e_key].strip().lower())
                if t_key and row[t_key] and row[t_key] != 'N/D':
                    knowledge_base[norm_name]['phones'].add(row[t_key].strip())
                if v_key and row[v_key] and not knowledge_base[norm_name]['ville']:
                    knowledge_base[norm_name]['ville'] = row[v_key]

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
    seen_names = {}

    # 2. Load Master V2 (Base)
    v2_rows = load_source(master_path)
    for row in v2_rows:
        name = row.get("Nom de l'établissement")
        if name:
            norm_name = normalize(name)
            clean_row = {f: row.get(f, '') for f in target_fieldnames}
            seen_names[norm_name] = clean_row
            final_data.append(clean_row)

    # 3. Add from Sheet & Enrich
    sheet_raw = []
    try:
        with open(sheet_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            sheet_raw = list(reader)
    except: pass

    for s_row in sheet_raw:
        if len(s_row) > 4:
            s_name = s_row[4]
            norm_s_name = normalize(s_name)
            
            # Find status
            statut_found = 'Non contacte'
            for cell in s_row:
                if any(kw in cell for kw in ['Publié', 'A décider', 'A supprimer', 'NO GO']):
                    statut_found = cell
                    break

            if norm_s_name not in seen_names:
                # NEW ENTRY -> Enrich from Knowledge Base
                new_row = {f: "" for f in target_fieldnames}
                new_row["Nom de l'établissement"] = s_name
                new_row['Statut'] = statut_found
                
                # Default tech data
                new_row['Photos'] = '0'
                new_row['SITE WEB HH'] = 'NON'
                new_row['DROPBOX'] = 'NON'
                new_row['APPLICATION HH'] = 'NON'
                new_row['Statut closing'] = 'En cours'
                
                # Enrichment
                k_match = get_best_match(norm_s_name, knowledge_base)
                if k_match:
                    emails = sorted(list(k_match['emails']))
                    phones = sorted(list(k_match['phones']))
                    new_row['Email 1 Extrait'] = emails[0] if emails else 'N/D'
                    new_row['Email 2 Extrait'] = emails[1] if len(emails) > 1 else 'N/D'
                    new_row['Téléphone Extrait'] = " / ".join(phones) if phones else 'N/D'
                    new_row['Ville (Contact)'] = k_match['ville']
                    new_row['Ville (Propriété)'] = k_match['ville']
                else:
                    new_row['Email 1 Extrait'] = 'N/D'
                    new_row['Email 2 Extrait'] = 'N/D'
                    new_row['Téléphone Extrait'] = 'N/D'
                
                seen_names[norm_s_name] = new_row
                final_data.append(new_row)
            else:
                # EXISTING -> Just update status
                seen_names[norm_s_name]['Statut'] = statut_found

    # 4. Final Formulas and N°
    for idx, row in enumerate(final_data, 1):
        row["N°"] = idx
        row_idx = idx + 1
        row['Priorite'] = f'=IF(OR(E{row_idx}<5, H{row_idx}="NON", I{row_idx}="NON", J{row_idx}="NON"), "HAUTE", "MOYENNE")'
        row['Alerte Complétude'] = f'=IF(AND(H{row_idx}="OUI", I{row_idx}="OUI", J{row_idx}="OUI"), "✅ COMPLET", "⚠️ À OPTIMISER")'

    with open(output_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=target_fieldnames)
        writer.writeheader()
        writer.writerows(final_data)
    
    print(f"Generated Super Enriched File: {len(final_data)} rows.")

if __name__ == "__main__":
    generate_super_enriched_merge()
