---
id: project-microphage-ai
title: microphage.ai - Confidential access concierge
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
technologies: [Static site, Serverless functions, Supabase Auth, Resend]
team: 1 (Romain Bigache, solo)
url: https://microphage.ai
demo: null
links:
  - experience/microphage.md
---

# microphage.ai

| Key | Value |
|-----|-------|
| **Type** | Access concierge: reviewer hub, online NDA signature, confidential document spaces |
| **Status** | In production at microphage.ai |
| **Company** | Microphage (SASU) |
| **Team** | Romain Bigache (solo) |

## Short description

microphage.ai is the "concierge" of the Microphage ecosystem: the single entry point where prospects, reviewers and partners access confidential material. Instead of emailing decks and hoping for discretion, access runs through a controlled flow: sign an NDA online, receive credentials by email, enter a scoped document space.

## Key features

- **Online NDA signature**: the NDA is read and signed in the browser, signatures stored with the access grant
- **Scoped document spaces**: each audience sees only the dossier it was granted (product dossier, demo case wiki, gallery)
- **Credential delivery by email** (Resend) once access is granted
- **Auth on a dedicated Supabase instance**: profiles, per-document access rights, NDA signatures, custom access-token claims

## Stack

Static site plus serverless functions, dedicated Supabase project for auth and access control, Resend for transactional email. Deployed through Git push only.

## Related

- [experience/microphage.md](../experience/microphage.md)
