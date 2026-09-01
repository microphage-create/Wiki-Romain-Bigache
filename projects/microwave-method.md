---
id: project-microwave-method
title: Microwave Method - Open-source agent factory and governed wiki
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
team: 1 (Romain Bigache, solo)
url: https://github.com/microphage-create/microwave-method
demo: null
links:
  - experience/microphage.md
  - methodology.md
  - projects/mycelium.md
---

# Microwave Method

| Key | Value |
|-----|-------|
| **Type** | Open-source package: agent factory + governed LLM wiki method |
| **Status** | Published on PyPI (`uvx microwave-method`) |
| **Repo** | Public, [microphage-create/microwave-method](https://github.com/microphage-create/microwave-method) |
| **Team** | Romain Bigache (solo) |

## Short description

Microwave Method packages the working method behind the Microphage ecosystem into an installable open-source tool: a factory that scaffolds specialized agents and a governed, Karpathy-style LLM wiki that keeps their knowledge base clean over time (atomic notes, frontmatter, wikilinks, promote-or-purge governance).

Install and run with a single command: `uvx microwave-method`. Onboarding is designed as a "wow first run": the package bootstraps a first agent (agent zero) end to end, desktop shortcut included.

## Why it exists

Multi-agent setups rot fast: knowledge duplicates, rules contradict each other, dead notes pile up. The method treats the wiki as a governed system (dedicated writer and gatekeeper roles, staging then promote or purge) instead of a dump folder. It is the same discipline that maintains the Microphage rule vaults, extracted and generalized.

## Related

- [experience/microphage.md](../experience/microphage.md)
- [methodology.md](../methodology.md)
- [mycelium.md](./mycelium.md)
