# Guide de Configuration : Synchronisation Google Docs CLI

Ce guide vous explique comment connecter votre environnement local à Google Docs en utilisant le CLI `@googleworkspace/cli`.

## 1. Installation du CLI

Exécutez la commande suivante dans votre terminal (PowerShell) :

```powershell
npm install -g @googleworkspace/cli
```

*Note : Si vous rencontrez une erreur de permission, ouvrez PowerShell en mode Administrateur.*

## 2. Configuration sur Google Cloud Console

Pour que le CLI puisse accéder à vos documents, vous devez créer un "projet" sur Google Cloud :

1. Allez sur [Google Cloud Console](https://console.cloud.google.com/).
2. Créez un nouveau projet (ex: "Mon Projet Documents").
3. Activez les APIs suivantes :
   - **Google Docs API**
   - **Google Drive API**
4. Configurez l'**Écran de consentement OAuth** :
   - Type : Externe.
   - Ajoutez votre propre email dans "Test users".
5. Créez des **Identifiants** :
   - Cliquez sur "Créer des identifiants" > **ID client OAuth**.
   - Type d'application : **Application de bureau**.
   - Téléchargez le fichier JSON et enregistrez-le sous le nom `credentials.json` dans ce dossier.

## 3. Authentification

Une fois le fichier `credentials.json` en place, exécutez :

```powershell
gws auth setup --credentials credentials.json
gws auth login
```

Une fenêtre de navigateur s'ouvrira pour vous demander d'autoriser l'accès.

## 4. Utilisation

Vous pourrez ensuite synchroniser vos fichiers. Par exemple, pour transformer un fichier Markdown local en Google Doc :

```powershell
gws docs create --title "Mon Mémoire" --from "memoire/Mémoire bachelor.md"
```

---
*Besoin d'aide pour une commande spécifique ? Demandez-moi !*
