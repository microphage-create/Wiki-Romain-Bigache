---
id: stack
title: Stack technique exhaustive
type: stack
domain: technology
tags: [stack, technical, llm, frameworks, infra, security, tools]
status: live
created: 2026-04-30
updated: 2026-04-30
links:
  - profile.md
  - projects/microphage-analyzer-pro.md
  - projects/altaria.md
  - projects/la-plume-bforbank.md
  - projects/fusil-paris.md
---

# Stack technique - Romain Bigache

> Document complémentaire au CV. À partager quand un recruteur ou un acheteur tech demande le détail des outils, modèles et architectures maîtrisés.

## Modèles LLM utilisés en production ou sur projets

**OpenAI** - GPT-4, GPT-5 (variants Thinking / Pro / mini), Codex. Utilisé chez ADEO dès la sortie de GPT-3.5 (novembre 2022) et chez BforBank pour le bot RAG GPT custom de production éditoriale.

**Anthropic Claude** - Opus 4, Sonnet 4 et Sonnet 4.6 (utilisé quotidiennement dans le flux dev). Multi-provider via Vercel AI SDK sur les projets Microphage.

**Google Gemini** - Gemini 2.5 Pro en production sur **« La Plume »** (assistant IA interne BforBank, RAG complet + agent LangGraph + génération d'image). Veille active sur Gemini 3 Pro.

**Microsoft Copilot et Microsoft 365 Copilot** - projet Altaria conçu en amont du déploiement Copilot 365 chez Altarea (CAC40), avec acculturation des collaborateurs.

**Mistral, Llama, ComfyUI** - utilisés sur projets perso et sides (Prompt Oracle pour la génération visuelle). Veille active sur l'open-source compétitif (DeepSeek, Qwen, Gemma 4).

## Frameworks et orchestration

- **Vercel AI SDK v6** multi-provider (abstraction OpenAI / Claude / Gemini)
- **LangGraph** : orchestration d'agents (router → summarizer → RAG → tool calling → génération d'image), utilisé en production sur La Plume
- **MCP (Model Context Protocol)** : utilisé sur projets internes
- **Tool calling, function calling, structured outputs**
- **Prompt caching Anthropic** (sur Microphage Analyzer Pro)
- **Evaluations (evals)** systématisées en CI

## RAG et bases vectorielles

- **Embeddings** : text-multilingual-embedding-002 (FR/EN sur La Plume)
- **Supabase pgvector** : base vectorielle en production
- **SemanticSplitter custom** avec paramètres de chunking sur mesure (taille de buffer, breakpoint percentile, longueur min, regex de séparation)
- **Hybrid retrieval** : matcher 3 couches (metadata filtering + BM25 + classifier LLM) sur Microphage Analyzer Pro
- **Pattern d'ingestion sources internes hétérogènes** : couplage FAQ + tickets + retours service client → corpus LLM-ready (BforBank, 250+ articles)

## Stack front

- **TypeScript strict**, JavaScript, Node.js
- **Next.js 16, React 19** (App Router, Server Components)
- **Tailwind CSS 4, shadcn/ui, Radix UI, Framer Motion**
- **Design system maison LLM-ready** (Tailwind Plus + Catalyst)
- **Figma Plugin API** (build esbuild)

## Stack back et infra

- **Hono** sur Cloudflare Workers (Microphage Analyzer Pro)
- **Vercel** serverless + Edge Functions (fusil.paris, Altaria)
- **Supabase** (PostgreSQL + Storage + Auth + Edge Functions Deno + RLS + pgvector)
- **Fly.io** sur projets ad hoc
- **Upstash Redis** (rate limiting + cost guard)
- **Monorepo pnpm 9 + Turbo 2**
- **Monitoring** : Sentry + PostHog
- **Tests** : Vitest + Playwright (102 tests automatisés sur morphow-api, en CI/CD)
- **CI/CD** : GitHub Actions + Vercel Preview

## Sécurité

- **HMAC-SHA256 maison** (Web Crypto API native, sur fusil.paris pour vérif webhooks Stripe)
- **Rate limiting in-memory** custom sur Vercel serverless
- **Timing-safe comparison** anti-timing-attacks
- **Whitelist de paths** (allow-list) sur proxy admin
- **Headers HTTP** : CSP avec frame-ancestors, HSTS 1 an, X-Frame-Options DENY, Permissions-Policy, Referrer-Policy
- **CORS strict** par origine
- **Audit XSS** : 3 vulnérabilités identifiées et corrigées en audit interne sur Microphage Analyzer Pro
- **Multi-tenant** avec isolation par tenant
- **Row Level Security (RLS)** Supabase sur tables sensibles

## Paiement et e-commerce

- **Stripe Checkout Sessions + Webhooks** (avec vérification HMAC custom)
- **PayPal** (create-order + capture-order)
- **Codes promo** avec validation server-side
- **Mails transactionnels bilingues FR/EN** via Resend
- **Chronopost** intégration multi-zones (FR / EU / Suisse / UK / Monde)

## Intégrations Workspace

- **Google Calendar API** + **Google Drive API** en production sur romainbigache.com (OAuth2 + Workspace API + tool streaming UI + cron Vercel pour sync nocturne)
- **Pattern OAuth + Workspace API + tool streaming** maîtrisé

## Outils de pilotage projet

- **Méthodes** : agile (sprints, rituels), kanban
- **Outils** : Notion, Linear, GitHub Projects, Figma, Slack
- **Environnement BforBank** : pilotage avec PM, Tribe Leader, équipes marketing, Service Relation Client (SRC), Direction et validations Compliance

## Ce que je ne maîtrise pas (transparence)

Détail dans [expertise.md](./expertise.md).

## Related

- [profile.md](./profile.md)
- [expertise.md](./expertise.md)
- [projects/microphage-analyzer-pro.md](./projects/microphage-analyzer-pro.md)
- [projects/altaria.md](./projects/altaria.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
- [projects/fusil-paris.md](./projects/fusil-paris.md)
