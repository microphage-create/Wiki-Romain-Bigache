---
id: _schema
title: Schema du wiki
type: meta
domain: wiki-conventions
tags: [meta, schema, conventions, llm-wiki]
status: live
created: 2026-04-30
updated: 2026-04-30
authority: source-of-truth
---

# Schema du wiki Romain Bigache

Document de reference pour comprendre la structure et les conventions de ce wiki.
Methodologie : Karpathy LLM Wiki adapte au profil pro.

## Principes

1. **Single source of truth.** Chaque fait n'existe qu'a un seul endroit. Si une info doit apparaitre dans plusieurs fichiers, elle est extraite dans son propre fichier et linkee.
2. **Frontmatter YAML systematique.** Tous les fichiers .md ont un frontmatter complet.
3. **Cross-links explicites.** Section `## Related` en bas de chaque fichier qui liste les fichiers connexes.
4. **Fichiers atomiques.** Un sujet = un fichier. Pas de melange.
5. **Index dense.** README.md sert de table des matieres et expose les facts cles en metadata.
6. **Lint regulier.** Detecter contradictions, gaps, fichiers orphelins.

## Frontmatter requis

| Champ | Type | Description |
|-------|------|-------------|
| `id` | string | Identifiant unique du fichier (slug, sans extension) |
| `title` | string | Titre humain du document |
| `type` | enum | Voir taxonomie ci-dessous |
| `domain` | string | Domaine fonctionnel (ex: `experience`, `project`, `stack`) |
| `tags` | array | Mots-cles pour discovery LLM |
| `status` | enum | `draft` / `live` / `archived` |
| `created` | date | Date de creation (YYYY-MM-DD) |
| `updated` | date | Date de derniere modif |

## Frontmatter optionnel

| Champ | Type | Description |
|-------|------|-------------|
| `links` | array | Liste de fichiers connexes (chemin relatif) |
| `period` | string | Periode (ex: `2024-2025`) |
| `client` | string | Nom du client si projet |
| `industries` | array | Industries adressees |
| `technologies` | array | Technos cles |
| `url` | string | URL publique si demo |
| `confidential` | bool | Si certaines infos sont a flouter |

## Taxonomie des types

- `meta` : documents de structure (ce schema, README)
- `profile` : identite, pitch, contact
- `cv` : CV brut
- `stack` : stack technique
- `availability` : dispo et modalites
- `expertise` : focus expertise
- `keywords` : mots-cles ATS et indexation
- `education` : formation et autodidaxie
- `methodology` : methodologies signature
- `process` : process operationnel quotidien
- `experience` : fiche mission (1 fichier par employeur)
- `project` : fiche projet (1 fichier par realisation)
- `personal` : hors-pro (sport, benevolat, side projects)

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
├── personal.md            # JJB, benevolat, label musique
├── experience/
│   ├── microphage.md
│   ├── bforbank.md
│   ├── adeo-leroy-merlin.md
│   ├── oxgen.md
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

Source de verite pour la liste des fichiers : `git ls-files`. Cette arborescence est indicative, ne pas la maintenir a la main.

## Conventions de redaction

- Markdown standard (CommonMark + GFM tables).
- Pas de tiret cadratin (em-dash). Utiliser `:` ou `-` ou `,`.
- Liens internes en chemin relatif : `[microphage](./experience/microphage.md)`.
- Pas de phrases sans accent (orthographe FR complete).
- Identifiants `id` en kebab-case sans accent.
- Tags en kebab-case sans accent.

## Confidentialite

Certains noms sont floutes pour preserver les negociations en cours :
- `360Learning` -> "premier client edtech B2B"
- `Ledger` -> "VP Design d'un acteur hardware crypto"
- `Tenexa` -> "ESN HLD 1000 personnes"

Sont conserves nominativement :
- `Altarea` / `Altaria` (vente non finalisee, cas non sensible)
- `BforBank` (mention deja publique sur LinkedIn et CV)
- Tous les anciens employeurs et clients OXGEN deja publics

## Lint

A chaque mise a jour, verifier :
- [ ] Frontmatter complet et valide
- [ ] Cross-links non casses
- [ ] Pas de duplication d'info
- [ ] `updated` mis a jour
- [ ] Pas de tiret cadratin
- [ ] Pas de mention nominale `360Learning` / `Ledger` / `Tenexa`

## Related

- [README.md](./README.md)
