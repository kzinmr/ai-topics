---
title: "A new feature for my blog, built using my voice"
author: Simon Willison
url: https://simonwillison.net/2026/Oct/9/built-using-my-voice/
source: simonwillison.net
captured: 2026-10-09
date: 2026-10-09
type: raw-article
tags: [coding-agents, prompt-engineering]
sources:
  - https://simonwillison.net/2026/Oct/9/built-using-my-voice/
  - https://x.com/simonw/status/2108547065634844839
---

# A new feature for my blog, built using my voice

Simon Willison shipped a Newsletters index page for simonwillison.net, built almost entirely
by voice with Codex voice mode (ChatGPT desktop app, Codex tab) running against a local
development environment — while cooking dinner. Model used: **GPT-6 Astra High**.

## Workflow

1. Typed one initial prompt: "Start dev server and open in browser" — gave the agent a live
   visual preview of the site to track progress against.
2. Clicked "Start new voice chat" (distinct from the microphone button), set the laptop in the
   kitchen, and talked through the feature spec in natural, disfluent speech for ~30 minutes
   (the time it took to cook dinner). Full voice transcript (with disfluencies) published as a Gist:
   https://gist.github.com/simonw/a65a22204f6f7228cc59b4bc34d7c7c8
3. The model handled a Django feature: new model + migration, admin config, view code,
   templates, and import functions.

## What was built (mostly by voice)

- New Django model/migration for imported newsletters + Admin configuration
- Four working imports: recent Substack items via RSS; the rest of Substack via its
  undocumented `/api/v1/archive` API (which GPT-6 Astra knew about, then searched to
  figure out pagination); published monthly newsletters from `simonw/monthly-newsletter-archive`;
  latest private sponsors-only newsletter from a private repo
- `/newsletters/` and `/newsletters/2026/` archive pages; newsletters appear on day/month
  archive pages but not tag pages or homepage
- GPT-6 Astra designed the page and iterated on the design from Simon's verbal feedback while
  glancing at the local preview across the kitchen

## Finishing with a review

After cooking, Simon had Codex open a PR and reviewed in the GitHub PR interface. Found one
design decision he disagreed with (Git subprocess for one import script; he preferred the GitHub
API since the source was a private repo). Switched to typing for ~30 more minutes of prompt-based
fixes and tweaks before landing and deploying.

## Takeaways (Simon's conclusions)

- Voice coding mode is **better for multi-tasking than as a daily driver**: visual preview + ability
  to type/paste when something can't be communicated vocally makes it much more powerful than
  phone voice mode (which he previously used for research/brainstorming while walking the dog).
- He still switches to typing for details — pasting examples/error messages or highlighting code
  remains more efficient than describing them in words.
- Requires a home workspace: "no way I'd want to talk to my computer like this in a shared workspace."
- Killer feature: build stuff while cooking instead of listening to podcasts.

Related: PR https://github.com/simonw/simonwillisonblog/pull/719 ("Add newsletters with
archives, search, and Substack import buttons").
