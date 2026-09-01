---
id: project-mulotte
title: Mulotte Club - E-commerce for one-of-a-kind secondhand pieces
type: project
category: site
domain: project
tags: [microphage, mulotte, e-commerce, stripe, supabase, club, secondhand]
status: live
created: 2026-09-01
updated: 2026-09-01
period: 2026 / present
client: Mulotte
industries: [Fashion, Secondhand, E-commerce]
technologies: [Next.js 15, Supabase, Stripe, Resend]
team: 1 (Romain Bigache, solo)
url: https://mulotte.club
demo: https://mulotte.club
links:
  - experience/microphage.md
  - projects/fusil-paris.md
---

# Mulotte Club

| Key | Value |
|-----|-------|
| **Type** | E-commerce site for a curated secondhand shop |
| **Status** | In production at [mulotte.club](https://mulotte.club) |
| **Company** | Microphage (SASU) |
| **Team** | Romain Bigache (solo) |

## Short description

Online shop for Mulotte, a curated secondhand brand selling one-of-a-kind pieces. The whole catalog logic differs from classic e-commerce: every item is unique, so the product model, stock handling and checkout are built around single-unit scarcity.

The signature feature is the Club: members get early access to new drops before the public. Items can be reserved for 24 hours against a Stripe deposit, which handles the "unique piece, several interested buyers" problem without cart racing.

## Key features

- Unique-piece catalog (single-unit stock, no variants)
- Club membership with early access to drops
- 24-hour reservation with Stripe deposit
- Transactional emails via Resend
- Custom domain email routing for the brand

## Stack

Next.js 15, Supabase (catalog, members, reservations), Stripe (deposits and payments), Resend (transactional email), deployed on mulotte.club.

## Related

- [experience/microphage.md](../experience/microphage.md)
- [fusil-paris.md](./fusil-paris.md)
