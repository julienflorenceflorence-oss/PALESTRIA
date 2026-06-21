# Guide de Style Prestige

Ce document définit les standards visuels pour toute la gamme de documents "Prestige".

## Palette de Couleurs

| Élément | Code Hex | Description |
| :--- | :--- | :--- |
| **Fond Principal** | `#0F1115` | Noir prestige profond |
| **Arrière-plan Carte** | `#161a23` | Gris anthracite sombre |
| **Or Signature** | `#D4AF37` | Couleur principale des accents |
| **Or Clair** | `#F7EF8A` | Pour les effets de brillance |
| **Or Sombre** | `#8A6426` | Pour la profondeur des dégradés |
| **Texte Principal** | `#F4F4F4` | Blanc cassé doux |
| **Texte Secondaire**| `#B0B0B0` | Gris argenté pour les descriptions |

## Typographie

1. **Titres et En-têtes** : `Cinzel`, serif. Majuscules systématiques, letter-spacing important (3-6px).
2. **Corps de texte** : `Montserrat`, sans-serif. Poids léger (300) pour l'élégance, gras (700) pour l'emphase.

## Composants UI

### Cartes (Cards)
- **Bordure** : `1px solid rgba(212, 175, 55, 0.15)`.
- **Radius** : `10px`.
- **Effet Hover** : Translation verticale de `-10px`, bordure or pleine, ombre portée profonde.
- **Effet Visited** : Boutons "Consulter" passant en or plein après clic (via `localStorage`).

### Dock Mobile
- **Position** : `fixed`, bottom.
- **Flou** : `backdrop-filter: blur(15px)`.
- **Contrainte** : Doit contenir un bouton de retour au menu principal et un CTA (Appel à l'action).

## Règles de mise en page
- **A4 Digital** : Les documents doivent être pensés comme des pages de magazine de luxe.
- **Zéro Scroll** : En mode visionneuse, le document doit tenir dans le `viewport` (`object-fit: contain`).
