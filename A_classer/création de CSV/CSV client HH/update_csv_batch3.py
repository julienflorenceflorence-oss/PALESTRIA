import csv

def update_csv_batch3():
    # File path
    file_path = 'CLIENTS_Triage_Enrichi_V2.csv'
    
    # Read existing rows
    rows = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    # Data batch 53-80
    updates = {
        '53': {'Phone': '06 77 31 03 58', 'Email1': 'contact@ecrinsousleschenes.com'},
        '54': {'Ville': 'Rustiques', 'Pays': 'France', 'Email1': 'N/D (Booking)'},
        '55': {'Phone': '06 17 24 94 73', 'Email1': 'ahermann@mail.pf'},
        '56': {'Phone': '06 10 92 33 24', 'Email1': 'carole.totaro@sfr.fr'},
        '57': {'Phone': '06 71 12 03 91', 'Email1': 'daniele.arfelis@gmail.com'},
        '58': {'Phone': '06 60 700 400', 'Email1': 'contact@my-happy.house', 'Ville': 'Sète', 'Pays': 'France'},
        '59': {'Phone': '06 51 20 73 53 / 03 89 49 55 99', 'Email1': 'contact@gite-oree-des-vignes.alsace'},
        '60': {'Phone': '06 80 80 72 87', 'Email1': 'olivia.geoffroy@yahoo.fr'},
        '61': {'Phone': '06 60 700 400', 'Email1': 'contact@my-happy.house'},
        '62': {'Phone': '06 58 13 45 86', 'Email1': 'N/D (Formulaire)'},
        '63': {'Phone': '05 62 39 50 88', 'Email1': 'accueil@vignec.fr'},
        '64': {'Phone': '05 58 79 94 93 / 06 84 78 07 25', 'Email1': 'contact@lafermedemarsan.com', 'Ville': 'Miramont-Sensacq', 'Pays': 'France'},
        '65': {'Phone': '05 62 09 82 85', 'Email1': 'contact@ferme-de-mounet.com', 'Ville': 'Eauze', 'Pays': 'France'},
        '69': {'Phone': '09 87 03 23 12 / 06 60 31 82 63', 'Email1': 'contact@lagrandemaisonmazamet.fr', 'Ville': 'Mazamet', 'Pays': 'France'},
        '70': {'Phone': '06 40 63 88 61 / 06 19 86 55 88', 'Email1': 'gitesvillagesaintpapoul@gmail.com'},
        '71': {'Phone': '06 07 60 14 61', 'Email1': 'N/D'},
        '72': {'Phone': '06 70 10 00 05 / 06 09 41 09 10', 'Email1': 'bienvenue@lajolievie.fr'},
        '73': {'Phone': '06 80 20 90 66', 'Email1': 'lamagnaneriededions@gmail.com'},
        '76': {'Phone': '05 63 40 47 80', 'Email1': 'contact@clement-termes.com'},
        '77': {'Phone': '05 63 33 26 63 / 06 37 93 99 42', 'Email1': 'info@chateau-de-terride.com'},
        '78': {'Phone': '06 88 55 09 03', 'Email1': 'N/D', 'Ville': 'Verdun-sur-Garonne', 'Pays': 'France'},
        '79': {'Phone': '04 68 11 40 70', 'Email1': 'contact.11@gites-sud.fr'},
        '80': {'Phone': '06 75 64 37 12', 'Email1': 'alain@lamaisondesdouceurs.fr'},
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

    # Write back
    with open(file_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    update_csv_batch3()
    print("CSV Batch 3 updated.")
