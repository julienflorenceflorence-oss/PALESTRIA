# Configuration du Prestige Engine

Ce document définit comment personnaliser l'apparence et le type de document produit par le moteur.

## 1. Palettes de Couleurs (Themes)

Le moteur utilise des variables CSS. Voici les thèmes recommandés :

| Thème | Background (`--bg`) | Accent (`--accent`) | Hover/Glow (`--glow`) |
| :--- | :--- | :--- | :--- |
| **Prestige Gold** | `#0F1115` | `#D4AF37` | `#F7EF8A` |
| **Questia Cyber** | `#05070d` | `#00e5ff` | `#b8ff3d` |
| **Cyber Blue** | `#050505` | `#00D2FF` | `#00FFFF` |
| **Emerald Royal** | `#0A120D` | `#50C878` | `#A7F3D0` |
| **Onyx Red** | `#0D0D0D` | `#E74C3C` | `#FF7675` |

## 2. Détails Questia (Questia Details)
Pour le projet Questia, respecter ces nuances :
- **Panneaux (`--card-bg`)** : `#0a0e18`
- **Texte Principal** : `#eef1f7`
- **Texte Secondaire** : `#8a93a8`
- **Alertes / Corail** : `#ff5a6a`
- **Police Signature** : `Bricolage Grotesque` (remplace Montserrat pour ce projet).

## 2. Types de Missions (Layouts)

### A. Portfolio Digital (`layout-portfolio.html`)
- **Usage** : Présentation interactive, liens vers des pièces jointes.
- **Structure** : Grille de cartes (Cards) avec effets de survol.
- **Navigation** : Dock mobile fixe avec boutons d'action.

### B. Rapport / Mémoire A4 (`layout-a4.html`)
- **Usage** : Documents longs, contrats, thèses.
- **Structure** : Pages successives (210x297mm) avec bordures intérieures.
- **Pagination** : Automatique en bas de page (P. 01, P. 02...).

### C. Signature & Mini-Doc
- **Usage** : E-mails, petites fiches techniques.
- **Structure** : Mono-bloc compact, focus sur la typographie.

## 3. Variables de Contenu
Le moteur doit être capable d'injecter :
- `{{title}}` : Titre principal (Font: Cinzel).
- `{{subtitle}}` : Slogan ou catégorie.
- `{{content}}` : Corps du document (Font: Montserrat).
- `{{footer_left}}` : Texte à gauche du footer (ex: Nom de section).
- `{{footer_right}}` : Texte à droite ou numéro de page.
