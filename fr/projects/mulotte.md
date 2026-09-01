---
id: project-mulotte
title: Mulotte Club - E-commerce de pièces uniques de seconde main
type: project
category: site
domain: project
tags: [microphage, mulotte, e-commerce, stripe, supabase, club, secondhand]
status: live
created: 2026-09-01
updated: 2026-09-01
period: 2026 / present
client: Mulotte
industries: [Mode, Seconde main, E-commerce]
technologies: [Next.js 15, Supabase, Stripe, Resend]
team: 1 (Romain Bigache, seul)
url: https://mulotte.club
demo: https://mulotte.club
links:
  - experience/microphage.md
  - projects/fusil-paris.md
---

# Mulotte Club

| Clé | Valeur |
|-----|--------|
| **Type** | Site e-commerce d'une friperie curatée |
| **Statut** | En production sur [mulotte.club](https://mulotte.club) |
| **Entreprise** | Microphage (SASU) |
| **Équipe** | Romain Bigache (seul) |

## Description courte

Boutique en ligne de Mulotte, friperie curatée qui vend des pièces uniques. Toute la logique catalogue diffère de l'e-commerce classique : chaque article est unique, donc le modèle produit, la gestion du stock et le checkout sont construits autour de la rareté à exemplaire unique.

La feature signature est le Club : les membres accèdent aux nouveaux drops en avant-première. Une pièce peut être réservée 24 heures contre un acompte Stripe, ce qui règle le problème « pièce unique, plusieurs acheteurs intéressés » sans course au panier.

## Features clés

- Catalogue de pièces uniques (stock à exemplaire unique, pas de variantes)
- Adhésion Club avec accès anticipé aux drops
- Réservation 24 h avec acompte Stripe
- Emails transactionnels via Resend
- Routage email personnalisé du domaine pour la marque

## Stack

Next.js 15, Supabase (catalogue, membres, réservations), Stripe (acomptes et paiements), Resend (email transactionnel), déployé sur mulotte.club.

## Related

- [experience/microphage.md](../experience/microphage.md)
- [fusil-paris.md](./fusil-paris.md)
