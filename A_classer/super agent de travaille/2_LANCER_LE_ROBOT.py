import asyncio
from playwright.async_api import async_playwright
import os

# CONFIGURATION
URL_CLASSE = "https://my.apolearn.com/classroom/4784619"
EMAIL = "VOTRE_EMAIL" 
PASSWORD = "VOTRE_MOT_DE_PASSE"
DOSSIER_DESTINATION = "./Archives_Apolearn_4784619"

async def run_autowork():
    async with async_playwright() as p:
        print(f"[1/4] Lancement du navigateur...")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()

        print(f" -> Navigation vers : {URL_CLASSE}")
        await page.goto(URL_CLASSE)
        
        try:
            print(" -> Tentative de connexion automatique...")
            await page.wait_for_selector("input", timeout=10000)
            inputs = await page.locator("input").all()
            for i in inputs:
                type_attr = await i.get_attribute("type")
                if type_attr == "email" or type_attr == "text": await i.fill(EMAIL)
                if type_attr == "password": await i.fill(PASSWORD)
            await page.keyboard.press("Enter")
        except:
            print("\n⚠️ MERCI DE VOUS CONNECTER MANUELLEMENT DANS LE NAVIGATEUR...")

        # ATTENTE DE CONNEXION
        while True:
            if "classroom/4784619" in page.url:
                print(f"\n✅ CONNEXION DÉTECTÉE ! Début de la recherche AGRESSIVE...")
                break
            await asyncio.sleep(2)

        if not os.path.exists(DOSSIER_DESTINATION): os.makedirs(DOSSIER_DESTINATION)

        print(f"[3/4] Scan profond des documents...")
        await page.wait_for_timeout(5000) # On attend que la page soit vraiment chargée
        
        # ON CHERCHE ABSOLUMENT TOUT CE QUI RESSEMBLE À UN LIEN OU UN BOUTON DE RESSOURCE
        # On cible les liens avec "download", "resource", "file", "pdf", etc.
        all_elements = await page.locator("a, button, .resource-item, .file-item").all()
        to_download = []
        
        for el in all_elements:
            try:
                text = await el.inner_text()
                href = await el.get_attribute("href")
                # Filtre agressif sur le texte ou l'adresse
                if href and ("/download/" in href or "/resource/" in href or "/file/" in href or ".pdf" in href or "/view/" in href):
                    to_download.append(el)
                elif text and any(ext in text.lower() for ext in [".pdf", ".zip", ".docx", ".pptx", "télécharger", "download"]):
                    to_download.append(el)
            except: continue

        # On enlève les doublons
        to_download = list(dict.fromkeys(to_download))

        print(f"[4/4] {len(to_download)} ressources potentielles identifiées. Extraction en cours...")
        
        for i, el in enumerate(to_download):
            try:
                # On essaie de cliquer pour déclencher le téléchargement
                async with page.expect_download(timeout=5000) as download_info:
                    await el.click(force=True)
                download = await download_info.value
                file_path = os.path.join(DOSSIER_DESTINATION, download.suggested_filename)
                await download.save_as(file_path)
                print(f" ✅ [{i+1}/{len(to_download)}] Téléchargé : {download.suggested_filename}")
            except:
                continue

        print(f"\n🏆 TRAVAIL TERMINÉ ! Fichiers sauvegardés dans : {DOSSIER_DESTINATION}")
        input("Appuyez sur Entrée pour quitter...")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_autowork())
