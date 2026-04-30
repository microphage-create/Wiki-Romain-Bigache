---
id: project-la-plume-bforbank
title: La Plume + customer service chat (BforBank)
type: project
domain: project
tags: [bforbank, banking, gemini-2.5-pro, langgraph, rag, semantic-splitter, multilingual-embeddings, marketplace, customer-chat, salesforce-pattern, zendesk-pattern]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2023-12 / 2025-12
client: BforBank (Credit Agricole subsidiary)
industries: [Banking, Fintech, Financial Services]
team: 1 (Romain Bigache, freelance Lead Content Designer)
url: null
demo: null
technologies: [Gemini 2.5 Pro, text-multilingual-embedding-002, LangGraph, SemanticSplitter, GPT-4, RAG, BforBank GPT marketplace]
links:
  - experience/bforbank.md
  - stack.md
  - expertise.md
---

# La Plume + customer service chat (BforBank)

| Key | Value |
|-----|-------|
| **Type** | Internal AI assistant + LLM-ready corpus for customer service chat |
| **Status** | In production |
| **Year** | 2023 - 2025 |
| **Company** | BforBank (Credit Agricole subsidiary) |
| **Industries** | Banking, Fintech, Financial Services |
| **Size** | Large enterprise |
| **Period** | December 2023 - December 2025 |

## Short title

Two AI workstreams in banking at BforBank.

## Short description

Two distinct AI workstreams delivered during the Lead Content Designer engagement at BforBank.

**"La Plume"**: internal AI assistant for designers, on Gemini 2.5 Pro with LangGraph orchestration, deployed in the BforBank GPT marketplace.

**Customer service chat launch**: coupling of 3 heterogeneous internal sources (public FAQs, tickets, customer service feedback) and production of 250+ LLM-ready articles via a custom RAG GPT bot.

## Long description

### Workstream 1 - La Plume, internal AI assistant for designers

#### Problem

BforBank's design teams had to produce content consistent with the brand voice in a regulated banking environment, where every screen (account opening flows, life insurance, loan simulators, FAQs, transactional emails) must comply with both editorial guidelines and a high legal bar. Designers spent significant time on copy back-and-forths, with no dedicated UX writing assistant.

#### Solution

"La Plume" is deployed in the BforBank GPT marketplace, an internal platform where employees publish and use specialized assistants. La Plume is positioned across the Design, Marketing and Product categories.

#### RAG architecture (built by me)

- text-multilingual-embedding-002 embeddings to handle FR / EN documents
- SemanticSplitter with custom chunking parameters (buffer size, breakpoint percentile threshold, chunks per doc, min length, separation regex)
- Indexing on editorial guidelines, internal UX writing guidelines, reference documentation

#### Prompts and guardrails

Wrote the main system prompt, the prompts for each mode, and the editorial guardrails to block formulations forbidden by banking compliance. Calibrated generation parameters (creativity, length).

#### Agent workflow (LangGraph)

Router that picks the mode adapted to the request -> summarizer for long inputs -> RAG module to fetch references -> direct generation via the model -> tool calling for structured actions -> image generation for supporting visuals.

Runs on Gemini 2.5 Pro.

#### Use cases covered for designers

- Microcopy generation and rewriting
- Editorial guideline consistency checks
- Multiple proposals on the same message
- Translations
- Simplification of legal phrasing
- Illustration generation on UX concepts

### Workstream 2 - Customer service chat launch (in-app clients)

#### Problem

BforBank was preparing the launch of an AI chat dedicated to its connected clients in the mobile app. For a branchless online bank, chat is a critical channel: it must answer fast, accurately, and within a regulated frame (financial information, sensitive topics like fraud, account closure, banking rights, life insurance, taxation).

To run with an LLM, the chat needed a unified, homogeneous knowledge base usable at inference time, while internal sources were fragmented across public FAQs, customer service tickets, internal feedback and internal guidelines.

#### Mission

Structure all the documentation needed to power the chat:

- Scraping and retrieval of existing FAQs (public site, help base, in-app flows)
- Retrieval and cleaning of customer service feedback + internal feedback (the real user questions and the real validated human answers)
- Coupling the 3 heterogeneous sources to identify under-covered topics, redundancies, contradictions and editorial blind spots
- Full normalization: tone, structure, level of detail, granularity, phrasing, legal compliance, BforBank guideline alignment
- Rewriting and production of 250+ LLM-ready articles (clear title, identifiable intent, self-contained answer, context, alternative phrasings, explicit exclusions to avoid hallucinations on regulated topics)

#### Editorial production tool

Built a custom RAG GPT bot that ingested the 3 coupled sources and produced pre-drafted articles in the target format, then validated and finalized by hand. Internal tool, not a deliverable. It enabled the shift from heterogeneous raw material to a coherent corpus usable by the chat, at a pace far above pure manual production.

## Technologies used

### La Plume

- Gemini 2.5 Pro (main LLM)
- text-multilingual-embedding-002 (Google multilingual embeddings)
- LangGraph (agent workflow orchestration: router, summarize, RAG, tools, generate_image, tools_calling)
- SemanticSplitter (semantic RAG chunking, custom parameters)
- Tool calling and image generation
- BforBank GPT internal platform (specialized assistant marketplace)

### Customer service chat launch

- Scraping of existing FAQ sources (public FAQs, help base, in-app flows)
- Coupling with customer service tickets and internal feedback
- Custom RAG GPT bot for editorial production (internal tool)
- Production of 250+ LLM-ready articles (target structure: title, intent, self-contained answer, alternative phrasings, explicit exclusions)
- Editorial normalization against BforBank guidelines

## Impact

- La Plume in production in the BforBank GPT internal marketplace, used by design teams
- 250+ LLM-ready articles produced to power the in-app customer service chat
- Documentation and editorial material structured for the chat launch
- Coupling of 3 heterogeneous internal sources (FAQs, tickets, internal feedback) into a coherent corpus
- **Pattern "ingest heterogeneous internal sources, normalize, produce an LLM-ready corpus, power an agent" directly transferable to Salesforce or Zendesk connectors**
- **Confirmed adoption**: La Plume used daily by BforBank design teams after rollout, integrated into the customer journey production workflow. 250+ article corpus deployed in production, powering the in-app chat for connected clients.

## Related

- [experience/bforbank.md](../experience/bforbank.md)
- [stack.md](../stack.md)
- [expertise.md](../expertise.md)
