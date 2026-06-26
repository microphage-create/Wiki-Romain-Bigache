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
| **Statut** | Phase 1 validee, Phases 2 et 3 livrees (rebuild Figma sur Horizon DS, design system theme), pages template en cours de declinaison |
| **Client** | Suez (groupe), CAC40, services a l'environnement, ~40 000 salaries |
| **Canal** | OXGEN (agence change communications, canal historique) |
| **Langues** | Francais, anglais |
| **Cible d'integration** | ServiceNow Service Portal (Horizon Design System) |
| **Multi-BU** | Suez Group, Eau France, Recyclage & Valorisation, International |
| **Methode** | Maquette HTML interactive d'abord, assistee par IA, comme artefact de decision |

## Description courte

Direction artistique pour la refonte de My Suez, l'intranet corporate du groupe Suez (eau, dechets, energie), pour environ 40 000 salaries, du siege au terrain. Le travail a demarre par une maquette HTML interactive de qualite production, generee vite par codegen IA sur un design system deja cure, utilisee comme l'artefact sur lequel le client tranche. Une fois la direction figee, elle alimente Figma comme source de verite pour l'integrateur, en vue d'un build natif ServiceNow Service Portal.

## Contexte

Suez a fait un rebrand en 2022 (nouveau logo, palette de couleurs elargie) et revoit aujourd'hui son portail digital interne. Le My Suez actuel est date : terne, bleu et vert basiques, pas de vrai parti pris. La mission, amenee via OXGEN, vise a donner au comite executif et a la com interne une cible qu'ils peuvent voir et tester avant d'engager le budget d'une refonte longue.

Deux contraintes structurent tout :

- **Double audience.** Les salaries siege a La Defense, huit heures par jour devant un laptop, et les salaries terrain (ingenieurs eau, agents d'exploitation, techniciens dechets) qui lisent l'intranet de facon utilitaire, vite, souvent en mouvement. L'interface doit tenir les deux.
- **Realite d'integration.** Le build final sort dans ServiceNow Service Portal, produit par un integrateur tiers. Le design ne peut pas trop s'eloigner des composants natifs Service Portal, sinon il meurt en maintenabilite. La cible doit donc etre ambitieuse visuellement et disciplinee techniquement en meme temps.

Le perimetre de l'exploration couvre la home et des templates de contenu, adressant le portail support IT, le self-service RH, les applications metier (HSE / declaration d'incident, achats, voyages, formations), l'annuaire et les dashboards operationnels, et les outils DSI / gouvernance applicative.

## Le coeur : la maquette interactive comme artefact de decision

Le goulot d'etranglement d'une refonte d'intranet enterprise, ce n'est pas le talent design. C'est la decision. Les comites bloquent des semaines sur des boards Figma plats et des specs PDF parce que personne ne peut sentir le produit. Ils valident une direction qu'ils ne peuvent pas tester, le build derive ensuite des boards, et tout le monde decouvre l'ecart six mois trop tard.

Le move ici, c'est d'eviter la boucle lente Figma-first et de mettre a la place une vraie maquette HTML cliquable, de qualite production, devant le client. Les parties prenantes l'ouvrent dans un navigateur, la parcourent, la testent sur mobile, changent de theme, changent de langue. La direction se choisit sur un artefact que les gens utilisent vraiment, pas sur une image fixe.

C'est la logique de la maison temoin. Personne ne lance un lotissement de 50 logements sans visiter la maison temoin d'abord : toucher les murs, ouvrir les placards, valider. La maquette interactive, c'est la maison temoin de la refonte. On clique, et le comite executif tranche sur du concret.

L'effet sur le planning est tout l'interet : le choix de direction passe de semaines d'aller-retour sur des boards a quelques jours sur un artefact vivant, et la refonte ServiceNow longue qui suit est de-risquee avant meme qu'un seul sprint soit cadre.

## Pourquoi assistee par IA, et pourquoi ca accelere le choix

La maquette se construit vite parce qu'elle repose sur deux choses : le codegen IA et un design system deja cure et pre-construit (la reference craft `_canonical/` et la couche de tokens brand). L'IA n'invente pas le langage design, elle accelere l'assemblage d'un langage deja affirme et audite.

Cette combinaison fait tenir trois metiers dans une seule personne. Sur un setup classique, une direction aussi finie demande un designer, un developpeur front et un content designer, plus la taxe de coordination entre eux. Fait en solo, design plus code plus contenu dans une seule tete, cette taxe disparait, et une cible de qualite production sort en deux a quatre semaines au lieu de deux a quatre mois.

La qualite n'est pas sacrifiee a la vitesse parce que l'audit est automatise, pas manuel :

- **Lighthouse** pour la performance, l'accessibilite, les best practices, le SEO
- **axe-core** pour la conformite WCAG AA
- **Playwright** pour l'audit visuel automatise a travers themes, variantes et langues

L'artefact que le client clique n'est donc pas un prototype jetable. Il est mesure, accessible et deployable, ce qui est exactement ce qui le rend credible comme artefact de decision et, plus tard, comme contrat.

## De la maquette a Figma : le rebuild sur Horizon DS

Voila ce qui s'est reellement passe, et c'est la preuve que la methode marche. La Phase 1 a fige la direction sur la maquette interactive. Les Phases 2 et 3 ont reproduit cette maquette dans Figma, le plus fidelement possible, cette fois construite a partir des composants natifs du Horizon Design System (le design system de ServiceNow Service Portal). La maquette HTML a cesse d'etre un pitch pour devenir la reference de fidelite que le rebuild Figma devait atteindre.

Reproduire une direction affirmee avec des composants natifs, c'est la ou la plupart des refontes perdent le design. Ici l'ecart a ete comble par customisation chirurgicale, pas par un fork :

- **Le carrousel** a demande un vrai composant custom. Le carrousel de news groupe que la direction appelait n'existait pas en natif, il a donc ete construit comme une vraie customisation au-dessus du systeme.
- **Quelques autres composants** ont pris des customisations legeres, juste assez pour honorer la direction sans sortir de la librairie native Horizon.

Le client a ete tres content du resultat : la direction ambitieuse a survecu au passage en composants natifs.

Ensuite le systeme a ete rendu reutilisable. Tout le design system plus la palette de couleurs selectionnee sont passes dans Figma en tokens, et le theme a ete deploye sur le design system lui-meme. De la, le theme se propage : toutes les autres pages de l'intranet et les pages template peuvent se decliner depuis le DS theme, plutot que d'etre redessinees une par une.

La chaine se lit donc : la maquette HTML interactive fige la direction, le rebuild Figma fidele sur Horizon DS la rend native et maintenable, les tokens Figma plus un theme deploye en font un systeme qui passe a l'echelle de tout l'intranet, et l'integrateur le shippe dans ServiceNow Service Portal contre ce systeme.

## Contraintes gerees

- **Composants natifs ServiceNow Service Portal.** Pas de widgets custom-heavy que l'integrateur ne pourrait pas maintenir. Les couleurs custom par card et un player video custom, par exemple, sont out parce que la plateforme ne les supporte pas proprement. Les encadrements et pictos colores, que la plateforme autorise, portent l'ambition visuelle a la place.
- **Theming multi-BU.** Jusqu'a 8 themes brand testes, mappant Suez Group, Eau France, Recyclage & Valorisation et International sur le meme code composant par overrides de tokens. Sans fork.
- **Bilingue FR / EN** par defaut, contenu relie via des attributs data-i18n pour une extension sure.
- **Densite double audience.** Hierarchie claire et lisibilite forte pour le terrain, assez de densite d'information pour les power users du siege. Mobile-friendly par defaut, meme si le mobile n'est pas la priorite V1.
- **Discipline brand.** Palette elargie, plus de respiration, plus de personnalite, une rupture assumee avec l'intranet actuel date, sans sortir de la charte officielle Suez.

## Resultats

Phase 1 (direction) :

- **Lighthouse 93 performance, 100 accessibilite, 100 best practices, 100 SEO** sur la maquette de reference DA V1
- Conforme **WCAG AA**, audite via axe-core
- Home plus section de contenu, avec **jusqu'a 8 themes brand** et **FR / EN**
- Cycle d'iteration mene en **2 directions, 2 tours d'ajustements**, chacune validee sur la maquette vivante plutot que sur des boards
- Deploye sur une preview Vercel pour les walkthroughs des parties prenantes (lien garde prive)

Phases 2 et 3 (rebuild Figma et theming) :

- Direction reproduite dans Figma a partir des composants natifs **Horizon Design System**, validee par le client
- **Carrousel** construit comme un vrai composant custom, customisations legeres sur quelques autres
- Tout le design system plus la palette selectionnee captures en **tokens Figma**
- **Theme deploye sur le design system**, pour que les pages template et le reste de l'intranet se declinent depuis lui plutot que d'etre redessines un par un

## Ce que ce cas demontre

- **Un role, pas un livrable.** AI Product Builder applique au design engineering enterprise : une personne portant design, code et contenu, utilisant l'IA pour comprimer le planning sans lacher la qualite production.
- **Une methode qui de-risque le budget.** La maquette interactive transforme une refonte longue et a fort enjeu en une decision prise sur un artefact concret et mesure, avant que l'argent soit engage.
- **Aisance enterprise.** Contraintes ServiceNow Service Portal, theming multi-BU, accessibilite, contenu bilingue, double audience siege et terrain, handoff integrateur. Le contexte DSI dans lequel Romain travaille via OXGEN depuis huit ans.

## Outils et stack

- HTML5 plus Tailwind CSS, compile statiquement pour la production
- JavaScript vanilla, aucune dependance framework sur le livrable
- Figma pour la couche design system cote integrateur
- ServiceNow Service Portal plus Horizon Design System comme cible d'integration
- Lighthouse, axe-core et Playwright pour l'audit automatise performance, accessibilite et visuel
- Fonts self-hosted, images optimisees, lazy loading, anti-CLS
- Vercel pour le staging et la preview live

## Related

- [experience/microphage.md](../experience/microphage.md)
- [experience/oxgen.md](../experience/oxgen.md)
- [expertise/interactive-mockup.md](../expertise/interactive-mockup.md)
- [methodology.md](../methodology.md)
- [stack.md](../stack.md)
