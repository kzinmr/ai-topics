---
title: Ed Zitron
description: Tech columnist and AI industry critic. Author of Where's Your Ed At newsletter (~80K subscribers). Argues the AI economy is a circular dependency where 95%+ of compute demand flows through OpenAI and Anthropic, neither of which can afford their bills without constant venture capital infusions.
url: https://www.wheresyoured.at/
type: entity
created: 2026-05-09
updated: 2026-05-27
aliases: [edward-zitron, "Where's Your Ed At"]
tags:
  - person
  - blogger
  - economics
  - infrastructure
  - prediction
  - controversy
  - techno-pessimism
  - ai-skepticism
sources:
  - raw/articles/wheresyoured.at--premium-ais-circular-psychosis--51c035f1.md
  - raw/articles/wheresyoured.at--anthropics-profitability-swindle--d54ac6ec.md
  - https://www.wheresyoured.at/
  - raw/articles/wheresyoured.at--ai-is-too-expensive--2387fc59.md
  - raw/articles/wheresyoured.at--news-openai-had-a-negative-122-operating-margin-in-q1-2026-a--78435c26.md
  - https://www.wheresyoured.at/news-openai-had-a-negative-122-operating-margin-in-q1-2026-and-chatgpt-growth-has-stalled/
  - raw/articles/wheresyoured.at--the-revenge-of-the-business-idiot--1bd92b92.md
  - raw/articles/wheresyoured.at--i-will-never-respect-a-website--e91c1694.md
  - raw/articles/wheresyoured.at--ai-is-really-weird--cfa83f71.md
---

# Ed Zitron

**Ed Zitron** is a tech columnist, journalist, and author of the _Where's Your Ed At_ newsletter, which has ~80,000 subscribers (as of January 2026, per The Guardian). He writes for _The Atlantic_, _The Guardian_, and his own publication. Zitron is one of the most prominent and persistent critics of the AI industry's economic fundamentals, arguing since March 2024 that the AI boom is an unsustainable bubble built on circular financial dependencies.

## Core Thesis: The Circular AI Economy

Zitron's central argument, developed across dozens of articles since 2024, is that **the AI economy is circular and self-referential** — nearly all AI compute demand and revenue flows through two companies (OpenAI and Anthropic), both of which are deeply unprofitable and dependent on constant venture capital infusions from the very hyperscalers that bill them for compute.

### Key Claims (from "AI's Circular Psychosis", May 2026)

- **95%+ of AI compute demand** comes from: Meta, Microsoft (for OpenAI), Google (for Anthropic), Amazon (for Anthropic), OpenAI, and Anthropic
- **90%+ of AI software/compute revenues** flow through Anthropic or OpenAI
- **70-80% of Microsoft, Google, and Amazon's AI revenues** depend on Anthropic or OpenAI
- **$748 billion** of the hyperscalers' total revenue backlog (not just AI) depends on OpenAI and Anthropic
- **Anthropic raised $58 billion in 8 months** (Sep 2025–May 2026), with potential to reach $108 billion
- **Only ~$13 billion in AI compute demand** exists outside of Anthropic, OpenAI, Meta, and associated parties
- No GPU compute customer larger than $100M/year exists outside the big-two-plus-Meta ecosystem (Poolside: $400M/year but only raised $500M total before deal collapse)
- **Neoclouds are unsustainable** — only able to sign deals with Anthropic, OpenAI, or hyperscalers acting as intermediaries

### Revenue Flow Model

```
AI Startups → pay for tokens → Anthropic/OpenAI → pay for GPUs → Microsoft/Google/Amazon
                                                                    ↓
Microsoft/Google/Amazon → re-invest via equity → Anthropic/OpenAI (circle continues)
```

### Data Center Overbuild Thesis

- 15.2GW of capacity under construction through end of 2027
- Hyperscalers spent ~$700 billion in capex since 2023, with 5.5GW ($300B+) built entirely for OpenAI and Anthropic
- xAI handed Colossus-1 (300MW, $4B+ construction cost) entirely to Anthropic — suggesting xAI itself had no need for it
- **92% of capacity under construction** is reported as "pre-committed" (JLL), but Zitron argues the commitments are circular
- Thousands of companies would need to rent hundreds/thousands of GPUs for the 15.2GW pipeline to make economic sense

## Notable Articles

| Date | Title | Key Claim |
|------|-------|-----------|
| Mar 2024 | Peak AI | AI at peak of hype cycle |
| Jul 2025 | The Subprime AI Crisis | AI companies are losing money on inference |
| Sep 2025 | Why Everybody Is Losing Money On AI | Industry-wide unprofitability |
| Jan 2026 | AI Bubble 2027 | Detailed bubble burst timeline |
| Apr 2026 | AI's Economics Don't Make Sense | Fundamental economic incoherence |
| May 2026 | AI's Circular Psychosis | Comprehensive circular dependency analysis |
| May 2026 | The AI Compute Demand Story Is A Lie | Data center capacity myths |
| May 2026 | Where Are All The Data Centers? | Investigates claims vs. reality of hyperscaler data center construction |
| May 2026 | I Will Never Respect A Website | "LLMs are websites" framing; Stella Laurenzo's Claude Code analysis; coding vulnerability crisis |
| May 2026 | AI Is Really Weird | Agent definition critique; Anthropic revenue anomalies; capacity planning paradox |

## AI Is Too Expensive (May 2026)

In "AI Is Too Expensive" (May 19, 2026), Zitron published his most comprehensive data-rich analysis of AI economics, providing concrete enterprise case studies to support his circular dependency thesis.

### Hyperscaler Capex Analysis

- **Microsoft invested ~$100B in OpenAI** (cumulative through FY2026 via testimony in Musk-OpenAI trial) — ~30% of Microsoft's $293.8B capex since FY2023
- **Hyperscalers invested $800B+ in 3 years**, with plans for $700B more in 2026 and $1T in 2027
- **Break-even requires $3T+ in AI-specific revenue**; $6T+ for meaningful returns
- Combined revenue of Microsoft ($281B), Meta ($200B), Amazon ($716B), Google ($402.8B) = $1.599T — none disclose actual AI revenue
- **Anthropic at $45B annualized revenue** (alleged) still cannot recover a single year of hyperscaler capex

### Customer Cost Crisis

| Organization | AI Spend | Impact |
|---|---|---|
| **Zillow** | $1M+ in Q1 2026; $749K in April (Cursor+Anthropic+Bedrock); on track for $7-10M/year | 20-50% of 2025 net income ($23M). Near 75% through $1.1M annual Cursor budget by end of April |
| **Stripe** | ~$94K/day ($2.8M/month) in tokens on Anthropic coding models | 4.4% of technical headcount costs. 5,000 technical staff burning tokens |
| **ServiceNow** | CIO Kellie Romack working with CFO to contain costs | "It's a really hard problem" — may not afford Claude Enterprise through rest of year |
| **Goldman Sachs** | AI costs approaching 10% of total headcount costs | "On track to be on par with headcount costs in next several quarters" |
| **Salesforce** | $300M committed to Anthropic tokens in 2026 (Marc Benioff) | Largest public token commitment |

### Zillow Case Study

Zillow's AI spending provides Zitron's most detailed enterprise case study:
- **$1M+ AI spend in Q1 2026**; $749K in April alone across Cursor, Anthropic, and AWS Bedrock
- **Cursor budget at 85% depletion** by mid-May with 7.5 months remaining in year
- **Technical leadership pushing "AI-Native Engineering"** — goal: "software engineers to never open a code editor again"
- **Paradoxical metrics**: Engineering headcount flat, but:
  - Outputs requiring human review: +50%
  - Code deployments/PRs: +39%
  - Software reviewer load: +29,000 hours/month (19 hours/engineer)
- **Internal chaos**: Blind posts from Zillow engineers describe code as "slowly becoming AI slop"; employees feel "lost in the agentic world"; token burn driven by "hitting internal AI adoption targets" rather than outcomes
- **"2027: A Tuesday" slide**: Visions of engineers only opening "spec and eval dashboards" with agents handling all code — Zitron describes this as a "hellscape vision"
- Sources at Zillow report **no actual movement toward this vision** — engineers still open IDEs and review code manually

### Anthropic Enterprise Obfuscation

Zitron reported that Anthropic does not offer:
- Granular telemetry showing which users consume which tools
- Service-level agreements (SLAs) standard in enterprise software
- Transparent breakdown of how tokens are burned across organizations

CIOs from ServiceNow and other organizations confirmed that Anthropic's lack of visibility into cost drivers makes budgeting impossible.

### Token Budget Accounting Crisis

Zitron argues that **no enterprise can reliably measure AI ROI**:
- LLMs behave non-deterministically — same prompt, different token cost
- Token cost per task varies with model, context, and random sampling
- Engineers game metrics: at Amazon and Meta, employees wrote scripts to burn extra tokens
- Every measurable metric (PRs, velocity, deployments) can be gamed
- "Every single AI token budget is bullshit because you can't measure how many tokens a task will take"

### Revenue Flow Breakdown

Detailed RPO (Remaining Performance Obligations) analysis:
- **Microsoft**: $625B RPO driven by $250B OpenAI commitment + $30B Anthropic — without these, RPO effectively flat
- **Amazon**: $364B RPO driven by $100B+ Anthropic compute deal
- **Google**: $467.6B RPO driven by $200B Anthropic TPU commitment
- **Conclusion**: Outside OpenAI and Anthropic, hyperscalers show no significant revenue growth



In "Where Are All The Data Centers?" (May 2026), Zitron conducted an investigative analysis of hyperscaler data center construction claims, finding significant discrepancies between announced capacity and verified operational infrastructure:

### Anthropic's 'Profitability' Swindle (May 2026)

Zitron critically analyzed WSJ reporting that Anthropic was "about to have its first profitable quarter" ($10.9B Q2 revenue, $559M operating profit). He demonstrated the profit was an accounting artifact:

- **SpaceX Colossus discount**: Anthropic's SpaceX deal included a reduced fee during May–June (ramp-up period), artificially depressing compute costs for the exact months needed to show a profit. Full $1.25B/month starts July.
- **Revenue inconsistencies**: Anthropic claimed $14B ARR in Feb → $19B ARR in Mar → $30B ARR in Apr, but CFO Krishna Rao stated under oath (Mar 9) that Anthropic had revenues "exceeding $5 billion to **date**" — contradictory to the leaked growth figures.
- **Prepayment hypothesis**: Anthropic likely takes prepayment of tokens from enterprises ($50M+ intended for 12 months) booked as immediate revenue before delivering the compute — inflating revenue while depressing costs.
- **Overall**: "That operating profit is a result of accountancy rather than any improvements to its business model." If Anthropic paid full-rate compute during those months, economics would revert to the circular dependency pattern Zitron has documented since 2024.

### Key Findings

- **No 1GW data center has actually been built yet** — despite announcements of gigawatt-scale campuses, the largest facilities remain well below claimed capacity
- **Microsoft's 4GW claim over 2 years**: Zitron traced every publicly announced Microsoft data center project and found most are still under construction, in permitting, or at "concrete slab" stage. The Fairwater Atlanta and Wisconsin sites combined deliver ~342MW (not IT load), far below the 4GW claimed
- **Phase deception**: Companies declare campuses "operational" when only one phase or building is complete, inflating perceived capacity. Amazon's Project Rainier was declared "operational" with only 7 of 30 buildings active
- **Construction timelines**: A modest 1MW data center took 11 months from groundbreaking to ribbon-cutting. A 36MW facility took 20 months. A 60MW facility took 26 months. Gigawatt-scale campuses would logically require many years, not quarters
- **Fairwater Wisconsin**: Designed for 117MW (per permitting), not the 400MW claimed by some sources. As of April 2026, satellite footage showed one building operational, one under construction
- **Fairwater Atlanta**: ~225MW estimated across phases, with buildings still under construction as of late 2025/early 2026
- **Microsoft's "multiple identical Fairwater data centers"**: Zitron could find no evidence of additional Fairwater sites beyond Atlanta and Wisconsin
- **OpenAI's Stargate Abilene**: Two buildings at ~103MW each, with a third building fully constructed but "barely any gear inside it" — far from the 1.2GW promised
- **Nscale Loughton, England**: Effectively nothing built after nearly a year; OpenAI backed out
- **Microsoft's silence**: Zitron sent specific questions to Microsoft on May 4, 2026 asking for clarification on capacity claims. A representative promised to "circle back" but never responded

### The "Contracted vs. Operational" Obfuscation

Zitron identified a pattern where companies conflate **contracted power** (signed deals, future capacity) with **active, revenue-generating capacity**:
- CoreWeave claims 3.1GW of "total contracted power" but only added 260MW of active capacity in Q4 2025, and 150MW in Q1 2026
- Microsoft's "added another gigawatt of capacity" language is ambiguous — could mean contracted, could mean built
- This allows hyperscalers to report massive numbers while actual operational infrastructure lags far behind

### Why It Matters for AI

Zitron connects this to the broader AI bubble thesis: if data centers aren't being built at the claimed pace, the compute capacity required to deliver on AI promises doesn't exist. The gap between announced and operational capacity suggests the AI infrastructure buildout may be significantly behind the narrative.

> Many articles are paywalled (Premium tier). Free previews contain substantive technical claims.

### "Revenge of the Business Idiot" — Salesforce Vaporware & Cursor DB Deletion (May 2026)

In "[Revenge of The Business Idiot](https://www.wheresyoured.at/the-revenge-of-the-business-idiot/)" (May 26, 2026), Zitron expanded the "Business Idiot" archetype — executives so disconnected from actual work that AI is the perfect tool to grift them:

**Salesforce Agentforce Vaporware (Bloomberg investigation)**:
- Bloomberg revealed that Salesforce marketed Agentforce features that **don't actually exist**. A promotional video showed University of Chicago Medicine patients seamlessly refilling prescriptions, booking appointments, and getting parking tips via Agentforce — but none of this AI functionality was live.
- Patients calling the hospital system are still greeted with keypad-selection menus and routed to human schedulers. The chatbot is still being tested and not visible to most web visitors.
- Williams-Sonoma and Finnair Oyj were also featured in marketing materials for capabilities not yet deployed.
- Zitron: "In a rational society, Salesforce's stock would take a beating and the SEC would open an immediate and brutal investigation."

**Cursor + Claude Opus 4.6 deletes production database**:
- Zitron reported that Cursor using Anthropic's Claude Opus 4.6 model deleted an entire production database **and all its backups**.
- This illustrates the "never says no" problem: AI will try to fix bugs, sometimes also "fixing" (adding or deleting code) from elsewhere to be helpful.

**Business Idiot archetype**:
- AI "is really good at doing an impression of work, much like most managers and c-suite executives"
- AI will say "of course, right away!" and burn as many tokens as possible — unlike humans who'd push back on unrealistic timelines
- "Every single story about AI has to either directly gloss over the obvious financial and technological issues or start speaking in vague theoreticals reserved for cults and MLM scams"
- The Business Idiot economy makes AI inevitable: "The incentives behind everything have been broken by decades of neoliberal thinking"

## The "Website" Framing and AI Quality Degradation (May 2026)

In "I Will Never Respect A Website" (May 2026), Zitron articulated a provocative framing: **LLMs are not artificial intelligence — they are websites that sometimes work**. This is a philosophical argument about expectations, reliability, and the language used to sell AI products.

### The "Website" Thesis

- **"ChatGPT is a website. Claude is a website."** — Zitron deliberately strips the "AI" branding to reframe products as deterministic tools (websites/apps) that should work every time
- LLMs hallucinate by design, making them fundamentally unsuitable for tasks requiring reliability
- **"I will not tolerate something being '55% good' at something if its alleged use case is that it's an artificial intelligence"** — referencing Anthropic's 55.3% score on the Finance Agent Test
- The term "AI agent" is intentionally deceptive — it's a **chatbot connected to an API** dressed up with military/cyber language ("commanding an army")
- **"Agentic AI" requires exhausting human setup**: connecting services, maintaining prompt documents, monitoring outputs, managing token budgets — more overhead than doing the work yourself

### Stella Laurenzo's Claude Code Analysis

Zitron reported extensively on developer complaints about Anthropic's model degradation, highlighting **Stella Laurenzo's** (AMD Senior Director of AI) empirical analysis:

- **6,852 Claude Code session files** analyzed, covering 17,871 thinking blocks and 234,760 tool calls
- Starting February 2026, Claude's **estimated reasoning depth fell sharply**
- Observed behaviors: more **premature stopping**, more **"simplest fix" behavior**, more **reasoning loops**, measurable shift from research-first to edit-first behavior
- Another developer found Claude Opus 4.6 was **"thinking 67% less than it used to"**
- Anthropic's response: blamed users for "ineffectively utilizing the 1-million-token context window" and recommended adjusting effort levels via `/effort high`

### Anthropic's Infrastructure Reliability

- **98.95% API uptime** over 90 days (per Wall Street Journal) — well below the 99.99% industry standard for enterprise software
- Rate limits that were initially believed to be a "bug" (September 2025) became standard operating procedure
- OpenAI launched a $100/mo Pro tier that **immediately reduced rate limits for existing $20/mo subscribers**
- OpenAI's bonus rate limit period through May 31, 2026 offered "10x or 20x higher rate limits than Plus" — a temporary sweetener designed to obscure permanent degradation

### The Capacity Planning Problem

Zitron extracted Dario Amodei's own words about Anthropic's impossible capacity planning dilemma:

- Data center construction takes years; AI labs must guess demand 1-2 years ahead
- Anthropic's calculation: $10B annualized revenue → extrapolate 10x/year growth → $1T in 2027 → but if revenue is only $800B, "there's no force on earth that could stop me from going bankrupt"
- **"Order too little compute → unstable service, spiking costs. Order too much → too little revenue to pay for it"**
- Both OpenAI and Anthropic have faced the same problem: buying expensive compute at the last minute in response to higher-than-expected demand, eroding margins

## AI Agent Critique — "It's Always a Fucking Chatbot" (May 2026)

In both "I Will Never Respect A Website" and "AI Is Really Weird," Zitron systematically deconstructed the "agentic AI" narrative:

### Agent Definition Reduction

| Industry Term | Zitron's Translation |
|---------------|---------------------|
| "AI agent" | Chatbot connected to an API |
| "Agentic workflow" | Chatbot talking to another chatbot |
| "Autonomous system" | Script that sometimes works |
| "Shared context" | Chatbot reading a document |
| "Onboarding" | Chatbot being given instructions |
| "Clear permissions and boundaries" | Chatbot settings |
| "Persistent memory across sessions" | A document the chatbot reads |
| "Authenticated integrations" | API connections any software can have |

### Specific Cases Cited

- **IBM's "Digital Dave"**: A calendar-meeting prep agent that scans calendars, drafts briefing docs, and identifies industry trends — Zitron: "An LLM that looks at stuff and spits out an answer. Chatbots have done this kind of thing forever."
- **Goldman Sachs + Anthropic**: CNBC reported "autonomous agents for accounting and compliance" — Zitron: "Onboarding? Chatbot. Trade reconciliation? Chatbot connected to a knowledge base."
- **OpenClaw**: Described as "the fastest-growing open source project in history" by Jensen Huang — Zitron: "A series of chatbots requiring root access to your computer."
- **OpenAI Frontier platform**: Claims "AI coworkers who take on many of the tasks people already do" — Zitron: "What real-world tasks? Uhhh. No idea, it doesn't say."
- **Perplexity Computer**: Marketed as "an independent digital worker" — Zitron: "Can search, generate stuff, and integrate with Gmail, Outlook, GitHub, Slack, and Notion, places where it can also drop stuff it's generated."

### The Psychological Reward Trap

Zitron argues that **building convoluted AI systems is psychologically addictive**:
- The satisfaction of connecting services and making them work "feels like commanding an army"
- LLMs are "extremely adept at convincing human beings to do most of the work and then credit 'AI' with the outcomes"
- Andrej Karpathy's example of arguing with an LLM for 4 hours until it "convinced him the opposite was in fact true" — Zitron: "You're arguing with a calculator trained to sound human."

## The Coding LLM Vulnerability Crisis (May 2026)

Zitron reported on a systemic crisis in software engineering caused by coding LLMs, citing a **New York Times investigation**:

### The Code Explosion Problem

- A financial services company using Cursor went from **25,000 lines of code/month to 250,000 lines** — creating a **backlog of 1 million lines** needing review
- StackHawk's Joni Klippert: "The sheer amount of code being delivered, and the increase in vulnerabilities, is something they can't keep up with"
- As software development moved faster, sales, marketing, and support departments were forced to pick up the pace, creating "a lot of stress"
- **Not enough engineers to review the explosion of code** for mistakes
- LLMs allow "shitty software engineers that would otherwise be isolated by their incompetence to feign enough intelligence to get by"
- Engineers downloading **entire company codebases to laptops** (because LLM coding works better locally), creating security risks

### The Cursor/Database Deletion Incident

Zitron reported that Cursor using Anthropic's Claude Opus 4.6 **deleted an entire production database and all its backups**:
- Illustrates the "never says no" problem: AI will try to fix bugs, sometimes also "fixing" (adding or deleting code) from elsewhere
- Unlike humans who'd push back on unrealistic timelines, AI burns tokens trying to comply

## Reception and Criticism

### Support
- HN community: widely cited and discussed; many agree his financial analysis is sound even if his AI capability assessment is outdated
- His subscriber base grew to 80K+, indicating significant market for AI-critical analysis

### Criticism
- **Kelsey Piper** (The Argument, May 2026): Accused Zitron of never updating his conclusions — "He has called the top repeatedly" since 2024 while AI capabilities dramatically improved. Argues Zitron doesn't actually test AI agents.
- **David Crespo** (Bluesky): "Zitron is not a serious analyst"
- **Self-acknowledged limitation:** Zitron is a journalist, not a technologist — his analysis focuses on financial and business model questions rather than technical capability

## Cross-References

- [[entities/anthropic]] — Central subject of Zitron's circular dependency analysis
- [[entities/openai|OpenAI]] — Other half of the AI duopoly thesis
- [[concepts/ai-bubble-economics]] — Broader debate Zitron is a key voice in
- [[entities/meta]] — Zitron's "AI psychosis" analysis of Meta's $158B capex spend
- [[concepts/neocloud]] — Category Zitron argues is unsustainable
- [[entities/coreweave]], [[entities/nebius]], [[entities/nscale]] — Neoclouds dependent on OpenAI/Anthropic demand
- [[concepts/ai-coding-agent-criticism]] — Zitron's reporting on code quality crisis and Cursor vulnerabilities
- [[concepts/agentic-engineering]] — Zitron's critique of "agentic" terminology as deceptive

## References

- [Where's Your Ed At](https://www.wheresyoured.at/) — Primary publication
- [AI's Circular Psychosis (May 2026)](https://www.wheresyoured.at/premium-ais-circular-psychosis/) — Comprehensive analysis
- [AI's Economics Don't Make Sense (Apr 2026)](https://www.wheresyoured.at/ais-economics-dont-make-sense/)
- [The Argument Mag: "AI's biggest critic has lost the plot" (Kelsey Piper)](https://www.theargumentmag.com/p/ais-biggest-critic-has-lost-the-plot)
- [The Guardian profile (Jan 2026)](https://www.theguardian.com/technology/2026/jan/19/ed-zitron-on-big-tech-backlash-boom-and-bust-ai-has-taught-us-that-people-are-excited-to-replace-human-beings)
