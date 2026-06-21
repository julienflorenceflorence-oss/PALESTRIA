import csv

def update_csv_batch5():
    file_path = 'CLIENTS_Triage_Enrichi_V2.csv'
    
    rows = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    updates = {
        '111': {'Phone': '06 47 06 23 93', 'Email1': 'les3angesdesigean@gmail.com'},
        '112': {'Phone': '07 82 45 96 97', 'Email1': 'lesbastidesderoquemaure81@gmail.com'},
        '113': {'Phone': '06 77 72 96 12', 'Email1': 'contact@chalets-du-bonheur.com'},
        '114': {'Phone': '06 52 73 59 76', 'Email1': 'o.saillant@free.fr'},
        '115': {'Phone': '04 50 52 83 37', 'Email1': 'info@lescongeres.com', 'Ville': 'Le Grand-Bornand', 'Pays': 'France'},
        '116': {'Phone': '06 84 60 05 86', 'Email1': 'lescoulissesduchateau@gmail.com'},
        '117': {'Phone': '05 63 94 08 92 / 06 88 47 20 72', 'Email1': 'andreiseric@orange.fr'},
        '118': {'Phone': '06 18 01 74 50', 'Email1': 'melodiebeaume@hotmail.com'},
        '119': {'Phone': '06 18 01 74 50', 'Email1': 'melodiebeaume@hotmail.com'},
        '120': {'Phone': '06 18 01 74 50', 'Email1': 'melodiebeaume@hotmail.com', 'Ville': 'Oloron-Sainte-Marie', 'Pays': 'France'},
        '121': {'Phone': '07 87 20 71 90', 'Email1': 'contact@lesgrangesdelabbaye.com'},
        '122': {'Phone': '07 80 16 15 27', 'Email1': 'contact@leshautsdejeanvert.fr'},
        '123': {'Phone': '06 64 56 61 50', 'Email1': 'contact@leshautsdurebeillou.com', 'Ville': 'Flourens', 'Pays': 'France'},
        '124': {'Phone': '06 64 56 61 50', 'Email1': 'contact@leshautsdurebeillou.com'},
        '125': {'Phone': '07 66 84 32 58', 'Email1': 'contact@vacances-lespiedsdansleau.fr'},
        '126': {'Phone': '04 75 38 64 54', 'Email1': 'contact@lesvillasduvendoule.com'},
        '127': {'Phone': '06 03 80 43 44 / 04 68 75 40 87', 'Email1': 'loftdoc@gmail.com'},
        '128': {'Phone': '06 80 90 49 71', 'Email1': 'bcbg1@hotmail.com'},
        '129': {'Phone': '06 77 97 40 86 / 05 63 26 42 76', 'Email1': 'contact@loupapagai.com'},
        '130': {'Phone': '06 58 10 27 79', 'Email1': 'madamelesvans@gmail.com'},
        '131': {'Phone': '06 59 09 11 65', 'Email1': 'N/D', 'Ville': 'Fenouillet', 'Pays': 'France'},
        '132': {'Phone': '05 57 25 25 13 / 07 85 73 70 31', 'Email1': 'reservation@lafleurdebouard.com'},
        '133': {'Phone': '05 62 39 19 03', 'Email1': 'maisonseignou@gmail.com'},
        '134': {'Phone': '06 62 05 30 21', 'Email1': 'N/D'},
        '135': {'Phone': '06 61 93 01 33', 'Email1': 'contact@maylandie.fr', 'Ville': 'Ferrals-les-Corbières', 'Pays': 'France'},
        '136': {'Phone': '06 07 88 11 98', 'Email1': 'naturazome@gmail.com'},
        '137': {'Phone': '06 82 83 19 08', 'Email1': 'guezello.francoise56@orange.fr', 'Ville': 'Carnac', 'Pays': 'France'},
        '138': {'Phone': '07 82 37 20 95', 'Email1': 'N/D (Formulaire)', 'Ville': 'Bourg-de-Visa', 'Pays': 'France'},
        '139': {'Phone': '06 33 67 17 40', 'Email1': 'alcoveredu510@gmail.com', 'Ville': 'Montauban', 'Pays': 'France'},
        '140': {'Phone': '05 63 67 83 50', 'Email1': 'contact@collinedebouties.com', 'Ville': 'Labarthe', 'Pays': 'France'},
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
    update_csv_batch5()
    print("CSV Batch 5 updated.")
