---
id: writing-morphow-mascotte-ia
title: J'ai généré 352 mascottes IA. La bonne n'en faisait pas partie.
type: writing
domain: blog-article
tags: [morphow, mascotte, prompt-oracle, comfyui, gemini, illustrator, propriete-intellectuelle, workflow-ia]
status: published
created: 2026-04-30
updated: 2026-05-07
url: https://romainbigache.com/fr/blog/morphow-mascotte-ia
slug: morphow-mascotte-ia
links:
  - writing.md
  - projects/mycelium.md
---

# J'ai généré 352 mascottes IA. La bonne n'en faisait pas partie.

Je construis un SaaS qui s'appelle Morphow. Des webapps modulaires en white label pour les entreprises: onboarding, formation, quiz, sondages. Le genre de produit qui a besoin d'une identité forte. Pas un logo Canva. Une mascotte. Un personnage qui peut vivre dans l'interface, réagir aux actions de l'utilisateur, incarner la marque.

Au début, j'avais pas grand-chose de concret. Je voyais le Pokemon Métamorph, un Barbapapa (promis, c'est pas de la nostalgie de mes 10 ans...), un truc blanc qui flotte. C'est tout. Le reste est venu en itérant.

J'ai décidé de le générer moi-même. Avec mon propre outil.

## L'outil: /prompt-oracle

Avant de parler de la mascotte, il faut parler de l'outil qui l'a générée. Parce que c'est pas Midjourney. C'est pas DALL-E. C'est un agent que j'ai construit moi-même.

/prompt-oracle, c'est une skill Claude Code qui orchestre ComfyUI en local avec Gemini 2.5 Flash comme modèle de génération. L'agent écrit les prompts, configure les workflows, lance les générations, et organise les outputs. Il a 8 modes: prompt simple, workflow ComfyUI complet, batch de variations, character sheet multi-poses, refinement itératif, et génération d'icones 3D.

Le truc important: ComfyUI tourne en local sur ma machine, mais Gemini 2.5 Flash reste une API cloud - la différence c'est le prix: ~0.04$ par image au lieu de 0.50$ chez Midjourney. Je peux générer 4 variations en 15 secondes et itérer 352 fois sans réfléchir au budget.

Et c'est exactement ce que j'ai fait.

## Phase 1: le point de départ Pokemon

La mascotte de Morphow, c'est Morphow. Le personnage et la marque ne font qu'un. Morphow = Morph On Web. Et le clin d'oeil a Métamorph, le Pokemon qui se transforme en n'importe quoi, n'est pas un hasard. C'est exactement ce que fait le produit: des webapps qui prennent la forme du besoin du client.

Mes premiers prompts partaient de là. Un Métamorph blanc, en 3D, style clay/vinyl.

Le résultat était mignon. Mais rose. Et trop Pokemon. On voyait immédiatement la référence. Si quelqu'un chez Nintendo tombait dessus, ça sentait le cease & desist.

Il fallait s'éloigner de la source.

## Phase 2: les fausses pistes

C'est là que ça devient intéressant. Quand tu dis à une IA "éloigne-toi de Métamorph mais garde l'esprit", elle part dans tous les sens.

Direction Ectoplasma: un monstre blanc avec des yeux rouges et des dents. Agressif, intimidant. Direction humanoïde: un alien blanc et fin, debout sur deux jambes. Trop anthropomorphe. Direction fantôme classique: un petit fantôme blanc souriant, complètement générique. Direction méduse: tentacules iridescentes, intéressante mais trop aquatique.

Et une dizaine d'autres directions encore. Chaque batch de 4 images prenait 15 secondes. En une soirée, j'avais 50 directions différentes.

Le problème: chaque direction avait un truc bien. Mais aucune n'avait tout. Le fantôme avait la bonne forme mais pas de personnalité. Le Gengar avait du caractère mais faisait peur. Le blob était original mais illisible en petit format.

## Phase 3: le déclic

Au bout de ~80 itérations, j'ai généré un truc qui m'a fait pause.

Un fantôme Pac-Man blanc. Des yeux mi-clos, angulaires. Pas de bouche. Il flotte. Il te regarde avec une sorte de supériorité décontractée. Comme s'il savait un truc que tu sais pas.

C'était ça, le personnage. Pas le design exact, mais l'attitude. Les yeux angulaires noirs sur fond blanc iridescent, sans bouche. L'expression passe par les sourcils. Minimal, reconnaissable, déclinable.

À partir de là, j'ai resserré. Plus de divergence. Que de la convergence.

## Phase 4: la convergence (et la frustration)

Les 120 itérations suivantes, c'était de la chirurgie. Ajuster les proportions. Tester des poses (debout, en marche, assis). Varier la matière (vinyl, clay, glossy, matte). Affiner les sourcils, l'inclinaison des yeux, la taille de la tête par rapport au corps.

Et c'est là que j'ai touché le mur.

L'IA génère des images. Pas des personnages. Chaque génération est unique. Les proportions bougent de 2-3% entre chaque image. Les yeux ne sont jamais exactement au même endroit. Un bras est légèrement plus gros que l'autre. La silhouette change subtilement d'un batch à l'autre.

Pour une image isolée, c'est imperceptible. Pour un character sheet (face, profil, 3/4, dos), c'est un cauchemar. Tu n'arrives jamais à avoir le même personnage sous plusieurs angles. Et pour des expressions (joyeux, triste, en colère, neutre), c'est pire: chaque émotion produit un personnage légèrement différent.

352 itérations. Des dizaines de "presque ça". Et toujours ce 5% qui manquait.

## Le pivot: du 3D au flat

J'ai lâché l'affaire à 3h du mat. Mais pas la tête. Dans le lit, j'ai ouvert Gemini sur mon tel et j'ai commencé à lui parler du projet. Pas de prompts image. Juste une conversation. Ce que je voulais, ce que je n'arrivais pas à obtenir, pourquoi la 3D bloquait.

Gemini m'a parlé de la stratégie Intel: simplifier radicalement. Un logo qui marche en 16px comme en 4K. Pas de reflets, pas de textures, pas de 3D. Du flat. Du vectoriel. Et il avait raison: mes itérations 3D étaient belles en grand mais illisibles en petit. Un favicon, une notification, un avatar de chat: tout ça demande un personnage lisible en quelques pixels.

On a tranché: ce sera du flat. Et là, Gemini m'a proposé une version basée sur mes itérations 3D. Mêmes proportions, mêmes yeux angulaires, même absence de bouche. Mais en flat, avec un contour fin et un remplissage blanc iridescent.

Bingo. J'ai cassé les traits du milieu sur le corps, gardé les yeux angulaires, et le personnage était là. Pas en 3D. En flat. Lisible, déclinable, et surtout: reproductible.

## Le graphiste

J'ai appelé Rémi.

Rémi Rohart, illustrateur. Mais attention: je suis pas arrivé les mains vides en disant "dessine-moi une mascotte". J'avais un personnage quasi terminé. La forme, l'attitude, les proportions, la matière, les yeux angulaires, l'absence de bouche, l'iridescence. 352 itérations pour arriver là. Ce que j'avais pas, c'est la rigueur d'exécution: un personnage identique sous chaque angle, des expressions cohérentes, et un fichier vectoriel exploitable.

Je lui ai envoyé mes meilleures sorties IA comme brief visuel. Pas un cahier des charges de 40 pages. Les images. "C'est ça le personnage. Je veux exactement ça, mais en propre. Multi-angles, expressions pour les états de l'app, et un doc do & don't."

Il a bossé sur Illustrator. En 48 heures, il avait:

- Le personnage vectorisé sous 6 angles (face, profil gauche, 3/4, profil droit, dos, icone app)
- Les proportions exactes avec guides de construction
- 5 expressions d'application: déterminé (défaut), empty state, error, success, loading
- Un guide "Do & Don't": pas de vêtements, pas de bouche, expression uniquement par yeux et sourcils, possibilité d'ajouter un objet en main mais à éviter
- Les transformations autorisées (le personnage peut se transformer en cube, boite, formes géométriques)
- La palette couleur exacte (#2B0545, #F1E5FF) avec centre de dégradé radial défini

Livraison Figma propre. Chaque élément utilisable tel quel dans l'interface.

Ce que Rémi a apporté en 48h, c'est pas le personnage - le personnage existait déjà. C'est ce que l'IA n'aurait jamais pu faire en 2000 itérations: la cohérence. Le même personnage, exactement le même, sous tous les angles et dans toutes les émotions. Des proportions fixes. Des guides de construction pour que n'importe qui puisse le reproduire. Un système, pas une image.

Mais cette livraison a aussi réglé un problème que la plupart des articles "j'ai tout fait avec l'IA" préfèrent ignorer.

## La zone grise de la propriété intellectuelle

En l'état du droit, une image générée par IA n'est pas protégeable par le droit d'auteur. Pas en France, pas aux US. L'US Copyright Office l'a dit clairement en 2023: pas d'auteur humain, pas de copyright. En Europe, la position est similaire - le droit d'auteur protège les oeuvres originales issues d'une création intellectuelle humaine. Un prompt, aussi élaboré soit-il, n'est pas considéré comme un acte de création suffisant.

Concrètement: mes 352 images ComfyUI ne m'appartiennent pas au sens juridique. N'importe qui pourrait reprendre la même esthétique, le même personnage, et je n'aurais aucun recours.

C'est un problème quand tu construis une marque. Ta mascotte, c'est ton identité. Si elle n'est pas protégeable, elle ne vaut rien juridiquement. Et j'ai touché ce mur concrètement: j'ai voulu déposer le personnage comme marque figurative à l'INPI. Impossible. Pas d'auteur humain, pas de dépôt.

Soyons honnêtes: je suis le premier à défendre le fait de bien payer un graphiste. Mais là, je bosse à blanc depuis des mois. Zéro revenu, que de l'investissement. Payer un illustrateur pour un character sheet complet, c'était au-dessus de ce que je pouvais mettre. Mais ne rien faire du tout, c'était pire. Alors j'ai trouvé un entre-deux: faire bosser un illustrateur trois jours au lieu de trois semaines. Parce que le brief était déjà fait. 352 itérations, c'est 352 décisions visuelles. Rémi n'a pas eu à chercher le personnage. Il était là. Il a juste eu à le construire proprement.

Rémi a repris le personnage sur Illustrator, en partant de mes sorties IA comme base visuelle, et l'a entièrement reconstruit en vectoriel. Son travail est une oeuvre originale, protégée par le droit d'auteur dès sa création. Les fichiers vectoriels, le character sheet, les expressions: tout ça m'appartient légalement (avec cession de droits). Je peux déposer la mascotte comme marque figurative. Je peux attaquer si quelqu'un la copie.

L'IA a généré l'inspiration. L'humain a généré la propriété intellectuelle.

C'est pas un détail. Pour un SaaS qui veut lever, se vendre, ou simplement protéger son identité, la question "est-ce que ta mascotte t'appartient vraiment?" a une réponse binaire. Et si la réponse repose uniquement sur des sorties d'IA, c'est non.

## Ce que j'ai appris

L'IA est un explorateur, pas un artisan. En 352 itérations, j'ai couvert un espace de possibilités qu'un brainstorming humain aurait mis des semaines à parcourir. J'ai testé des directions que je n'aurais jamais envisagées (la méduse, le chien détective, le blob informe). Certaines étaient nulles. D'autres m'ont surpris. Et c'est de cette exploration que le brief final est sorti.

Mais l'exploration ne suffit pas. À un moment, il faut figer. Décider que CE personnage, avec CES proportions, CES yeux, à CE angle, c'est le bon. Et le reproduire à l'identique 50 fois. Ça, l'IA ne sait pas faire. Pas encore.

Et même si elle savait, le résultat ne t'appartiendrait pas.

Le vrai workflow, c'est pas IA vs humain. C'est IA puis humain. L'IA ouvre l'espace. L'humain le ferme. Et l'humain signe.

Et le fait d'avoir construit mon propre outil de génération a rendu l'exploration 10x plus rapide et 100x moins chère qu'avec n'importe quel service cloud. 352 itérations à ~0.04$ pièce, ça fait ~14$. Le résultat, c'est un brief visuel tellement précis que l'illustrateur a livré en 48h sans aller-retour.

> ~14 dollars d'IA et un bon illustrateur. C'est comme ça qu'on design une mascotte en 2026.

## Related

- [writing.md](../writing.md)
- [projects/mycelium.md](../projects/mycelium.md)
