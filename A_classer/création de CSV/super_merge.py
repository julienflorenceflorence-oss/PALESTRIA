import pandas as pd
import os
import re
import unicodedata

def normalize(s):
    if not isinstance(s, str): return ""
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.lower().replace('-', ' ').replace('_', ' ')
    s = re.sub(r'[^a-z0-9\s]', '', s)
    return " ".join(s.split())

def main():
    base = r"C:\Users\julien\OneDrive\Bureau\geminicli\création de CSV"
    target_path = os.path.join(base, "CSV client HH", "CLIENTS _ - Triage Clients.csv")
    output_path = os.path.join(base, "CSV client HH", "CLIENTS_Triage_Final_V3.csv")
    
    # Sources CSV
    sources = [
        os.path.join(base, "extraction_donnees_adhesions_complet.csv"),
        os.path.join(base, "extraction_donnees_adhesions_final.csv"),
        os.path.join(base, "prospection_hebergement.csv"),
        os.path.join(base, "extraction_donnees_adhesions.csv"),
        os.path.join(base, "extraction_contrats.csv")
    ]

    # 1. Charger le fichier cible
    df_target = pd.read_csv(target_path)
    
    # 2. Collecter toutes les paires (Nom, Email, Tel) de TOUTES les sources
    all_known_data = []
    for src in sources:
        if not os.path.exists(src): continue
        print(f"Chargement source : {os.path.basename(src)}")
        try:
            df = pd.read_csv(src, encoding='utf-8-sig')
        except:
            df = pd.read_csv(src, encoding='latin1')
            
        # Normaliser les noms de colonnes pour trouver Nom, Email, Tel
        cols = {c.lower(): c for c in df.columns}
        
        # Trouver les colonnes probables
        n_col = next((cols[c] for c in ['nom_entreprise', 'nom de l'établissement', 'nom_etablissement', 'nom', 'entreprise'] if c in cols), None)
        e_col = next((cols[c] for c in ['email_direct', 'email_generique', 'email', 'courriel', 'email 1 extrait'] if c in cols), None)
        t_col = next((cols[c] for c in ['telephone_mobile', 'telephone_standard', 'telephone', 'tel', 'téléphone extrait'] if c in cols), None)
        
        if n_col:
            for _, row in df.iterrows():
                name = str(row[n_col]) if pd.notna(row[n_col]) else ""
                email = str(row[e_col]) if e_col and pd.notna(row[e_col]) else ""
                tel = str(row[t_col]) if t_col and pd.notna(row[t_col]) else ""
                
                if name and (email or tel):
                    all_known_data.append({
                        'norm_name': normalize(name),
                        'email': email.lower() if "@" in email else "",
                        'tel': tel if tel != "N/D" else ""
                    })

    # 3. Enrichissement intelligent
    emails_1, emails_2, phones = [], [], []

    for _, row in df_target.iterrows():
        name = str(row["Nom de l'établissement"])
        norm_name = normalize(name)
        
        found_emails = set()
        found_phones = set()
        
        # Chercher dans notre base de données connue
        for entry in all_known_data:
            # Match si le nom de l'un contient l'autre ou vice-versa
            if norm_name and entry['norm_name'] and (norm_name in entry['norm_name'] or entry['norm_name'] in norm_name):
                if entry['email'] and "my-happy.house" not in entry['email']:
                    found_emails.add(entry['email'])
                if entry['tel']:
                    found_phones.add(entry['tel'])
        
        # Nettoyage et Ajout
        emails = sorted(list(found_emails))
        tels = sorted(list(found_phones))
        
        emails_1.append(emails[0] if len(emails) > 0 else "N/D")
        emails_2.append(emails[1] if len(emails) > 1 else "N/D")
        phones.append(" / ".join(tels) if tels else "N/D")

    # 4. Sauvegarder
    df_target['Téléphone Extrait'] = phones
    df_target['Email 1 Extrait'] = emails_1
    df_target['Email 2 Extrait'] = emails_2
    
    df_target.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"TERMINÉ ! Fichier généré : {output_path}")

if __name__ == "__main__":
    main()
