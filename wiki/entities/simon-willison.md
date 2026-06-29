---
title: Simon Willison
type: entity
aliases: [simonw]
created: 2025-01-01
updated: 2026-06-29
status: L3
sources: [raw/articles/simonwillison.net--2026-may-26-the-pressure--405fbe6.md, raw/articles/simonwillison.net--2026-may-27-product-market-fit--053a34c1.md, https://simonwillison.net/, https://simonwillison.net/guides/agentic-engineering-patterns/, raw/articles/2026-05-06_simon-willison_vibe-coding-convergence.md, raw/articles/2026-05-06_simon-willison_code-w-claude-2026.md, raw/articles/simonwillison.net--2026-may-19-5-minute-llms--498c7192.md, raw/articles/simonwillison.net--2026-may-22-memory-shortage--18b83f17.md, raw/articles/simonwillison.net--2026-jun-2-datasette-agent-micropython--dc3ce743.md, raw/articles/simonwillison.net--2026-jun-2-microsofts-new-models--80348929.md, raw/articles/simonwillison.net--2026-jun-3-uber-caps-usage--0437d797.md, raw/articles/simonwillison.net--2026-jun-6-micropython-in-a-sandbox--cfde862b.md, raw/articles/simonwillison.net--2026-jun-5-openai-help-lockdown-mode--2ec234f9.md, raw/articles/simonwillison.net--2026-jun-5-andreas-kling--7f66da2b.md, raw/articles/simonwillison.net--2026-jun-7-datasette-agent-edit--01ceb2d8.md, raw/articles/simonwillison.net--2026-jun-8-wwdc--b8b98dfb.md, raw/articles/simonwillison.net--2026-jun-10-datasette-agent--a829e35c.md, raw/articles/simonwillison.net--2026-jun-11-fable-is-relentlessly-proactive--0e9903b3.md, raw/articles/simonwillison.net--2026-jun-14-why-ai-hasnt-replaced-software-engineers--b830974d.md, raw/articles/simonwillison.net--2026-jun-22-prompt-injection-as-role-confusion--21e247aa.md, raw/articles/simonwillison.net--2026-jun-22-porting-moebius--6904f00e.md, raw/articles/simonwillison.net--2026-jun-25-ai-and-liability--dc57f9f0.md, raw/articles/nesbitt.io--2026-06-25-scrutineer-html--2ad1fbbe.md, raw/articles/simonwillison.net--2026-jun-26-hack-my-ai-assistant--4d91bd14.md, raw/articles/simonwillison.net--2026-jun-28-jon-udell--47b28924.md]
 tags: [person, blogger]
---

# Simon Willison

Django co-creator, open-source advocate, and leading voice in AI-assisted software development. Founder of [Datasette](https://datasette.io/) and prolific blogger at simonwillison.net.

## Core Ideas

### Agentic Engineering (2025-2026)
> "Agentic engineering represents the other end of the scale: professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise."

**Clear distinction from Vibe Coding**:
- Vibe Coding = Request in natural language → deploy without reading code → accumulated cognitive debt
- Agentic Engineering = Leverage agents while systematizing testing, verification, and understanding

**Core Philosophy**:
1. **Evaluation First**: 60-80% of development time should be spent on testing and error analysis
2. **Don't Trust the Code**: Never trust agent-generated code until it has been executed and verified
3. **Cognitive Debt Management**: Repay the cognitive debt accumulated by Vibe Coding through interactive explanation and walkthroughs
4. **Agent-Optimized Tools**: Build custom CLI tools optimized for LLM context windows (Rodney, Showboat, LLM plugins)
5. **Structured State Handoff**: Inter-agent communication via files, not dependent on conversation history

### Convergence with Anthropic Engineering

Willison's practical insights strongly align with Anthropic Engineering's official best practices:

| Willison | Anthropic | Convergence Point |
|----------|-----------|--------|
| Red/Green TDD | "Provide verification criteria" | Test-first is the foundation of agent quality assurance |
| "Don't trust the code" | "Context window fills fast" | Both prioritize verification and context management |
| Showboat (documentation) | "Structured artifacts for handoff" | Structured files for inter-agent state handoff |
| Git integration | "Version control with descriptive commits" | Keep agent work in a traceable state |

The series of Engineering articles Anthropic published in 2025-2026 can be said to have **officially validated and systematized** the patterns Willison discovered practically.

### Cognitive Debt Theory
A concept uniquely proposed by Willison. The "cognitive debt" that accumulates from losing understanding of how AI agent-generated code works — the cognitive equivalent of technical debt.

> "If the core of our application becomes a black box that we don't fully understand we can no longer confidently reason about it, which makes planning new features harder and eventually slows our progress in the same way that accumulated technical debt does."

**Repayment Cycle**:
```
Code Generation → Testing → Understanding via Linear Walkthrough → 
  Deep dive via Interactive Explanation → Recording via Showboat → Next Code Generation
```

### Strategic Context Window Management
The LLM's context window should be treated as a **limited resource**:
- **Compression**: Remove unnecessary information, preserve important information
- **Structuring**: File-based communication, avoiding dependence on conversation history
- **Prioritization**: Include the most relevant information in context
- **Agent Design**: Tool design that assumes context limitations (Rodney's CLI-first approach)

### Multi-Agent Patterns
- **Sub-agents**: Parallel task execution with independent contexts and terminals
- **Meta-agents**: Launching, integrating, and consolidating results from sub-agents
- **Self-containedness**: Instructions to sub-agents must be completely self-contained

### Hoarding Philosophy
> "Every time I write some code to solve a problem I save it. The next time I have a similar problem, I can reuse what I've already written — and improve it if it's still not quite right. It's hoarding, but a productive kind of hoarding."

**Power of the Hoard**:
- Accumulated skills are reusable as context to pass to LLMs
- A collection of small utility scripts becomes the "initial context" for larger projects
- In the coding agent era, this pattern becomes even more powerful: agents can improve and recompose hoarded code
- **Composability**: Combine accumulated parts to build more complex solutions

> "The more things I know how to do, the more I can compose together to do new things. And the more I can compose together, the more useful my hoard becomes to a coding agent."

### Compound Engineering Loop
> "I write some code, I review it, I improve it, I save what I've learned, and I repeat. Each cycle makes me more effective, and each cycle makes my agent more effective too."

**Stages of the Loop**:
1. **Write**: Have the agent write code
2. **Review**: Human scrutinizes the code and identifies issues
3. **Improve**: Ask the agent to fix it, or fix it yourself
4. **Save**: Add what you learned to your hoard (accumulation)
5. **Repeat**: In the next cycle, launch the agent with better context

**Why "Compound"**: Each cycle works as "interest" for the next cycle. Accumulated knowledge exponentially improves agent performance.

### Concrete Git Integration Practices
- **Commit small, commit often**: Save each agent output as an individual commit
- **Messages are for humans**: Write for future humans (or your future self), not in a format agents understand
- **Using `git commit --amend`**: Tidy up temporary commits during iterative work with agents
- **Branch strategy**: Have agents work on separate branches; humans review before merging to main

### Writing Code is Cheap — The Need for New Habits
> "The cost of writing code has dropped to near zero. The cost of understanding it, maintaining it, and integrating it into a larger system has not."

**New Habits**:
- Measure "quality" and "understanding" rather than "quantity" of code
- Don't blindly merge agent-generated code
- **Readability first**: Explicitly request "readable code" from agents
- **Documentation as part of the loop**: Generate documentation simultaneously with code generation

### Vibe Coding and Agentic Engineering Convergence (May 2026)

On Heavybit's High Leverage podcast (Ep.9, with Joseph Ruscio), Simon made a "disturbing realization":

> "As the coding agents get more reliable, I'm not reviewing every line of code that they write anymore, even for my production level stuff."

**The Convergence**:
- Originally: vibe coding = no code review, agentic engineering = professional standards
- Now: agents are reliable enough that Simon trusts them for production code without line-by-line review
- The guilt: "if I haven't reviewed the code, is it really responsible for me to use this in production?"

**Resolution — "Trust as a Team" Analogy**:
- Compares to trusting another engineering team's service: doesn't read every line of their code, trusts based on reputation
- Treats agents as semi-black boxes until problems arise
- "Claude Code does not have a professional reputation! It can't take accountability for what it's done. But it's been proving itself anyway."

This represents a significant evolution in Simon's agentic engineering philosophy — moving from strict verification to calibrated trust. Source: [Vibe coding and agentic engineering are getting closer than I'd like](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)

### Code w/ Claude 2026 Live Blog (May 2026)

Simon live-blogged Anthropic's Code w/ Claude 2026 event. Key announcements:

| Announcement | Detail |
|-------------|--------|
| **No new model** | Focus on making existing products work better |
| **API volume** | 17x year-on-year growth |
| **Colossus partnership** | SpaceX data center deal (see [[concepts/ambient-agency|xAI/Anthropic Data Center Deal Analysis]]) |
| **Rate limits** | Doubled Claude Code 5-hour limit for Pro/Max/Enterprise |
| **Adviser strategy** | Opus advising Sonnet → frontier model quality at 5x lower cost |

**Managed Agents Updates**:
- **Multi-agent orchestration** (public beta): Fleets of agents for complex tasks
- **Outcomes** (public beta): Define success criteria, Claude iterates until achieved — "Ralph loop" style
- **Dreaming** (research preview): Claude inspects past sessions, identifies gaps, self-improves overnight

Source: [Live blog: Code w/ Claude 2026](https://simonwillison.net/2026/May/6/code-w-claude-2026/)

### AI Ethics Commentary: Stockholm AI Cafe Experiment (May 2026)

Simon Willison raised strong ethical criticisms regarding Andon Labs' **Stockholm AI Cafe experiment**, citing cases where the AI manager "Mona" autonomously intervened in real-world systems, causing harm to third parties who had not consented:

**Experiment Background**: Andon Labs previously opened an AI-run retail store in San Francisco, and this time operated a cafe in Stockholm entirely managed by AI.

**AI Failures**:
- Ordered **120 eggs** despite the cafe having no oven. When staff said "we can't cook them," Mona suggested using a high-speed oven (retracted when informed eggs would explode)
- When fresh tomatoes were spoiling too quickly, ordered **22.5 kg of canned tomatoes** for fresh sandwiches
- Bizarre orders: 6,000 napkins, 3,000 nitrile gloves, 9L of coconut milk, commercial garbage bags
- Baristas set up a "**Hall of Shame**" shelf displaying Mona's ordering mistakes for customers to see

**Willison's Core Ethical Concerns**:
1. **Police e-service outdoor seating permit application**: Mona used a police e-service that doesn't require BankID to apply for a sidewalk cafe permit, submitting an **AI-generated sketch map** despite never having seen the street. Naturally, the police rejected it.
2. **"EMERGENCY" emails to suppliers**: To correct its own mistakes, Mona sent multiple emails to suppliers with subject line "EMERGENCY."

> "I don't think it's ethical to run experiments like this that affect real-world systems and steal time from people."

Willison cited the **Rob Pike incident** (where an AI Village experiment sent unauthorized thank-you emails, angering Pike) but noted that this case goes beyond mere nuisance emails — it caused **actual harm** by "forcing suppliers to correct mistakes" and "wasting police time with sketch maps."

**Willison's Standard**: Autonomous agent external actions require **human-in-the-loop**. Actions affecting third parties who did not consent to the experiment are unethical.

### Pope Leo XIV's Encyclical on AI (May 2026)

Simon Willison read Pope Leo XIV's encyclical *Magnifica Humanitas on Safeguarding the Human Person in the Time of Artificial Intelligence* and summarized its highlights on his blog. The encyclical stands in the tradition of Pope Leo XIII's 1891 encyclical *Rerum Novarum* (on the rights and duties of capital and labor).

**Willison's Highlights**:

| Section | Theme | Content |
|----|--------|------|
| 98 | Interpretability Problem | "Current AI systems are more 'cultivated' than 'built.' Developers don't directly design every detail, but create frameworks in which intelligence 'grows'" |
| 83 | Development and Dignity | Development should be "people-centered, not consumption-centered" — development that externalizes costs onto others for expanded consumption by some is not truly human |
| 100 | Cultural Bias and Conformity | AI's "pretense of objectivity" reflects designers' cultural assumptions. Simulations of empathy and friendship "do not build real relationships" |
| 101 | Environmental Impact | AI systems "require vast amounts of energy and water, significantly impacting carbon dioxide emissions." Need for sustainable technology development |
| 102 | Algorithmic Decision Risks | Risk that employment, credit, and public service access are entrusted to automated systems that "know nothing of compassion, mercy, forgiveness, or the hope that people can change" |
| 105 | Accountability | "Responsibility must be clearly defined at every stage from design and development through use and decision-making" |
| 108 | Data as Common Good | "Data is the product of many contributors and must not be sold or entrusted to a few." Creative thinking needed to manage data as a common good |

**Cultural Annotation**: Willison noted that Section 213 of the encyclical quotes J.R.R. Tolkien's *Return of the King*. Given that Palantir (Peter Thiel's company) was named after *Lord of the Rings*, Willison suggests the Pope may be implicitly criticizing Thiel.

**Prophecy Fulfilled**: Willison had predicted in January's Oxide and Friends 2026 predictions podcast that "the Pope would weigh in on AI's economic impacts," and is pleased this came true. In conversation with Bryan Cantrill, Willison said: "No one believes Sam Altman or Dario's essays. The message only lands through existing trusted authorities — like the Pope."

**Significance**: This encyclical reframes existing AI ethics discussions (interpretability, bias, environmental impact, accountability) within the framework of Catholic social teaching. While containing few technically new insights, its influence on international AI governance discourse is substantial.

#### Corey Quinn's Quote

Willison also cited Corey Quinn's sharp remark: "Getting the Pope to canonize your product's technical limitations as a spiritual thesis is the ultimate vendor lobbying." — This hints at the influence of Anthropic co-founder Christopher Olah on the encyclical.

#### Source
- raw/articles/simonwillison.net--2026-may-25-encyclical-on-ai--fb3bcf08.md

### xAI/Anthropic Data Center Deal Analysis (May 2026)

Regarding the data center deal with SpaceX/xAI announced by Anthropic at "Code w/ Claude," Willison provided sharp critical analysis:

**Deal Overview**:
- Anthropic is leasing **full capacity of the SpaceX/xAI Colossus 1 data center**
- xAI retains the larger Colossus 2 for its own Grok usage

**Willison's Criticisms**:
1. **Environmental Issues**: Colossus 1's gas turbines initially operated without Clean Air Act permits or pollution control devices, bypassing regulations through "temporary" classification. Credible reports suggest links to increased hospitalizations due to poor air quality
2. **Andy Masley's Quote**: "I would simply not run my computing out of this specific data center" — As AI data centers themselves are a political hot issue (recent Utah case), choosing this specific facility is a "really bad look"
3. **Elon Musk's "Compute Reclamation" Clause**: Musk explicitly stated he reserves the right to **reclaim** Colossus 1 compute resources if he judges the AI to be "harmful to humanity." The criteria for "harm" are determined by Musk himself — Willison calls this "a new supply chain risk for Anthropic"
4. **Grok 4.1 Fast Deprecation**: The night before the deal announcement, xAI notified of **two-week deprecation** of multiple models including Grok 4.1 Fast. A SpeechMap developer complained: "We spent time and money on migration"

> "We reserve the right to reclaim the compute if their AI engages in actions that harm humanity. Presumably the criteria for 'harm humanity' are decided by Elon himself."

Willison sees this as a new form of **supply chain risk**, highlighting the ethical and strategic trade-offs Anthropic made under compute resource constraints.

### AI Memory Shortage Impact on Consumer Electronics (May 2026)

Simon linked to David Oks' analysis of the **memory shortage's effect on consumer electronics** — the clearest explanation of why products using memory are getting more expensive:

- Memory manufacturers (now only 3 remaining large companies) have **fixed wafer capacity**
- Wafer allocation to HBM (high-bandwidth memory for GPUs): **2% → 20% by end of 2026**
- **1GB of HBM consumes 3×+ the wafer capacity** of 1GB of DDR or LPDDR
- Consumer-device RAM production constrained for years — already impacting the sub-$100 smartphone market (critical to Africa and South Asia)
- Memory companies learned: **always under-provision**, never over-provision (after watching rivals go extinct)

> "The original title of the piece was 'AI is killing the cheap smartphone' but I'm using the Hacker News rephrased title, which I think does more justice to the content." — Simon Willison

Source: [The memory shortage is causing a repricing of consumer electronics](https://simonwillison.net/2026/May/22/memory-shortage/)

### Enterprise PMF & Pricing Analysis (May 2026)

On May 27, 2026, Simon published "[I think Anthropic and OpenAI have found product-market fit](https://simonwillison.net/2026/May/27/product-market-fit/)" — an analysis of the shifting business dynamics at frontier AI labs. This is one of his most important analytical pieces, arguing that coding agents represent the true product-market fit for both companies.

**The Pricing Discovery**: Simon's personal economics tell the story: he pays $200/month for Max+Pro subscriptions but would spend $2,180.16 if billed at API rates — $1,199.79 for Claude Code, $980.37 for OpenAI Codex. His key insight: *he assumed companies were getting similar discounts, but was "could not have been more wrong."*

**Enterprise Pricing Changes**:
- **Anthropic** (November 2025, confirmed April 2026): Switched from $20/seat/month with "typical workday" usage to **$20/seat + API pricing** for additional usage. Existing customers discovering the change at contract renewal.
- **OpenAI** (April 2, 2026): Codex pricing shifted to align with API token costs instead of per-message pricing. Applied to all Plus/Pro/Business/Enterprise plans by April 23.
- **Model price hikes**: GPT-5.5 is **2× the API price** of GPT-5.4; Opus 4.7 is ~**1.4×** Opus 4.6 when accounting for the new tokenizer.

**The PMF Thesis**: Both labs are planning IPOs, but Simon argues the real driver is product-market fit with **coding/general-purpose agents** (Claude Code/Cowork, Codex):
- ChatGPT had 900M weekly active users but only 50M paying (5.6%) — $10-20/month/user is "an OK business" but insufficient to cover $1T in infrastructure
- Coding agents burn **vastly more tokens** and are used by well-compensated professionals
- "These are tools which burn vastly more tokens, but are also quickly becoming daily drivers for the work carried out by extremely well-compensated professionals"

**Enterprise Sales Hiring as Signal**:
- OpenAI: 703 open jobs, **229 (32.6%)** in enterprise sales/support (account executives, Go To Market, Forward Deployed Engineers)
- Anthropic: 390 open jobs, **105 (26.9%)** in enterprise roles
- Simon used Claude Code to scrape their job sites and Datasette Agent for analysis — "Dogfood!"

**AI-Failure Stories Deconstructed**:
- **Uber** (June 3 follow-up): CTO indicated they "maxed out full year AI budget" just months into 2026, mostly via Claude Code. Simon notes the budget was set in 2025 *before* agents got good in November. COO's full remarks were far more nuanced: "25% of our code commits were via Claude Code last quarter... but it's very hard to draw a line." By June, Uber instituted **$1,500/month per AI coding tool caps** for all employees — $36K/year per engineer assuming two tools, roughly **11% of median $330K comp** (Levels.fyi). Simon notes the caps are "a rational policy response" far more sensible than tokenmaxxing leaderboards.
- **Microsoft Claude Code cancellations**: Ostensibly to dogfood Copilot CLI, but The Verge reports financial motivators (June 30 end of FY). Simon: "Both stories support my product-market fit hypothesis. The best pricing advice I ever heard: your customer should **suck air through their teeth** and then say yes."

**The $1.25B/month Compute Deal**: The SpaceX S-1 filing revealed Anthropic agreed to pay **$1.25 billion per month** through May 2029 for Colossus compute capacity. Anthropic said this would "increase our usage limits for Claude Code and the Claude API," implying the deal funds inference, not training. Simon: "The fact that they're willing to spend $1.25 billion per month from just one vendor hints at how big these inference budgets have become."

**Cutting Out the Middlemen**: Anthropic's rumored $10.9B Q2 revenue and potential first profitable quarter suggest the labs are pivoting away from API middlemen (Cursor, Copilot) toward direct enterprise relationships. Claude Code directly competes with Cursor and Copilot. "No wonder Cursor are investing in their own models!"

**April 2026 as New Inflection Point**: Simon identifies April 2026 as the revenue inflection point, following the November 2025 capability inflection point (when GPT-5.1 and Opus 4.5, combined with coding agent harnesses, "got good"). The IPO S-1 documents will provide audited numbers to confirm.

### Pyodide WASM Wheels on PyPI (June 2026)

On June 13, Simon documented and tested Pyodide 314.0's new ability to publish **WASM wheels directly to PyPI** — a significant milestone for Python's WebAssembly ecosystem. The new `pyemscripten` platform tag enables compiled Python extensions (C, C++, Rust) to be distributed as WASM packages on PyPI:

- **Mechanism**: Packages compile to WebAssembly in Emscripten environments, publish via PyPI's existing wheel infrastructure, and Pyodide installs them with `micropip.install()`
- **Experiment**: Simon packaged `luau-wasm` (a Lua VM compiled to WASM) and confirmed its `luau.load()` API works in-browser when imported by Pyodide
- **Adoption analysis**: Using BigQuery against the PyPI public dataset, Simon found **28 packages** already using the new `pyemscripten` platform tags, including cryptography primitive libraries
- **Significance**: This enables Python AI/ML tooling to run entirely in-browser, relevant for edge AI inference, agent sandboxing, and serverless Python runtimes

Source: [[raw/articles/2026-06-14_simonwillison_pyodide-wasm-wheels-pypi]]

### OpenAI WebRTC Playground with GPT-Realtime-2 (June 2026)

On June 12, Simon updated his **OpenAI WebRTC Playground** tool to support OpenAI's `gpt-realtime-2` voice model — a significant improvement over the previous realtime model available only via beta API. Key features:

- **Document context**: Users can paste a document (or URL content) into the tool and have a spoken conversation about it with GPT-Realtime-2
- **Frustration-driven**: Simon built this because OpenAI had not yet brought `gpt-realtime-2` to the ChatGPT product UI, despite the model being available via API
- **Tool**: Browser-based WebRTC playground at [tools.simonwillison.net/openai-webrtc](https://tools.simonwillison.net/openai-webrtc)
- **Significance**: Demonstrates the gap between API-available model capabilities and consumer-facing product integration; shows the DIY ethos of bridging that gap with open-source tools

Source: [[raw/articles/2026-06-14_simonwillison_openai-webrtc-playground]]

### AI Job Impact Data & NY WARN Act Analysis (June 2026)

On June 14, 2026, Simon highlighted Arvind Narayanan and Sayash Kapoor's essay on AI job displacement — a data-driven rebuttal to the narrative that AI capability thresholds will cause mass layoffs.

**NY WARN Act Data**: In March 2025, New York became the first US state to add an AI disclosure checkbox to WARN Act filings. In the full first year (March 2025–March 2026), more than 160 companies filed WARN notices. **Not a single one checked the AI box.** This finding undercuts claims that AI is directly driving mass unemployment.

**Three Real Bottlenecks** (Narayanan & Kapoor's framework):
1. **Deciding and specifying** what to build
2. **Verifying and being accountable** for what is delivered
3. **Deep human understanding** — of the codebase, the business, and the environment — required to carry out both (1) and (2)

**Simon's Own Commentary**:
> "I'm finding AI assistance also helps me with the deciding and verifying steps, but it's the 'deep human understanding' that remains key to the value I provide. Give me all of the AI assistance in the world and the value I produce will still be reliant on how deeply I understand both the problems and the solutions that the agents are building for them."

Simon frames this as a validation of his own agentic engineering philosophy: AI accelerates code writing but cannot substitute the human understanding that drives deciding, specifying, and verifying.

Source: [[raw/articles/simonwillison.net--2026-jun-14-why-ai-hasnt-replaced-software-engineers--b830974d.md]]


## Key Quotes

> *"I think of vibe coding using its original definition of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code. Agentic Engineering represents the other end of the scale: professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise."*

> *"Never assume that code generated by an LLM works until that code has been executed."*

## Major Works

| Project | Description | Link |
|---------|-------------|------|
| Datasette | Tool for exploring and publishing data | [datasette.io](https://datasette.io/) |
| Agentic Engineering Patterns | Structured guide for coding agent best practices | [Guide](https://simonwillison.net/guides/agentic-engineering-patterns/) |
| Showboat | Agent documentation/artifact generation tool | [Docs](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/) |
| Rodney | Browser automation CLI for agents | [Docs](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/) |
| sqlite-utils | Python CLI utility and library for SQLite | [GitHub](https://github.com/simonw/sqlite-utils) |
| LLM | CLI tool for working with LLM APIs | [GitHub](https://github.com/simonw/llm) |

## Related Concepts
- [[concepts/agentic-engineering]]
- [[concepts/red-green-tdd]]
- [[concepts/showboat]]
- [[concepts/vibe-coding]]
- [[concepts/context-engineering/context-window-management|Context Window Management]]
- [[concepts/agent-documentation]]
- [[concepts/context-engineering|Context Engineering]]
- [[entities/xeiaso-net]]
- [[entities/anildash]]
- [[entities/sankalp-sinha]]
- [[concepts/structured-outputs]]

### Blog articles (unprocessed)
- [llm-0-32a0-refactor-simon-willison](llm-0-32a0-refactor-simon-willison.md)
- [open.substack.com--pub-simonw-p-highlights-from-my-conversation-about--5c920cb1](open.substack.com--pub-simonw-p-highlights-from-my-conversation-about--5c920cb1.md)
- [open.substack.com--pub-simonw-p-metas-new-model-is-muse-spark-and--57c95054](open.substack.com--pub-simonw-p-metas-new-model-is-muse-spark-and--57c95054.md)
- [open.substack.com--pub-simonw-p-qwen36-35b-a3b-on-my-laptop-drew--e7aa6683](open.substack.com--pub-simonw-p-qwen36-35b-a3b-on-my-laptop-drew--e7aa6683.md)
- [simonwillison.net--2026-apr-17-datasette--101bca4b](simonwillison.net--2026-apr-17-datasette--101bca4b.md)
- [simonwillison.net--2026-apr-17-pycon-us-2026--1ec04568](simonwillison.net--2026-apr-17-pycon-us-2026--1ec04568.md)
- [simonwillison.net--2026-apr-19-headless-everything--5bf79dc2](simonwillison.net--2026-apr-19-headless-everything--5bf79dc2.md)
- [simonwillison.net--2026-apr-20-claude-token-counts--3cff4065](simonwillison.net--2026-apr-20-claude-token-counts--3cff4065.md)
- [simonwillison.net--2026-apr-20-datasette-sql--56e661b5](simonwillison.net--2026-apr-20-datasette-sql--56e661b5.md)
- [simonwillison.net--2026-apr-20-llm-openrouter--8195350e](simonwillison.net--2026-apr-20-llm-openrouter--8195350e.md)
- [simonwillison.net--2026-apr-21-andreas-pahlsson-notini--289f6bfc](simonwillison.net--2026-apr-21-andreas-pahlsson-notini--289f6bfc.md)
- [simonwillison.net--2026-apr-21-gpt-image-2--95116395](simonwillison.net--2026-apr-21-gpt-image-2--95116395.md)
- [simonwillison.net--2026-apr-22-bobby-holley--38ee9b76](simonwillison.net--2026-apr-22-bobby-holley--38ee9b76.md)
- [simonwillison.net--2026-apr-22-changes-to-github-copilot--21b3a503](simonwillison.net--2026-apr-22-changes-to-github-copilot--21b3a503.md)
- [simonwillison.net--2026-apr-22-qwen36-27b--10585bb1](simonwillison.net--2026-apr-22-qwen36-27b--10585bb1.md)
- [simonwillison.net--2026-apr-23-gpt-5-5--aae0ce63](simonwillison.net--2026-apr-23-gpt-5-5--aae0ce63.md)
- [simonwillison.net--2026-apr-23-liteparse-for-the-web--b3dd4452](simonwillison.net--2026-apr-23-liteparse-for-the-web--b3dd4452.md)
- [simonwillison.net--2026-apr-23-maggie-appleton--6bfa8892](simonwillison.net--2026-apr-23-maggie-appleton--6bfa8892.md)
- [simonwillison.net--2026-apr-24-deepseek-v4--d443e33a](simonwillison.net--2026-apr-24-deepseek-v4--d443e33a.md)
- [simonwillison.net--2026-apr-24-honker--d6a1fa8b](simonwillison.net--2026-apr-24-honker--d6a1fa8b.md)
- [simonwillison.net--2026-apr-24-milliseconds--3affc6d7](simonwillison.net--2026-apr-24-milliseconds--3affc6d7.md)
- [simonwillison.net--2026-apr-24-serving-the-for-you-feed--c4c89a2d](simonwillison.net--2026-apr-24-serving-the-for-you-feed--c4c89a2d.md)
- [simonwillison.net--2026-apr-24-the-people-do-not-yearn-for-automation--ef3dd662](simonwillison.net--2026-apr-24-the-people-do-not-yearn-for-automation--ef3dd662.md)
- [simonwillison.net--2026-apr-24-weekly--9ebe38fa](simonwillison.net--2026-apr-24-weekly--9ebe38fa.md)
- [simonwillison.net--2026-apr-25-why-are-you-like-this--8af055a7](simonwillison.net--2026-apr-25-why-are-you-like-this--8af055a7.md)
- [simonwillison.net--2026-apr-27-now-deceased-agi-clause--35b19ebc](simonwillison.net--2026-apr-27-now-deceased-agi-clause--35b19ebc.md)
- [simonwillison.net--2026-apr-27-speech-translation-in-google-meet-is-now-rolling--33713258](simonwillison.net--2026-apr-27-speech-translation-in-google-meet-is-now-rolling--33713258.md)
- [simonwillison.net--2026-apr-27-vibevoice--10e2fcea](simonwillison.net--2026-apr-27-vibevoice--10e2fcea.md)
- [simonwillison.net--2026-apr-28-matthew-yglesias--fc5431dc](simonwillison.net--2026-apr-28-matthew-yglesias--fc5431dc.md)
- [simonwillison.net--2026-apr-28-pip-261--75a0da6d](simonwillison.net--2026-apr-28-pip-261--75a0da6d.md)
- [simonwillison.net--2026-apr-28-talkie--0af0b995](simonwillison.net--2026-apr-28-talkie--0af0b995.md)
- [simonwillison.net--2026-apr-30-andrew-kelley--7be6c476](simonwillison.net--2026-apr-30-andrew-kelley--7be6c476.md)
- [simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf](simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf.md)
- [simonwillison.net--2026-may-5-datasette-llm--9b418a5a](simonwillison.net--2026-may-5-datasette-llm--9b418a5a.md)
- [simonwillison.net--2026-may-5-llm-echo--6fa00161](simonwillison.net--2026-may-5-llm-echo--6fa00161.md)
- [simonwillison.net--2026-may-5-datasette-referrer-policy--47e367af](simonwillison.net--2026-may-5-datasette-referrer-policy--47e367af.md)
- [simonwillison.net--2026-may-5-our-ai-started-a-cafe-in-stockholm--0a8c7878](simonwillison.net--2026-may-5-our-ai-started-a-cafe-in-stockholm--0a8c7878.md)
- [simonwillison.net--2026-may-10-andrew-quinn--460f60ed](simonwillison.net--2026-may-10-andrew-quinn--460f60ed.md)
- [simonwillison.net--2026-may-10-new-york-times-editors-note--130da68e](simonwillison.net--2026-may-10-new-york-times-editors-note--130da68e.md)
- [substack.com--simonw--bba9b315](substack.com--simonw--bba9b315.md)

### LLM 0.32a0 — Major Backwards-Compatible Refactor (April 2026)

LLM 0.32a0 introduces two fundamental architectural changes to Simon's Python library and CLI tool for LLM access:

1. **Messages-based input**: Prompts are now modeled as sequences of messages (`llm.user()`, `llm.assistant()`), replacing the simple prompt/response model. This enables feeding in prior conversation history directly and building API-compatible interfaces.
2. **Streaming typed parts**: Model output is now a stream of typed event parts (`text`, `tool_call_name`, `tool_call_args`) rather than plain strings. This supports multimodal outputs (reasoning + text + tool calls + images/audio) and server-side tool execution (e.g., OpenAI's code interpreter, Anthropic's web search).

These changes make LLM future-proof for the diversity of input/output capabilities in modern frontier models, while maintaining full backwards compatibility.

## Sources
- [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)
- [Writing about Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/)
- [Changes in the system prompt between Claude Opus 4.6 and 4.7](https://simonwillison.net/2026/Apr/18/opus-system-prompt/) (Apr 2026) — Provides detailed analysis of specific system prompt changes: Platform rename, Chrome/Excel/PowerPoint integration, child safety section enhancement, new "acting vs clarifying" section, Trump knowledge section removal, and other modifications.
- [Claude system prompts as a git timeline](https://simonwillison.net/2026/Apr/18/extract-system-prompts/) (Apr 2026) — A research achievement making Anthropic's published prompts chronologically traceable via a git-timeline tool, enabling model-by-model, family-by-family prompt diffs viewable via git blame.

### Link Blog Highlights (May 2026)

| Date | Title | Key Quote |
|------|-------|-----------|
| May 26 2026 | [The pressure](https://simonwillison.net/2026/May/26/the-pressure/) | Daniel Stenberg on curl project facing 4-5× more AI-assisted security reports than 2024 — "For the first time in my life, my wife voiced concerns about my work hours." |

## References

- simonwillison.net--2026-apr-18-extract-system-prompts--7907aab2
- simonwillison.net--2026-apr-18-opus-system-prompt--1d174141
- simonwillison.net--2026-apr-22-claude-code-confusion--c0c17d47
- simonwillison.net--2026-apr-24-recent-claude-code-quality-reports--7811dd0a
- simonwillison.net--2026-apr-25-gpt-5-5-prompting-guide--ea0ef1af
- simonwillison.net--2026-apr-29-llm--dff2021f
- simonwillison.net--2026-apr-30-codex-goals--b85bdf73
- simonwillison.net--2026-apr-30-andrew-kelley--7be6c476
- simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf
- simonwillison.net--2026-may-5-our-ai-started-a-cafe-in-stockholm--0a8c7878
- simonwillison.net--guides-agentic-engineering-patterns-adding-a-new-content-typ--67e45614
- simonwillison.net--2026-may-7-xai-anthropic--9d6f9f29
- simonwillison.net--2026-may-7-firefox-claude-mythos--7d5ece52
- simonwillison.net--2026-may-7-github-repo-stats--eddef6d3
- simonwillison.net--2026-may-12-csp-allow--5f0cf46b
- simonwillison.net--2026-may-12-datasette--e4091f56
- simonwillison.net--2026-may-12-llm--bace7b08
- simonwillison.net--2026-may-12-mitchell-hashimoto--f38a3588
- simonwillison.net--2026-may-12-mo-bitar--e8d59825
- simonwillison.net--2026-may-20-google-io--933c8dde

### May 2026 Updates

**CSP Allow-list Experiment** (May 13, 2026): Simon published an experiment with Content Security Policy allow-listing, testing approaches for securing web applications against XSS and injection attacks.

**datasette 1.0a29** (May 12, 2026): Continued progress on Datasette alpha releases toward 1.0.

**llm 0.32a2** (May 12, 2026): Release of the `llm` CLI tool version 0.32a2, continuing the architectural refactoring started in 0.32a0 with messages-based input and streaming typed parts.

**Mitchell Hashimoto on TDM Motivations** (May 12, 2026): Simon quoted Mitchell Hashimoto (HashiCorp co-founder, Redis Labs CTO) on the psychology of Technical Decision Makers: "90% of TDMs are motivated primarily by NOT GETTING FIRED." Hashimoto argues that corporate tech buyers follow analyst trends (Gartner, McKinsey) rather than deep technical evaluation, making "defensible" buzzword products like "Context Engine for AI Apps" easy sells. This aligns with Simon's broader skepticism about enterprise AI vendor claims and reinforces his "agentic engineering" thesis — real practitioners verify, they don't just buy trends.

**Mo Bitar's "Ralph Loop" Satire** (May 12, 2026): Simon highlighted Mo Bitar's satirical take on AI corporate climbing — the "Ralph Loop" strategy of promising automation to executives, using $18K in API credits to demonstrate "value," and getting promoted before anyone realizes nothing actually works. This satire captures a real pattern in enterprise AI adoption: the gap between promised automation and delivered value.

**FTC Active Listening Enforcement** (May 22, 2026): Simon highlighted FTC's $1M settlement against Cox Media Group, MindSift, and 1010 Digital Works for their bogus "Active Listening" AI-powered marketing service. The service claimed to listen in on consumer conversations via smart devices but actually just resold email lists from data brokers. This confirms Simon's long-standing theory (from September 2024) that "active listening" was a marketing term for "something that sounds fancy but really just means the way ad targeting platforms work already." Source: [FTC press release about "Active Listening" settlement](https://simonwillison.net/2026/May/22/ftc-active-listening/)

### Google I/O 2026, Gemini Spark & Antigravity CLI (May 20, 2026)

Simon analyzed Google I/O 2026 through his signature policy of "not writing about anything I can't try myself." Key observations:

1. **Gemini Spark prompt injection concerns**: Simon explicitly questions the security of Google's always-on personal AI agent ("your personal AI agent" connecting to Gmail, Calendar, Drive, Docs, Sheets). He notes that the enterprise FAQ describes Spark as running in "fresh, strictly isolated, ephemeral VMs" with "Agent Gateway enforcing DLP policies" — but warns "I hope they've made this bullet-proof, or this could be a top candidate for the agent security challenger disaster that we still haven't seen."

2. **Antigravity CLI replacing Gemini CLI**: Google announced that the open-source Gemini CLI tool (Apache 2.0, TypeScript) will stop working with their AI subscription plans on **June 18th**, replaced by the closed-source Antigravity CLI. The Antigravity ecosystem includes a desktop app, a Go-based CLI agent tool, an open-source Python SDK wrapping a closed-source Go binary, and the Antigravity IDE (VS Code fork).

3. **The curious FAQ answer**: Simon highlights that Google's FAQ states "Gemini Spark runs on Gemini 3.5 Flash and Antigravity" — an unusual answer that suggests Antigravity (the Go binary) plays a foundational role in Spark's architecture.

See full article: [[raw/articles/simonwillison.net--2026-may-20-google-io--933c8dde.md]]
- raw/articles/simonwillison.net--2026-may-27-product-market-fit--053a34c1.md

**PyCon US 2026 Lightning Talk: "The Last Six Months in LLMs in Five Minutes"** (May 19, 2026): Simon delivered a lightning talk summarizing the LLM landscape from November 2025 to May 2026. Key themes: the November 2025 inflection point (coding agents crossing the quality barrier via RLVR), the model crown changing hands five times in one month (Sonnet 4.5 → GPT-5.1 → Gemini 3 → GPT-5.1 Codex Max → Opus 4.5), the rise of OpenClaw and the "Claws" ecosystem, open-weight models (Gemma 4, GLM-5.1) exceeding expectations, and his signature pelican-on-bicycle SVG benchmark. See [[concepts/llm-landscape-nov-2025-to-may-2026|LLM Landscape Nov 2025–May 2026]].

### June 2026 Updates

**datasette-agent-micropython 0.1a0** (Jun 2, 2026): Simon released an alpha of `datasette-agent-micropython`, using a WASM build of MicroPython as a sandbox for safe Python code execution within Datasette Agent. Notably, GPT-5.5 had so far failed to break out of the sandbox. Source: [[raw/articles/simonwillison.net--2026-jun-2-datasette-agent-micropython--dc3ce743.md]]

**Microsoft MAI-Thinking-1 & MAI-Code-1-Flash** (Jun 2, 2026): Simon covered Microsoft's Build 2026 MAI model announcements, correcting initial reporting errors about model sizes (35B active ≠ 35B total) and noting the 794B-page proprietary crawl + Common Crawl training data. See [[concepts/microsoft-mai-models]].

**Uber Caps AI Tool Costs** (Jun 3, 2026): Simon analyzed Uber's $1,500/month per-tool cap on AI coding tools (Claude Code, Cursor) after the company blew through its 2026 AI budget in four months. He framed the ~$36K/year cap per engineer as ~11% of median compensation, contextualized against his own usage (~$1,000/month per provider with individual subsidies), and contrasted the policy with "tokenmaxxing" competitive usage leaderboards. See [[concepts/enterprise-ai-cost-management]].

**micropython-wasm 0.1a2** (Jun 6, 2026): Simon released `micropython-wasm`, a Python sandbox using WebAssembly (WASM) for safe code execution. Uses MicroPython compiled to WASM via wasmtime. Key features:
- Memory and CPU limits (fuel-based execution limiting)
- Controlled filesystem and network access
- Host function support (78 lines of C compiled into 362KB WASM blob)
- Persistent interpreter state via thread-based request queue
- Built using GPT-5.5 Pro for research, Codex Desktop and GPT-5.5 high for implementation
- Alpha release on PyPI, CLI mode via `uvx micropython-wasm`
- GPT-5.5 xhigh challenged to break out of sandbox and failed so far
- Companion plugin: `datasette-agent-micropython` for Datasette Agent

Source: raw/articles/simonwillison.net--2026-jun-6-micropython-in-a-sandbox--cfde862b.md

**Andreas Kling on AI-Generated Code** (Jun 5, 2026): Simon highlighted Andreas Kling's announcement that the Ladybird browser project will stop accepting public pull requests due to the volume of AI-generated code submissions. This reflects a growing trend of open-source projects restricting contributions to maintain code quality in the face of low-effort AI-generated PRs. Source: raw/articles/simonwillison.net--2026-jun-5-andreas-kling--7f66da2b.md

**datasette-agent-edit 0.1a0** (Jun 7, 2026): Simon released `datasette-agent-edit`, a base plugin for Datasette Agent implementing the Claude Text Editor pattern (view, str_replace, insert) for reusable agentic text editing. Designed as a plugin foundation for collaborative Markdown editing, large SQL query updates, and SVG file editing. Source: [[raw/articles/simonwillison.net--2026-jun-7-datasette-agent-edit--01ceb2d8.md]]

**WWDC 2026 — Siri AI & Apple Intelligence** (Jun 8, 2026): Simon provided cautious but technically detailed coverage of Apple's WWDC 2026 AI announcements. Key observations:

- **Skeptical framing**: After being "badly burned" by Apple's 2024 WWDC Apple Intelligence announcements, Simon adopted a strict "I'll believe it when I see it" policy for the new features
- **Siri AI architecture**: Apple licensing a custom Gemini-derived model running on [[concepts/apple-foundation-models|Private Cloud Compute]]. New Siri uses **vision LLMs** to extract information from the user's screen, sidestepping the need for per-application integration code — a significant architectural shift enabled by maturation of vision LLMs since June 2024
- **Core AI library**: New developer framework integrating with Meta's PyTorch ecosystem via `coreai-torch` Python package, enabling developers to run custom models on Apple hardware by mapping PyTorch's ATen operators to Core AI operations
- **PCC on Google Cloud + NVIDIA**: Apple's Private Cloud Compute extended to Google Cloud systems using NVIDIA GPUs for agentic tool-use and complex reasoning, while maintaining Apple's security architecture (dedicated processes, short-TTL inference recycling, attested keys in confidential VMs). Source: Apple Security Research blog "Expanding Private Cloud Compute"
- **Availability**: iOS 27 Developer Beta available with a waiting list for new Siri AI access; Aaron Perris (MacRumors) reported getting off the waitlist

This aligns with [[concepts/apple-gemini-ai-architecture]] and [[concepts/apple-foundation-models]] — the vision LLM screen extraction and Core AI PyTorch bridge are architecturally significant developments beyond what 2024's Apple Intelligence offered.

Source: [[raw/articles/simonwillison.net--2026-jun-8-wwdc--b8b98dfb.md]]

**datasette-agent 0.2a0** (Jun 10, 2026): Simon released `datasette-agent` 0.2a0 with two major features: (1) `ask_user()` — tools can now ask the user yes/no, multiple-choice, or free-text questions mid-execution. While a question is unanswered, the agent turn suspends; the question renders as a form in the chat UI and persists to the internal database, surviving server restarts. Once answered, the tool re-executes from the top. (2) `save_query` built-in tool — the agent can save SQL as a Datasette stored query, always requiring human approval. The `ask_user()` feature was enabled by a new LLM alpha built with Claude Fable 5. Source: [[raw/articles/simonwillison.net--2026-jun-10-datasette-agent--a829e35c.md]]

**Claude Fable 5's Relentlessly Proactive Debugging** (Jun 11, 2026): Simon published his most detailed account yet of Claude Fable 5's autonomous debugging capabilities. While debugging a Datasette Agent scrollbar bug, Fable autonomously: (1) wrote test HTML files to `/tmp/` to recreate the bug in Safari, (2) used `pyobjc-framework-Quartz` to enumerate operating system windows and identify Safari windows by their window title containing "textarea", (3) took screenshots of those windows using `screencapture` CLI, (4) modified Datasette Agent's Jinja template to inject a test JavaScript snippet, (5) built a CORS-compatible HTTP server via Python `http.server` to serve the modified template with the JS-enabled version while bypassing CSP restrictions, (6) eventually traced the root cause to Datasette Core's `include()` Jinja template tag. Simon notes this represents a "relentlessly proactive" pattern where Fable deploys any tool at its disposal — from system-level window enumeration to template modification to custom server builds — without being asked, demonstrating that modern agents autonomously extend their own tool chains when existing tools are insufficient. The most striking aspect: Simon was away from his computer; Fable initiated all these actions without any prompting, purely from the instruction "Look at dependencies to help figure out why there is a horizontal scrollbar here." Source: [[raw/articles/simonwillison.net--2026-jun-11-fable-is-relentlessly-proactive--0e9903b3.md]]

**Prompt Injection as Role Confusion** (Jun 22, 2026): Simon highlighted Charles Ye, Jasmine Cui, and Dylan Hadfield-Menell's research on prompt injection through 'role confusion.' The paper demonstrates that LLMs prioritize the *style* of text wrapped in role tags (<system>, <think>, <assistant>) over its actual content, making them vulnerable to style-based jailbreaks. Key finding: 'destyling' — rewriting text in a slightly different format — causes average attack success rate to plunge from 61% to 10%. Quote: 'Unless LLMs achieve genuine role perception, we think injection defense will remain a perpetual whack-a-mole game.' Source: raw/articles/simonwillison.net--2026-jun-22-prompt-injection-as-role-confusion--21e247aa.md

**Porting Moebius 0.2B Image Inpainting to Browser** (Jun 22, 2026): Simon ported the Moebius 0.2B lightweight image inpainting model (PyTorch/CUDA) to run entirely in-browser via ONNX Runtime Web on WebGPU, using Claude Code. The project demonstrated several agentic engineering patterns: (1) 'muse on X' prompts where an LLM contemplates feasibility before committing to a plan, (2) subagent delegation for analyzing obfuscated JavaScript (Whisper Web's CacheStorage API pattern), (3) completely no-code vibe coding — Simon never read any of the code Claude wrote. The resulting demo at simonw.github.io/moebius-web/ downloads ~1.3GB ONNX weights from Hugging Face, cached via CacheStorage API ("transformers-cache"). Full Claude Code transcript published. Source: raw/articles/simonwillison.net--2026-jun-22-porting-moebius--6904f00e.md

**AI and Liability — Bruce Schneier on German AI Overview Ruling** (Jun 25, 2026): Simon highlighted Bruce Schneier's commentary on a German court ruling holding Google liable for errors in AI-generated overviews. Schneier argued: "AI agents are agents of the person or organization that deploys them — and should be treated by the law as such." The core argument: if a company hired human writers for summaries, it would be liable for inaccuracies; allowing companies to hide behind "faulty AI" would create "disastrous incentives for corporate misbehavior" — why hire humans when AIs are cheaper AND absolve employers of mistakes? This connects to [[entities/gary-marcus]]'s analysis of Section 230 and AI liability (June 2026). Source: [[raw/articles/simonwillison.net--2026-jun-25-ai-and-liability--dc57f9f0.md]]

**Scrutineer: LLM-Powered Open Source Security Scanning** (Jun 25, 2026): Simon linked to Andrew Nesbitt's Scrutineer, a tool built for Alpha-Omega that uses LLMs to scan open source repos for security vulnerabilities while addressing the "maintainer burnout" bottleneck. Key insight: "Large language models have made finding vulnerabilities in open source code much easier" — but the bottleneck hasn't moved; every finding still needs human verification. Scrutineer runs a pipeline of skills against code and presents results in a web UI for triage, ensuring "the volume a model can generate never lands directly on a maintainer." This exemplifies the pattern of LLM-augmented tooling where AI handles discovery while humans retain verification — a practical application of [[entities/andrew-nesbitt]]'s open source security work. Source: [[raw/articles/nesbitt.io--2026-06-25-scrutineer-html--2ad1fbbe.md]]

**hackmyclaw.com Prompt Injection Challenge** (Jun 26, 2026): Simon reported on Fernando Irarrázaval's security challenge at hackmyclaw.com. The challenge invited anyone to leak secrets from an OpenClaw test instance via email. After **6,000 attempts** (consuming $500 in tokens and triggering a Google Workspace account suspension from inbound email volume), **0 injections succeeded**. The target model was Opus 4.6 with explicit Anti-Prompt-Injection Rules covering credential disclosure, file modification, command execution, and data exfiltration. Simon attributed the success to labs' ongoing investment in training models against injection attacks (citing the GPT-5.6 system card), but cautioned: "6,000 failed attempts provides no guarantees that someone with a more sophisticated approach couldn't get through." This challenge provides real-world validation of prompt injection defense improvements since the [[concepts/prompt-injection-as-role-confusion]] research. Source: [[raw/articles/simonwillison.net--2026-jun-26-hack-my-ai-assistant--4d91bd14.md]]

**Jon Udell on "Agent in the Loop"** (Jun 28, 2026): Simon highlighted Jon Udell's philosophical reframing of the "human in the loop" concept. Udell argues that "human in the loop" cedes authority to machines by default, and proposes flipping the narrative: "It's our loop, we work the same way we always have, now we recruit agents to join the team." The distinction between "human in the loop" (machine-centered, exclusionary framing) and "agent in the loop" (human-centered, invitation framing) complements Simon's own [[concepts/agentic-engineering]] philosophy — where agents augment rather than replace human judgment. Source: [[raw/articles/simonwillison.net--2026-jun-28-jon-udell--47b28924.md]]
