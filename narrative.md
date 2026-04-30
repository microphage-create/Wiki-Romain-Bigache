---
id: narrative
title: Recit central et positionnement
type: narrative
domain: positioning
tags: [pitch, positioning, objections, talking-points, keywords]
status: live
created: 2026-04-30
updated: 2026-04-30
links:
  - profile.md
  - availability.md
  - expertise.md
  - role.md
---

# Recit central - Romain Bigache

## La phrase qui resume tout

> Je suis le seul profil qui peut concevoir, architecturer, coder, designer et pitcher un POC d'agent IA en grand compte, en solo, en 3 semaines, avec 2 ans de Gemini en production et un pattern directement transposable sur des connecteurs Salesforce / Zendesk.

Cette phrase est l'epine dorsale de tout le pack. CV, reponses, portfolio : chaque piece ne fait que prouver cette phrase sous un angle different.

## Regles de coherence (a respecter partout)

### Positionnement

- **Titre unique** : AI Product Builder
- **Pas** : AI Product Architect, Lead Designer, UX Writer, Senior Designer, Prompt Engineer
- **Sur Collective** : "Senior AI Product Builder - Agents IA & RAG en production"

### Mots-cles differenciants

- "Architecture Karpathy LLM Wiki"
- "Profil hybride designer + dev full-stack + content"
- "Production-grade des le jour 1"
- "POC livre en 3 semaines en solo"
- "Pattern transposable"

### Mots a eviter

- Tiret cadratin (em-dash) : utiliser `:` ou `()` ou `,`
- "De toute facon", "En effet", "Par ailleurs"
- "Prompt Engineering" seul (commodite 2026)
- "UX Writer" comme titre principal (handicap commercial)
- "Senior Designer" (positionnement executant)

## Argumentaire de defense TJM

Si on me challenge sur "850 EUR/j c'est cher pour un profil pas encore Lead valide externe" :

> Mon TJM correspond au milieu de fourchette du marche IA Paris en 2026 (750-1500 EUR). Mon portfolio prouve que je suis deja sur des missions Lead avec validation client externe : Microphage Analyzer Pro est en livraison chez un client edtech B2B sur un deploiement reel, j'ai pitche au VP Design d'un acteur hardware crypto, j'ai shippe Altaria pour Altarea (CAC40) via OXGEN. Avant Microphage, j'ai ete Lead UX Writer & Visual chez BforBank pendant 2 ans avec management d'une equipe de 3 personnes. Je porte mes projets de A a Z (concept, archi, code, UI, pitch comex, deploiement interne), ce qui supprime la coordination de 3 metiers et fait gagner 30-50% sur le time-to-production d'un POC. Sur un cycle court, ce TJM est rentabilise en 2 semaines.

Variantes selon profil interlocuteur :
- **Acheteur prix-driven** : insister sur le gain de coordination (1 personne au lieu de 3), donc ROI accelere
- **Acheteur valeur-driven** : insister sur la rarete du profil hybride et les preuves grands comptes
- **Acheteur mefiant junior** : preciser qu'une demo POC peut etre fournie avant l'entretien

Detail tarification : [availability.md](./availability.md).

## Reponses aux objections recurrentes

### Objection 1 - "Tu as l'air tres solo, comment tu travailles en equipe ?"

Mon recit met en avant le solo parce que c'est mon differenciateur produit (livrer un POC en 3 semaines sans coordonner 3 metiers). Mais j'ai aussi 2 ans en environnement bancaire processe chez BforBank ou je managais une equipe de 3 personnes (2 designers + 1 alternante) en agile, avec rituels, sprints, et coordination quotidienne avec PM, Tribe Leader, equipes marketing, Service Relation Client, Direction et validations Compliance. Et je coordonne des freelances DA / motion / graphisme depuis 4 ans via OXGEN sur des campagnes a 5+ stakeholders pour des DSI grands comptes. Le solo est un mode operatoire choisi sur certains projets, pas une incapacite a travailler en equipe.

### Objection 2 - "On ne voit pas tes outils de pilotage projet (Jira, Linear, Notion, methodes agiles)"

Chez BforBank j'etais en agile complet : sprints, rituels, gestion de dependances avec les equipes Tech, Compliance, Marketing et la Direction. Sur Microphage et Altaria, j'utilise Notion + Linear pour la roadmap et le suivi, GitHub Projects pour le delivery technique. Je peux raconter un sprint planning concret chez BforBank ou un cycle de validation Compliance si tu veux des exemples precis.

### Objection 3 - "Tu n'as pas de prod sur GCP / Vertex AI / Agent Builder"

Vrai, ma stack actuelle est Vercel + Cloudflare Workers + Supabase. Mais j'ai construit la meme chose cote production-grade sur d'autres infras : multi-tenant avec rate limiter / cost guard via Upstash Redis, monitoring Sentry + PostHog, audit XSS, tests Vitest + Playwright en CI/CD, 102 tests automatises sur morphow-api. Le passage a Vertex AI ou Agent Builder, c'est un changement d'infrastructure pas d'architecture. Si vous me donnez un brief de POC, je vous livre une demo fonctionnelle avant l'entretien.

Detail : [expertise.md](./expertise.md).

### Objection 4 - "850 EUR/jour c'est cher pour un profil pas encore Lead valide externe"

Voir argumentaire TJM ci-dessus.

### Objection 5 - "Comment tu geres les arbitrages et desaccords avec un client ?"

Chez BforBank, sur la refonte parcours assurance vie, on avait des contraintes Compliance qui rendaient impossibles certaines formulations UX writing preferees par les designers. J'ai pivote vers une approche en double piste : version Compliance-friendly pour la prod, version 'ideale' documentee pour les futures evolutions reglementaires. Sur Altaria, desaccord avec OXGEN sur la strategie de deploiement (eux voulaient un Town Hall classique, j'ai propose la guerilla interne avec 5 supports places dans les moments d'attente). On a tranche en faisant les deux : guerilla en phase 2, Town Hall en phase 3. Methode : reformuler le desaccord en probleme commun a resoudre, proposer 2-3 options arbitrables, accepter le compromis.

## Preuves a recycler partout

1. **Microphage Analyzer Pro** : livraison chez un client edtech B2B en mai 2026 + pitch a un VP Design d'un acteur hardware crypto. Detail : [projects/microphage-analyzer-pro.md](./projects/microphage-analyzer-pro.md).
2. **Altaria** : 3 semaines en solo + Altarea CAC40 + distribue via OXGEN + nego ESN HLD 1000 personnes. Detail : [projects/altaria.md](./projects/altaria.md).
3. **La Plume** : Gemini 2.5 Pro + LangGraph + deploye dans la marketplace BforBank GPT. Detail : [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).
4. **Chat service client BforBank** : 250+ articles LLM-ready + 3 sources hetero (pattern Salesforce/Zendesk). Detail : [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).
5. **OXGEN** : 50+ campagnes pour DSI Danone, Safran, Enedis, Citeo, Verallia, Naval Group, Altarea. Detail : [experience/oxgen.md](./experience/oxgen.md).

## Specialites IA (mots-cles ATS)

Generative AI, GenAI, LLM, Large Language Models, agents IA autonomes, multi-agents, agent orchestration, agentic workflows, agentic coding, RAG, agentic RAG, embeddings, vector search, semantic search, hybrid retrieval, BM25, reranking, chunking, semantic splitter, prompt engineering, prompt caching, structured outputs, JSON mode, function calling, MCP, vision models, OCR, multimodal AI, image generation, voice AI, conversational AI, chatbots, voicebots, NLU, NLP, intent detection, knowledge bases, content design system, AI adoption, AI enablement, AI literacy, AI transformation, AI strategy, AI product, AI prototyping, agent design.

## Industries (mots-cles ATS)

Banque, fintech, banque en ligne, assurance, retail, e-commerce, marketplace, foncier, immobilier, jeux, paris en ligne, IT, conseil, transformation digitale, change management, services publicitaires, advertising, marketing, formation, edtech, learning, SaaS, B2B SaaS, B2C SaaS, design tools, AI tools, vertical SaaS, white-label, freemium, multi-tenant SaaS, grand compte, CAC40, SBF120, scale-up, startup.

## Profil hybride (mots-cles)

Designer + dev full-stack + content. End-to-end ownership, solo founder, builder, shipper, design engineer, product engineer, hybrid profile, T-shaped, cross-functional, autonomous, Lead valide client externe, stakeholder management, arbitrages comex, conduite de projet bout en bout, senior, lead. Production-grade des le jour 1.

## Activation et communication interne

Communication interne, communication corporate, change communications, AI adoption, AI enablement, deploiement interne, go-to-market interne, campagne d'adoption interne, communication de transformation, communication IT, accompagnement utilisateur, conduite du changement, copywriting interne, direction artistique, brand content interne, storytelling d'entreprise, strategie editoriale interne, charte editoriale, affichage interne, guerilla marketing interne, social interne (Viva Engage, Workplace, Slack, Teams), newsletter interne, supports comex, Town Hall, kit d'animation manager, formation collaborateurs, ateliers IA, masterclass interne. 50+ campagnes internes pilotees via OXGEN pour DSI et Directions Innovation grands comptes.

## Related

- [profile.md](./profile.md)
- [availability.md](./availability.md)
- [expertise.md](./expertise.md)
- [role.md](./role.md)
- [stack.md](./stack.md)
