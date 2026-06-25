import os
import sys
import re
import shutil
import subprocess

def main():
    print("=== PIPELINE DE ROTATION DE VERSION & COMPILATION ===")
    
    # Configuration des dossiers
    base_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.normpath(os.path.join(base_path, ".."))
    
    html_dir = os.path.join(project_path, "HTML")
    pdf_dir = os.path.join(project_path, "PDF")
    
    html_archive_dir = os.path.join(html_dir, "Archives")
    pdf_archive_dir = os.path.join(pdf_dir, "Archives")
    
    # 1. Détection automatique de la version actuelle
    # On scanne les dossiers Archives pour trouver le numéro de version le plus élevé
    max_ver = 0
    version_regex = re.compile(r"V(\d+)", re.IGNORECASE)
    
    if os.path.exists(html_archive_dir):
        for f in os.listdir(html_archive_dir):
            m = version_regex.search(f)
            if m:
                max_ver = max(max_ver, int(m.group(1)))
                
    if os.path.exists(pdf_archive_dir):
        for f in os.listdir(pdf_archive_dir):
            m = version_regex.search(f)
            if m:
                max_ver = max(max_ver, int(m.group(1)))
                
    if max_ver == 0:
        # Valeur par défaut si rien n'est trouvé dans les archives
        max_ver = 14
        
    current_ver_num = max_ver
    new_ver_num = current_ver_num + 1
    
    # Permet de surcharger via argument de ligne de commande
    if len(sys.argv) > 1:
        arg = sys.argv[1].upper().replace("V", "")
        if arg.isdigit():
            new_ver_num = int(arg)
            current_ver_num = new_ver_num - 1
            print(f"[Info] Version forcée par l'utilisateur : V{new_ver_num}")
            
    current_ver = f"V{current_ver_num}"
    new_ver = f"V{new_ver_num}"
    
    print(f"[*] Version actuelle identifiée : {current_ver}")
    print(f"[*] Nouvelle version à compiler : {new_ver}")
    
    # Fichiers actifs actuels
    active_html = os.path.join(html_dir, "RAPPORT_DE_MISSION_SOUTENANCE.html")
    active_pdf = os.path.join(pdf_dir, "Rapport_de_mission_Julien_Florence.pdf")
    
    # Chemins cibles d'archivage (avec suffixe de version)
    archive_html_name = f"RAPPORT_DE_MISSION_{current_ver}_SOUTENANCE.html"
    archive_pdf_name = f"Rapport de mission {current_ver} SOUTENANCE - A150 - Julien Florence.pdf"
    
    target_archive_html = os.path.join(html_archive_dir, archive_html_name)
    target_archive_pdf = os.path.join(pdf_archive_dir, archive_pdf_name)
    
    # 2. Rotation : Archivage des fichiers actifs actuels
    print("\n--- ÉTAPE 1 : ROTATION DES VERSIONS ---")
    
    if os.path.exists(active_html):
        print(f"[*] Archivage de l'HTML actif vers : HTML/Archives/{archive_html_name}")
        os.makedirs(html_archive_dir, exist_ok=True)
        shutil.copy2(active_html, target_archive_html)
        print("[OK] HTML archivé avec succès.")
    else:
        print("[!] Aucun fichier HTML actif trouvé à archiver. La compilation générera le premier.")
        
    if os.path.exists(active_pdf):
        print(f"[*] Archivage du PDF actif vers : PDF/Archives/{archive_pdf_name}")
        os.makedirs(pdf_archive_dir, exist_ok=True)
        shutil.copy2(active_pdf, target_archive_pdf)
        print("[OK] PDF archivé avec succès.")
    else:
        print("[!] Aucun fichier PDF actif trouvé à archiver. La compilation générera le premier.")
        
    # 3. Compilation : Génération des nouveaux fichiers actifs
    print("\n--- ÉTAPE 2 : COMPILATION ---")
    
    # Exécution de build_rdm_soutenance.py
    build_script = os.path.join(base_path, "build_rdm_soutenance.py")
    if os.path.exists(build_script):
        print("[*] Exécution du constructeur HTML (build_rdm_soutenance.py)...")
        try:
            subprocess.run([sys.executable, build_script], check=True)
            print("[OK] Génération HTML terminée.")
        except subprocess.CalledProcessError as e:
            print(f"[ERREUR] Échec du constructeur HTML. Code de sortie: {e.returncode}")
            sys.exit(1)
    else:
        print(f"[ERREUR] Le script de construction {build_script} est introuvable.")
        sys.exit(1)
        
    # Exécution de generate_pdf.py
    pdf_script = os.path.join(base_path, "generate_pdf.py")
    if os.path.exists(pdf_script):
        print("[*] Exécution du générateur PDF (generate_pdf.py)...")
        try:
            # Playwright nécessite souvent un environnement asynchrone, generate_pdf.py le gère en interne.
            subprocess.run([sys.executable, pdf_script], check=True)
            print("[OK] Génération PDF terminée.")
        except subprocess.CalledProcessError as e:
            print(f"[ERREUR] Échec du générateur PDF. Code de sortie: {e.returncode}")
            sys.exit(1)
    else:
        print(f"[ERREUR] Le script de génération PDF {pdf_script} est introuvable.")
        sys.exit(1)
        
    # 4. Vérification finale
    print("\n--- ÉTAPE 3 : VÉRIFICATION ---")
    html_ok = os.path.exists(active_html)
    pdf_ok = os.path.exists(active_pdf)
    
    if html_ok and pdf_ok:
        print(f"[OK] Le pipeline a réussi !")
        print(f"      - Nouveau fichier HTML actif : HTML/RAPPORT_DE_MISSION_SOUTENANCE.html")
        print(f"      - Nouveau fichier PDF actif  : PDF/Rapport_de_mission_Julien_Florence.pdf")
        print(f"      - Ancienne version archivée sous : {current_ver}")
    else:
        if not html_ok:
            print("[ERREUR] Le fichier HTML actif n'a pas été généré.")
        if not pdf_ok:
            print("[ERREUR] Le fichier PDF actif n'a pas été généré.")
        sys.exit(1)

if __name__ == "__main__":
    main()
