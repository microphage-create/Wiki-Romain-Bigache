---
id: project-altaria
title: Altaria - Acculturation IA pour Altarea (CAC40)
type: project
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
| **Type** | Application web gamifiee d'acculturation IA |
| **Statut** | POC livre et demontre au comex, suite commerciale en discussion |
| **Annee** | 2025 |
| **Entreprise** | Altarea (client final, pitche via OXGEN) |
| **Industries** | Immobilier, Education, AI/ML |
| **Taille client** | Grande entreprise (CAC40) |
| **Equipe** | Romain Bigache, seul. Coordination OXGEN sur le brief et le pitch |
| **Demo** | [altaria.microphage.ai/access](https://altaria.microphage.ai/access) |
| **Periode de production** | 3 semaines en solo |

## Titre court

POC d'acculturation IA pour grand compte foncier, shippe en 3 semaines en solo.

## Description courte

Application gamifiee d'acculturation a l'IA generative pour Altarea (CAC40), pitchee via OXGEN en amont du deploiement de Microsoft Copilot 365. Shippee en 3 semaines en solo : concept, architecture, code, design, contenu pedagogique, illustrations et campagne de deploiement guerilla. Discussions en cours pour distribution en marque blanche.

**Demo accessible** : [altaria.microphage.ai/access](https://altaria.microphage.ai/access)

## Description longue

### Contexte

Altarea, foncier du CAC40 et leader de la transformation urbaine bas carbone, preparait le deploiement de Microsoft Copilot 365 aupres de ses collaborateurs. OXGEN devait piloter un dispositif d'adoption en trois temps : prise de parole de la direction aux voeux, campagne teasing « choc d'adhesion », Town Hall post-deploiement. L'axe creatif retenu etait « WE ARE ALTARIA / NOUS SOMMES ALTARIA » : un claim, une application produit, une communaute.

### Positionnement

J'ai porte Altaria comme materialisation produit du claim. Pas une formation classique, pas un enieme outil informatique : une application qui incarne la promesse du slogan en proposant une experience d'acculturation IA gamifiee, pensee comme l'onboarding humain au deploiement de Copilot 365.

### Perimetre solo

Concept, architecture, code, design, contenu pedagogique, illustrations, copy, campagne de deploiement. 3 semaines du brief a la production. Coordination OXGEN sur le brief client et le pitch comex.

### Modules en production (15)

- **Hub** avec XP bar et streak
- **Profil** avec stats radar et 19 badges sur 3 niveaux de rarete
- **Quiz** 30 questions sur 3 niveaux
- **Formation** avec 3 mondes / 15 lecons / 75 activites
- **AI Lesson** (generation dynamique par IA)
- **Bullshit ?** (jeu de detection de desinformation IA)
- **Rocket Science** (jeu d'arcade pedagogique avec leaderboard)
- **Classement** avec 24 NPC simules
- **FAQ** 30 Q/R
- **Lexique** 30 termes
- **Discussion** (chat IA avec deux modes vocaux)
- **Prompter** (generateur et ameliorateur de prompts)
- **Calendrier** de deploiement
- **Onboarding tour**
- **Booking** integre

### Cas d'usage metier couverts (extraits du brief client)

- Redaction de compte-rendu
- Preparation d'argumentaire
- Analyse de documents et de donnees
- Creation de visuel

Chaque cas est ancre dans le quotidien des collaborateurs Altarea, toutes filiales confondues.

### Strategie d'adoption - campagne guerilla

Conception et illustration avec OXGEN d'une campagne d'affichage interne en 5 supports places dans les moments d'attente du quotidien : machine a cafe, ascenseur, toilettes, imprimante, miroir des sanitaires. Chaque support porte une accroche contextuelle au lieu et un QR code vers l'app. Visuels et copy de moi.

### Dramaturgie d'acces

L'app n'est accessible que via le wifi corporate. Securite (aucune donnee ne fuite a l'exterieur) et dramaturgie de l'experience (l'app n'existe que dans les bureaux, ce qui renforce le rituel d'usage et la viralite interne entre collegues).

### Securite applicative des le POC

- Sessions signees HMAC-SHA256
- Validation Zod sur toutes les entrees
- Rate limiting par endpoint
- Row Level Security Supabase sur 9 tables
- Headers HTTP (HSTS, CSP avec nonce, Permissions-Policy desactivant camera / micro / geo)
- Kill switch et date d'expiration de la demo
- Systeme Sentinel custom anti-leak

## Technologies utilisees

- Next.js 15 (App Router)
- React 19
- TypeScript 5.9
- Tailwind CSS 4
- Vercel AI SDK v4 (multi-provider)
- OpenAI API et Anthropic Claude API
- Supabase (base de donnees, auth, RLS sur 9 tables)
- Zod (validation schemas)
- Sessions HMAC-SHA256 signees
- Middleware Next.js (access gate, CSP avec nonce, kill switch, date d'expiration)
- Web Audio API (sons synthetises)
- PWA (installable sur mobile et desktop)

## Impact

- POC livre en 3 semaines en solo, du brief a la mise en production
- Demo accessible : [altaria.microphage.ai/access](https://altaria.microphage.ai/access)
- POC livre et demontre au comex client, vente non finalisee
- Negociation en cours avec une ESN HLD 1000 personnes pour relance en marque blanche
- Sert de preuve commerciale sur les pitchs grands comptes (CAC40) du cabinet OXGEN

## Related

- [experience/microphage.md](../experience/microphage.md)
- [experience/oxgen.md](../experience/oxgen.md)
- [stack.md](../stack.md)
