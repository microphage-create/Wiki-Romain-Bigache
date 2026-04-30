---
id: project-microphage-analyzer-pro
title: Microphage Analyzer Pro - Plugin Figma B2B IA
type: project
domain: project
tags: [microphage, figma-plugin, b2b-saas, multi-tenant, llm-wiki, hybrid-retrieval, prompt-caching, hono, cloudflare-workers]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2024 / present
client: Microphage (SASU)
industries: [SaaS, AI/ML, Design Tools]
team: 1 (Romain Bigache, solo)
url: null
demo: null
technologies: [TypeScript, Figma Plugin API, esbuild, pnpm 9, Turbo 2, Hono, Cloudflare Workers, OpenAI, Upstash Redis, Supabase, Sentry, PostHog, Vitest, Playwright]
links:
  - experience/microphage.md
  - stack.md
---

# Microphage Analyzer Pro

| Cle | Valeur |
|-----|--------|
| **Type** | Plugin Figma B2B SaaS multi-tenant |
| **Statut** | En production, premier deploiement client en cours |
| **Annee** | 2024 - en cours |
| **Entreprise** | Microphage (SASU) |
| **Industries** | SaaS, AI/ML, Design Tools |
| **Equipe** | Romain Bigache (seul) |

## Titre court

Plugin Figma B2B d'audit UX writing par IA

## Description courte

Plugin Figma B2B qui audite, reecrit et conseille sur l'UX writing des maquettes via IA. 5 modes en production. Architecture Karpathy LLM Wiki avec 785 regles structurees comme source de verite unique. Premier deploiement chez un client edtech B2B (livraison mai 2026), pitche au VP Design d'un acteur hardware crypto.

## Description longue

### Probleme

Les equipes design des grandes entreprises produisent des ecrans Figma en continu sans verification systematique de la qualite du contenu. Les regles UX writing internes (charte editoriale, ton, accessibilite, conformite) sont rarement appliquees de maniere homogene. L'audit manuel coute des heures de relecture par sprint.

### Solution

Microphage Analyzer Pro couvre cinq modes d'usage :

1. **Audit** : analyse une selection Figma et detecte les violations de regles
2. **Rewrite** : propose une reecriture conforme
3. **Rewrite-from-audit** : reecrit a partir des erreurs detectees
4. **Insights** : analyse statistique sur un projet
5. **Chat** : interroge le content design system du client

L'audit et le rewrite analysent a la fois la capture visuelle et les metadonnees Figma extraites du noeud selectionne (geometrie, typographie, naming, structure des calques). La vision sert de source de verite primaire, les metadonnees fournissent le contexte structurel.

### Architecture

L'ensemble suit la methodologie Karpathy LLM Wiki : un wiki de 785 regles UX writing structurees en 17 categories sert de source de verite unique, sans aucune regle metier codee en dur dans les prompts.

Le matcher hybride opere sur 3 couches :
1. **Metadata filtering** (80% des cas)
2. **BM25 keyword search** (15%)
3. **Classifier LLM** (5%, residual)

Architecture multi-tenant pensee des le depart pour generer un nouveau pack tenant sans toucher au coeur produit.

### Securite

- 3 vulnerabilites XSS critiques identifiees et corrigees en audit
- Rate limiting et cost guard via Upstash Redis
- Monitoring Sentry + PostHog
- Tests Vitest + Playwright en CI/CD

## Technologies utilisees

- TypeScript strict
- Monorepo pnpm 9 + Turbo 2
- Plugin Figma (Figma Plugin API, build esbuild)
- Backend Hono sur Cloudflare Workers
- LLM OpenAI (provider abstrait) avec prompt caching Anthropic
- Wiki UX writing V4 proprietaire (785 regles, 17 categories)
- Rate limiting et cost guard via Upstash Redis
- Base de donnees Supabase (table reports)
- Monitoring Sentry + PostHog
- Tests Vitest + Playwright
- CI/CD GitHub Actions + Vercel Preview

## Impact

- POC en cours de livraison chez un client edtech B2B (mai 2026)
- Pitche devant le VP Design d'un acteur hardware crypto
- Architecture multi-tenant prete pour la signature client #2

## Related

- [experience/microphage.md](../experience/microphage.md)
- [stack.md](../stack.md)
