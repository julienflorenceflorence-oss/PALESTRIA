# 📅 To-Do List : Projet Agent IA Data Analyste

## 1. Rôles Humains Clés
*   **PO (Product Owner) :** Gère la vision métier et valide les sorties.
*   **PE (Prompt Engineer) :** Conçoit et optimise les instructions de l'IA.
*   **DA (Data Analyst) :** Définit les métriques, nettoie les données et vérifie les calculs de l'IA.

## 2. Planning de Développement (Besoins Humains)

### **PHASE 1 : ARCHITECTURE & LOGIQUE (Jours 1-2)**
- [ ] **PO/PE :** Finalisation de l'arbre de décision (si l'utilisateur répond "A", l'IA demande "B").
- [ ] **DA :** Création d'un set de données "Gold" (données parfaites) et d'un set "Dirty" (données avec erreurs) pour test.
- [ ] **PE :** Rédaction du "System Prompt" maître (voir Document Master_Prompt_Agent_IA.md).

### **PHASE 2 : INGESTION & NETTOYAGE (Jours 3-5)**
- [ ] **DA/Dev :** Configuration des scripts de nettoyage (suppression des doublons, normalisation des dates).
- [ ] **PE :** Optimisation des prompts pour l'extraction de données complexes (PDF et JSON imbriqués).
- [ ] **PO :** Validation de la conformité RGPD (anonymisation des noms clients dans les exports CRM).

### **PHASE 3 : INTELLIGENCE & VISUALISATION (Jours 6-8)**
- [ ] **DA :** Définition des formules de calcul pour les KPIs complexes (LTV, ROAS réel).
- [ ] **PE :** Programmation de l'agent pour qu'il génère des graphiques via **Mermaid.js** ou des tableaux Markdown.
- [ ] **PO :** Création du dictionnaire des "Niveaux de difficulté" (ex: Une tâche "High" nécessite > 4h de travail humain).

### **PHASE 4 : RECETTE & QA (Jours 9-10)**
- [ ] **Equipe :** "Bug Bash" (test intensif). Essayer de tromper l'IA avec des données contradictoires.
- [ ] **DA :** Vérification mathématique des résultats de l'IA sur un échantillon de 100 lignes.
- [ ] **PO :** Rédaction du guide utilisateur (Comment uploader ses fichiers et poser les bonnes questions).

### **PHASE 5 : DÉPLOIEMENT & FORMATION (Jours 11+)**
- [ ] **PO :** Formation des utilisateurs finaux sur la lecture des rapports.
- [ ] **Equipe :** Mise en place d'une boucle de feedback pour l'amélioration continue des prompts.
