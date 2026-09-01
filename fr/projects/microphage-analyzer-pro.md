---
id: project-microphage-analyzer-pro
title: Microphage Analyzer Pro - Outil B2B IA pour l'UX writing
type: project
category: app
domain: project
tags: [microphage, b2b-saas, multi-tenant, ai, index-first, vision-llm, governed-vault]
status: live
created: 2026-04-30
updated: 2026-09-01
period: 2025-11 / present
client: Microphage (SASU)
industries: [SaaS, AI/ML, Design Tools]
team: 1 (Romain Bigache, solo)
url: null
demo: null
links:
  - experience/microphage.md
---

# Microphage Analyzer Pro

| Cle | Valeur |
|-----|--------|
| **Type** | Outil B2B SaaS multi-tenant IA pour l'UX writing |
| **Statut** | En production, premier déploiement client en cours |
| **Démarrage projet** | Novembre 2025 (création SASU + structuration produit) |
| **Entreprise** | Microphage (SASU) |
| **Industries** | SaaS, AI/ML, Design Tools |
| **Équipe** | Romain Bigache (seul) |

## Titre court

Outil B2B IA d'audit UX writing dans les workflows design.

## Genèse

Microphage Analyzer Pro est lancé en novembre 2025, en même temps que la création de Microphage (la mission BforBank touchait à sa fin). Le produit s'appuie sur trois ans de R&D personnelle antérieure en UX writing assisté par IA, consolidée et structurée en produit B2B autonome au moment de la création de Microphage.

## Description courte

Outil B2B IA qui audite, réécrit et conseille sur l'UX writing dans les workflows design. Plusieurs pilotes enterprise en pipeline.

## Description longue

### Problème

Les équipes design des grandes entreprises produisent des écrans en continu sans vérification systématique de la qualité du contenu. Les règles UX writing internes (charte éditoriale, ton, accessibilité, conformité) sont rarement appliquées de manière homogène. L'audit manuel coûte des heures de relecture par sprint.

### Solution

Microphage Analyzer Pro couvre l'audit, la réécriture, l'analyse statistique et les requêtes conversationnelles sur le content design system du client. Architecture multi-tenant conçue pour onboarder de nouveaux clients enterprise sans toucher au cœur produit.

Depuis mi-2026, le moteur tourne en index-first : un seul appel vision (service d'audit FastAPI + Gemini) reçoit un index compact du vault de règles gouverné (897 règles, une ligne par règle) plus la capture d'écran, ouvre les fiches complètes à la demande via un tool `read_rules`, déroule une critique designer adversariale, et rend verdicts et réécritures. Le vault lui-même est maintenu par un pipeline gouverné red/blue (rédacteurs de règles + gatekeeper) hérité de la méthode Karpathy LLM wiki.

Une web app compagnon et une interface chat autonome sont sur la roadmap pour étendre l'outil au-delà de la surface design.

## Impact

- Premier engagement client enterprise (edtech B2B), plusieurs pilotes en pipeline
- Architecture multi-tenant prête à accueillir de nouveaux clients

## Related

- [experience/microphage.md](../experience/microphage.md)
