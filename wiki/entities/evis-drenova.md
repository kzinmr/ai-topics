---
title: Evis Drenova
type: entity
created: 2026-05-08
updated: 2026-05-23
status: L2
tags:
  - person
  - entrepreneur
  - coding-agents
  - search
  - infrastructure
  - privacy
  - ycombinator
  - software-engineering
sources:
  - "raw/articles/2026-05-06_entire-improving-agentic-search-in-coding-agents.md"
  - https://www.evis.dev/
  - https://evis.substack.com/
  - https://github.com/evisdren
  - https://www.linkedin.com/in/evis-drenova-89857944
  - https://talent.substack.com/p/why-i-joined-evis-drenova-entire
aliases:
  - "@evisdrenova"
  - "edrenova"
  - "evisdren"
---

# Evis Drenova

**Evis Drenova** (@evisdrenova) is a Principal Software Engineer at **Entire**, the developer platform founded by former GitHub CEO Thomas Dohmke. Previously, he co-founded **Neosync** (YC S22), an open-source data security company specializing in synthetic data, which was acquired by Grow Therapy (Sequoia-backed). His career spans the full stack of modern software — from AI agent infrastructure and data privacy to Rust systems programming and enterprise product management.

## Key Facts

| Field | Value |
|-------|-------|
| X Handle | [@evisdrenova](https://x.com/evisdrenova) |
| Website | [evis.dev](https://www.evis.dev/) |
| GitHub | [github.com/evisdren](https://github.com/evisdren) |
| LinkedIn | [evis-drenova-89857944](https://linkedin.com/in/evis-drenova-89857944) |
| Substack | [The Early Days](https://evis.substack.com/) |
| Role | Principal Software Engineer @ Entire (2026–present) |
| Previous | CEO/Co-founder @ Neosync (YC S22, acq. Grow Therapy) |
| Education | University of Chicago Booth (MBA), UMass Amherst (BS) |
| Location | San Francisco, CA |
| Background | Albanian-born, grew up in Boston |

## Biography

### Early Life & Education

Evis Drenova was born in Albania and grew up in Boston, Massachusetts. He earned a Bachelor's degree from the **University of Massachusetts Amherst** (2009–2013), followed by an **MBA from the University of Chicago Booth School of Business** (2018–2020). 

### Early Career (2013–2018)

Drenova began his career in enterprise software sales and consulting:
- **Experian Data Quality** (2013–2015) — Sales Development Associate → Inside Account Manager → Account Executive
- **Oracle** (2015) — Enterprise Application Sales and Consulting
- **IBM** (2015–2018) — Senior Consultant → Managing Consultant, Global Business Services

### TrueData & Skyflow (2018–2022)

Moving into product management and privacy engineering:
- **TrueData** (2018–2020) — Product Manager → Director of Product Management. TrueData partnered with mobile app publishers to aggregate mobile data for marketing and analytics
- **Skyflow** (2020–2022) — Lead Product Manager. Skyflow provides a data privacy vault architecture to isolate, protect, and govern sensitive data. Drenova was an early product hire at the company

During this period, he also served as an **MBA Associate at Foundation Capital** (2020), giving him exposure to VC and early-stage investing.

### Neosync (2022–2025)

In June 2022, Drenova co-founded **Neosync**, part of the **YC S22** batch. Neosync built an open-source data replication and anonymization platform that specialized in **synthetic data** — creating production-like, privacy-safe datasets for development and testing.

Key milestones:
- Grew from $0 to $150K in 6 months, then executed a strategic pivot
- Built distributed data security platform from zero to acquisition
- **Acquired by Grow Therapy** (August 2025) — a leading behavioral health platform backed by Sequoia. Drenova and co-founder Nick Zelei joined Grow Therapy to bring Neosync's privacy-first technology into mental healthcare
- Drenova stayed at Grow Therapy for his earn-out period, then left to join Entire

> "Nick Zelei and I started Neosync with the vision to give developers access to high quality, production-like synthetic data to unlock the value of that data without worrying about data privacy and security."

### Entire (2026–present)

In early 2026, Drenova joined **Entire** as a **Principal Software Engineer**. Entire was founded by former GitHub CEO Thomas Dohmke and raised the largest seed round in dev tools history: **$60M at a $300M valuation** from Felicis, Madrona, M12, and angels including Datadog's CEO, YC's CEO, and Jerry Yang.

Drenova's path to Entire was unusual: he had been exploring agentic coding infrastructure independently on weekends, starting an open-source project rethinking Git for the era of coding agents. His blog post on the topic reached Thomas Dohmke, leading to a conversation that turned into a full-time job.

> "The basic premise was that Git wasn't built to handle agentic coding from a performance perspective, so what would it look like to reinvent it?"

He turned down offers from 2 foundational model labs (OpenAI/Anthropic-level) to join a smaller team — motivated by "working on hard problems with really smart people in a small team at the forefront of an industry."

## Key Research

### Agentic Code Search Study (May 2026)

Drenova authored the landmark study *"How We Improved Agentic Search"* while at Entire, analyzing **1,983 real coding-agent checkpoints** (~202K tool calls) from Entire's open-source CLI:

- **48.8% of all tool calls are search-related** (file reads, grep, bash fallback)
- **Faster search does NOT mean faster agents**: Even a 9× search speedup only improved end-to-end runtime by 1.6%
- **Better ranking improves agent accuracy**: pgr's Hit@1 went from 26% → 34% (implementation tasks: 14.3% → 42.9%)
- **Tool execution bottleneck**: Only ~0.4% of total agent wall clock — the real bottleneck is model inference + planning, not search speed

This is one of the first public, data-driven analyses of how coding agents actually spend their time and what truly improves their effectiveness.

## Writing & Philosophy

### Blog: evis.dev

Drenova maintains a technical blog at [evis.dev](https://www.evis.dev/) covering AI, systems programming, and philosophy:

#### Technical Deep Dives
- **"From Matmul to Meaning"** (Oct 2025) — Three-part series on how neural networks learn, starting from matrix multiplication
- **"Porting Llama2.c to Rust"** (Sep 2025) — Systems-level ML implementation
- **"Building an Autograd System in Rust"** (Nov 2025) — Rust ML infrastructure
- **"Benchmarking Tensor Operations in Rust"** (Jul 2025) — Performance engineering

#### AI & Society
- **"A Code-Abundant World"** (Dec 2025) — Speculative essay on what happens when coding agents produce vast amounts of code
- **"Memory in AI Agents"** (Jul 2025) — Agent memory architecture exploration
- **"Are Proactive Agents Next?"** (Jun 2025) — Prediction on agent evolution
- **"Does It Matter Who Writes the Code?"** (Aug 2025) — Code authorship in the age of agents
- **"Is This Time Different?"** (Oct 2025) — Reflections on the AI hype cycle

#### Startups & Career
- **"Plant a Flag"** (Dec 2025) — Career advice on committing to hard problems
- **"Product Taste"** (Dec 2025) — How to develop product intuition
- **"Embrace the Logarithms"** (Jan 2026) — Thinking in scales and orders of magnitude

### Substack: The Early Days

Drenova also writes [The Early Days](https://evis.substack.com/), focused on startup lessons, enterprise sales, and early-stage reflections.

### Intellectual Themes

Drenova's writing consistently explores:
- **Systems thinking** — Understanding how pieces compose into larger wholes (from Rust autograd to agent infrastructure)
- **Privacy-first engineering** — Building for data security by default (through Neosync and Skyflow)
- **Multi-disciplinary synthesis** — Moving between ML, systems programming, and business strategy
- **Honest reflection** — Willingness to share failures and missteps (pivots, enterprise sales lessons)

## Career Timeline

| Period | Role | Company |
|--------|------|---------|
| 2026–present | Principal Software Engineer | Entire |
| 2025–2026 | Staff Product Manager | Grow Therapy (acquirer) |
| 2022–2025 | Co-founder & CEO | Neosync (YC S22) |
| 2020–2022 | Lead Product Manager | Skyflow |
| 2019–2020 | Director of Product Management | TrueData |
| 2020 | MBA Associate | Foundation Capital |
| 2018–2019 | Product Manager | TrueData |
| 2015–2018 | Managing Consultant → Senior Consultant | IBM |
| 2015 | Enterprise Sales | Oracle |
| 2013–2015 | Account Executive → SDA | Experian Data Quality |

## Related Pages

- [[entities/entire]] — Entire, AI agent observability & search platform
- [[entities/thomas-dohmke]] — Entire founder, ex-GitHub CEO
- [[concepts/agentic-search]] — Agentic code search

## Sources

- [evis.dev](https://www.evis.dev/) — Personal website and blog
- [The Early Days (Substack)](https://evis.substack.com/) — Startup reflections
- [LinkedIn: Evis Drenova](https://linkedin.com/in/evis-drenova-89857944)
- [Why I Joined: Evis Drenova / Entire](https://talent.substack.com/p/why-i-joined-evis-drenova-entire)
- Raw article: 2026-05-06_entire-improving-agentic-search-in-coding-agents.md
