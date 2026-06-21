## **1\. La Source de Vérité (Le Tableau de Bord)**

Créez un Google Sheet avec deux onglets :

* **Onglet `Config` :** Un tableau simple avec deux colonnes : `Paramètre` | `Valeur`.  
  * *Exemple :* `Nom` | `Jean Dupont`, `Poste` | `Directeur`, `Photo_URL` | `[Lien Drive]`.  
* **Onglet `Tracking` :** Pour enregistrer automatiquement chaque scan (Date, Heure, Appareil).

## **2\. Le Cœur du Système (Google Apps Script)**

Le script fera office de "cerveau" entre votre Google Sheet et la carte de visite. Il aura deux fonctions :

1. **`doGet()` :** Envoie les données du Sheet vers la carte de visite au format JSON.  
2. **`doPost()` :** Reçoit les notifications de scan pour alimenter l'onglet `Tracking`.

---

## **3\. Cahier des charges mis à jour (À copier pour l'IA)**

**Prompt pour Gemini CLI :**

"Génère une solution de carte de visite digitale dynamique avec les spécifications suivantes :

1. **Data Source :** Utilise un Google Sheet comme base de données pour le contenu (Nom, Tel, Email, Photo URL). Les modifications dans le Sheet doivent se refléter instantanément sur la carte sans toucher au code.  
2. **Frontend (HTML/JS) :** \> \* Interface mobile-first, élégante, avec un bouton 'Ajouter aux contacts'.  
   * Utilise `fetch()` pour récupérer les données depuis l'API Google Apps Script.  
   * Génère un fichier VCF à la volée en JavaScript incluant la photo (Base64).  
3. **Tracking :** Chaque ouverture de la page doit déclencher un log automatique (Timestamp \+ User-Agent) dans un onglet 'Tracking' du même Google Sheet via une requête POST.  
4. **Hébergement :** Le fichier HTML doit être optimisé pour être servi via Google Drive ou GitHub Pages.  
5. **Maintenabilité :** Commente le code pour que je puisse facilement changer les IDs du Google Sheet."

---

## **4\. Pourquoi cette méthode est la plus efficace pour vous ?**

* **Agilité :** Vous changez de poste ou de numéro ? Modifiez une cellule dans votre téléphone via l'app Google Sheets, et votre QR Code reste le même mais l'information est à jour.  
* **Analyse de Performance :** Votre onglet `Tracking` devient un véritable outil de mesure de votre prospection. Vous saurez exactement quand votre carte est consultée.  
* **Maîtrise :** Vous gardez la main sur l'outil sans dépendre d'un abonnement tiers (Linktree ou autre).

