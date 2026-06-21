import csv

def update_csv_v2():
    # File path
    file_path = 'CLIENTS_Triage_Enrichi_V2.csv'
    
    # Read existing rows
    rows = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    # Data batch 20-50
    updates = {
        '20': {'Phone': '06 81 56 61 92', 'Email1': 'chateaulabaronnie@gmail.com'},
        '21': {'Phone': '06 37 68 35 94 / 05 63 71 09 45', 'Email1': 'chateaudeverdalle81@gmail.com'},
        '22': {'Phone': '07 86 53 97 31 / 02 47 26 42 10', 'Email1': 'info@chateaulavillaine.com'},
        '23': {'Phone': '07 83 23 39 36', 'Email1': 'chateaulesestournels@gmail.com'},
        '24': {'Phone': '04 68 78 24 82', 'Email1': 'info@chateaustjacques.com'},
        '25': {'Phone': '06 61 44 60 15', 'Email1': 'bienvenue@chezpepemerle.fr'},
        '26': {'Phone': '02 62 01 09 87 / 06 92 35 08 60', 'Email1': 'sandijoux@gmail.com', 'Ville': 'Cilaos', 'Pays': 'Réunion'},
        '27': {'Phone': '06 87 45 16 67 / 06 52 04 50 57', 'Email1': 'contact@closdescoustoulins.com', 'Ville': 'Lacoste', 'Pays': 'France'},
        '28': {'Phone': '05 63 57 61 48', 'Email1': 'contact@combettesgaillac.com'},
        '30': {'Phone': '+212 6 78 31 12 27 / +212 5 28 87 13 33', 'Email1': 'darbounkhal@gmail.com'},
        '31': {'Phone': '06 22 93 17 84', 'Email1': 'corinnebourgela@gmail.com'},
        '32': {'Phone': '06 03 38 55 13', 'Email1': 'davidjdd@neuf.fr'},
        '33': {'Phone': '+33 (0)6 07 35 10 80', 'Email1': 'contact@domainedelocrerie.com'},
        '34': {'Phone': '+33 (0)6 15 54 33 13', 'Email1': 'reservations@domainedeladurantie.com'},
        '35': {'Phone': '06 21 88 88 33 / 06 12 38 26 04', 'Email1': 'domaine.rivaliere@gmail.com'},
        '36': {'Phone': '+33 (0)6 30 76 03 22', 'Email1': 'info@lesfargues.com'},
        '37': {'Phone': '06 19 65 32 89 / 07 71 37 25 05', 'Email1': 'lafermeduchateaumarquefave@gmail.com'},
        '38': {'Phone': '+33 (0)4 68 50 30 10', 'Email1': 'contact@riberach.com'},
        '39': {'Phone': '+212 525 072 107', 'Email1': 'contact@essaouira-lodge.com'},
        '40': {'Phone': '+33 6 78 66 05 84', 'Email1': 'contact@legitedicietdailleurs.com'},
        '41': {'Phone': '06 52 73 59 76', 'Email1': 'o.saillant@free.fr'},
        '43': {'Phone': '06 22 94 60 46 / 06 12 89 05 69', 'Email1': 'anne.rigaud63@gmail.com'},
        '44': {'Phone': '06 25 65 24 85', 'Email1': 'gitesdudaudou@yahoo.com'},
        '45': {'Phone': '06 63 19 19 87', 'Email1': 'N/D (Formulaire)'},
        '46': {'Phone': '06 10 92 33 24', 'Email1': 'contact@kasalilou.com'},
        '47': {'Phone': '06 65 98 14 76', 'Email1': 'N/D', 'Ville': 'Pont-Croix', 'Pays': 'France'},
        '48': {'Phone': '+33 (0)6 37 78 20 72', 'Email1': 'contact@laccrochecoeur.fr'},
        '49': {'Phone': '+33 (0)7 52 55 00 97', 'Email1': 'info@lannicha.com'},
        '50': {'Phone': '07 85 70 90 62', 'Email1': 'contact@arche-de-moissac.com'},
        '51': {'Phone': '+33 6 08 15 09 40', 'Email1': 'contact@lecrindelacite.com'},
    }

    # Apply updates
    for row in rows:
        n = row['N°']
        if n in updates:
            u = updates[n]
            if 'Phone' in u: row['Téléphone Extrait'] = u['Phone']
            if 'Email1' in u: row['Email 1 Extrait'] = u['Email1']
            if 'Ville' in u: row['Ville'] = u['Ville']
            if 'Pays' in u: row['Pays'] = u['Pays']

    # Write header and all rows back
    with open(file_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    update_csv_v2()
    print("CSV Batch 2 updated.")
