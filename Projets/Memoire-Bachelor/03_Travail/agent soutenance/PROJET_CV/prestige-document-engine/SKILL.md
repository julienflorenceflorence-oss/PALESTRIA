---
name: prestige-document-engine
description: Moteur de génération de documents ultra-premium et technologiques. Permet de dupliquer l'esthétique "Édition Prestige" (Noir/Or ou thèmes personnalisés) pour des portfolios, rapports A4, ou contrats, avec navigation intelligente et design haute fidélité.
---

# Prestige Document Engine

Ce skill transforme n'importe quel contenu (CV, Rapport, Contrat, Portfolio) en un document d'exception respectant les codes du luxe et de la tech.

## Capacités Clés

1.  **Thématisation Flexible** : Supporte plusieurs palettes (Gold, Cyber Blue, Emerald, Onyx) via des variables CSS définies dans [references/config-schema.md](references/config-schema.md).
2.  **Double Moteur de Rendu** :
    *   **Layout Portfolio** (`assets/layout-portfolio.html`) : Grille de cartes interactives pour le web et mobile.
    *   **Layout A4 Prestige** (`assets/layout-a4.html`) : Format document pour impression ou PDF haute qualité avec bordures et pagination.
3.  **Composants de Précision** : Boutons avec dégradés, effets de survol magnétiques, et visionneuse de documents intégrée.

## Workflow d'Utilisation

### 1. Définition de la Mission
Identifier le type de document souhaité :
*   Portfolio/Présentation -> `assets/layout-portfolio.html`
*   Rapport/Mémoire/Contrat -> `assets/layout-a4.html`

### 2. Choix du Thème
Sélectionner une palette dans le schéma de configuration. Par défaut, le thème **Prestige Gold** est appliqué.

### 3. Génération du Contenu
Extraire les données et les injecter dans le template. Pour les portfolios, veiller à attribuer des IDs uniques aux cartes pour assurer le fonctionnement du système d'ancres.

## Directives de Design Mandatoires

*   **Typographie** : Titres en `Cinzel` (Majuscules), Corps en `Montserrat`.
*   **Navigation Mobile** : Toujours inclure le dock de navigation en bas d'écran et le script de blocage paysage pour garantir l'expérience utilisateur.
*   **Finitions** : Utiliser des bordures de 1px avec une opacité réduite pour un rendu élégant et professionnel.
