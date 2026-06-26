---
id: project-my-suez
title: My Suez - intranet redesign
type: project
category: site
domain: project
tags: [microphage, my-suez, suez, intranet, enterprise, b2b, design-system, multi-bu, interactive-mockup, ai-codegen, servicenow, figma, horizon-design-system, figma-tokens, lighthouse, wcag-aa, bilingual]
status: in-progress
created: 2026-05-08
updated: 2026-06-26
period: 2026-05 / present
client: Suez (group)
industries: [Industry, Water, Waste, Energy]
technologies: [HTML5, Tailwind CSS, Vanilla JS, Figma, ServiceNow Service Portal, Lighthouse, axe-core, Playwright, Vercel]
team: 1 (Romain Bigache, solo)
url: null
demo: null
confidential: true
links:
  - experience/microphage.md
  - experience/oxgen.md
  - expertise/interactive-mockup.md
  - methodology.md
  - stack.md
---

# My Suez - Intranet redesign

| Key | Value |
|-----|-------|
| **Type** | Enterprise intranet redesign (direction artistique) |
| **Status** | Phase 1 validated, Phases 2 and 3 delivered (Figma rebuild on Horizon DS, design system themed), template pages rolling out |
| **Client** | Suez (group), CAC40, environmental services, ~40,000 employees |
| **Channel** | OXGEN (change communications agency, historical channel) |
| **Languages** | French, English |
| **Integration target** | ServiceNow Service Portal (Horizon Design System) |
| **Multi-BU** | Suez Group, Eau France, Recyclage & Valorisation, International |
| **Method** | Interactive HTML mockup first, AI-assisted, as the decision artifact |

## Short description

Direction artistique for the redesign of My Suez, the corporate intranet of the Suez group (water, waste, energy), serving around 40,000 employees from headquarters offices to field sites. The work led with a production-grade interactive HTML mockup, generated fast with AI codegen on top of a curated design system, used as the artifact the client decides on. Once the direction is locked, it feeds Figma as the integrator-facing source of truth for a native ServiceNow Service Portal build.

## Context

Suez ran a brand refresh in 2022 (new logo, expanded color palette) and is now reviewing its internal digital portal. The current My Suez is dated: terne, basic blue and green, no real point of view. The mission, brought in through OXGEN, is to give the executive committee and internal comms a target they can actually see and feel before committing budget to a multi-month rebuild.

Two structural constraints shape everything:

- **Dual audience.** Office staff at La Defense in front of a laptop eight hours a day, and field employees (water engineers, recycling operators, waste technicians) who read the intranet in a utilitarian way, fast, often on the move. The interface has to hold both.
- **Integration reality.** The final build ships in ServiceNow Service Portal, produced by a third-party integrator. The design cannot drift far from native Service Portal components, or it dies in maintainability. So the cible has to be ambitious visually and disciplined technically at the same time.

Scope of the exploration covers the home page plus content templates, addressing the IT support portal, HR self-service, business apps (HSE / incident reporting, purchasing, travel, training), directory and operational dashboards, and DSI / IT governance tooling.

## The core move: interactive mockup as the decision artifact

The bottleneck in enterprise intranet refontes is not design talent. It is the decision. Committees stall for weeks on flat Figma boards and PDF specs because no one can feel the product. They approve a direction they cannot test, then the build drifts from the boards, and everyone discovers the gap six months too late.

The move here was to skip the slow Figma-first loop and put a real, clickable, production-grade HTML mockup in front of the client instead. Stakeholders open it in a browser, navigate it, test it on mobile, switch theme, switch language. The direction gets chosen on an artifact people actually use, not on a static image.

This is the show home logic. No one greenlights a 50-unit housing development without walking through the show home first: touch the walls, open the closets, validate. The interactive mockup is the show home of the refonte. Click it, and the executive committee decides on something concrete.

The effect on the timeline is the whole point: the direction-choice compresses from weeks of back-and-forth on boards to a couple of days on a live artifact, and the downstream multi-month ServiceNow rebuild is de-risked before a single sprint is scoped.

## Why AI-assisted, and why it accelerates the choice

The mockup is built fast because it sits on two things: AI codegen and a curated, pre-built design system (the `_canonical/` craft reference and the brand token layer). The AI does not invent the design language, it accelerates the assembly of a language that is already opinionated and audited.

That combination collapses three trades into one person. On a classic setup, a direction this polished needs a designer, a front-end developer and a content designer, plus the coordination tax between them. Done solo, design plus code plus content in one head, that tax disappears, and a production-grade target lands in two to four weeks instead of two to four months.

Quality is not sacrificed for speed because the auditing is automated, not manual:

- **Lighthouse** for performance, accessibility, best practices, SEO
- **axe-core** for WCAG AA compliance
- **Playwright** for automated visual auditing across themes, variants and languages

So the artifact the client clicks is not a throwaway prototype. It is measured, accessible and deployable, which is exactly what makes it credible as a decision artifact and, later, as a contract.

## From mockup to Figma: the rebuild on Horizon DS

This is what actually happened, and it is the proof the method works. Phase 1 locked the direction on the interactive mockup. Phases 2 and 3 reproduced that mockup in Figma, as faithfully as possible, this time built from the native components of the Horizon Design System (the ServiceNow Service Portal design system). The HTML mockup stopped being a pitch and became the fidelity reference the Figma rebuild had to match.

Reproducing an opinionated direction with native components is where most refontes lose the design. Here the gap was closed with surgical customization, not a fork:

- **The carousel** required a genuine custom component. The grouped-news carousel the direction called for did not exist natively, so it was built as a real customization on top of the system.
- **A few other components** took lighter customizations, enough to honor the direction without breaking out of the native Horizon library.

The client was very happy with the result: the ambitious direction survived the move to native components.

Then the system was made reusable. The full design system plus the selected color palette went into Figma as tokens, and the theme was deployed onto the design system itself. From there the theme cascades: every other intranet page and template page can be declined from the themed DS, rather than redrawn one by one.

So the chain reads: the interactive HTML mockup locks the direction, the faithful Figma rebuild on Horizon DS makes it native and maintainable, Figma tokens plus a deployed theme turn it into a system that scales to the whole intranet, and the integrator ships it in ServiceNow Service Portal against that system.

## Constraints handled

- **ServiceNow Service Portal native components.** No custom-heavy widgets that the integrator cannot maintain. Per-card custom colors and a custom video player, for instance, are out because the platform does not support them cleanly. Encadrements and colored pictos, which the platform allows, carry the visual ambition instead.
- **Multi-BU theming.** Up to 8 brand themes tested, mapping Suez Group, Eau France, Recyclage & Valorisation and International to the same component code through token overrides. No fork.
- **Bilingual FR / EN** by default, content bound via data-i18n attributes for safe extension.
- **Dual audience density.** Clear hierarchy and high readability for field staff, enough information density for office power users. Mobile-friendly by default, even though mobile is not the V1 priority.
- **Brand discipline.** Expanded palette, more breathing room, more personality, a deliberate break from the dated current intranet, without leaving the official Suez charter.

## Results

Phase 1 (direction):

- **Lighthouse 93 performance, 100 accessibility, 100 best practices, 100 SEO** on the reference DA V1 mockup
- **WCAG AA** compliant, audited via axe-core
- Home page plus content section, with **up to 8 brand themes** and **FR / EN**
- Iteration cycle run as **2 directions, 2 rounds of adjustments**, each validated on the live mockup rather than on boards
- Deployed on a Vercel preview for stakeholder walkthroughs (link kept private)

Phases 2 and 3 (Figma rebuild and theming):

- Direction reproduced in Figma from native **Horizon Design System** components, validated by the client
- **Carousel** built as a genuine custom component, lighter customizations on a few others
- Full design system plus selected palette captured as **Figma tokens**
- **Theme deployed onto the design system**, so template pages and the rest of the intranet decline from it rather than being redrawn one by one

## What this case demonstrates

- **A role, not a deliverable.** AI Product Builder applied to enterprise design engineering: one person carrying design, code and content, using AI to compress the timeline without dropping production quality.
- **A method that de-risks budget.** The interactive mockup turns a multi-month, high-stakes rebuild into a decision made on a concrete, measured artifact, before the money is committed.
- **Enterprise fluency.** ServiceNow Service Portal constraints, multi-BU theming, accessibility, bilingual content, dual office and field audience, integrator handoff. The CIO-office context Romain has worked in through OXGEN for eight years.

## Tools and stack

- HTML5 plus Tailwind CSS, compiled statically for production
- Vanilla JavaScript, no framework dependency on the deliverable
- Figma for the integrator-facing design system layer
- ServiceNow Service Portal plus Horizon Design System as the integration target
- Lighthouse, axe-core and Playwright for automated performance, accessibility and visual auditing
- Self-hosted fonts, optimized images, lazy loading, anti-CLS
- Vercel for staging and live preview

## Related

- [experience/microphage.md](../experience/microphage.md)
- [experience/oxgen.md](../experience/oxgen.md)
- [expertise/interactive-mockup.md](../expertise/interactive-mockup.md)
- [methodology.md](../methodology.md)
- [stack.md](../stack.md)
