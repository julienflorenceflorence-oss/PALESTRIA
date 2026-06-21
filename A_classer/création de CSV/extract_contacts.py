import os
import re
import csv
import pandas as pd
from pypdf import PdfReader
from pathlib import Path
import unicodedata

def normalize_string(s):
    if not isinstance(s, str):
        return ""
    # Enlever les accents, mettre en minuscule, remplacer les tirets par des espaces
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.lower().replace('-', ' ').replace('_', ' ')
    # Ne garder que l'alphanumérique
    s = re.sub(r'[^a-z0-9\s]', '', s)
    # Supprimer les espaces multiples
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + " "
    except Exception as e:
        print(f"Erreur de lecture PDF {pdf_path}: {e}")
    return text

def extract_contacts_from_text(text):
    # Regex Email
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    
    # Filtres Emails
    # On ignore les domaines internes et techniques
    internal_domains = ['my-happy.house', 'entegraps.fr', 'google.com', 'microsoft.com']
    valid_emails = []
    for e in emails:
        e_low = e.lower()
        if not any(dom in e_low for dom in internal_domains) and not e_low.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            valid_emails.append(e_low)
    
    # Regex Téléphone
    phone_pattern = r'(?:(?:\+|00)\d{1,3}[\s.-]?)?(?:\(0\)[\s.-]?)?0?[1-9](?:[\s.-]?\d{2}){4}'
    phones = re.findall(phone_pattern, text)
    
    # Filtres Téléphones (on dégage les morceaux du RIB Happy House connus)
    # RIB HH: FR76 1027 8022 0400 0207 7910 220
    rib_parts = ['10278022', '04000207', '7910220', '1027 8022', '0400 0207', '7910 220']
    
    valid_phones = []
    for p in phones:
        p_clean = re.sub(r'\D', '', p)
        # On ignore si c'est un morceau de RIB ou si c'est trop long/court
        if any(rib in p.replace(' ', '') for rib in rib_parts):
            continue
        if len(p_clean) >= 10 and len(p_clean) <= 12:
            # Formatage Gold Standard : +33
            if p_clean.startswith('0'):
                p_formatted = "+33" + p_clean[1:]
            elif p_clean.startswith('33'):
                p_formatted = "+" + p_clean
            else:
                p_formatted = p
            valid_phones.append(p_formatted)
            
    return list(set(valid_emails)), list(set(valid_phones))

def main():
    base_dir = r"C:\Users\julien\OneDrive\Bureau\geminicli\création de CSV\1- Adhésion Hébergeurs"
    csv_path = r"C:\Users\julien\OneDrive\Bureau\geminicli\création de CSV\CSV client HH\CLIENTS _ - Triage Clients.csv"
    output_csv = r"C:\Users\julien\OneDrive\Bureau\geminicli\création de CSV\CSV client HH\CLIENTS_Triage_Clients_Enrichi.csv"
    
    # Créer le dossier s'il n'existe pas
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    # Lecture du CSV
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Fichier introuvable: {csv_path}")
        return

    # Indexation des dossiers par nom normalisé
    folders = {}
    if os.path.exists(base_dir):
        for folder_name in os.listdir(base_dir):
            folder_path = os.path.join(base_dir, folder_name)
            if os.path.isdir(folder_path):
                # Extraire le nom de l'entreprise du dossier (ex: "2024 - 104 - 75 - Chez Pepe Merle - ...")
                parts = folder_name.split(' - ')
                if len(parts) >= 4:
                    company_name = parts[3].strip()
                elif len(parts) == 3:
                    company_name = parts[2].strip()
                else:
                    company_name = folder_name
                
                norm_name = normalize_string(company_name)
                folders[norm_name] = folder_path
                # Ajouter aussi le nom complet du dossier normalisé au cas où
                folders[normalize_string(folder_name)] = folder_path
    
    # Listes pour les nouvelles colonnes
    all_emails_col1 = []
    all_emails_col2 = []
    all_phones_col = []
    
    for index, row in df.iterrows():
        nom_etab = str(row.get("Nom de l'établissement", ""))
        norm_etab = normalize_string(nom_etab)
        
        # Chercher le dossier correspondant
        matched_folder = None
        for k, v in folders.items():
            if norm_etab and (norm_etab in k or k in norm_etab):
                matched_folder = v
                break
                
        emails_found = []
        phones_found = []
        
        if matched_folder:
            print(f"-> Traitement de : {nom_etab}")
            for root, _, files in os.walk(matched_folder):
                for f in files:
                    if f.lower().endswith('.pdf'):
                        pdf_path = os.path.join(root, f)
                        # Ignorer les très gros fichiers (ex: > 10 Mo) pour gagner du temps
                        try:
                            if os.path.getsize(pdf_path) > 10 * 1024 * 1024:
                                print(f"   Ignoré (trop lourd) : {f}")
                                continue
                        except:
                            pass
                            
                        print(f"   Lecture de : {f}")
                        text = extract_text_from_pdf(pdf_path)
                        e, p = extract_contacts_from_text(text)
                        emails_found.extend(e)
                        phones_found.extend(p)
        
        # Dédoublonner
        emails_found = list(set(emails_found))
        phones_found = list(set(phones_found))
        
        # Remplir les données
        if not phones_found:
            all_phones_col.append("N/D")
        else:
            all_phones_col.append(" / ".join(phones_found))
            
        if len(emails_found) == 0:
            all_emails_col1.append("N/D")
            all_emails_col2.append("N/D")
        elif len(emails_found) == 1:
            all_emails_col1.append(emails_found[0])
            all_emails_col2.append("N/D")
        else:
            all_emails_col1.append(emails_found[0])
            all_emails_col2.append(emails_found[1])
            
    # Ajout au dataframe
    df['Téléphone Extrait'] = all_phones_col
    df['Email 1 Extrait'] = all_emails_col1
    df['Email 2 Extrait'] = all_emails_col2
    
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"Extraction terminée. Fichier généré : {output_csv}")

if __name__ == '__main__':
    main()
