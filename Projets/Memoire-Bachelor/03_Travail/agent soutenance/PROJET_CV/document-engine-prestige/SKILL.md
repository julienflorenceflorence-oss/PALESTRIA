---
name: document-engine-prestige
description: Moteur de création de documents "Édition Prestige". Applique une identité visuelle luxueuse (Noir/Or) et des fonctionnalités UX avancées (visionneuse dynamique, ancres de retour, dock mobile) à n'importe quel contenu de communication.
---

# Document Engine Prestige

Ce skill transforme des contenus bruts en documents de communication haut de gamme, optimisés pour la lecture digitale et mobile.

## Principes Fondamentaux

- **Identité Visuelle Signature** : Fond `#0F1115`, accents `#D4AF37`, polices `Cinzel` et `Montserrat`.
- **Navigation Fluide** : Utilisation d'une visionneuse dynamique pour les pièces jointes et d'ancres pour le retour à la position exacte.
- **Rigueur Structurelle** : Organisation en "Cards" élégantes avec effets de survol interactifs.

## Workflows Spécifiques

### 1. Création d'un Document de Base
Pour générer une page de présentation ou un portfolio :
1. Utiliser le template `assets/index-template.html`.
2. Organiser le contenu en sections thématiques (`.grid`).
3. Appliquer les IDs uniques à chaque carte pour activer le système d'ancres.

### 2. Configuration de la Visionneuse
Pour permettre la consultation de documents externes (PDF/Images) :
1. Déployer `assets/viewer.html` à la racine.
2. Formater les liens comme suit : `viewer.html?file=PATH&title=TITLE&id=ANCHOR`.

### 3. Optimisation Mobile
1. Assurer la présence du `.fixed-dock` pour les actions principales.
2. Vérifier que le blocage d'orientation paysage est actif pour garantir le design.

## Références et Assets

- **Guide de Style Complet** : Voir [references/style-guide.md](references/style-guide.md) pour les codes CSS et les règles typographiques.
- **Template Visionneuse** : Utiliser `assets/viewer.html`.
- **Template Page Principale** : Utiliser `assets/index-template.html`.
