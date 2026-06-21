# Documentation Technique : Architecture CV Prestige

Ce document détaille la structure et les mécaniques du projet pour permettre une duplication parfaite avec de nouveaux contenus.

## 1. Architecture des Fichiers
*   `index.html` : Page principale (CV). Gère l'ordre d'affichage spécifique (Photo > Nom > Résumé).
*   `diplomes.html` : Portfolio de compétences. Gère le Dock Premium et la grille adaptative.
*   `CONTRANTES_CV.md` : La charte graphique et technique (Loi du projet).

## 2. Design System (Édition Prestige)
*   **Contraintes Visuelles** :
    *   `border-radius: 10px` : Appliqué à TOUT (Cartes, Boutons, Photo).
    *   `border: 2px solid #D4AF37` : Pour les éléments d'action (CTA).
    *   `background: #0F1115` : Fond noir profond.
*   **Typographies** :
    *   `Cinzel` : Titres, Boutons, Dates (Identité Luxe).
    *   `Montserrat` : Corps de texte (Lisibilité Tech).

## 3. Mécaniques Mobiles (Le Savoir-Faire)
### A. Verrouillage Portrait Intelligent
Utilise une requête média combinant orientation et type de pointeur pour ne bloquer que les mobiles/tablettes :
```css
@media screen and (orientation: landscape) and (max-width: 1024px) and (pointer: coarse) {
    body::before { /* Overlay de blocage */ }
    .container { display: none !important; }
}
```

### B. Le Dock Flottant (diplomes.html)
Pour éviter le "clipping" (cadre coupé par le navigateur), le dock est décollé du bord :
```css
.fixed-dock {
    position: fixed;
    bottom: 25px; /* Décollage critique */
    border-radius: 10px;
    padding-bottom: calc(15px + env(safe-area-inset-bottom)); /* Sécurité iPhone */
}
```

### C. Dégagement du contenu (Scroll)
Un espaceur physique en fin de page garantit que le dernier texte (Copyright) remonte au-dessus des boutons :
```css
.mobile-spacer { height: 350px; display: block; }
```

## 4. Guide de Modification (Pour un nouveau CV)
1.  **Dates** : Utiliser uniquement l'année (`YYYY`) ou `YYYY – Présent`.
2.  **Missions** : Utiliser des listes `<ul>` avec des puces Or (`•`).
3.  **Ordre Mobile** : Dans le CSS de `index.html`, ajuster les propriétés `order` (1: Photo, 2: Header, 3: Qui suis-je, 4: Expériences).
4.  **CTA Unique** : Placer le bouton `Portefolio` (classe `btn-mini-portfolio`) physiquement après le cadre de la certification la plus importante.

## 5. Déploiement
*   **GitHub Pages** : Le dossier `PROJET_CV` est le dossier de travail Git.
*   **Commande de mise à jour** : `git add . ; git commit -m "update" ; git push origin main --force`
