---
id: project-altaria
title: Altaria - AI Acculturation for Altarea (CAC40)
type: project
domain: project
tags: [altaria, altarea, cac40, copilot-365, gamification, pwa, hmac, rls, oxgen, solo, 3-weeks]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2025
client: Altarea (CAC40 real estate)
distribution: OXGEN
industries: [Real Estate, Education, AI/ML]
team: 1 (Romain Bigache, solo + OXGEN coordination)
url: https://altaria.microphage.ai/access
demo: https://altaria.microphage.ai/access
technologies: [Next.js 15, React 19, TypeScript 5.9, Tailwind CSS 4, Vercel AI SDK v4, OpenAI, Anthropic Claude, Supabase, Zod, HMAC-SHA256, RLS, PWA]
links:
  - experience/microphage.md
  - experience/oxgen.md
  - stack.md
---

# Altaria

| Key | Value |
|-----|-------|
| **Type** | Gamified AI acculturation web app |
| **Status** | POC delivered and demoed to the executive committee, commercial follow-up in discussion |
| **Year** | 2025 |
| **Company** | Altarea (end client, pitched via OXGEN) |
| **Industries** | Real Estate, Education, AI/ML |
| **Client size** | Large enterprise (CAC40) |
| **Team** | Romain Bigache, solo. OXGEN coordination on the brief and the pitch |
| **Demo** | [altaria.microphage.ai/access](https://altaria.microphage.ai/access) |
| **Production period** | 3 weeks solo |

## Short title

AI acculturation POC for a large CAC40 real estate group, shipped solo in 3 weeks.

## Short description

Gamified AI acculturation app for Altarea (CAC40), pitched via OXGEN ahead of the Microsoft Copilot 365 rollout. Shipped solo in 3 weeks: concept, architecture, code, design, learning content, illustrations and an internal guerrilla deployment campaign. Discussions for a white-label launch in progress.

**Live demo**: [altaria.microphage.ai/access](https://altaria.microphage.ai/access)

## Long description

### Context

Altarea, a CAC40 real estate group and a leader in low-carbon urban transformation, was preparing the rollout of Microsoft Copilot 365 to its employees. OXGEN was leading a three-stage adoption program: leadership address at the new year ceremony, teasing campaign, post-rollout Town Hall.

### Positioning

I drove Altaria as the product materialization of the adoption program. Not a classic training, not yet another IT tool: an app that delivers a gamified AI acculturation experience, designed as the human onboarding for the Copilot 365 rollout.

### Solo scope

Concept, architecture, code, design, learning content, illustrations, copy, deployment campaign. 3 weeks from brief to production. OXGEN coordination on the client brief and the executive committee pitch.

### Modules in production (15)

- **Hub** with XP bar and streak
- **Profile** with stats radar and 19 badges across 3 rarity tiers
- **Quiz** 30 questions across 3 levels
- **Training** with 3 worlds / 15 lessons / 75 activities
- **AI Lesson** (dynamic AI-generated content)
- **Bullshit?** (AI misinformation detection game)
- **Rocket Science** (educational arcade game with leaderboard)
- **Leaderboard** with 24 simulated NPCs
- **FAQ** 30 Q/A
- **Glossary** 30 terms
- **Discussion** (AI chat with two voice modes)
- **Prompter** (prompt generator and improver)
- **Deployment calendar**
- **Onboarding tour**
- **Built-in booking**

### Business use cases covered (from the client brief)

- Meeting summaries
- Pitch preparation
- Document and data analysis
- Visual creation

Each use case is grounded in the daily work of Altarea employees, across all subsidiaries.

### Adoption strategy - guerrilla campaign

Designed and illustrated with OXGEN an internal poster campaign across 5 physical media placed in everyday office waiting moments. Each medium carries a context-aware hook tied to its location and a QR code to the app. Visuals and copy by me.

### Access

Access restricted to the client's corporate WiFi (compliance constraint). Positive side effect: it reinforces the usage ritual and internal virality between colleagues, since the app only exists inside the offices.

### Application security from the POC

- HMAC-SHA256-signed sessions
- Zod validation on every input
- Per-endpoint rate limiting
- Supabase Row Level Security
- HTTP headers (HSTS, CSP with nonce, Permissions-Policy disabling camera / mic / geo)
- Kill switch and demo expiration date
- Custom anti-leak system (protecting learning content from export)

## Technologies used

- Next.js 15 (App Router)
- React 19
- TypeScript 5.9
- Tailwind CSS 4
- Vercel AI SDK v4 (multi-provider)
- OpenAI API and Anthropic Claude API
- Supabase (database, auth, RLS on 9 tables)
- Zod (schema validation)
- HMAC-SHA256-signed sessions
- Next.js middleware (access gate, CSP with nonce, kill switch, expiration date)
- Web Audio API (synthesized sounds)
- PWA (installable on mobile and desktop)

## Impact

- POC delivered solo in 3 weeks, from brief to production
- Live demo: [altaria.microphage.ai/access](https://altaria.microphage.ai/access)
- POC delivered and demoed to the client's executive committee, sale not finalized
- Discussions for a white-label launch with Tenexa
- Used as a commercial proof point on OXGEN's large-account (CAC40) pitches

## Related

- [experience/microphage.md](../experience/microphage.md)
- [experience/oxgen.md](../experience/oxgen.md)
- [stack.md](../stack.md)
