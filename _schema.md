---
id: _schema
title: Wiki schema
type: meta
domain: wiki-conventions
tags: [meta, schema, conventions, llm-wiki]
status: live
created: 2026-04-30
updated: 2026-04-30
authority: source-of-truth
---

# Romain Bigache wiki schema

Reference document for understanding this wiki's structure and conventions.
Methodology: Karpathy LLM Wiki adapted to a professional profile.

## Principles

1. **Single source of truth.** Each fact exists in exactly one place. If a piece of info needs to appear in multiple files, it gets extracted into its own file and linked.
2. **Systematic YAML frontmatter.** All .md files have full frontmatter.
3. **Explicit cross-links.** A `## Related` section at the bottom of each file lists adjacent files.
4. **Atomic files.** One topic = one file. No mixing.
5. **Dense index.** README.md serves as the table of contents and exposes key facts as metadata.
6. **Regular linting.** Detect contradictions, gaps, orphan files.

## Required frontmatter

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique file identifier (slug, no extension) |
| `title` | string | Human-readable title |
| `type` | enum | See taxonomy below |
| `domain` | string | Functional domain (e.g. `experience`, `project`, `stack`) |
| `tags` | array | Keywords for LLM discovery |
| `status` | enum | `draft` / `live` / `archived` |
| `created` | date | Creation date (YYYY-MM-DD) |
| `updated` | date | Last modification date |

## Optional frontmatter

| Field | Type | Description |
|-------|------|-------------|
| `links` | array | List of related files (relative path) |
| `period` | string | Period (e.g. `2024-2025`) |
| `client` | string | Client name if project |
| `industries` | array | Industries addressed |
| `technologies` | array | Key technologies |
| `url` | string | Public URL if demo |
| `confidential` | bool | If some info needs to be redacted |
| `category` | enum | For `type: project` only. One of: `app` (software product), `tool` (internal tool), `site` (website), `case` (creative campaign). Used by the portfolio site to group projects. |

## Type taxonomy

- `meta`: structural documents (this schema, README)
- `profile`: identity, pitch, contact
- `cv`: raw CV
- `stack`: technical stack
- `availability`: availability and terms
- `expertise`: expertise focus
- `keywords`: ATS keywords and indexing
- `education`: education and self-learning
- `methodology`: signature methodologies
- `process`: daily operational process
- `writing`: blog articles, author voice
- `experience`: mission file (1 file per employer)
- `project`: project file (1 file per delivery)
- `personal`: off-work (sport, volunteering, side projects)
- `press`: external third-party content (testimonials, interviews, press mentions)

## Repo structure

```
Wiki-Romain-Bigache/
├── README.md              # Main index
├── _schema.md             # This file
├── profile.md             # Identity + pitch
├── cv.md                  # Raw CV
├── stack.md               # Technical stack
├── availability.md        # Availability + terms
├── expertise.md           # GCP / Gemini / connectors
├── keywords.md            # ATS keywords and indexing
├── education.md           # Education and self-learning
├── methodology.md         # Signature methodologies (Karpathy LLM Wiki, etc.)
├── process.md             # How I work day-to-day
├── writing.md             # Blog articles index
├── writing/               # Blog articles reproduced in full
│   ├── morphow-mascotte-ia.md
│   ├── vibe-coding-burnout.md
│   ├── ai-product-builder.md
│   ├── personal-branding-introvert.md
│   ├── content-design.md
│   └── entretiens.md
├── personal.md            # BJJ, volunteering, music label
├── experience/
│   ├── microphage.md
│   ├── bforbank.md
│   ├── adeo-leroy-merlin.md
│   ├── oxgen.md
│   ├── freelance-creative.md
│   ├── cdiscount.md
│   ├── fdj.md
│   ├── leboncoin.md
│   ├── speak-ux.md
│   └── havas-paris.md
└── projects/
    ├── microphage-analyzer-pro.md
    ├── altaria.md
    ├── la-plume-bforbank.md
    ├── fusil-paris.md
    ├── romainbigache-com.md
    └── mycelium.md
```

Source of truth for the file list: `git ls-files`. The tree above is indicative, not maintained by hand.

## Writing conventions

- Standard markdown (CommonMark + GFM tables).
- No em-dash. Use `:` or `-` or `,`.
- Internal links as relative paths: `[microphage](./experience/microphage.md)`.
- No unaccented sentences in French sources (full FR orthography upstream).
- `id` identifiers in kebab-case, no accents.
- Tags in kebab-case, no accents.

## Confidentiality

The only name still redacted is:
- `360Learning` -> "first B2B edtech client" (deployment contracted but in progress)

Kept by name:
- `Altarea` / `Altaria` (sale not finalized, non-sensitive case)
- `BforBank` (already public on LinkedIn and CV)
- `Ledger` (pitched by Marcel to the VP Design)
- `Tenexa` (white-label negotiation in progress)
- All former employers and OXGEN clients already public

## Lint

On every update, check:
- [ ] Frontmatter complete and valid
- [ ] No broken cross-links
- [ ] No duplicated info
- [ ] `updated` field refreshed
- [ ] No em-dash
- [ ] No nominal mention of `360Learning`

## Related

- [README.md](./README.md)
