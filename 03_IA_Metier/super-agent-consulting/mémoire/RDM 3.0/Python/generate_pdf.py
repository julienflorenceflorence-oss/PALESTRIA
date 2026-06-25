import os
import asyncio
import sys
from datetime import datetime

# Tentative d'import de Playwright
try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Erreur : La bibliothèque 'playwright' n'est pas installée.")
    print("Veuillez exécuter : pip install playwright && playwright install chromium")
    sys.exit(1)

async def generate_rdm_pdf():
    """
    Génère le PDF du Rapport de Mission avec un rendu Chromium haute fidélité.
    Respecte l'esthétique 'Édition Prestige' et la nomenclature Rocket School.
    """
    
    # --- CONFIGURATION ---
    PROMOTION = "A150" # À ajuster selon votre promotion
    NOM_COMPLET = "Julien Florence"
    
    FILE_NAME_HTML = "RAPPORT_DE_MISSION_ULTRA_PRESTIGE.html"
    FILE_NAME_PDF = f"Rapport de mission - {PROMOTION} - {NOM_COMPLET}.pdf"
    
    # Récupération des chemins absolus
    base_path = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.normpath(os.path.join(base_path, "..", "HTML", "RAPPORT_DE_MISSION_SOUTENANCE.html"))
    pdf_path = os.path.normpath(os.path.join(base_path, "..", "PDF", "Rapport_de_mission_Julien_Florence.pdf"))

    if not os.path.exists(html_path):
        print(f"Erreur : Le fichier source {html_path} est introuvable.")
        return

    print(f"--- GÉNÉRATEUR PDF PRESTIGE (Rocket School) ---")
    print(f"[@] Source : {html_path}")
    print(f"[*] Traitement en cours...")

    async with async_playwright() as p:
        # Lancement du navigateur (headless)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        # Chargement du fichier HTML (avec protocole file:// pour les images locales)
        try:
            await page.goto(f"file://{html_path}", wait_until="networkidle")
            
            # Attente supplémentaire pour s'assurer que les polices Google Fonts sont chargées
            await page.wait_for_timeout(2000) 
            
            # Génération du PDF
            # On utilise les dimensions A4 exactes définies dans le CSS
            try:
                await page.pdf(
                    path=pdf_path,
                    format="A4",
                    print_background=True,
                    display_header_footer=False,
                    margin={
                        "top": "0mm",
                        "right": "0mm",
                        "bottom": "0mm",
                        "left": "0mm",
                    },
                    prefer_css_page_size=True # Important pour respecter @page { size: A4 }
                )
                print(f"[OK] Succès ! Le PDF a été généré avec succès.")
                print(f"[>] Sortie : {pdf_path}")
            except Exception as pdf_err:
                if "Permission denied" in str(pdf_err) or "lock" in str(pdf_err).lower() or "permission" in str(pdf_err).lower():
                    fallback_path = pdf_path.replace(".pdf", "_TEMP.pdf")
                    print(f"[WARNING] Le PDF principal est actuellement verrouillé (probablement ouvert dans Acrobat ou Chrome).")
                    print(f"[*] Tentative de génération sur le chemin alternatif : {fallback_path}")
                    await page.pdf(
                        path=fallback_path,
                        format="A4",
                        print_background=True,
                        display_header_footer=False,
                        margin={
                            "top": "0mm",
                            "right": "0mm",
                            "bottom": "0mm",
                            "left": "0mm",
                        },
                        prefer_css_page_size=True
                    )
                    print(f"[OK] Succès ! Le PDF alternatif a été généré.")
                    print(f"[>] Sortie temporaire : {fallback_path}")
                    print(f"[!] IMPORTANT : Veuillez fermer votre lecteur PDF pour permettre d'écraser le fichier principal.")
                else:
                    raise pdf_err
            
        except Exception as e:
            print(f"[X] Une erreur est survenue lors de la génération : {str(e)}")
            sys.exit(1)
        finally:
            await browser.close()

if __name__ == "__main__":
    # Exécution du script asynchrone
    try:
        asyncio.run(generate_rdm_pdf())
    except KeyboardInterrupt:
        print("\nArrêt par l'utilisateur.")
