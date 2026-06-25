import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdf():
    # Chemins des fichiers
    html_input = os.path.abspath(r'mémoire/RDM 3.0/RDM_FINAL_PRO_2026.html')
    pdf_output = os.path.abspath(r'mémoire/RDM 3.0/Rapport_de_mission_Apollo_1_Julien_Florence.pdf')

    print(f"--- Démarrage de la génération PDF ---")
    
    async with async_playwright() as p:
        # Lancement du navigateur (Chromium)
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Chargement du fichier HTML avec attente de fin de chargement
        print(f"Chargement du fichier : {html_input}")
        await page.goto(f"file://{html_input}", wait_until="load")
        
        # Petit délai de sécurité pour laisser le temps aux polices Google de s'appliquer
        await asyncio.sleep(2)

        # Génération du PDF avec les contraintes académiques
        print("Conversion en cours...")
        await page.pdf(
            path=pdf_output,
            format="A4",
            print_background=True,  # Crucial pour garder le fond Onyx et Or
            margin={
                "top": "0mm",
                "bottom": "0mm",
                "left": "0mm",
                "right": "0mm"
            },
            display_header_footer=False,
            prefer_css_page_size=True
        )

        await browser.close()
    
    print(f"--- Succès ! PDF généré ici : {pdf_output} ---")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
