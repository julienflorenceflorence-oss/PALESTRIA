import pandas as pd
import re
import json

def get_star_rating(text):
    if not isinstance(text, str):
        return 0
    match = re.search(r'(\d+)\s*étoile', text)
    if match:
        return int(match.group(1))
    return 0

def process_prospects(urls):
    all_dfs = []
    first_file_columns = None

    for i, url in enumerate(urls):
        try:
            df = pd.read_csv(url, dtype=str) # Read all as string to avoid type issues
            if i == 0:
                first_file_columns = df.columns
                all_dfs.append(df)
            else:
                df.columns = first_file_columns
                all_dfs.append(df)
        except Exception as e:
            print(f"Could not read or process {url}. Error: {e}")
            continue

    if not all_dfs:
        print("No data could be fetched.")
        return

    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Drop duplicates just in case
    combined_df.drop_duplicates(subset=['Nom_du_POI', 'Adresse_Ligne_1', 'Code_Postal'], inplace=True)

    # Filtering
    # 1. Telephone_Final is not empty
    filtered_df = combined_df[combined_df['Telephone_Final'].notna() & (combined_df['Telephone_Final'] != '')].copy()

    # 2. & 3. Classements_du_POI contains star rating and it's 3, 4, or 5
    filtered_df['rating'] = filtered_df['Classements_du_POI'].apply(get_star_rating)
    filtered_df = filtered_df[filtered_df['rating'] >= 3]

    # Select 14,500 prospects
    selection_df = filtered_df.head(14500)
    
    # Save to CSV
    # Need to remove the 'rating' column which was added for filtering
    csv_output_df = selection_df.drop(columns=['rating'])
    csv_output_df.to_csv('selection_14500_prospects.csv', index=False, encoding='utf-8-sig')

    # Create JSON
    prospects_json = []
    # Using selection_df which has the 'rating' column
    for index, row in selection_df.iterrows():
        # Generate a unique ID from the original index
        unique_id = index 
        prospects_json.append({
            "id": unique_id,
            "name": row.get('Nom_du_POI', ''),
            "type": "Hotel", # As inferred
            "department": row.get('Département', ''),
            "rating": row.get('rating', 0),
            "zipCode": row.get('Code_Postal', ''),
            "city": row.get('Commune', ''),
            "phone": row.get('Telephone_Final', ''),
            "status": "Pending", # Default value
            "note": "" # Default value
        })

    with open('prospects.json', 'w', encoding='utf-8') as f:
        json.dump(prospects_json, f, ensure_ascii=False, indent=4)
    
    num_prospects = len(selection_df)
    print(f"Created 'selection_14500_prospects.csv' and 'prospects.json' with {num_prospects} prospects.")

if __name__ == '__main__':
    urls = [
        "https://docs.google.com/spreadsheets/d/16xEkmHnZJmAEbcEilli95TWWwD5pIBJKesXGpFr1YfQ/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1CB6oz_q-F2GGt6PFoftaHUqSS5BCyysCTBGSfFgdktQ/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1DLW4Ql_GD656-cfBxjl01oDUw2o_ejxGm7YvEFYhMWA/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1Jv89nD2IirexXHznnPhAx_TOwPgj6Riikb2ZP7nDIFw/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1Npettna1YMDfVOvJmbW9p6PxdhhQ1QfL2VXYzXeX3aI/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1U7jzOMtjO9Wta73vWC_ez0xy7TnIq87XFgNrL3ypCiE/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1VE8-exPjxLZqm66dgqwQJ98FcMUXnCa-18EQQqR8ijc/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1_Upc5p9KgYqDYCq82ZN74jGof7Y9JYq-yyCIgL5Cyvg/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1cqQrmj5j3-w9Zlr-0JlrW-J5BfaIWtpn9wT3zZCLYto/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1dJNnyOZC6kTjC-i38nhTaU0w7PfK5Nf0bzfr9ZkZcog/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1jgxlR0q_3iSkTgOBOt1shgXPwmXykQOOrAAdAyy2tiI/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1mozjzEIcoWc5hPTjo6nbRh8q_36Et5CkglHS5ElocP0/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1oksjEFt3Omy37aSJIyvfFpx_TH7-kQKptThGs2KDi5k/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1r-pMxVqe0aTBlH87crHQY0nY6BaEY7YV1jHvOetpXF8/export?format=csv",
        "https://docs.google.com/spreadsheets/d/1shGLiDKfUycyHnY9-85G1U3FTxwnGQypN-o7dbXducc/export?format=csv"
    ]
    process_prospects(urls)
