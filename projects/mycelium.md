---
id: project-mycelium
title: Mycelium - Outillage Claude Code interne
type: project
domain: project
tags: [mycelium, claude-code, agentic-coding, internal-tooling, productivity, mcp]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2026 / present
client: Personnel / Microphage interne
industries: [Internal Tooling, AI/ML, Productivity]
team: 1 (Romain Bigache, solo)
url: null
demo: null
technologies: [Claude Code, MCP, slash commands, subagents, hooks, settings, memory, Markdown, YAML]
links:
  - experience/microphage.md
  - stack.md
---

# Mycelium

| Cle | Valeur |
|-----|--------|
| **Type** | Outillage interne Claude Code (skills custom, agents, hooks, memoire) |
| **Statut** | En production interne |
| **Annee** | 2026 - en cours |
| **Visibilite** | Non public (asset interne Microphage) |
| **Equipe** | Romain Bigache (seul) |

## Titre court

Stack d'outillage Claude Code interne pour orchestrer le travail multi-projet en solo.

## Description courte

Mycelium est l'infrastructure interne qui industrialise le travail solo de Marcel sur tous les projets Microphage : skills Claude Code dedies par domaine (creative, dev, ops, business), subagents specialises, hooks de session, memoire persistente structuree. Permet de tenir le rythme de livraison (POC en 3 semaines) en automatisant le boilerplate cognitif.

## Description longue

### Probleme resolu

Travailler en solo sur 4-6 projets en parallele (Microphage Analyzer Pro, Altaria, fusil.paris, romainbigache.com, missions clients) demande de jongler entre des contextes tres differents : design, code, copy, ops, juridique. Le cout de switching mental est enorme et fragmente la productivite.

### Approche

Au lieu de re-expliquer le contexte a Claude Code a chaque session, Mycelium structure la connaissance en :

- **Skills par domaine** : chaque domaine professionnel (design, dev, copy, ops, juridique) a sa skill custom avec sa personnalite, ses regles, son workspace, ses files I/O
- **Subagents specialises** : delegation des recherches longues, audits, refactos a des agents focalises
- **Hooks de session** : automatisation des routines start/end, registry update, retro
- **Memoire persistente** : capture des apprentissages, decisions, patterns reutilisables a travers les sessions
- **Conventions documentees** : nomenclature, structure de dossiers, file protection, anti-duplication

### Resultat

L'environnement complet est instancie en moins de 5 secondes au demarrage. Claude Code peut piloter une session Microphage Analyzer Pro, basculer sur un sprint Altaria, repondre a un brief OXGEN, et terminer sur une analyse juridique dans la meme conversation, sans charge cognitive supplementaire.

### Methodologie

Mycelium applique la methodologie Karpathy LLM Wiki sur l'outillage interne lui-meme : single source of truth, lazy loading, fichiers atomiques par skill, frontmatter conventionne. La structure du wiki sert de meta-modele : Mycelium est documente exactement comme il documente les autres projets.

## Pourquoi c'est differenciant

Profil designer + dev + content + ops, le tout orchestre par une stack Claude Code custom : Marcel ne se contente pas d'utiliser des outils IA, il les forge pour son propre flux de travail. C'est ce qui permet la compression du cycle (POC en 3 semaines) qui est sa signature commerciale.

## Visibilite

Repo non public (asset strategique interne). Disponible en demo live ou en walkthrough sur demande, dans un cadre confidentiel.

## Related

- [experience/microphage.md](../experience/microphage.md)
- [stack.md](../stack.md)
- [expertise.md](../expertise.md)
