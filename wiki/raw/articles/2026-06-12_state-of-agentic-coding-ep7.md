---
title: "State of Agentic Coding #7 — with Armin and Ben"
created: 2026-06-12
updated: 2026-06-12
author: Armin Ronacher (@mitsuhiko), Ben Vinegar (@bentlegen)
source: YouTube
url: https://www.youtube.com/watch?v=QqtW2q9ftu0
type: talk
duration: 94:31
tags:
  - coding-agents
  - agentic-engineering
  - prediction
  - developer-tooling
  - ai-slop
  - ai-safety
  - open-weight
  - youtube
---

# State of Agentic Coding #7 — with Armin and Ben

**Series**: [[concepts/coding-agents/state-of-agentic-coding|State of Agentic Coding]]
**Hosts**: Armin Ronacher ([@mitsuhiko](https://x.com/mitsuhiko)), Ben Vinegar ([@bentlegen](https://x.com/bentlegen))
**Published**: June 12, 2026 | **Duration**: 94:31 | **Views**: 10,377

## Talk Overview

The seventh episode of the State of Agentic Coding series marks roughly one year of agentic coding for both hosts. This episode examines the widening gap between "token haves and have-nots," the industry's incentive to maximize token spend, Bun's Zig-to-Rust rewrite as a landmark slop fork, the maturation of local/open-weight models (DwarfStar 4), and candid year-out predictions on model plateau, dead internet theory, and the concentration of power in AI.

## Core Thesis

One year into agentic coding, the fundamental dynamics haven't changed: models are faster but code is worse, autonomous loops remain impractical for most developers, and the industry's primary incentive (token revenue) is misaligned with user value. The real unlocks have been human-crafted primitives (diffs, trees, libghosty), not autonomous agent loops.

## Key Insights

### Ch1: Introduction (00:00) — One Year of Agentic Coding

- Both hosts reflect on their "anniversary" — Armin's public declaration of agent-first coding in his ["AI Changes Everything"](https://lucumr.pocoo.org/2025/6/4/changes/) blog post (June 2025)
- A year ago, Copilot may have still had more users than Cursor. Claude Code had <0.1% share
- Armin still works mostly from the terminal, not in a "Minority Report" multi-agent UI
- Earendil is building two products: **Lefos** (personal agent) and **Pi** (coding agent)
- Ben runs **Modem** — an AI product manager for non-coding shipping tasks (feedback curation, tickets, release notes)
- Ben's codebase: ~270K lines, 99% AI-generated ("tastefully curated codegen"), with elaborate staging/production/eval pipeline
- Despite testing infrastructure, subtle regressions slip through constantly — "even with a 10 million token context window you would avoid these problems"

### Ch2: Looping & the Token Haves and Have-Nots (07:00)

- **Neither host practices autonomous looping** — surprising to their audience
- Sil Pi's tweet: "I miss when programming was free" — programming is still free but expectations demand paid tools
- At AI Engineer Miami, Max Doebler and Sil Pi also had no agents running — "most people I know do not have agents running 24/7"
- Armin: "I couldn't even fathom coming up with even $100,000 worth of tokens a month"
- Peter Steinberger (OpenClaw): reportedly ~$1.2M/month in raw token cost
- Two worlds emerging: those with massive token budgets operating in loop mode, and everyone else
- Ben's **memory leak anecdote**: Three engineers (Ben, Armin, CTO Mike) spent 24 hours with multiple models trying to debug a Cloudflare Worker OOM — agents produced technically correct but irrelevant hypotheses. The actual cause was a newly imported package that bloated bundle size. "No amount of vibing with the LLM brought us here."
- **AI psychosis refined**: Not a fugue state, but subtle perspective warping — "if you managed to loop a feature in and it gets uptake, you might think you're a genius, but it actually had to do with the previous distribution"
- Boris Cherny (Anthropic) and Peter Steinberger both said: "Your job is not to prompt anymore. Your job is to architect a system that runs loops."

### Ch3: They Really Want You to Buy Tokens (17:59)

- **Inference is margin-positive**: Even with heavily subsidized plans, modeled across the entire user base, inference generates profit
- Armin paying $200/month for an account he barely uses — "this is free money for them"
- **Copilot moved to usage-based pricing**, bundled usage decreased significantly
- **Claude credits system**: `claude-p` (programmatic CLI usage) no longer counts toward subscription — replaced by separate "programmatic agent credits"
- Claude's Ultra mode / sub-agents also draw from credits, not subscription
- **Token spend is the first usage metric that directly correlates with dollars** — unprecedented in the industry. "Never before in our industry have we had a sort of metric that correlates so closely to dollars."
- Comparison to MAU/DAU: those metrics didn't directly translate to revenue. Token spend does
- Armin's conspiracy theory: Human-in-the-loop traces are more valuable for training than machine-generated traces — incentivizes human prompting over autonomous loops
- **Security as forced spend**: AI vulnerability scanners creating a self-perpetuating security racket. "It's an incredible product — it both creates problems and solves the problems you created and you pay both times."
- Sentry prompt injection attack: AI-generated GitHub issues containing prompt injection to replace Sentry with an infected npm package
- FT graph: App releases up tremendously, app usage flat or declining
- Uber reportedly spending $500M on tokens, now imposing $1,500/month limits per developer
- Token spend as "oil company telling you to burn more petrol"

### Ch4: Will Bun Be the First Truly Valuable Slop Fork? (34:34)

- **Bun's Zig-to-Rust rewrite**: Jared (Bun's creator, now at Anthropic) used "Robun" (an agent that acts on GitHub issues) to rewrite Bun from Zig to Rust
- Cloud Code runs on Bun — millions of devices depend on it. This is a slop fork with real distribution
- **Why rewrite Zig to Rust?** Zig's trade-offs (cross-compilation, manual memory management) are optimized for humans, not machines. "All the benefits that Zig has are for humans and not necessarily for machines."
- **Ruby and Zig as "Louisiana French"**: Languages optimized for human creativity but underrepresented in LLM training data. Chad Fowler at RubyConf Austria: prompting AI to solve problems, Ruby never appeared in top language choices
- Ruby's fatal flaw for AI: massive non-local state, runtime metaprogramming — "you need to load everything in the codebase because magic methods could appear anywhere"
- **Zig bans all AI contributions** — even using LLMs to research issues is prohibited. "A brave choice" but potentially fatal for adoption
- Armin considering rewriting his Zig project in Rust: "Why cement myself into Zig when I have Rust as an alternative?"
- **Anthropic's strategic play**: If Bun rewrite proves stable in 3 months, enterprises may use it as leverage to rewrite legacy codebases. "The best way to architect the codebase for agents" could become a consulting revenue stream
- **Chardet slop fork update**: Fully rewritten, 100% AI-generated, zero open issues — "the world is still standing"
- Ben: "We are basically witnessing the elimination of programming languages that serve humans best in favor of languages that serve machines best"

### Ch5: Open-Weight Models & Running Locally (52:30)

- **Local models now at "Claude Code a year ago" quality** — can drive a coding loop, not completely useless
- **DwarfStar 4 (DS4)** by antirez: End-to-end optimized DeepSeek V4 Flash for Apple Silicon
  - One-click install via Pi extension — "almost as convenient as signing up for Anthropic"
  - Prefill: ~450 tokens/sec, generation: ~25-26 tokens/sec
  - Performance maintained until ~80% context fill
  - 96GB memory footprint (2-bit quantization) — enough parameters for genuine knowledge
  - "The first time I actually felt really convinced that I can use a local model at all for anything serious"
- Armin re-quantized DS4 on a 14" M5 Max — **battery drained from 100% to 2% while fully plugged in** (80W power + battery insufficient)
- Ben's experience with DeepSeek V4 Flash (non-quantized): "This reminds me of what models were like a year ago" — powerful but needs supervision
- **More companies entering open-weight space**: Microsoft ("ethically trained"), Nvidia, Cohere (Command A+, 218B total/25B active, Apache 2.0), Gemma 4
- Investor interest: portfolio companies need open-weight models before they grow large enough to lock in
- Not every company can depend on Anthropic/OpenAI "playing nice" — Anthropic tends to kick out competitors from their ecosystem

### Ch6: Year-Out Predictions (65:32)

- **Armin's predictions**:
  - Every company will pay for tokens within a year, at minimum for security
  - Somewhere in the next 24 months: painful readjustment — "it's 1999 but you don't know if it's '97, '98, or '99"
  - Not everyone will be "Ralph looping" — dark factory won't exist next year
  - Models plateauing: GPT 5.5 didn't feel like a tremendous jump from 5.4. David Kramer at Sentry thinks Opus 4.6 is better than 4.8
  - **RL-targeted regression**: Newer Opus models perform worse on off-trodden paths. "If you're doing something that previously still worked because the reinforcement learning wasn't quite so reinforcing, the older models might actually do better"
  - The hard things haven't changed: "We're just trying to do everything really quick now with way worse code"

- **Ben's predictions**:
  - Won't feel substantively different in a year
  - The Ralph loop wouldn't have fixed the memory leak problem — three humans with agents for 24 hours couldn't find what the CTO found by asking "didn't we have this happen before?"
  - **Dead internet hitting development**: No more Stack Overflow posts, no blog posts about Cloudflare Worker oddities — agents have nothing to index for niche problems

- **Shared skepticism**: Model quality improvements are real but the fundamental workflow (human in terminal, supervised coding) hasn't changed

### Ch7: Dead Internet & Where the Good Software Went (78:01)

- **Dead internet theory is real** and will negatively impact progress
- Pi issue tracker: 90% of issues are agent-generated — "it takes me too long to figure out what's a good agent generated issue versus a trash agent generated issue"
- Armin's thought experiment: "If I were as wealthy as Anthropic, I would be hiring companies to write software without AI" — the only way to generate clean training data
- **Slop Scan project** (Ben): Pins notable open-source projects to pre-AI checkpoints (Jan 1, 2025), compares to known slop repositories, extracts patterns. "The value is strictly in the past."
- **No one writing solutions anymore**: The knowledge corpus that made LLMs good is not being replenished
- **Fast fashion of software**: People build something, don't get adoption, throw it away, find next flash-in-the-pan
- **Primitives > AI coding**: The real unlocks are diffs.com, trees, libghosty, canvas/trawl — "the primitives are the bigger unlock to what's possible than the AI coding"
- LLMs are "extensively driven" toward not using dependencies — because dependencies consume tokens
- Ben: "I've seen no evidence of anybody building some really great library with just an LLM in the loop. It's people with taste with people in the loop."
- **Three-column agent harness multiplexer**: Every app looks the same — tree view left, agent middle, diffs right. Built on the same handful of human-written primitives

### Ch8: Open Source, Copyright & the Concentration of Power (92:05)

- Model providers may change licensing: code created by their LLMs becomes their copyright, users get a license
- **Concentration of power**: Only US and China have significant model labs. After that: UK (DeepMind/Google), France (Mistral), Canada (Cohere) — "that's it"
- Even within countries that have labs, it's "small" — Mistral is tiny compared to US labs
- Ben: "We think about concentration of power in companies, but actually if you step out it's incredibly concentrated within one country"
- Google's memory efficiency discovery could have "profound effects" — one breakthrough could change the game
- Ben's prediction: "One tremendous discovery will happen in a year. I have no idea what it is."

## Notable Quotes

> "It's an incredible product — it both creates problems and solves the problems you created and you pay both times." — Armin on AI security tools

> "We are basically witnessing the elimination of programming languages that serve humans best." — Ben

> "I couldn't even fathom coming up with even $100,000 worth of tokens a month. Like it's just I don't even know how I would spend it." — Armin

> "Never before in our industry have we had a sort of metric that correlates so closely to dollars." — Ben on token spend

> "The first time I had that experience of actually feeling really convinced that I can use a local model at all for anything serious." — Armin on DwarfStar 4

> "No amount of vibing with the LLM brought us here. We didn't use our brains." — Ben on the memory leak debugging failure

> "If I were as wealthy as Anthropic, I would be hiring companies to write software without AI." — Armin

> "I've seen no evidence of anybody building some really great library with just an LLM in the loop. It's people with taste." — Ben

> "I miss when programming was free." — Sil Pi (quoted by Ben)

## Connection to Wiki Concepts

- [[concepts/coding-agents/state-of-agentic-coding]] — Series overview
- [[concepts/slop-fork]] — Bun Zig→Rust rewrite as the most significant slop fork yet
- [[concepts/ai-slop]] — Dead internet, training data degradation, 90% agent-generated issues
- [[concepts/context-engineering/context-management|Context Management]] — 10M token windows still insufficient
- [[concepts/coding-agents/ai-coding-agent-criticism]] — Model plateau, RL-targeted regression, loop skepticism
- [[concepts/harness-engineering]] — Pi vs Claude Code feature divergence
- [[concepts/ai-generated-issues-in-oss]] — Pi tracker: 90% agent-generated
- [[concepts/agent-first-design]] — Language elimination (Ruby, Zig) in favor of machine-friendly languages
- [[concepts/ds4-deepseek-flash-metal]] — DwarfStar 4 local inference
- [[entities/armin-ronacher]] — Host, Earendil/Pi/Lefos
- [[entities/ben-vinegar]] — Co-host, Modem
- [[entities/openclaw]] — Peter's $1.2M/month token spend, looping philosophy
- [[entities/antirez-com]] — DwarfStar 4 creator
- [[entities/pi]] — Coding agent, extension ecosystem
- [[entities/cursor]] — Context for model wars
- [[entities/cloudflare]] — Worker memory limits, "forbidden stack" (Vercel+CF)
