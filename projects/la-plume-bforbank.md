---
id: project-la-plume-bforbank
title: La Plume + chat service client (BforBank)
type: project
domain: project
tags: [bforbank, banking, gemini-2.5-pro, langgraph, rag, semantic-splitter, multilingual-embeddings, marketplace, chat-client, salesforce-pattern, zendesk-pattern]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2024-12 / 2025-12
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
| **Annee** | 2024 - 2025 |
| **Entreprise** | BforBank (filiale Credit Agricole) |
| **Industries** | Banque, Fintech, Services Financiers |
| **Taille** | Grande entreprise |
| **Date** | Decembre 2023 - Decembre 2025 |

## Titre court

Deux chantiers IA en banque chez BforBank.

## Description courte

Deux chantiers IA distincts livres pendant la mission Lead Content Designer chez BforBank.

**« La Plume »** : assistant IA interne pour les designers, sur Gemini 2.5 Pro avec orchestration LangGraph, deploye dans la marketplace BforBank GPT.

**Lancement du chat service client** : couplage de 3 sources internes heterogenes (FAQ publiques, tickets, retours SRC) et production de 250+ articles LLM-ready via un bot RAG GPT custom.

## Description longue

### Chantier 1 - La Plume, assistant IA interne pour designers

#### Probleme

Les equipes design de BforBank devaient produire du contenu coherent avec le ton de la marque, dans un environnement bancaire regule ou chaque ecran (parcours d'ouverture de compte, assurance vie, simulateurs de credit, FAQ, mails transactionnels) doit respecter a la fois la charte editoriale et un niveau d'exigence legale eleve. Les designers passaient un temps important en allers-retours sur la copy, sans assistant dedie a l'UX writing.

#### Solution

« La Plume » est deployee dans la marketplace BforBank GPT, plateforme interne ou les collaborateurs publient et consomment des assistants specialises (a cote d'Email Booster, Pimp My Prompt, Expert charte BFB-GPT, Aide a la redaction SRC, Methode 80/20). La Plume est positionnee sur les categories Design, Marketing et Product.

#### Architecture RAG (que j'ai montee)

- Embeddings text-multilingual-embedding-002 pour gerer documents FR / EN
- SemanticSplitter avec parametres de chunking sur mesure (taille de buffer, seuil de breakpoint percentile, nombre de chunks par doc, longueur min, regex de separation)
- Indexation sur charte editoriale, guidelines UX writing internes, doc de reference

#### Prompts et garde-fous

Redaction du system prompt principal, des prompts de chaque mode, et des garde-fous editoriaux pour bloquer les formulations interdites par la conformite bancaire. Calibration des parametres de generation (creativite, longueur).

#### Workflow d'agent (LangGraph)

Router qui choisit le mode adapte a la requete → summarizer pour les longues entrees → module RAG pour aller chercher les references → generation directe via le modele → tool calling pour les actions structurees → generation d'image pour visuels d'accompagnement.

Tourne sur Gemini 2.5 Pro.

#### Cas d'usage couverts pour les designers

- Generation et reformulation de microcopy
- Verification de coherence avec la charte
- Propositions multiples sur un meme message
- Traductions
- Simplification d'expressions juridiques
- Generation d'illustrations sur des concepts UX

### Chantier 2 - Lancement du chat service client (clients in-app)

#### Probleme

BforBank preparait le lancement d'un chat IA dedie a ses clients connectes dans l'application mobile. Pour une banque en ligne sans reseau d'agences, le chat est un canal critique : il doit repondre vite, juste, et dans un cadre regule (informations financieres, sujets sensibles type fraude, opposition, droit au compte, assurance vie, fiscalite).

Pour fonctionner avec un LLM, le chat avait besoin d'une base de connaissance unifiee, homogene et exploitable en inference, la ou les sources internes etaient fragmentees entre FAQ publiques, tickets service client, retours SRC et guidelines internes.

#### Mission

Structurer toute la documentation necessaire au tirage du chat :

- Scraping et recuperation des FAQ existantes (site public, base d'aide, parcours app)
- Recuperation et nettoyage des remontees service client + SRC (les vraies questions des utilisateurs et les vraies reponses humaines validees)
- Couplage des 3 sources heterogenes pour identifier sujets sous-traites, redondances, contradictions et zones d'ombre editoriales
- Homogeneisation complete : ton, structure, niveau de detail, granularite, formulation, conformite legale, alignement charte BforBank
- Reecriture et production de 250+ articles LLM-ready (titre clair, intent identifiable, reponse autoportante, contexte, formulations alternatives, exclusions explicites pour eviter les hallucinations sur les sujets regules)

#### Outil de production editoriale

Construction d'un bot RAG GPT custom qui ingerait les 3 sources couplees et produisait des articles pre-rediges au format attendu, valides et finalises ensuite a la main. Outil interne, pas un livrable. Il a permis de passer de la matiere brute heterogene a un corpus coherent et exploitable par le chat, a un rythme bien superieur a la production manuelle pure.

## Technologies utilisees

### La Plume

- Gemini 2.5 Pro (modele LLM principal)
- text-multilingual-embedding-002 (embeddings Google multilingues)
- LangGraph (orchestration workflow d'agent : router, summarize, RAG, tools, generate_image, tools_calling)
- SemanticSplitter (chunking semantique du RAG, parametres sur mesure)
- Tool calling et generation d'image
- Plateforme interne BforBank GPT (marketplace d'assistants specialises)

### Lancement du chat service client

- Scraping des sources FAQ existantes (FAQ publiques, base d'aide, parcours app)
- Couplage avec tickets service client et retours SRC
- Bot RAG GPT custom pour la production editoriale (outil interne)
- Production de 250+ articles LLM-ready (structure cible : titre, intent, reponse autoportante, formulations alternatives, exclusions explicites)
- Homogeneisation editoriale selon la charte BforBank

## Impact

- La Plume en production dans la marketplace interne BforBank GPT, utilisee par les equipes design
- 250+ articles LLM-ready produits pour alimenter le chat service client des clients in-app
- Documentation et matiere editoriale structurees pour le lancement du chat
- Couplage de 3 sources internes heterogenes (FAQ, tickets, retours SRC) en un corpus coherent
- **Pattern « ingerer des sources internes heterogenes, homogeneiser, produire un corpus LLM-ready, alimenter un agent » directement transposable sur des connecteurs Salesforce ou Zendesk**

## Avis client

Disponibles sur demande.

## Related

- [experience/bforbank.md](../experience/bforbank.md)
- [stack.md](../stack.md)
- [expertise.md](../expertise.md)
- [narrative.md](../narrative.md)
