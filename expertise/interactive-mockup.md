---
id: interactive-mockup
title: Interactive mockup as contract
type: expertise
domain: design-engineering
tags: [interactive-mockup, html-prototype, frontend-craft, design-system, enterprise-refonte, lighthouse, wcag-aa, multi-theme, bilingual, show-home, btp-analogy]
status: draft
created: 2026-05-23
updated: 2026-05-23
confidential: true
links:
  - ../methodology.md
  - ../projects/fusil-paris.md
  - ../stack.md
  - ../process.md
---

# Interactive mockup as contract

Standalone prestation for enterprise refontes of intranets, portals, and internal apps. Deliverable: a production-grade HTML mockup that serves as the executable spec between stakeholders and the engineering team. No more drift between Figma and the build.

## The show home analogy

Before building a 50-unit housing development, no one signs off without visiting the show home. You walk through it, you touch the walls, you open the closets, you validate. Once the show home is approved, the construction crew knows exactly what to reproduce.

The same logic applies to enterprise digital refontes: 500K to 2M EUR engineering investments are routinely greenlit on flat Figma boards and PDF specs that the build will drift from. The interactive mockup IS the show home. Click it, test it on mobile, audit accessibility, switch themes, switch language. Once validated, the engineering team has a contract, not an inspiration.

## Who it is for

Three recurring buyer profiles:

1. **Enterprise intranet refontes** (ServiceNow Service Portal, SharePoint moderne, custom platforms). Heads of Workplace, Heads of Internal Comms, DSI. The intranet has been carried around for 5 to 10 years, the executive committee needs to see the target before allocating budget to a 12-month rebuild.
2. **B2B SaaS portal refresh**. Product VPs, Heads of Design. The portal feels dated, sales loses deals on UX, but no one wants to commit dev resources without seeing the cible.
3. **Internal apps modernization** (HR, IT, ops tooling). Heads of internal product, IT directors. Tooling drift over years has stacked features without revision; the mockup forces alignment on the next-generation experience before the rebuild.

## What you get

A fully working HTML mockup, deployable as a static site, that includes:

- One to four key pages (home + 2 to 3 templates), depending on scope
- Production-grade performance (Lighthouse 90+ on performance, 100 on accessibility, best practices, SEO)
- WCAG AA accessibility compliance, audited via axe-core
- Multi-theme support if the brand requires it (8 themes maximum tested in the reference benchmark)
- Bilingual content (FR / EN by default), bound via data-i18n attributes for safe extension
- Responsive across mobile, tablet, desktop
- Self-hosted fonts, optimized images, lazy loading, anti-CLS
- Sticky header with auto-hide, accessible mobile drawer, micro-interactions polished to production standards
- Single index.html or modular .html files, deployed on Vercel preview for live validation

## How it works (4 steps, BTP analogy filed throughout)

### 1. Permit application (1 to 2 days)

Brief intake. Single session, structured notes. Constraints captured: existing brand, integration target (ServiceNow, SharePoint, custom), priority page set, accessibility level, target audience. Output: a one-pager scope document.

### 2. Foundation work (3 to 5 days)

Design tokens, type system, color system, spacing rhythm, component library. Aligned with the existing brand if it exists, structured from scratch if not. Output: foundations.css and the first hero shipped on Vercel preview. Multi-theme architecture wired if applicable.

### 3. Show home build (5 to 10 days)

Full key page set built. Accessibility audit pass via axe-core. Performance audit pass via Lighthouse. Responsive cross-device. Interaction polish (hover, focus, scroll behavior, micro-animations). Bilingual content wired. Deployed live on Vercel for stakeholder walkthroughs.

### 4. Handover (1 day)

Final walkthrough with the client. Documented design system if requested. Code handed over as a private repo. The construction team (Inetum, Capgemini, Atos, internal engineering, or third-party integrator) takes the HTML mockup as the spec contract for the rebuild. Optional decennial guarantee equivalent: design system code lives in a versioned repo, available for ongoing reference.

## Pricing (confidential, indicative)

| Scope | Price (EUR) |
|-------|-------------|
| Single-page validation mockup (home only) | 8,000 to 12,000 |
| Multi-page mockup (home + 2 to 3 pages) | 13,000 to 18,000 |
| Brand Contract layer (design tokens, voice, components in code) | +6,000 to 10,000 |
| Additional variant or theme iteration | +3,000 to 5,000 |
| Brand and tokens workshop (1 to 2 days on-site) | 3,000 to 5,000 |

Pricing posture: forfait per-scope. No hourly billing. No revisions beyond the agreed iteration count without re-negotiation.

## Differentiators vs alternatives

- **Versus Figma flat mockup**: an interactive HTML mockup eliminates the spec drift that happens when the build team interprets the design. Pixel-perfect, animations included, accessibility tested, performance measured.
- **Versus low-code prototyping (Webflow, Framer)**: production-grade code that can be lifted directly into a Next.js or vanilla integration. No vendor lock-in, no monthly fee on the deliverable.
- **Versus dev-first prototype**: cost compressed to 2 to 4 weeks instead of 2 to 4 months. The mockup is design-led, not engineering-led, so the cible is opinionated and validated before engineering scopes its sprint plan.

## Proof of work

- **Suez (CAC40, environmental services, 40,000 employees)**: intranet refonte direction artistique V1. Home page + content section, 8 brand themes, FR and EN, ServiceNow Service Portal target. Lighthouse 93 performance, 100 accessibility, 100 best practices, 100 SEO. WCAG AA. Status: Phase 1 delivered, Phase 2 (Brand Contract) in negotiation. To be anonymized in public publication until Phase 2 validation closes.
- **fusil.paris**: SEO and editorial refonte, content-driven mockup pattern applied to e-commerce.
- Additional case studies to add as missions close.

## Tools and stack

- HTML5 + Tailwind CSS (compiled statically for production)
- Vanilla JavaScript, no framework dependency
- PIL for image optimization (LANCZOS resize, quality 78-82, progressive)
- Lighthouse for performance auditing
- axe-core for accessibility auditing
- Playwright for automated visual auditing
- Vercel for staging and preview deployments
- Self-hosted Google Fonts via custom build script

## Sources

- Reference benchmark: Suez DA V1 mockup, 1,999 lines, Lighthouse 93 performance, 100 accessibility, 100 best practices, 100 SEO
- Method foundation: project Mycelium and the `_canonical/` design system documentation
- Reusable patterns: 22 universal patterns documented in `_canonical/patterns/UNIVERSAL-PATTERNS.md` (Mycelium)

## Related

- [methodology.md](../methodology.md)
- [projects/fusil-paris.md](../projects/fusil-paris.md)
- [stack.md](../stack.md)
- [process.md](../process.md)
