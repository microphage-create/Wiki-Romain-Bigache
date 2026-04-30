---
id: project-mycelium
title: Mycelium - Outillage Claude Code interne
type: project
domain: project
tags: [mycelium, claude-code, agentic-coding, internal-tooling, productivity, mcp, slash-commands, subagents, hooks]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2026 / present
client: Personnel / Microphage interne
industries: [Internal Tooling, AI/ML, Productivity]
team: 1 (Romain Bigache, solo)
url: null
demo: null
technologies: [Claude Code, MCP, slash commands, subagents, hooks, settings, memory, Markdown, YAML, API Legifrance, API Judilibre, Playwright, Python, TypeScript]
links:
  - experience/microphage.md
  - methodology.md
  - process.md
  - stack.md
---

# Mycelium

| Cle | Valeur |
|-----|--------|
| **Type** | Outillage Claude Code interne (skills custom, subagents, hooks, memoire) |
| **Statut** | En production interne, ~30 skills actives |
| **Annee** | 2026 - en cours |
| **Visibilite** | Repo non public (asset strategique) |
| **Equipe** | Romain Bigache (seul) |

## Titre court

Stack d'outillage Claude Code interne pour orchestrer le travail multi-projet en solo.

## Description courte

Mycelium est l'infrastructure interne qui industrialise le travail solo de Marcel sur tous les projets Microphage : ~30 skills Claude Code dediees par domaine, subagents specialises, hooks de session, memoire persistante structuree. Permet de tenir le rythme de livraison (POC en 3 semaines) en automatisant le boilerplate cognitif et en branchant chaque skill aux bonnes APIs externes (Legifrance, Judilibre, Figma, GitHub, Stripe, etc.).

## Architecture

Mycelium applique le pattern LLM Wiki sur l'outillage interne : single source of truth, lazy loading, fichiers atomiques par skill, frontmatter conventionne, cross-links entre skills.

Detail methodologique : [methodology.md](../methodology.md).

### Familles de skills

#### Creative (4 skills)

- **`/copywriter`** : redaction corporate, hooks, headlines, adaptation ton/cible, multi-langue. Knowledge base de briefs et templates par client.
- **`/da`** : direction artistique, moodboards, planches DA, identite visuelle.
- **`/prompt-oracle`** : prompts image IA (Gemini, DALL-E), styles visuels, generation `.ico` et `.png` en pipeline ComfyUI.
- **`/plannermaster`** : strategie communication, plans de campagne, decks, analyses marche.

#### Dev (8 skills)

- **`/portal`** : dev portal Next.js + shadcn/ui + Turborepo. Pilote des squads via queue inter-skills.
- **`/portal-alpha`** : Factory Pipeline (json-render + Zod, generation IA d'apps).
- **`/portal2`** : portal v2 (Next.js 16 + MUI v6 + Framer Motion + Supabase).
- **`/api`** : dev API Hono + Zod + Supabase + Upstash Redis.
- **`/figma`** : plugins Figma B2C grand public (Extractor + Analyzer, TypeScript + esbuild).
- **`/figma-pro`** : Analyzer Pro B2B multi-tenant (pnpm + Turbo 2 + Hono Edge + Vitest + Playwright).
- **`/darwin-figma`** : audit et optimisation iterative des plugins Figma sur 8 dimensions.
- **`/nextjs`** : dev Next.js generique (init, pages, composants, forms, API, DB, auth, SEO, tests, deploy, perf).

#### Ops (7 skills)

- **`/ops`** : DevToolsOps. Health checks, fix infra, backup repos, scan secrets/junk/stale, craft d'outils desktop CLI, veille tech (suivi star-history sur la toolbox).
- **`/tri`** : rangement fichiers, nomenclature, nettoyage. Mode `dry` pour scan sans execution.
- **`/env-creator`** : generation `.env` securisee, gestion secrets projet.
- **`/team`** : orchestration de workers W1-W8, taches paralleles avec subagents.
- **`/audit`** : audit fiabilite, detection failles, review code.
- **`/lint`** : lint d'une knowledge base markdown (frontmatter, wikilinks, staleness, score /10).
- **`/capture`** : screenshots multi-viewport via Playwright (sites + localhost), dark/light, pour book et portfolio.

#### Business (3 skills)

- **`/juriste`** : analyse contrats, conformite RGPD / CGV, redaction juridique. **Rattachee aux API Legifrance et Judilibre** pour recherche en loi et jurisprudence officielles. Knowledge base d'analyses et templates de contrats.
- **`/devis`** : chiffrage de prestations (dev, audit UX, e-learning, DA, copy, IA), grilles de marche, generation de propales.
- **`/carriere`** : CV, lettres de motivation, mails professionnels, suivi d'evolution, bilan de competences.

#### System (8 skills)

- **`/wiki`** : V4 wiki engine (785 regles, 17 categories, AN013 envelope). Modes : `lookup`, `stats`, `audit` (vision capture), `rewrite`, `corpus` (mining JSONs plugin-coach), `improve` (propose modifs regle), `diff` (backend vs LLM), `list`. Lazy load strict P0.
- **`/save`** / **`/resume`** : sauvegarde session avec frontmatter YAML + reprise par tags/skill.
- **`/auto-learn`** : capture apprentissages session vers memoire persistante.
- **`/review-weekly`** : rituel hebdomadaire (scan queues, reprises, plans, memoire, detection stale, dashboard 1 ecran + actions).
- **`/mega-research`** : recherche parallele 8 workers (subagents).
- **`/devil`** : attaque adversariale, destruction de plans / code, red team interne. Permet de stress-tester les architectures avant livraison.
- **`/devil-loop`** : boucle adversariale autonome (devil en continu).

#### Personnal (2 skills)

- **`/modder`** : game modding (analyze engine, create mods, patch files, extract assets, wiki perso).
- **`/poe`** : Pillars of Eternity 1+2 build oracle (meta builds, theorycrafting, synergies).

### Subagents specialises

- **`Explore`** : agent d'exploration codebase rapide (find files, search, codebase QA).
- **`Plan`** : architecte logiciel pour designs d'implementation step-by-step.
- **`general-purpose`** : recherches multi-step et taches complexes.
- **`code-reviewer`** : second avis sur PR, audits de code.
- **Subagents de skill** : darwin-skill, huashu-nuwa, shadcn-ui (skills wrapped en agents).

### Hooks et conventions

- **Session start** : check queues inter-skills, charge contexte, active skills selon les arguments.
- **Registry update** : maintien d'un index global des skills disponibles.
- **File protection** : interdit toute modification de `.claude/` sans confirmation.
- **Anti-duplication** : check d'existence avant creation de fichier.
- **Convention skill** : template markdown obligatoire (META, STARTUP, REGLES, WORKFLOW).

### Memoire persistante

- `MEMORY.md` : index principal, charge automatiquement en contexte
- `memory/*.md` : memoires atomiques par sujet (user, feedback, project, reference)
- Cycle write-on-learn : chaque correction utilisateur, decision archi, ou feedback est saved en memoire pour futures sessions

## Pourquoi c'est differenciant

Profil designer + dev + content + ops, le tout orchestre par une stack Claude Code custom. Marcel ne se contente pas d'utiliser des outils IA : il les forge pour son propre flux de travail. C'est ce qui permet la compression du cycle (POC en 3 semaines) qui est sa signature commerciale.

L'outillage est meta-applique : Mycelium est documente exactement comme il documente les autres projets (frontmatter YAML, single source of truth, cross-links). Ce wiki Romain Bigache lui-meme est un produit de la methodologie Mycelium.

## Visibilite

Repo non public (asset strategique interne). Walkthrough disponible en demo live, dans un cadre confidentiel.

## Related

- [methodology.md](../methodology.md)
- [process.md](../process.md)
- [experience/microphage.md](../experience/microphage.md)
- [stack.md](../stack.md)
