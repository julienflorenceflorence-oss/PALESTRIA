import csv

def update_csv_batch6():
    file_path = 'CLIENTS_Triage_Enrichi_V2.csv'
    
    rows = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    updates = {
        '141': {'Phone': '+689 89 55 25 25', 'Email1': 'notremaisondelabaiedecook@gmail.com', 'Ville': 'Pao-Pao (Moorea)', 'Pays': 'Polynésie française'},
        '142': {'Phone': '07 52 63 20 55', 'Email1': 'otroispuits@gmail.com'},
        '143': {'Phone': '+33 6 75 60 23 20', 'Email1': 'info@ostalada46.fr'},
        '144': {'Phone': '05 63 65 57 95 / 07 68 26 42 98', 'Email1': 'N/D (Formulaire)'},
        '146': {'Phone': '07 79 77 75 13', 'Email1': 'mprohr.france@gmail.com'},
        '147': {'Phone': '+33 6 07 03 47 99', 'Email1': 'info@regisland.com'},
        '148': {'Phone': '+212 6 11 34 35 50', 'Email1': 'riadlaportedubouregreg@gmail.com'},
        '149': {'Phone': '+212 661 687 131', 'Email1': 'almalamzrou@yahoo.fr'},
        '150': {'Phone': '06 58 41 67 00', 'Email1': 'contact@suite785-montauban.com', 'Ville': 'Montauban', 'Pays': 'France'},
        '151': {'Phone': '06 50 62 18 21', 'Email1': 'mnfevents81@gmail.com', 'Ville': 'Castelnau-de-Lévis', 'Pays': 'France'},
        '152': {'Phone': '+33 7 71 73 94 36', 'Email1': 'suska@thehappyhamlet.com'},
        '153': {'Phone': '06 73 22 20 55', 'Email1': 'giteunairdefamille@gmail.com'},
        '154': {'Phone': '+33 6 98 00 25 32', 'Email1': 'N/D (Dreamsway)'},
        '155': {'Phone': '06 76 13 18 99', 'Email1': 'vanillebourbon82@gmail.com'},
        '156': {'Phone': '+33 6 23 61 45 86', 'Email1': 'emilie.pujolcudicini@gmail.com'},
        '157': {'Phone': '06 61 35 46 41', 'Email1': 'nicolascarboni2a@gmail.com'},
        '158': {'Phone': '06 28 80 44 68', 'Email1': 'franck.martin.lp@hotmail.fr'},
        '159': {'Phone': '+33 6 33 87 99 91', 'Email1': 'contact@villamaskali.com'},
        '160': {'Phone': '+33 6 80 90 49 71', 'Email1': 'bcbg1@hotmail.com'},
        '161': {'Phone': '+33 6 98 00 25 32', 'Email1': 'N/D (Dreamsway)'},
    }

    for row in rows:
        n = row['N°']
        if n in updates:
            u = updates[n]
            if 'Phone' in u: row['Téléphone Extrait'] = u['Phone']
            if 'Email1' in u: row['Email 1 Extrait'] = u['Email1']
            if 'Ville' in u: row['Ville'] = u['Ville']
            if 'Pays' in u: row['Pays'] = u['Pays']

    with open(file_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    update_csv_batch6()
    print("CSV Batch 6 updated.")
