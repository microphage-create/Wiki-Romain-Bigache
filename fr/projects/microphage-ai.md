---
id: project-microphage-ai
title: microphage.ai - Concierge d'accès confidentiel
type: project
category: site
domain: project
tags: [microphage, concierge, nda, supabase-auth, serverless, access-control]
status: live
created: 2026-09-01
updated: 2026-09-01
period: 2026 / present
client: Microphage (SASU)
industries: [SaaS, Legal Tech]
technologies: [Site statique, Fonctions serverless, Supabase Auth, Resend]
team: 1 (Romain Bigache, seul)
url: https://microphage.ai
demo: null
links:
  - experience/microphage.md
---

# microphage.ai

| Clé | Valeur |
|-----|--------|
| **Type** | Concierge d'accès : hub relecteurs, signature de NDA en ligne, espaces documentaires confidentiels |
| **Statut** | En production sur microphage.ai |
| **Entreprise** | Microphage (SASU) |
| **Équipe** | Romain Bigache (seul) |

## Description courte

microphage.ai est le « concierge » de l'écosystème Microphage : le point d'entrée unique par lequel prospects, relecteurs et partenaires accèdent aux contenus confidentiels. Plutôt que d'envoyer des decks par email en espérant la discrétion, l'accès passe par un flux contrôlé : signature du NDA en ligne, réception des identifiants par email, entrée dans un espace documentaire délimité.

## Features clés

- **Signature de NDA en ligne** : le NDA se lit et se signe dans le navigateur, signatures stockées avec le droit d'accès
- **Espaces documentaires délimités** : chaque audience ne voit que le dossier qui lui est ouvert (dossier produit, wiki du cas démo, galerie)
- **Envoi des identifiants par email** (Resend) une fois l'accès accordé
- **Auth sur une instance Supabase dédiée** : profils, droits d'accès par document, signatures NDA, claims custom du token d'accès

## Stack

Site statique plus fonctions serverless, projet Supabase dédié pour l'auth et le contrôle d'accès, Resend pour l'email transactionnel. Déploiement par Git push uniquement.

## Related

- [experience/microphage.md](../experience/microphage.md)
