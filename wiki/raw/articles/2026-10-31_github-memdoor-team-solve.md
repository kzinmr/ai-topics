---
source: https://github.com/guregodevo/memdoor
author: guregodevo
collected: 2026-11-01
type: article
sha256: f17ca75a3ce33ce8e90a861ac0d07ab35181818f6c39fd862b1abd29cf745478
---

# Memdoor — GitHub README (guregodevo/memdoor, Apache-2.0, 111 stars, 238 commits)

Memdoor: A lightweight coding and automation agent in one CLI binary. Run locally or over SSH, optimize token use, and automate CI and cron with durable workflows. Topics: agentic-workflows, ai-agent, coding-agent, developer-tools, golang, llm, openrouter, terminal, tui, workflow.

Memdoor — "Your daemon agents on every door." A lightweight coding and automation agent in a single CLI binary. Run it locally or connect over SSH to another machine — no Docker or Python required. Work interactively from a terminal, your IDE or phone, or start a run from a shell script, CI or a schedule and finish it from any of those, on a gateway you own. BYOK.

One binary to deploy. A headless-first CLI. Multi-step jobs kept as files in your repo, with checks, approval gates and resume. Less of your token bill, through a decision model in front of the chat model.

## Five Qwen3.8-27B agents beat Fable 5 on LiveCodeBench Hard

Five Qwen3.8-27B agents beat Fable 5 on LiveCodeBench Hard, as a Memdoor workflow. GVS5H's harness rebuilt with the authors' exact prompts and loop, on the first ten problems of their list, five passes each: a mean of 9.8 of 10, against 9.6 for the authors' own harness and 8.0 for Fable 5 in a single call. All 50 runs are published: every request, reply, program and grader output. The workflow is YAML and names no model: point it at yours, or at a local one with memdoor connect local (Ollama, llama.cpp, vLLM, LM Studio). examples/workflows/team-solve.

Install: curl -fsSL https://memdoor.ai/install.sh | bash; export OPENROUTER_API_KEY (or ANTHROPIC/OPENAI/GEMINI keys), or no key at all with `memdoor connect local` against an open-weight model on the machine. Headless-first: start a run from a shell script, CI or a cron schedule, finish it from terminal/IDE/phone; durable workflows stored as files in the repo with checks, approval gates and resume; a decision model sits in front of the chat model to reduce token spend.

---

## HN discussion highlights (item 50320995, 269pts)

[guregodevo] Here the intent is to replicate GVS5H with memdoor, a headless coding agent I created months ago. Anyone can reshape the harness by redefining the steps in yaml files, models and temperatures.

[guregodevo] The original author harness is already giving 9.6 score which is pretty good. However this harness loop can take more than 1 hour on the hardest problem at 100 token/sec. A smarter model such as 3.8-flash-next could get 10 score and resolve the hardest problem faster.

[roenxi] That's pretty interesting, because with the Bonsai 2 quantisations it is quite achievable to get Qwen 27B running at 50 t/s on reasonably priced gaming machine. Which in turn suggests that Fable 5 coding performance can be achieved locally with a bit of clever harnessing. The important thing here is the cap for local performance looks like it could be quite high.

[SwellJoe] Bonsai 2-bit quantization is notably dumber than Qwen 27B at eight bits or even four bits. I doubt you'll get this level of quality even with five of them.

[Havoc] The bonsai quants are not that awesome. 5GB of bonsai weights end up being similar to 5GB of QAT weights even when one is derived from a 27B and the other from an 8B.

[vikramkr] Apparently it's really easy to get Internet points by making up a harness and showing that good open source models can do as well as the frontier, you know, on useless saturated and contaminated benchmarks from years ago that don't reflect any of the agentic work we actually use these models for.

[walrus01] I'd like to see this done with qwen 3.8-flash-next (Q8 or full precision) which beats 3.8-27B on just about every coding/command line use benchmark, in particular comparisons like terminalbench 4.0.

[guregodevo] Actually we tried Cerebras. It caps output at 32K tokens so the 128K reasoning (the author budget) didn't fit. Cerebras speed is real though.

[fedpost] We desperately need to keep local models competitive with the hyper scalers. With anthropic now restricting game reverse engineering I think we're about to cross a Rubicon of censorship.

[mkl / egeres] GVS5H, which this is based on, was discussed here a week ago: https://news.ycombinator.com/item?id=50228167
