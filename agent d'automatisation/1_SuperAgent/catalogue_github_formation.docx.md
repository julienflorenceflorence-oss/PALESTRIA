  
**CATALOGUE DES OUTILS**

**GITHUB POUR L'IA GÉNÉRATIVE**

**& LE VIBE CODING**

 

Document de formation professionnelle

54 dépôts GitHub classifiés, vérifiés et commentés

**Mars 2026**

**OCCIRANK**

Jérémy — Consultant SEO & Formateur IA

# **Guide de lecture**

Ce document recense les dépôts GitHub partagés dans les groupes de travail « L'Équipage » et « Vibe Coding ». Chaque outil est classifié par catégorie d'usage et par plateforme cible.

## **Plateformes cibles**

| Plateforme | Description |
| :---- | :---- |
| **Claude** | Spécifique à l'écosystème Anthropic (Claude Code, Claude Desktop) |
| **OpenClaw** | Écosystème OpenClaw (ex-Clawdbot/Moltbot) — 250K+ ⭐ GitHub |
| **Multi** | Compatible multi-plateformes (Claude, GPT, Gemini, Ollama, etc.) |
| **GPT** | Optimisé pour l'écosystème OpenAI / ChatGPT |
| **Gemini** | Spécifique à Google Gemini |
| **n8n** | Nodes pour la plateforme d'automatisation n8n |

## **Indicateurs de statut**

🟢 Très actif / Actif — Mises à jour régulières, communauté vivante

🟡 Expérimental / Récent / Maintenance — Fonctionnel mais évolution incertaine

🔵 Archive / Référence — Projet historique, pas de développement actif

# **💻  Agents de Code en Terminal (CLI)**

*Outils en ligne de commande pour coder avec l'IA directement dans le terminal. Ce sont les piliers du vibe coding professionnel.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**claude-code**](https://github.com/anthropics/claude-code) | Agent de code officiel d'Anthropic. Terminal-first, comprend votre codebase, gère git. Support MCP, plugins, skills. | 78K+ | **Claude** | 🟢 Très actif | Mars 2026 |
| [**cline**](https://github.com/cline/cline) | Extension VS Code pour coder avec l'IA. Multi-modèles. Attention : attaque supply chain v2.3.0 (fév 2026). | 30K+ | **Multi** | 🟡 Actif (vigilance sécu) | Mars 2026 |
| [**crush**](https://github.com/charmbracelet/crush) | Agent de code TUI glamour. Multi-modèles via OpenRouter, Anthropic, OpenAI. Support LSP, MCP. Ex-OpenCode. | 21K+ | **Multi** | 🟢 Très actif | Mars 2026 |
| [**oh-my-opencode**](https://github.com/code-yeongyu/oh-my-opencode) | CLI unifié qui réunit tous les modèles (Claude, GPT, Gemini, etc.) sur un seul outil en bypass d'origine. | \~2K | **Multi** | 🟢 Actif | Fév 2026 |
| [**Claudy-V2**](https://github.com/uglyswap/Claudy-V2) | Alternative communautaire à Claude Code. Projet expérimental visant à surpasser les performances de Claude Code. | \<1K | **Claude** | 🟡 Expérimental | Jan 2026 |
| [**phi-code**](https://github.com/uglyswap/phi-code) | Agent de code basé sur les modèles Phi (Microsoft). Approche légère et locale. | \<1K | **Multi** | 🟡 Expérimental | Mars 2026 |
| [**rtk**](https://github.com/rtk-ai/rtk) | Agent de code CLI avec bons retours utilisateurs. Approche simplifiée pour le développement assisté par IA. | \~5K | **Multi** | 🟢 Actif | Mars 2026 |
| [**gstack**](https://github.com/garrytan/gstack) | Stack IA complète par Garry Tan (Y Combinator). Approche full-stack du développement assisté. | \~1K | **Multi** | 🟡 Récent | Mars 2026 |

# **🦞  Écosystème OpenClaw**

*OpenClaw (ex-Clawdbot/Moltbot) est le projet le plus starré sur GitHub en 2026 (250K+ ⭐). Assistant IA personnel autonome, self-hosted. Attention aux enjeux de sécurité.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**openclaw**](https://github.com/openclaw/openclaw) | Agent IA autonome personnel. Exécute des tâches réelles (email, domotique, achats). Self-hosted. CVE-2026-25253 connu. | 250K+ | **OpenClaw** | 🟢 Très actif | Mars 2026 |
| [**zeptoclaw**](https://github.com/qhkm/zeptoclaw) | Variante Rust ultra-légère (6MB). Isolation container, détection prompt injection, circuit breaker. Sécurité renforcée. | \~5K | **OpenClaw** | 🟢 Actif | Fév 2026 |
| [**gitclaw**](https://github.com/beunwa/gitclaw) | Fork/variante communautaire d'OpenClaw avec améliorations spécifiques. Développé par la communauté française. | \<1K | **OpenClaw** | 🟢 Actif | Mars 2026 |
| [**openclaw-mission-control**](https://github.com/abhi1693/openclaw-mission-control) | Dashboard de contrôle pour OpenClaw. Interface web pour gérer et monitorer les instances OpenClaw. | \<1K | **OpenClaw** | 🟡 Récent | Mars 2026 |

# **🤖  Frameworks Multi-Agents & IA**

*Frameworks pour orchestrer plusieurs agents IA collaborant ensemble. Essentiels pour comprendre l'architecture des systèmes multi-agents.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**MetaGPT**](https://github.com/FoundationAgents/MetaGPT) | Framework multi-agents où les GPT jouent des rôles (PM, architecte, dev). Pipeline de développement logiciel complet. | 50K+ | **Multi** | 🟢 Actif | Mars 2026 |
| [**smolagents**](https://github.com/huggingface/smolagents) | Framework d'agents léger par Hugging Face. Approche minimaliste pour créer des agents IA efficaces. | 15K+ | **Multi** | 🟢 Très actif | Mars 2026 |
| [**eliza**](https://github.com/elizaOS/eliza) | Framework d'agents IA pour Web3/crypto. Multi-modèles, multi-plateformes, plugins extensibles. | 20K+ | **Multi** | 🟢 Actif | Mars 2026 |
| [**AgentGPT**](https://github.com/reworkd/AgentGPT) | Agents IA autonomes dans le navigateur. Définir un objectif et l'agent le décompose en tâches. | 32K+ | **GPT** | 🟡 Maintenance | 2025 |
| [**OpenManus**](https://github.com/mannaandpoem/OpenManus) | Framework open source pour agents IA généralistes. Alternative aux solutions fermées. | \~12K | **Multi** | 🟢 Actif | Mars 2026 |
| [**agentation**](https://github.com/benjitaylor/agentation) | Framework d'orchestration d'agents IA. Gestion de workflows complexes multi-agents. | \~1K | **Multi** | 🟡 Récent | Mars 2026 |
| [**OBLITERATUS**](https://github.com/elder-plinius/OBLITERATUS) | Jailbreak / prompt engineering avancé. Collection de techniques de manipulation de LLMs. | \~2K | **Multi** | 🟡 Expérimental | Mars 2026 |

# **🔌  Serveurs MCP (Model Context Protocol)**

*Le protocole MCP permet aux LLMs d'interagir avec des services externes. Ces serveurs étendent les capacités de Claude Code, Cline, Crush, etc.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**playwright-mcp**](https://github.com/microsoft/playwright-mcp) | Serveur MCP officiel Microsoft pour automatiser les navigateurs web via Playwright. | 10K+ | **Multi** | 🟢 Très actif | Mars 2026 |
| [**chrome-devtools-mcp**](https://github.com/ChromeDevTools/chrome-devtools-mcp) | MCP officiel Chrome DevTools. Contrôler Chrome depuis Claude sans extension, fonctionne en headless. | \~3K | **Multi** | 🟢 Actif | Mars 2026 |
| [**brightdata-mcp**](https://github.com/brightdata/brightdata-mcp) | MCP pour BrightData (scraping/données web). Accès aux données structurées du web depuis un agent IA. | \~2K | **Multi** | 🟢 Actif | Fév 2026 |
| [**coolify-mcp**](https://github.com/StuMason/coolify-mcp) | MCP pour Coolify (PaaS self-hosted). Gérer vos déploiements Coolify depuis Claude Code. | \<1K | **Multi** | 🟢 Actif | 2025 |
| [**lazy-mcp**](https://github.com/voicetreelab/lazy-mcp) | Proxy MCP qui expose 2 méta-outils et charge les vrais outils à la demande. Réduit \~95% les tokens. | \<1K | **Multi** | 🟢 Actif | Déc 2025 |
| [**ccpm**](https://github.com/automazeio/ccpm) | Claude Code Plugin Manager. Gestionnaire de plugins et MCPs pour Claude Code. | \<1K | **Claude** | 🟡 Récent | Déc 2025 |

# **🎨  Vibe Coding & Méthodologies**

*Outils et méthodes pour le 'vibe coding' — créer des applications complètes par prompts, sans coder manuellement.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**dyad**](https://github.com/dyad-sh/dyad) | App builder IA local et open source. Alternative gratuite à Lovable/v0/Bolt. Supporte Gemini, OpenRouter. | \~8K | **Multi** | 🟢 Très actif | Mars 2026 |
| [**BMAD-METHOD**](https://github.com/bmad-code-org/BMAD-METHOD) | Méthodologie pour construire un SaaS sans erreurs en préservant le contexte. Process structuré pour agents. | \~3K | **Claude** | 🟢 Actif | Jan 2026 |
| [**superpowers**](https://github.com/obra/superpowers) | Collection de prompts et techniques avancées pour Claude Code. Booste les capacités de l'agent. | \~2K | **Claude** | 🟢 Actif | Jan 2026 |

# **🔒  Sécurité & Pentest**

*Outils de sécurité, audit et pentest. Indispensables pour sécuriser les environnements d'agents IA autonomes.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**shannon**](https://github.com/KeygraphHQ/shannon) | Framework de pentest IA. Analyse de sécurité automatisée de projets. Peut révéler des vulnérabilités surprenantes. | \~3K | **Multi** | 🟢 Actif | Mars 2026 |
| [**claude-code-safety-net**](https://github.com/kenryu42/claude-code-safety-net) | Filet de sécurité pour Claude Code. Prévient les actions destructrices non intentionnelles. | \<1K | **Claude** | 🟢 Actif | Déc 2025 |
| [**destructive\_command\_guard**](https://github.com/Dicklesworthstone/destructive_command_guard) | Protection contre les commandes destructrices en prod. Intercepte rm \-rf, DROP TABLE, etc. | \~1K | **Multi** | 🟢 Actif | Jan 2026 |
| [**holehe**](https://github.com/megadose/holehe) | OSINT : vérifie si un email est associé à des comptes sur divers services. Outil d'enrichissement de données. | 7K+ | **Multi** | 🟡 Maintenance | 2025 |

# **⚙️  Outils DevOps & Infrastructure**

*Solutions self-hosted, interfaces d'administration et outils d'infrastructure pour les déploiements d'agents IA.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**open-webui**](https://github.com/open-webui/open-webui) | Interface web pour LLMs (Ollama, OpenAI). Self-hosted, multi-utilisateurs, RAG intégré. | 70K+ | **Multi** | 🟢 Très actif | Mars 2026 |
| [**gollama**](https://github.com/sammcj/gollama) | Gestionnaire TUI pour modèles Ollama. Lister, télécharger, supprimer des modèles locaux. | \~2K | **Multi** | 🟢 Actif | 2025 |
| [**teable**](https://github.com/teableio/teable) | Alternative open source à Airtable. Base de données relationnelle avec interface tableur. | 15K+ | **Multi** | 🟢 Très actif | Mars 2026 |
| [**docuseal**](https://github.com/docusealco/docuseal) | Signature électronique open source. Alternative à DocuSign, self-hosted. | 10K+ | **Multi** | 🟢 Actif | Mars 2026 |
| [**novu**](https://github.com/novuhq/novu) | Infrastructure de notifications open source. Email, SMS, push, in-app. API unifiée. | 35K+ | **Multi** | 🟢 Très actif | Mars 2026 |

# **🛠️  Productivité Dev & Utilitaires**

*Outils complémentaires pour améliorer le workflow de développement avec l'IA.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**gpt-crawler**](https://github.com/BuilderIO/gpt-crawler) | Crawler web qui génère des fichiers de connaissances pour GPTs custom et RAG. | 18K+ | **GPT** | 🟡 Maintenance | 2025 |
| [**public-apis**](https://github.com/public-apis/public-apis) | Liste collaborative d'APIs publiques gratuites. Ressource indispensable pour tout développeur. | 330K+ | **Multi** | 🟢 Communautaire | Mars 2026 |
| [**coding\_agent\_session\_search**](https://github.com/Dicklesworthstone/coding_agent_session_search) | Recherche dans les sessions d'agents de code. Retrouver des conversations passées avec Claude Code. | \<1K | **Claude** | 🟢 Actif | Fév 2026 |
| [**humanizer**](https://github.com/blader/humanizer) | Rend le contenu IA plus humain. Basé sur le manifeste Wikipedia de détection de contributions IA. | \~1K | **Multi** | 🟡 Récent | Fév 2026 |
| [**claude-mem**](https://github.com/thedotmack/claude-mem) | Système de mémoire persistante pour Claude Code. Conserve le contexte entre les sessions. | \<1K | **Claude** | 🟡 Expérimental | Jan 2026 |
| [**serena**](https://github.com/oraios/serena) | Outil de workflows automatisés pour Cline. Automatisation des tâches répétitives. | \~1K | **Multi** | 🟢 Actif | Jan 2026 |

# **📊  SEO & Marketing Digital**

*Nodes n8n et outils spécialisés pour le SEO et le marketing digital.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**n8n-nodes-gtm**](https://github.com/elevate-agency-data/n8n-nodes-gtm) | Node n8n pour Google Tag Manager. Automatiser la gestion des tags GTM via workflows n8n. | \<500 | **n8n** | 🟢 Actif | 2025 |
| [**n8n-nodes-googleanalytics**](https://github.com/elevate-agency-data/n8n-nodes-googleanalytics) | Node n8n pour Google Analytics. Extraction de données GA4 dans des workflows automatisés. | \<500 | **n8n** | 🟢 Actif | 2025 |

# **🎤  API Temps Réel & Multimédia**

*Outils pour les interactions IA en temps réel (voix, vidéo, WebRTC).*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**speech-assistant-openai-realtime-api-node**](https://github.com/twilio-samples/speech-assistant-openai-realtime-api-node) | Assistant vocal Twilio \+ OpenAI Realtime API. Conversations vocales en temps réel avec l'IA. | \~2K | **GPT** | 🟢 Actif | 2025 |
| [**gemini-webrtc-web-simple**](https://github.com/pipecat-ai/gemini-webrtc-web-simple) | WebRTC \+ Gemini. Communication temps réel plus rapide que les sockets pour l'IA. | \~1K | **Gemini** | 🟢 Actif | 2025 |
| [**Veo-3-Meta-Framework**](https://github.com/snubroot/Veo-3-Meta-Framework) | Framework de prompting avancé pour Veo 3 (génération vidéo Google). Techniques avancées. | \~1K | **Google** | 🟡 Niche | 2025 |

# **🔬  Recherche & Fondamentaux**

*Projets de recherche et références fondamentales en IA/NLP.*

| Dépôt | Description | Stars | Plateforme | Statut | MAJ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [**bert**](https://github.com/google-research/bert) | BERT (Google). Modèle fondateur du NLP moderne. Référence historique pour comprendre les transformers. | 38K+ | **Google** | 🔵 Archive/Référence | 2023 |
| [**conductor**](https://github.com/gemini-cli-extensions/conductor) | Extension CLI pour Gemini. Orchestrateur pour le CLI Gemini de Google. | \<1K | **Gemini** | 🟡 Récent | Déc 2025 |

# **📈  Synthèse par plateforme**

| Plateforme | Nb | Principaux outils |
| :---- | :---- | :---- |
| **Claude / Anthropic** | **13** | claude-code, Crush, Cline, Claudy-V2, BMAD-METHOD, superpowers, claude-mem, claude-code-safety-net, ccpm, coding\_agent\_session\_search, oh-my-opencode, phi-code, destructive\_command\_guard |
| **OpenClaw** | **4** | openclaw, zeptoclaw, gitclaw, openclaw-mission-control |
| **Multi-plateforme** | **28** | MetaGPT, smolagents, Dyad, RTK, playwright-mcp, open-webui, teable, novu, shannon, public-apis, humanizer, etc. |
| **OpenAI / GPT** | **3** | AgentGPT, gpt-crawler, speech-assistant-openai |
| **Google / Gemini** | **4** | BERT, conductor, gemini-webrtc, Veo-3-Meta-Framework |
| **n8n** | **2** | n8n-nodes-gtm, n8n-nodes-googleanalytics |

# **⚠️  Alertes de sécurité**

**Cline v2.3.0 (fév 2026\)** — Attaque supply chain via npm. Le package compromis installait silencieusement OpenClaw. Mettre à jour vers v2.4.0+. Vérifier l'absence d'installation non souhaitée d'OpenClaw.

**OpenClaw CVE-2026-25253 (CVSS 8.8)** — Cross-site WebSocket hijacking permettant RCE. 42 000 instances exposées avec contournement d'authentification. Mettre à jour et sécuriser les déploiements.

**ClawHavoc** — 341 skills malveillants sur ClawHub ont compromis 9 000+ installations. Vérifier l'intégrité des skills installés.

*Consolidation mars 2026*

*Données GitHub vérifiées le 15 mars 2026\. Les statistiques (stars, statut) évoluent rapidement.*

*Document généré par Claude (Anthropic) pour OCCIRANK — Formation professionnelle*