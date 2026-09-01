---
id: _schema
title: Schéma du wiki
type: meta
domain: wiki-conventions
tags: [meta, schema, conventions, llm-wiki]
status: live
created: 2026-04-30
updated: 2026-04-30
authority: source-of-truth
---

# Schéma du wiki Romain Bigache

Document de référence pour comprendre la structure et les conventions de ce wiki.
Méthodologie : Karpathy LLM Wiki adapté au profil pro.

## Principes

1. **Single source of truth.** Chaque fait n'existe qu'à un seul endroit. Si une info doit apparaître dans plusieurs fichiers, elle est extraite dans son propre fichier et linkée.
2. **Frontmatter YAML systématique.** Tous les fichiers .md ont un frontmatter complet.
3. **Cross-links explicites.** Section `## Related` en bas de chaque fichier qui liste les fichiers connexes.
4. **Fichiers atomiques.** Un sujet = un fichier. Pas de mélange.
5. **Index dense.** README.md sert de table des matières et expose les facts clés en metadata.
6. **Lint régulier.** Détecter contradictions, gaps, fichiers orphelins.

## Frontmatter requis

| Champ | Type | Description |
|-------|------|-------------|
| `id` | string | Identifiant unique du fichier (slug, sans extension) |
| `title` | string | Titre humain du document |
| `type` | enum | Voir taxonomie ci-dessous |
| `domain` | string | Domaine fonctionnel (ex: `experience`, `project`, `stack`) |
| `tags` | array | Mots-clés pour discovery LLM |
| `status` | enum | `draft` / `live` / `archived` |
| `created` | date | Date de création (YYYY-MM-DD) |
| `updated` | date | Date de dernière modif |

## Frontmatter optionnel

| Champ | Type | Description |
|-------|------|-------------|
| `links` | array | Liste de fichiers connexes (chemin relatif) |
| `period` | string | Période (ex: `2024-2025`) |
| `client` | string | Nom du client si projet |
| `industries` | array | Industries adressées |
| `technologies` | array | Technos clés |
| `url` | string | URL publique si demo |
| `confidential` | bool | Si certaines infos sont à flouter |
| `category` | enum | Pour `type: project` uniquement. Une valeur parmi : `app` (produit logiciel), `tool` (outil interne), `site` (site web), `case` (campagne créative). Utilisé par le site portfolio pour grouper les projets. |

## Taxonomie des types

- `meta` : documents de structure (ce schéma, README)
- `profile` : identité, pitch, contact
- `cv` : CV brut
- `stack` : stack technique
- `availability` : dispo et modalités
- `expertise` : focus expertise
- `keywords` : mots-clés ATS et indexation
- `education` : formation et autodidaxie
- `methodology` : méthodologies signature
- `process` : process opérationnel quotidien
- `writing` : articles de blog, voix d'auteur
- `experience` : fiche mission (1 fichier par employeur)
- `project` : fiche projet (1 fichier par réalisation)
- `personal` : hors-pro (sport, bénévolat, side projects)
- `press` : contenu tiers externe (témoignages, interviews, mentions presse)

## Structure du repo

```
Wiki-Romain-Bigache/
├── README.md              # Index principal
├── _schema.md             # Ce fichier
├── profile.md             # Identite + pitch
├── cv.md                  # CV brut
├── stack.md               # Stack technique
├── availability.md        # Dispo + modalites
├── expertise.md           # GCP / Gemini / connecteurs
├── keywords.md            # Mots-cles ATS et indexation
├── education.md           # Formation et autodidaxie
├── methodology.md         # Methodologies signature (Karpathy LLM Wiki, etc.)
├── process.md             # Comment je travaille au quotidien
├── writing.md             # Index des articles de blog
├── writing/               # Articles de blog reproduits integralement
│   ├── morphow-mascotte-ia.md
│   ├── vibe-coding-burnout.md
│   ├── ai-product-builder.md
│   ├── personal-branding-introvert.md
│   ├── content-design.md
│   └── entretiens.md
├── personal.md            # JJB, benevolat, label musique
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

Source de vérité pour la liste des fichiers : `git ls-files`. Cette arborescence est indicative, ne pas la maintenir à la main.

## Conventions de rédaction

- Markdown standard (CommonMark + GFM tables).
- Pas de tiret cadratin (em-dash). Utiliser `:` ou `-` ou `,`.
- Liens internes en chemin relatif : `[microphage](./experience/microphage.md)`.
- Pas de phrases sans accent (orthographe FR complète).
- Identifiants `id` en kebab-case sans accent.
- Tags en kebab-case sans accent.

## Confidentialité

Le seul nom encore flouté est :
- `360Learning` -> "premier client edtech B2B" (déploiement contractualisé mais en cours)

Sont conservés nominativement :
- `Altarea` / `Altaria` (vente non finalisée, cas non sensible)
- `BforBank` (mention déjà publique sur LinkedIn et CV)
- `Ledger` (pitché par Marcel au VP Design)
- `Tenexa` (négociation marque blanche en cours)
- Tous les anciens employeurs et clients OXGEN déjà publics

## Lint

À chaque mise à jour, vérifier :
- [ ] Frontmatter complet et valide
- [ ] Cross-links non cassés
- [ ] Pas de duplication d'info
- [ ] `updated` mis à jour
- [ ] Pas de tiret cadratin
- [ ] Pas de mention nominale `360Learning`

## Related

- [README.md](./README.md)
