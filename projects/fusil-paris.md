---
id: project-fusil-paris
title: fusil.paris - Handcrafted jewelry e-commerce
type: project
domain: project
tags: [fusil-paris, e-commerce, jewelry, next-js-16, edge-functions, deno, stripe, paypal, hmac, security, chronopost, bilingual, solo, co-founded]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2024 / present
client: fusil.paris (co-founded with Edouard)
industries: [E-commerce, Jewelry, Crafts]
team: 2 (Romain Bigache - tech/design/copy, Edouard - cofounder, jewelry creation)
url: https://fusil.paris
demo: https://fusil.paris
technologies: [Next.js 16, React 19, TypeScript 5, Tailwind CSS 4, Supabase, Edge Functions Deno, Stripe, PayPal, Resend, Chronopost, HMAC-SHA256, Web Crypto API, Vercel]
links:
  - experience/microphage.md
  - stack.md
---

# fusil.paris

| Key | Value |
|-----|-------|
| **Type** | Handcrafted jewelry e-commerce (co-founded) |
| **Status** | In production |
| **Year** | 2024 - ongoing |
| **URL** | [fusil.paris](https://fusil.paris) |
| **Company** | fusil.paris (handcrafted 925 silver jewelry brand made in Paris) |
| **Industries** | E-commerce, Jewelry, Crafts |
| **Team** | Romain Bigache (concept, design, code, security, deployment, copy, emails), Edouard (cofounder, jewelry creation) |

## Short title

Handcrafted jewelry e-commerce, designed, coded and deployed solo.

## Short description

Full e-commerce store for fusil.paris (925 silver jewelry handmade in Paris). Designed, coded and deployed end-to-end solo: Next.js 16 + React 19 front, dual-provider checkout (Stripe + PayPal), 12 Deno Edge Functions, bilingual FR/EN transactional emails, multi-zone Chronopost shipping, secured admin panel, banking-grade security (HMAC-SHA256, CSP, HSTS, rate limiting, timing-safe auth).

## Long description

### Context

fusil.paris is a brand of 925 silver jewelry handcrafted in Paris (Brut, Leaf, Paris, Hors Serie collections), co-founded with Edouard. The site serves as both narrative showcase and e-commerce store with a 250-380 EUR cart, requiring a high bar on trust and payment security.

### Solo scope

Art direction, copy, code (front + back), payment integration, security, transactional emails, admin panel, deployment, monitoring. End-to-end.

### Front and SEO

Next.js 16 (App Router) + React 19 + Tailwind 4 + TypeScript 5. Bilingual FR/EN site, optimized for social sharing and SEO: Schema.org JSON-LD (JewelryStore), Open Graph, Twitter Cards, PWA-friendly metadata (theme-color, apple-mobile-web-app-capable, viewport-fit cover). Reusable UI components, performance tuned for conversion.

### Backend Edge Functions (Deno + Supabase)

12 Edge functions deployed covering the full order lifecycle:

- Stripe webhooks (custom HMAC-SHA256 verification via native Web Crypto API, no Stripe SDK dependency)
- Client-side confirmation for idempotency
- Admin authentication with timing-safe comparison
- Order cancellation with automatic refund
- Secure client order retrieval (token-based)
- Partial or full Stripe refund
- Return request workflow
- 5 bilingual FR/EN transactional email functions (confirmation, shipping, delivery, ready-to-ship, showroom appointment)

### Production-grade security

- **Custom HMAC-SHA256 verification of Stripe webhooks** via native Web Crypto API, without relying on the Stripe SDK: timestamp + v1 signature
- **In-memory rate limiting** on Vercel serverless: 60 req/min global + 5 auth failures/min, with sliding windows and periodic cleanup
- **Timing-safe comparison** for the admin token: protection against timing attacks via bit-by-bit comparison
- **Path whitelist** in the admin proxy (allow-list, not deny-list): only the required Supabase endpoints are authorized
- **Vercel security headers**: CSP with restrictive frame-ancestors, HSTS 1 year with includeSubDomains, X-Content-Type-Options, X-Frame-Options DENY, X-XSS-Protection, Referrer-Policy strict-origin-when-cross-origin, Permissions-Policy disabling camera / mic / geolocation
- **Strict CORS** on admin: only from fusil.paris and www.fusil.paris
- **Body size limit** on admin requests to prevent abuse
- **Supabase service role key** never exposed client-side: everything goes through a Vercel proxy

### Dual-provider checkout

- **Stripe Checkout Sessions** with shipping rates per zone (FR, EU, Switzerland, UK, World, pickup) and idempotent webhook
- **PayPal** full integration (create-order + capture-order) with state and error handling
- **Promo codes** with server-side validation: minimum amount, expiration dates, discount type (% or fixed)

### Bilingual FR/EN transactional emails

All customer emails (confirmation, shipping, delivery, appointment, return, refund) support FR + EN with automatic language detection from Stripe metadata. Inline HTML templates with text fallback. Sent via Resend.

### Multi-zone shipping (Chronopost)

Rates and lead times per zone: France free (2-3 days), Europe free (3-5 days), Switzerland EUR 25, UK EUR 25 ex-tax (UK taxes on top), World EUR 35 (4-7 days), in-store pickup free. Automatic carrier display on the client side. Tracking number entry on the admin side, automatic generation of the direct chronopost.fr tracking link in the shipping email sent to the customer.

### Secured admin panel

Full management of products, orders, promo codes, settings, lookbook and application logs. Token-based authentication protected via environment variable, rate limiting on auth failures, timing-safe comparison (anti timing-attack), path whitelist on the Vercel proxy.

### Monitoring

Vercel Insights for performance, Supabase for application tracing, centralized Stripe + PayPal logs.

## Technologies used

### Front

- Next.js 16 (App Router)
- React 19
- TypeScript 5
- Tailwind CSS 4
- Schema.org JSON-LD (JewelryStore) for SEO
- Open Graph, Twitter Cards
- PWA-friendly metadata

### Backend

- Supabase (PostgreSQL + Storage + Auth + Edge Functions Deno)
- 12 Deno Edge Functions (native Web Crypto API)
- Vercel serverless (admin proxy, payment)
- Supabase tables: orders, products, promo_codes, settings, lookbook, debug_logs

### Payment and billing

- Stripe Checkout Sessions + Stripe Webhooks (custom HMAC-SHA256 verification)
- PayPal (create-order + capture-order)
- Promo codes with server-side validation

### Shipping

- Chronopost (all zones: FR / EU / Switzerland / UK / World)
- Automatic tracking link generation in the shipping email

### Transactional emails

- Resend API
- Bilingual FR/EN templates
- Auto language detection via Stripe metadata

### Security

- HMAC-SHA256 (native Web Crypto API)
- Custom in-memory rate limiting
- Timing-safe comparison
- Path whitelist
- HTTP headers: CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Permissions-Policy, Referrer-Policy
- Strict CORS by origin

### Deployment

- Vercel (front + serverless API)
- Vercel Insights (analytics)
- Environment variables for secrets

## Impact

- Site live at [fusil.paris](https://fusil.paris)
- Full e-commerce delivered solo end-to-end
- Banking-grade security in place from the first commit (custom HMAC, rate limiting, timing-safe auth)
- Bilingual FR/EN across all customer touchpoints (front + emails)
- Dual payment provider (Stripe + PayPal) to maximize conversion rate

## Related

- [experience/microphage.md](../experience/microphage.md)
- [stack.md](../stack.md)
