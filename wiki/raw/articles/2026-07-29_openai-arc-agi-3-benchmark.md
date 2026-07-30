---
title: "How enabling two settings tripled our scores on the ARC-AGI-3 benchmark"
source_url: "https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/"
source_domain: "openai.com"
author: "OpenAI"
date: "2026-07-29"
date_ingested: "2026-07-30"
type: raw_article
tags:
  - ai-benchmarks
  - arc-agi
  - openai
  - gpt-5.6-sol
  - reasoning
  - agent-performance
  - compaction
  - responses-api
  - evaluation
extraction: complete
extraction_method: "jina.ai reader (Cloudflare blocked direct fetch)"
hn_url: "https://news.ycombinator.com/item?id=49104184"
hn_points: 29
hn_comments: 4
---

# How enabling two settings tripled our scores on the ARC-AGI-3 benchmark

**Source:** [openai.com](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/)
**Date:** July 29, 2026
**Author:** OpenAI

---

_A sped-up video of GPT‑5.6 Sol attempting to solve puzzles in the ARC-AGI-3 benchmark, with the official harness (left) and our Responses API harness (right), which retains reasoning and enables compaction. On the leaderboard for [this game](https://arcprize.org/tasks/cd82), no frontier model solves any level beyond the first. With our harness, GPT‑5.6 Sol solves all six._

GPT‑5.6 Sol has solved longstanding open problems in mathematics like the [cycle double cover conjecture](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf) and beaten games like Pokémon FireRed. But on ARC-AGI-3, a benchmark of 2D puzzle games, GPT‑5.6 Sol scored just 7.8%, and GPT‑5.5 could barely play the games at all, scoring a paltry 0.4%.

Were 2D puzzle games unusually difficult for our models? Or was something else going on?

Benchmarks rarely measure AI models in isolation. They also measure less visible choices about API settings, harness design, and prompting. In the case of ARC-AGI-3, we discovered that turning on two API settings we use in ChatGPT and Codex—retained reasoning and compaction—tripled scores and cut output tokens by 6x on the public task set.

_With the official harness, GPT‑5.6 Sol scored 13.3% on the ARC-AGI-3 public set. With retained reasoning and compaction, it scored 38.3%. Scores measure Relative Human Action Efficiency ([RHAE](https://docs.arcprize.org/methodology))—a metric comparing model performance to a human baseline. Based on [official gameplay logs](https://huggingface.co/datasets/magic-sword/arc_agi_3_public_demo_human_testing), we estimate the average human tester scored 48%. Models are not told how they will be scored, and cannot see their score throughout—actions only return a text representation of each frame and what level they are on._

## ARC-AGI-3

ARC-AGI-3 is a benchmark designed to measure how well AI agents learn and reason. Agents explore unfamiliar 2D games and infer how they work without explicit instructions. You can play 25 demo games at [arcprize.org/tasks](https://arcprize.org/tasks).

ARC-AGI-3 uses an intentionally generic harness, without tools or special features. ARC's reasoning was that a simple harness makes model shortcomings more visible and makes model comparisons more fair. Commercial developers, by contrast, optimize harnesses for each model's features and quirks.

_Ethan Mollick [shows](https://x.com/emollick/status/2075950897029374334) GPT‑5.6 Sol in Codex beating a randomized daily challenge in Slay the Spire 2, a game released after GPT‑5.6 Sol's knowledge cutoff._

But as we looked deeper, we discovered much of the model's confusion was not inherent to the model itself, but due to settings in the harness.

First, we noticed that after each game action, all private reasoning was discarded. This meant that with each action, GPT‑5.6 Sol was asked to figure out the game anew, unable to remember its past thinking. The model could still see a record of past moves and brief accompanying notes, but it could not see the plans, insights, or thoughts that led to them.

Second, we saw that the harness used a rolling truncation window, causing older actions to become invisible as the history grew. So not only was GPT‑5.6 Sol unable to remember its past thinking, it was losing memory of its past actions too.

Together, these two features of the harness—discarding reasoning and rolling truncation—helped explain why GPT‑5.6 Sol was struggling to learn over time.

## Agents do best when they remember what they've done

Our models are trained to think with private reasoning messages before they output replies or tool calls. These private thinking messages are retained as part of the conversation history. If a conversation grows too long, we summarize it and continue.

This is how our models are trained, and also how they are deployed in ChatGPT and Codex. To better match our production setup, we implemented the ARC-AGI-3 harness with our [Responses API](https://developers.openai.com/blog/responses-api). Our API makes it easy to manage context: for GPT‑5.6, passing the previous response ID automatically retains reasoning across tool calls and turns.

With reasoning retained, we noticed two big changes. First, GPT‑5.6 Sol spent less time thinking before each action, because it no longer had to interpret the game from scratch every turn. Second, when it was able to remember its past thoughts, GPT‑5.6 Sol was much better at learning over time and employing coherent strategies.

The next improvement came from replacing rolling truncation with [compaction](https://developers.openai.com/api/docs/guides/compaction), another setting in the Responses API.

The ARC-AGI-3 harness addresses context limits with rolling truncation. When the conversation context exceeds 175,000 characters, the oldest messages are discarded.

Rolling truncation has two drawbacks. First, the model loses earlier observations and actions. Second, it spends much of the tasks operating with a fuller context window, which can slightly impair performance.

When we enabled compaction on ARC-AGI-3, GPT‑5.6 Sol was better able to preserve what it had learned about each game across longer runs, and achieved a higher score with fewer output tokens.

To illustrate the effect of retaining reasoning and enabling compaction, here's an animation showing GPT‑5.6 Sol's 175K context window as it solves a series of ARC-AGI-3 puzzles with each harness.

_The two central columns depict how the model context window is used differently by each harness. With better memory of its past, GPT‑5.6 Sol thinks less per action and proceeds much faster. Note: our implementation uses a limit of 175,000 tokens instead of characters, but this ends up being quite similar, as the vast majority of text is action grids which are tokenized at a 1:1 ratio by our tokenizer._

Together, retaining reasoning and compaction allow GPT‑5.6 Sol (max) to achieve roughly 3x the score with 6x fewer output tokens.

## Conclusion and recommendations

We hope these experiments serve as a reminder that evals rarely measure models in isolation—they also measure a bundle of less visible choices about API settings, harness design, and prompting. This isn't the first time we've been surprised by low scores on a public benchmark and then discovered that the eval runner was using a generic harness that dropped reasoning messages.

If you're an API developer trying to maximize performance, we recommend using the same settings that we deploy in our own products:

* Use our Responses API, not our legacy Chat Completions API
* Retain reasoning
* Use compaction

And if you're comparing models, we recommend relying on evals that use the settings above, which best match real-world use in ChatGPT and Codex.

We are grateful to ARC for their years of creative work on AGI evaluation, and for their analysis that inspired us to take a closer look here.

---

## HN Discussion Highlights

**HN Thread:** https://news.ycombinator.com/item?id=49104184 (29 points, 4 comments)

**simianwords:** On one hand I agree with ARC team that harnesses can incorporate some logic and overfit to win the tests. But also, the specific harness that OpenAI wants to use is not cherry picked. What then should be the rules? Same harness for all or company's standard commercial harness? Technically even that could incorporate some hacks.

**FacelessJim:** "Agents do best when they remember what they've done" — Sometimes I am baffled that sentences like this are used as headlines. I know I'll sound dismissive… but: duh?!

**embedding-shape:** I think this blog post might be a "reply" of sorts to Anthropic's tweet from some days earlier: "On ARC-AGI-3, an evaluation where AI models must solve novel problems, Opus 5's score is three times as high as the next best model." [Source](https://x.com/claudeai/status/2080699504576045299)
