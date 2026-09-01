---
id: methodology
title: Signature methodologies
type: methodology
domain: technology
tags: [karpathy-llm-wiki, hybrid-retrieval, rag, prompt-caching, single-source-of-truth, methodology]
status: live
created: 2026-04-30
updated: 2026-05-23
links:
  - projects/microphage-analyzer-pro.md
  - projects/la-plume-bforbank.md
  - stack.md
---

# Signature methodologies

Recurring architectural patterns and working methods used across Microphage AI projects.

## LLM Wiki

Pattern for organizing business knowledge as a structured wiki: YAML frontmatter, single source of truth, atomic files, explicit cross-links. Business rules don't live in prompts, they live in the wiki.

I started tooling this approach on cds-wiki and Microphage Analyzer Pro before pushing the methodology much further. Andrej Karpathy published a gist in April 2026 that formalizes the same pattern more thoroughly: the convergence of both approaches confirmed the direction.

### Application on Microphage Analyzer Pro

- 785 UX writing rules structured into 17 categories in a proprietary wiki
- Single source of truth: zero rule hard-coded in prompts
- Frontmatter per rule (id, type, severity, domain, examples)
- Cross-links between related rules
- Tenant pack generation: derives a new client wiki without touching the core product

### Benefit

Editing a rule = editing a markdown file, no redeploy, no regression on other rules. Auditable, reviewable by non-techs (designers, content owners).

## 3-layer hybrid matcher

Retrieval pattern for matching a rule or a piece of knowledge in a dense wiki, with a controlled LLM budget.

### Layer 1 - Metadata filtering (80% of cases)

Filtering by tags / domain / type / locale in the YAML frontmatter. Very fast, very deterministic, covers most matches.

### Layer 2 - BM25 keyword search (15%)

If layer 1 doesn't decide: full-text BM25 search on the filtered corpus. Still zero LLM call, still fast.

### Layer 3 - LLM classifier (5% residual)

If layers 1 and 2 fail: LLM call in classifier mode on the remaining top-N candidates. LLM cost is minimal because the candidate set is already narrow.

### Benefit

Controlled LLM budget: 95% of matches happen with 0 LLM calls. Sub-second latency on most requests. Predictable API costs.

### Application

Microphage Analyzer Pro uses this pattern to match UX writing violations against 785 candidate rules, with acceptable p95 latency and predictable API cost even at multi-tenant scale.

## Heterogeneous internal source ingestion pattern

Reusable pattern to turn a fragmented client knowledge base into an LLM-ready corpus exploitable by an agent.

### Steps

1. **Scraping and retrieval** of existing sources (FAQ, help base, documentation)
2. **Source pairing**: cross-reference public FAQ + customer service tickets + customer service feedback to identify under-covered topics, redundancies, contradictions
3. **Normalization**: tone, structure, level of detail, granularity, phrasing, compliance
4. **LLM-ready rewriting**: clear title, identifiable intent, self-contained answer, alternative phrasings, explicit exclusions
5. **Production tooling**: custom RAG GPT bot to produce drafts at a sustainable pace, human validation at finalization

### Application at BforBank

250+ articles produced in one month from 3 heterogeneous internal sources (FAQ, customer service tickets, customer service feedback). Corpus deployed in production, feeding the in-app chat for logged-in customers.

### Transferable

Pattern directly applicable to Salesforce, Zendesk, ServiceNow connectors, or any enterprise ticketing / FAQ system.

Detail: [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Cycle compression (3-week solo POC)

Fast delivery method that removes the coordination of 3 trades on a POC.

### Principle

Hybrid profile designer + full-stack dev + content + change comms in a single person. No handover between trades, no intermediate specs, no cross-team validation cycles per deliverable.

### Conditions for success

- Clear client brief in 1 session
- Designated sponsor for fast arbitration
- Stable templated stack (Next.js + Vercel AI SDK + Supabase + Cloudflare Workers, same across projects)
- Production-grade security in the bootstrap skeleton (HMAC, RLS, rate limiting already templated)
- Mature internal tooling (cf [projects/mycelium.md](./projects/mycelium.md))

### Result

Altaria: 15 modules in production, 3 weeks, from brief to CAC40 C-suite pitch.

## Production-grade from day 1

Default position: every Microphage project starts with security + tests + monitoring patterns already in place, not in a post-MVP hardening phase.

### Systematic skeleton

- Zod validation on all inputs
- In-memory rate limiting or Upstash Redis
- HMAC-SHA256 on signed webhooks
- Supabase RLS on sensitive tables
- CSP + HSTS + Permissions-Policy by default
- Vitest unit + integration tests from the first commit
- Playwright e2e from the first user-facing screen
- Sentry + PostHog monitoring wired from kickoff

### Benefit

No security tech debt to repay at go-live. The POC is already prod-ready, the sales cycle can start at the demo.

## Interactive mockup as contract

Deliverable pattern for enterprise refontes of intranets, portals, and internal apps: a production-grade HTML mockup serves as the executable spec contract between stakeholders and the engineering team. Replaces flat Figma boards and PDF specs, which routinely drift during the build.

> Note: this methodology section is in active drafting (added 2026-05-23). Validated method, copy and naming may still iterate. Source of truth: [expertise/interactive-mockup.md](./expertise/interactive-mockup.md).

### Principle

Before a 500K to 2M EUR engineering investment, the cible must be walkable. The show home analogy applies: no one signs off on a 50-unit housing development without visiting the model home. The mockup IS the show home for the digital refonte.

### Stack

- HTML5 + Tailwind CSS compiled statically (no runtime framework cost)
- Vanilla JavaScript for interactions, no framework dependency
- Self-hosted fonts, optimized images, anti-CLS
- Deployed as static site on Vercel preview for live stakeholder walkthroughs

### Quality bar

- Lighthouse 90+ performance, 100 accessibility, 100 best practices, 100 SEO
- WCAG AA color contrast, heading order, aria labels, focus management
- Multi-theme support via [data-mode] attribute
- Bilingual content (FR and EN) via data-i18n attributes
- Responsive cross-device, mobile-first refined

### Process

Four steps, BTP analogy filed throughout: permit application (brief intake), foundation work (tokens and type system), show home build (full key pages), handover (engineering team takes mockup as build contract).

### Benefit

Eliminates spec drift between design and build. The engineering team has a contract, not an inspiration. Sales cycle compresses: executive committee validates the cible before allocating engineering budget. Cost compressed to 2 to 4 weeks instead of 2 to 4 months of dev-first prototyping.

### Application

Suez intranet refonte V1: 1,999-line single-page HTML, 8 themes, FR and EN, Lighthouse 93 / 100 / 100 / 100, WCAG AA, ServiceNow Service Portal target. Phase 1 delivered May 2026, Phase 2 (Brand Contract layer) in negotiation.

Detail: [expertise/interactive-mockup.md](./expertise/interactive-mockup.md).

## Related

- [expertise/interactive-mockup.md](./expertise/interactive-mockup.md)
- [projects/microphage-analyzer-pro.md](./projects/microphage-analyzer-pro.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
- [projects/mycelium.md](./projects/mycelium.md)
- [stack.md](./stack.md)
