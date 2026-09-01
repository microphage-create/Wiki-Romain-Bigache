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

Process opérationnel quotidien sur les projets Microphage. Pour les recruteurs et acheteurs qui se demandent comment un solo livre des produits IA en 3 semaines en production-grade.

## Stack de pilotage

- **Claude Code** comme environnement principal de développement (IDE + agentic coding)
- **Mycelium** : outillage interne (skills custom, subagents, hooks, mémoire) qui industrialise les routines, cf [projects/mycelium.md](./projects/mycelium.md)
- **Notion + Linear + GitHub Projects** pour la roadmap et le suivi des tâches
- **Figma** pour le design (UI + plugins)
- **Slack** pour les clients en mission longue

## Cycle de développement type

### Phase 1 - Cadrage (1-2 jours)

- Brief client en session unique, prise de notes structurées
- Specs écrites en markdown dans le repo (single source of truth)
- Architecture document (ADR) sur les choix structurants : runtime, provider LLM, base de données, auth
- Plan de delivery découpé en stories acceptées préalablement

### Phase 2 - Build (cycle court)

- Stack templatée : Next.js 16 + Vercel AI SDK + Supabase + Cloudflare Workers ou Vercel serverless
- Squelette sécurité dès le jour 1 (HMAC, RLS, rate limiting, CSP, HSTS, validation Zod)
- Tests Vitest unit + integration sur les modules critiques dès le 1er commit
- Playwright e2e dès que l'UI est exposée au user
- Monitoring Sentry + PostHog branchés en setup initial
- CI/CD GitHub Actions + Vercel Preview pour reviews continues

### Phase 3 - Livraison

- Demo client live en condition réelle (pas de slides)
- Déploiement progressif : preview > staging > production
- Documentation utilisateur et technique livrée avec le produit
- Handover ou maintien selon le contrat

## Principes opérationnels

### Production-grade dès le jour 1

Pas de phase "MVP minable", pas de dette technique sécurité à rembourser. Le POC est déjà prod-ready. Détail : [methodology.md](./methodology.md).

### Compression du cycle

1 personne = 0 coordination. Concept + archi + code + design + copy + go-to-market dans la même tête. Pas de handover, pas de specs intermédiaires, pas de cycles de validation cross-équipe.

### Documentation continue

Chaque décision structurante (archi, choix de lib, pattern) est documentée en ADR ou en note dans le repo. La mémoire ne vit pas dans la tête, elle vit dans le code.

### Veille technique active

Suivi quotidien des releases : Vercel AI SDK, LangGraph, shadcn/ui, Next.js, Supabase, providers LLM. Veille active sur les patterns émergents (MCP, prompt caching, hybrid retrieval).

## Outillage IA dans le quotidien

- **Claude Code** : agentic coding, refactos, audits, génération de tests
- **Vercel AI SDK** : multi-provider sur tous les projets (OpenAI + Anthropic + Gemini)
- **Tool calling et streaming UI** : pattern réutilisé sur romainbigache.com et les apps clientes
- **MCP** : utilisé sur projets internes pour exposer des sources de connaissance aux agents
- **Prompt caching Anthropic** : cost optimization sur les contextes récurrents

## Posture en mission

- **Autonome end-to-end** sur les sujets cadrés
- **Stakeholder management** maîtrisé (preuve : agile complet en environnement Compliance bancaire chez BforBank, 50+ campagnes pilotées pour DSI grands comptes via OXGEN)
- **Communication directe** : pas de jargon inutile, pas de surdocumentation, pas de status updates verbeux
- **Anti-bullshit** : si une approche ne marche pas ou si un brief est instable, le signaler tôt
- **Engagement long-terme possible** sur missions longue durée, freelance via SASU Microphage Intelligence

## Related

- [projects/mycelium.md](./projects/mycelium.md)
- [methodology.md](./methodology.md)
- [stack.md](./stack.md)
- [availability.md](./availability.md)
