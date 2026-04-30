---
id: process
title: How I work
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

# How I work

Daily operational process on Microphage projects. For recruiters and buyers wondering how a solo builder ships production-grade AI products in 3 weeks.

## Pilot stack

- **Claude Code** as the main dev environment (IDE + agentic coding)
- **Mycelium**: internal tooling (custom skills, subagents, hooks, memory) that industrializes routines, see [projects/mycelium.md](./projects/mycelium.md)
- **Notion + Linear + GitHub Projects** for roadmap and task tracking
- **Figma** for design (UI + plugins)
- **Slack** for clients on long-running missions

## Typical dev cycle

### Phase 1 - Framing (1-2 days)

- Client brief in a single session, structured note-taking
- Specs written in markdown inside the repo (single source of truth)
- Architecture document (ADR) on structuring choices: runtime, LLM provider, database, auth
- Delivery plan broken into pre-accepted stories

### Phase 2 - Build (short cycle)

- Templated stack: Next.js 16 + Vercel AI SDK + Supabase + Cloudflare Workers or Vercel serverless
- Security skeleton from day 1 (HMAC, RLS, rate limiting, CSP, HSTS, Zod validation)
- Vitest unit + integration tests on critical modules from the first commit
- Playwright e2e as soon as UI is exposed to the user
- Sentry + PostHog monitoring wired in initial setup
- CI/CD GitHub Actions + Vercel Preview for continuous reviews

### Phase 3 - Delivery

- Live client demo in real conditions (no slides)
- Progressive rollout: preview > staging > production
- User and technical documentation shipped with the product
- Handover or maintenance, depending on the contract

## Operational principles

### Production-grade from day 1

No "shitty MVP" phase, no security tech debt to repay. The POC is already prod-ready. Detail: [methodology.md](./methodology.md).

### Cycle compression

1 person = 0 coordination. Concept + architecture + code + design + copy + go-to-market in the same head. No handover, no intermediate specs, no cross-team validation cycles.

### Continuous documentation

Every structuring decision (architecture, library choice, pattern) is documented as an ADR or a note in the repo. Memory doesn't live in the head, it lives in the code.

### Active technical monitoring

Daily tracking of releases: Vercel AI SDK, LangGraph, shadcn/ui, Next.js, Supabase, LLM providers. Active monitoring of emerging patterns (MCP, prompt caching, hybrid retrieval).

## AI tooling in daily work

- **Claude Code**: agentic coding, refactors, audits, test generation
- **Vercel AI SDK**: multi-provider on every project (OpenAI + Anthropic + Gemini)
- **Tool calling and streaming UI**: pattern reused on romainbigache.com and client apps
- **MCP**: used on internal projects to expose knowledge sources to agents
- **Anthropic prompt caching**: cost optimization on recurring contexts

## Posture in mission

- **End-to-end autonomy** on framed scopes
- **Stakeholder management** mastered (proof: full agile in a Compliance-driven banking environment at BforBank, 50+ campaigns run for enterprise CIO offices via OXGEN)
- **Direct communication**: no useless jargon, no over-documentation, no verbose status updates
- **Anti-bullshit**: if an approach isn't working or a brief is unstable, flag it early
- **Long-term commitment possible** on long missions, freelance via SASU Microphage Intelligence

## Related

- [projects/mycelium.md](./projects/mycelium.md)
- [methodology.md](./methodology.md)
- [stack.md](./stack.md)
- [availability.md](./availability.md)
