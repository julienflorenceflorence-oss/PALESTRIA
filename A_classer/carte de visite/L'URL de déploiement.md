L'**URL de déploiement**, c'est tout simplement l'**adresse web unique** (le lien) que Google génère pour votre carte de visite une fois que le code est prêt.

C'est ce lien que vous allez transformer en **QR Code**. Sans cette URL, votre carte de visite reste un projet "privé" sur votre compte ; une fois déployée, elle devient une application accessible par n'importe quel smartphone qui scanne votre code.

### **Où la trouver concrètement ?**

Après avoir collé le code dans l'éditeur **Google Apps Script**, suivez ces étapes précises :

1. Cliquez sur le gros bouton bleu **"Déployer"** (en haut à droite).  
2. Choisissez **"Nouveau déploiement"**.  
3. Cliquez sur l'icône "rouage" à côté de "Sélectionner un type" et choisissez **"Application Web"**.  
4. Remplissez les champs comme ceci :  
   * **Description :** Carte de visite digitale.  
   * **Exécuter en tant que :** Moi (votre adresse Gmail).  
   * **Qui a accès :** **Tout le monde** (C'est l'étape cruciale pour que vos prospects puissent voir la carte sans se connecter à Google).  
5. Cliquez sur **"Déployer"**.  
6. Une fenêtre s'ouvre avec un lien qui commence par `https://script.google.com/macros/s/.../exec`.

**C'est cela, votre URL de déploiement.**

