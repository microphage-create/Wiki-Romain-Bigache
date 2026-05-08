---
id: writing-personne-ne-peaufine
title: Tout le monde sait coder. Personne ne peaufine.
type: writing
domain: blog-article
tags: [peaufinage, mockup, front-ui, design, polish, ux, ai-coding]
status: draft
created: 2026-05-08
updated: 2026-05-08
url: https://romainbigache.com/fr/blog/personne-ne-peaufine
slug: personne-ne-peaufine
links:
  - writing.md
  - process.md
---

# Tout le monde sait coder. Personne ne peaufine.

Y'a un truc qui me dérange depuis quelques mois : les interfaces sont de plus en plus mal finies. Sites institutionnels, startups qui viennent de lever 50 millions, indie hackers. Le bouton CTA n'est pas centré. Le libellé flotte au-dessus du milieu. Le hover state pop dans le néant. T'as l'impression que personne ne s'arrête plus sur ce qu'il a sous les yeux.

Tout le monde sait coder maintenant, et personne ne peaufine. C'est ça la vraie maladie.

Du coup quand on me demande comment je fais pour livrer des interfaces qui tiennent debout, je donne pas une méthode magique. Je donne juste ce qui marche pour moi : un fichier HTML statique avant d'ouvrir le moindre fichier React.

## Ce que j'ai posé cette semaine

J'ai voulu refaire le widget de booking de mon site. Une liste de créneaux dans le chat, click sur l'heure, confirm. Au lieu d'ouvrir mon repo Next.js et de me lancer dans le TSX, j'ai ouvert un fichier HTML vide.

J'ai posé 9 états côte à côte sur la même page : skeleton pendant le tool call du LLM, calendrier avec scarcity, liste de créneaux horaires, récap, édition d'email inline, état "en cours", confirmation, erreur 409 quand le créneau est pris ailleurs au même moment, et le cas où le LLM doit demander un prénom parce que l'email est opaque.

![Mockup statique : état recap](../../assets/mockup-driven/04-recap-default.png)

2 heures. Tous les états visibles en même temps, en plein écran, en dark et en light, en français et en anglais. Avant la moindre ligne de React.

## Pourquoi pas direct en code

Le truc, c'est pas que ça gagne du temps. Si j'avais codé direct, j'aurais fini plus vite. Mais ça aurait été moins bien.

En code, tu vois jamais tous tes états ensemble. Tu vois l'happy path en dev, tu testes l'erreur en l'invoquant manuellement, tu vois le state "loading" deux secondes avant qu'il disparaisse. Tu peaufines pas un état que tu vois deux secondes. Tu peaufines un état que t'as sous les yeux pendant 2 heures.

L'autre raison, c'est que c'est juste logique. Tu fais le front avant le back. Le mockup HTML, c'est ton front sans le back : pas d'API à brancher, pas de state à gérer, pas de provider à wrapper. Juste le rendu. Tu itères 15 fois en une heure parce qu'il n'y a rien d'autre à casser. Une fois le front calé, le back devient une exécution propre derrière une UI déjà dessinée.

Et plus personne ne regarde son code de toute façon. On regarde le rendu sur localhost. Le mockup HTML te donne ce rendu plus vite, sans le coût d'avoir tout branché.

Et surtout, tu vois ce qui manque. En posant la séquence "click sur l'heure → POST de réservation", j'ai vu qu'il manquait quelque chose entre les deux. L'utilisateur n'a aucun moment pour relire ce qu'il s'apprête à confirmer. Nom, email, date, heure. J'ai rajouté un récap avec un crayon d'édition inline sur chaque champ. Ce qu'on appelle un poka-yoke en lean : un détrompeur. Pas grand chose en quantité de code. Une vraie économie en taux d'erreur.

J'aurais sans doute pas pensé à ce récap en codant direct. J'aurais branché l'API de booking sur le click slot, vu que ça marchait, validé le ticket. C'est en regardant le mockup, en posant les états côte à côte, que le trou apparaît. Le mockup HTML te montre les questions que t'avais pas vues.

Pareil pour le copy. À côté du success state, tu vois que "ce créneau vient d'être pris" sonne accusateur. Tu corriges en "ce créneau est déjà pris", neutre. Un mot qui change, mais tu fais le changement parce que t'as les deux versions sous les yeux. En code, t'aurais lu ce copy dans un fichier de strings, pas dans son contexte.

![Mockup statique : état erreur 409](../../assets/mockup-driven/08-error.png)

## Et chaque composant tu le gardes

Le truc tout bête, c'est que peaufiner le mockup t'oblige à te concentrer sur chaque composant. Pas en survol, pas en passant. Vraiment. Et chaque composant mérite cette attention.

Un composant bien fait, c'est un composant qu'on réutilise. Tu le bouges sur le projet suivant, tu le bouges trois projets après. La deuxième fois, c'est gratuit. Le mockup propre, c'est pas un coût ponctuel, c'est un investissement.

Et surtout, c'est un truc dont t'es fier longtemps. Pas le composant livré dans la journée parce que ça pressait et que tu refais six mois après parce que t'as honte. Celui que tu peux laisser tel quel pendant deux ans.

C'est comme acheter une paire de pompes à 60 euros ou à 500 euros. Les 60 euros, tu les remplaces tous les 6 mois et tu les jettes au passage. Les 500 euros, tu les gardes cinq ans, tu les fais recoudre une fois chez le cordonnier, et elles ont plus belle allure à la fin qu'au début.

## Quand j'ouvre le TSX

Quand je passe au code, je ne décide plus rien. Je copie-colle des décisions déjà prises.

Le récap avec les crayons est posé. Le copy est arrêté. Le timing du stagger ? 18ms entre chaque cellule du calendrier, marqué dans le mockup. Le glow pendant le POST ? .08 alpha sur l'accent, dans le CSS du mockup. Le code devient l'exécution d'un plan visuel déjà écrit. Plus de "le bouton n'est pas calé, je vais essayer autre chose". Plus de re-design en plein milieu d'un commit.

## Pas une méthode

Je ne sais pas si c'est une méthode. Pour des cas simples, je code direct. Pour un widget avec 9 états et des animations, le mockup HTML me permet de pas livrer bâclé.

Le truc qui me rassure, c'est que peaufiner s'apprend pas en 2 heures de mockup. Le mockup, c'est juste un terrain où peaufiner devient possible. Si t'as pas l'œil, t'auras pas l'œil sur HTML non plus. Mais si t'as l'œil et que tu codes direct, tu peaufines pas, parce que t'as pas le temps.

> Tout le monde sait coder. Personne ne peaufine. C'est probablement la chose la plus rare en 2026.

Voilà, c'est mon truc en ce moment. 2 heures de HTML statique pour pas livrer bâclé. C'est pas grand chose. C'est juste suffisant.

## Related

- [writing.md](../writing.md)
- [process.md](../process.md)
