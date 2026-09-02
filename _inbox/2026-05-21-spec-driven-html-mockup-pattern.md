---
title: "Spec-driven development : pourquoi le single-page HTML est la bonne méthode pour les mockups premium en 2026"
date: 2026-05-21
tags: [design-system, methodologie, mockup, cross-framework, ai-native, design-tokens, dtcg, suez-da-v1]
status: inbox
type: making-of
source-conversation: Session Suez DA V1, 21 mai 2026
---

# Spec-driven development : pourquoi le single-page HTML est la bonne méthode pour les mockups premium

## Contexte de la conversation

Session de 8h+ sur la maquette Suez DA V1 (mission OxGen × Suez IT). Output : mockup HTML single-page Lighthouse 93/100/100/100, WCAG AA full, 8 thèmes, FR/EN, déployé sur Vercel pour validation client Heloise Mesquita / Renée Clément. Restitution mardi 26 mai 2026.

Pendant la phase "audit / capitalisation", Marcel a soulevé une question critique : **single-page HTML mockup est-il la bonne méthode, ou un pattern accidentel ?**

## La méthode que Marcel pratique (sans le nommer)

1. Mockup en **HTML single-page** (Tailwind, vanilla JS, inline CSS) pour valider la DA
2. Itérations rapides avec client (zéro build, edit + refresh)
3. **Traduction ad-hoc** vers le framework cible (ServiceNow Service Portal, React, etc.) en phase de livraison

Cette approche a un nom officiel : **"Spec-driven development"** ou **"Mockup-first development"**. La maquette HTML/CSS/JS EST la spec exécutable. Le code prod est une compilation de cette spec.

Différence avec "wireframe → mockup Figma → code" classique : le mockup n'est pas une image, c'est déjà du code qui marche.

## Pour cette méthode

- **Output mesurable** : Lighthouse 93/100/100/100, WCAG AA, FCP 2.0s sur 4G simulé
- **Vitesse d'itération** : 200+ edits en une session vs 20 si setup React + Storybook
- **Communication client** : Heloise ouvre un lien, navigue. Pas besoin d'expliquer un Storybook
- **AI-friendly** : 1999 lignes dans un fichier unique = Claude voit tout d'un coup. Avec 50 composants React éclatés, on perd le contexte global
- **Source of truth visuelle** : pas de drift entre maquette et code
- **Compatibilité présentation** : tourne partout (Vercel, FTP, email link)
- **Pas d'abstraction qui ment** : ce que tu vois EST ce qu'on livre

## Quand cette méthode marche bien

- Mockup de validation client (1-2 semaines de cycle)
- DA / direction artistique où le visuel et l'interaction sont les livrables
- Sites éditoriaux (portfolio, landing, hub corporate, marketing)
- Quand le code final sera un framework différent (ServiceNow, SharePoint, intégrateur legacy)
- Quand l'IA est dans le workflow : single file = AI voit tout

## Quand cette méthode foire

- App produit long-terme : 50 écrans, gestion d'état, data fetching → React/Vue/Svelte from day 1
- Multi-page avec composants partagés réels → copy-paste = drift inévitable
- Équipe de 5+ devs → friction collaborative sur un fichier de 2000 lignes
- Tests unitaires de composants → impossible sans extraction

## Le vrai gap de la méthode (et son nom)

**Phase 2 : la traduction.** Quand on doit livrer du code à un intégrateur (Inetum pour ServiceNow Service Portal) ou à un dev React, **comment garantir que la traduction préserve les patterns, les tokens, l'identité ?**

Aujourd'hui = ad-hoc, à la main, à chaque client. Risque de drift entre maquette validée et code livré.

## L'état du marché 2026 (réponse honnête)

Personne n'a vraiment résolu "composant universel cross-framework". Les tentatives sérieuses :

- **shadcn/ui** : React/Next.js ONLY. Les ports (svelte, vue, solid) sont **community-driven, maintenus séparément**, pas une source unique. Drift inévitable.
- **Mitosis (Builder.io)** : JSX → React/Vue/Svelte/Solid/Angular. Marche pour des composants simples, foire sur les patterns complexes.
- **Web Components / Lit** : standard W3C, mais adoption limitée (problèmes styling cross-shadow-DOM, accessibility héritée)
- **Penpot, Visual Copilot, Anima, Locofy** : design-to-code, un framework à la fois, qualité variable
- **Style Dictionary (Amazon)** : tokens JSON → CSS/iOS/Android. **Uniquement les tokens, pas les composants**.
- **DTCG (Design Tokens Community Group)** : standard ouvert W3C pour les tokens. Adopté Adobe/Microsoft/Salesforce. Pas pour composants.

**Le gap structurel est réel.** Pas juste pour les freelances design system, pour l'industrie entière.

## Le pattern complet manquant

```
1. Single-page HTML mockup        (rapide pour valider client)
            ↓
2. Extraction patterns vers DS     (spec markdown/JSON, brand-agnostic)
            ↓
3. Compilation multi-target        (AI-driven : HTML brut ServiceNow, React shadcn, Vue, etc.)
            ↓
4. Tokens semantic partagés         (garantie cohérence visuelle cross-target)
```

Étape 1 = maîtrisée. Étape 4 = embryonnaire (morphow-kit a déjà les 3-layer tokens raw/semantic/component). **Étapes 2 et 3 manquent**.

## Pourquoi c'est le bon moment de creuser

3 forces alignées en 2026 :

1. **Adoption IA mainstream** : Claude / Cursor / Codex peuvent générer du code idiomatique multi-framework depuis une spec
2. **Standardisation tokens** : DTCG devient le standard W3C, adopté par les big tech. Le format spec est mûr.
3. **Démocratisation Figma → Code** : les designers veulent que leurs specs vivent dans le code, pas juste dans Figma

## Lien avec la thèse carrière "Lead DS + Content DS + IA-Enabled"

Memory déjà gravée : "Figma Agent va décimer les designers d'exécution mais multiplier la valeur des architectes DS qui définissent les règles que les agents consomment."

Le pattern complet matche pile :
- **Architecte DS** → écrit la spec markdown (toi, Christophe)
- **Agent (Claude, Cursor)** → compile en code idiomatique pour le target
- **Brand context** → applique tokens + voice du client

Profil rare en France : DS Lead + Content + IA + niche ServiceNow Horizon.

## Cas d'application immédiat : Suez Phase 2 (option +6K€ Brand Contract DS)

C'est précisément le moment de tester le pattern complet :
- Maquette HTML validée Phase 1 → spec markdown dans morphow-kit/brands/suez-workplace/
- Compilation AI → HTML brut Service Portal (target Inetum)
- Tokens shared → si Suez bascule un jour sur React, on re-compile depuis la même source

Gains :
1. Crédibilité technique sur Suez (intégrateur impressionné)
2. Démonstration au market (article making-of)
3. Validation de l'approche cross-framework pour futurs clients OxGen

## Le moat business

Inetum (intégrateur Suez) ne sait pas faire ça à ce niveau. Personne ne sait. Le "moat" = la combinaison **Spec-driven + AI compilation + tokens semantic cross-target + niche enterprise legacy (ServiceNow, SharePoint)**. C'est exactement où l'incompétence de l'industrie en design industriel rencontre l'opportunité IA.

## Questions ouvertes pour l'article final

- Quel framework de référence pour la spec ? Markdown structuré, JSON Schema, TypeScript declarations ?
- Comment garantir que la compilation AI préserve l'intent ? Tests visuels Playwright + Lighthouse ?
- Au-delà des composants UI : peut-on étendre aux patterns d'interaction (auto-hide header, FR/EN toggle, etc.) ?
- Quel statut juridique des compilations ? Le code généré appartient au client, mais le système de compilation appartient à l'architecte ?
- Open-source ou propriétaire ? Quel modèle économique pour ce type d'outil ?

## Notes pour rédaction de l'article

- Titre potentiel : "Spec-driven HTML : le pattern oublié qui redevient pertinent à l'ère de l'IA"
- Public cible : lead DS, head of design, CTO, designers ayant un pied dans le code
- Format : making-of long (3000-5000 mots) + code samples + screenshots Suez DA V1
- Plateforme : wiki Romain Bigache (writing/) + cross-post LinkedIn (vu thèse carrière "AI Product Builder")
- Ton : opinionated, factuel, honnête (pas de hype), exemples concrets de la session Suez

## À ne pas oublier

- Référence Christophe (lead DS, ami Marcel) qui creuse le même problème = potentiel projet commun
- Le making-of doit montrer le **process** (les 200 edits, les 4 bugs récurrents, l'audit morphow-kit) pas juste le résultat final
- Lighthouse 93/100/100/100 comme preuve concrète
- Vidéo de scroll de la maquette en CTA visuel
