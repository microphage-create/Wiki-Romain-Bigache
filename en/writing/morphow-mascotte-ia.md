---
id: writing-morphow-mascotte-ia
title: I generated 352 AI mascots. The right one wasn't in there.
description: How I designed Morphow's mascot using a custom AI agent, 352 iterations, and a human illustrator to actually own the IP.
type: writing
domain: blog-article
tags: [morphow, mascot, prompt-oracle, comfyui, gemini, illustrator, intellectual-property, ai-workflow]
status: published
created: 2026-04-30
updated: 2026-04-30
url: https://romainbigache.com/en/blog/morphow-mascotte-ia
slug: morphow-mascotte-ia
links:
  - writing.md
  - projects/mycelium.md
---

# I generated 352 AI mascots. The right one wasn't in there.

I'm building a SaaS called Morphow. Modular white-label webapps for companies: onboarding, training, quizzes, surveys. The kind of product that needs a strong identity. Not a Canva logo. A mascot. A character that can live inside the interface, react to user actions, embody the brand.

At first I had nothing concrete. I was seeing the Pokemon Ditto, a Barbapapa (swear it's not 10-year-old me being nostalgic), some white thing floating around. That's it. The rest came through iteration.

I decided to generate it myself. With my own tool.

## The tool: /prompt-oracle

Before talking about the mascot, I need to talk about the tool that made it. Because it's not Midjourney. It's not DALL-E. It's an agent I built myself.

/prompt-oracle is a Claude Code skill that orchestrates ComfyUI locally with Gemini 2.5 Flash as the generation model. The agent writes the prompts, configures the workflows, runs the generations, and organizes the outputs. It has 8 modes: simple prompt, full ComfyUI workflow, batch variations, multi-pose character sheet, iterative refinement, 3D icon generation.

The important bit: ComfyUI runs locally on my machine, but Gemini 2.5 Flash is still a cloud API. The difference is the price: ~$0.04 per image instead of $0.50 on Midjourney. I can generate 4 variations in 15 seconds and iterate 352 times without thinking about budget.

And that's exactly what I did.

## Phase 1: the Pokemon starting point

The Morphow mascot is Morphow. The character and the brand are one. Morphow = Morph On Web. And the nod to Ditto, the Pokemon that shapeshifts into anything, is no accident. That's exactly what the product does: webapps that take the shape of the client's need.

My first prompts started there. A white Ditto, in 3D, clay/vinyl style.

The output was cute. But pink. And too Pokemon. You could spot the reference instantly. If anyone at Nintendo stumbled on it, that was a cease & desist waiting to happen.

I needed to get away from the source.

## Phase 2: the dead ends

This is where it gets interesting. When you tell an AI "move away from Ditto but keep the spirit," it goes everywhere.

Gengar direction: a white monster with red eyes and teeth. Aggressive, intimidating. Humanoid direction: a thin white alien standing on two legs. Too anthropomorphic. Classic ghost direction: a smiling little white ghost, completely generic. Jellyfish direction: iridescent tentacles, interesting but too aquatic.

And a dozen more. Each batch of 4 images took 15 seconds. In one evening I had 50 different directions.

The problem: each direction had something good. None had everything. The ghost had the right shape but no personality. The Gengar had character but was scary. The blob was original but unreadable at small size.

## Phase 3: the click

After ~80 iterations, I generated something that made me pause.

A white Pac-Man ghost. Half-closed, angular eyes. No mouth. Floating. Looking at you with this kind of relaxed superiority. Like it knew something you didn't.

That was the character. Not the exact design, but the attitude. Angular black eyes on iridescent white, no mouth. Expression goes through the eyebrows. Minimal, recognizable, scalable.

From there, I tightened. No more divergence. Just convergence.

## Phase 4: convergence (and frustration)

The next 120 iterations were surgery. Adjust proportions. Test poses (standing, walking, sitting). Vary the material (vinyl, clay, glossy, matte). Tune the eyebrows, the eye angle, the head-to-body ratio.

That's when I hit the wall.

AI generates images. Not characters. Each generation is unique. Proportions shift 2-3% between images. Eyes are never in exactly the same spot. One arm is slightly bigger than the other. The silhouette changes subtly from batch to batch.

For a single image, it's imperceptible. For a character sheet (front, profile, 3/4, back), it's a nightmare. You can never get the same character from multiple angles. And for expressions (happy, sad, angry, neutral), it's worse: each emotion produces a slightly different character.

352 iterations. Dozens of "almost there." And always that 5% missing.

## The pivot: from 3D to flat

I gave up at 3am. But not the head. In bed I opened Gemini on my phone and started talking to it about the project. No image prompts. Just a conversation. What I wanted, what I couldn't get, why 3D was blocking me.

Gemini brought up the Intel strategy: simplify radically. A logo that works at 16px and at 4K. No reflections, no textures, no 3D. Flat. Vector. And it was right: my 3D iterations looked nice big but were unreadable small. A favicon, a notification, a chat avatar: all of that needs a character readable in a few pixels.

We made the call: it's going to be flat. And then Gemini proposed a version based on my 3D iterations. Same proportions, same angular eyes, same no-mouth. But flat, with a thin outline and an iridescent white fill.

Bingo. I broke the middle lines on the body, kept the angular eyes, and the character was there. Not 3D. Flat. Readable, scalable, and most importantly: reproducible.

## The illustrator

I called Remi.

Remi Rohart, illustrator. But heads up: I didn't show up empty-handed asking him to "draw me a mascot." I had a near-finished character. The shape, the attitude, the proportions, the material, the angular eyes, the no-mouth, the iridescence. 352 iterations to get there. What I didn't have was execution rigor: an identical character from every angle, consistent expressions, and a usable vector file.

I sent him my best AI outputs as a visual brief. Not a 40-page spec. The images. "This is the character. I want exactly this, but clean. Multi-angle, expressions for app states, and a do & don't doc."

He worked in Illustrator. In 48 hours he had:

- The character vectorized in 6 angles (front, left profile, 3/4, right profile, back, app icon)
- Exact proportions with construction guides
- 5 application expressions: determined (default), empty state, error, success, loading
- A "Do & Don't" guide: no clothing, no mouth, expression only through eyes and eyebrows, hand-held object possible but discouraged
- Authorized transformations (the character can morph into a cube, box, geometric shapes)
- The exact color palette (#2B0545, #F1E5FF) with a defined radial gradient center

Clean Figma delivery. Every element usable as-is in the interface.

What Remi brought in 48h wasn't the character: the character already existed. It was what AI couldn't have done in 2000 iterations: consistency. The same character, exactly the same, from every angle and in every emotion. Fixed proportions. Construction guides so anyone can reproduce it. A system, not an image.

But this delivery also fixed a problem most "I did it all with AI" articles prefer to ignore.

## The IP gray zone

Under current law, an AI-generated image isn't protected by copyright. Not in France, not in the US. The US Copyright Office said it clearly in 2023: no human author, no copyright. In Europe the position is similar: copyright protects original works resulting from human intellectual creation. A prompt, however elaborate, isn't considered a sufficient act of creation.

Concretely: my 352 ComfyUI images don't legally belong to me. Anyone could take the same aesthetic, the same character, and I'd have no recourse.

That's a problem when you're building a brand. Your mascot is your identity. If it's not protectable, it's worth nothing legally. And I hit that wall in practice: I tried to register the character as a figurative trademark with the INPI (the French trademark office). Impossible. No human author, no filing.

Let's be honest: I'm the first to defend paying illustrators properly. But I've been working unpaid for months. Zero revenue, only investment. Paying an illustrator for a full character sheet was above what I could put in. But doing nothing was worse. So I found the in-between: have an illustrator work three days instead of three weeks. Because the brief was already done. 352 iterations is 352 visual decisions. Remi didn't have to find the character. It was there. He just had to build it cleanly.

Remi took the character into Illustrator, using my AI outputs as visual basis, and rebuilt it entirely as vector. His work is an original creation, copyright-protected from the moment it exists. The vector files, the character sheet, the expressions: all of that is legally mine (with rights assignment). I can register the mascot as a figurative trademark. I can sue if someone copies it.

The AI generated the inspiration. The human generated the IP.

That's not a detail. For a SaaS that wants to raise, sell, or simply protect its identity, the question "do you actually own your mascot?" has a binary answer. And if the answer relies only on AI outputs, it's no.

## What I learned

AI is an explorer, not a craftsman. In 352 iterations I covered a possibility space that human brainstorming would have taken weeks to walk through. I tested directions I'd have never considered (the jellyfish, the detective dog, the shapeless blob). Some were terrible. Others surprised me. And the final brief came out of that exploration.

But exploration isn't enough. At some point you have to lock it down. Decide that THIS character, with THESE proportions, THESE eyes, at THIS angle, is the one. And reproduce it identically 50 times. AI can't do that. Not yet.

And even if it could, the result wouldn't be yours.

The real workflow isn't AI vs human. It's AI then human. AI opens the space. The human closes it. And the human signs.

And the fact that I built my own generation tool made exploration 10x faster and 100x cheaper than any cloud service. 352 iterations at ~$0.04 each is ~$14. The result is a visual brief so precise that the illustrator delivered in 48h with no back-and-forth.

> ~14 dollars of AI and a good illustrator. That's how you design a mascot in 2026.

## Related

- [writing.md](../writing.md)
- [projects/mycelium.md](../projects/mycelium.md)
