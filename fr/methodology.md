---
id: methodology
title: Méthodologies signature
type: methodology
domain: technology
tags: [karpathy-llm-wiki, hybrid-retrieval, rag, prompt-caching, single-source-of-truth, methodology]
status: live
created: 2026-04-30
updated: 2026-05-23
links:
  - projects/microphage-analyzer-pro.md
  - projects/la-plume-bforbank.md
  - stack.md
---

# Méthodologies signature

Patterns architecturaux et méthodes de travail récurrents utilisés sur les projets IA Microphage.

## LLM Wiki

Pattern d'organisation de la connaissance métier comme un wiki structuré : frontmatter YAML, single source of truth, fichiers atomiques, cross-links explicites. La règle métier ne vit pas dans les prompts, elle vit dans le wiki.

J'ai commencé à outiller cette logique sur cds-wiki et Microphage Analyzer Pro, sans avoir encore poussé la méthodologie très loin. Andrej Karpathy a publié en avril 2026 un gist qui formalise le même pattern de manière plus complète : la rencontre des deux approches a confirmé la direction.

### Application sur Microphage Analyzer Pro

- 785 règles UX writing structurées en 17 catégories dans un wiki propriétaire
- Source de vérité unique : zéro règle codée en dur dans les prompts
- Frontmatter par règle (id, type, sévérité, domaine, exemples)
- Cross-links entre règles connexes
- Génération de pack tenant : dérive un nouveau wiki client sans toucher au cœur produit

### Avantage

Modification d'une règle = modification d'un fichier markdown, sans redéploiement, sans régression sur les autres règles. Auditable, reviewable par non-techs (designers, content owners).

## Matcher hybride 3 couches

Pattern de retrieval pour matcher une règle ou une connaissance dans un wiki dense, avec un budget LLM contrôlé.

### Couche 1 - Metadata filtering (80% des cas)

Filtrage par tags / domaine / type / locale dans le frontmatter YAML. Très rapide, très déterministe, couvre la majorité des matches.

### Couche 2 - BM25 keyword search (15%)

Si la couche 1 ne tranche pas : recherche full-text BM25 sur le corpus filtré. Toujours zéro appel LLM, toujours rapide.

### Couche 3 - Classifier LLM (5% residual)

Si les couches 1 et 2 échouent : appel LLM en mode classifier sur les top-N candidats restants. Coût LLM minime car le candidate set est déjà réduit.

### Avantage

Budget LLM contrôlé : 95% des matches se font en 0 appel LLM. Latence sous-seconde sur la majorité des requêtes. Coûts API prévisibles.

### Application

Microphage Analyzer Pro utilise ce pattern pour matcher les violations UX writing sur 785 règles candidates, avec une latence p95 acceptable et un coût API prédictible même à l'échelle multi-tenant.

## Pattern d'ingestion sources internes hétérogènes

Pattern réutilisable pour transformer un référentiel client fragmenté en corpus LLM-ready exploitable par un agent.

### Étapes

1. **Scraping et récupération** des sources existantes (FAQ, base d'aide, documentation)
2. **Couplage des sources** : faire dialoguer FAQ publiques + tickets service client + retours SRC pour identifier sujets sous-traités, redondances, contradictions
3. **Homogénéisation** : ton, structure, niveau de détail, granularité, formulation, conformité
4. **Réécriture en format LLM-ready** : titre clair, intent identifiable, réponse autoportante, formulations alternatives, exclusions explicites
5. **Outil de production** : bot RAG GPT custom pour produire les drafts à un rythme tenable, validation humaine en finalisation

### Application sur BforBank

250+ articles produits en un mois à partir de 3 sources internes hétérogènes (FAQ, tickets service client, retours SRC). Corpus déployé en production, alimente le chat in-app des clients connectés.

### Transposable

Pattern directement applicable à des connecteurs Salesforce, Zendesk, ServiceNow, ou tout système de gestion de tickets / FAQ d'entreprise.

Détail : [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md).

## Compression du cycle (POC 3 semaines en solo)

Méthode de livraison rapide qui supprime la coordination de 3 métiers sur un POC.

### Principe

Profil hybride designer + dev full-stack + content + change comms en une seule personne. Pas de handover entre métiers, pas de specs intermédiaires, pas de cycles de validation cross-équipe à chaque livrable.

### Conditions de réussite

- Brief client clair en 1 session
- Sponsor désigné pour les arbitrages rapides
- Stack technique déjà stabilisée (Next.js + Vercel AI SDK + Supabase + Cloudflare Workers, idem entre projets)
- Sécurité production-grade dans le squelette de démarrage (HMAC, RLS, rate limiting déjà templates)
- Outillage interne mature (cf [projects/mycelium.md](./projects/mycelium.md))

### Résultat

Altaria : 15 modules en production, 3 semaines, du brief au pitch comex CAC40.

## Production-grade dès le jour 1

Default position : tout projet Microphage démarre avec les patterns sécurité + tests + monitoring déjà en place, pas en phase de durcissement post-MVP.

### Squelette systématique

- Validation Zod sur toutes les entrées
- Rate limiting in-memory ou Upstash Redis
- HMAC-SHA256 sur les webhooks signés
- RLS Supabase sur les tables sensibles
- CSP + HSTS + Permissions-Policy par défaut
- Tests Vitest unit + integration dès le 1er commit
- Playwright e2e dès le 1er écran user-facing
- Monitoring Sentry + PostHog branchés au démarrage

### Avantage

Pas de dette technique sécurité à rembourser au moment du go-live. Le POC est déjà prod-ready, le cycle commercial peut s'engager dès la demo.

## Maquette interactive comme contrat

Pattern de livrable pour les refontes d'intranets, portails et applications internes en entreprise : une maquette HTML production-grade sert de spécification exécutable entre les parties prenantes et l'équipe de développement. Remplace les planches Figma plates et les specs PDF, dont le build s'écarte régulièrement.

> Note : cette section méthodologie est en cours de drafting actif (ajoutée 2026-05-23). Méthode validée, copy et nommage peuvent encore itérer. Source de vérité : [expertise/interactive-mockup.md](./expertise/interactive-mockup.md).

### Principe

Avant un investissement développement de 500K à 2M EUR, la cible doit être traversable. L'analogie de la maison témoin s'applique : personne ne signe pour un lotissement de 50 maisons sans avoir visité la maison témoin. La maquette EST la maison témoin de la refonte digitale.

### Stack

- HTML5 + Tailwind CSS compilé statiquement (aucun coût framework runtime)
- JavaScript vanilla pour les interactions, aucune dépendance framework
- Polices self-hosted, images optimisées, anti-CLS
- Déployé en site statique sur Vercel preview pour les walkthroughs live avec les parties prenantes

### Standard de qualité

- Lighthouse 90+ performance, 100 accessibilité, 100 best practices, 100 SEO
- Contraste de couleur WCAG AA, ordre des headings, aria labels, gestion du focus
- Support multi-thèmes via attribut [data-mode]
- Contenu bilingue (FR et EN) via attributs data-i18n
- Responsive cross-device, mobile-first refined

### Processus

Quatre étapes, analogie BTP filée du début à la fin : permis de construire (brief intake), fondations (tokens et système typographique), construction de la maison témoin (set complet de pages clés), réception de chantier (l'équipe de développement reprend la maquette comme contrat de build).

### Avantage

Élimine la dérive de spec entre design et build. L'équipe de développement a un contrat, pas une inspiration. Le cycle commercial se compresse : le comité exécutif valide la cible avant d'allouer le budget d'ingénierie. Coût compressé à 2 à 4 semaines au lieu de 2 à 4 mois de prototypage dev-first.

### Application

Refonte intranet Suez V1 : maquette HTML single-page de 1 999 lignes, 8 thèmes, FR et EN, Lighthouse 93 / 100 / 100 / 100, WCAG AA, cible ServiceNow Service Portal. Phase 1 livrée en mai 2026, Phase 2 (couche Brand Contract) en négociation.

Détail : [expertise/interactive-mockup.md](./expertise/interactive-mockup.md).

## Related

- [expertise/interactive-mockup.md](./expertise/interactive-mockup.md)
- [projects/microphage-analyzer-pro.md](./projects/microphage-analyzer-pro.md)
- [projects/la-plume-bforbank.md](./projects/la-plume-bforbank.md)
- [projects/mycelium.md](./projects/mycelium.md)
- [stack.md](./stack.md)
