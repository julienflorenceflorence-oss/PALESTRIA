# Agence IA - MLR PROD 2.0

*Brief / cahier des charges. Document vivant. MAJ : 2026-06-08.*

> Ce brief cadre la construction d'une structure d'agents IA qui accompagne le CEO dans l'ensemble de ses besoins. Il dit **quoi** construire, **dans quel ordre**, et **selon quelles règles**. Profil et critères du CEO : voir [know-me.md](know-me.md). Modèle de référence à reproduire : voir [inspiration/modele-a-reproduire.md](inspiration/modele-a-reproduire.md).

---

## 1. Objectif

Avoir une entreprise d'agents et sous-agents qui gèrent l'ensemble des services du CEO, **Ruddy MARIE-LUCE**, structurée comme une vraie entreprise (sous-directeur, directeurs de pôle, équipes).

**Finalité business** : faire de cette structure le **levier** qui permet d'atteindre les objectifs de revenus (court terme 2 000 €/mois, moyen terme 4 000 €/mois net, long terme 10 000 €/mois passif) sans coût d'équipe humaine.

**En une phrase** : une structure IA qui m'accompagne dans tous mes besoins (acquisition, e-commerce, immobilier, marchés), avec mes données en local, un standard de qualité non négociable, et une construction par paliers stables.

---

## 2. Périmètre fonctionnel (les besoins → les pôles)

> **Modèle (recadré 2026-06-09)** : l'agence **vend des services à des clients** (revenu principal). En **complément**, elle fait tourner les **business propres du CEO** (eshop, plus tard trading/immo). L'e-commerce est une **activité du CEO, pas une cible**.

### Pôles métier

| Pôle | Nature | Couvre |
|------|--------|--------|
| **Acquisition** | Service (vente) | Prospection de clients **RGPD/conformité** (beachhead, D-030), détection d'intention, scoring, outreach conforme RGPD. **Hook = audit RGPD du site du prospect.** |
| **Conformité RGPD** | Service (livrable) | Audit de conformité + mise en conformité (le service vendu). S'appuie sur l'audit (E4) + le pôle Légal. |
| **E-commerce (eshop CEO)** | Business propre | **La boutique du CEO** (static + Stripe), activité complémentaire. Tendances, conception vitrine, copy, CRO servent SA boutique. |
| **Immobilier / Marchés** | Business propre (V4/V8) | Hors V1. |

### Pôles support (transversaux, au service des pôles métier)

| Pôle | Couvre |
|------|--------|
| **Data & Mémoire** | Archivage des recherches, knowledge base **locale**, mémoire vectorielle, indexation |
| **Légal & Conformité** | RGPD, mentions légales, CGV, contrats, copie/sauvegarde du legal en ligne |
| **R&D / Veille** | Études profondes, sourcing d'informations, backtesting, synthèses |
| **Qualité** | Agent-juge (note /10, seuil 8), correcteur, contrôle avant livraison |
| **Orchestration** | Le sous-directeur : routage des demandes, planification, prise de décision |

> Chaque pôle est vaste : il sera découpé en sous-zones / agents spécialisés au fil de la construction, pas d'un coup.

---

## 3. Structure de l'agence (hiérarchie)

```
CEO (Ruddy)
 └─ Sous-directeur / Orchestrateur   ← prend la majorité des décisions, route les demandes
     ├─ Pôles MÉTIER
     │   ├─ Directeur Acquisition      → équipe d'agents (prospection, intention, scoring, outreach)
     │   ├─ Directeur E-commerce       → équipe d'agents (tendances, site, SEO, copy, CRO)
     │   ├─ Directeur Immobilier       → équipe d'agents (sourcing, analyse, stratégie)
     │   └─ Directeur Marchés          → équipe d'agents (recherche, backtest, veille)
     └─ Pôles SUPPORT
         ├─ Directeur Data & Mémoire   → archivage, KB locale, mémoire vectorielle
         ├─ Directeur Légal/Conformité → RGPD, contrats, legal
         ├─ Directeur R&D / Veille     → études, sourcing, backtests
         └─ Pôle Qualité (Juge)        → note /10, correcteur, gate de livraison
```

**Principe** : un directeur de pôle reçoit une demande de l'orchestrateur, la décompose pour ses agents, agrège le résultat, le fait passer par la Qualité avant de remonter.

---

## 4. Processus

- **Décision** : le sous-directeur (orchestrateur) prend la majorité des décisions et route les demandes vers le bon pôle.
- **Production** : chaque pôle produit des éléments qui répondent aux **critères et à la personnalité du CEO** (cf. [know-me.md](know-me.md)).
- **Boucle qualité** : tout rendu est **noté /10** par l'agent-Juge.
  - **≥ 8/10** → livré.
  - **< 8/10** → renvoyé au correcteur, repasse en production. Si échec répété (ex. 3 fois) → escalade au CEO.
- **Traçabilité** : toute décision structurante est tracée dans le registre ([recherche/REGISTRE-DECISIONS-STACK.md](recherche/REGISTRE-DECISIONS-STACK.md)) et toute recherche archivée par le pôle Data.

### 4.1 Matrice d'autonomie & règles d'escalade

Définit **quand un agent agit seul** et **quand il remonte au CEO**. Objectif : maximiser l'autonomie (zone verte large) tout en bloquant le CEO uniquement sur l'irréversible et l'engageant (zone rouge).

| Zone | L'agent… | Exemples concrets |
|------|----------|-------------------|
| 🟢 **Autonome** (fait seul, ne notifie pas) | agit sans rien demander | recherche / OSINT sur sources publiques, veille, collecte de coordonnées pro publiées, génération d'audits et de brouillons, audit SEO, mise à jour de la KB, déploiement en **preview**, tests |
| 🟡 **Fait puis notifie** (asynchrone, ne bloque pas) | agit et poste un compte-rendu (Slack/Telegram) | publication de contenu non-sensible, envoi d'une séquence email **déjà validée**, corrections mineures, rapport quotidien, mise en ligne d'un livrable interne |
| 🔴 **Validation CEO requise** (bloque et escalade avec contexte) | s'arrête et attend | **1er envoi à un prospect réel** (validation base légale RGPD), engagement / contrat / devis client, **toute dépense d'argent**, publication à portée juridique (CGV, mentions), suppression irréversible, toute action **hors périmètre du brief** |

**Règles transverses :**
- **Escalade qualité** : un rendu qui échoue **3 fois** au Juge (≥8/10) → escalade CEO. Pas de boucle infinie.
- **Doute = zone rouge** : si un agent hésite sur la zone, il traite comme 🔴 (remonte). Mieux vaut une remontée de trop qu'une bêtise irréversible.
- **Tout 🔴 franchi laisse une trace** dans le registre / journal.

---

## 5. Principes directeurs (non négociables)

1. **Souveraineté des données** : la donnée sensible et les recherches restent **en local**. Le cloud est l'exception justifiée, pas le défaut.
2. **Standard de qualité** : seuil **8/10** minimum. Pas de livraison en dessous.
3. **Construction incrémentale** : V1 → V2 → V4 → V8. On ne passe au palier suivant **que lorsque le palier courant est sans erreur**. Une faille ignorée se décuple.
4. **Preuves obligatoires** : toute reco / stratégie / décision s'appuie sur sources, données, backtest. Pas d'affirmation gratuite (red flag CEO).
5. **Conformité par conception** : RGPD et légalité intégrés dès le départ, surtout sur l'acquisition. La validation de la base légale d'une prospection reste **humaine** (CEO), jamais 100 % automatisée.
   - **Règle de sourcing (RGPD)** : on ne collecte/contacte **que via des sources où le pro a délibérément publié ses coordonnées pour être contacté** (son site pro public, annuaires pro type Pages Jaunes, registres pro). Jamais de données personnelles non destinées au contact, ni de données issues de fuites.
6. **Format de restitution** : TLDR d'abord, détail ensuite. Ton direct et pédagogue. Challenge du CEO quand il a tort.

---

## 6. Contraintes & exclusions

- **Environnement** : macOS (poste du CEO).
- **À ne PAS reproduire du modèle de référence** (voir avertissements dans [inspiration/modele-a-reproduire.md](inspiration/modele-a-reproduire.md)) : usage Tor/Mullvad sur données leakées, modèles « débridés » tiers, business-cloner. Hors-cadre légal/RGPD de MLR PROD.
- **Pas de trading automatique** en V1 (voir §8).

---

## 7. Critères de succès

| Niveau | Critère mesurable |
|--------|-------------------|
| **Technique** | Le socle (orchestration + qualité + data) tourne sans erreur, la boucle 8/10 fonctionne de bout en bout. |
| **Business court terme** | Le pôle Acquisition contribue à faire passer le revenu de **980 € → 2 000 €/mois**. |
| **Business moyen terme** | Les pôles métier soutiennent l'objectif **4 000 €/mois net**. |
| **Long terme** | Immobilier + Marchés alimentent l'objectif **10 000 €/mois passif** (d'ici ~2 ans). |

---

## 8. Hors-périmètre V1

- **Marchés (Bourse / Crypto)** : reportés après V1. Quand ils arriveront, périmètre limité à l'**aide à la décision** (recherche, backtest, alerte) ; **l'exécution des ordres reste manuelle**. Pas de trading automatique.
- **Immobilier** : construit après l'Acquisition (objectif long terme).
- Le **cœur technique avancé** du modèle de référence (équivalent « JARVIS », sentinelles, compression mémoire extrême) : à reconcevoir plus tard, pas un prérequis V1.

---

## 9. Roadmap de construction

> Ordre dicté par le principe incrémental et par l'objectif court terme (sécuriser les 2 000 €/mois).

- **V1 — Socle + deux pôles métier (en parallèle)**
  1. **Orchestration** (sous-directeur) : routage, prise de décision, structure de fichiers `.claude/`.
  2. **Qualité** (agent-Juge + correcteur) : la boucle 8/10.
  3. **Data & Mémoire** : archivage local des recherches, knowledge base.
  4. **Acquisition** (pôle métier) : prospection + détection d'intention, conforme RGPD.
  5. **E-commerce** (pôle métier, en parallèle) : veille tendances, conception site/eshop, SEO, copy, CRO.
  6. **Légal/Conformité** (version minimale) : garde-fou RGPD pour l'acquisition.

  > Les deux pôles métier se construisent en parallèle, mais chacun respecte le principe incrémental dans son propre périmètre (un pôle n'avance pas sur une de ses briques tant qu'elle a une erreur).

- **V2 — Consolidation & élargissement**
  - Renforcement Data + R&D / Veille au service d'Acquisition et E-commerce.

- **V4 — Patrimoine**
  - **Immobilier** (sourcing, analyse, stratégie).

- **V8 — Marchés**
  - **Bourse + Crypto** en aide à la décision (exécution manuelle).

---

## 10. Décisions actées

| Date | Décision |
|------|----------|
| 2026-06-08 | V1 démarre par le socle (Orchestration/Qualité/Data) puis les pôles **Acquisition** et **E-commerce** en **parallèle**. |
| 2026-06-08 | **Marchés (Bourse/Crypto) hors-périmètre V1** ; quand intégrés, aide à la décision uniquement, exécution manuelle. |
| 2026-06-08 | **Infra V1 = Mac uniquement.** Pas de VPS en V1. Le scheduling d'envoi email est délégué au serveur du fournisseur (Resend/Apollo), donc ne nécessite pas de machine 24/7. **VPS = version future conditionnelle** (signaux : boucles d'agent décrochées de la session, service self-hosté à joindre en permanence, inbound temps réel). |
| 2026-06-08 | ~~Cible Acquisition = TPE/PME e-commerce~~ → **RÉVISÉ 2026-06-09** : erreur de cadrage (l'e-commerce est l'activité du CEO, pas une cible). |
| **2026-06-09** | **Recadrage modèle** : l'agence **vend des services** (revenu principal) ; l'**eshop est l'activité complémentaire du CEO** (static + Stripe, pas Shopify). |
| **2026-06-09** | **Beachhead services = TPE/PME ayant un besoin RGPD/conformité.** Hook = audit RGPD du site du prospect → proposition de mise en conformité. Réutilise toute la machine d'audit/collecte/outreach déjà construite, pointée sur l'angle RGPD. |
| 2026-06-08 | **Canaux outreach : email B2B uniquement** (agent). **Pas de LinkedIn** (risque TOS/compte). **Téléphone délégué à l'associé commercial** pour le sous-ensemble à forte valeur (l'agent prépare la fiche + audit, l'humain appelle). Courrier postal = test niche. Inbound SEO = V2. |
| 2026-06-08 | **Stockage = PostgreSQL + pgvector en local** (data relationnelle RGPD + mémoire vectorielle, une brique, zéro migration vers V2). Obsidian en complément pour la KB humaine. Choix confirmé après challenge vs Qdrant (2 systèmes inutiles en V1) et sqlite-vec (migration future + tooling plus jeune). |
| 2026-06-08 | **Règle de sourcing RGPD** : ne contacter que via des sources où le pro a publié ses coordonnées pour être contacté (site pro, annuaires type Pages Jaunes, registres pro). |
| 2026-06-08 | **Pôle Légal V1 = garde-fou RGPD uniquement** (validation base légale, conformité du sourcing/outreach). Génération CGV/mentions reportée en V2. |
| 2026-06-09 | Le « segment RGPD » (ex-secondaire) **devient le beachhead principal** (cf. ci-dessus). Segments suivants possibles : automatisation/IA, missions freelance IT. |
| 2026-06-08 | **Matrice d'autonomie** (3 zones) ajoutée au brief (§4.1). |

---

## 11. Questions ouvertes (à trancher avant V1)

- [ ] **Budget mensuel cible** d'outils/abonnements (pour arbitrer MCP payants vs gratuits).
- [ ] **KPIs par pôle** : 1-2 métriques concrètes par pôle pour cadrer le Juge (à définir au lancement de chaque pôle).
