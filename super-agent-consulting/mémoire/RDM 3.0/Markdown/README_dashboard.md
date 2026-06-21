# Documentation du Dashboard Prospects

## 1. Objectif de l'outil

Ce document décrit le fonctionnement du tableau de bord interactif des prospects et la manière de le mettre à jour avec vos propres données.

L'outil est composé de deux fichiers principaux situés dans le dossier `super-agent-consulting/mémoire/RDM 3.0/` :
1.  `dashboard_prospects.html` : L'interface visuelle et interactive du tableau de bord.
2.  `prospects.json` : Le fichier contenant la base de données des prospects. **C'est le seul fichier que vous aurez à modifier.**

---

## 2. Comment Utiliser le Dashboard

Pour utiliser le tableau de bord, il suffit d'ouvrir le fichier `dashboard_prospects.html` avec n'importe quel navigateur web (Chrome, Firefox, etc.).

Les fonctionnalités incluses sont :
*   **Recherche dynamique :** Tapez un nom ou une ville dans la barre de recherche.
*   **Filtres multiples :** Combinez les filtres par type, département et statut.
*   **Pagination :** Naviguez entre les pages si les résultats sont nombreux.

---

## 3. Comment Mettre à Jour les Données

Toute la puissance de cet outil réside dans sa capacité à afficher les données que vous lui fournissez via le fichier `prospects.json`.

### Structure des Données

Le fichier `prospects.json` doit contenir une liste d'objets, où chaque objet représente un prospect et respecte la structure suivante :

```json
{
  "id": 1,
  "name": "Nom de l'établissement",
  "type": "PROFESSIONNEL ou PARTICULIER",
  "department": "75",
  "rating": 5,
  "zipCode": "75001",
  "city": "Paris",
  "phone": "01 23 45 67 89",
  "status": "SUIVI NÉGO",
  "note": "Description ou note sur le prospect."
}
```
**Champs importants :**
*   `rating`: Doit être un nombre (ex: `3`), pas du texte (ex: `"⭐⭐⭐"`).
*   `status`: Doit correspondre à l'une des valeurs suivantes pour que les couleurs s'affichent correctement : `SUIVI NÉGO`, `NRP`, `REFUS CATÉGORIQUE`, `REFUS ARGUMENTÉ`.

### Méthode simple pour mettre à jour (avec un fichier CSV)

La façon la plus simple de gérer vos 14 000 prospects est de les avoir dans un fichier CSV (Excel). Voici comment le convertir automatiquement au format `prospects.json` requis.

**Étape 1 : Préparez votre fichier CSV**

Assurez-vous que votre fichier CSV (par exemple `mes_prospects.csv`) contient les en-têtes de colonnes suivantes :
`name,type,department,rating,zipCode,city,phone,status,note`

**Étape 2 : Utilisez un script de conversion**

Je vous ai préparé un script Python simple. Vous pouvez le sauvegarder dans un fichier nommé `convert.py` dans le même dossier et l'exécuter.

```python
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
                prospects.append({
                    "id": i + 1,
                    "name": row.get("name", ""),
                    "type": row.get("type", ""),
                    "department": row.get("department", ""),
                    "rating": int(row.get("rating", 0)) if row.get("rating", "0").isdigit() else 0,
                    "zipCode": row.get("zipCode", ""),
                    "city": row.get("city", ""),
                    "phone": row.get("phone", ""),
                    "status": row.get("status", ""),
                    "note": row.get("note", "")
                })
        
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(prospects, json_file, indent=2, ensure_ascii=False)
            
        print(f"✅ Conversion réussie ! {len(prospects)} prospects ont été écrits dans {json_file_path}")

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier {csv_file_path} est introuvable.")
    except Exception as e:
        print(f"❌ Une erreur est survenue : {e}")

# --- UTILISATION ---
# 1. Placez votre fichier CSV (ex: 'mes_prospects.csv') dans le même dossier.
# 2. Modifiez le nom du fichier ci-dessous si nécessaire.
# 3. Exécutez ce script Python.
# 4. Le fichier 'prospects.json' sera automatiquement créé ou mis à jour.
csv_input = 'mes_prospects.csv'
json_output = 'prospects.json'

convert_csv_to_json(csv_input, json_output)

```

**En résumé, pour toute mise à jour future :**
1.  Modifiez votre fichier CSV.
2.  Exécutez le script `convert.py`.
3.  Ouvrez `dashboard_prospects.html` pour voir le résultat à jour.
