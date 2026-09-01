---
id: project-altaria
title: Altaria - Acculturation IA pour Altarea (CAC40)
type: project
category: app
domain: project
tags: [altaria, altarea, cac40, copilot-365, gamification, pwa, hmac, rls, oxgen, solo, 3-semaines]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2025
client: Altarea (foncier CAC40)
distribution: OXGEN
industries: [Immobilier, Education, AI/ML]
team: 1 (Romain Bigache, solo + coordination OXGEN)
url: https://altaria.microphage.ai/access
demo: https://altaria.microphage.ai/access
technologies: [Next.js 15, React 19, TypeScript 5.9, Tailwind CSS 4, Vercel AI SDK v4, OpenAI, Anthropic Claude, Supabase, Zod, HMAC-SHA256, RLS, PWA]
links:
  - experience/microphage.md
  - experience/oxgen.md
  - stack.md
---

# Altaria

| Cle | Valeur |
|-----|--------|
| **Type** | Application web gamifiée d'acculturation IA |
| **Statut** | POC livré et démontré au comex, suite commerciale en discussion |
| **Année** | 2025 |
| **Entreprise** | Altarea (client final, pitché via OXGEN) |
| **Industries** | Immobilier, Éducation, AI/ML |
| **Taille client** | Grande entreprise (CAC40) |
| **Équipe** | Romain Bigache, seul. Coordination OXGEN sur le brief et le pitch |
| **Démo** | [altaria.microphage.ai/access](https://altaria.microphage.ai/access) |
| **Période de production** | 3 semaines en solo |

## Titre court

POC d'acculturation IA pour grand compte foncier, shippé en 3 semaines en solo.

## Description courte

Application gamifiée d'acculturation à l'IA générative pour Altarea (CAC40), pitchée via OXGEN en amont du déploiement de Microsoft Copilot 365. Shippée en 3 semaines en solo : concept, architecture, code, design, contenu pédagogique, illustrations et campagne de déploiement guérilla. Discussions en cours pour distribution en marque blanche.

**Démo accessible** : [altaria.microphage.ai/access](https://altaria.microphage.ai/access)

## Description longue

### Contexte

Altarea, foncier du CAC40 et leader de la transformation urbaine bas carbone, préparait le déploiement de Microsoft Copilot 365 auprès de ses collaborateurs. OXGEN devait piloter un dispositif d'adoption en trois temps : prise de parole de la direction aux vœux, campagne teasing, Town Hall post-déploiement.

### Positionnement

J'ai porté Altaria comme matérialisation produit du dispositif d'adoption. Pas une formation classique, pas un énième outil informatique : une application qui propose une expérience d'acculturation IA gamifiée, pensée comme l'onboarding humain au déploiement de Copilot 365.

### Périmètre solo

Concept, architecture, code, design, contenu pédagogique, illustrations, copy, campagne de déploiement. 3 semaines du brief à la production. Coordination OXGEN sur le brief client et le pitch comex.

### Modules en production (15)

- **Hub** avec XP bar et streak
- **Profil** avec stats radar et 19 badges sur 3 niveaux de rareté
- **Quiz** 30 questions sur 3 niveaux
- **Formation** avec 3 mondes / 15 leçons / 75 activités
- **AI Lesson** (génération dynamique par IA)
- **Bullshit ?** (jeu de détection de désinformation IA)
- **Rocket Science** (jeu d'arcade pédagogique avec leaderboard)
- **Classement** avec 24 NPC simulés
- **FAQ** 30 Q/R
- **Lexique** 30 termes
- **Discussion** (chat IA avec deux modes vocaux)
- **Prompter** (générateur et améliorateur de prompts)
- **Calendrier** de déploiement
- **Onboarding tour**
- **Booking** intégré

### Cas d'usage métier couverts (extraits du brief client)

- Rédaction de compte-rendu
- Préparation d'argumentaire
- Analyse de documents et de données
- Création de visuel

Chaque cas est ancré dans le quotidien des collaborateurs Altarea, toutes filiales confondues.

### Stratégie d'adoption - campagne guérilla

Conception et illustration avec OXGEN d'une campagne d'affichage interne en 5 supports physiques placés dans les moments d'attente du quotidien des bureaux. Chaque support porte une accroche contextuelle au lieu et un QR code vers l'app. Visuels et copy de moi.

### Accès

Accès restreint au réseau corporate du client (contrainte conformité). Effet de bord positif : renforce le rituel d'usage et la viralité interne entre collègues, l'app n'existant que dans les bureaux.

### Sécurité applicative dès le POC

- Sessions signées HMAC-SHA256
- Validation Zod sur toutes les entrées
- Rate limiting par endpoint
- Row Level Security Supabase
- Headers HTTP (HSTS, CSP avec nonce, Permissions-Policy désactivant camera / micro / geo)
- Kill switch et date d'expiration de la démo
- Système custom anti-leak (protéger les contenus pédagogiques de l'export)

## Technologies utilisees

- Next.js 15 (App Router)
- React 19
- TypeScript 5.9
- Tailwind CSS 4
- Vercel AI SDK v4 (multi-provider)
- OpenAI API et Anthropic Claude API
- Supabase (base de données, auth, RLS sur 9 tables)
- Zod (validation schemas)
- Sessions HMAC-SHA256 signées
- Middleware Next.js (access gate, CSP avec nonce, kill switch, date d'expiration)
- Web Audio API (sons synthétisés)
- PWA (installable sur mobile et desktop)

## Impact

- POC livré en 3 semaines en solo, du brief à la mise en production
- Démo accessible : [altaria.microphage.ai/access](https://altaria.microphage.ai/access)
- POC livré et démontré au comex client, vente non finalisée
- Discussions pour un lancement en marque blanche avec Tenexa
- Sert de preuve commerciale sur les pitchs grands comptes (CAC40) du cabinet OXGEN

## Related

- [experience/microphage.md](../experience/microphage.md)
- [experience/oxgen.md](../experience/oxgen.md)
- [stack.md](../stack.md)
