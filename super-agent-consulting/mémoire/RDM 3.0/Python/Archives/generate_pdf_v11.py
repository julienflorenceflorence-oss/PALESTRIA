import os
import asyncio
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Erreur : La bibliothèque 'playwright' n'est pas installée.")
    sys.exit(1)

async def generate_rdm_pdf():
    PROMOTION = "A150"
    NOM_COMPLET = "Julien Florence"

    FILE_NAME_HTML = "RAPPORT_DE_MISSION_V11_SOUTENANCE.html"
    FILE_NAME_PDF = f"Rapport de mission V11 SOUTENANCE - {PROMOTION} - {NOM_COMPLET}.pdf"

    base_path = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base_path, FILE_NAME_HTML)
    pdf_path = os.path.join(base_path, FILE_NAME_PDF)

    if not os.path.exists(html_path):
        print(f"Erreur : Le fichier source {FILE_NAME_HTML} est introuvable")
        return

    print(f"--- GÉNÉRATEUR PDF V11 SOUTENANCE ---")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        try:
            await page.goto(f"file://{html_path}", wait_until="networkidle")
            await page.wait_for_timeout(2000)

            await page.pdf(
                path=pdf_path,
                format="A4",
                print_background=True,
                display_header_footer=False,
                margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"},
                prefer_css_page_size=True
            )
            print(f"[✓] Succès ! Le PDF a été généré avec succès : {FILE_NAME_PDF}")

        except Exception as e:
            print(f"[X] Erreur lors de la génération : {str(e)}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(generate_rdm_pdf())
