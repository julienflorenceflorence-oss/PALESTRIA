import csv
import os

data_dir = 'DATAs'
files = [f for f in os.listdir(data_dir) if f.startswith('datatourisme-reg-') and f.endswith('.csv')]

region_stats = {}
category_stats = {}
stars_distribution = {
    '1 étoile': 0, '2 étoiles': 0, '3 étoiles': 0, '4 étoiles': 0, '5 étoiles': 0
}

total_pois = 0

for file in files:
    region_name = file.replace('datatourisme-reg-', '').replace('.csv', '').upper()
    region_stats[region_name] = 0
    
    file_path = os.path.join(data_dir, file)
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            # Use delimiter detection or common delimiters
            reader = csv.DictReader(f)
            for row in reader:
                total_pois += 1
                region_stats[region_name] += 1
                
                # Categories (split by |)
                cats = row.get('Categories_de_POI', '').split('|')
                for cat in cats:
                    cat_name = cat.split('#')[-1]
                    if cat_name:
                        category_stats[cat_name] = category_stats.get(cat_name, 0) + 1
                
                # Rankings/Stars
                ranking = row.get('Classements_du_POI', '')
                for star in stars_distribution.keys():
                    if star in ranking:
                        stars_distribution[star] += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Get Top 10 Categories
top_categories = dict(sorted(category_stats.items(), key=lambda item: item[1], reverse=True)[:10])

print("--- REGIONAL DISTRIBUTION ---")
for reg, count in region_stats.items():
    print(f"{reg}: {count}")

print("\n--- TOP 10 CATEGORIES ---")
for cat, count in top_categories.items():
    print(f"{cat}: {count}")

print("\n--- STARS DISTRIBUTION ---")
for star, count in stars_distribution.items():
    print(f"{star}: {count}")

print("\n--- TOTAL POIs ---")
print(total_pois)
