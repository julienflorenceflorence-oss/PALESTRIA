---
name: know-me
description: Profil complet du CEO Ruddy MARIE-LUCE — identité, objectifs, profil mental, façon de travailler. Chargé en début de session pour que les agents s'alignent sur sa personnalité et ses critères.
metadata:
  type: user
maj: 2026-06-08
---

# Know-me — Ruddy MARIE-LUCE (CEO)

> **Rôle de ce fichier.** Contexte d'identité chargé au démarrage de chaque session/agent. Il dit _qui je suis, ce que je veux, comment je fonctionne et comment vous devez travailler avec moi_. Objectif : que chaque rendu colle à ma personnalité et à mes critères, sans dévier. Un rendu qui ignore ce fichier est hors-cible.
>
> ⚠️ **Ne pas confondre avec le modèle à reproduire.** Le système « NovaTech / Edith » vu en visio et dans `inspiration/` n'est **pas** le mien : c'est une référence que je veux copier (voir [inspiration/modele-a-reproduire.md](inspiration/modele-a-reproduire.md)). Ce fichier-ci ne décrit que **moi**.

---

## 1. Identité

- **Nom** : Ruddy MARIE-LUCE
- **Rôle** : CEO / fondateur
- **Entité / projet** : **MLR PROD 2.0** — agence d'agents IA structurée comme une entreprise (cf. [brief.md](brief.md))
- **Environnement** : macOS
- **Langue** : français (tutoiement)

---

## 2. Activités

- Trading
- Investissement
- Dropshipping
- Commerce
- Construction de systèmes automatisés (agents IA)
- Consultant client (tech)
- Full stack developer web & mobile
- Copywriter

---

## 2bis. Profil développeur / technique

> ⚠️ La stack des projets MLR PROD actuels (Astro, Pocketbase, Bun/Hono/Satori, pgvector…) est une **stack CIBLE vers laquelle Ruddy migre**, PAS son socle d'expérience. Ne jamais présumer qu'il « maîtrise Astro » : c'est en cours d'adoption. Le socle réel est ci-dessous.

### Séniorité
**9 ans d'XP** (hors stage). Expérience de **lead dev** et de **formateur** (équipes entières + juniors). Parcours **ESN** → multi-secteurs, multi-contextes.

### Socle d'expérience (cœur de métier, par niveau)
- **Back** : **ExpressJS / TypeScript** (majorité) + **Symfony / PHP** (origine). Ratio ~**60 TS / 40 PHP**.
- **Front** : **Next.js (~90 %)** + **Vue.js (~10 %)**. **Angular rouillé** (dernière utilisation en v12).
- **Mobile** : **Flutter (~98 %, fort)** = sa maîtrise actuelle, mais **direction stratégique = React Native / Expo** (à monter en compétence, immature aujourd'hui ; cf. logique du pari ci-dessous). **Ionic rouillé**.
- **Scripts / data / growth** : **Python** (usage croissant, lié au growth).
- **Web3** : **Solidity**, niveau modeste.
- **BDD** : **PostgreSQL** ; **MongoDB** (chat / temps réel).
- **DevOps** : Kubernetes (base), Ansible, Jenkins, Prometheus, Grafana, Kong, Docker. **Gère lui-même les déploiements de ses clients.**

### Réflexes & méthode de travail
- **Process** : relève du besoin → planning scrum → dev. Ordre design/fonctionnel selon le projet :
  - Client frileux / besoin visuel fort → **design d'abord**, puis fonctionnel.
  - Cas général (web) → **50-70 % du fonctionnel**, puis **100 % du visuel pour démo client**, puis on finit le fonctionnel.
  - **Mobile → TOUJOURS le visuel d'abord.**
- **Back client** : **plus de Node en prod client** (trop gourmand + contraintes de maintenance, puisqu'il gère les déploiements). **Node reste son défaut sur ses projets perso.**
- **Veille active** failles/MAJ pour choisir les versions à déployer (qualité de service).
- **Déteste Java.** Évite les **CMS (WordPress…)** (dépendance, contrôle minime) et le **legacy** (migration = plaie).

### Partis-pris d'architecture
- **Modularité = le motto** : archis **orientées services, hexagonal, modulaires**. Pouvoir modifier vite une fonction sans casser le projet.
- **Monolithe** : réservé aux projets très particuliers / rapides.
- **REST par défaut.** **GraphQL** seulement en cas spécifique (grosse conso de ressources, éviter de multiplier les endpoints) — « sexy sur le papier, chiant à maintenir ».
- **SSR pour le SEO** ; **SPA** évitées sauf **lead magnets** (là c'est le plus pertinent).
- **Tests** : **unitaires + E2E + stress test**. **DDD** : pas encore dans sa philosophie, mais y réfléchit. **Monorepo** : cas spéciaux, pas prio.

### Le « pourquoi » de la migration (vers la stack cible)
- **Quitte Next.js** : trop de **failles** ces derniers temps.
- **Quitte Symfony/PHP** : « super socle mais trop contraignant » → **Django** (plus léger, plus stable) **et c'est du Python**, qu'il utilise de plus en plus (synergie growth).
- **Mobile : Flutter → React Native / Expo** (décision tranchée 2026-06-10). **Pari sur le futur, pas sur le confort** : abandon de la maîtrise Flutter (98 %) au profit de RN (immature chez lui aujourd'hui), choix assumé.
- **Direction d'ensemble** : **Python/Django** (back) · **Astro** (front marketing) · **React Native / Expo** (mobile).

#### Logique du pari mobile (RN > Flutter) — raisonnement à re-challenger si les conditions changent
1. **Risque mono-vendeur.** Flutter = **Google** (licenciements 2024 des équipes Flutter/Dart, fork communautaire « Flock » né de la frustration, ratio ~1 mainteneur / 20 000 devs) + langage **Dart** mono-usage. RN = backing **distribué** (Meta + Microsoft + Shopify + **Expo, 45 M$ Série B**) + **TS/React**, le plus gros écosystème, talent transférable.
2. **Alignement écosystème.** Son web est **Next.js/TS** → RN partage langage, logique, types (monorepo). Flutter/Dart = silo séparé, zéro partage.
3. **Le clincher (spécifique à l'agence).** MLR PROD = **des agents IA qui construisent du logiciel**. Les LLM écrivent **TS/React ≫ Dart/Flutter** (volume de training data ; Expo a même un « Expo Agent »). **Parier sur Flutter handicaperait la thèse même de l'agence** (une stack que ses propres agents écrivent mal). RN/TS = la stack **agent-compatible**.
- **Coût assumé** : perte de productivité pendant la montée en compétence RN (Flutter = sa force actuelle).
- **Condition de réexamen** : Google ré-investit massivement dans Flutter **et** Dart devient bien supporté par les LLM ; ou le mobile devient marginal dans l'activité.
- **Tactique** : une app urgente peut sortir en Flutter (sa force), mais **le neuf et l'apprentissage vont sur RN/Expo**.

### Compétences transverses
- **RGPD / IA Act** : en **formation active** (c'est le beachhead de l'agence → enjeu de crédibilité).
- **Copywriting** : **certifié**, pratique régulière.
- **Marketing / growth** : **diplôme en cours** (école de commerce) — growth hacking, acquisition digitale.

### Secteurs
**Ouvert à tout** (l'ESN l'a envoyé partout). Déjà adressés : banque · e-commerce · anti-gaspillage · transport en commun · **militaire** · **spatial** · opérateur télécom → à l'aise en environnements **exigeants / haute conformité / haute criticité**.

---

## 3. Objectifs

| Horizon                               | Objectif                                                                                 | État actuel                 |
| ------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------- |
| **Court terme (3 mois)**              | Rembourser le crédit conso de **5 k€** + atteindre **2 000 €/mois** de revenus réguliers | actuellement **980 €/mois** |
| **Moyen terme (1 an)**                | Générer **4 000 €/mois net** (après impôts/charges)                                      | —                           |
| **Long terme (d'ici 35 ans, ~2 ans)** | Investissements et/ou business générant **10 000 €/mois en passif**                      | —                           |

**Vision** : bâtir des sources de revenus passives (immobilier ou autre) qui découplent le revenu du temps de travail. L'agence d'agents IA est le levier pour y arriver sans coût d'équipe.

**Cap géographique (ajout 2026-06-24)** : objectif de vie **digital nomad dans la Caraïbe**. Conséquences opérationnelles à garder en tête sur toutes les missions/clients : privilégier le **full remote** et l'**async** (décalage France ↔ Caraïbe ~UTC-4, soit 5-6 h ; matin Caraïbe = après-midi France). Le revenu court terme reste calibré **France/EU async** (clients FR servables à distance, contrats EUR) : c'est le chemin le plus rapide vu son profil et son beachhead RGPD, sans fermer la porte aux missions internationales/US (mieux synchronisées depuis la Caraïbe) le moment venu.

---

## 4. Profil mental / fonctionnement

- **Prise de décision** : analyse d'abord, et besoin de **maîtriser au moins 95 %** du sujet avant d'agir. Pas d'action à l'aveugle.
- **Rapport au temps** : **patient par nature**, mais je me fixe une **deadline de 2 ans** comme cadre de cap. Patience ≠ laisser traîner.
- **Rapport aux autres** : j'apprends à **déléguer progressivement**, mais la **confiance est très difficile** à accorder. Je dois valider avant de lâcher.
- **Rapport à moi-même** : **très exigeant** (pour demander plus aux autres, je dois d'abord être irréprochable). La critique envers moi est la bienvenue si elle est **constructive** : je veux m'améliorer, sans m'auto-flageller.
- **Niveau de confiance en moi** : ~**55 % en général**, ~**95 % en tech**.

---

## 5. Le tranchant (points faibles, paradoxe, red flags)

- **Point faible assumé** : l'humain « social » n'est pas mon terrain. Réseautage, blabla, **négociation** : non. → _L'agent doit compenser : préparer, cadrer, scripter, voire prendre en charge la partie relationnelle/négociation à ma place._
- **Paradoxe** : j'ai pourtant de **bonnes compétences d'analyse de l'humain**. Le potentiel est là, mais **sous-estimé ou brisé**. → _À réactiver, pas à contourner par défaut._
- **Red flags (= rendu 0/10, rejet immédiat)** :
  - Idées **non réfléchies**, **non back-testées**, **sans sources, sans preuves**
  - Côté humain : personnes **non ponctuelles** ou **non sincères**

---

## 6. Façon de travailler avec moi (instructions agents)

- **Ton** : direct **ET** pédagogue. Concret. J'utilise des **analogies** pour faire passer une idée ; fais-en si ça clarifie. Cherche le **mot juste** : transmettre l'info avec la meilleure pertinence prime sur le volume.
- **Format** : **TLDR d'abord, puis le détail complet** en dessous.
- **Posture** : **challenge-moi**. Contredis-moi quand j'ai tort, avec arguments. Je ne veux pas un exécutant complaisant.
- **Toujours** : sources, preuves, back-test, raisonnement explicite. Pas d'affirmation gratuite (cohérent avec mes red flags).

---

## 7. Standard de qualité (critère de notation)

- **Tout rendu est noté /10** par rapport à ma demande et à ce profil (principe posé dans le brief MLR PROD 2.0).
- **Seuil d'acceptation : ≥ 8/10.** En dessous, le rendu repart en correction, il n'est pas livré.
- Critères implicites de la note : pertinence vs demande · preuves/sources · rigueur · alignement avec ce profil · concision utile (TLDR puis détail).

---

## 8. Positionnement business (consultant)

- **Cible** : déjà définie (axe freelance IT / RGPD côté missions). À court terme, viser aussi l'**investissement immobilier ou autre** pour dégager du passif.
- **Différenciateur** : « **un tech qui comprend vos douleurs et parle votre jargon** ». Pont entre l'expertise technique et le langage métier du client.
- **Tabous / clients refusés** : pas de client **raciste assumé, fasciste, ou grossier**. Le reste se décide **au feeling**.

---

## 9. Liens

- Brief projet : [brief.md](brief.md)
- Modèle à reproduire : [inspiration/modele-a-reproduire.md](inspiration/modele-a-reproduire.md)
- Registre des décisions stack : [recherche/REGISTRE-DECISIONS-STACK.md](recherche/REGISTRE-DECISIONS-STACK.md)
- Source de ce profil : entretien du 2026-06-08 (mes réponses directes) + brief

---

## À compléter / préciser plus tard

- [x] Détail de la **cible client** consultant : 3 ICP définis le 2026-06-24 (1. TPE/PME services B2B — RGPD + sécurité email ; 2. commerçants indépendants site+boutique — cookies/SEO ; 3. professions réglementées — RGPD données sensibles + facturation élec). Listes de prospection : `projet/recherche/2026-06-24/prospection-emploi/`.
- [ ] **Stratégie immobilière** envisagée (type de bien, zone, montage) une fois le court terme sécurisé.
- [ ] Trancher les 4 questions ouvertes du brief (§11) avant de coder la V1.
