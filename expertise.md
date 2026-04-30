---
id: expertise
title: Expertise GCP / Gemini / Workspace / connecteurs
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

Detail factuel sur le niveau d'expertise par techno : ce qui est en production, ce qui ne l'est pas.

## Gemini : 2 ans en production

La Plume chez BforBank fonctionne sur Gemini 2.5 Pro. Architecture RAG montee en interne, prompts rediges en interne. En parallele, multi-provider via Vercel AI SDK v6 (OpenAI, Claude, Gemini) sur tous les projets Microphage : tool calling, streaming, evals.

Build avec l'IA plus largement depuis la sortie de GPT-3.5 (novembre 2022) chez ADEO : premier prompt interne, puis Content Design System en RAG (ChatGPT + N8N + Supabase). Donc 3,5 ans de pratique cumulee sur les modeles generatifs.

Detail : [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Google Enterprise / Workspace : integrations en production

Sur romainbigache.com :
- Calendar API connectee a l'agenda avec rendu UI streame directement dans le chat IA (tool call avec rendu live)
- Cron Vercel pour la sync nocturne
- Google Drive integre sur plusieurs autres projets

Pattern OAuth + Workspace API + tool streaming UI maitrise.

## GCP / Vertex AI / Agent Builder : pas en production

Stack actuelle : Vercel + Cloudflare Workers + Supabase. Pas de prod sur GCP / Vertex AI / Agent Builder.

Familier avec les concepts et les patterns d'agents (maitrises sur LangGraph + Vercel AI SDK).

Production-grade equivalente livree sur d'autres infrastructures :
- La Plume sur LangGraph
- Microphage Analyzer Pro multi-tenant
- Altaria avec secu HMAC + RLS

## Connecteurs Salesforce / Zendesk : pas en nominatif, pattern equivalent livre

Pas d'integration nominative Salesforce ou Zendesk.

Pattern equivalent livre chez BforBank : bot RAG GPT custom qui a couple 3 sources internes heterogenes (FAQ publiques, tickets service client, retours SRC) et genere 250+ articles LLM-ready en un mois, mis en production, alimentant un chat client connecte dans l'app.

C'est exactement le pattern d'un connecteur metier : ingerer un referentiel client, homogeneiser, generer du contenu structure, le servir via un agent.

Detail : [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Production-grade au sens strict

- 102 tests automatises sur morphow-api (unit + integration + e2e)
- 3 vulnerabilites XSS identifiees et corrigees en audit interne sur Microphage Analyzer Pro (pas de pentest externe a date)
- Multi-tenant avec rate limiter, CORS, auth middleware
- Monitoring Sentry + PostHog
- CI/CD GitHub Actions + Vercel Preview

## Related

- [stack.md](./stack.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
