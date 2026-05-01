---
id: project-cloud-academy-coach
title: Cloud Academy Coach - POC technique sur Gemini Enterprise
type: project
domain: project
tags: [microphage, gcp, vertex-ai-search, gemini, cloud-run, agent-builder, rag, function-calling, poc, energy-utility]
status: live
created: 2026-05-01
updated: 2026-05-01
period: 2026-05
client: Démo technique (POC interne, contexte fictif acteur énergie)
industries: [Énergie, Utilities, Formation interne]
team: 1 (Romain Bigache, solo)
url: https://cloud-academy-ui-90119460065.europe-west1.run.app
demo: https://cloud-academy-ui-90119460065.europe-west1.run.app
technologies: [Gemini 2.5 Pro, Vertex AI Search, Cloud Run, Next.js 15, TypeScript, React 19, Tailwind 4, GoogleGenAI SDK, Docker, Cloud Build]
duration: 1 nuit (mai 2026)
links:
  - experience/microphage.md
  - expertise.md
  - stack.md
---

# Cloud Academy Coach

| Clé | Valeur |
|-----|--------|
| **Type** | POC technique solo sur stack GCP cible |
| **Statut** | Live, public |
| **Date** | Mai 2026 |
| **Société** | Microphage (SASU) |
| **Industrie cible** | Énergie / Utilities (acteur transition énergétique) |
| **Équipe** | Romain Bigache (solo) |
| **Durée de build** | 1 nuit |

## Pitch court

POC technique livré en une nuit pour démontrer la maîtrise de Gemini Enterprise Agent Platform (Vertex AI Agent Builder + Vertex AI Search + Cloud Run). Une academy interne d'un acteur énergie fictif, où un agent IA orchestrateur génère un parcours adaptatif et coache l'apprenant en RAG conversationnel sur 16 modules indexés.

## Genèse

Construit en mai 2026 pour répondre à une opportunité freelance Theodo (Lead GenAI GCP, mission contexte transition énergétique). Plutôt que de prétendre à 6 ans de prod GCP que je n'ai pas, j'ai préféré livrer en une nuit une démo cliquable sur la stack exacte de la mission, puis assumer la transparence : "pas en production sur GCP, mais voici ce que je sais en faire en quelques heures".

Le POC s'inspire d'un pattern réel observé chez plusieurs acteurs énergie : academy interne avec une matrice rôles × modules × niveaux qui devient ingérable à mesure que l'effectif et le catalogue grossissent. La promesse : remplacer cette matrice statique par un agent IA qui personnalise le parcours en live.

## Description courte

Webapp Next.js 15 sur Cloud Run europe-west1. Onboarding 8 questions, agent orchestrateur Gemini 2.5 Pro avec 5 tools, datastore Vertex AI Search avec 16 modules pédagogiques indexés, parcours adaptatif gamifié, drawer Coach RAG side-panel, lesson player Duolingo-style.

## Description longue

### Le problème adressé

Dans une grande organisation énergie, le service formation tient à jour une matrice Excel : 15 rôles métier × 16 modules cloud × 3 niveaux de maîtrise. Trois personnes administrent cette matrice, l'enrichissent, l'aiguillent. Mais les collaborateurs ne suivent pas leur parcours assigné : les modules n'arrivent pas dans le bon ordre, les prérequis sont opaques, les exemples restent génériques au lieu d'être contextualisés sur le métier (Smart Grid, Linky, énergies renouvelables).

### La solution livrée

Cinq composants coordonnés :

1. **Onboarding interactif** : 8 questions guidées (prénom, entité, rôle, niveau, modules déjà complétés, priorité 6 mois) qui collectent un profil collaborateur structuré.

2. **Agent orchestrateur Gemini 2.5 Pro** : function calling sur 5 tools custom (`get_role_matrix`, `search_modules`, `check_prerequisites`, `assign_modules`, `book_calendar`). L'agent diagnostique le profil, recherche les modules pertinents, vérifie les prérequis, assigne le parcours et réserve une session pour le premier module. Tous ses tool calls sont visibles en live dans l'UI (asset pitch tech).

3. **Datastore Vertex AI Search** : 16 modules pédagogiques riches (~3000 mots chacun, format HTML), ingérés dans le datastore `cloud-academy-modules`. Disponibles pour le RAG conversationnel avec grounding automatique.

4. **Parcours hub adaptatif** : tableau de bord personnalisé avec les modules recommandés par l'agent, leur statut (à faire / en cours / complété / verrouillé par prérequis), métriques XP, progression globale.

5. **Lesson player Duolingo-style** : intro / sections markdown / quiz / cas pratique / bilan XP. Boutons "Approfondir avec Coach" contextuels qui ouvrent un drawer RAG avec le contexte de la slide.

6. **Drawer Coach RAG** : side-panel persistent 33vw avec chat conversationnel. Streaming NDJSON, sources Vertex Search citées en pills cliquables (« 📚 M16 Disaster Recovery »), contexte profil maintenu entre sessions.

### Architecture technique

```
┌─────────────────────┐
│ Frontend Next.js 15 │ ← Cloud Run europe-west1
│ Tailwind 4 + RSC    │   2 vCPU, 2 Gi, min-instances=1
└──────────┬──────────┘
           │ NDJSON stream
┌──────────▼──────────┐
│ /api/agent          │ ← orchestrateur (5 tools)
│ /api/chat           │ ← RAG conversationnel
└──────────┬──────────┘
           │ @google/genai SDK
┌──────────▼──────────────────────────────┐
│ Vertex AI / Gemini 2.5 Pro (location=global) │
│  ├─ Function calling (5 tools)          │
│  └─ Tool retrieval VertexAISearch       │
│       ↓                                 │
│  Datastore cloud-academy-modules        │
│  16 documents HTML indexés              │
└─────────────────────────────────────────┘
```

Auth via Application Default Credentials du service account Cloud Run (rôles `aiplatform.user` + `discoveryengine.viewer`). Aucune SA key fichier (org policy bloque la création).

### Stack tech

- **Front** : Next.js 15 + React 19 + TypeScript + Tailwind 4 + Open Sans + shadcn-style components custom
- **Streaming** : NDJSON via ReadableStream + watchdog 45s côté client
- **Backend** : routes Next.js API (Node runtime, maxDuration 60s)
- **AI** : @google/genai SDK avec mode `vertexai: true` (Application Default Credentials)
- **Datastore** : Vertex AI Search (`cloud-academy-modules_1777599701196`), 16 docs HTML
- **Deploy** : Dockerfile multi-stage Node 20 Alpine, Cloud Build, Artifact Registry
- **Region** : europe-west1 (proche client énergie)

## Captures

### 1. Onboarding

![Onboarding intro](./screenshots/cloud-academy-coach/01-onboarding-intro.png)

Pattern Altaria-like : titre WordReveal mot par mot avec accent souligné, mascotte Breath bleu Enedis #1423DC, bouton primary 3D Duolingo-style avec ombre dure rétractable au click. Signature stack en mono fixed-bottom (« powered by Gemini Enterprise Agent Platform / Microphage Intelligence »).

### 2. Parcours hub

![Parcours hub](./screenshots/cloud-academy-coach/02-parcours-hub.png)

6 modules personnalisés affichés en cards avec gradient pillar (Plateforme / Process Outils / SRE), métriques XP, progression globale. Chaque card a un état (en cours / complété / verrouillé par prérequis) que l'agent a calculé. Le parcours s'adapte aux modules déjà complétés du profil.

### 3. Lesson player

![Lesson player](./screenshots/cloud-academy-coach/03-lesson-player.png)

Pattern Duolingo : intro de module avec pill ID + niveau + durée, objectifs en bullets bleu Enedis, bouton primary pour démarrer. Slides séquentielles ensuite : sections markdown / quiz / cas pratique / bilan XP gagné.

### 4. Drawer Coach (état initial)

![Coach drawer empty](./screenshots/cloud-academy-coach/04-coach-drawer-empty.png)

Side-panel 33vw fixed-right, animation slide-in 350ms cubic-bezier soft. Pas de backdrop sur desktop (le contenu lesson reste actionnable à gauche). 4 quick replies premium avec icônes Lucide (no emoji) en bas du panel.

### 5. Drawer Coach avec grounding RAG

![Coach drawer RAG](./screenshots/cloud-academy-coach/05-coach-drawer-rag.png)

Question utilisateur : « Comment fonctionne un VPC partagé ? ». L'agent Gemini répond en streaming, contextualise la réponse pour Yassine (Cloud Security Engineer) avec exemples métier énergie (Smart Grid, compteurs Linky), et cite explicitement les modules M03 Networking Cloud Avancé et M11 Sécurité Cloud comme sources. Les sources apparaissent en pills cliquables qui routent vers `/modules/MXX`.

## Difficultés rencontrées

### 1. Org policy GCP qui bloque l'accès public

Le projet GCP est sous une org `fusil.paris` qui force `iam.allowedPolicyMemberDomains` (impossible d'ajouter `allUsers` à un service Cloud Run). Premier deploy : URL renvoie `403 Forbidden`.

Fix : créer un override de cette org policy au niveau projet. Pour ça, il a fallu se grant `roles/orgpolicy.policyAdmin` au niveau organisation (rôle qui n'est pas dans `Administrateur de l'organisation` par défaut). Une fois fait, override appliqué + binding `allUsers : roles/run.invoker` autorisé après ~3 minutes de propagation.

### 2. SA keys interdites par org policy

`iam.disableServiceAccountKeyCreation` empêche de générer une clé SA pour auth locale ou Vercel. Pivot vers Cloud Run + ADC du SA par défaut.

### 3. Build Cloud Run silencieux

Premier build via `gcloud run deploy --source` : log vide, échec sans diagnostic. Fix : passer en `gcloud builds submit --tag` séparément du deploy, qui stream les logs en direct dans le terminal.

### 4. Latence RAG cold start

Sur la 2ème question dans le drawer Coach, l'API mettait > 30s à répondre. Trois fixes :
- `--min-instances=1` pour éliminer le cold start Cloud Run
- `GOOGLE_CLOUD_LOCATION=global` au lieu de `us-central1` pour réduire la latence transatlantique
- `--memory=2Gi --cpu=2` pour plus de CPU alloué
- Watchdog 45s côté frontend avec message friendly si pas de chunk reçu

### 5. Markdown rejeté par Vertex AI Search

L'ingestion datastore refusait les fichiers `.md` (`INVALID_FORMAT content_mimeType`). Conversion automatique en HTML via un script dédié, ré-upload, ré-indexation.

## Ce que ça démontre

- **Agent orchestrateur Gemini avec function calling production-grade** (5 tools, gestion des prerequis, history multi-turn, system prompt riche, function declarations strictement typées)
- **RAG conversationnel sur Vertex AI Search** avec grounding automatique et citation des sources
- **Streaming NDJSON propre** end-to-end (Cloud Run → Next.js stream → React state)
- **Stack 100% GCP** : Vertex AI, Cloud Run, Cloud Build, Artifact Registry, Vertex AI Search, IAM, Org Policy
- **Capacité de delivery solo** : 16 modules pédagogiques riches générés par sub-agents en parallèle, agent + UI livrés en une nuit, pitch comex 1-pager exporté en PDF, déploiement public résistant aux org policies restrictives
- **Design system Altaria-like cohérent** : pas d'emoji, icônes Lucide stroke 2.2, accent bleu Enedis #1423DC parcimonieux, ombres soft, animations cubic-bezier 200-350ms

## Limitations assumées

- Pas de DB serveur : profil et parcours stockés en `localStorage` côté client (POC choice). En prod chez le client, on remplace par Firestore ou Cloud SQL.
- Pas de tests automatisés : POC d'1 nuit, pas de CI. Sur Microphage Analyzer Pro (en prod) j'ai 102 tests Vitest + Playwright.
- Pas d'auth applicative au-dessus de `--allow-unauthenticated` : démo publique. En prod : IAP + IAM + sessions Firestore.
- 16 modules synthétiques générés par LLM. En prod : ingestion du vrai catalogue formation client.

## Liens

- **Démo live** : [https://cloud-academy-ui-90119460065.europe-west1.run.app](https://cloud-academy-ui-90119460065.europe-west1.run.app)
- **1-pager comex (PDF)** : sur demande (pack candidature Theodo)
- **Code source** : sur demande (dossier candidature, repo privé)

## Related

- [microphage](../experience/microphage.md)
- [expertise](../expertise.md)
- [stack](../stack.md)
- [methodology](../methodology.md)
