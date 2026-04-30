---
id: methodology
title: Methodologies signature
type: methodology
domain: technology
tags: [karpathy-llm-wiki, hybrid-retrieval, rag, prompt-caching, single-source-of-truth, methodology]
status: live
created: 2026-04-30
updated: 2026-04-30
links:
  - projects/microphage-analyzer-pro.md
  - projects/la-plume-bforbank.md
  - stack.md
---

# Methodologies signature

Patterns architecturaux et methodes de travail recurrents utilises sur les projets IA Microphage.

## Karpathy LLM Wiki applique

Inspiree du pattern propose par Andrej Karpathy : organiser la connaissance metier comme un wiki structure (frontmatter YAML, single source of truth, fichiers atomiques, cross-links explicites) plutot que de coder les regles en dur dans les prompts.

### Application sur Microphage Analyzer Pro

- 785 regles UX writing structurees en 17 categories dans un wiki proprietaire
- Source de verite unique : zero regle codee en dur dans les prompts
- Frontmatter par regle (id, type, severite, domaine, exemples)
- Cross-links entre regles connexes
- Generation de pack tenant : derive un nouveau wiki client sans toucher au coeur produit

### Avantage

Modification d'une regle = modification d'un fichier markdown, sans redeploiement, sans regression sur les autres regles. Auditable, reviewable par non-techs (designers, content owners).

### Application sur ce wiki

Ce wiki Romain Bigache applique la meme methodologie sur la documentation pro : 22 fichiers .md atomiques, frontmatter YAML systematique, routing dans le README, cross-links via section `Related`.

Detail : [_schema.md](./_schema.md).

## Matcher hybride 3 couches

Pattern de retrieval pour matcher une regle ou une connaissance dans un wiki dense, avec un budget LLM controle.

### Couche 1 - Metadata filtering (80% des cas)

Filtrage par tags / domaine / type / locale dans le frontmatter YAML. Tres rapide, tres deterministe, couvre la majorite des matches.

### Couche 2 - BM25 keyword search (15%)

Si la couche 1 ne tranche pas : recherche full-text BM25 sur le corpus filtre. Toujours zero appel LLM, toujours rapide.

### Couche 3 - Classifier LLM (5% residual)

Si les couches 1 et 2 echouent : appel LLM en mode classifier sur les top-N candidats restants. Cout LLM minime car le candidate set est deja reduit.

### Avantage

Budget LLM controle : 95% des matches se font en 0 appel LLM. Latence sous-seconde sur la majorite des requetes. Couts API previsibles.

### Application

Microphage Analyzer Pro utilise ce pattern pour matcher les violations UX writing sur 785 regles candidates, avec une latence p95 acceptable et un cout API predictible meme a l'echelle multi-tenant.

## Pattern d'ingestion sources internes heterogenes

Pattern reutilisable pour transformer un referentiel client fragmente en corpus LLM-ready exploitable par un agent.

### Etapes

1. **Scraping et recuperation** des sources existantes (FAQ, base d'aide, documentation)
2. **Couplage des sources** : faire dialoguer FAQ publiques + tickets service client + retours SRC pour identifier sujets sous-traites, redondances, contradictions
3. **Homogeneisation** : ton, structure, niveau de detail, granularite, formulation, conformite
4. **Reecriture en format LLM-ready** : titre clair, intent identifiable, reponse autoportante, formulations alternatives, exclusions explicites
5. **Outil de production** : bot RAG GPT custom pour produire les drafts a un rythme tenable, validation humaine en finalisation

### Application sur BforBank

250+ articles produits en un mois a partir de 3 sources internes heterogenes (FAQ, tickets service client, retours SRC). Corpus deploye en production, alimente le chat in-app des clients connectes.

### Transposable

Pattern directement applicable a des connecteurs Salesforce, Zendesk, ServiceNow, ou tout systeme de gestion de tickets / FAQ d'entreprise.

Detail : [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Compression du cycle (POC 3 semaines en solo)

Methode de livraison rapide qui supprime la coordination de 3 metiers sur un POC.

### Principe

Profil hybride designer + dev full-stack + content + change comms en une seule personne. Pas de handover entre metiers, pas de specs intermediaires, pas de cycles de validation cross-equipe a chaque livrable.

### Conditions de reussite

- Brief client clair en 1 session
- Sponsor designe pour les arbitrages rapides
- Stack technique deja stabilisee (Next.js + Vercel AI SDK + Supabase + Cloudflare Workers, idem entre projets)
- Securite production-grade dans le squelette de demarrage (HMAC, RLS, rate limiting deja templates)
- Outillage interne mature (cf [projects/mycelium.md](./projects/mycelium.md))

### Resultat

Altaria : 15 modules en production, 3 semaines, du brief au pitch comex CAC40.

## Production-grade des le jour 1

Default position : tout projet Microphage demarre avec les patterns securite + tests + monitoring deja en place, pas en phase de durcissement post-MVP.

### Squelette systematique

- Validation Zod sur toutes les entrees
- Rate limiting in-memory ou Upstash Redis
- HMAC-SHA256 sur les webhooks signes
- RLS Supabase sur les tables sensibles
- CSP + HSTS + Permissions-Policy par defaut
- Tests Vitest unit + integration des le 1er commit
- Playwright e2e des le 1er ecran user-facing
- Monitoring Sentry + PostHog branches au demarrage

### Avantage

Pas de dette technique securite a rembourser au moment du go-live. Le POC est deja prod-ready, le cycle commercial peut s'engager des la demo.

## Related

- [projects/microphage-analyzer-pro.md](./projects/microphage-analyzer-pro.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
- [projects/mycelium.md](./projects/mycelium.md)
- [stack.md](./stack.md)
