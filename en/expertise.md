---
id: expertise
title: GCP / Gemini / Workspace / connectors expertise
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

# Applied AI expertise

Factual breakdown of expertise level by technology: what's in production, what isn't.

## Gemini: 2 years in production

La Plume at BforBank runs on Gemini 2.5 Pro. RAG architecture built in-house, prompts written in-house. In parallel, multi-provider via Vercel AI SDK v6 (OpenAI, Claude, Gemini) on every Microphage project: tool calling, streaming, evals.

Building with AI more broadly since GPT-3.5 shipped (November 2022) at ADEO: first internal prompt, then a RAG-powered Content Design System (ChatGPT + N8N + Supabase). So 3.5 years of cumulative practice on generative models.

Detail: [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Google Enterprise / Workspace: integrations in production

On romainbigache.com:
- Calendar API connected to the calendar with UI rendering streamed directly inside the AI chat (tool call with live rendering)
- Vercel cron for nightly sync
- Google Drive integrated on several other projects

OAuth + Workspace API + tool streaming UI pattern mastered.

## GCP / Vertex AI / Agent Builder: not in production

Current stack: Vercel + Cloudflare Workers + Supabase. No production work on GCP / Vertex AI / Agent Builder.

Familiar with the concepts and agent patterns (mastered on LangGraph + Vercel AI SDK).

Equivalent production-grade work delivered on other infrastructure:
- La Plume on LangGraph
- Microphage Analyzer Pro multi-tenant
- Altaria with HMAC + RLS security

## Salesforce / Zendesk connectors: not by name, equivalent pattern delivered

No nominal Salesforce or Zendesk integration.

Equivalent pattern delivered at BforBank: a custom RAG GPT bot that paired 3 heterogeneous internal sources (public FAQ, customer service tickets, customer service feedback) and generated 250+ LLM-ready articles in one month, deployed in production, feeding a customer chat connected inside the app.

That's exactly the pattern of a business-system connector: ingest a customer reference base, normalize it, generate structured content, serve it through an agent.

Detail: [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Production-grade in the strict sense

- 102 automated tests on morphow-api (unit + integration + e2e)
- 3 XSS vulnerabilities identified and fixed in internal audit on Microphage Analyzer Pro (no external pentest to date)
- Multi-tenant with rate limiter, CORS, auth middleware
- Sentry + PostHog monitoring
- CI/CD GitHub Actions + Vercel Preview

## Related

- [stack.md](./stack.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
