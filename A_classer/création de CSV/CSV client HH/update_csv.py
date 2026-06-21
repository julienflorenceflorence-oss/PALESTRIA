import csv
import io

def update_csv():
    # Load V2 as the base
    v2_rows = []
    with open('CLIENTS_Triage_Enrichi_V2.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            v2_rows.append(row)

    # Load Enrichi V1 to get previous data
    enrichi_v1_data = {}
    with open('CLIENTS_Triage_Clients_Enrichi.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Téléphone Extrait'] != 'N/D' or row['Email 1 Extrait'] != 'N/D':
                enrichi_v1_data[row['N°']] = {
                    'Téléphone': row['Téléphone Extrait'],
                    'Email 1': row['Email 1 Extrait'],
                    'Email 2': row['Email 2 Extrait']
                }

    # New data found manually
    new_data = {
        '1': {'Phone': '+33 6 01 79 38 62', 'Email1': '4ubedspa@gmail.com'},
        '2': {'Phone': '07 56 91 06 06', 'Email1': 'lesrelaisducapitole@gmail.com'},
        '3': {'Phone': '06 14 46 29 75 / 06 27 08 60 00', 'Email1': 'location@arbiview.com'},
        '4': {'Phone': '+212 661 488 504 / +212 662 188 889', 'Email1': 'contact@atlaskasbah.com', 'Ville': 'Agadir', 'Pays': 'Maroc'},
        '5': {'Phone': '05 63 67 35 15 / 06 49 45 07 98', 'Email1': 'auxcoteauxdaussac@gmail.com'},
        '6': {'Phone': '06 10 08 57 94 / 06 22 26 32 70', 'Email1': 'auxrivesdelacourtade@gmail.com'},
        '7': {'Phone': '06 30 41 69 57 / 06 19 01 28 67', 'Email1': 'contact@domaineducolombier-tarn.com'},
        '9': {'Ville': 'Toulouse', 'Pays': 'France'},
        '10': {'Phone': '05 63 66 74 60 / 06 20 93 44 70', 'Email1': 'castel.boismarie@gmail.com'},
        '11': {'Ville': 'Toulouse', 'Pays': 'France'},
        '12': {'Phone': '06 12 95 00 44', 'Email1': 'info@chalet-guytoune.com'},
        '13': {'Phone': '+33 6 74 87 41 20', 'Email1': 'contact@locationshygge.com'},
        '15': {'Phone': '+33 6 50 90 29 76', 'Email1': 'fabienne@chaletnantailly.fr'},
        '16': {'Phone': '05 62 39 19 03 / 07 65 85 05 01', 'Email1': 'maisonseignou@gmail.com'},
        '17': {'Ville': 'Toulouse', 'Pays': 'France'},
        '18': {'Phone': '+33 6 07 43 12 80', 'Email1': 'Welcome@chateau-bagen.com'},
        '19': {'Phone': '+33 6 11 31 36 28', 'Email1': 'chateaudaigrefeuille31@gmail.com'},
    }

    # Apply updates
    for row in v2_rows:
        num = row['N°']
        # Update from Enrichi V1
        if num in enrichi_v1_data:
            row['Téléphone Extrait'] = enrichi_v1_data[num]['Téléphone']
            row['Email 1 Extrait'] = enrichi_v1_data[num]['Email 1']
            row['Email 2 Extrait'] = enrichi_v1_data[num]['Email 2']
        
        # Update from manual search
        if num in new_data:
            d = new_data[num]
            if 'Phone' in d: row['Téléphone Extrait'] = d['Phone']
            if 'Email1' in d: row['Email 1 Extrait'] = d['Email1']
            if 'Ville' in d: row['Ville'] = d['Ville']
            if 'Pays' in d: row['Pays'] = d['Pays']

    # Write back to V2
    with open('CLIENTS_Triage_Enrichi_V2.csv', mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(v2_rows)

if __name__ == "__main__":
    update_csv()
    print("CSV updated successfully.")
