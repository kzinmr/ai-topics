---
title: Andrew Nesbitt
type: entity
status: active
tags: [person]
sources: []
---


# Andrew Nesbitt

**URL:** https://nesbitt.io
**Blog:** nesbitt.io
**Twitter/X:** @teabass
**GitHub:** @andrew
**Company:** Ecosyste.ms, Octobox
**Location:** Bristol, UK
**Flagship Creation:** Ecosyste.ms — the largest open dataset of OSS metadata (packages, repositories, dependencies)
**Notable Package:** node-sass — 1.3B+ downloads
**Podcast Host:** The Manifest (manifest.fm) — dedicated entirely to package management

---

## Overview

Andrew Nesbitt is one of the most focused specialists in the open source ecosystem: he has spent the last decade thinking almost exclusively about **package management, dependency graphs, and software supply chain security**. His work at Ecosyste.ms has built the largest open metadata dataset tracking packages, repositories, and dependencies across every major ecosystem. His GitHub profile description is famously straightforward: *"I've spent the last decade thinking about package management and git."*

Nesbitt's intellectual contribution is not in building flashy tools but in **mapping and understanding the hidden infrastructure** that underlies all of software development. Ecosyste.ms catalogs 11.4 million packages, 262 million repositories, and 22 billion dependencies — a scale that makes it the definitive lens through which to understand how open source actually works.

His approach is characterized by **observational rigor**: he collects data, identifies patterns, and draws conclusions that challenge conventional wisdom. His podcast *The Manifest* is the only audio program dedicated entirely to package management, and he has appeared on The Changelog, Sustain, CHAOSScast, Open Source Security, and more. He is a vocal participant in OpenSSF, Alpha-Omega, CycloneDX, and CHAOSS communities.

Nesbitt's writing has become notably more prolific and philosophically rich in 2025–2026, exploring not just the technical but the **psychological and structural dimensions** of open source — from dependency confusion attacks via LLMs to guided meditation for developers stressed about their dependency trees.

---

## Timeline

| Date | Event |
|------|-------|
| 2008-02-27 | Joins GitHub (early adopter, 166 public repos) |
| 2013 | Talks on Nodecopter, JavaScript in the Real World, robotics |
| 2013-2014 | Node.js hardware hacking era — drone control, meetup organizing |
| 2014 | Hackference: "Robotics 101"; jQuery UK: "The Rise of JavaScript Hardware Hacking" |
| 2015 | South-West Elastic: "Elasticsearch on Rails" |
| 2016 | node-sass reaches 1.3B+ downloads; 24 Pull Requests gains traction |
| 2017 | Brighton Ruby: "Can my friends come too?" — on OSS community building |
| 2018 | Bath Ruby: "With a Little Help from My Friends" |
| 2019 | Republishing npm dependencies to IPFS as a micro-registry (FOSDEM) |
| 2019-2020 | Creates Libraries.io and Ecosyste.ms; starts The Manifest podcast |
| 2021 | Content Addressed Package Management talk |
| 2022 | Ecosyste.ms formally established; first major grant funding |
| 2023 | Ecosyste.ms 2023 Year End Update; package management research intensifies |
| 2024 | Major blog output begins: "How I Assess Open Source Libraries," "Why I'm Fascinated by Package Management," LLM dependency confusion research |
| 2025 | Podcast appearances on Open Source Security, Sustain, CHAOSScast; "State of OSS Funding" talk at CHAOSScon; "Introducing Package Chaos Monkey"; "PromptVer" (semver for LLMs); "git-pkgs" dependency history tool; OSS Community Benchmarks project |
| 2026 | FOSDEM talk: "Open source funding: you're doing it wrong" (with Benjamin Nickolls); OSS Summit NA panel on funding; EasyBuild User Meeting: "Ecosyste.ms: Exploring Open Source Software Landscapes"; available for consulting on package management and supply chain security; "Guided Meditation for Developers"; "Package Manager Magic Files"; ".gitlocal" — Git should let files ignore themselves |
| Active through Apr 2026 | 3500+ GitHub followers, 166 repos, active contributions to ecosyste-ms, octobox, git-pkgs |

---

## Core Ideas

### "Why I'm Fascinated by Package Management"

Nesbitt traces his obsession back to **gaming magazine cover CDs** — the physical act of collecting, installing, and managing software from magazines sparked an early interest that evolved into a career-long focus. His thesis is that package management is the **central nervous system of modern software development**, yet it remains poorly understood and under-investigated. He argues that the dependency graph is not just a technical artifact but a **social graph** — it encodes relationships between developers, organizations, and communities.

> *"From gaming magazine CDs to dependency graphs"*

This personal-to-professional arc is rare: he found a niche so specific and so foundational that few others even recognize it as a distinct field of study.

### The 22-Billion-Dependency Problem

Ecosyste.ms tracks **22 billion dependency links** between packages and repositories. This number is Nesbitt's most compelling data point for understanding modern software: an astonishingly small number of packages serve as **critical infrastructure** for the entire open source ecosystem. His research demonstrates that most software is built on a handful of shared dependencies, creating systemic risk that most organizations don't understand.

This leads directly into his work with OpenSSF and Alpha-Omega on **supply chain security**: if you don't know what you depend on, you can't secure it.

### LLMs as a Supply Chain Attack Vector

In 2024-2025, Nesbitt identified a novel security concern: **LLMs can leak internal package names, making dependency confusion attacks easier to scale**. When developers paste internal code or package names into AI models, those models may inadvertently expose proprietary package namespaces to the public internet. This was one of the earliest articulations of AI-specific supply chain risk in the package management domain.

> *"The LLM itself becomes the attack vector."*

### "Guided Meditation for Developers"

In early 2026, Nesbitt published a satirical-but-serious piece: *"A practice for finding peace in your dependency tree."* This piece reveals his understanding of the **psychological toll** of dependency management. Modern developers are overwhelmed by the sheer complexity of their dependency graphs — hundreds of transitive dependencies, each with their own update cycles, security advisories, and compatibility requirements. The "meditation" is both humor and genuine advice: you can't control the complexity, but you can learn to observe it without panic.

### Package Manager Magic Files

In February 2026, Nesbitt documented the **hidden configuration files** that package managers use: `.npmrc`, `MANIFEST.in`, `Directory.Packages.props`, `.pnpmfile.cjs`, and more. His analysis reveals that each package manager has its own "magic file" ecosystem — a parallel configuration language that developers must learn in addition to the package manager's documented interface. This is classic Nesbitt: finding the invisible infrastructure and making it visible.

### "Git Should Let Files Ignore Themselves"

In his `.gitlocal` concept (2026), Nesbitt proposes that Git should support **file-level ignore directives** — individual files declaring their own ignore rules. This extends his broader thesis that the current model (centralized `.gitignore` files maintained by humans) doesn't scale to modern project complexity. If a generated file knows it shouldn't be tracked, it should be able to say so.

### Categorizing Package Manager Clients

Nesbitt's 2025 analysis categorized package managers by **resolution algorithms, lockfile strategies, build hooks, and manifest formats**. This taxonomy is his most systematic contribution to understanding the package management landscape: instead of treating all package managers as equivalent, he maps their architectural differences and the trade-offs each makes. This work underpins his consulting practice and informs organizations choosing tooling.

### How to Assess Open Source Libraries

In a 2024 post, Nesbitt outlined his personal methodology for evaluating whether to adopt a dependency. His criteria go beyond GitHub stars and download counts: he looks at **maintenance velocity, dependency health, security posture, license compatibility, and the package manager's own metadata**. This is practical wisdom from someone who has seen the entire dependency graph.

### The "Package Chaos Monkey"

In 2026, Nesbitt introduced the concept of **resilience engineering for software supply chains** — deliberately testing what happens when dependencies fail. This extends Netflix's Chaos Monkey philosophy to the dependency layer: if a critical package disappears or introduces a breaking change, does your system survive?

### PromptVer: Semver for the LLM Age

Nesbitt's "PromptVer" proposal (2025) introduces a **semver-compatible versioning scheme designed specifically for LLM-generated content and prompts**. This recognizes that prompts and AI-generated code evolve differently than traditional software — they need versioning that accounts for model drift, prompt refinement, and non-deterministic outputs.

---

## Key Quotes

> *"I've spent the last decade thinking about package management and git."*

> *"From gaming magazine CDs to dependency graphs."* — on why he's fascinated by package management

> *"The npm client's default settings are a root cause of JavaScript's recurring supply chain security problems."*

> *"I'm not connecting these dots. I'm just pointing out that the dots are there."* — on open source conspiracies

> *"A practice for finding peace in your dependency tree."* — Guided Meditation for Developers

> *"LLMs can leak internal package names, making dependency confusion attacks easier to scale."*

---

## Writing Style & Philosophy

Nesbitt writes with **analytical precision and dry humor**. His posts are typically:

- **Data-driven** — backed by Ecosyste.ms datasets with real numbers
- **Taxonomic** — he creates classification systems (package manager types, assessment frameworks)
- **Observational** — he identifies patterns others miss, then documents them clearly
- **Slightly subversive** — his "guided meditation" and "conspiracy" posts reveal a playful side beneath the serious analysis
- **Community-oriented** — he actively solicits contributions, runs podcasts, and speaks at conferences
- **Anti-monetization of ideas** — his research and datasets are freely available via open APIs

His blogging cadence accelerated dramatically in 2025–2026, with 25 posts in January 2026 alone. This suggests a shift from building infrastructure to **communicating what the infrastructure reveals**.

---

## Technical Breadth

- **Package Management:** Resolution algorithms, lockfiles, manifest formats, build hooks, mirroring protocols, magic files
- **Software Supply Chain Security:** Dependency confusion, typosquatting, trusted publishing, SBOMs, SARIF, PURL, VERS, SWHID
- **Dependency Graphs:** 22 billion links, critical path analysis, ecosystem mapping
- **Git Internals:** Remote helpers, diff drivers, filters, hooks, subcommands, file-level ignores
- **Open Source Metadata:** Ecosyste.ms platform, APIs, rate limiting, data curation
- **OSS Community Dynamics:** Funding models, maintainer burnout, contribution incentives
- **LLM/AI Security:** Prompt versioning, model-based attack vectors, AI-assisted dependency analysis
- **Multiple Ecosystems:** Ruby gems, npm, Python/PyPI, Go modules, GitHub Actions

---

## Recent Themes (2024–2026)

- **Supply chain security:** npm defaults, dependency confusion, LLM attack vectors
- **Package manager taxonomy:** Categorizing clients by architecture, not just ecosystem
- **Dependency assessment methodology:** How to actually evaluate whether to adopt a library
- **OSS funding critique:** "Open source funding: you're doing it wrong" (FOSDEM 2026)
- **Resilience engineering:** Package Chaos Monkey, testing dependency failure modes
- **LLM-specific tooling:** PromptVer, semver for AI-generated content
- **Git extensibility:** .gitlocal, remote helpers, diff drivers
- **Developer psychology:** Guided meditation for dependency anxiety
- **Community benchmarking:** OSS Community Benchmarks where maintainers define what good AI-generated code looks like
- **Consulting availability:** Leveraging Ecosyste.ms expertise for organizational guidance

---

## Related

- [[Package Management]] — Resolution algorithms, lockfiles, manifests, supply chain security
- [[Software Supply Chain Security]] — PURL, VERS, SBOM, SWHID, SARIF specifications
- [[Dependency Graphs]] — Mapping the 22 billion dependency links in open source
- [[Open Source Metadata]] — Ecosyste.ms as the definitive catalog
- [[LLM Security]] — AI as a novel attack vector in dependency management
-  — Sustainable models for open source infrastructure
-  — Remote helpers, diff drivers, file-level ignore directives
-  — Package Chaos Monkey and dependency failure testing

---

## Influence

- **Ecosyste.ms** catalogs 11.4M packages, 262M repositories, 22B dependencies — the largest open metadata dataset
- **node-sass** achieved 1.3B+ downloads — one of the most-downloaded npm packages ever
- **The Manifest** podcast is the only audio program dedicated to package management
- **Libraries.io** — open source discovery service
- **24 Pull Requests** — holiday OSS contribution initiative
- Active contributor to Alpha-Omega, OpenSSF, CycloneDX, CHAOSS
- 3500+ GitHub followers, 166 public repositories
- Regular podcast guest: The Changelog (#665, #327, #188), Sustain (#270, #159), CHAOSScast (#121, #115), Open Source Security, Request For Commits (#3), Bet On Yourself (#22)
- Conference speaker at FOSDEM, EasyBuild, OSS Summit NA, Brighton Ruby, Bath Ruby, Full Frontal, LXJS, jQuery UK, Hackference

---

## Sources

- nesbitt.io — Personal blog and portfolio
- Ecosyste.ms — Open metadata platform (ecosyste.ms)
- The Manifest podcast (manifest.fm)
- "Why I'm Fascinated by Package Management" (2024)
- "How I Assess Open Source Libraries" (2024)
- "Guided Meditation for Developers" (2026)
- "Package Manager Magic Files" (2026)
- "Introducing Package Chaos Monkey" (2026)
- "PromptVer: A semver-compatible versioning scheme for the age of LLMs" (2025)
- ".gitlocal: Git Should Let Files Ignore Themselves" (2026)
- "Categorizing Package Manager Clients" (2025)
- GitHub: @andrew (166 public repos, joined 2008)
- Open Source Security podcast: "Ecosyste.ms with Andrew Nesbitt" (2025)
- FOSDEM 2026: "Open source funding: you're doing it wrong" (with Benjamin Nickolls)
- OSS Summit NA 2026 panel: "The Impact of Funding" (with Georg Link, Dawn Foster, Alyssa Wright)
