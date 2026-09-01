---
id: project-microphage-analyzer-pro
title: Microphage Analyzer Pro - B2B AI Tool for UX Writing
type: project
category: app
domain: project
tags: [microphage, b2b-saas, multi-tenant, ai, index-first, vision-llm, governed-vault]
status: live
created: 2026-04-30
updated: 2026-09-01
period: 2025-11 / present
client: Microphage (SASU)
industries: [SaaS, AI/ML, Design Tools]
team: 1 (Romain Bigache, solo)
url: null
demo: null
links:
  - experience/microphage.md
---

# Microphage Analyzer Pro

| Key | Value |
|-----|-------|
| **Type** | B2B SaaS multi-tenant AI tool for UX writing |
| **Status** | In production, first client deployment in progress |
| **Project start** | November 2025 (SASU incorporation + product structuring) |
| **Company** | Microphage (SASU) |
| **Industries** | SaaS, AI/ML, Design Tools |
| **Team** | Romain Bigache (solo) |

## Short title

B2B AI tool for UX writing audits in design workflows.

## Genesis

Microphage Analyzer Pro launched in November 2025, alongside the incorporation of Microphage (as the BforBank engagement was wrapping up). The product builds on three years of prior personal R&D in AI-assisted UX writing, consolidated and structured into a standalone B2B product when Microphage was created.

## Short description

B2B AI tool that audits, rewrites and advises on UX writing in design workflows. Several enterprise pilots in pipeline.

## Long description

### Problem

Design teams in large enterprises ship screens continuously without systematic content quality checks. Internal UX writing rules (editorial guidelines, tone, accessibility, compliance) are rarely applied consistently. Manual audits cost hours of review per sprint.

### Solution

Microphage Analyzer Pro covers audit, rewrite, statistical insights and conversational queries on a client's content design system. Multi-tenant architecture designed to onboard new enterprise clients without touching the product core.

Since mid-2026 the engine runs index-first: a single vision call (FastAPI audit service + Gemini) receives a compact index of the governed rule vault (897 rules, one line per rule) plus the screenshot, opens full rule files on demand through a `read_rules` tool, runs an adversarial designer critique, and returns verdicts plus rewrites. The vault itself is maintained through a governed red/blue pipeline (rule writers + gatekeeper) inherited from the Karpathy LLM wiki method.

A companion web app and a standalone chat interface are on the roadmap to extend the tool beyond the design surface.

## Impact

- First enterprise client engagement (B2B edtech), several pilots in pipeline
- Multi-tenant architecture ready to scale to additional clients

## Related

- [experience/microphage.md](../experience/microphage.md)
