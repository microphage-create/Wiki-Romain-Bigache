---
id: stack
title: Full technical stack
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

# Technical stack - Romain Bigache

> Companion document to the CV. Share this when a recruiter or technical buyer wants the detail of tools, models, and architectures.

## LLM models used in production or on projects

**OpenAI** - GPT-4, GPT-5 (Thinking / Pro / mini variants), Codex. Used at ADEO from the day GPT-3.5 shipped (November 2022) and at BforBank for the custom RAG GPT bot for editorial production.

**Anthropic Claude** - Opus 4, Sonnet 4, and Sonnet 4.6 (used daily in the dev workflow). Multi-provider via Vercel AI SDK on Microphage projects.

**Google Gemini** - Gemini 2.5 Pro in production on **"La Plume"** (BforBank internal AI assistant, full RAG + LangGraph agent + image generation). Active monitoring of Gemini 3 Pro.

**Microsoft Copilot and Microsoft 365 Copilot** - Altaria designed ahead of the Copilot 365 rollout at Altarea (CAC40), with employee enablement.

**Mistral, Llama, ComfyUI** - used on personal and side projects (Prompt Oracle for visual generation). Active monitoring of competitive open-source models (DeepSeek, Qwen, Gemma 4).

## Frameworks and orchestration

- **Vercel AI SDK v6** multi-provider (OpenAI / Claude / Gemini abstraction)
- **LangGraph**: agent orchestration (router → summarizer → RAG → tool calling → image generation), used in production on La Plume
- **MCP (Model Context Protocol)**: used on internal projects
- **Tool calling, function calling, structured outputs**
- **Anthropic prompt caching** (on Microphage Analyzer Pro)
- **Evaluations (evals)** systematized in CI

## RAG and vector stores

- **Embeddings**: text-multilingual-embedding-002 (FR/EN on La Plume)
- **Supabase pgvector**: vector store in production
- **Custom SemanticSplitter** with tailored chunking parameters (buffer size, breakpoint percentile, min length, separator regex)
- **Hybrid retrieval**: 3-layer matcher (metadata filtering + BM25 + LLM classifier) on Microphage Analyzer Pro
- **Heterogeneous internal source ingestion pattern**: pairing FAQ + tickets + customer service feedback into an LLM-ready corpus (BforBank, 250+ articles)

## Front stack

- **Strict TypeScript**, JavaScript, Node.js
- **Next.js 16, React 19** (App Router, Server Components)
- **Tailwind CSS 4, shadcn/ui, Radix UI, Framer Motion**
- **In-house LLM-ready design system** (Tailwind Plus + Catalyst)
- **Figma Plugin API** (esbuild build)

## Back and infra stack

- **Hono** on Cloudflare Workers (Microphage Analyzer Pro)
- **Vercel** serverless + Edge Functions (fusil.paris, Altaria)
- **Supabase** (PostgreSQL + Storage + Auth + Edge Functions Deno + RLS + pgvector)
- **Fly.io** on ad-hoc projects
- **Upstash Redis** (rate limiting + cost guard)
- **Monorepo pnpm 9 + Turbo 2**
- **Monitoring**: Sentry + PostHog
- **Tests**: Vitest + Playwright (102 automated tests on morphow-api, in CI/CD)
- **CI/CD**: GitHub Actions + Vercel Preview

## Security

- **Custom HMAC-SHA256** (native Web Crypto API, on fusil.paris for Stripe webhook verification)
- **Custom in-memory rate limiting** on Vercel serverless
- **Timing-safe comparison** against timing attacks
- **Path whitelist** (allow-list) on admin proxy
- **HTTP headers**: CSP with frame-ancestors, HSTS 1 year, X-Frame-Options DENY, Permissions-Policy, Referrer-Policy
- **Strict CORS** by origin
- **XSS audit**: 3 vulnerabilities identified and fixed in internal audit on Microphage Analyzer Pro
- **Multi-tenant** with per-tenant isolation
- **Row Level Security (RLS)** on Supabase sensitive tables

## Payment and e-commerce

- **Stripe Checkout Sessions + Webhooks** (with custom HMAC verification)
- **PayPal** (create-order + capture-order)
- **Promo codes** with server-side validation
- **Bilingual FR/EN transactional emails** via Resend
- **Chronopost** multi-zone integration (FR / EU / Switzerland / UK / Worldwide)

## Workspace integrations

- **Google Calendar API** + **Google Drive API** in production on romainbigache.com (OAuth2 + Workspace API + tool streaming UI + Vercel cron for nightly sync)
- **OAuth + Workspace API + tool streaming** pattern mastered

## Project management tools

- **Methods**: agile (sprints, ceremonies), kanban
- **Tools**: Notion, Linear, GitHub Projects, Figma, Slack
- **BforBank environment**: ran with PM, Tribe Leader, marketing teams, customer service (SRC), management, and Compliance sign-off

## What I don't master (transparency)

Detail in [expertise.md](./expertise.md).

## Related

- [profile.md](./profile.md)
- [expertise.md](./expertise.md)
- [projects/microphage-analyzer-pro.md](./projects/microphage-analyzer-pro.md)
- [projects/altaria.md](./projects/altaria.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
- [projects/fusil-paris.md](./projects/fusil-paris.md)
