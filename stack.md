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

> Document complementaire au CV. A partager quand un recruteur ou un acheteur tech demande le detail des outils, modeles et architectures maitrises.

## Modeles LLM utilises en production ou sur projets

**OpenAI** - GPT-4, GPT-5 (variants Thinking / Pro / mini), Codex. Utilise chez ADEO des la sortie de GPT-3.5 (novembre 2022) et chez BforBank pour le bot RAG GPT custom de production editoriale.

**Anthropic Claude** - Opus 4, Sonnet 4 et Sonnet 4.6 (utilise quotidiennement dans le flux dev). Multi-provider via Vercel AI SDK sur les projets Microphage.

**Google Gemini** - Gemini 2.5 Pro en production sur **« La Plume »** (assistant IA interne BforBank, RAG complet + agent LangGraph + generation d'image). Veille active sur Gemini 3 Pro.

**Microsoft Copilot et Microsoft 365 Copilot** - projet Altaria concu en amont du deploiement Copilot 365 chez Altarea (CAC40), avec acculturation des collaborateurs.

**Mistral, Llama, ComfyUI** - utilises sur projets perso et sides (Prompt Oracle pour la generation visuelle). Veille active sur l'open-source competitif (DeepSeek, Qwen, Gemma 4).

## Frameworks et orchestration

- **Vercel AI SDK v6** multi-provider (abstraction OpenAI / Claude / Gemini)
- **LangGraph** : orchestration d'agents (router → summarizer → RAG → tool calling → generation d'image), utilise en production sur La Plume
- **MCP (Model Context Protocol)** : utilise sur projets internes
- **Tool calling, function calling, structured outputs**
- **Prompt caching Anthropic** (sur Microphage Analyzer Pro)
- **Evaluations (evals)** systematisees en CI

## RAG et bases vectorielles

- **Embeddings** : text-multilingual-embedding-002 (FR/EN sur La Plume)
- **Supabase pgvector** : base vectorielle en production
- **SemanticSplitter custom** avec parametres de chunking sur mesure (taille de buffer, breakpoint percentile, longueur min, regex de separation)
- **Hybrid retrieval** : matcher 3 couches (metadata filtering + BM25 + classifier LLM) sur Microphage Analyzer Pro
- **Pattern d'ingestion sources internes heterogenes** : couplage FAQ + tickets + retours service client → corpus LLM-ready (BforBank, 250+ articles)

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
- **Tests** : Vitest + Playwright (102 tests automatises sur morphow-api, en CI/CD)
- **CI/CD** : GitHub Actions + Vercel Preview

## Securite

- **HMAC-SHA256 maison** (Web Crypto API native, sur fusil.paris pour verif webhooks Stripe)
- **Rate limiting in-memory** custom sur Vercel serverless
- **Timing-safe comparison** anti-timing-attacks
- **Whitelist de paths** (allow-list) sur proxy admin
- **Headers HTTP** : CSP avec frame-ancestors, HSTS 1 an, X-Frame-Options DENY, Permissions-Policy, Referrer-Policy
- **CORS strict** par origine
- **Audit XSS** : 3 vulnerabilites critiques identifiees et corrigees sur Microphage Analyzer Pro
- **Multi-tenant** avec isolation par tenant
- **Row Level Security (RLS)** Supabase sur tables sensibles

## Paiement et e-commerce

- **Stripe Checkout Sessions + Webhooks** (avec verification HMAC custom)
- **PayPal** (create-order + capture-order)
- **Codes promo** avec validation server-side
- **Mails transactionnels bilingues FR/EN** via Resend
- **Chronopost** integration multi-zones (FR / EU / Suisse / UK / Monde)

## Integrations Workspace

- **Google Calendar API** + **Google Drive API** en production sur romainbigache.com (OAuth2 + Workspace API + tool streaming UI + cron Vercel pour sync nocturne)
- **Pattern OAuth + Workspace API + tool streaming** maitrise

## Outils de pilotage projet

- **Methodes** : agile (sprints, rituels), kanban
- **Outils** : Notion, Linear, GitHub Projects, Figma, Slack
- **Environnement BforBank** : pilotage avec PM, Tribe Leader, equipes marketing, Service Relation Client (SRC), Direction et validations Compliance

## Ce que je ne maitrise pas (transparence)

Detail dans [expertise.md](./expertise.md).

## Related

- [profile.md](./profile.md)
- [expertise.md](./expertise.md)
- [projects/microphage-analyzer-pro.md](./projects/microphage-analyzer-pro.md)
- [projects/altaria.md](./projects/altaria.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
- [projects/fusil-paris.md](./projects/fusil-paris.md)
