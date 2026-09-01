---
id: project-my-suez
title: My Suez - refonte de l'intranet
type: project
category: site
domain: project
tags: [microphage, my-suez, suez, intranet, enterprise, b2b, design-system, multi-bu, interactive-mockup, ai-codegen, servicenow, figma, horizon-design-system, figma-tokens, lighthouse, wcag-aa, bilingual]
status: in-progress
created: 2026-05-08
updated: 2026-06-26
period: 2026-05 / present
client: Suez (groupe)
industries: [Industrie, Eau, Dechets, Energie]
technologies: [HTML5, Tailwind CSS, Vanilla JS, Figma, ServiceNow Service Portal, Lighthouse, axe-core, Playwright, Vercel]
team: 1 (Romain Bigache, seul)
url: null
demo: null
confidential: true
links:
  - experience/microphage.md
  - experience/oxgen.md
  - expertise/interactive-mockup.md
  - methodology.md
  - stack.md
---

# My Suez - Refonte de l'intranet

| Cle | Valeur |
|-----|--------|
| **Type** | Refonte d'intranet enterprise (direction artistique) |
| **Statut** | Phase 1 validée, Phases 2 et 3 livrées (rebuild Figma sur Horizon DS, design system theme), pages template en cours de déclinaison |
| **Client** | Suez (groupe), CAC40, services à l'environnement, ~40 000 salariés |
| **Canal** | OXGEN (agence change communications, canal historique) |
| **Langues** | Français, anglais |
| **Cible d'intégration** | ServiceNow Service Portal (Horizon Design System) |
| **Multi-BU** | Suez Group, Eau France, Recyclage & Valorisation, International |
| **Méthode** | Maquette HTML interactive d'abord, assistée par IA, comme artefact de décision |

## Description courte

Direction artistique pour la refonte de My Suez, l'intranet corporate du groupe Suez (eau, déchets, énergie), pour environ 40 000 salariés, du siège au terrain. Le travail a démarré par une maquette HTML interactive de qualité production, générée vite par codegen IA sur un design system déjà curé, utilisée comme l'artefact sur lequel le client tranche. Une fois la direction figée, elle alimente Figma comme source de vérité pour l'intégrateur, en vue d'un build natif ServiceNow Service Portal.

## Contexte

Suez a fait un rebrand en 2022 (nouveau logo, palette de couleurs élargie) et revoit aujourd'hui son portail digital interne. Le My Suez actuel est daté : terne, bleu et vert basiques, pas de vrai parti pris. La mission, amenée via OXGEN, vise à donner au comité exécutif et à la com interne une cible qu'ils peuvent voir et tester avant d'engager le budget d'une refonte longue.

Deux contraintes structurent tout :

- **Double audience.** Les salariés siège à La Défense, huit heures par jour devant un laptop, et les salariés terrain (ingénieurs eau, agents d'exploitation, techniciens déchets) qui lisent l'intranet de façon utilitaire, vite, souvent en mouvement. L'interface doit tenir les deux.
- **Réalité d'intégration.** Le build final sort dans ServiceNow Service Portal, produit par un intégrateur tiers. Le design ne peut pas trop s'éloigner des composants natifs Service Portal, sinon il meurt en maintenabilité. La cible doit donc être ambitieuse visuellement et disciplinée techniquement en même temps.

Le périmètre de l'exploration couvre la home et des templates de contenu, adressant le portail support IT, le self-service RH, les applications métier (HSE / déclaration d'incident, achats, voyages, formations), l'annuaire et les dashboards opérationnels, et les outils DSI / gouvernance applicative.

## Le cœur : la maquette interactive comme artefact de décision

Le goulot d'étranglement d'une refonte d'intranet enterprise, ce n'est pas le talent design. C'est la décision. Les comités bloquent des semaines sur des boards Figma plats et des specs PDF parce que personne ne peut sentir le produit. Ils valident une direction qu'ils ne peuvent pas tester, le build dérive ensuite des boards, et tout le monde découvre l'écart six mois trop tard.

Le move ici, c'est d'éviter la boucle lente Figma-first et de mettre à la place une vraie maquette HTML cliquable, de qualité production, devant le client. Les parties prenantes l'ouvrent dans un navigateur, la parcourent, la testent sur mobile, changent de thème, changent de langue. La direction se choisit sur un artefact que les gens utilisent vraiment, pas sur une image fixe.

C'est la logique de la maison témoin. Personne ne lance un lotissement de 50 logements sans visiter la maison témoin d'abord : toucher les murs, ouvrir les placards, valider. La maquette interactive, c'est la maison témoin de la refonte. On clique, et le comité exécutif tranche sur du concret.

L'effet sur le planning est tout l'intérêt : le choix de direction passe de semaines d'aller-retour sur des boards à quelques jours sur un artefact vivant, et la refonte ServiceNow longue qui suit est de-risquée avant même qu'un seul sprint soit cadré.

## Pourquoi assistée par IA, et pourquoi ça accélère le choix

La maquette se construit vite parce qu'elle repose sur deux choses : le codegen IA et un design system déjà curé et pré-construit (la référence craft `_canonical/` et la couche de tokens brand). L'IA n'invente pas le langage design, elle accélère l'assemblage d'un langage déjà affirmé et audité.

Cette combinaison fait tenir trois métiers dans une seule personne. Sur un setup classique, une direction aussi finie demande un designer, un développeur front et un content designer, plus la taxe de coordination entre eux. Fait en solo, design plus code plus contenu dans une seule tête, cette taxe disparaît, et une cible de qualité production sort en deux à quatre semaines au lieu de deux à quatre mois.

La qualité n'est pas sacrifiée à la vitesse parce que l'audit est automatisé, pas manuel :

- **Lighthouse** pour la performance, l'accessibilité, les best practices, le SEO
- **axe-core** pour la conformité WCAG AA
- **Playwright** pour l'audit visuel automatisé à travers thèmes, variantes et langues

L'artefact que le client clique n'est donc pas un prototype jetable. Il est mesuré, accessible et déployable, ce qui est exactement ce qui le rend crédible comme artefact de décision et, plus tard, comme contrat.

## De la maquette à Figma : le rebuild sur Horizon DS

Voilà ce qui s'est réellement passé, et c'est la preuve que la méthode marche. La Phase 1 a figé la direction sur la maquette interactive. Les Phases 2 et 3 ont reproduit cette maquette dans Figma, le plus fidèlement possible, cette fois construite à partir des composants natifs du Horizon Design System (le design system de ServiceNow Service Portal). La maquette HTML a cessé d'être un pitch pour devenir la référence de fidélité que le rebuild Figma devait atteindre.

Reproduire une direction affirmée avec des composants natifs, c'est là où la plupart des refontes perdent le design. Ici l'écart a été comblé par customisation chirurgicale, pas par un fork :

- **Le carrousel** a demandé un vrai composant custom. Le carrousel de news groupe que la direction appelait n'existait pas en natif, il a donc été construit comme une vraie customisation au-dessus du système.
- **Quelques autres composants** ont pris des customisations légères, juste assez pour honorer la direction sans sortir de la librairie native Horizon.

Le client a été très content du résultat : la direction ambitieuse a survécu au passage en composants natifs.

Ensuite le système a été rendu réutilisable. Tout le design system plus la palette de couleurs sélectionnée sont passés dans Figma en tokens, et le thème a été déployé sur le design system lui-même. De là, le thème se propage : toutes les autres pages de l'intranet et les pages template peuvent se décliner depuis le DS theme, plutôt que d'être redessinées une par une.

La chaîne se lit donc : la maquette HTML interactive fige la direction, le rebuild Figma fidèle sur Horizon DS la rend native et maintenable, les tokens Figma plus un thème déployé en font un système qui passe à l'échelle de tout l'intranet, et l'intégrateur le shippe dans ServiceNow Service Portal contre ce système.

## Contraintes gérées

- **Composants natifs ServiceNow Service Portal.** Pas de widgets custom-heavy que l'intégrateur ne pourrait pas maintenir. Les couleurs custom par card et un player video custom, par exemple, sont out parce que la plateforme ne les supporte pas proprement. Les encadrements et pictos colorés, que la plateforme autorise, portent l'ambition visuelle à la place.
- **Theming multi-BU.** Jusqu'à 8 thèmes brand testés, mappant Suez Group, Eau France, Recyclage & Valorisation et International sur le même code composant par overrides de tokens. Sans fork.
- **Bilingue FR / EN** par défaut, contenu relié via des attributs data-i18n pour une extension sûre.
- **Densité double audience.** Hiérarchie claire et lisibilité forte pour le terrain, assez de densité d'information pour les power users du siège. Mobile-friendly par défaut, même si le mobile n'est pas la priorité V1.
- **Discipline brand.** Palette élargie, plus de respiration, plus de personnalité, une rupture assumée avec l'intranet actuel daté, sans sortir de la charte officielle Suez.

## Résultats

Phase 1 (direction) :

- **Lighthouse 93 performance, 100 accessibilité, 100 best practices, 100 SEO** sur la maquette de référence DA V1
- Conforme **WCAG AA**, audité via axe-core
- Home plus section de contenu, avec **jusqu'à 8 thèmes brand** et **FR / EN**
- Cycle d'itération mené en **2 directions, 2 tours d'ajustements**, chacune validée sur la maquette vivante plutôt que sur des boards
- Déployé sur une preview Vercel pour les walkthroughs des parties prenantes (lien gardé privé)

Phases 2 et 3 (rebuild Figma et theming) :

- Direction reproduite dans Figma à partir des composants natifs **Horizon Design System**, validée par le client
- **Carrousel** construit comme un vrai composant custom, customisations légères sur quelques autres
- Tout le design system plus la palette sélectionnée capturés en **tokens Figma**
- **Theme déployé sur le design system**, pour que les pages template et le reste de l'intranet se déclinent depuis lui plutôt que d'être redessinés un par un

## Ce que ce cas démontre

- **Un rôle, pas un livrable.** AI Product Builder appliqué au design engineering enterprise : une personne portant design, code et contenu, utilisant l'IA pour comprimer le planning sans lâcher la qualité production.
- **Une méthode qui de-risque le budget.** La maquette interactive transforme une refonte longue et à fort enjeu en une décision prise sur un artefact concret et mesuré, avant que l'argent soit engagé.
- **Aisance enterprise.** Contraintes ServiceNow Service Portal, theming multi-BU, accessibilité, contenu bilingue, double audience siège et terrain, handoff intégrateur. Le contexte DSI dans lequel Romain travaille via OXGEN depuis huit ans.

## Outils et stack

- HTML5 plus Tailwind CSS, compilé statiquement pour la production
- JavaScript vanilla, aucune dépendance framework sur le livrable
- Figma pour la couche design system côté intégrateur
- ServiceNow Service Portal plus Horizon Design System comme cible d'intégration
- Lighthouse, axe-core et Playwright pour l'audit automatisé performance, accessibilité et visuel
- Fonts self-hosted, images optimisées, lazy loading, anti-CLS
- Vercel pour le staging et la preview live

## Related

- [experience/microphage.md](../experience/microphage.md)
- [experience/oxgen.md](../experience/oxgen.md)
- [expertise/interactive-mockup.md](../expertise/interactive-mockup.md)
- [methodology.md](../methodology.md)
- [stack.md](../stack.md)
