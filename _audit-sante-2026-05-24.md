---
id: audit-sante-2026-05-24
title: Audit santé Wiki-Romain-Bigache 2026-05-24
type: meta
domain: wiki-conventions
tags: [meta, audit, wiki-health, integrity-check, read-only]
status: live
created: 2026-05-24
updated: 2026-05-24
owner: sous-agent CHERCHEUR /v2 Microphage
mode: read-only audit, zero fix appliqué
---

# Audit santé wiki Romain Bigache — 2026-05-24

## Ce qui s'est passé

Sous-agent CHERCHEUR /v2 lancé sur le wiki perso `Wiki-Romain-Bigache/` (parcours Romain, 113 atomes EN+FR), premier audit santé global. Méthode dérivée de la session Sub 12 (audit wiki produit Microphage Analyzer Pro), adaptée à la convention spécifique de ce wiki : IDs en slug (pas namespacés `LRN-XXX`), cross-links en chemins markdown relatifs (`./projects/foo.md`), pas de wikilinks `[[ID]]`, mirror bilingue EN root + `fr/` subtree.

Méthode appliquée :
1. Inventaire factuel (113 fichiers .md hors `.git`, `_assets`, `scripts`)
2. Parse frontmatter par parser maison + comparaison `_schema.md` (8 champs required)
3. Recherche collisions ID `id:` frontmatter (avec règle du script `scripts/wiki-romain.py validate` : EN et FR sont 2 namespaces séparés)
4. Extraction tous markdown links `[text](./path.md)` + check existence
5. Détection orphelins (atomes jamais référencés par aucun autre)
6. Audit asymétries `## Related` (A→B sans B→A)
7. Couverture bilingue (EN sans FR ou inverse)
8. Conventions schéma : em-dash, 360Learning confidentiel, kebab-case naming
9. Diff `llms.txt` + `README.md` + `fr/README.md` vs réalité fs
10. Run du `scripts/wiki-romain.py validate` natif pour cross-check

Read-only strict, zéro fix appliqué, zéro commit.

## Ce qu'on a découvert

### Volumétrie

- **113 atomes** au total (hors scripts/templates et assets)
  - 54 fichiers EN root
  - 55 fichiers FR mirror
  - 2 fichiers `_inbox/` (capture brute via `/keep`)
  - 2 README + 2 _schema (hubs bilingues)
- 16 types frontmatter distincts (`project` 36, `experience` 28, `writing` 17, `expertise` 6, etc.)
- Le `wiki-romain.py validate` natif remonte **9 errors + 2 warnings** côté frontmatter/types

### Métriques santé wiki

- **Frontmatter cassé** : 1 fichier (`writing/ai-product-builder.md`) avec YAML parse fail (description non quotée contient un `: `). 6 autres fichiers writing/ ont la même structure non-quotée à risque mais leur description ne contient pas `: ` heureusement.
- **Broken markdown links** : 4 occurrences pointant vers `experience/adeo-leroy-merlin.md` qui n'existe pas côté EN (le fichier EN est nommé `experience/adeo.md`)
- **Types invalides** : `award` (×2) et `making-of` (×1) ne sont pas dans la taxonomie de `_schema.md`
- **Atomes orphelins** : 12 fichiers (10.6% du wiki) jamais référencés par aucun autre, dont 4 fichiers experience EN non liés depuis README/llms.txt (ecole-multimedia, entretiens-excellence, siestes-electroniques, cabanon-records, plus le souci adeo).
- **Asymétries `## Related`** : 159 paires unidirectionnelles
- **Indexes obsolètes** : `llms.txt` (115 lignes) et les 2 README (EN + FR) datent visiblement de la 1ère vague (2026-04-30 / 2026-05-08) et ratent 6+ atomes ajoutés ensuite
- **Em-dash** : 0 violation (conventions schéma OK sur ce point)
- **360Learning** : seules les 2 copies de `_schema.md` mentionnent "360Learning" (explicitement comme nom redacté dans la doctrine de confidentialité, pas une fuite)

---

## Findings HIGH (intégrité critique + drift indexes)

### HIGH-1 — `writing/ai-product-builder.md` frontmatter YAML cassé

**Symptôme** :
```yaml
description: A definition pulled from what I actually ship: apps, agents, e-commerce, plugins. Not slides about AI.
```

Le `: ` après "ship" fait croire au parser YAML qu'on ouvre une mapping nested. Le `wiki-romain.py validate` natif confirme :
> FRONTMATTER ISSUE (YAML invalid: mapping values are not allowed here): writing\ai-product-builder.md

**Impact** : tout consommateur YAML strict (futur site `romainbigache-com` Next.js si `gray-matter`, génération llms.txt si refacto, ATS export, etc.) plante en parsant l'article. L'atome devient invisible pour les indexes auto-générés et le CV pourrait perdre une référence centrale. Mon parser maison de l'audit a parsé en mode tolérant et n'a rien vu, c'est uniquement le validateur natif qui flag.

**Reco** : quoter toutes les `description:` avec `"..."` dans les 8 fichiers writing/ + 1 FR caspar (audit préventif), pas seulement le 1 qui crash aujourd'hui. Pattern systémique pas point fix.

**Fichiers à patcher** :
- `writing/ai-product-builder.md` (crash actuel)
- `writing/content-design.md` (risque latent si édition future ajoute `: `)
- `writing/entretiens.md`
- `writing/morphow-mascotte-ia.md`
- `writing/personal-branding-introvert.md`
- `writing/personne-ne-peaufine.md`
- `writing/vibe-coding-burnout.md`
- `fr/writing/caspar-le-narrateur.md`

### HIGH-2 — Filename mismatch `experience/adeo.md` vs schema + 4 broken links

**Symptôme** : `_schema.md` ligne 97 documente le fichier comme `experience/adeo-leroy-merlin.md`. FS réel : EN = `experience/adeo.md`, FR = `fr/experience/adeo-leroy-merlin.md`. **Asymétrie de naming entre EN et FR** sur le seul atome de ce type. Conséquence : 4 broken markdown links pointent vers le nom FR depuis EN :

- `cv.md` → `./experience/adeo-leroy-merlin.md` (cassé)
- `README.md` → `./experience/adeo-leroy-merlin.md` (cassé, 2×)
- `writing/content-design.md` → `../experience/adeo-leroy-merlin.md` (cassé)

L'atome `experience/adeo.md` est donc **orphelin côté EN** (jamais référencé via son vrai nom). L'`id:` est identique côté EN et FR (`experience-adeo-leroy-merlin`), donc le validate natif ne flagge rien.

**Impact** : site futur `romainbigache-com` qui construit la navigation depuis links markdown verra 4 liens cassés. Le CV PDF qui mentionne ADEO/Leroy Merlin loupe sa source. La cohérence bilingue est rompue (seul atome où le filename diverge entre EN et FR).

**Reco** : renommer `experience/adeo.md` → `experience/adeo-leroy-merlin.md` (aligner sur FR + schema), patcher les 4 liens cassés. Choix alternatif (rename FR vers `adeo.md`) impose de patcher le schéma + le validate.

### HIGH-3 — `llms.txt` et les 2 README sont stale (6+ atomes manquants)

**Symptôme** : `llms.txt` (auto-généré théoriquement) n'inclut PAS :
- `experience/ecole-multimedia.md` (2026-05-08)
- `experience/entretiens-excellence.md` (2026-05-08)
- `experience/siestes-electroniques.md` (archived)
- `experience/cabanon-records.md` (archived)
- `writing/personne-ne-peaufine.md` (2026-05-08)
- `fr/writing/caspar-le-narrateur.md` (2026-05-19, FR-only)
- Les 2 fichiers `_inbox/`

Idem côté `README.md` et `fr/README.md` (0 mention de ces fichiers).

`scripts/wiki-romain.py rebuild-llms-txt` existe mais n'a pas été lancé depuis ~16 jours. Soit le rebuild manuel a été oublié, soit aucun hook ne le force.

**Impact** : un agent qui ingère llms.txt au startup (ce qui est le point d'entrée du LLM index, c'est dans le nom du fichier) ignore l'existence de 6+ atomes dont 2 expériences pédagogiques (Polytechnique mentorat, École Multimédia masterclass) qui sont stratégiques pour le pitch carrière Marcel. Le CV PDF construit depuis ce wiki pourrait omettre ces expériences.

**Reco** : (a) lancer `python scripts/wiki-romain.py rebuild-llms-txt` maintenant, (b) ajouter dans `scripts/wiki-romain.py sync` un appel à `rebuild-llms-txt` avant le commit git, (c) patcher les 2 README à la main ou créer un `rebuild-readme` similaire au rebuild llms.txt.

### HIGH-4 — Types `award` et `making-of` invalides selon `_schema.md`

**Symptôme** : `_schema.md` ligne 55-68 taxonomie des types valides liste 14 types. `award` et `making-of` n'y sont pas, alors qu'ils sont utilisés :
- `awards/bjj-european-2025.md` + `fr/awards/bjj-european-2025.md` : `type: award`
- `_inbox/2026-05-21-spec-driven-html-mockup-pattern.md` : `type: making-of`

Le validate natif flag 3 errors :
> INVALID TYPE 'award': awards\bjj-european-2025.md
> INVALID TYPE 'award': fr\awards\bjj-european-2025.md
> INVALID TYPE 'making-of': _inbox\2026-05-21-spec-driven-html-mockup-pattern.md

**Impact** : le validate échoue avec exit code 1, donc un éventuel hook pre-commit `wiki-romain.py validate` bloque tout commit futur tant que ces types ne sont pas légalisés OU les fichiers retypés. C'est probablement pour ça que la chaîne sync git n'est pas blindée.

**Reco** : étendre `VALID_TYPES` dans `scripts/wiki-romain.py` pour inclure `award` et `making-of` (typage légitime, pas une faute), puis mettre à jour `_schema.md` taxonomie en miroir. Choix alternatif : retyper en `personal` pour award (cohérent avec `domain: personal`) et `writing` pour le making-of (cohérent avec son contenu).

### HIGH-5 — Inconsistance ID FR : `caspar-le-narrateur-fr` vs convention "même id EN/FR"

**Symptôme** : 53 paires d'atomes EN+FR partagent strictement le même `id:` frontmatter (par design — le `validate` les sépare en 2 buckets `ids_en` et `ids_fr`). Une seule exception : `fr/writing/caspar-le-narrateur.md` a `id: writing-caspar-le-narrateur-fr` (suffixe `-fr`) **sans qu'un atome EN équivalent existe**. C'est un FR-only puisque l'article n'est pas encore traduit.

**Impact** : double ambiguïté. (a) si Marcel traduit Caspar en EN demain et reprend l'id `writing-caspar-le-narrateur` côté EN, il aura 1 atome EN + 1 atome FR avec id différent (rupture de convention). (b) si un consommateur de l'index croit que `-fr` suffixe désigne "FR-only", il rate que les 53 autres FR n'ont jamais ce suffixe.

**Reco** : choisir une convention et la tenir. Soit (A) tous les FR ont id identique à EN (= renommer caspar id en `writing-caspar-le-narrateur`, accepter que sans EN l'atome reste FR-only par sa localisation `fr/`), soit (B) tous les FR ont suffixe `-fr` (= patcher les 52 autres FR pour ajouter `-fr`). Option A semble plus économe.

---

## Findings MEDIUM (drift structurel, asymétries, conventions partiellement appliquées)

### MEDIUM-1 — 10 fichiers `fr/projects/case-*.md` n'ont pas de section `## Related`

**Symptôme** : tous les EN case-* projects ont une section `## Related` en bas. Aucun des 10 FR `fr/projects/case-*.md` ne l'a. C'est systématique, pas anecdotique.

EN OK : altarea, citeo, danone-cyber, danone-itsurvey, enedis, idex, jja, manutan, pai-partners, safran
FR KO (les mêmes 10).

Tous ont bien le champ `links:` en frontmatter (donc la navigation forward existe), mais la convention `_schema.md` ligne 22 dit "Explicit cross-links. A `## Related` section at the bottom of each file lists adjacent files." → manqué pour ces 10.

**Reco** : ajouter `## Related` à chacun des 10 fichiers FR, miroir simple du EN homologue.

### MEDIUM-2 — `fr/writing/caspar-le-narrateur.md` orphelin + sans `## Related`

**Symptôme** : `fr/writing/caspar-le-narrateur.md` (article making-of, 2026-05-19) n'est référencé par aucun autre fichier ET n'a pas de section `## Related`. Le `fr/writing.md` (index des articles FR) ne le mentionne pas non plus.

**Reco** : ajouter Caspar à `fr/writing.md` index + section `## Related` au bas du Caspar pointant vers `writing.md`, `profile.md`, `projects/romainbigache-com.md`.

### MEDIUM-3 — 12 atomes orphelins (10.6% du wiki)

Liste complète (atomes jamais référencés par aucun autre via markdown link) :
1. `_inbox/2026-05-21-spec-driven-html-mockup-pattern.md` (normal, inbox)
2. `_inbox/README.md` (normal, helper)
3. `awards/bjj-european-2025.md` + miroir FR (orphelins malgré links: personal.md, asymétrie)
4. `experience/adeo.md` (cassé via mismatch filename, cf HIGH-2)
5. `experience/ecole-multimedia.md` + miroir FR (oubli index)
6. `experience/entretiens-excellence.md` + miroir FR (oubli index)
7. `experience/siestes-electroniques.md` + miroir FR (archived, mais 0 ref)
8. `fr/writing/caspar-le-narrateur.md` (FR-only, cf MEDIUM-2)

**Impact** : ces atomes existent mais ne sont jamais découverts par navigation. Si le futur site `romainbigache-com` construit le graph depuis les markdown links, ces pages auront orphan SEO.

**Reco** : revue manuelle de chaque orphelin → soit ajouter à README/llms.txt/index parent (si encore live), soit move `_archive/` (si vraiment dépassé). Les 2 archived (cabanon-records, siestes-electroniques) gagnent à être référencés au moins depuis `personal.md` ou `experience` hub.

### MEDIUM-4 — 159 asymétries `## Related` total

Échantillon : `cv.md` → `availability.md` (no back-link), `cv.md` → `stack.md` (no back-link), `education.md` → `experience/havas-paris.md` (no back-link), etc. Wiki Karpathy = graph bidirectionnel par doctrine. 159 paires = 1.4 par atome moyen → pas en cause individuellement mais cumul important pour la navigation reverse.

**Caveat (limite validité)** : certaines asymétries sont design (hubs comme README/profile linkent vers tout sans back-link nécessaire). Compte gonflé pour les 7 fichiers hub top-level.

**Reco** : script `wiki validate --check-symmetry` qui suggère les pairs (en excluant les hubs définis dans une liste). Pas une priorité P0, plombier de fond.

### MEDIUM-5 — `_inbox/2026-05-21-spec-driven-html-mockup-pattern.md` non conforme schema

**Symptôme** : 4 champs required manquants (`id`, `domain`, `created`, `updated`) + type `making-of` non listé schema. Le validate flag 5 errors sur ce fichier.

**Impact** : `_inbox/` est zone "capture brute via `/keep`" donc tolérance attendue, MAIS si Marcel `/review-weekly` digère plus tard cet atome (ce qui est le workflow officiel), il faut soit le promouvoir en `writing/` avec frontmatter complet, soit ajouter une exception `_inbox/` dans le validate.

**Reco** : (a) `wiki-romain.py validate` ignore `_inbox/` dans son scan (ajout d'un `EXCLUDE_DIRS`), OU (b) `/keep` génère un frontmatter minimal valide même en inbox (id timestamp slug, type `making-of` une fois ajouté, domain=`inbox`, created/updated=now). Option B plus saine.

### MEDIUM-6 — 60 atomes avec `updated: 2026-04-30` jamais re-stampés (53% du wiki)

**Symptôme** : 60 fichiers ont `updated: 2026-04-30` (date de seed initial). Aucune édition tracée depuis 24 jours alors que certains ont vraisemblablement été modifiés (e.g. `stack.md`, `keywords.md`, `expertise.md` mentionnent technologies/clients récents). Soit les éditions ne refresh pas `updated`, soit vraiment aucune édition.

**Limite validité** : impossible de différencier depuis ce rapport "non édité" vs "édité sans refresh updated". Le git log ferait foi mais hors scope read-only.

**Reco** : `scripts/wiki-romain.py update --refresh-updated <path>` qui met à jour le champ + hook pre-commit qui refresh `updated` sur tous les fichiers stagés. Sinon le champ devient mensonger.

### MEDIUM-7 — `experience/adeo.md` non-conforme kebab-case selon le schema convention

**Symptôme** : convention `_schema.md` ligne 121 "id identifiers in kebab-case, no accents". `experience/adeo.md` filename est kebab-case (OK) mais l'id `experience-adeo-leroy-merlin` ne match plus le filename `adeo`. Ailleurs dans le wiki la convention id = `<type>-<filename>` est respectée (verifié sur 53 paires).

**Reco** : aligner via HIGH-2 (rename file → `adeo-leroy-merlin.md`).

### MEDIUM-8 — `expertise/interactive-mockup.md` confidential flag actif sans review trace

**Symptôme** : 2 fichiers (`expertise/interactive-mockup.md` + miroir FR) ont `confidential: true`. Le validate warn : "review before push public". Aucun fichier d'audit ne trace si la review a été faite. Si le wiki est poussé sur GitHub privé, OK. Sur public, leak.

**Reco** : `_inbox/_audit-confidential.md` ou tag explicite dans chaque fichier `confidential_reviewed_by: <name> on <date>`.

---

## Findings LOW (typos, conventions partielles, débris)

### LOW-1 — `expertise.md` indexe `expertise/direction-de-creation.md` et `expertise/interactive-mockup.md` mais le schema ne les liste pas dans repo structure

`_schema.md` ligne 73-112 ne mentionne pas le sous-dossier `expertise/`. Sous-dossier existe pourtant. Doc obsolète.

### LOW-2 — `awards/` sous-dossier idem non mentionné dans schema repo structure

Schema repo structure ne mentionne pas `awards/`. Fichiers existent.

### LOW-3 — `projects/cloud-academy-coach.md` et `projects/video-transcriber.md` n'ont pas de FR mirror

EN-only sur 3 fichiers : `experience/adeo.md`, `projects/cloud-academy-coach.md`, `projects/video-transcriber.md`. Les 2 projets sont récents (2026-05) et probablement pas encore traduits. Pas un bug, à flagger comme dette de traduction.

`scripts/wiki-romain.py missing-translation` existe (ligne 318) probablement pour ça. À lancer pour confirmer le diagnostic et tracker.

### LOW-4 — Le `description:` non quotée est un anti-pattern systémique sur 8 fichiers writing/

Cf HIGH-1. Aujourd'hui 1 seul crash (ai-product-builder), mais les 7 autres sont latents. Si Marcel édite leur description en ajoutant `: ` (très probable, c'est un séparateur naturel en pitch FR), boom.

### LOW-5 — `_schema.md` ligne 109 liste `projects/` avec 5 fichiers — réel 16 fichiers

Drift documentaire similaire au `_index.md` du wiki produit. Pas critique car le wiki en JS rebuild depuis filesystem, mais induit un lecteur humain en erreur.

### LOW-6 — Pas de section "Lint" runnée traçable

Le `_schema.md` ligne 137 dit "On every update, check: [ ] Frontmatter complete ... [ ] No em-dash ... [ ] No nominal mention of 360Learning". Aucun fichier ne trace la dernière exécution. Le `validate` existe mais n'écrit pas de log.

### LOW-7 — `_inbox/README.md` sans frontmatter

Cf MEDIUM-5. Validate flag. Mais c'est un README de dossier, exception légitime. Reco : add exception dans validate pour `*/README.md`.

### LOW-8 — `fr/_schema.md` est une copie carbone du EN _schema (non testé) — risque drift entre 2 sources of truth

Si Marcel patch un schema, doit-il patcher l'autre ? Pas de mécanisme de sync entre les 2. Doublon de source-of-truth.

### LOW-9 — `links:` array vs `## Related` section : 2 mécanismes parallèles, pas consolidés

Le frontmatter a `links: [path1, path2]`, ET le body a `## Related` avec liens markdown. Les 2 sont maintenus en parallèle, source de divergence. Aucun script ne valide que `links:` ⊆ `## Related` ou inverse.

### LOW-10 — Le wiki perso a 0 capture date `updated:` post 2026-05-23 sauf `methodology.md`

Très peu d'activité récente. Probable que les sessions /v2 et /suez de mai 24 n'ont rien capturé sur le wiki perso (ce qui est cohérent — c'est un wiki parcours, pas un wiki produit).

---

## Limites de validité (steelman own results)

Avant de transmettre ce rapport, voici les biais identifiés :

1. **Parser frontmatter maison vs YAML strict** : mon audit utilise un parser regex-based tolérant pour récupérer même les frontmatters cassés (sinon je manquerais HIGH-1). Conséquence : j'ai pu sur-interpréter certains champs sur les fichiers à frontmatter exotique. J'ai cross-checké avec le `validate` natif pour les 9 erreurs flagged.

2. **Markdown link regex** : `\[([^\]]+)\]\((\./[^)]+\.md|...)\)` match les liens classiques mais peut rater des cas : liens multi-lignes, liens avec parenthèses internes, liens MDX si jamais le wiki en a (a priori non, c'est du markdown brut). 4 broken links flagged est un minorant.

3. **Détection orphelins par seule analyse statique** : un atome peut être "orphelin" dans le wiki mais référencé depuis le futur site `romainbigache-com/` (lib séparée) ou depuis le CV PDF généré. Hors scope read-only. Le compte 12 orphelins peut être réduit après check externe.

4. **Asymétries `## Related` (159)** : compte mécanique, ne distingue pas asymétries design (hubs) des asymétries bugs. Surestimation probable. Le vrai chiffre actionnable est plutôt 30-50 (à valider manuellement par Marcel ou un patch tool).

5. **Bilingue EN/FR** : j'ai considéré que tout fichier EN doit avoir FR mirror et inverse. C'est la convention mais le schema ne l'enforce pas strictement (3 projets EN-only récents sont design, pas dette). Le `missing-translation` natif est plus précis que mon comptage naïf.

6. **Test sur YAML "à risque"** : j'ai marqué 7 fichiers writing/ comme "anti-pattern systémique" parce qu'ils ont description non-quotée. En réalité, seul 1 crash actuellement (ai-product-builder). Les 6 autres sont des risques latents, pas des bugs présents. Distinction important pour la priorisation.

7. **Drift indexes** : j'ai constaté que llms.txt + README ratent 6+ atomes, mais je n'ai pas vérifié si `scripts/wiki-romain.py rebuild-llms-txt` produit ces atomes manquants ou s'il a aussi un bug. À tester en relançant la commande après les fixes HIGH-1/2/4.

**Ce que ce rapport prouve** : il y a au moins 5 findings HIGH structurels, 8 MEDIUM, 10 LOW dans l'état actuel du wiki perso.

**Ce qu'il ne prouve PAS** : qu'il n'y en a pas d'autres, en particulier (a) contradictions sémantiques entre EN et FR (par ex. claims différents dans `cv.md` EN vs FR — non testé), (b) staleness vraie vs faux-stale via git log (hors scope), (c) cohérence des `tags:` cross-atomes (un tag `ux-writing` orthographié `ux-writer` ou `uxwriting` ailleurs — non testé). Probabilité élevée que ces classes existent.

---

## Sur ton disque

- Ce rapport : [_audit-sante-2026-05-24.md](file:///C:/Users/Marcel/Documents/GitHub/Wiki-Romain-Bigache/_audit-sante-2026-05-24.md)
- Aucun autre fichier touché. READ-ONLY strict respecté.
- Script audit Python (réutilisable) : [audit_wiki_perso.py](file:///C:/Users/Marcel/Documents/GitHub/mycelium/Temp/audit_wiki_perso.py)

---

## Ce que tu fais ensuite (3 niveaux d'arbitrage Marcel)

**P0 immédiat (10-15 min, fix bug avéré)** :
1. Quoter `description:` de `writing/ai-product-builder.md` (et les 7 autres writing/ par cohérence préventive). Cf HIGH-1.
2. Renommer `experience/adeo.md` → `experience/adeo-leroy-merlin.md` + patch 4 liens cassés (cv.md, README.md ×2, writing/content-design.md). Cf HIGH-2.
3. Étendre `VALID_TYPES` dans `scripts/wiki-romain.py` pour inclure `award` + `making-of` (alignement schema). Cf HIGH-4.

**P1 cette semaine (30-60 min, drift indexes + conventions)** :
4. Lancer `python scripts/wiki-romain.py rebuild-llms-txt`. Cf HIGH-3.
5. Patcher README.md + fr/README.md à la main pour ajouter les 6+ atomes manquants (ou créer script `rebuild-readme`).
6. Décider conv id FR : soit retirer le `-fr` de `caspar-le-narrateur` (option A), soit patcher les 52 autres (option B). Cf HIGH-5.
7. Ajouter section `## Related` aux 10 `fr/projects/case-*.md`. Cf MEDIUM-1.
8. Référencer ou archiver les 12 orphelins (ecole-multimedia, entretiens-excellence, siestes-electroniques, cabanon-records, Caspar FR, etc.). Cf MEDIUM-3.

**P2 chantier infra (1-2 sessions dédiées)** :
9. `scripts/wiki-romain.py validate` étendu : (a) exception `_inbox/` et `*/README.md`, (b) check `links:` ⊆ `## Related`, (c) flag `description:` non quotée si contient `: `, (d) flag asymétries `## Related` avec liste hubs autorisés, (e) rebuild indexes auto.
10. Hook pre-commit qui run `validate` + refresh `updated:` sur fichiers stagés + rebuild llms.txt.
11. Sync `fr/_schema.md` ⇄ `_schema.md` automatique (ou éliminer le doublon).
12. `wiki-romain.py audit-confidential` qui trace les `confidential: true` review.

**Pas de pression à tout faire ce soir.** Wiki perso marche fonctionnellement, le seul vrai crash est HIGH-1 sur 1 fichier. Le reste est dette qualité accumulée.

---

## Métriques finales

- **5 findings HIGH** (YAML cassé, filename mismatch + 4 broken links, indexes stale, types invalides, convention ID FR)
- **8 findings MEDIUM** (10 FR cases sans Related, orphelin Caspar, 12 orphelins total, 159 asym Related, _inbox non conforme, updated stale 60 fichiers, naming/id mismatch adeo, confidential review tracking)
- **10 findings LOW** (schema doc obsolète × 2, 3 EN-only projets, 7 description non-quotée latentes, drift schema vs réalité, lint trace, README inbox, schema dual EN/FR, links vs Related)

**Méta-pattern émergent** : la cause systémique des findings HIGH/MEDIUM = **absence d'un cycle "validate → rebuild → commit" automatisé**. Le wiki a TOUS les outils nécessaires (`scripts/wiki-romain.py validate`, `rebuild-llms-txt`, `sync`) mais aucun hook ne les chaîne. Résultat : le validate échoue silencieusement (9 errors), les indexes drift, et les conventions partielles (ID FR, types, `## Related`) s'accumulent.

Comparaison avec audit Sub 12 wiki produit : le wiki produit a un drift sémantique (doctrine pivotée non capturée). Le wiki perso a un drift mécanique (outils existent mais pas chaînés). Wiki perso est en meilleure santé sémantique mais moins outillé en CI. Inversement, le wiki produit a un index minifié maintenu, le wiki perso oublie de rebuild llms.txt.

**Reco transverse meta** : un hook unique `pre-commit` dans les 2 wikis qui chaîne `validate + rebuild-indexes + refresh-updated`. C'est la seule defense P0 contre le drift cumulatif.

## Related

- [README.md](./README.md)
- [_schema.md](./_schema.md)
- Audit jumeau wiki produit : `microphage-analyzer-pro-bmad/wiki/sessions/2026-05-24-audit-sante-wiki-karpathy.md`
