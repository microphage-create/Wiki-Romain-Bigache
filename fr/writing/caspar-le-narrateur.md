---
id: writing-caspar-le-narrateur-fr
title: Caspar, ou comment on se cache derrière son lion
description: Petit making-of d'un site personnel commencé à Madrid, devant une peinture qui ne me lâchait pas. Pourquoi j'ai construit un assistant ronchon plutôt qu'une vitrine, comment l'avatar est passé d'un rat à un lion dessiné puis à un lion paramétrique, et ce que tout ça dit du métier en 2026.
type: writing
domain: blog-article
tags: [caspar, site-personnel, narrateur, ia, making-of, patinir, saint-jerome, immersion, avatar, shader, abstraction]
status: draft
created: 2026-05-16
updated: 2026-05-19
url: https://romainbigache.com/fr/blog/caspar-le-narrateur
slug: caspar-le-narrateur
links:
  - writing.md
  - profile.md
---

# Caspar, ou comment on se cache derrière son lion

Mon site personnel n'a pas commencé devant un écran. Il a commencé à Madrid, au musée du Prado, devant une peinture que je n'avais pas prévu de voir.

## Le tableau du Prado

C'est un Patinir. *Paysage avec saint Jérôme*, peint vers 1516. Un peintre flamand qui dessinait des paysages immenses et qui glissait, en bas, un saint minuscule dans un coin du tableau. Là, le saint est dans une petite hutte sous un rocher, à gauche. Le lion est assis à côté de lui. Le reste de l'image, c'est un monde : montagnes calcaires, vallée verte, ville, fleuve, mer, ciel orageux d'un côté qui se déchire en lumière de l'autre.

Je suis resté longtemps devant. Ce qui m'a touché, ce n'est pas le saint, ni le lion, ni le bestiaire iconographique. C'est l'écart. Le saint est à l'écart de tout ce monde, dans son rocher, avec son lion, et le monde continue sans lui, énorme et indifférent. Il a l'air bien, dans son coin. La nature est belle. Il vit en fusion avec elle, avec les animaux, et il y a là quelque chose de profondément rassurant et de transcendant.

Je me projetais quelque part dans cette scène. Pas comme spectateur, comme habitant.

Je ne savais pas encore que j'étais en train de regarder l'origine de mon site.

## Un narrateur plutôt que moi

Je peux parler en mon nom propre. Beaucoup de gens le font sur leur site personnel : une photo, une bio, un manifeste. Très bien. Je n'aime pas trop me mettre en avant. Je ne suis pas asocial, je préfère simplement que quelqu'un d'autre tienne le micro.

Mettre la vedette sur un personnage, c'est se mettre en vedette d'une manière plus modeste. C'est un détour qui dit autant que la ligne droite, peut-être davantage. Le visiteur entre dans un univers, rencontre quelqu'un, écoute son récit, et au fil de la conversation, il comprend qu'il y a quelqu'un derrière. Mais ce quelqu'un ne lui a pas tendu la main en premier. C'est le narrateur qui ouvre la porte.

Il y a autre chose que je n'avais pas remarqué tout de suite. Dans son récit, Caspar choisit. Il refuse de raconter son histoire à n'importe qui. Il la dit à ceux qui ont pris le temps. Il ne nourrit pas tous les visiteurs. Il vous bouscule, il vous fait attendre, il vous demande de revenir. C'est exactement ce que je fais avec les clients. Je filtre. Je ne prends pas n'importe quelle mission, je ne travaille pas avec n'importe qui. Je préfère perdre des recruteurs robotiques qui ne maîtrisent pas le métier pour lequel ils recrutent, plutôt que de gagner un client qui me traitera comme du bétail. Je m'en fous des marchands de viande.

J'avais projeté ma posture dans la fiction sans le faire exprès. Caspar fait au visiteur ce que je fais aux clients. C'est peut-être la preuve que le personnage tient debout : il prolonge mon attitude sans qu'il ait fallu la coder explicitement.

## Trois Caspar

Donner un visage à ce narrateur a pris trois itérations. Le récit qui suit est celui d'un design qui s'est cherché, et qui a fini par s'effacer pour mieux exister.

### Premier Caspar : Splinter

La première version du site avait un autre narrateur. Un rat. Un rat qui ressemblait beaucoup à Maître Splinter, des Tortues Ninja, parce que c'était exactement lui. Un vieux rat sage avec une ceinture noire, un maître d'arts martiaux, qui avait accès à la connaissance universelle. Le genre de personnage qui te guide en te bousculant un peu.

Le problème, c'est que Splinter appartient à quelqu'un. Légalement, je n'avais pas le droit de l'utiliser. J'ai pivoté.

Il en reste une trace. Dans la section technique du site, celle qui parle d'hallucinations IA, le rat apparaît encore. C'est une démonstration : j'ai laissé un modèle vidéo générer ses propres dérives à partir d'une image de base, et le rat se déforme progressivement, s'écarte du modèle, devient autre chose. C'est exactement ce qu'une IA fait quand elle hallucine : elle s'écarte du réel, doucement, sans prévenir. Le rat est devenu sa propre métaphore. C'est l'easter egg du site, et c'est aussi ma dédicace silencieuse à la première version.

### Deuxième Caspar : le dessin à capuche

Quand il a fallu trouver un remplaçant à Splinter, je suis retourné à Madrid, dans ma tête. Le lion du tableau m'avait gardé. J'ai commencé par le dessiner. Pas en croquant moi-même, mais en pilotant une IA générative pour produire un portrait de lion qui aurait du caractère. Une illustration figurative, à mi-chemin entre la mascotte et le portrait.

Ce qui m'a plu dans cette version, et qui n'a jamais quitté le projet, c'est la capuche. Le lion portait une capuche sombre qui mangeait une partie de son visage, ne laissait apparaître que les yeux et un bout de crinière. Cette ambiance presque monacale, un peu inquiétante, plus proche du moine encapuchonné que de la peluche : c'était ça que je cherchais. Sombre, replié, à l'écart. Très proche, finalement, du saint dans son rocher.

Mais le dessin lui-même ne marchait pas. Deux raisons.

La première, c'est que l'illustration mangeait toute l'attention. Vous arriviez sur le site, vous ne lisiez plus, vous regardiez le lion. Or Caspar doit être présent, pas dominant. Un narrateur n'est pas la couverture du livre.

La seconde, c'est que malgré la capuche, le rendu glissait quand même vers l'enfantin. Un lion croqué, même bien fait, même drapé dans un capuchon, garde un trait de pelage, une expression, un brin de Simba. Le site de quelqu'un qui fait du conseil et de la direction technique ne peut pas s'ouvrir sur une figurine de salon.

L'idée de la capuche, elle, je l'ai gardée. C'est elle qui a fait basculer la troisième version.

### Troisième Caspar : l'abstraction

J'ai pivoté une deuxième fois, et cette version est celle que vous voyez aujourd'hui. Pas un dessin, pas une mascotte, un avatar paramétrique fait de deux briques : un anneau de fumée WebGL pour la crinière et la présence, et deux yeux SVG inline pour le regard. Le shader vit en boucle, indépendamment de moi. Les yeux clignent toutes les cinq secondes. Tout est piloté par des paramètres : un seul composant, vingt-quatre humeurs.

Cette version-là est, en réalité, une distillation de la précédente. La capuche sombre du Caspar dessiné est devenue le fond charbon. La crinière qui dépassait du capuchon est devenue l'anneau de fumée animé. Les yeux qui perçaient l'ombre sont restés des yeux qui percent l'ombre, mais en SVG, en six lignes de code. On garde l'esprit, on jette le contour. Le visage est sombre, à peine suggéré, et le regard parle. C'est exactement la même intention, mais portée par de la géométrie et du bruit GPU au lieu d'un trait d'illustration.

Et surtout, comme tout est paramétrique, on peut décliner à l'infini. Changer la couleur de l'iris, accélérer le shader, ralentir la respiration, plisser les yeux, dilater la pupille. Le lion peut être calme, ivre, endormi, terrifié, amoureux, sans qu'on dessine quoi que ce soit de nouveau. Une seule signature visuelle, des centaines d'expressions possibles.

L'abstraction fait baisser le volume sans faire taire le personnage. On sent qu'il y a quelqu'un, on ne se sent pas écrasé par lui. C'était la troisième tentative, c'est la bonne.

## L'iconographie qu'on prend, le saint qu'on évite

Le saint dans son rocher avait un lion. Toute l'iconographie chrétienne le sait : saint Jérôme, traducteur de la Vulgate, copiste de manuscrits, ermite dans le désert, et son lion qu'il aurait apprivoisé en lui retirant une épine de la patte. Vous le trouverez chez Antonello da Messina, chez Carpaccio, chez Dürer, chez Carlo Crivelli avec sa robe terracotta, chez El Greco en cardinal rouge, chez Hemessen, chez Guercino. Toujours le même duo : un vieux savant et un lion.

J'ai pris l'iconographie. Je n'ai pas pris le saint.

Mon narrateur est le lion. Pas le saint, pas le copiste, pas l'ermite. Le lion. Et il s'appelle Caspar, ce qui n'est pas un nom de lion, comme il l'admet lui-même quelque part dans son récit. C'est un nom d'homme, un nom qu'on aurait pu donner à un enfant au siècle dernier en regardant pleuvoir par la fenêtre. Il le sait. Il l'a gardé.

Pourquoi le lion plutôt que le saint ? Parce que le saint, c'est moi qui voulais l'éviter. Parce que le lion regarde, écoute, dort, n'écrit pas, ne traduit pas, ne se met pas en avant. Il est là. Sa présence vaut quelque chose. Et parce qu'un lion qui parle est plus intéressant qu'un saint qui prêche.

## La mécanique de l'avatar

Je reviens un instant sur la version actuelle, parce que la manière dont elle est faite dit quelque chose sur le métier.

L'anneau de fumée vient d'un shader open source. Un composant WebGL qui rend du bruit GPU en temps réel : un anneau ondulant, animé, qui reprend deux couleurs d'accent du site. En mode sombre il flotte sur fond charbon avec des nuances de bleu-vert fané, en mode clair il s'inverse. C'est la crinière, et c'est aussi la respiration du personnage : il bouge, donc il vit.

Les yeux, c'est six lignes de SVG. Une amande horizontale asymétrique pour chaque œil, avec le coin extérieur pointu et le coin intérieur arrondi. Deux cercles concentriques pour l'iris et la pupille. Un léger tilt vers le bas en bord externe pour rappeler le regard de fauve. La pupille est ronde, pas verticale. La pupille verticale, c'est le chat domestique ou le serpent. Le lion regarde droit, comme un humain qui aurait des paupières plus lourdes.

J'ai testé une trentaine de formes avant de figer celle-là. Des amandes, des gouttes, des étoiles, des œils de serpent, des hexagones. À chaque fois, je validais sur des photos de référence : trois portraits de lion, un de léopard des neiges, un de chat domestique pour comprendre ce qu'il ne fallait surtout pas faire. La forme finale n'est pas une copie photographique, c'est une stylisation qui garde le signal félin sans tomber dans l'identification précise. Si je dessinais le lion, on aurait un Simba. En le réduisant à deux amandes et deux cercles, on garde l'idée du fauve et on rend toute la place au texte.

L'iris reprend la couleur d'accent du site. Caspar respire avec le site. Quand vous basculez le thème, ses yeux changent de pigment sans qu'il bouge.

Puis sont venues les humeurs. Vingt-quatre, classées en deux familles.

Douze émotions de base : neutre, perdu, confus, excité, trop mangé, trop bu, amoureux, endormi, choqué, en colère, triste, pensif.

Douze états de parole : parle posé, murmure, déclame, chuchote, hésite, affirme, questionne, rit, bafouille, réfléchit en parlant, conclut, sentence dramatique.

Chaque humeur combine trois leviers : la forme et l'orientation des yeux, la position de la pupille pour diriger le regard, et un ajustement des paramètres du shader pour que la crinière elle-même réagisse. Quand il est endormi, l'anneau ralentit et s'aplatit, presque immobile. Quand il déclame, il s'épaissit, vibre plus fort, comme une voix qui porte. Quand il bafouille, le shader devient haché. Quand il chuchote, il s'efface.

Ce n'est pas une image, c'est une marionnette technique. Et c'est ça que j'aime dans le métier : trouver un dispositif qui rend justice à une intention, sans tomber dans la décoration. Un lion fait de fumée et de géométrie, qui change d'humeur sans changer de visage. C'est plus juste, pour moi, qu'un portrait fixe.

## Un lion ronchon

Caspar n'est pas un assistant lisse. Il boude, il rouspète, il s'embarque dans des digressions, il s'arrête en plein milieu. Il ne dit pas "bonjour, comment puis-je vous aider aujourd'hui". Il dit "vous m'avez nourri, asseyez-vous".

Beaucoup d'assistants IA sont serviables. Le mien est ronchon. J'ai préféré ça parce que c'est plus rassurant, plus drôle, plus engageant, et que ça sort du lot.

Plus rassurant, ce n'est pas évident à expliquer. Un assistant capricieux devrait, en théorie, inquiéter plutôt que rassurer. Mais ça projette le visiteur dans un monde qui a du charme. Un monde qui rappelle un peu l'enfance, l'adolescence, les années quatre-vingt-dix. Il y a là une forme de nostalgie qui n'est pas un défaut, et qui ne masque pas non plus une faiblesse. C'est la culture où j'ai grandi, et celle qui me parle.

Mon site mélange plusieurs univers. Le développement, le côté un peu hacker, un peu éthique, cliché assumé. Les jeux vidéo, les sons, les couleurs, l'humour. Une certaine forme d'esthétisme qui vient d'ailleurs que de la tech. Je voulais qu'on retrouve toute une pâte de ma personnalité là-dedans. C'est mon site, c'est ma carte de visite, et je veux qu'elle me ressemble.

Côté écriture, j'ai mis la barre haut. Pas la prétention de faire mieux que les grands jeux narratifs qui m'ont marqué : *Pillars of Eternity* surtout, pour le récit construit, le lore détaillé, la cohérence dense. Mais l'ambition d'atteindre une qualité d'écriture qui ne soit pas du remplissage. Caspar parle comme un narrateur de Saint-Exupéry qui aurait joué à un CRPG.

## Méta-démonstration

Je vous parle de Caspar, mais je ne vous parle pas vraiment de Caspar. Je vous parle de ce que je sais faire.

Mon métier, c'est concevoir et orchestrer des dispositifs IA. Direction artistique, direction technique, direction de l'expérience. Un rôle d'architecte. L'exécution est faite par les agents. La valeur, c'est de savoir quoi leur demander, dans quel ordre, et de garder l'œil sur la cohérence globale.

Cent pour cent du contenu du site a été généré par IA. Les voix, les sons, les images, le code, le récit. Moi, j'ai dirigé. C'est exactement ce que je vends, et c'est exactement ce que le site démontre, simplement en existant.

Je préfère cette démonstration au case study. Vous écrivez un article sur un outil que vous avez livré : très bien, voici la technique, voici le code, voici la démarche. Mais le visiteur reste extérieur. Quand le site EST la démo, le visiteur est dedans. Il l'éprouve. Il en sort avec une expérience, pas avec une lecture.

C'est aussi pour ça que je revendique la transparence sur l'IA. Caspar est explicitement un assistant IA dans la fiction : Romain l'a trouvé, lui a confié le site, lui a demandé de raconter ce qui lui traverse l'esprit. Je ne cache rien. Et c'est tant mieux, parce que de toute façon, en 2026, les gens sentent l'IA. Vouloir la déguiser est une perte de temps. Vouloir la mettre en scène est un geste de métier.

## Moins, mais excellent

Je ne sais pas faire les choses à moitié. C'est sans doute ma marque de fabrique, et c'est peut-être un défaut. Je suis un peu zinzin sur le détail. Quand un truc n'est pas bien, ça me pique.

La conséquence, c'est que je préfère réduire le périmètre que diminuer la qualité. Moins de choses, mais toutes bien faites. Le récit de Caspar fait quarante pages, pas trois cents. Les illustrations sont au nombre de douze, pas de cinquante. Les sons sont neuf, pas trente. À chaque fois, j'ai coupé jusqu'à ce que je puisse soigner tout ce qui restait.

L'avatar tient dans la même logique. J'aurais pu garder le Caspar dessiné, plus immédiat, plus impressionnant à première vue. J'aurais eu un lion, vraiment, en image. J'ai préféré le réduire à ce qu'il avait de juste : la capuche, l'ombre, le regard, la crinière qui bouge. Tout le reste, l'illustration, le trait, le pelage, j'ai laissé tomber. Moins de pixel, plus de présence.

C'est une posture commerciale et politique. Commerciale parce qu'elle me différencie : je suis designer, développeur, directeur de création, à la fois, et je ne laisse rien au hasard. Politique parce qu'elle dit non à l'inflation contemporaine du tout-tout-le-temps, à l'esthétique du remplissage, au scope qui dilue. On peut aussi dire les choses comme ça : je préfère un site magnifique à un site exhaustif.

Et c'est gratos. Le site est ouvert à tous, le chat avec Caspar est offert, c'est moi qui paye quand vous lui parlez. On peut me reprocher d'être bourgeois, pédant, élitiste dans la forme, je l'entends. Mais le geste est démocratique. Vous entrez sans payer, vous restez si vous voulez, vous parlez si vous voulez. C'est même très populaire, dans le fond.

## Un carnet de bord

Une version du site est prête. Il y aura lundi des clients qui taperont mon nom sur internet et qui découvriront tout ça. Cette version-là est mon livrable.

Mais le site n'est pas terminé. Il ne le sera jamais. Je vais continuer à y ajouter des choses, à corriger, à creuser. C'est un carnet de bord, pas un produit fini. Caspar aura d'autres récits, d'autres humeurs, d'autres histoires à raconter. La section technique va évoluer. La direction artistique va se préciser. Le chat va s'enrichir. Le site va vieillir avec moi.

Ma mère, qui a regardé tout ça, m'a écrit : *"On a vraiment l'impression d'être pris comme un rat dans une IA, la couleur sombre, la musique, le vide, on approche cette sensation de néant. C'est flippant. Mais si c'est ton objectif, c'est très réussi."* Elle a ajouté, plus tard : *"On sent que l'humain a été désintégré."* Et après réflexion : *"Parce que c'est toi le manipulateur de l'IA."*

Je n'ai pas su quoi répondre, sinon que oui, j'ai fusionné un peu avec la machine. Ce n'est pas une formule, c'est un constat. Le métier de 2026, pour moi, c'est apprendre à orchestrer des agents tout en gardant intacte la part qui ne se génère pas : le goût, le regard, l'envie d'être à l'écart.

Comme dans le tableau de Patinir, à Madrid. Un saint, un lion, et un monde immense qui passe à côté sans les voir.

Caspar, c'est ma manière à moi d'être assis dans le rocher.
