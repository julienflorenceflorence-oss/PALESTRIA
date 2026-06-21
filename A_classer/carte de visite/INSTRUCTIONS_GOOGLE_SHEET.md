# Configuration de votre Google Sheet

Pour que votre carte de visite fonctionne, vous devez créer un Google Sheet et y configurer deux onglets.

## 1. Création du Google Sheet
1. Allez sur [Google Sheets](https://sheets.google.com/) et créez un nouveau document.
2. Donnez-lui un nom (ex: "Ma Carte de Visite").
3. **Récupérez l'ID du document** : Il se trouve dans l'URL, entre `/d/` et `/edit`.
   * *Exemple :* `https://docs.google.com/spreadsheets/d/1ABC_123_XYZ/edit` -> l'ID est `1ABC_123_XYZ`.

## 2. Configuration des onglets

### Onglet "Config"
Renommez la première feuille en **`Config`** et remplissez-la comme suit :

| Paramètre | Valeur |
| :--- | :--- |
| Nom | Julien FLORENCE |
| Poste | Directeur du développement commercial |
| Entreprise | CERCLE ORIGINE / Happy House |
| Mobile | 06 61 74 75 73 |
| Email | [VOTRE EMAIL] |
| Site_Web | https://www.my-happy.house/ |
| LinkedIn | https://www.linkedin.com/in/julien-florence-2536a083/ |
| Photo_URL | [LIEN DE VOTRE PHOTO] |
| Bio | Co-fondateur & Président - Stratégie Réseau & Développement |

### Onglet "Tracking"
Créez un deuxième onglet nommé **`Tracking`**. Laissez la première ligne pour les entêtes :
`Date | Heure | Appareil | Action`

## 3. Mise à jour du code
1. Ouvrez votre projet **Google Apps Script**.
2. Dans le fichier `Code.gs`, remplacez `'VOTRE_ID_GOOGLE_SHEET_ICI'` par l'ID que vous avez récupéré à l'étape 1.
3. Cliquez sur **Déployer > Nouveau déploiement**.
4. Sélectionnez **Application Web**.
5. Exécuter en tant que : **Moi**.
6. Qui a accès : **Tout le monde**.
7. Copiez l'URL de déploiement et mettez-la à jour dans votre fichier `GENERER_MON_QR_CODE.html`.
