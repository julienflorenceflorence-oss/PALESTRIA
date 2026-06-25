# Fichier : convert.py
import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path):
    """
    Lit les données d'un fichier CSV et les convertit en un fichier JSON
    formaté pour le dashboard_prospects.html.
    """
    prospects = []
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            # Assurez-vous que votre CSV utilise le point-virgule comme séparateur si besoin
            # csv_reader = csv.DictReader(csv_file, delimiter=';') 
            csv_reader = csv.DictReader(csv_file)
            
            for i, row in enumerate(csv_reader):
                # Correction pour correspondre aux en-têtes de votre CSV
                rating_str = ''.join(filter(str.isdigit, row.get("Classements_du_POI", "0")))
                prospects.append({
                    "id": i + 1,
                    "name": row.get("Nom_du_POI", ""),
                    "type": row.get("Type_Client", ""),
                    "department": row.get("Code_postal_et_commune", "").split('#')[0][:2],
                    "rating": int(rating_str) if rating_str.isdigit() else 0,
                    "zipCode": row.get("Code_postal_et_commune", "").split('#')[0],
                    "city": row.get("Code_postal_et_commune", "").split('#')[1] if '#' in row.get("Code_postal_et_commune", "") else "",
                    "phone": row.get("Telephone_Final", ""),
                    "status": row.get("Statut_Prospection", ""),
                    "note": row.get("Dernier_Commentaire", "")
                })
        
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(prospects, json_file, indent=2, ensure_ascii=False)
            
        print(f"✅ Conversion réussie ! {len(prospects)} prospects ont été écrits dans {json_file_path}")

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier {csv_file_path} est introuvable.")
    except Exception as e:
        print(f"❌ Une erreur est survenue : {e}")

# --- UTILISATION ---
# Le script est maintenant adapté pour utiliser directement votre fichier CSV.
csv_input = 'super-agent-data-analyst/Prospection_Segmentee_Affinée.csv'
json_output = 'prospects.json'

convert_csv_to_json(csv_input, json_output)
