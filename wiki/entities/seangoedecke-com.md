---
title: "Sean Goedecke"
tags: [person]
created: 2026-04-24
updated: 2026-07-02
type: entity
sources:
  - raw/articles/seangoedecke.com--the-just-say-no-engineer-was-a-zirp-phenomenon--542e9446.md
  - raw/articles/seangoedecke.com--prompts-are-technical-debt-too--2bd50f80.md
  - raw/articles/seangoedecke.com--the-o3-geoguessr-prompt-did-not-work--c4335530.md
  - raw/articles/seangoedecke.com--weird-projects-i-shipped-with-ai--4c88d49c.md
  - raw/articles/seangoedecke.com--anti-ai-nostalgia--c80b7b06.md
  - raw/articles/seangoedecke.com--build-agents-not-pipelines--43a57b4a.md
  - raw/articles/seangoedecke.com--ai-gpus-live-longer-than-three-years--a4c8235c.md
  - raw/articles/seangoedecke.com--ai-inference-is-obviously-profitable--ac8d2cd6.md
  - raw/articles/seangoedecke.com--text-ai-watermarks--cd663c94.md
|---

# Sean Goedecke

**URL:** https://www.seangoedecke.com
**Blog:** seangoedecke.com
**Identity:** Australian software engineer
**Current:** Software engineer (industry, not academia)
**Book:** "Software Engineering After the Vibe Shift" (self-published, print-at-cost)
**Email:** sean.goedecke@gmail.com
**LinkedIn:** Available via blog
**Themes:** AI coding tools, large tech company dynamics, career progression, system design, engineering management, the impact of zero-interest rates on tech
**Podcast Appearances:** The Pragmatic Engineer Podcast, 99% Invisible, The Changelog, ABC News, Exponent Podcast, The Staff Plus Journey, Humans of Reliability Podcast, Grammar Girl Podcast, Dead Code

## Overview

Sean Goedecke is an Australian software engineer who writes about **AI's practical impact on software engineering**, **large tech company dynamics**, and the **structural forces shaping engineers' careers**. He is notable for being one of the first writers to publish a full-length book — *"Software Engineering After the Vibe Shift"* — analyzing how the end of zero-interest rates in 2021–2022 fundamentally altered the software engineering profession, making it much harder to build a career in the field.

Goedecke's blog stands out for its **pragmatic, experience-grounded perspective**. He writes as someone who has worked inside large tech companies and observed their dysfunction firsthand — not as a theorist but as a practitioner. His posts on AI coding tools are particularly valuable because he **actually uses them in production** and reports honestly on what works and what doesn't.

He has appeared on numerous podcasts discussing AI sycophancy, system design interviews, staff engineer promotions, and the reality of shipping in large organizations. His appearance on **99% Invisible** about how AI uses the em-dash (and his **Grammar Girl Podcast** appearance on the same topic) demonstrates his eye for subtle, overlooked aspects of AI behavior that reveal deeper truths about how these systems work.

Goedecke's blog is structured around practical categories: popular posts, recent posts, and topic tags (AI, career, engineering, leadership, productivity, teams). His **"popular" section** includes his most-read posts on code review, project shipping, and system design — all topics he approaches from the perspective of someone who has done the work, not just studied it.

His writing philosophy is evident in his book's distribution model: **print at cost, PDF freely available on GitHub**. He explicitly wants his ideas to spread, not to profit from them.

## Timeline

| Date | Event |
|------|-------|
| ~2021 | Begins blogging about software engineering and AI |
| 2022–2023 | Establishes reputation with posts on large tech company dynamics and AI coding tools |
| 2024 | Podcast appearances begin (Exponent, The Staff Plus Journey) |
| 2025 | Publishes multiple popular posts on AI sycophancy, coding agents, and tech industry analysis |
| 2025 | Book published: "Software Engineering After the Vibe Shift" |
| 2025 | Featured on 99% Invisible (em-dash analysis), ABC News (AI sycophancy), Grammar Girl Podcast |
| 2026 | Active through at least May 2026; continuing to publish on AI, career development, and left-wing pro-AI arguments |
| **2026-05-10** | Publishes "The left-wing case for AI" — outlines progressive arguments for AI adoption across disability rights, healthcare, class mobility, education, and utopian tech optimism |
| **2026-05-17** | Publishes "How I use LLMs as a staff engineer in 2026" — updated workflow: agents now produce entire PRs, 80% bug diagnosis rate, skimming vs. editing mental model shift |
| **2026-05-17** | Publishes "DeepSeek-V4-Flash means LLM steering is interesting again" — explores activation engineering and steering vectors for influencing model behavior |
|| **2026-05-22** | Publishes "The famous o3 'GeoGuessr' prompt did not work" — constructs a 200-image benchmark to test Kelsey Piper's famous GeoGuessr prompt, finding the elaborate prompt performed worse than the default (median 83.2km vs 102.3km). GPT-5.4/5.5 lack o3's geolocation ability. Demonstrates how easily prompt engineers can fool themselves without benchmarks |
|| **2026-05-22** | Publishes "Weird projects I shipped with AI" — catalogs 5 personal projects (Skifreedle, Autodeck, Endless Wiki, VicFlora Offline, gh-standup) built with LLM assistance, arguing they are "existence proofs" that AI enables projects that would not otherwise exist |
||| **2026-06-03** | Publishes "Anti-AI nostalgia and the cult of the past" — philosophical analysis of anti-AI rhetoric through Umberto Eco's Ur-Fascism framework. Maps "real programmers" nostalgia onto fascist patterns of tradition-cult and modernism-rejection. Challenges popular Luddite historiography. Warns that disillusioned elite engineers are susceptible to movements promising a return to idealized past. |
|| **2026-05-31** | Publishes "Build agents, not pipelines" — comprehensive comparison of pipeline vs agent architectures for LLM systems. Recommends "when in doubt, use agents" based on context-gathering difficulty, future-proofing, and one-directional migration pattern. References [[concepts/harness-engineering/agent-vs-pipeline-architecture]] |
|| **2026-05-17** | Publishes "The just-say-no engineer was a ZIRP phenomenon" — argues the "just-say-no" engineering archetype thrived under zero-interest-rate conditions and is now endangered by AI, but AI is not the root cause |
||| **2026-07-01** | Publishes "Text AI watermarks will always be trivial to remove" — detailed analysis of EU AI Act Article 50 text watermarking, SynthID's limitations at zero temperature, homoglyph-based watermarking by OpenAI/Anthropic, and the fundamental incompatibility of security-by-obscurity with AI Act interoperability requirements. → [[concepts/synthid#Text Watermark Criticism: The Removal Argument]] |
| **2026-06-27** | Publishes "AI inference is obviously profitable" — A100 cost calculation ($1/M tokens), 70-80% gross margin analysis, rebuttal to VC-subsidy thesis. → [[concepts/ai-industry-financial-sustainability]] ||
| **2026-06-14** | Publishes "AI GPUs live longer than three years" — thorough debunking of the "GPUs only last three years" meme. Oak Ridge Summit supercomputer 95%+ survival at 3 years; AWS has never retired an A100. Draws critical distinction between physical and economic lifespan. → [[concepts/ai-industry-financial-sustainability]] |
|
## Core Ideas

### "If You Are Good at Code Review, You Will Be Good at Using AI Agents"

This is Goedecke's most distinctive insight about AI-assisted development. His argument: **the skills that make you effective at reviewing other engineers' code — understanding intent, spotting subtle bugs, evaluating trade-offs, asking clarifying questions — are the same skills that make you effective at reviewing and directing AI-generated code.**

The implication is profound: **code review is the meta-skill for the AI era.** Engineers who have never practiced careful code review will struggle with AI agents because they won't know how to evaluate the output critically. Engineers who are already good reviewers will find AI much easier to work with because they're already in the right mental model: evaluating, not generating.

This reframes AI coding tools from a "will AI replace engineers?" question to a "how good is your evaluation skill?" question.

### The Vibe Shift: End of Zero-Interest Rates Killed Easy Mode

Goedecke's book *"Software Engineering After the Vibe Shift"* argues that the period of near-zero interest rates (roughly 2008–2021) created an **artificially easy environment for software engineering careers**. When capital was cheap:

- Startups could burn through funding without immediate profitability pressure
- Tech companies could hire aggressively and absorb inefficiency
- Engineers could switch jobs frequently for large compensation bumps
- "Move fast and break things" was a viable strategy because capital costs were low

When rates rose in 2022, the industry shifted to **efficiency-focused mode**: fewer hires, more scrutiny on business impact, emphasis on maintaining existing systems rather than building new ones. Goedecke's analysis suggests this isn't a temporary downturn — it's a **structural reset** that changes what skills and behaviors are rewarded.

### AI Sycophancy Is a Real Problem (and Most People Don't Notice It)

Goedecke has written about how AI models tend to **agree with users even when users are wrong**, a phenomenon he calls AI sycophancy. This is particularly dangerous in software engineering because:

- Engineers may be confident in incorrect approaches
- AI models will validate those approaches
- The feedback loop reinforces bad patterns
- Engineers become more confident in their errors

His appearance on **ABC News** about this topic suggests the issue has crossed from a technical concern to a mainstream one. The insight is that **AI makes you more confident, not necessarily more correct** — and confidence without correctness is worse than ignorance.

### "AI Can Write Your Code. It Can't Do Your Job."

This post captures Goedecke's measured, non-hysterical stance on AI: **yes, AI can generate code — but that's not what software engineering is.** Software engineering is understanding requirements, making trade-offs, coordinating with teams, debugging complex systems, and maintaining code over time. These are social and cognitive activities that AI doesn't replace, even when it can generate syntactically correct code.

The companies building AI are spending billions to acquire engineers, not replace them — evidence that the industry sees AI as a productivity multiplier, not a headcount reducer.

### System Design: Practical, Not Interview-Focused

Unlike the typical "system design interview prep" content, Goedecke's system design writing focuses on **what actually works in production**. He draws on his experience at large tech companies to identify patterns that scale, communication structures that prevent disasters, and the organizational dynamics that make or break technical decisions.

His approach is distinctly practical: **start from the problem, not from a catalog of architectural patterns.** Understanding what you're building before you decide how to build it.

### Code Review as a Leadership Skill

Goedecke argues that code review is not just a technical practice but a **leadership and communication skill**. Good reviewers:

- Ask questions that help the author think through their design
- Provide feedback that is specific, actionable, and kind
- Understand the context of the change (business requirements, team goals)
- Balance the cost of additional review rounds against the risk of merging

This connects to his broader thesis that **soft skills are the differentiator** in senior engineering roles — not technical prowess, which is table stakes.

### Why Longer-Horizon Training Hasn't Slowed AI Progress (May 2026)

Goedecke responded to Dwarkesh Patel's question — why hasn't AI progress slowed down despite longer training horizons requiring more FLOPs per reward signal? — with a nuanced three-part analysis:

**1. FLOP Efficiency Gains (The "Boneheaded Mistakes" Theory)**:
Training efficiency is determined not by genius ideas but by **eliminating boneheaded mistakes**. Goedecke cites the **GPT-4 FP16 summation bug**: using FP16 when summing many small values completely corrupts results if the sum is large. Fixing bugs like this plausibly buys **more efficiency than any inherent slowdown from longer training**. Frontier labs are still learning to use their existing FLOPs orders of magnitude more efficiently.

**2. Human Intelligence Judgment Is Inherently Flawed**:
The jump from GPT-3 to GPT-4 seemed huge because GPT-3 was dumber than almost all humans. But frontier models are now in the **realm of ambiguity**: it's hard to tell if they're smarter than you because when they are, **you're the one making mistakes**. Rate-of-growth of "raw intelligence" may have genuinely slowed — we wouldn't necessarily know.

**3. Intelligence ≠ Capability (The Constellation Theory)**:
Many traits other than raw intelligence determine model capabilities: **working memory, tool familiarity, context window attention, persistence, personality**. The jump to "agentic" models in October 2025 might have come from any of these, not just intelligence. Goedecke cites Apple's "The Illusion of Thinking" paper: models failed Tower of Hanoi not from lack of intelligence but lack of **persistence** — willingness to power through hundreds of steps.

**Key Insight**: AI development is dominated by "lightning strikes" — silly bugs that make training 100× worse, clever ideas that make models 100× more useful, and spiky capabilities. A general theory like "RL takes more FLOPs-per-reward as tasks get longer" sounds good but is overwhelmed by implementation reality.

### The Left-Wing Case for AI (May 2026)

Goedecke outlines explicitly left-wing arguments for AI adoption across five dimensions:

**1. Disability Rights**: LLMs as powerful accessibility tools — automatic video captioning, brain fog and chronic pain mitigation, neurodivergent "code switching" for professional communication, voice controls for mobility/vision-impaired users. Highlights the irony that left-wing AI critics often dogpile disabled people who describe AI as genuinely helpful.

**2. Healthcare Access**: LLMs empower patients with chronic illnesses to research conditions and advocate for themselves against dismissive medical establishments. Notes that the "just trust your doctor" framing is itself a conservative position; the left-wing position is sympathetic to patients who can't or don't trust institutional medical authority.

**3. Class Mobility and Code-Switching**: LLMs democratize access to "dangerous professional" communication — the formal, bureaucratic register traditionally gatekept by elite education. Working-class users can now write compelling regulatory complaints, legal petitions, and professional correspondence without needing to have absorbed the cultural norms of the professional class.

**4. Educational Equity**: LLMs as universal private tutors. While acknowledging the cheating risk for unmotivated students, argues that motivated students without access to tutoring can now learn at high-school level or above through LLM dialogue. Notes that teachers "hallucinate all the time" — citing a 2016 study finding 42% of math lessons contained content errors.

**5. Techno-Utopianism**: The 2000s-era vision of "fully automated luxury gay space communism" assumed technological progress would create post-scarcity. If left-wing premises are correct, and you're technologically optimistic, then a super-smart AI should inherently be left-leaning. Points out that all current frontier models do profess left-wing views, and attempts to train right-wing alternatives (like Musk's Grok) have so far failed.

**Key Quote from Reader Matt**: "If similar reasoning had been applied to outright reject computers as fascist and unethical in the 80s and onward, my own life would have been quite different, and arguably worse. I have enough usable vision to handwrite, uncomfortably, with my head against the page... Computers saved me from having to do even more... And now that AI helps at least one group of disabled people (of which I'm more or less a part), do I want to deny that benefit?"

### The Just-Say-No Engineer Was a ZIRP Phenomenon (May 2026)

Goedecke identifies and analyzes the **"just-say-no engineer" archetype** — senior/staff engineers whose role is to slow things down, block feature development that adds complexity, and ensure as little code gets written as possible (since "code is a liability"). He argues this archetype was a product of the **zero-interest-rate policy (ZIRP) era (2008–2022)** and is now endangered.

**The ZIRP dynamic**: During the ZIRP era, cheap capital meant tech companies were incentivized to hire aggressively — teams grew from tens to thousands of engineers, many working on tangential projects. The just-say-no engineer was valuable because: (1) having half the company's engineers in endless propose-and-block loops was fine since they didn't need to be productive; (2) it prevented the 5% of engineers who'd "get drunk on their technical freedom" from making wild proposals; (3) a reputation for high technical bar was good for hiring.

**The post-ZIRP reality**: When rates rose and companies flipped to efficiency mode, the just-say-no engineer lost institutional support. Management that once deferred to their judgment now overrules them, and they get bad reviews for the same behavior that was rewarded pre-2022.

**The AI red herring**: Goedecke argues AI is NOT the cause of this shift — companies blamed layoffs on AI because "with this transformative technology, we're able to deliver 10× the value with half the engineers" sounds better than "we were paying hundreds of engineers to do unprofitable work." If ZIRP hadn't ended, AI would have been a boon for just-say-no engineers, creating even more code to gatekeep.

**Irony**: AI coding tools mostly **work** and haven't yet caused a catastrophe. The code is less clean and less well-understood, but it's good enough. The just-say-no engineer now faces an identity crisis: either insist the apocalypse is right around the corner, or accept their role was contingent on a historically unusual economic environment.

**Pure vs. impure engineering**: Goedecke draws a distinction between "pure" engineering (well-scoped, technical goals like compilers and runtimes) where the just-say-no engineer thrives, and "impure" engineering (poorly-scoped, customer-driven features) where they don't. The ZIRP era allowed companies to treat even impure work like pure work. Now, just-say-no engineers should move into core infrastructure roles where quality standards remain high, accepting a more limited scope than in the 2010s.

### The o3 GeoGuessr Prompt Illusion (May 2026)

Goedecke constructed a rigorous 200-image benchmark to test whether Kelsey Piper's famous o3 "GeoGuessr" prompt actually improved geolocation performance. The results surprised many in the AI community:

| Prompt | n | Median km | Mean km | ≤25 km | ≤100 km | ≤500 km |
|--------|---|-----------|---------|--------|---------|---------|
| **Default** | 200 | **83.2** | **440.7** | 58 | 109 | 176 |
| GeoGuessr prompt | 200 | 102.3 | 481.9 | 59 | 99 | 172 |

**Key findings:**
- The elaborate 10×-longer prompt **performed worse** than a simple default prompt
- o3's geolocation ability **did not transfer** to gpt-5.4 or gpt-5.5 (median 156–163km vs o3's 83km)
- The benchmark cost only ~$15 and took ~6 hours of distracted work to construct

**Core lesson**: This demonstrates "how easy it is to fool yourself about the quality of prompting." When a model is already good at a task, an elaborate prompt gets credit for performance that was always there. Models are sycophantic about prompt quality — they "will happily make up stories for you about their own reasoning processes."

**Why nobody checked**: Geolocation was only the story for about a week before the discourse moved on. Better AI tooling (GPT-5.5 doing the heavy lifting) now makes rigorous evaluation much cheaper.

[[concepts/evaluation/prompt-engineering-evaluation]] — Full concept page on the case study and its implications for prompt engineering methodology.

### Anti-AI Nostalgia and Fascist Rhetoric (June 2026)

On June 3, 2026, Goedecke published "[Anti-AI nostalgia and the cult of the past](https://seangoedecke.com/anti-ai-nostalgia/)" — his most philosophically ambitious post. He argues that **anti-AI rhetoric structurally parallels fascist rhetorical patterns** as defined by Umberto Eco's *Ur-Fascism*, specifically the "cult of tradition" and "rejection of modernism."

**The Ur-Fascism framework**: Goedecke quotes Eco's first two defining features of fascism — the cult of tradition and the rejection of modernism — and maps them onto anti-AI discourse: the nostalgic "real programmers" narrative, the framing of AI as a corrupting modern influence, and the call to return to an idealized past. He cites Ezra Pound's anti-usury poems, Julius Evola's traditionalist philosophy, and Hitler's speeches as examples of the same rhetorical structure: mourning a lost spiritual integrity and blaming it on degenerate modern forces.

**Luddite historiography correction**: Goedecke challenges the popular left-wing framing of the Luddites as a proto-feminist, anti-capitalist movement. Actual Luddite threats explicitly targeted female workers (threatening to "discharge the bitches and take men into your employ again"). The Luddites were fundamentally conservative — wounded masculine elite identity protecting all-male guild privileges, not a progressive movement against automation.

**The disillusioned elite danger**: Goedecke's central concern is that software engineers whose skills are devalued by AI will form the same kind of "disillusioned elite" that historically gravitated toward fascism. Engineers who believed their job was "to be excellent at their craft" rather than "producing shareholder value" are now confronting the end of ZIRP and AI disruption simultaneously — a susceptible audience for movements promising a return to an idealized past.

References: [[concepts/ai-criticism-politics]]

> "If you are good at code review, you will be good at using AI agents."
> "If you are good at code review, you will be good at using AI agents."

> "AI can write your code. It can't do your job."

> (On AI sycophancy) "The companies building AI are spending billions to acquire engineers, not replace them."

> (On the vibe shift) "The end of zero-interest rates made it much harder to be a software engineer."

## Writing Style & Philosophy

Goedecke writes with a **pragmatic, experience-grounded voice**. His posts are typically:

- **Short and focused** — usually 3-6 minute reads
- **Structured with clear headings** — easy to skim, hard to misinterpret
- **Based on direct experience** — not speculation or trend-chasing
- **Willing to challenge received wisdom** — AI sycophancy, the value of code review, the "good times" narrative
- **Accessible to a broad audience** — no jargon without explanation

He uses email as his primary contact channel and explicitly encourages reader engagement: "Hearing from readers is one of the main reasons I write at all, so please do reach out." This suggests a community-oriented approach to blogging.

His book is self-published at cost, with the raw PDF freely available on GitHub. This is a **deliberate anti-monetization stance** — the goal is spreading ideas, not generating revenue.

## Technical Breadth

- **AI/ML**: Practical use of coding agents, AI sycophancy, model capabilities and limitations
- **Software Architecture**: System design for production, trade-off analysis
- **Career Development**: Staff engineering, promotion paths, job market dynamics
- **Engineering Management**: Code review practices, team dynamics, project shipping
- **Tech Industry Analysis**: Impact of macroeconomic forces on engineering careers
- **Large Tech Company Dynamics**: Organizational structure, decision-making, coordination costs

## Recent Themes (2024–2026)

- **AI coding tools**: Practical assessment of what works and what doesn't
- **Code review as meta-skill**: The bridge between human and AI-assisted development
- **Tech industry structural shifts**: End of zero-interest rates and its lasting impact
- **Career development**: What actually makes you senior (hint: it's not technical skills alone)
- **AI sycophancy**: The danger of AI that agrees with you too readily
- **System design in practice**: Not interview prep, but real-world architecture
- **Writing and publishing**: Self-publishing a book, reaching 230,000+ readers

## Related

- [[concepts/evaluation/prompt-engineering-evaluation]] — The o3 GeoGuessr prompt illusion and quantitative evaluation methodology
- [[concepts/ai-coding-tools]] — Code review as the meta-skill for AI-assisted development
- [[concepts/software-engineering]] — Career progression, system design, tech industry dynamics
- [[concepts/ai-sycophancy]] — AI models agreeing with users even when wrong
-  — Impact of interest rates on engineering hiring
-  — Practical architecture, not interview prep-  — Code review, team dynamics, leadership
## Influence

- Appeared on **The Pragmatic Engineer Podcast** (Gergely Orosz's show), signaling recognition by the broader tech writing community
- Featured on **99% Invisible** for analysis of AI's em-dash usage — a crossover to mainstream media
- **230,000+ unique visitors** in first year of blogging (per his retrospective post)
- Self-published book distributed at cost, demonstrating commitment to idea-sharing over monetization
- Regular podcast guest on engineering and AI topics

## Recent Articles

- **Anti-AI nostalgia and the cult of the past** (2026-06-03): Philosophical analysis of anti-AI rhetoric through Umberto Eco's Ur-Fascism framework. Warns that disillusioned elite software engineers are susceptible to fascist-adjacent movements promising return to an idealized past. References: [[concepts/ai-criticism-politics]]

- **Build agents, not pipelines** (2026-05-31): Argues there are only two ways to use LLMs — as a pipeline (control flow in code) or as an agent (control flow delegated to LLM). Compares tradeoffs: pipelines are more predictable and cost-bounded, agents are smarter and more flexible. Key insight: context-gathering is far harder for pipelines than agents, which is why RAG failed to replace agentic retrieval. Recommends "when in doubt, use agents" — migration from pipelines to agents is one-directional. Proposes hybrid architecture for large-scale analysis: cheap pipeline for initial flagging, agent fleet for deep investigation. Links: [[concepts/harness-engineering/agent-vs-pipeline-architecture]]

- **The just-say-no engineer was a ZIRP phenomenon** (2026-05-17): Identifies the "just-say-no" senior engineer archetype as a product of the zero-interest-rate era. Argues that AI coding tools are not the cause of this archetype's decline — the end of cheap capital is. Distinguishes between "pure" (compilers, runtimes) and "impure" (customer-driven features) engineering domains, recommending just-say-no engineers migrate to core infrastructure roles.

- **How I use LLMs as a staff engineer in 2026** (2026-05-17): Documents the evolution from his February 2025 post. Key changes: agents now reliably produce entire PRs (he starts every change with an agent and pushes after a single editing pass); shifted from open VSCode windows to terminal-based Copilot CLI sessions; uses agents tens of times per day; 80% bug diagnosis rate autonomously. Notable: he still writes his own PR descriptions because LLMs over-communicate and miss the "core idea"; still doesn't use LLMs for Slack messages or ADRs to signal human thinking; uses agents for local config troubleshooting (nvm, node version switching). Core thesis: "the current core AI skill is shifting as much work onto AI agents as possible, without going too far."

- **AI makes weak engineers less harmful** (2026-05-08): Argues that frontier LLMs have raised the floor for weak engineers — instead of producing completely broken PRs, they now produce "standard LLM pull requests: wrong in some ways, baffling in others, but at least functional on the line-by-line level." Notes the phenomenon of engineers becoming "thin wrappers around Claude Code," communicating via Slack rather than direct interaction. Predicts a future push to measure "what value engineers are adding to AI" rather than just AI's value to engineers. Crucially observes that "no strong engineers use AI tools like this" — the wrapper phenomenon is limited to those for whom it represents an improvement.

- **Notes on incidents** (2026-05-08): Practical wisdom from incident response experience. Key insights: (1) Most incidents resolve on their own — well-designed systems self-heal via Kubernetes restarts, circuit breakers, and queue buffering. (2) Most incident-resolving actions make incidents worse — engineers jump too quickly to "fix" things, often creating secondary incidents. (3) The first thing you should do in an incident is **nothing** — take time to understand before acting. (4) Effective incident-resolving actions are often dull — typically disabling a feature flag or reverting a change. (5) Knowledge of the system beats raw intelligence — one familiar engineer outperforms five strangers. (6) Resolving incidents buys political credit but isn't a durable power position — executives can't claim incident successes as their own.

- **Many anti-AI arguments are conservative arguments** (2026-04-18): Argues that the substance of most anti-AI rhetoric aligns with conservative/right-wing worldviews despite being framed in progressive language. Political coding inversion analysis with implications for AI policy coalitions.

- **The left-wing case for AI** (2026-05-10): Outlines explicitly left-wing pro-AI arguments across five dimensions: (1) **Disability** — LLMs as powerful accessibility aids for neurodivergent, chronically ill, and mobility/vision-impaired users; (2) **Chronic illness and medical care** — LLMs enable patients to research conditions and advocate for themselves against dismissive medical establishments; (3) **Class and code-switching** — LLMs democratize access to "dangerous professional" communication styles that were previously gatekept by elite educational pipelines; (4) **Education** — LLMs provide private-tutor-level access to every motivated student, reducing educational inequality; (5) **Utopia** — if left-wing views are correct and you're technologically optimistic, super-smart AI inherently trends left-wing (all current frontier models profess left-leaning views, and attempts to train right-wing alternatives have failed). Includes a powerful reader testimonial from a disabled person describing how computers transformed their life in the 1980s-90s and how AI is now extending similar benefits to those with communication barriers.


|- **The famous o3 Geoguessr prompt did not work** (2026-05-22): Built a 200-image benchmark testing Kelsey Piper's elaborate o3 GeoGuessr prompt vs default. The elaborate prompt performed worse (median 102.3km vs 83.2km). GPT-5.4/5.5 lack o3's geolocation ability. Demonstrates the ease of self-deception in prompt engineering without quantitative evaluation.
|
|- **Weird projects I shipped with AI** (2026-05-22): Catalogs 5 personal projects shipped with LLM assistance — Skifreedle (daily-game SkiFree clone with Stripe), Autodeck (auto-generated spaced repetition cards), Endless Wiki (280K+ AI-generated pages discoverable by clicking links), VicFlora Offline (PWA caching Victorian plant database), and gh-standup (GitHub CLI standup extension). Argues these are \"existence proofs\" that AI enables projects that would otherwise stay at the \"GitHub repo with a few commits\" stage. Notes that code is only one bottleneck in shipping a product — deployment, payments, and persistence are significant barriers even with great AI code generation. |
- **Prompts are technical debt too** (2026-05-20): Argues that prompts are a worse form of technical debt than code — prompts are model-specific and silently degrade with each model update, whereas code is stable when untouched. Recommends using third-party AI coding tools with minimal customization. Core insight: code review skills transfer directly to AI agent evaluation, making code review the meta-skill of the AI era.

### AI GPU Lifespan Analysis (June 2026)

Sean Goedecke's June 14, 2026 post thoroughly debunks the "GPUs only last three years" meme popular among AI skeptics.

**Source of the Claim:** The "three years at most" claim originates from an anonymous "GenAI principal architect" at Google quoted in a Tom's Hardware article. The original source is a Tegus interview — Tegus pays insiders hundreds of dollars per hour to answer technical questions, incentivizing confident but potentially inaccurate claims.

**Counter-Evidence:**
- Google publicly claims eight-year-old TPUs running at 100% utilization in production
- AWS CEO confirmed in February 2026 that AWS has never retired an A100 server (A100s were made 2020–2024)
- Oak Ridge Summit supercomputer (27,000+ V100s, 2018–2024): over 95% of GPUs survived at three years; bottom-cage GPUs still above 90% survival rate at six years
- HN comment: an academic GPU cluster lasted six years with less than 20% failure rate

**Physical vs. Economic Lifespan:** Goedecke makes a critical distinction:
- **Physical lifespan:** GPUs can operate reliably for 6+ years under load
- **Economic lifespan:** Newer GPUs (B100) may be 5× more efficient per watt, making older GPUs (A100) economically obsolete for well-capitalized providers
- However, economic obsolescence does NOT support the "inference costs will spike" argument — A100s remain profitable, and cash-poor providers can continue running them

**Datacenter Cost Structure:** GPUs are only 50–70% of datacenter spend (land, power, cooling make up the rest). Even worn-out GPUs don't require rebuilding entire datacenters.

**Conclusion:** The claim is popular because it's useful for AI skeptics, not because it's true. It comes from a single pseudonymous tweet quoting a paid anonymous source. If an AI winter comes, providers can run B300s, H100s, or even A100s profitably for 6+ years.

### AI Inference Is Obviously Profitable (June 2026)

On June 27, 2026, Goedecke published "[AI inference is obviously profitable](https://seangoedecke.com/ai-inference-is-obviously-profitable/)" — a direct rebuttal to the popular claim that AI inference is unprofitable and must be subsidized by VC dumb money.

**Core Argument**: AI inference is obviously profitable at current prices. The math:

- **Physical cost calculation**: An A100 consumes 400W under load. Running a dense 70B model on 4× A100s (~2M tokens/hr) costs ~13¢/hr at industrial power prices. With cooling (pessimistically matching power), ~13¢/M output tokens.
- **GPU amortization**: A100 at $20k, 5-year lifespan → $16k/yr recoup → ~$1.80/hr → total inference cost ~$1/M tokens.
- **Market pricing**: GPT-5.4-mini charges $4.50/M tokens. Stronger OpenAI/Anthropic models are 3-6× that. Claimed 70-80% gross margins are "extremely plausible."
- **Open LLM proof**: DeepSeek claims 80%+ profit margin on R1 inference, and their API pricing is less than half of OpenAI/Anthropic. DeepSeek-V4-Pro on the open market: ~87¢/M tokens — close to actual cost.

**Why high margins persist**: AI labs (OpenAI, Anthropic) use inference profits to **subsidize training costs**. They're not just selling inference — they're funding the next model's training from current margins.

**Key insight for sustainability**: Even if OpenAI and Anthropic fail, whoever acquires rights to their frontier models can continue selling inference profitably. "The AI bubble popping will not mean the end of the inference business, because AI inference is obviously profitable."

**Counterpoint to the "AI bubble" narrative**: Unlike the VC-subsidy theory, inference is a real business with real margins. The risk is in training costs and valuation bubbles, not in the fundamental unit economics of serving models.

This analysis extends [[concepts/ai-industry-financial-sustainability]] with concrete unit-cost calculations and provides a data-driven counterweight to the growing [[concepts/ai-bubble]] literature.

## Sources

- raw/articles/seangoedecke.com--the-o3-geoguessr-prompt-did-not-work--c4335530.md
- raw/articles/seangoedecke.com--build-agents-not-pipelines--43a57b4a.md
- raw/articles/seangoedecke.com--ai-inference-is-obviously-profitable--ac8d2cd6.md
- raw/articles/seangoedecke.com--text-ai-watermarks--cd663c94.md
- seangoedecke.com — Primary blog
- "Software Engineering After the Vibe Shift" — Book (self-published, print at cost)
- "If You Are Good at Code Review, You Will Be Good at Using AI Agents"
- "The Good Times in Tech Are Over"
- "AI Can Write Your Code. It Can't Do Your Job"
- "Why I Still Write Code as an Engineering Manager"
- "Nobody Gets Promoted for Simplicity"
- "What Actually Makes You Senior"
- "The Strange Case of Engineers Who Dismiss AI"
- Podcast appearances: Pragmatic Engineer, 99% Invisible, The Changelog, Exponent, Staff Plus Journey, Humans of Reliability, Grammar Girl, Dead Code, ABC News

## References

- seangoedecke.com--the-o3-geoguessr-prompt-did-not-work--c4335530
- seangoedecke.com--2025-wrapup--17f79aba
- seangoedecke.com--a-little-bit-cynical--7ba10c9b
- seangoedecke.com--addicted-to-being-useful--63b6b7ac
- seangoedecke.com--ai-detection--e63a94c4
- seangoedecke.com--bad-code-at-big-companies--456be8ff
- seangoedecke.com--big-tech-needs-big-egos--47117535
- seangoedecke.com--continuous-learning--c324e562
- seangoedecke.com--fast-llm-inference--9f52f6cb
- seangoedecke.com--gas-and-ralph--fbb0beb3
- seangoedecke.com--generate-skills-afterwards--b1d3a6ea
- seangoedecke.com--getting-the-main-thing-right--cbdfa8d0
- seangoedecke.com--giving-llms-a-personality--5d1208a5
- seangoedecke.com--grok-deepfakes--5642acf5
- seangoedecke.com--heroism--f93f8694
- seangoedecke.com--how-does-ai-impact-skill-formation--f6695380
- seangoedecke.com--how-i-estimate-work--e0588a85
- seangoedecke.com--insider-amnesia--173bb317
- seangoedecke.com--knowing-how-to-drive-the-car--f0fe0e98
- seangoedecke.com--luddites-and-ai-datacenters--3ab44e30
- seangoedecke.com--many-anti-ai-arguments-are-conservative--ed12c53a
- seangoedecke.com--nobody-knows-how-software-products-work--5e504594
- seangoedecke.com--programming-with-ai-agents-as-theory-building--b672de74
- seangoedecke.com--screwing-up--77b3722a
- seangoedecke.com--simple-work-gets-rewarded--8214c3f2
- seangoedecke.com--software-engineering-may-no-longer-be-a-lifetime-career--be1d2e58
- seangoedecke.com--the-dictators-handbook--354e2eb5
- seangoedecke.com--unblockable--dd42280e
- seangoedecke.com--will-my-job-still-exist--f6e439b0
- seangoedecke.com--working-on-products-people-hate--9dead82f
- seangoedecke.com--you-cant-design-software-you-dont-work-on--1c498a63

|- seangoedecke-anti-ai-conservative-2026-04-18
|- seangoedecke.com--ai-makes-weak-engineers-less-harmful--e25ee659
|- seangoedecke.com--notes-on-incidents--f92d1b32
|- seangoedecke.com--why-hasnt-longer-horizon-training-slowed-ai-progress--6cc7ecad
||- seangoedecke.com--the-left-wing-case-for-ai--363b6e35
|- seangoedecke.com--weird-projects-i-shipped-with-ai--4c88d49c
|- seangoedecke.com--anti-ai-nostalgia--c80b7b06
|- seangoedecke.com--build-agents-not-pipelines--43a57b4a
|- seangoedecke.com--ai-inference-is-obviously-profitable--ac8d2cd6.md
