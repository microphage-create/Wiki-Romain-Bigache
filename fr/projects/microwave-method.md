---
id: project-microwave-method
title: Microwave Method - Factory d'agents et wiki gouverné open source
type: project
category: tool
domain: project
tags: [microphage, microwave-method, open-source, pypi, agents, llm-wiki, karpathy-method, governance]
status: live
created: 2026-09-01
updated: 2026-09-01
period: 2026 / present
client: Microphage (SASU), open source
industries: [Developer Tools, AI/ML]
technologies: [Python, PyPI, Claude Code, Markdown]
team: 1 (Romain Bigache, seul)
url: https://github.com/microphage-create/microwave-method
demo: null
links:
  - experience/microphage.md
  - methodology.md
  - projects/mycelium.md
---

# Microwave Method

| Clé | Valeur |
|-----|--------|
| **Type** | Package open source : factory d'agents + méthode de wiki LLM gouverné |
| **Statut** | Publié sur PyPI (`uvx microwave-method`) |
| **Repo** | Public, [microphage-create/microwave-method](https://github.com/microphage-create/microwave-method) |
| **Équipe** | Romain Bigache (seul) |

## Description courte

Microwave Method empaquette la méthode de travail derrière l'écosystème Microphage en outil open source installable : une factory qui scaffolde des agents spécialisés et un wiki LLM gouverné façon Karpathy qui garde leur base de connaissances propre dans la durée (notes atomiques, frontmatter, wikilinks, gouvernance promote-or-purge).

Installation et lancement en une commande : `uvx microwave-method`. L'onboarding est pensé « wow first run » : le package bootstrap un premier agent (agent zéro) de bout en bout, raccourci bureau inclus.

## Pourquoi ça existe

Les setups multi-agents pourrissent vite : la connaissance se duplique, les règles se contredisent, les notes mortes s'empilent. La méthode traite le wiki comme un système gouverné (rôles dédiés de rédacteur et de gatekeeper, staging puis promote ou purge) plutôt que comme un dossier de vrac. C'est la même discipline qui maintient les vaults de règles Microphage, extraite et généralisée.

## Related

- [experience/microphage.md](../experience/microphage.md)
- [methodology.md](../methodology.md)
- [mycelium.md](./mycelium.md)
