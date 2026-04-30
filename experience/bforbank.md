---
id: experience-bforbank
title: BforBank - Lead UX Writer & Visual
type: experience
domain: experience
tags: [bforbank, banking, ai, rag, langgraph, gemini, content-design, management, agile, compliance]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2024-05 / 2025-12
employer: BforBank (filiale Credit Agricole)
location: Paris, France
industry: Banque en ligne / Fintech
links:
  - projects/la-plume-bforbank.md
  - stack.md
  - expertise.md
---

# BforBank - Lead UX Writer & Visual

| Cle | Valeur |
|-----|--------|
| **Periode** | Mai 2024 - Decembre 2025 (1 an 7 mois) |
| **Localisation** | Paris, France |
| **Entreprise** | BforBank (filiale Credit Agricole) |
| **Industrie** | Banque en ligne |
| **Role** | Lead UX Writer & Visual |

## Mission

Refonte en profondeur des contenus, FAQ, documentation et IA appliquee chez BforBank. Approche globale pour remettre de la coherence partout, et simplifier a la fois l'usage et la production.

C'est sur cette mission que j'ai commence a developper mes propres outils IA, passant progressivement du role de Lead UX Writer a celui de builder.

## Management

Management direct d'une equipe de 3 personnes : 2 designers + 1 alternante.

## Pilotage

Pilotage en agile (sprints, rituels) en environnement bancaire fortement processe :

- PM (Product Manager)
- Tribe Leader (responsable de tribu agile)
- Equipes Marketing
- Service Relation Client (SRC)
- Direction
- Validations Compliance et Conformite

## Chantier 1 - « La Plume » : assistant IA interne pour les designers

Architecture RAG complete sur Gemini 2.5 Pro avec orchestration LangGraph. Embeddings text-multilingual-embedding-002 (FR/EN), SemanticSplitter custom, indexation sur charte editoriale et guidelines.

Workflow d'agent : router → summarizer → RAG → generation → tool calling → generation d'image. Garde-fous editoriaux pour bloquer les formulations interdites par la conformite bancaire.

Deployee dans la marketplace BforBank GPT, utilisee par les equipes design.

Detail complet : [projects/la-plume-bforbank.md](../projects/la-plume-bforbank.md).

## Chantier 2 - Lancement du chat service client (clients in-app)

Direction de la methodologie data : couplage de 3 sources internes (FAQ publiques, tickets service client, retours SRC) en un corpus unifie. Production de 250+ articles LLM-ready (titre, intent, reponse autoportante, formulations alternatives, exclusions explicites pour eviter les hallucinations sur sujets regules). Construction d'un bot RAG GPT custom comme outil de production editoriale interne pour tenir le rythme.

Detail complet : [projects/la-plume-bforbank.md](../projects/la-plume-bforbank.md).

## Chantier 3 - Plugin Figma proprietaire

Developpement du plugin Figma d'audit UX writing devenu projet fondateur de Microphage. Premier prototype d'analyse de maquettes par IA (vision + metadonnees Figma).

Detail : [projects/microphage-analyzer-pro.md](../projects/microphage-analyzer-pro.md).

## Chantier 4 - Refonte editoriale globale

Audit complet des interfaces mobile et desktop (incoherences, doublons, messages flous ou absents). Reecriture des contenus problematiques et creation de tous les micro-contenus des nouveaux parcours, en binome avec les designers.

FAQ augmentee : redaction de centaines d'articles au format conversationnel (chatbot) et classique (SEO, support).

Refonte de parcours encadres par des obligations legales strictes (assurance vie). Integration des contenus dans Lokalise pour la coherence multilingue.

Animation d'ateliers de formation a l'UX writing et aux usages IA.

## Competences mobilisees

- Management d'equipe en environnement bancaire regule
- Pilotage de projet en agile multi-stakeholders
- Architecture RAG et orchestration d'agents IA
- Methodologie data pour LLM (corpus structures)
- Direction editoriale en cadre Compliance
- Animation et formation

## Related

- [projects/la-plume-bforbank.md](../projects/la-plume-bforbank.md)
- [projects/microphage-analyzer-pro.md](../projects/microphage-analyzer-pro.md)
- [stack.md](../stack.md)
- [expertise.md](../expertise.md)
- [narrative.md](../narrative.md)
