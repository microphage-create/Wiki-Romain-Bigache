---
id: experience-bforbank
title: BforBank - Lead UX Writer & Visual
type: experience
domain: experience
tags: [bforbank, banking, ai, rag, langgraph, gemini, content-design, management, agile, compliance]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2023-12 / 2025-12
employer: BforBank (filiale Credit Agricole)
location: Paris, France
industry: Banque en ligne / Fintech
links:
  - projects/la-plume-bforbank.md
  - stack.md
  - expertise.md
---

# BforBank - Lead UX Writer & Visual

| Clé | Valeur |
|-----|--------|
| **Période** | Décembre 2023 - Décembre 2025 (2 ans) |
| **Localisation** | Paris, France |
| **Entreprise** | BforBank (filiale Crédit Agricole) |
| **Industrie** | Banque en ligne |
| **Rôle** | Lead UX Writer & Visual |

## Mission

Refonte en profondeur des contenus, FAQ, documentation et IA appliquée chez BforBank. Approche globale pour remettre de la cohérence partout, et simplifier à la fois l'usage et la production.

C'est sur cette mission que j'ai commencé à développer mes propres outils IA, passant progressivement du rôle de Lead UX Writer à celui de builder.

## Management

Management direct d'une équipe de 3 personnes : 2 designers + 1 alternante.

## Pilotage

Pilotage en agile (sprints, rituels) en environnement bancaire fortement processé :

- PM (Product Manager)
- Tribe Leader (responsable de tribu agile)
- Équipes Marketing
- Service Relation Client (SRC)
- Direction
- Validations Compliance et Conformité

## Chantier 1 - « La Plume » : assistant IA interne pour les designers

Architecture RAG complète sur Gemini 2.5 Pro avec orchestration LangGraph. Embeddings text-multilingual-embedding-002 (FR/EN), SemanticSplitter custom, indexation sur charte éditoriale et guidelines.

Workflow d'agent : router → summarizer → RAG → génération → tool calling → génération d'image. Garde-fous éditoriaux pour bloquer les formulations interdites par la conformité bancaire.

Déployée dans la marketplace BforBank GPT, utilisée par les équipes design.

Detail complet : [projects/la-plume-bforbank.md](../projects/la-plume-bforbank.md).

## Chantier 2 - Lancement du chat service client (clients in-app)

Direction de la méthodologie data : couplage de 3 sources internes (FAQ publiques, tickets service client, retours SRC) en un corpus unifié. Production de 250+ articles LLM-ready (titre, intent, réponse autoportante, formulations alternatives, exclusions explicites pour éviter les hallucinations sur sujets régulés). Construction d'un bot RAG GPT custom comme outil de production éditoriale interne pour tenir le rythme.

Detail complet : [projects/la-plume-bforbank.md](../projects/la-plume-bforbank.md).

## Chantier 3 - Plugin Figma proprietaire

Développement du plugin Figma d'audit UX writing devenu projet fondateur de Microphage. Premier prototype d'analyse de maquettes par IA (vision + métadonnées Figma).

Detail : [projects/microphage-analyzer-pro.md](../projects/microphage-analyzer-pro.md).

## Chantier 4 - Refonte editoriale globale

Audit complet des interfaces mobile et desktop (incohérences, doublons, messages flous ou absents). Réécriture des contenus problématiques et création de tous les micro-contenus des nouveaux parcours, en binôme avec les designers.

FAQ augmentée : rédaction de centaines d'articles au format conversationnel (chatbot) et classique (SEO, support).

Refonte de parcours encadrés par des obligations légales strictes (assurance vie). Intégration des contenus dans Lokalise pour la cohérence multilingue.

Animation d'ateliers de formation à l'UX writing et aux usages IA.

## Compétences mobilisées

- Management d'équipe en environnement bancaire régulé
- Pilotage de projet en agile multi-stakeholders
- Architecture RAG et orchestration d'agents IA
- Méthodologie data pour LLM (corpus structurés)
- Direction éditoriale en cadre Compliance
- Animation et formation

## Related

- [projects/la-plume-bforbank.md](../projects/la-plume-bforbank.md)
- [projects/microphage-analyzer-pro.md](../projects/microphage-analyzer-pro.md)
- [stack.md](../stack.md)
- [expertise.md](../expertise.md)
- [press.md](../press.md)
