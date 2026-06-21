import json
import os

def update_report():
    # 1. Charger les données JSON
    try:
        with open('data_viti_france_2026.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Erreur : Le fichier JSON 'data_viti_france_2026.json' est introuvable.")
        return

    # 2. Charger le Template HTML
    try:
        with open('Template_Rapport_Viticole.html', 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print("Erreur : Le fichier Template 'Template_Rapport_Viticole.html' est introuvable.")
        return

    # 3. Préparer les blocs régionaux dynamiquement
    region_blocks_html = ""
    for key, info in data['regions'].items():
        block = f"""
        <div class="region-block">
            <span class="tag tag-{info['tag']}">{info['title']}</span>
            <h3>{info['title']}</h3>
            <p><strong>Prix :</strong> {info['price']} | <strong>Volume :</strong> {info['vol']}</p>
            <ul>
                <li><strong>Observation :</strong> {info['insight']}</li>
            </ul>
        </div>
        """
        region_blocks_html += block

    # 4. Remplacer les placeholders
    replacements = {
        "{{REF}}": data['meta']['ref'],
        "{{EDITION}}": data['meta']['edition'],
        "{{DATE_EDITION}}": data['meta']['date_edition'],
        "{{VOL_TOTAL}}": data['kpis']['vol_total'],
        "{{TREND_RED}}": data['kpis']['trend_red'],
        "{{TREND_CREMANT}}": data['kpis']['trend_cremant'],
        "{{PRICE_MIN_BX}}": data['kpis']['price_min_bx'],
        "{{REGION_BLOCKS}}": region_blocks_html
    }

    final_html = template
    for key, value in replacements.items():
        final_html = final_html.replace(key, value)

    # 5. Sauvegarder le rapport final
    output_path = 'Rapport_Viticole_Chirurgical.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"✅ Rapport mis à jour avec succès : {output_path}")

if __name__ == "__main__":
    update_report()
