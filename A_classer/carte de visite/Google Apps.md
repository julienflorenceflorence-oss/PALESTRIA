### **Étape 1 : Le Google Sheet (Votre Tableau de Contrôle)**

1. Créez un nouveau Google Sheet nommé "Ma Carte Digitale".  
2. **Onglet 1 (Nommé "Config")** : Créez deux colonnes : `Paramètre` et `Valeur`.  
   * Ligne 1 : `Nom` | `Votre Nom`  
   * Ligne 2 : `Poste` | `Négociateur Immobilier / Manager`  
   * Ligne 3 : `Tel` | `+33600000000`  
   * Ligne 4 : `Email` | `votre@email.com`  
   * Ligne 5 : `Photo_URL` | `[Lien de votre photo hébergée sur Drive]`  
3. **Onglet 2 (Nommé "Tracking")** : Laissez-le vide, le script s'en chargera.

### **Étape 2 : Le Code Google Apps Script (Le Backend)**

Dans votre Sheet, allez dans **Extensions \> Apps Script** et remplacez le code par celui-ci :

JavaScript  
function doGet() {  
  return HtmlService.createHtmlOutputFromFile('Index')  
    .setTitle("Ma Carte de Visite")  
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');  
}

// Fonction pour récupérer les infos du Sheet  
function getProfileData() {  
  var sheet \= SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Config");  
  var data \= sheet.getDataRange().getValues();  
  var profile \= {};  
  data.forEach(row \=\> { profile\[row\[0\]\] \= row\[1\]; });  
    
  // Log du scan dans l'onglet Tracking  
  var trackSheet \= SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Tracking");  
  trackSheet.appendRow(\[new Date(), "Scan détecté"\]);  
    
  return profile;  
}

### **Étape 3 : L'Interface (Le fichier Index.html)**

Dans l'éditeur Apps Script, cliquez sur le **\+** à côté de "Bibliothèques", choisissez "HTML" et nommez le fichier `Index`. Collez ce code :

HTML  
\<\!DOCTYPE html\>  
\<html\>  
\<head\>  
    \<style\>  
        body { font-family: 'Segoe UI', sans-serif; background: \#f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }  
        .card { background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; width: 300px; }  
        img { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid \#007bff; }  
        h2 { margin: 10px 0 5px; color: \#333; }  
        p { color: \#666; margin-bottom: 20px; }  
        .btn { background: \#007bff; color: white; border: none; padding: 12px 20px; border-radius: 5px; cursor: pointer; text-decoration: none; display: inline-block; font-weight: bold; }  
    \</style\>  
\</head\>  
\<body\>  
    \<div class="card" id="cardContent"\>  
        \<p\>Chargement...\</p\>  
    \</div\>

    \<script\>  
        google.script.run.withSuccessHandler(showCard).getProfileData();

        function showCard(data) {  
            const container \= document.getElementById('cardContent');  
            container.innerHTML \= \`  
                \<img src="${data.Photo\_URL}" alt="Photo"\>  
                \<h2\>${data.Nom}\</h2\>  
                \<p\>${data.Poste}\</p\>  
                \<button class="btn" onclick="downloadVCF('${data.Nom}', '${data.Tel}', '${data.Email}')"\>  
                    Ajouter au répertoire  
                \</button\>  
            \`;  
        }

        function downloadVCF(nom, tel, email) {  
            const vcard \= \`BEGIN:VCARD\\nVERSION:3.0\\nFN:${nom}\\nTEL:${tel}\\nEMAIL:${email}\\nEND:VCARD\`;  
            const blob \= new Blob(\[vcard\], { type: 'text/vcard' });  
            const url \= window.URL.createObjectURL(blob);  
            const a \= document.createElement('a');  
            a.href \= url;  
            a.download \= 'contact.vcf';  
            a.click();  
        }  
    \</script\>  
\</body\>  
\</html\>

### **Étape 4 : Déploiement (La mise en ligne)**

1. Dans Apps Script, cliquez sur **Déployer \> Nouveau déploiement**.  
2. Type : **Application Web**.  
3. Exécuter en tant que : **Moi**.  
4. Qui a accès : **Tout le monde** (important pour que le scan fonctionne sans connexion Google pour l'autre personne).  
5. Copiez l'URL fournie : **C'est le lien de votre carte.**

### **Pourquoi ce système répond parfaitement à vos critères :**

* **Facilité de modification** : Vous changez votre numéro ou votre titre directement dans le Google Sheet, et la carte se met à jour instantanément sans retoucher au code.  
* **Suivi (Tracking)** : Chaque fois que quelqu'un ouvre le lien, une ligne s'ajoute dans l'onglet "Tracking" avec la date et l'heure.  
* **Rapidité** : Le bouton génère un fichier `.vcf` standard lisible par tous les smartphones (iOS/Android).

