---
id: project-mycelium
title: Mycelium - Outillage Claude Code interne
type: project
category: tool
domain: project
tags: [mycelium, claude-code, agentic-coding, internal-tooling, productivity, mcp, slash-commands, subagents, hooks]
status: live
created: 2026-04-30
updated: 2026-05-07
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
| **Type** | Outillage Claude Code interne (skills custom, subagents, hooks, mémoire) |
| **Statut** | En production interne, ~30 skills actives |
| **Année** | 2026 - en cours |
| **Visibilité** | Repo non public (asset stratégique) |
| **Équipe** | Romain Bigache (seul) |

## Titre court

Stack d'outillage Claude Code interne pour orchestrer le travail multi-projet en solo.

## Description courte

Mycelium est l'infrastructure interne qui industrialise le travail solo de Marcel sur tous les projets Microphage : ~30 skills Claude Code dédiées par domaine, subagents spécialisés, hooks de session, mémoire persistante structurée. Permet de tenir le rythme de livraison (POC en 3 semaines) en automatisant le boilerplate cognitif et en branchant chaque skill aux bonnes APIs externes (Legifrance, Judilibre, Figma, GitHub, Stripe, etc.).

## Architecture

Mycelium applique le pattern LLM Wiki sur l'outillage interne : single source of truth, lazy loading, fichiers atomiques par skill, frontmatter conventionné, cross-links entre skills.

Détail méthodologique : [methodology.md](../methodology.md).

### Familles de skills

#### Creative (4 skills)

- **`/copywriter`** : rédaction corporate, hooks, headlines, adaptation ton/cible, multi-langue. Knowledge base de briefs et templates par client.
- **`/da`** : direction artistique, moodboards, planches DA, identité visuelle.
- **`/prompt-oracle`** : prompts image IA (Gemini, DALL-E), styles visuels, génération `.ico` et `.png` en pipeline ComfyUI.
- **`/plannermaster`** : stratégie communication, plans de campagne, decks, analyses marché.

#### Dev (8 skills)

- **`/portal`** : dev portal Next.js + shadcn/ui + Turborepo. Pilote des squads via queue inter-skills.
- **`/portal-alpha`** : Factory Pipeline (json-render + Zod, génération IA d'apps).
- **`/portal2`** : portal v2 (Next.js 16 + MUI v6 + Framer Motion + Supabase).
- **`/api`** : dev API Hono + Zod + Supabase + Upstash Redis.
- **`/figma`** : plugins Figma B2C grand public (Extractor + Analyzer, TypeScript + esbuild).
- **`/figma-pro`** : Analyzer Pro B2B multi-tenant (pnpm + Turbo 2 + Hono Edge + Vitest + Playwright).
- **`/darwin-figma`** : audit et optimisation itérative des plugins Figma sur 8 dimensions.
- **`/nextjs`** : dev Next.js générique (init, pages, composants, forms, API, DB, auth, SEO, tests, deploy, perf).

#### Ops (7 skills)

- **`/ops`** : DevToolsOps. Health checks, fix infra, backup repos, scan secrets/junk/stale, craft d'outils desktop CLI, veille tech (suivi star-history sur la toolbox).
- **`/tri`** : rangement fichiers, nomenclature, nettoyage. Mode `dry` pour scan sans exécution.
- **`/env-creator`** : génération `.env` sécurisée, gestion secrets projet.
- **`/team`** : orchestration de workers W1-W8, tâches parallèles avec subagents.
- **`/audit`** : audit fiabilité, détection failles, review code.
- **`/lint`** : lint d'une knowledge base markdown (frontmatter, wikilinks, staleness, score /10).
- **`/capture`** : screenshots multi-viewport via Playwright (sites + localhost), dark/light, pour book et portfolio.

#### Business (3 skills)

- **`/juriste`** : analyse contrats, conformité RGPD / CGV, rédaction juridique. **Rattachée aux API Legifrance et Judilibre** pour recherche en loi et jurisprudence officielles. Knowledge base d'analyses et templates de contrats.
- **`/devis`** : chiffrage de prestations (dev, audit UX, e-learning, DA, copy, IA), grilles de marché, génération de propales.
- **`/carriere`** : CV, lettres de motivation, mails professionnels, suivi d'évolution, bilan de compétences.

#### System (8 skills)

- **`/wiki`** : V4 wiki engine (785 règles, 17 catégories, AN013 envelope). Modes : `lookup`, `stats`, `audit` (vision capture), `rewrite`, `corpus` (mining JSONs plugin-coach), `improve` (propose modifs règle), `diff` (backend vs LLM), `list`. Lazy load strict P0.
- **`/save`** / **`/resume`** : sauvegarde session avec frontmatter YAML + reprise par tags/skill.
- **`/auto-learn`** : capture apprentissages session vers mémoire persistante.
- **`/review-weekly`** : rituel hebdomadaire (scan queues, reprises, plans, mémoire, détection stale, dashboard 1 écran + actions).
- **`/mega-research`** : recherche parallèle 8 workers (subagents).
- **`/devil`** : attaque adversariale, destruction de plans / code, red team interne. Permet de stress-tester les architectures avant livraison.
- **`/devil-loop`** : boucle adversariale autonome (devil en continu).

#### Personnal (2 skills)

- **`/modder`** : game modding (analyze engine, create mods, patch files, extract assets, wiki perso).
- **`/poe`** : Pillars of Eternity 1+2 build oracle (meta builds, theorycrafting, synergies).

### Skills phares

Une poignée de skills sont profondément outillées, pas de simples wrappers de slash-command. Trois des plus abouties :

#### `/devil-loop` - Boucle adversariale autonome

Produit -> une attaque adversariale en 15 phases (`/devil`) cherche les failles -> auto-fix de toutes les objections -> nouvelle attaque -> ... boucle jusqu'à `0 CRITICAL + 0 HIGH + 0 MEDIUM`, ou jusqu'à la limite `--max-iterations` (défaut 15). Pas de "acceptable avec réserves" : on sort à zéro ou on continue. Par conception, aucune intervention utilisateur entre les passes. L'attaquant de l'itération N+1 attaque à froid, sans mémoire des passes précédentes, ce qui force les corrections à exister dans le texte plutôt que dans les intentions. Détection de stagnation : si le score d'erreurs ne bouge pas sur deux itérations, la boucle change d'approche (reformulation, restructuration) au lieu de patcher ; trois stagnations déclenchent une sortie forcée avec diagnostic. Un rapport markdown horodaté est écrit pour chaque run (sortie propre, max atteint, stagnation, annulation) sous `_system/reports/devil-loop/`, avec le vecteur de progression : `[13] -> [4] -> [0]`. Fonctionne sur prose, code, architecture, specs. Utilisée en production sur outputs de recherche au long cours, briefs d'opportunité produit, et sur les fichiers de skill eux-mêmes, pour les durcir avant déploiement.

![devil-loop](../../assets/skills/devil-loop.png)

#### `/copywriter` - Machine à copy multi-mode avec base de connaissances lazy-loadée

Cinq modes : créatif (slogans, jeux de mots, social, campagnes, roast) ; brief (analyse, création) ; web (landing, UX writing, email, CTA, pricing) ; visuals (bridge vers `/prompt-oracle`) ; portal (édition chat depuis l'application portail). Base de connaissances de 24 fichiers spécialisés, lazy-loadés via une table de routage qui plafonne à 3 fichiers par tâche pour tenir le budget de contexte. `BRIEFS-INDEX.yaml` par client avec filtrage `status: active | done`, le picker de démarrage n'affiche que le travail vivant. Workflow forcé : analyse -> deux ou trois directions de concept -> validation utilisateur -> production seulement après. Treize principes durs distillés depuis des sessions en production (la clarté bat le malin, pas de pronom ambigu, la spécificité bat la généralité, pas de claim sans preuve). Export MCP Canva natif (PRO avec repères de coupe plus REGULAR), convention de nommage forcée (`[CLIENT]_[BRIEF]_[TYPE]_[DDMMYY]_v[N].[ext]`), Prez Engine pour des decks HTML standalone depuis un brief YAML unique. Le mode portal émet des blocs `EDIT: slideId/elementEl` que le portail affiche en cartes diff Apply / Reject, une révision copy peut donc partir depuis un téléphone.

![copywriter](../../assets/skills/copywriter.png)

#### `/prompt-oracle` - Orchestrateur de prompts image et ComfyUI (Gemini 2.5 Flash)

Huit modes spécialisés accessibles depuis un menu d'en-tête : PROMPT (prompt Gemini unique optimisé), WORKFLOW (workflow ComfyUI JSON complet), BATCH (série de variations), CHARACTER (character sheet multi-poses avec identité cohérente), REFINE (prompt existant amélioré via Devil Loop), DOCS (consultation documentation), UI SCAN (analyse une capture d'UI et propose illustrations, icônes, empty states), 3D ICON (icônes 3D clay ou glossy à fond transparent). Bridge ComfyUI : écrit les prompts, peut lancer le serveur local, puis `/copywriter fetch` ramène les images générées dans le dossier de livrable client correspondant. Cibles de coût et de latence affichées dans l'en-tête : Gemini 2.5 Flash, ~$0,04 par image, 3-5 secondes de génération. Reference-driven par conception : un brief vague ("a nice professional image") est rejeté avec une demande de référence visuelle précise au lieu d'être honoré. Les images générées sont auto-routées vers le dossier client/projet correspondant, l'output atterrit directement là où le livrable est en cours d'assemblage. Cas de référence : [J'ai généré 352 mascottes IA](../writing/morphow-mascotte-ia.md) détaille cette skill appliquée au projet de mascotte Morphow.

![prompt-oracle](../../assets/skills/prompt-oracle.png)

### Subagents spécialisés

- **`Explore`** : agent d'exploration codebase rapide (find files, search, codebase QA).
- **`Plan`** : architecte logiciel pour designs d'implémentation step-by-step.
- **`general-purpose`** : recherches multi-step et tâches complexes.
- **`code-reviewer`** : second avis sur PR, audits de code.
- **Subagents de skill** : darwin-skill, huashu-nuwa, shadcn-ui (skills wrapped en agents).

### Hooks et conventions

- **Session start** : check queues inter-skills, charge contexte, active skills selon les arguments.
- **Registry update** : maintien d'un index global des skills disponibles.
- **File protection** : interdit toute modification de `.claude/` sans confirmation.
- **Anti-duplication** : check d'existence avant création de fichier.
- **Convention skill** : template markdown obligatoire (META, STARTUP, REGLES, WORKFLOW).

### Mémoire persistante

- `MEMORY.md` : index principal, chargé automatiquement en contexte
- `memory/*.md` : mémoires atomiques par sujet (user, feedback, project, reference)
- Cycle write-on-learn : chaque correction utilisateur, décision archi, ou feedback est saved en mémoire pour futures sessions

## Pourquoi c'est différenciant

Profil designer + dev + content + ops, le tout orchestré par une stack Claude Code custom. Permet la compression du cycle de delivery (POC en 3 semaines) en automatisant le boilerplate cognitif de chaque domaine.

## Visibilité

Repo non public (asset stratégique interne). Walkthrough disponible en démo live, dans un cadre confidentiel.

## Related

- [methodology.md](../methodology.md)
- [process.md](../process.md)
- [experience/microphage.md](../experience/microphage.md)
- [stack.md](../stack.md)
