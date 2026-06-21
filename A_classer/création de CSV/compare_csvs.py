import csv

def compare_csvs():
    master_path = 'CSV client HH/CLIENTS_Triage_Enrichi_V2.csv'
    sheet_path = 'prompt générato/prospection_hebergement.csv'
    
    master_names = set()
    try:
        with open(master_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("Nom de l'établissement")
                if name:
                    master_names.add(name.strip().lower())
    except Exception as e:
        print(f"Error reading master: {e}")

    sheet_rows = []
    try:
        with open(sheet_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if len(row) > 4:
                    sheet_rows.append(row)
    except Exception as e:
        print(f"Error reading sheet: {e}")

    new_names = []
    for row in sheet_rows:
        # Based on my previous check, name is in col 5 (index 4)
        name = row[4].strip().lower()
        if name and name not in master_names:
            new_names.append(row[4])
            
    print(f"Total rows in Sheet: {len(sheet_rows)}")
    print(f"Total unique names in Master: {len(master_names)}")
    print(f"Names in Sheet NOT in Master: {len(new_names)}")
    if new_names:
        print(f"First 10 new names: {new_names[:10]}")

if __name__ == "__main__":
    compare_csvs()
