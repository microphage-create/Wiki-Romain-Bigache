---
id: interactive-mockup
title: Maquette interactive comme contrat
type: expertise
domain: design-engineering
tags: [maquette-interactive, prototype-html, frontend-craft, design-system, refonte-entreprise, lighthouse, wcag-aa, multi-theme, bilingue, maison-temoin, analogie-btp]
status: draft
created: 2026-05-23
updated: 2026-05-23
confidential: true
links:
  - ../methodology.md
  - ../stack.md
  - ../process.md
---

# Maquette interactive comme contrat

Prestation autonome pour les refontes d'intranets, portails et applications internes en entreprise. Le livrable : une maquette HTML production-grade qui sert de spécification exécutable entre les parties prenantes et l'équipe de développement. Plus de dérive entre Figma et le build.

## L'analogie de la maison témoin

Avant de construire un lotissement de 50 maisons, personne ne signe sans visiter la maison témoin. On traverse les pièces, on touche les murs, on ouvre les placards, on valide. Une fois la maison témoin approuvée, le constructeur sait exactement quoi reproduire.

La même logique s'applique aux refontes digitales en entreprise : 500K à 2M EUR de développement sont régulièrement engagés sur des planches Figma plates et des specs PDF dont le build va s'écarter. La maquette interactive EST la maison témoin. On clique, on teste sur mobile, on audite l'accessibilité, on change de thème, on change de langue. Une fois validée, l'équipe de développement a un contrat, pas une inspiration.

## Pour qui

Trois profils acheteurs récurrents :

1. **Refontes d'intranets en entreprise** (ServiceNow Service Portal, SharePoint moderne, plateformes custom). Responsables Workplace, Responsables Communication Interne, DSI. L'intranet traîne depuis 5 à 10 ans, le comité exécutif a besoin de voir la cible avant d'allouer un budget de 12 mois de rebuild.
2. **Refresh de portail B2B SaaS**. Directeurs Produit, Heads of Design. Le portail est daté, le sales perd des deals sur l'UX, mais personne ne veut engager de ressources dev sans voir la cible.
3. **Modernisation d'applications internes** (RH, IT, outils opérationnels). Responsables produit interne, directeurs informatiques. La dérive fonctionnelle accumulée sur des années a empilé des features sans révision ; la maquette force l'alignement sur l'expérience nouvelle génération avant le rebuild.

## Ce que vous obtenez

Une maquette HTML entièrement fonctionnelle, déployable comme site statique, qui inclut :

- Une à quatre pages clés (accueil + 2 à 3 templates), selon le scope
- Performance production-grade (Lighthouse 90+ sur performance, 100 sur accessibilité, best practices, SEO)
- Conformité accessibilité WCAG AA, auditée via axe-core
- Support multi-thèmes si la marque le requiert (jusqu'à 8 thèmes testés dans le benchmark de référence)
- Contenu bilingue (FR / EN par défaut), lié via les attributs data-i18n pour extension propre
- Responsive sur mobile, tablette, desktop
- Polices self-hosted, images optimisées, lazy loading, anti-CLS
- Header sticky avec auto-hide, drawer mobile accessible, micro-interactions polies au standard production
- Fichier index.html unique ou fichiers .html modulaires, déployés sur Vercel preview pour la validation live

## Comment ça marche (4 étapes, analogie BTP filée)

### 1. Permis de construire (1 à 2 jours)

Brief intake. Une seule session, prise de notes structurée. Contraintes capturées : marque existante, cible d'intégration (ServiceNow, SharePoint, custom), set de pages prioritaires, niveau d'accessibilité, audience cible. Livrable : un one-pager scope.

### 2. Fondations (3 à 5 jours)

Design tokens, système typographique, système de couleurs, rythme de spacing, bibliothèque de composants. Aligné sur la marque existante si elle existe, structuré depuis zéro sinon. Livrable : foundations.css et le premier hero shippé sur Vercel preview. Architecture multi-thèmes câblée si applicable.

### 3. Construction de la maison témoin (5 à 10 jours)

Le set complet de pages clés est construit. Audit accessibilité via axe-core. Audit performance via Lighthouse. Responsive cross-device. Polish des interactions (hover, focus, scroll behavior, micro-animations). Contenu bilingue câblé. Déployé live sur Vercel pour les walkthroughs avec les parties prenantes.

### 4. Réception de chantier (1 jour)

Walkthrough final avec le client. Documentation du design system si demandée. Code remis sous forme de repo privé. L'équipe de construction (Inetum, Capgemini, Atos, ingénierie interne, ou intégrateur tiers) prend la maquette HTML comme spécification contractuelle pour le rebuild. Équivalent de la garantie décennale en option : le code du design system vit dans un repo versionné, disponible pour référence dans la durée.

## Tarifs (confidentiels, indicatifs)

| Scope | Prix (EUR) |
|-------|------------|
| Maquette single-page de validation (accueil uniquement) | 8 000 à 12 000 |
| Maquette multi-pages (accueil + 2 à 3 pages) | 13 000 à 18 000 |
| Couche Brand Contract (tokens, voice, composants en code) | +6 000 à 10 000 |
| Variante ou itération de thème supplémentaire | +3 000 à 5 000 |
| Atelier marque et tokens (1 à 2 jours sur site) | 3 000 à 5 000 |

Posture pricing : forfait par scope. Pas de facturation horaire. Pas de révisions au-delà du nombre d'itérations convenu sans renégociation.

## Différenciateurs vs alternatives

- **Versus la maquette Figma plate** : une maquette HTML interactive élimine la dérive de spec qui survient quand l'équipe build interprète le design. Pixel-perfect, animations incluses, accessibilité testée, performance mesurée.
- **Versus le prototypage low-code (Webflow, Framer)** : code production-grade qui peut être repris directement dans une intégration Next.js ou vanilla. Pas de vendor lock-in, pas d'abonnement mensuel sur le livrable.
- **Versus le prototype dev-first** : coût compressé à 2 à 4 semaines au lieu de 2 à 4 mois. La maquette est design-led, pas engineering-led, donc la cible est tranchée et validée avant que l'équipe dev ne planifie son sprint.

## Preuves de réalisation

- **Suez (CAC40, services environnementaux, 40 000 collaborateurs)** : refonte intranet, direction artistique V1. Page d'accueil + section contenu, 8 thèmes de marque, FR et EN, cible ServiceNow Service Portal. Lighthouse 93 performance, 100 accessibilité, 100 best practices, 100 SEO. WCAG AA. Statut : Phase 1 livrée, Phase 2 (Brand Contract) en négociation. À anonymiser en publication publique tant que la validation Phase 2 n'est pas close.
- **fusil.paris** : refonte SEO et éditoriale, pattern maquette content-driven appliqué à un e-commerce.
- Cas supplémentaires à ajouter au fil des missions.

## Outils et stack

- HTML5 + Tailwind CSS (compilé statiquement en production)
- JavaScript vanilla, aucune dépendance framework
- PIL pour l'optimisation des images (LANCZOS resize, qualité 78-82, progressive)
- Lighthouse pour l'audit performance
- axe-core pour l'audit accessibilité
- Playwright pour l'audit visuel automatisé
- Vercel pour le staging et les preview deployments
- Google Fonts self-hosted via script de build custom

## Sources

- Benchmark de référence : maquette Suez DA V1, 1 999 lignes, Lighthouse 93 perf, 100 a11y, 100 bp, 100 SEO
- Fondation méthode : projet Mycelium et la documentation design system `_canonical/`
- Patterns réutilisables : 22 patterns universels documentés dans `_canonical/patterns/UNIVERSAL-PATTERNS.md` (Mycelium)

## Related

- [methodology.md](../methodology.md)
- [stack.md](../stack.md)
- [process.md](../process.md)
