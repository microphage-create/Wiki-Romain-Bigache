---
id: project-romainbigache-com
title: romainbigache.com - Site personnel avec agent IA
type: project
category: site
domain: project
tags: [personal-site, oauth, google-workspace, calendar-api, drive-api, tool-streaming, vercel, next-js, ai-agent]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2025 / present
client: Personnel
industries: [Personal, AI/ML]
team: 1 (Romain Bigache, solo)
url: https://romainbigache.com
demo: https://romainbigache.com
technologies: [Next.js, TypeScript, Vercel AI SDK, OpenAI, Anthropic Claude, Google Calendar API, Google Drive API, OAuth2, Vercel Cron, tool calling, streaming UI]
links:
  - experience/microphage.md
  - expertise.md
  - stack.md
---

# romainbigache.com

| Cle | Valeur |
|-----|--------|
| **Type** | Site personnel + agent IA conversationnel |
| **Statut** | En production |
| **Année** | 2025 - en cours |
| **URL** | [romainbigache.com](https://romainbigache.com) |
| **Équipe** | Romain Bigache (seul) |

## Titre court

Site personnel avec agent IA conversationnel et intégrations Google Workspace en production.

## Description courte

Site portfolio + chat IA personnel adossé à Google Workspace (Calendar et Drive en prod). Démonstration concrète du pattern OAuth2 + Workspace API + tool streaming UI : l'agent peut consulter et résumer l'agenda, lire des documents Drive et streamer le rendu directement dans la conversation.

## Description longue

### Concept

Site personnel conçu comme démonstrateur produit : un agent IA conversationnel branché sur les outils Google Workspace de Marcel, qui sert simultanément de portfolio (l'agent peut commenter ses propres projets) et de preuve d'exécution sur le pattern Workspace integration en autonomie complète.

### Intégrations en production

- **Google Calendar API** : connexion OAuth2 à l'agenda perso, l'agent peut consulter les disponibilités, résumer la semaine, identifier les RDV. Rendu UI streamé directement dans le chat : le tool call exécute, les données arrivent, l'UI se construit en live au-dessus de la réponse texte.
- **Google Drive API** : OAuth2 sur Drive personnel, lecture de documents, résumés à la volée, navigation par dossiers. Sync nocturne via cron Vercel pour pré-indexer les documents récents.

### Architecture

- **Front** : Next.js 16, React 19, TypeScript strict, Tailwind, shadcn/ui
- **AI** : Vercel AI SDK v6 multi-provider (OpenAI, Anthropic Claude), tool calling, streaming UI
- **Auth** : OAuth2 Google avec refresh tokens, scopes minimaux (calendar.readonly, drive.readonly)
- **Cron** : Vercel Cron Jobs pour sync nocturne Drive
- **Déploiement** : Vercel serverless

### Pattern réutilisable

Le pattern complet (OAuth2 + Workspace API + tool streaming UI + cron sync) est documenté et réutilisable sur tout poste demandant une intégration Google Workspace, Microsoft Graph, ou tout autre Workspace API similaire (Notion, Slack, Linear).

## Technologies utilisees

- Next.js 16 (App Router)
- React 19
- TypeScript strict
- Tailwind CSS 4 + shadcn/ui
- Vercel AI SDK v6
- OpenAI API + Anthropic Claude API
- Google Calendar API + Google Drive API
- OAuth2 (refresh tokens, scope-limited)
- Vercel Cron Jobs
- Streaming UI (tool calls avec rendu live)

## Performance Lighthouse

Rapports du 30 avril 2026 (Lighthouse 13.0.1, HeadlessChromium 146).

### Page d'accueil `romainbigache.com/`

| Catégorie | Mobile |
|-----------|--------|
| **Performance** | 95 / 100 |
| **Accessibility** | 95 / 100 |
| **Best Practices** | 100 / 100 |
| **SEO** | 100 / 100 |

Core Web Vitals (mobile, Moto G Power, 4G lente) :

| Métrique | Valeur |
|----------|--------|
| First Contentful Paint (FCP) | 1,4 s |
| Largest Contentful Paint (LCP) | 2,0 s |
| Total Blocking Time (TBT) | 210 ms |
| Cumulative Layout Shift (CLS) | 0 |
| Speed Index | 3,1 s |

### Page portfolio `romainbigache.com/fr/portfolio`

| Catégorie | Mobile | Desktop |
|-----------|--------|---------|
| **Performance** | 99 / 100 | 99 / 100 |
| **Accessibility** | 95 / 100 | 95 / 100 |
| **Best Practices** | 100 / 100 | 100 / 100 |
| **SEO** | 100 / 100 | 100 / 100 |

Core Web Vitals (mobile) :

| Métrique | Valeur |
|----------|--------|
| First Contentful Paint (FCP) | 1,4 s |
| Largest Contentful Paint (LCP) | 1,8 s |
| Total Blocking Time (TBT) | 30 ms |
| Cumulative Layout Shift (CLS) | 0 |

Tous les Core Web Vitals dans le vert sur les deux pages. CLS = 0 (zéro saut visuel pendant le chargement). TBT = 30 ms sur portfolio (excellent, blocage minimal du thread principal).

## Impact

- Site en production sur [romainbigache.com](https://romainbigache.com)
- Lighthouse mobile home : 95 / 95 / 100 / 100
- Lighthouse mobile et desktop portfolio : 99 / 95 / 100 / 100
- SEO 100 / 100 sur toutes les pages testées
- Démonstrateur du pattern Google Workspace integration
- Sert de plateforme de démo lors des pitchs et entretiens
- Maintien hands-on des intégrations OAuth2 + tool streaming en autonomie

## Related

- [experience/microphage.md](../experience/microphage.md)
- [expertise.md](../expertise.md)
- [stack.md](../stack.md)
