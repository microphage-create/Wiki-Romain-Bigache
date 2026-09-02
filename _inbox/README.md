# _inbox/

Capture flat de bouts à digérer plus tard : anecdotes, observations, tips, citations, idées d'articles, leçons.

## Comment on remplit

Pendant une session Claude Code (n'importe quelle skill, n'importe quel repo), Marcel invoque `/keep`. La skill pose 2 questions courtes (contenu + tags optionnels), génère un fichier ici.

Format : `YYYY-MM-DD-HHMMSS-{slug}.md`

## Comment on digère

- **Pendant `/review-weekly`** : scan rapide de l'inbox, identifier les bouts qui méritent un article, un projet, une note mémoire.
- **Quand Marcel veut écrire un article** : grep par tags ou date, retrouver les anecdotes pertinentes.
- **Quand un thème émerge** : 3+ entrées avec le même tag = signal pour écrire.

## Ce que c'est PAS

- Pas une source de vérité (les fichiers principaux du wiki le sont).
- Pas un journal complet (juste les bouts qui valent le coup d'être gardés).
- Pas pour les composants validés (utiliser `/block save` → `morphow-kit`).
- Pas pour les apprentissages mémoire système (utiliser `/auto-learn` → `mycelium/memory/`).

## Convention

Frontmatter minimal :

```yaml
---
captured: 2026-05-08T15:23:30
tags: [mockup, peaufinage, anecdote]
status: inbox
---

[contenu tel quel]
```

`status` peut évoluer : `inbox` → `digested` (quand le bout a alimenté un article) ou supprimé.
