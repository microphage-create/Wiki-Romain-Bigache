---
id: project-fusil-paris
title: fusil.paris - E-commerce de bijoux artisanaux
type: project
category: site
domain: project
tags: [fusil-paris, e-commerce, jewelry, next-js-16, edge-functions, deno, stripe, paypal, hmac, security, chronopost, bilingual, solo, co-founded]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2024 / present
client: fusil.paris (co-fondee avec Edouard)
industries: [E-commerce, Bijouterie, Artisanat]
team: 2 (Romain Bigache - tech/design/copy, Edouard - cofondateur, creation des bijoux)
url: https://fusil.paris
demo: https://fusil.paris
technologies: [Next.js 16, React 19, TypeScript 5, Tailwind CSS 4, Supabase, Edge Functions Deno, Stripe, PayPal, Resend, Chronopost, HMAC-SHA256, Web Crypto API, Vercel]
links:
  - experience/microphage.md
  - stack.md
---

# fusil.paris

| Cle | Valeur |
|-----|--------|
| **Type** | E-commerce de bijoux artisanaux (co-fondé) |
| **Statut** | En production |
| **Année** | 2024 - en cours |
| **URL** | [fusil.paris](https://fusil.paris) |
| **Entreprise** | fusil.paris (marque de bijoux en argent 925 faits main à Paris) |
| **Industries** | E-commerce, Bijouterie, Artisanat |
| **Équipe** | Romain Bigache (concept, design, code, sécurité, déploiement, copy, mails), Edouard (co-fondateur, création des bijoux) |

## Titre court

E-commerce de bijoux artisanaux, conçu, codé et déployé en solo.

## Description courte

Boutique e-commerce complète pour fusil.paris (bijoux en argent 925 faits main à Paris). Conçue, codée et déployée en solo de bout en bout : front Next.js 16 + React 19, paiement double provider (Stripe + PayPal), 12 Edge Functions Deno, mails transactionnels bilingues FR/EN, expédition Chronopost multi-zones, panel admin sécurisé, sécurité bancaire (HMAC-SHA256, CSP, HSTS, rate limiting, timing-safe auth).

## Description longue

### Contexte

fusil.paris est une marque de bijoux en argent 925 fabriqués artisanalement à Paris (collections Brut, Leaf, Paris, Hors Série), co-fondée avec Edouard. Le site sert à la fois de vitrine narrative et de boutique e-commerce avec un panier de 250-380 EUR, donc avec un niveau d'exigence élevé sur la confiance et la sécurité de paiement.

### Périmètre solo

Direction artistique, copy, code (front + back), intégration paiement, sécurité, mails transactionnels, panel admin, déploiement, monitoring. De bout en bout.

### Front et SEO

Next.js 16 (App Router) + React 19 + Tailwind 4 + TypeScript 5. Site bilingue FR/EN, optimisé pour le partage social et le référencement : Schema.org JSON-LD (JewelryStore), Open Graph, Twitter Cards, métadonnées PWA-friendly (theme-color, apple-mobile-web-app-capable, viewport-fit cover). Composants UI réutilisables, performance optimisée pour la conversion.

### Backend Edge Functions (Deno + Supabase)

12 fonctions Edge déployées couvrant tout le cycle de vie commande :

- Webhooks Stripe (vérification HMAC-SHA256 maison via Web Crypto API native, sans dépendance Stripe SDK)
- Confirmation côté client pour idempotence
- Authentification admin avec timing-safe comparison
- Annulation de commande avec remboursement automatique
- Récupération sécurisée d'une commande client (token-based)
- Remboursement Stripe partiel ou total
- Workflow de demande de retour
- 5 fonctions de mails transactionnels bilingues FR/EN (confirmation, expédition, livraison, prête à expédier, RDV showroom)

### Sécurité production-grade

- **Vérification HMAC-SHA256 maison des webhooks Stripe** via Web Crypto API native, sans dépendre de la lib Stripe SDK : timestamp + signature v1
- **Rate limiting in-memory** sur Vercel serverless : 60 req/min global + 5 échecs d'auth/min, avec fenêtres glissantes et nettoyage périodique
- **Timing-safe comparison** pour le token admin : protection contre les timing attacks par comparaison bit à bit
- **Whitelist de paths** dans le proxy admin (allow-list, pas deny-list) : seuls les endpoints Supabase nécessaires sont autorisés
- **Headers sécurité Vercel** : CSP avec frame-ancestors restrictif, HSTS 1 an avec includeSubDomains, X-Content-Type-Options, X-Frame-Options DENY, X-XSS-Protection, Referrer-Policy strict-origin-when-cross-origin, Permissions-Policy désactivant camera / micro / géolocalisation
- **CORS strict** sur l'admin : uniquement depuis fusil.paris et www.fusil.paris
- **Limite de taille body** sur les requêtes admin pour éviter les abus
- **Service role key Supabase** jamais exposé côté client : tout passe par un proxy Vercel

### Paiement double provider

- **Stripe Checkout Sessions** avec shipping rates par zone (FR, EU, Suisse, UK, World, pickup) et webhook idempotent
- **PayPal** intégration complète (create-order + capture-order) avec gestion des états et des erreurs
- **Codes promo** avec validation côté serveur : montant minimum, dates d'expiration, type de réduction (% ou fixe)

### Mails transactionnels bilingues FR/EN

Tous les emails clients (confirmation, expédition, livraison, RDV, retour, remboursement) supportent FR + EN avec détection automatique de la langue depuis les metadata Stripe. Templates HTML inline avec fallback texte. Envoyés via Resend.

### Multi-zones d'expédition (Chronopost)

Tarifs et délais par zone : France gratuite (2-3 jours), Europe gratuite (3-5 jours), Suisse 25 EUR, UK 25 EUR HT (taxes UK en sus), Monde 35 EUR (4-7 jours), retrait en boutique gratuit. Affichage automatique du transporteur côté client. Saisie du numéro de suivi côté admin, génération automatique du lien de tracking direct vers chronopost.fr dans l'email d'expédition envoyé au client.

### Panel admin sécurisé

Gestion complète des produits, commandes, codes promo, settings, lookbook et logs applicatifs. Authentification par token protégé en variable d'environnement, rate limiting sur les échecs d'auth, comparaison timing-safe (anti timing-attack), whitelist de paths sur le proxy Vercel.

### Monitoring

Vercel Insights pour la performance, Supabase pour le tracing applicatif, logs Stripe + PayPal centralisés.

## Technologies utilisees

### Front

- Next.js 16 (App Router)
- React 19
- TypeScript 5
- Tailwind CSS 4
- Schema.org JSON-LD (JewelryStore) pour le SEO
- Open Graph, Twitter Cards
- Métadonnées PWA-friendly

### Backend

- Supabase (PostgreSQL + Storage + Auth + Edge Functions Deno)
- 12 Edge Functions Deno (Web Crypto API native)
- Vercel serverless (proxy admin, paiement)
- Tables Supabase : orders, products, promo_codes, settings, lookbook, debug_logs

### Paiement et facturation

- Stripe Checkout Sessions + Stripe Webhooks (vérification HMAC-SHA256 custom)
- PayPal (create-order + capture-order)
- Code promo avec validation server-side

### Expédition

- Chronopost (toutes zones : FR / EU / Suisse / UK / Monde)
- Génération automatique du lien de tracking dans l'email d'expédition

### Mails transactionnels

- Resend API
- Templates bilingues FR/EN
- Détection auto de langue via metadata Stripe

### Sécurité

- HMAC-SHA256 (Web Crypto API native)
- Rate limiting in-memory custom
- Timing-safe comparison
- Whitelist de paths
- Headers HTTP : CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Permissions-Policy, Referrer-Policy
- CORS strict par origine

### Déploiement

- Vercel (front + API serverless)
- Vercel Insights (analytics)
- Variables d'environnement pour secrets

## Impact

- Site en production sur [fusil.paris](https://fusil.paris)
- E-commerce complet livré en solo de A à Z
- Sécurité bancaire en place dès le 1er commit (HMAC custom, rate limiting, timing-safe auth)
- Bilingue FR/EN sur l'ensemble des touchpoints clients (front + emails)
- Double provider de paiement (Stripe + PayPal) pour maximiser le taux de conversion

## Related

- [experience/microphage.md](../experience/microphage.md)
- [stack.md](../stack.md)
