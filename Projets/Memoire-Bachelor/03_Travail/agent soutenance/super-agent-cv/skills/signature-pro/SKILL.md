# Skill : Signature & Template Pro (Logique Placeholders)

Ce skill permet à l'agent de générer du code HTML de diffusion (Email/Signature) ultra-compatible et personnalisable.

## 1. Structure de l'Agent IA (Logique de l'algorithme)
L'agent fonctionne par remplissage de balises (Placeholders). Il génère le code sans avoir besoin des informations finales :
- **Le Conteneur** : Un tableau HTML (`<table>`) de 500px à 600px de large, bordures à 0, pour garantir la compatibilité mobile.
- **La Grille (Layout)** :
    - **Zone A (Gauche)** : Emplacement Image (Logo ou Photo).
    - **Zone B (Droite)** : Bloc texte hiérarchisé.
    - **Zone C (Bas)** : Barre de boutons/réseaux sociaux.

## 2. Spécifications du Design (Modèle HHdir)
- **Typographie** : Polices système sécurisées (Arial, Verdana, Helvetica). Utiliser la variable `{{font_family}}`.
- **Hiérarchie visuelle** :
    - `{{Nom_Prenom}}` : Gras, taille 14px.
    - `{{Poste_Fonction}}` : Italique ou majuscules, taille 12px.
    - `{{Coordonnees}}` : Taille 11px, avec icônes discrètes.
- **Les Boutons (CTA)** : Cellules de tableau avec bords arrondis (`border-radius`) et couleur de fond variable `{{primary_color}}`.

## 3. Liste des "Placeholders" (Variables)
- `{{HEX_COLOR}}` : Couleur des boutons et traits.
- `{{IMAGE_URL}}` : Lien photo/logo hébergé (Cloud).
- `{{CALENDLY_LINK}}` : Lien de prise de rendez-vous.
- `{{SOCIAL_LINKS}}` : Liste d'URLs (LinkedIn, etc.).

## 4. Configuration Technique
- **Mode de sortie** : HTML Inline CSS uniquement (style directement dans les balises).
- **Optimisation Mobile** : Règle `display: block !important;` pour que la photo passe au-dessus du texte sur smartphone.
- **Zéro pièce jointe** : Avertissement obligatoire sur le stockage externe des images.
