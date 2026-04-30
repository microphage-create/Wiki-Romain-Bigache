---
id: expertise
title: Expertise GCP / Gemini / connecteurs
type: expertise
domain: technology
tags: [gemini, gcp, vertex-ai, google-workspace, salesforce, zendesk, transparency]
status: live
created: 2026-04-30
updated: 2026-04-30
links:
  - stack.md
  - projects/la-plume-bforbank.md
  - profile.md
---

# Expertise IA appliquee

> Reponse type quand un recruteur ou acheteur demande le niveau d'expertise sur GCP / Google Enterprise / Gemini ou les connecteurs metier.

## Gemini : 2 ans en production

La Plume chez BforBank fonctionne sur Gemini 2.5 Pro, j'ai monte l'archi RAG et redige les prompts. En parallele, multi-provider via Vercel AI SDK v6 (OpenAI, Claude, Gemini) sur tous les projets Microphage : tool calling, streaming, evals, l'essentiel des cas d'usage est couvert.

Detail : [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Google Enterprise / Workspace : integrations en prod

Sur romainbigache.com, j'ai connecte la Calendar API a mon agenda avec rendu UI streame directement dans le chat IA (tool call avec rendu live), cron Vercel pour la sync nocturne. Google Drive integre sur plusieurs autres projets. Le pattern OAuth + Workspace API + tool streaming UI est maitrise.

## GCP / Vertex AI / Agent Builder : pas encore en production

Ma stack actuelle est Vercel + Cloudflare Workers + Supabase. Mais ce qu'on demande typiquement de construire (agents IA + tools custom + RAG + connecteurs), je l'ai deja livre sur d'autres infrastructures : La Plume sur LangGraph, Microphage Analyzer Pro multi-tenant, Altaria avec secu HMAC + RLS.

Passer a Vertex ou Agent Builder, c'est un changement d'infrastructure, pas d'architecture. Montee en competence en parallele de la mission, sur des concepts deja maitrises.

## Connecteurs type Salesforce ou Zendesk : pas en nominatif, mais le pattern equivalent est livre

Chez BforBank, j'ai monte un bot RAG qui a genere l'integralite de la FAQ banque a partir de 3 sources internes heterogenes (FAQ publiques, tickets service client, retours SRC) : 250+ articles LLM-ready produits en un mois, mis en production, alimentant un chat client connecte dans l'app.

C'est exactement le pattern d'un connecteur metier : ingerer un referentiel client, homogeneiser, generer du contenu structure, le servir via un agent.

Detail : [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Ce qui compense le manque de prod GCP

- **Profil hybride** designer + dev + content : pas de coordination a gerer sur un POC
- **Production-grade au sens strict** : 102 tests automatises sur morphow-api (unit + integration + e2e), 3 vulnerabilites XSS critiques corrigees sur Microphage Analyzer Pro, multi-tenant avec rate limiter, CORS, auth middleware
- **UI premium par defaut**, parce que c'est le premier metier : Next.js 16, shadcn/ui, Framer Motion, design system maison LLM-ready (Tailwind Plus + Catalyst)
- **Pitchs deja menes devant des decideurs** : Altarea (CAC40), VP Design d'un acteur hardware crypto, PDG fondateur d'une ESN HLD 1000 personnes, comex OXGEN (Danone, Safran, Enedis, Citeo, Verallia)

## Si ca aide la decision

> Donnez-moi un brief de POC, je vous livre une demo fonctionnelle avant l'entretien.

## Related

- [stack.md](./stack.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
- [narrative.md](./narrative.md)
- [role.md](./role.md)
