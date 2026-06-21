import pandas as pd
import os
import re
import unicodedata

def normalize_string(s):
    if not isinstance(s, str):
        return ""
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.lower().replace('-', ' ').replace('_', ' ')
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def clean_phone(p):
    if not isinstance(p, str) or pd.isna(p): return ""
    p_clean = re.sub(r'\D', '', p)
    if len(p_clean) >= 10:
        if p_clean.startswith('0'): return "+33" + p_clean[1:]
        if p_clean.startswith('33'): return "+" + p_clean
    return p

def is_valid_email(e):
    if not isinstance(e, str) or pd.isna(e): return False
    e = e.lower()
    internal = ['my-happy.house', 'entegraps.fr', 'google.com']
    return "@" in e and not any(dom in e for dom in internal)

def main():
    base_path = r"C:\Users\julien\OneDrive\Bureau\geminicli\création de CSV"
    triage_path = os.path.join(base_path, "CSV client HH", "CLIENTS _ - Triage Clients.csv")
    sources = [
        os.path.join(base_path, "extraction_donnees_adhesions_complet.csv"),
        os.path.join(base_path, "prospection_hebergement.csv"),
        os.path.join(base_path, "extraction_donnees_adhesions_final.csv"),
        os.path.join(base_path, "extraction_donnees_adhesions.csv")
    ]
    output_path = os.path.join(base_path, "CSV client HH", "CLIENTS_Triage_Enrichi_V2.csv")

    # Charger le fichier cible
    df_target = pd.read_csv(triage_path)
    
    # Dictionnaire de correspondance (Nom normalisé -> {emails: set, phones: set})
    master_data = {}

    # Parcourir toutes les sources pour collecter les infos
    for src in sources:
        if not os.path.exists(src): continue
        print(f"Analyse de la source : {os.path.basename(src)}")
        try:
            # Essayer différents encodages si besoin
            df_src = pd.read_csv(src, encoding='utf-8', on_bad_lines='skip')
        except:
            df_src = pd.read_csv(src, encoding='latin1', on_bad_lines='skip')

        # Identifier les colonnes Nom, Email et Tel (varient selon les fichiers)
        col_map = {
            'nom': ["Nom_Entreprise", "Nom de l'établissement", "Nom de l'entreprise", "Entreprise"],
            'email': ["Email_Direct", "Email_Generique", "Email", "Courriel", "Email 1 Extrait"],
            'tel': ["Telephone_Mobile", "Telephone_Standard", "Telephone", "Tel", "Téléphone Extrait"]
        }

        # Trouver les colonnes réelles dans ce CSV
        actual_cols = {k: [c for c in v if c in df_src.columns] for k, v in col_map.items()}

        for _, row in df_src.iterrows():
            # Trouver le nom de l'établissement
            name = ""
            for c in actual_cols['nom']:
                if pd.notna(row[c]):
                    name = str(row[c])
                    break
            
            if not name: continue
            norm_name = normalize_string(name)
            if norm_name not in master_data:
                master_data[norm_name] = {'emails': set(), 'phones': set()}

            # Collecter Emails
            for c in actual_cols['email']:
                val = str(row[c])
                if is_valid_email(val):
                    master_data[norm_name]['emails'].add(val.lower().strip())

            # Collecter Téléphones
            for c in actual_cols['tel']:
                val = str(row[c])
                if pd.notna(row[c]) and val != "N/D":
                    master_data[norm_name]['phones'].add(clean_phone(val))

    # Appliquer les données au fichier cible
    new_phones = []
    new_emails_1 = []
    new_emails_2 = []

    for _, row in df_target.iterrows():
        etab_name = str(row["Nom de l'établissement"])
        norm_etab = normalize_string(etab_name)
        
        # Matcher le nom (exact ou partiel)
        info = master_data.get(norm_etab, {'emails': set(), 'phones': set()})
        
        # Si pas de match exact, chercher si le nom de l'un est dans l'autre
        if not info['emails'] and not info['phones']:
            for k, v in master_data.items():
                if norm_etab in k or k in norm_etab:
                    info = v
                    break

        # Emails
        emails = sorted(list(info['emails']))
        new_emails_1.append(emails[0] if len(emails) > 0 else "N/D")
        new_emails_2.append(emails[1] if len(emails) > 1 else "N/D")

        # Téléphones
        phones = [p for p in info['phones'] if p]
        new_phones.append(" / ".join(phones) if phones else "N/D")

    # Mettre à jour le DataFrame
    df_target['Téléphone Extrait'] = new_phones
    df_target['Email 1 Extrait'] = new_emails_1
    df_target['Email 2 Extrait'] = new_emails_2

    # Sauvegarder
    df_target.to_csv(output_csv_path := output_path, index=False, encoding='utf-8-sig')
    print(f"Fusion terminée ! Fichier généré : {output_csv_path}")

if __name__ == "__main__":
    main()
