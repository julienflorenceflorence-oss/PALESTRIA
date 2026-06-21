import pandas as pd

# 1. Création de la Dimension Région Viticole (D_RegionViticole)
referentiel_data = [
    [31, "Haute-Garonne", "Sud-Ouest", "Vignoble du Sud-Ouest", "Bassin Garonnais (Fronton)"],
    [81, "Tarn", "Sud-Ouest", "Vignoble du Sud-Ouest", "Bassin Garonnais (Gaillac)"],
    [82, "Tarn-et-Garonne", "Sud-Ouest", "Vignoble du Sud-Ouest", "Bassin Garonnais"],
    [11, "Aude", "Languedoc-Roussillon", "Vignoble du Languedoc", "Bassin Languedoc"],
    [30, "Gard", "Languedoc-Roussillon", "Vignoble du Languedoc", "Bassin Rhodanien/Languedoc"],
    [34, "Herault", "Languedoc-Roussillon", "Vignoble du Languedoc", "Bassin Languedoc"],
    [66, "Pyrenees-Orientales", "Languedoc-Roussillon", "Vignoble du Roussillon", "Bassin Roussillon"],
    [32, "Gers", "Sud-Ouest", "Vignoble du Sud-Ouest", "Gascogne"],
    [46, "Lot", "Sud-Ouest", "Vignoble du Sud-Ouest", "Quercy/Cahors"],
]

df_referentiel = pd.DataFrame(referentiel_data, columns=["Departement", "DepartementNom", "BassinViticole", "RegionViticole", "SousZone"])

# 2. Création de données fictives pour l'exemple (F_VentesVrac)
ventes_data = [
    ["2023-2024", 31, "AOP", "Rosé", "Non", 1500, 115],
    ["2023-2024", 81, "AOP", "Rouge", "Non", 2200, 105],
    ["2023-2024", 34, "IGP", "Blanc", "Oui", 8500, 95],
    ["2024-2025", 31, "AOP", "Rosé", "Non", 1350, 122],
    ["2024-2025", 34, "IGP", "Blanc", "Oui", 8100, 98],
    ["2024-2025", 66, "AOP", "Rouge", "Non", 1200, 145],
]

df_ventes = pd.DataFrame(ventes_data, columns=["Campagne", "Departement", "TypeProduit", "Couleur", "Bio", "Volume_hl", "Prix_EUR_hl"])

# Ajout d'une colonne calculée CA
df_ventes["CA_Potentiel_EUR"] = df_ventes["Volume_hl"] * df_ventes["Prix_EUR_hl"]

# 3. Exportation vers le fichier Excel final
file_path = "Master_Viticole_Analyses.xlsx"

with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
    df_ventes.to_excel(writer, sheet_name="F_VentesVrac", index=False)
    df_referentiel.to_excel(writer, sheet_name="D_RegionViticole", index=False)

print(f"--- Fichier généré avec succès : {file_path} ---")
