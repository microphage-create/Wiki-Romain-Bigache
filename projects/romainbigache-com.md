---
id: project-romainbigache-com
title: romainbigache.com - Personal site with AI agent
type: project
category: site
domain: project
tags: [personal-site, oauth, google-workspace, calendar-api, drive-api, tool-streaming, vercel, next-js, ai-agent]
status: live
created: 2026-04-30
updated: 2026-04-30
period: 2025 / present
client: Personal
industries: [Personal, AI/ML]
team: 1 (Romain Bigache, solo)
url: https://romainbigache.com
demo: https://romainbigache.com
technologies: [Next.js, TypeScript, Vercel AI SDK, OpenAI, Anthropic Claude, Google Calendar API, Google Drive API, OAuth2, Vercel Cron, tool calling, streaming UI]
links:
  - experience/microphage.md
  - expertise.md
  - stack.md
---

# romainbigache.com

| Key | Value |
|-----|-------|
| **Type** | Personal site + conversational AI agent |
| **Status** | In production |
| **Year** | 2025 - ongoing |
| **URL** | [romainbigache.com](https://romainbigache.com) |
| **Team** | Romain Bigache (solo) |

## Short title

Personal site with conversational AI agent and Google Workspace integrations in production.

## Short description

Portfolio site + personal AI chat hooked into Google Workspace (Calendar and Drive in production). Concrete demonstration of the OAuth2 + Workspace API + tool streaming UI pattern: the agent can read and summarize the calendar, read Drive documents, and stream the rendering directly into the conversation.

## Long description

### Concept

Personal site designed as a product demonstrator: a conversational AI agent wired into Marcel's Google Workspace tools, serving simultaneously as portfolio (the agent can comment on its own projects) and proof of execution on the Workspace integration pattern in full autonomy.

### Integrations in production

- **Google Calendar API**: OAuth2 connection to the personal calendar, the agent can check availability, summarize the week, identify meetings. UI rendering streamed directly into the chat: tool call executes, data arrives, UI builds live above the text response.
- **Google Drive API**: OAuth2 on personal Drive, document reading, on-the-fly summaries, folder navigation. Nightly sync via Vercel cron to pre-index recent documents.

### Architecture

- **Front**: Next.js 16, React 19, TypeScript strict, Tailwind, shadcn/ui
- **AI**: Vercel AI SDK v6 multi-provider (OpenAI, Anthropic Claude), tool calling, streaming UI
- **Auth**: Google OAuth2 with refresh tokens, minimal scopes (calendar.readonly, drive.readonly)
- **Cron**: Vercel Cron Jobs for nightly Drive sync
- **Deployment**: Vercel serverless

### Reusable pattern

The full pattern (OAuth2 + Workspace API + tool streaming UI + cron sync) is documented and reusable on any role requiring Google Workspace, Microsoft Graph, or any similar Workspace API integration (Notion, Slack, Linear).

## Technologies used

- Next.js 16 (App Router)
- React 19
- TypeScript strict
- Tailwind CSS 4 + shadcn/ui
- Vercel AI SDK v6
- OpenAI API + Anthropic Claude API
- Google Calendar API + Google Drive API
- OAuth2 (refresh tokens, scope-limited)
- Vercel Cron Jobs
- Streaming UI (tool calls with live rendering)

## Lighthouse Performance

Reports from April 30, 2026 (Lighthouse 13.0.1, HeadlessChromium 146).

### Homepage `romainbigache.com/`

| Category | Mobile |
|----------|--------|
| **Performance** | 95 / 100 |
| **Accessibility** | 95 / 100 |
| **Best Practices** | 100 / 100 |
| **SEO** | 100 / 100 |

Core Web Vitals (mobile, Moto G Power, slow 4G):

| Metric | Value |
|--------|-------|
| First Contentful Paint (FCP) | 1.4 s |
| Largest Contentful Paint (LCP) | 2.0 s |
| Total Blocking Time (TBT) | 210 ms |
| Cumulative Layout Shift (CLS) | 0 |
| Speed Index | 3.1 s |

### Portfolio page `romainbigache.com/fr/portfolio`

| Category | Mobile | Desktop |
|----------|--------|---------|
| **Performance** | 99 / 100 | 99 / 100 |
| **Accessibility** | 95 / 100 | 95 / 100 |
| **Best Practices** | 100 / 100 | 100 / 100 |
| **SEO** | 100 / 100 | 100 / 100 |

Core Web Vitals (mobile):

| Metric | Value |
|--------|-------|
| First Contentful Paint (FCP) | 1.4 s |
| Largest Contentful Paint (LCP) | 1.8 s |
| Total Blocking Time (TBT) | 30 ms |
| Cumulative Layout Shift (CLS) | 0 |

All Core Web Vitals in the green on both pages. CLS = 0 (zero visual shift during load). TBT = 30 ms on portfolio (excellent, minimal main thread blocking).

## Impact

- Site live at [romainbigache.com](https://romainbigache.com)
- Lighthouse mobile home: 95 / 95 / 100 / 100
- Lighthouse mobile and desktop portfolio: 99 / 95 / 100 / 100
- SEO 100 / 100 across all tested pages
- Demonstrator of the Google Workspace integration pattern
- Used as a demo platform during pitches and interviews
- Hands-on maintenance of OAuth2 + tool streaming integrations in full autonomy

## Related

- [experience/microphage.md](../experience/microphage.md)
- [expertise.md](../expertise.md)
- [stack.md](../stack.md)
