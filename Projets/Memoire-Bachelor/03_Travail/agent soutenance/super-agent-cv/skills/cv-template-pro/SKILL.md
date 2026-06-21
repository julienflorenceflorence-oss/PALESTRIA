# Skill : CV Template Pro (Édition Prestige)

Ce skill transforme Gemini en un expert de la création de CV et Dossiers de Compétences haut de gamme.

## 🎨 Design System Impératif
- **Couleurs** : Fond #0F1115, Accents Or #D4AF37, Texte #F4F4F4.
- **Bordures** : `border-radius: 10px` sur TOUS les conteneurs et boutons.
- **Typographie** : 'Cinzel' (Titres/Action), 'Montserrat' (Contenu).

## 📱 Contraintes Mobiles (Prestige-Ready)
- **Orientation** : Blocage Landscape obligatoire pour les écrans < 13" avec overlay personnalisé.
- **Dock Mobile** : Boutons de bas de page flottants (décollés du bord de 25px) pour éviter le clipping navigateur.
- **Scroll Safety** : Toujours inclure un `.mobile-spacer` de 350px en fin de contenu.
- **Ordre d'affichage** : 1. Photo (arrondie 10px), 2. Identité, 3. Résumé/Qui suis-je, 4. Expériences.

## 📄 Structure du Code
- Utiliser uniquement du **HTML5 sémantique** et du **Vanilla CSS**.
- **Dates** : Format `YYYY` ou `YYYY – Présent` uniquement.
- **Bouton Portefolio** : Toujours placer le bouton "Portefolio" (classe `.btn-mini-portfolio`) physiquement sous le cadre de la certification majeure sur mobile.

## 🛠️ Instructions de Génération
Lorsqu'un utilisateur fournit un contenu brut (texte), le skill doit :
1. Structurer le contenu selon le modèle de `index.html` (CV) ou `diplomes.html` (Portfolio).
2. Appliquer les variables CSS de la charte.
3. Injecter les médias queries de blocage portrait intelligent.
