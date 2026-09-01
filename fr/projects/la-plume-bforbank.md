---
id: project-la-plume-bforbank
title: La Plume + chat service client (BforBank)
type: project
category: tool
domain: project
tags: [bforbank, banking, gemini-2.5-pro, langgraph, rag, semantic-splitter, multilingual-embeddings, marketplace, chat-client, salesforce-pattern, zendesk-pattern]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2023-12 / 2025-12
client: BforBank (filiale Credit Agricole)
industries: [Banque, Fintech, Services Financiers]
team: 1 (Romain Bigache, Lead Content Designer freelance)
url: null
demo: null
technologies: [Gemini 2.5 Pro, text-multilingual-embedding-002, LangGraph, SemanticSplitter, GPT-4, RAG, BforBank GPT marketplace]
links:
  - experience/bforbank.md
  - stack.md
  - expertise.md
---

# La Plume + chat service client (BforBank)

| Cle | Valeur |
|-----|--------|
| **Type** | Assistant IA interne + corpus LLM-ready pour chat service client |
| **Statut** | En production |
| **Année** | 2023 - 2025 |
| **Entreprise** | BforBank (filiale Crédit Agricole) |
| **Industries** | Banque, Fintech, Services Financiers |
| **Taille** | Grande entreprise |
| **Période** | Décembre 2023 - Décembre 2025 |

## Titre court

Deux chantiers IA en banque chez BforBank.

## Description courte

Deux chantiers IA distincts livrés pendant la mission Lead Content Designer chez BforBank.

**« La Plume »** : assistant IA interne pour les designers, sur Gemini 2.5 Pro avec orchestration LangGraph, déployé dans la marketplace BforBank GPT.

**Lancement du chat service client** : couplage de 3 sources internes hétérogènes (FAQ publiques, tickets, retours SRC) et production de 250+ articles LLM-ready via un bot RAG GPT custom.

## Description longue

### Chantier 1 - La Plume, assistant IA interne pour designers

#### Problème

Les équipes design de BforBank devaient produire du contenu cohérent avec le ton de la marque, dans un environnement bancaire régulé où chaque écran (parcours d'ouverture de compte, assurance vie, simulateurs de crédit, FAQ, mails transactionnels) doit respecter à la fois la charte éditoriale et un niveau d'exigence légale élevé. Les designers passaient un temps important en allers-retours sur la copy, sans assistant dédié à l'UX writing.

#### Solution

« La Plume » est déployée dans la marketplace BforBank GPT, plateforme interne où les collaborateurs publient et consomment des assistants spécialisés. La Plume est positionnée sur les catégories Design, Marketing et Product.

#### Architecture RAG (que j'ai montée)

- Embeddings text-multilingual-embedding-002 pour gérer documents FR / EN
- SemanticSplitter avec paramètres de chunking sur mesure (taille de buffer, seuil de breakpoint percentile, nombre de chunks par doc, longueur min, regex de séparation)
- Indexation sur charte éditoriale, guidelines UX writing internes, doc de référence

#### Prompts et garde-fous

Rédaction du system prompt principal, des prompts de chaque mode, et des garde-fous éditoriaux pour bloquer les formulations interdites par la conformité bancaire. Calibration des paramètres de génération (créativité, longueur).

#### Workflow d'agent (LangGraph)

Router qui choisit le mode adapté à la requête → summarizer pour les longues entrées → module RAG pour aller chercher les références → génération directe via le modèle → tool calling pour les actions structurées → génération d'image pour visuels d'accompagnement.

Tourne sur Gemini 2.5 Pro.

#### Cas d'usage couverts pour les designers

- Génération et reformulation de microcopy
- Vérification de cohérence avec la charte
- Propositions multiples sur un même message
- Traductions
- Simplification d'expressions juridiques
- Génération d'illustrations sur des concepts UX

### Chantier 2 - Lancement du chat service client (clients in-app)

#### Problème

BforBank préparait le lancement d'un chat IA dédié à ses clients connectés dans l'application mobile. Pour une banque en ligne sans réseau d'agences, le chat est un canal critique : il doit répondre vite, juste, et dans un cadre régulé (informations financières, sujets sensibles type fraude, opposition, droit au compte, assurance vie, fiscalité).

Pour fonctionner avec un LLM, le chat avait besoin d'une base de connaissance unifiée, homogène et exploitable en inférence, là où les sources internes étaient fragmentées entre FAQ publiques, tickets service client, retours SRC et guidelines internes.

#### Mission

Structurer toute la documentation nécessaire au tirage du chat :

- Scraping et récupération des FAQ existantes (site public, base d'aide, parcours app)
- Récupération et nettoyage des remontées service client + SRC (les vraies questions des utilisateurs et les vraies réponses humaines validées)
- Couplage des 3 sources hétérogènes pour identifier sujets sous-traités, redondances, contradictions et zones d'ombre éditoriales
- Homogénéisation complète : ton, structure, niveau de détail, granularité, formulation, conformité légale, alignement charte BforBank
- Réécriture et production de 250+ articles LLM-ready (titre clair, intent identifiable, réponse autoportante, contexte, formulations alternatives, exclusions explicites pour éviter les hallucinations sur les sujets régulés)

#### Outil de production éditoriale

Construction d'un bot RAG GPT custom qui ingérait les 3 sources couplées et produisait des articles pré-rédigés au format attendu, validés et finalisés ensuite à la main. Outil interne, pas un livrable. Il a permis de passer de la matière brute hétérogène à un corpus cohérent et exploitable par le chat, à un rythme bien supérieur à la production manuelle pure.

## Technologies utilisees

### La Plume

- Gemini 2.5 Pro (modèle LLM principal)
- text-multilingual-embedding-002 (embeddings Google multilingues)
- LangGraph (orchestration workflow d'agent : router, summarize, RAG, tools, generate_image, tools_calling)
- SemanticSplitter (chunking sémantique du RAG, paramètres sur mesure)
- Tool calling et génération d'image
- Plateforme interne BforBank GPT (marketplace d'assistants spécialisés)

### Lancement du chat service client

- Scraping des sources FAQ existantes (FAQ publiques, base d'aide, parcours app)
- Couplage avec tickets service client et retours SRC
- Bot RAG GPT custom pour la production éditoriale (outil interne)
- Production de 250+ articles LLM-ready (structure cible : titre, intent, réponse autoportante, formulations alternatives, exclusions explicites)
- Homogénéisation éditoriale selon la charte BforBank

## Impact

- La Plume en production dans la marketplace interne BforBank GPT, utilisée par les équipes design
- 250+ articles LLM-ready produits pour alimenter le chat service client des clients in-app
- Documentation et matière éditoriale structurées pour le lancement du chat
- Couplage de 3 sources internes hétérogènes (FAQ, tickets, retours SRC) en un corpus cohérent
- **Pattern « ingérer des sources internes hétérogènes, homogénéiser, produire un corpus LLM-ready, alimenter un agent » directement transposable sur des connecteurs Salesforce ou Zendesk**
- **Adoption confirmée** : La Plume utilisée quotidiennement par les équipes design BforBank après déploiement, intégrée au workflow de production des parcours clients. Corpus de 250+ articles déployé en production, alimente le chat in-app des clients connectés.

## Related

- [experience/bforbank.md](../experience/bforbank.md)
- [stack.md](../stack.md)
- [expertise.md](../expertise.md)
