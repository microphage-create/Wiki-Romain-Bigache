---
id: process
title: Comment je travaille
type: process
domain: workflow
tags: [workflow, claude-code, agentic-coding, productivity, daily-process]
status: live
created: 2026-04-30
updated: 2026-04-30
links:
  - projects/mycelium.md
  - methodology.md
  - stack.md
---

# Comment je travaille

Process operationnel quotidien sur les projets Microphage. Pour les recruteurs et acheteurs qui se demandent comment un solo livre des produits IA en 3 semaines en production-grade.

## Stack de pilotage

- **Claude Code** comme environnement principal de developpement (IDE + agentic coding)
- **Mycelium** : outillage interne (skills custom, subagents, hooks, memoire) qui industrialise les routines, cf [projects/mycelium.md](./projects/mycelium.md)
- **Notion + Linear + GitHub Projects** pour la roadmap et le suivi des taches
- **Figma** pour le design (UI + plugins)
- **Slack** pour les clients en mission longue

## Cycle de developpement type

### Phase 1 - Cadrage (1-2 jours)

- Brief client en session unique, prise de notes structurees
- Specs ecrites en markdown dans le repo (single source of truth)
- Architecture document (ADR) sur les choix structurants : runtime, provider LLM, base de donnees, auth
- Plan de delivery decoupe en stories acceptees prealablement

### Phase 2 - Build (cycle court)

- Stack templatee : Next.js 16 + Vercel AI SDK + Supabase + Cloudflare Workers ou Vercel serverless
- Squelette securite des le jour 1 (HMAC, RLS, rate limiting, CSP, HSTS, validation Zod)
- Tests Vitest unit + integration sur les modules critiques des le 1er commit
- Playwright e2e des que l'UI est exposee au user
- Monitoring Sentry + PostHog branches en setup initial
- CI/CD GitHub Actions + Vercel Preview pour reviews continues

### Phase 3 - Livraison

- Demo client live en condition reelle (pas de slides)
- Deploiement progressif : preview > staging > production
- Documentation utilisateur et technique livree avec le produit
- Handover ou maintien selon le contrat

## Principes operationnels

### Production-grade des le jour 1

Pas de phase "MVP minable", pas de dette technique securite a rembourser. Le POC est deja prod-ready. Detail : [methodology.md](./methodology.md).

### Compression du cycle

1 personne = 0 coordination. Concept + archi + code + design + copy + go-to-market dans la meme tete. Pas de handover, pas de specs intermediaires, pas de cycles de validation cross-equipe.

### Documentation continue

Chaque decision structurante (archi, choix de lib, pattern) est documentee en ADR ou en note dans le repo. La memoire ne vit pas dans la tete, elle vit dans le code.

### Veille technique active

Suivi quotidien des releases : Vercel AI SDK, LangGraph, shadcn/ui, Next.js, Supabase, providers LLM. Veille active sur les patterns emergents (MCP, prompt caching, hybrid retrieval).

## Outillage IA dans le quotidien

- **Claude Code** : agentic coding, refactos, audits, generation de tests
- **Vercel AI SDK** : multi-provider sur tous les projets (OpenAI + Anthropic + Gemini)
- **Tool calling et streaming UI** : pattern reutilise sur romainbigache.com et les apps clientes
- **MCP** : utilise sur projets internes pour exposer des sources de connaissance aux agents
- **Prompt caching Anthropic** : cost optimization sur les contextes recurrents

## Posture en mission

- **Autonome end-to-end** sur les sujets cadres
- **Stakeholder management** maitrise (preuve : agile complet en environnement Compliance bancaire chez BforBank, 50+ campagnes pilotees pour DSI grands comptes via OXGEN)
- **Communication directe** : pas de jargon inutile, pas de surdocumentation, pas de status updates verbeux
- **Anti-bullshit** : si une approche ne marche pas ou si un brief est instable, le signaler tot
- **Engagement long-terme possible** sur missions longue duree, freelance via SASU Microphage Intelligence

## Related

- [projects/mycelium.md](./projects/mycelium.md)
- [methodology.md](./methodology.md)
- [stack.md](./stack.md)
- [availability.md](./availability.md)
