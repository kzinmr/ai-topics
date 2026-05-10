---
title: "Introducing Composer 1.5 · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/composer-1-5"
scraped: "2026-05-10T01:19:41.802419+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Introducing Composer 1.5 · Cursor

**Source**: [https://cursor.com/blog/composer-1-5](https://cursor.com/blog/composer-1-5)

Blog
/
research
Feb 9, 2026
·
research
Introducing Composer 1.5
3 min read
A few months ago, we released our first agentic coding model,
Composer 1
. Since then, we've made significant improvements to the model’s coding ability.
Our new release, Composer 1.5, strikes a strong balance between speed and intelligence for daily use. Composer 1.5 was built by scaling reinforcement learning 20x further on the same pretrained model. The compute used in our post-training of Composer 1.5 even surpasses the amount used to pretrain the base model.
We see continued improvements on coding ability as we scale. Measured by our internal benchmark of real-world coding problems, we find that the model quickly surpasses Composer 1 and continues to climb in performance. The improvements are most significant on challenging tasks.
Composer 1.5 is a thinking model. In the process of responding to queries, the model generates thinking tokens to reason about the user’s codebase and plan next steps. We find that these thinking stages are critical to the model’s intelligence. At the same time, we wanted to keep Composer 1.5 fast and interactive for day-to-day use. To achieve a balance, the model is trained to respond quickly on easy problems with minimal thinking, while on hard problems it will think until it has found a satisfying answer.
1
To handle longer running tasks, Composer 1.5 has the ability to self-summarize. This allows the model to continue exploring for a solution even when it runs out of available context. We train self-summarization into Composer 1.5 as part of RL by asking it to produce a useful summary when context runs out in training. This may trigger several times recursively on hard examples. We find that self-summarization allows the model to maintain its original accuracy as context length varies.
Composer 1.5 is a significantly stronger model than Composer 1 and we recommend it for interactive use. Its training demonstrates that RL for coding can be continually scaled with predictable intelligence improvements.
Learn more about Composer 1.5 pricing
here
.
Terminal-Bench 2.0 is an agent evaluation benchmark for terminal use maintained by the Laude Institute. Anthropic model scores use the Claude Code harness and OpenAI model scores use the Simple Codex harness. Our Cursor score was computed using the official
Harbor evaluation framework
(the designated harness for Terminal-Bench 2.0) with default benchmark settings. We ran 2 iterations per model-agent pair and report the average. More details on the benchmark can be found at the official
Terminal Bench website
. For other models besides Composer 1.5, we took the max score between the
official leaderboard
score and the score recorded running in our infrastructure.
↩
Filed under:
research
Author
:
Cursor Team
