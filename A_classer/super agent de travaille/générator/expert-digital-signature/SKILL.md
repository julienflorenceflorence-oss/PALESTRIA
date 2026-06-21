---
name: expert-digital-signature
description: Crée des signatures e-mail professionnelles haut de gamme "Expert Digital & Stratégie". Utilise ce skill pour générer des signatures HTML respectant les codes de l'IA, du marketing digital et du ROI (bleu cyan, noir anthracite, design épuré).
---

# Expert Digital Signature

## Overview
Ce skill permet de générer des signatures e-mail HTML optimisées pour les experts en marketing digital et stratégie. Elle incarne le concept de "l'humain augmenté" avec un design épuré, technique et orienté vers la performance (ROI).

## Guidelines & Specifications

### 1. Vision Artistique
- **Précision Technique** : Design minimaliste, utilisation généreuse de l'espace vide (White Space).
- **Impact Visuel** : Accents Bleu Cyan contrastant avec un texte Noir Anthracite.

### 2. Palette & Typographie
- **Bleu Cyan (#00E5FF)** : Liens, barre de séparation, boutons CTA.
- **Noir Anthracite (#212121)** : Nom et texte principal.
- **Police** : Montserrat (ou Arial en fallback), Sans-Serif moderne.

### 3. Principes UX Appliqués
- **Loi de Hick** : Options limitées au strict nécessaire (LinkedIn, Portfolio).
- **Loi de Fitts** : Zone de clic large pour le bouton d'action principal.
- **UX Writing** : Voix active centrée sur les résultats ("Transformer les budgets en croissance").

## Usage Workflow

1. **Collecte des données** : Demandez à l'utilisateur son Nom, son Titre (ex: Expert Ads), son Téléphone et ses liens (LinkedIn/Portfolio).
2. **Génération HTML** : Utilisez le template situé dans `assets/template.html`.
3. **Remplacement des placeholders** :
    - `[[NAME]]` : Prénom NOM
    - `[[JOB_TITLE]]` : Titre métier
    - `[[PHONE]]` : Format lisible (ex: +33 6 12 34 56 78)
    - `[[PHONE_LINK]]` : Format tel (ex: +33612345678)
    - `[[LINKEDIN_URL]]` : Lien profil LinkedIn
    - `[[PORTFOLIO_URL]]` : Lien vers les analyses ou portfolio

## Resources

- **Requirements** : Voir `references/requirements.md` pour le cahier des charges détaillé.
- **Template** : Voir `assets/template.html` pour la structure HTML/CSS de base.
