import csv

def update_csv_batch4():
    file_path = 'CLIENTS_Triage_Enrichi_V2.csv'
    
    rows = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    updates = {
        '81': {'Phone': '04 68 50 30 10', 'Email1': 'contact@riberach.com'},
        '82': {'Phone': '06 18 07 32 35', 'Email1': 'contact@ecogite-la-noe.fr'},
        '83': {'Phone': '06 80 87 47 92', 'Email1': 'N/D (Formulaire)', 'Ville': 'Saint-Antonin-Noble-Val', 'Pays': 'France'},
        '84': {'Phone': '07 61 92 39 57', 'Email1': 'contact@peniche-saint-louis.fr'},
        '85': {'Email1': 'info@entegraps.eu'},
        '86': {'Phone': '+33 6 60 700 400', 'Email1': 'contact@my-happy.house'},
        '87': {'Phone': '05 32 00 20 93', 'Email1': 'lavilleenrosetoulouse@gmail.com', 'Ville': 'Colomiers', 'Pays': 'France'},
        '88': {'Phone': '06 51 01 77 75', 'Email1': 'lbdr@sfr.fr', 'Ville': 'Sauvagnon', 'Pays': 'France'},
        '89': {'Phone': '06 75 64 81 55', 'Email1': 'leboudoirdolympe@gmail.com'},
        '90': {'Phone': '06 87 29 88 82 / 04 68 24 44 49', 'Email1': 'contact@lechaletcathare.fr'},
        '91': {'Phone': '04 68 81 25 70', 'Email1': 'contact@chateau-valmy.com'},
        '92': {'Phone': '+33 6 60 700 400', 'Email1': 'contact@my-happy.house'},
        '93': {'Phone': '06 98 00 25 32', 'Email1': 'bienvenue@ledomainedengrazac.com'},
        '94': {'Phone': '06 98 31 79 61', 'Email1': 'philippe.risso@firea.com'},
        '95': {'Phone': '05 63 95 51 10', 'Email1': 'bienvenue@domainedubelvedere.com'},
        '96': {'Phone': '04 79 63 22 14', 'Email1': 'le.doux.nid@gmail.com'},
        '97': {'Phone': '+689 87 23 02 02', 'Email1': 'contact@fafarualodge.com', 'Ville': 'Tikehau', 'Pays': 'Polynésie française'},
        '98': {'Phone': '05 81 04 87 78 / 06 29 58 71 72', 'Email1': 'laverrouille@gmail.com'},
        '99': {'Phone': '06 22 94 60 46 / 06 12 89 05 69', 'Email1': 'anne.rigaud63@gmail.com'},
        '100': {'Phone': '07 67 95 35 88', 'Email1': 'legrandbassin@outlook.fr'},
        '101': {'Phone': '06 10 15 06 62', 'Email1': 'Lehameau@s-o-l.fr'},
        '102': {'Phone': '06 59 50 07 89', 'Email1': 'lejardinsecret32@outlook.fr', 'Ville': 'Montpezat (Gers)', 'Pays': 'France'},
        '103': {'Phone': '06 88 57 16 21', 'Email1': 'manoiramiel@gmail.com'},
        '104': {'Phone': '06 85 46 14 45', 'Email1': 'marielabaroudeuse@gmail.com'},
        '105': {'Phone': '06 88 30 88 47', 'Email1': 'lemoulindebouqueuil@orange.fr'},
        '106': {'Phone': '03 85 36 49 27', 'Email1': 'reception@moulindelabrevette.com'},
        '107': {'Phone': '+212 6 64 49 26 60', 'Email1': 'leflouka@gmail.com'},
        '108': {'Phone': '06 10 92 33 24', 'Email1': 'contact@stlarylocations.com'},
        '109': {'Phone': '07 69 77 64 60', 'Email1': 'lucas@monsieurspot.fr'},
        '110': {'Phone': '06 79 29 06 05', 'Email1': 'fgb.hospitalite@gmail.com'},
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
    update_csv_batch4()
    print("CSV Batch 4 updated.")
