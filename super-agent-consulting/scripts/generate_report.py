import os
import json

def generate_prestige_report(json_data_path, accent_color="#D4AF37", output_path="audit_palestria_prestige.html"):
    """
    Charge les données JSON, les injecte dans le template Master Audit et personnalise les couleurs.
    """
    template_path = os.path.join("templates", "template_master_audit.html")
    
    # Lecture des données
    with open(json_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Lecture du template
    if not os.path.exists(template_path):
        print(f"Erreur : Template non trouvé à {template_path}")
        return

    with open(template_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Remplacement dynamique de la couleur d'accentuation principale
    html_content = html_content.replace("--accent-color: #D4AF37;", f"--accent-color: {accent_color};")
    
    # Injection des données textuelles
    for key, value in data.items():
        placeholder = f"{{{{ {key} }}}}"
        html_content = html_content.replace(placeholder, str(value))

    # Sauvegarde du résultat
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Rapport généré avec succès : {output_path}")
    return output_path

if __name__ == "__main__":
    # Test avec Palestria
    json_path = os.path.join("scripts", "data_palestria.json")
    generate_prestige_report(json_path, accent_color="#D19A02") # Jaune I pour Palestria
