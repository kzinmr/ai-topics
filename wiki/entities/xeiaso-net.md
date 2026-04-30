---
title: Xe Iaso
type: entity
created: 2026-04-09
updated: 2026-04-27
tags:
- person
- blogger
- hn-popular
- infrastructure-engineering
- nix
- web-security
- free-software
aliases:
- xeiaso.net
- Cadey
- Xe
- Anubis
sources:
  - raw/articles/xeiaso.net--blog-2026-vibe-coding-sponsor-panel--10523b6c.md
  - raw/articles/xeiaso.net--blog-2026-ai-abstraction--744b692b.md
  - raw/articles/xeiaso.net--notes-2026-claude-code-wins-april-fools--f3f49e16.md
---

# Xe Iaso

| | |
|---|---|
| **Blog** | [xeiaso.net](https://xeiaso.net) |
| **RSS** | https://xeiaso.net/blog.rss |
| **GitHub** | [Xe](https://github.com/Xe) |
| **Patreon** | [xeiaso](https://patreon.com/xeiaso) |
| **Role** | Infrastructure engineer, open-source developer at Techaro |
| **Known for** | Anubis (AI scraper bot filter), Nix/NixOS advocacy, infrastructure engineering, prolific technical writing |
| **Bio** | Infrastructure engineer and open-source developer based in Canada (🇨🇦). Creator of Anubis, a widely-adopted proof-of-work challenge system for protecting websites against AI scrapers. Runs Techaro with a philosophy of open-source-first development. Prolific blogger covering infrastructure engineering, Nix, web security, and the social dynamics of the internet. |

## Core Ideas

Xe Iaso is an **infrastructure humanist** — someone who thinks deeply about the social and economic structures that underpin the internet, and builds tools to protect the small, independent web from the forces of scale and automation.

### Anubis: Protecting the Small Internet

Anubis, Xe's most impactful project, started as a response to a personal problem: **Amazon's web crawler was overloading their personal Git server**, ignoring `robots.txt` and working around restrictions. The project has since been adopted by GNOME, FFmpeg, Wine, UNESCO, SourceHut, FreeBSD, the Linux Kernel mailing list archives, and dozens of other projects.

The core insight: **the small internet is being crushed by automated scraping**, and traditional defenses (CAPTCHAs, `robots.txt`, rate limiting) are either too expensive or too easily bypassed. Anubis uses JavaScript-based proof-of-work challenges — imperceptible to real humans but computationally expensive for bots — to create an economic barrier to scraping.

> *"Anubis started out as a thing that I use to make my Git server not get bullied off the internet by Amazon's scraper. And it's sort of developed into a generic web application firewall."*

### The Threat Model of Popularity

Xe's essay on ["Building native packages is complicated"](https://xeiaso.net/blog/2025/anubis-packaging/) is a masterclass in **security-minded threat modeling for open-source maintainers**. When Anubis "hockey-sticked" in popularity, Xe faced a cascade of concerns:

- **Social proof as liability**: Being trusted by GNOME, FFmpeg, and UNESCO means any failure affects high-visibility organizations
- **Security software demands higher standards**: "Security software usually needs to be held to a higher standard than most other types of software"
- **The personal cost of maintaining trust**: "If this goes wrong, I'm going to get personally mega-cancelled"

Xe's Techaro standards — *"Be not a cancer upon the earth," "The purpose of a system is what it does"* — provide a philosophical framework for navigating these pressures.

### The Odd Number of Cores Bug

Xe discovered and wrote about a **processor topology bug** related to systems with an odd number of CPU cores — a finding that demonstrates their deep systems engineering instincts. The bug affects how thread pools and worker counts are calculated when the CPU count isn't evenly divisible, a class of error that only manifests on specific hardware configurations.

### The Small Internet Philosophy

Xe is a vocal advocate for the **"small internet"** — independent websites, personal servers, and community-scale infrastructure. Their work on Anubis is explicitly framed around this mission:

> *"The goal is to help protect the small internet so small communities can continue to exist at the scale they're currently operating at without having to resort to overly expensive servers or terrifyingly complicated setups."*

This philosophy extends to Xe's broader advocacy for self-hosting, open-source tooling, and infrastructure that doesn't require venture-scale resources to operate.

### Nix and Reproducible Infrastructure

Xe is a prominent voice in the Nix/NixOS community, advocating for **declarative, reproducible infrastructure** as the foundation for reliable systems. Their writing on Nix covers everything from development shells to production deployments, always with an eye toward practical, working solutions rather than theoretical purity.

### Claude Code /buddy: The Perfect April Fools Prank (2026)

Xe Iaso wrote a [short note](https://xeiaso.net/notes/2026/claude-code-wins-april-fools/) celebrating the Claude Code team's April Fools 2026 `/buddy` feature — a tamagochi-style coding companion that hatches when you run `/buddy` in Claude Code. Xe's robot companion, **Xentwine**, was described as:

> *"A methodical circuit-whisperer obsessed with untangling logical snarls; speaks in patient, patronizing riddles and will absolutely let you sit in your own bug for three minutes before offering the blindingly obvious fix."*

Xe's key observations on why this prank succeeded where others failed:

- **Opt-in by design**: You must manually create your buddy — off by default, no disruption
- **Non-intrusive**: Mostly stays out of the way during normal work
- **Tamagochi-like random interjections**: Adds personality without breaking flow
- **Interactive**: `/buddy pet` lets you pet your dragon, dog, or robot companion

Xe rated it **10/10** — calling it "the kind of harmless prank that all nerds should aspire for."

This note reflects Xe's broader appreciation for **well-designed developer tooling** and the human side of engineering culture — themes that run through their infrastructure and open-source work.

### The Human Cost of Automation

A recurring theme in Xe's writing is the **human impact of automated systems**. Whether it's AI scrapers overwhelming personal servers, or the social dynamics of open-source maintenance at scale, Xe consistently centers the human experience in infrastructure discussions. Their Patreon-funded development model is itself a statement: **important infrastructure work should be directly supported by the community that benefits from it**, not by venture capital or corporate sponsorship.

## Key Quotes

> *"The goal is to help protect the small internet so small communities can continue to exist at the scale they're currently operating at without having to resort to overly expensive servers or terrifyingly complicated setups."*

> *"Anubis started out as a thing that I use to make my Git server not get bullied off the internet by Amazon's scraper."*

> *"Security software usually needs to be held to a higher standard than most other types of software."*

> *"If this goes wrong, I'm going to get personally mega-cancelled."* — on the personal stakes of maintaining widely-trusted open-source security software

## Recent Blog Posts (2026)

Xe's recent writing in early-mid 2026 covers AI-assisted development and abstraction costs from an infrastructure engineer's perspective:

- **Vibe Coding Trip Report: Making a Sponsor Panel** (Apr 2026) — A practical experience report using Claude Code to build a conference sponsor panel. Key patterns: skills-as-context (writing instructions for the agent), mock-data-first iteration, and the "ugly but shipped" ethos. See [[concepts/harness-engineering/agentic-workflows/vibe-coding]] for analysis.
- **I Don't Know If I Like Working at Higher Levels of Abstraction** (Apr 2026) — A critical reflection on AI's impact on developer cognition and the cost of abstraction. Introduces the idea that "fine is the enemy of good" — AI's consistent mediocrity risks dulling human judgment. See [[concepts/harness-engineering/agentic-engineering]] for analysis.
- **Claude Code Won April Fools Day** (Apr 2026) — A lighthearted post about Claude Code's `/buddy` tamagochi feature during April Fools, praising it as a well-designed, opt-in prank that doesn't harm user productivity.

## Related

- [[concepts/small-internet]] — Protecting independent web infrastructure
- [[concepts/web-security]] — Proof-of-work challenges, bot filtering
- [[concepts/nixos]] — Declarative, reproducible infrastructure
-  — The social dynamics of maintaining popular projects
-  — Security-first thinking for open-source developers
-  — Xe's organization

## Sources

- [Anubis with Xe Iaso | Open Source Security](https://opensourcesecurity.io/2026/2026-01-anubis-xe/) (Jan 2026, podcast transcript)
- [Building native packages is complicated](https://xeiaso.net/blog/2025/anubis-packaging/) (2025)
- [Anubis works](https://xeiaso.net/notes/2025/anubis-works) (Apr 2025)
- [Weaponizing Hyperfocus](https://xeiaso.net/blog/weaponizing-hyperfocus/)
- [Anubis (software) — Wikipedia](https://en.wikipedia.org/wiki/Anubis_(software))
- [Xeiaso.net/about](https://xeiaso.net/about)
- [Claude Code won April Fools Day this year](https://xeiaso.net/notes/2026/claude-code-wins-april-fools/) (Apr 2026)
- [Vibe Coding Trip Report: Making a sponsor panel](https://xeiaso.net/blog/2026/vibe-coding-sponsor-panel/) (Mar 2026)

## References

- xeiaso.net--blog-2026-hospital-advice--d6becd3b
- xeiaso.net--blog-2026-seroquel-xanax-trip-report--3eb76d21
- xeiaso.net--blog-2026-some-thorns-have-roses--233fc2ff
- xeiaso.net--blog-2026-surgery-recovery-clankers--ebc6aee8
- xeiaso.net--notes-2026-ai-gpus-cant-process-graphics--12cd1c1c
- xeiaso.net--notes-2026-dns-fight--d224f8ab
- xeiaso.net--notes-2026-homelab-is-down--3bb3ebe4
