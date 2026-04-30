---
id: project-mycelium
title: Mycelium - Internal Claude Code tooling
type: project
domain: project
tags: [mycelium, claude-code, agentic-coding, internal-tooling, productivity, mcp, slash-commands, subagents, hooks]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2026 / present
client: Personal / Microphage internal
industries: [Internal Tooling, AI/ML, Productivity]
team: 1 (Romain Bigache, solo)
url: null
demo: null
technologies: [Claude Code, MCP, slash commands, subagents, hooks, settings, memory, Markdown, YAML, Legifrance API, Judilibre API, Playwright, Python, TypeScript]
links:
  - experience/microphage.md
  - methodology.md
  - process.md
  - stack.md
---

# Mycelium

| Key | Value |
|-----|-------|
| **Type** | Internal Claude Code tooling (custom skills, subagents, hooks, memory) |
| **Status** | Internal production, ~30 active skills |
| **Year** | 2026 - ongoing |
| **Visibility** | Private repo (strategic asset) |
| **Team** | Romain Bigache (solo) |

## Short title

Internal Claude Code tooling stack to orchestrate solo multi-project work.

## Short description

Mycelium is the internal infrastructure that industrializes Marcel's solo work across all Microphage projects: ~30 domain-specific Claude Code skills, specialized subagents, session hooks, structured persistent memory. Lets the delivery pace hold (POC in 3 weeks) by automating cognitive boilerplate and wiring each skill to the right external APIs (Legifrance, Judilibre, Figma, GitHub, Stripe, etc.).

## Architecture

Mycelium applies the LLM Wiki pattern to internal tooling: single source of truth, lazy loading, atomic files per skill, conventioned frontmatter, cross-links between skills.

Methodology details: [methodology.md](../methodology.md).

### Skill families

#### Creative (4 skills)

- **`/copywriter`**: corporate writing, hooks, headlines, tone/audience adaptation, multi-language. Knowledge base of briefs and templates per client.
- **`/da`**: art direction, moodboards, art direction boards, visual identity.
- **`/prompt-oracle`**: AI image prompts (Gemini, DALL-E), visual styles, `.ico` and `.png` generation in a ComfyUI pipeline.
- **`/plannermaster`**: communication strategy, campaign plans, decks, market analyses.

#### Dev (8 skills)

- **`/portal`**: portal dev with Next.js + shadcn/ui + Turborepo. Drives squads via inter-skill queue.
- **`/portal-alpha`**: Factory Pipeline (json-render + Zod, AI app generation).
- **`/portal2`**: portal v2 (Next.js 16 + MUI v6 + Framer Motion + Supabase).
- **`/api`**: API dev with Hono + Zod + Supabase + Upstash Redis.
- **`/figma`**: B2C consumer Figma plugins (Extractor + Analyzer, TypeScript + esbuild).
- **`/figma-pro`**: B2B multi-tenant Analyzer Pro (pnpm + Turbo 2 + Hono Edge + Vitest + Playwright).
- **`/darwin-figma`**: iterative audit and optimization of Figma plugins across 8 dimensions.
- **`/nextjs`**: generic Next.js dev (init, pages, components, forms, API, DB, auth, SEO, tests, deploy, perf).

#### Ops (7 skills)

- **`/ops`**: DevToolsOps. Health checks, infra fixes, repo backups, secrets/junk/stale scans, desktop CLI tool crafting, tech watch (star-history tracking on the toolbox).
- **`/tri`**: file sorting, naming, cleanup. `dry` mode for scan-only without execution.
- **`/env-creator`**: secured `.env` generation, project secrets management.
- **`/team`**: orchestration of W1-W8 workers, parallel tasks with subagents.
- **`/audit`**: reliability audit, vulnerability detection, code review.
- **`/lint`**: linting of a markdown knowledge base (frontmatter, wikilinks, staleness, score /10).
- **`/capture`**: multi-viewport screenshots via Playwright (sites + localhost), dark/light, for book and portfolio.

#### Business (3 skills)

- **`/juriste`**: contract analysis, GDPR / T&Cs compliance, legal writing. **Wired to the Legifrance and Judilibre APIs** for official law and case law search. Knowledge base of analyses and contract templates.
- **`/devis`**: service quoting (dev, UX audit, e-learning, art direction, copy, AI), market grids, proposal generation.
- **`/carriere`**: resume, cover letters, professional emails, evolution tracking, skills assessment.

#### System (8 skills)

- **`/wiki`**: V4 wiki engine (785 rules, 17 categories, AN013 envelope). Modes: `lookup`, `stats`, `audit` (vision capture), `rewrite`, `corpus` (mining plugin-coach JSONs), `improve` (proposes rule changes), `diff` (backend vs LLM), `list`. Strict P0 lazy load.
- **`/save`** / **`/resume`**: session save with YAML frontmatter + resume by tags/skill.
- **`/auto-learn`**: capture session learnings into persistent memory.
- **`/review-weekly`**: weekly ritual (scan queues, save points, plans, memory, stale detection, 1-screen dashboard + actions).
- **`/mega-research`**: parallel research with 8 workers (subagents).
- **`/devil`**: adversarial attack, plan / code destruction, internal red team. Stress-tests architectures before delivery.
- **`/devil-loop`**: autonomous adversarial loop (devil running continuously).

#### Personal (2 skills)

- **`/modder`**: game modding (analyze engine, create mods, patch files, extract assets, personal wiki).
- **`/poe`**: Pillars of Eternity 1+2 build oracle (meta builds, theorycrafting, synergies).

### Specialized subagents

- **`Explore`**: fast codebase exploration agent (find files, search, codebase QA).
- **`Plan`**: software architect for step-by-step implementation designs.
- **`general-purpose`**: multi-step research and complex tasks.
- **`code-reviewer`**: second opinion on PRs, code audits.
- **Skill subagents**: darwin-skill, huashu-nuwa, shadcn-ui (skills wrapped as agents).

### Hooks and conventions

- **Session start**: check inter-skill queues, load context, activate skills based on arguments.
- **Registry update**: maintains a global index of available skills.
- **File protection**: forbids any modification of `.claude/` without confirmation.
- **Anti-duplication**: existence check before file creation.
- **Skill convention**: mandatory markdown template (META, STARTUP, RULES, WORKFLOW).

### Persistent memory

- `MEMORY.md`: main index, automatically loaded into context
- `memory/*.md`: atomic memories per topic (user, feedback, project, reference)
- Write-on-learn cycle: every user correction, architecture decision, or feedback is saved to memory for future sessions

## Why it's differentiating

Designer + dev + content + ops profile, all orchestrated by a custom Claude Code stack. Compresses the delivery cycle (POC in 3 weeks) by automating the cognitive boilerplate of each domain.

## Visibility

Private repo (internal strategic asset). Live demo walkthrough available under NDA.

## Related

- [methodology.md](../methodology.md)
- [process.md](../process.md)
- [experience/microphage.md](../experience/microphage.md)
- [stack.md](../stack.md)
