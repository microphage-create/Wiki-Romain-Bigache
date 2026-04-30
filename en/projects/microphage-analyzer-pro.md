---
id: project-microphage-analyzer-pro
title: Microphage Analyzer Pro - B2B AI Figma Plugin
type: project
domain: project
tags: [microphage, figma-plugin, b2b-saas, multi-tenant, llm-wiki, hybrid-retrieval, prompt-caching, hono, cloudflare-workers]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2025-11 / present
client: Microphage (SASU)
industries: [SaaS, AI/ML, Design Tools]
team: 1 (Romain Bigache, solo)
url: null
demo: null
technologies: [TypeScript, Figma Plugin API, esbuild, pnpm 9, Turbo 2, Hono, Cloudflare Workers, OpenAI, Upstash Redis, Supabase, Sentry, PostHog, Vitest, Playwright]
links:
  - experience/microphage.md
  - stack.md
---

# Microphage Analyzer Pro

| Key | Value |
|-----|-------|
| **Type** | B2B SaaS multi-tenant Figma plugin |
| **Status** | In production, first client deployment in progress |
| **Project start** | November 2025 (SASU incorporation + product structuring) |
| **Company** | Microphage (SASU) |
| **Industries** | SaaS, AI/ML, Design Tools |
| **Team** | Romain Bigache (solo) |

## Short title

B2B Figma plugin for AI-driven UX writing audits.

## Genesis

Microphage Analyzer Pro launched in November 2025, alongside the incorporation of Microphage Intelligence (as the BforBank engagement was wrapping up). The product builds on three years of prior personal R&D: exploration of GPT-3.5 AI prompts at ADEO, first Figma prototype for UX writing analysis at BforBank, iterations on the LLM Wiki methodology and the editorial rules corpus. All this material was consolidated and structured into a standalone B2B product when Microphage was created.

## Short description

B2B Figma plugin that audits, rewrites and advises on UX writing in mockups via AI. 5 modes in production. Proprietary 785-rule wiki as a single source of truth (see [methodology.md](../methodology.md)). First deployment with a B2B edtech client (delivery May 2026), pitched to the VP Design of Ledger.

## Long description

### Problem

Design teams in large enterprises ship Figma screens continuously without systematic content quality checks. Internal UX writing rules (editorial guidelines, tone, accessibility, compliance) are rarely applied consistently. Manual audits cost hours of review per sprint.

### Solution

Microphage Analyzer Pro covers five usage modes:

1. **Audit**: analyzes a Figma selection and detects rule violations
2. **Rewrite**: proposes a compliant rewrite
3. **Rewrite-from-audit**: rewrites based on detected errors
4. **Insights**: statistical analysis on a project
5. **Chat**: queries the client's content design system

Audit and rewrite analyze both the visual capture and the Figma metadata extracted from the selected node (geometry, typography, naming, layer structure). Vision is the primary source of truth, metadata provides structural context.

### Architecture

The whole system follows the LLM Wiki pattern: a 785-rule UX writing wiki structured across 17 categories serves as the single source of truth, with zero business rules hard-coded into the prompts. Methodology details: [methodology.md](../methodology.md).

The hybrid matcher operates across 3 layers:
1. **Metadata filtering** (80% of cases)
2. **BM25 keyword search** (15%)
3. **LLM classifier** (5%, residual)

Multi-tenant architecture designed from day one to spin up a new tenant pack without touching the product core.

### Security

- 3 XSS vulnerabilities identified and fixed during internal audit (no external pentest to date)
- Rate limiting and cost guard via Upstash Redis
- Sentry + PostHog monitoring
- Vitest + Playwright tests in CI/CD

## Technologies used

- TypeScript strict
- pnpm 9 + Turbo 2 monorepo
- Figma plugin (Figma Plugin API, esbuild build)
- Hono backend on Cloudflare Workers
- OpenAI LLM (abstracted provider) with Anthropic prompt caching
- Proprietary UX writing Wiki V4 (785 rules, 17 categories)
- Rate limiting and cost guard via Upstash Redis
- Supabase database (reports table)
- Sentry + PostHog monitoring
- Vitest + Playwright tests
- GitHub Actions CI/CD + Vercel Preview

## Impact

- POC delivery in progress with a B2B edtech client (May 2026)
- Pitched to the VP Design of Ledger
- Multi-tenant architecture ready for client #2 signature

## Related

- [experience/microphage.md](../experience/microphage.md)
- [stack.md](../stack.md)
