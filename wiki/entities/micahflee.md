---
title: "Micah Lee"
tags: [person, coding-agents, local-llm]
sources:
  - raw/articles/micahflee.com--agentic-coding-techniques--fc5e06aa.md
  - raw/articles/micahflee.com--mandatory-update-a-short-story--a332b287.md
  - raw/articles/micahflee.com--sandboxing-coding-agents--2355e89c.md
created: 2026-04-24
updated: 2026-08-28
type: entity
---


# Micah Lee

## Overview

**Micah Lee** (he/him, pronounced "my-kah") is a security researcher, investigative data journalist, software engineer, and author. He is best known for building practical open-source privacy tools, analyzing leaked datasets, and advocating for tech activism that empowers journalists and ordinary citizens against state and corporate surveillance.

His work spans the full stack of information security — from developing widely used tools like **OnionShare** (secure file sharing over Tor) and **Dangerzone** (malware-safe document sanitization), to founding the **Lockdown Systems Collective**, which builds local-first alternatives to Big Tech data extraction (notably the [[concepts/cyd]] app). He is the author of *Hacks, Leaks, and Revelations: The Art of Analyzing Hacked and Leaded Data* (No Starch Press, 2024), a practical guide for journalists and activists working with leaked datasets.

Previously: Director of Information Security at [[concepts/the-intercept]] (where he handled OPSEC during the Edward Snowden leaks), Staff Technologist at the [[concepts/electronic-frontier-foundation]], and co-founder of . His journalism has appeared in *The Intercept*, *404 Media*, *WIRED*, and *Zeteo*.

---

## Timeline

| Period | Key Events |
|--------|-----------|
| 2013 | Provides OPSEC for journalists covering the  NSA leaks |
| 2014 | Develops **OnionShare** — open-source file sharing over [[concepts/dark-factory-software-factory]] |
| 2014–2024 | Director of Information Security at [[concepts/the-intercept]]; leads the SIDtoday Files project |
| 2016–2019 | Leads comprehensive reporting on NSA Signals Intelligence Directorate documents |
| 2018 | Reports on leaked WikiLeaks DMs with Cora Currier |
| 2020 | Develops **Dangerzone** — converts potentially malicious documents to safe PDFs |
| 2022 | Co-publishes investigation on TeleMessage spyware used by Trump officials |
| 2024 | Publishes *Hacks, Leaks, and Revelations* (No Starch Press) |
| 2025 | Founds **Lockdown Systems Collective**; develops [[concepts/cyd]] app; reports on [[concepts/iceblock]] app security failures; delivers BSidesPDX keynote on "Technofascism" |
| 2026 | Publishes Epstein files analysis on ; builds DHS Contracts Explorer from hacked data; writes extensively on Signal group nicknames, mercenary spyware, and app censorship |

---

## Core Ideas

### Technofascism and the Weaponization of Surveillance

Lee coined the term **"technofascism"** to describe the fusion of authoritarian governance with modern surveillance technology. In his October 2025 BSidesPDX keynote *Practical Defenses Against Technofascism*, he argues that the U.S. is experiencing "imperialism turned inward" — the same surveillance infrastructure once deployed abroad is now being directed at domestic populations.

> "What we've been seeing on the streets of the US, with ICE kidnappings and military invasions of cities, is the normal face of fascism, just with new technology."

His framework identifies several vectors of technofascist control: **mercenary spyware** (Paragon's Graphite, NSO Group's Pegasus), **device extraction** (Cellebrite), **cell-site simulators** (Stingrays), and **platform complicity** (Apple/Google voluntarily censoring apps at government request). Lee's analysis goes beyond technical threat modeling — he situates surveillance within a broader political economy where private tech companies are active collaborators, not reluctant participants.

### Open Source as Moral Imperative

A throughline of Lee's work is the conviction that security and privacy tools **must be open source** to be trustworthy. His critique of the ICEBlock app is illustrative:

> "This is, of course, not how secure software works. The most widely trusted security and privacy tools that people use are all open source. And the thing that makes this perfectly reasonable and safe is code review. If Joshua published the ICEBlock source code, people could verify his claims."

For Lee, closed-source security is an oxymoron. He extends this principle to his own tools — OnionShare, Dangerzone, and Cyd are all open source. His activism includes not just building tools, but publicly critiquing closed-source "activism theater" that claims to protect vulnerable populations while remaining unauditable.

### Collective Security Over Individual Hardening

Lee is skeptical of "personal OPSEC" culture that places the entire burden of privacy on individuals. His work consistently emphasizes **collective defense** and **community infrastructure**:

- The **Lockdown Systems Collective** builds tools designed for group coordination, not solo use
- His Signal group nickname post (January 2026) addresses a social engineering problem — group members with cryptic names like "E" or "🥑" undermine trust verification
- He recommends community-led rapid response networks over individual app-based solutions

> "Defenses must be collective, not individual, built on a shared, forgiving security culture."

### Data Journalism as Democratic Accountability

Lee's work with leaked datasets — from the NSA SIDtoday files to the Epstein documents to DHS contractor records — represents a consistent philosophy: **hacked and leaked data, when responsibly analyzed, is a critical tool for democratic accountability**. His book *Hacks, Leaks, and Revelations* systematizes this practice, teaching journalists how to download, verify, analyze, and report on leaked datasets without compromising sources or spreading misinformation.

His Epstein files work (November 2025) demonstrates this in action: taking 26,000+ documents, indexing them with Google Pinpoint for public searchability, and using entity extraction to map relationships between powerful figures. His DHS Contracts Explorer (March 2026) similarly transforms 17MB of raw JSON into an accessible, filterable visualization of government spending on immigration enforcement.

### Platform Complicity and App Store Censorship

Lee has been a vocal critic of Apple and Google's voluntary compliance with government censorship requests. When the Trump administration pressured Apple to remove ICEBlock, he framed it as a fundamental threat:

> "Native app stores are centralized choke points. Code is speech. The Trump administration pressuring Apple and Google to censor their app stores is a violation of the First Amendment."

He advocates for **web-based alternatives** to native apps precisely because they bypass these choke points. The survival of the "Eyes Up" web app (which archives ICE abuse footage) while native apps are removed illustrates his argument for decentralized, web-first organizing tools.

### Agentic Coding (2026)

In his August 2026 essay *Agentic coding techniques*, Lee describes coding agents as "actually useful" — an incredible time saver when the output is reviewed by someone who understands the code — in contrast to the AI slop flooding the internet. He pairs this pragmatism with a scathing critique of the AI industry, which he calls "a bubble built on hype and lies and debt": environmentally destructive data centers, power consolidated among "reactionary billionaire weirdos" chasing military contracts, and loss-leading pricing ($20/month plans that cost providers more than they earn). Believing frontier models are "cheaper now than they ever will be again," he intends to use them while he can; GitHub Copilot's switch to usage-based billing in June 2026 made it "way too expensive," so he stopped using it (keeping VS Code as his editor).

**Local open-weight models.** Lee runs a Framework Desktop server with 128GB of RAM and a GPU hosting an [[concepts/ollama]] server for private, local models. His best local coding model is `qwen3-coder-next:q8_0` (84GB); his best vision model is `qwen3-vl:32b-thinking-q8_0` (35GB). He reserves local LLMs for: code generation for secret projects whose source code — or very existence — can't be shared with third parties; direct analysis of sensitive datasets (frontier models often write the analysis code, which then runs against private data); a private Open WebUI chatbot; and large batches of small repetitive tasks. This local-first stance extends his [[concepts/open-source]] moral imperative to model weights.

**LLM skills workflow.** Lee adopted Matt Pocock's LLM skills, which "entirely changed" his agentic workflow: the **grilling session** skill has the LLM relentlessly question him about a feature to surface thorny implementation details and write a spec *before* any code; **/to-tickets** turns a detailed spec into GitHub issues automatically labeled "ready-for-agent" or "ready-for-human"; **/implement** can implement an entire well-defined issue in one go, including code review and a pull request. He also uses Expo Skills for thorny-but-tedious mobile maintenance and tracks Trail of Bits' skills repo for security research.

**Sandboxing agents.** Because autonomous agents require "extremely unsafe YOLO mode" — `claude --dangerously-skip-permissions` or `codex --dangerously-bypass-approvals-and-sandbox` — Lee runs them inside Docker Sandboxes (`sbx` command), preferring CLI versions of Claude and Codex over desktop apps because they're easier to sandbox. Each sandbox runs its own Docker VM (no shared Linux kernel), supports nested Docker (so Docker Compose test suites still work), proxies all network access through a host firewall with an allowed-domains allowlist (GitHub, NPM, PyPi by default, configurable per-sandbox), and provides per-sandbox credential isolation. See [[concepts/sandbox]] and [[concepts/agentic-engineering]] for related analysis.

**Isolating GitHub access.** Lee refuses to browser-login `gh` with full account access inside agent sandboxes — a prompt-injected agent could otherwise read all his secret repositories. Instead he creates fine-grained, repo-scoped personal access tokens (PATs) stored in the `sbx` secrets manager scoped to the specific sandbox, and forwards a dedicated signing-only SSH key into the container for commit signing. A rogue agent is thus contained to a Docker container *and* a single GitHub repo.

**Agent-transparency commit signing (Aug 2026).** In the follow-up *Sandboxing coding agents*, Lee details the setup end-to-end and argues everyone should be transparent about AI use in code: commits made by LLMs should (1) use an author name that makes clear it's not a human, and (2) be signed with a dedicated agent-only SSH key. He generates a separate `~/.ssh/agent-signing-key`, registers its public key on GitHub as a **signing key only** (never an authentication key — otherwise the agent could clone everything his account can access), and provides a `start-isolated-ssh.sh` script that spins up an isolated `ssh-agent` loading only the agent signing key before forwarding it into the Docker Sandbox. This makes "verified" commits attributable to the agent without exposing his personal/Yubikey-backed identity or the rest of his repos. See [[raw/articles/micahflee.com--sandboxing-coding-agents--2355e89c.md]].

---

## Key Quotes

> "What we've been seeing on the streets of the US, with ICE kidnappings and military invasions of cities, is the normal face of fascism, just with new technology."

> "Code is speech. The Trump administration pressuring Apple and Google to censor their app stores is a violation of the First Amendment."

> "This is, of course, not how secure software works. The most widely trusted security and privacy tools that people use are all open source."

> "Defenses must be collective, not individual, built on a shared, forgiving security culture."

> "Any person whose device was confiscated and later returned by a security service should assume that the device can no longer be trusted without detailed, expert analysis." — *citing Citizen Lab*

> "Native app stores are centralized choke points."

---

## Recent Themes (2024–2026)

**2024:** Published *Hacks, Leaks, and Revelations* — systematizing his methodology for working with leaked datasets as a form of democratic journalism.

**2025:** Founded the [[concepts/lockdown-systems-collective]] and began developing [[concepts/cyd]], an open-source app for local-first personal data backup. Delivered his BSidesPDX keynote on technofascism. Published critical analysis of the ICEBlock app as "activism theater." Co-reported on TeleMessage spyware. Published Epstein files analysis for .

**2026:** Built the DHS Contracts Explorer from hacked immigration enforcement data. Published practical guides on Signal group security (nicknames as identity verification). Continued analysis of mercenary spyware threats (Paragon/Graphite, NSO/Pegasus) and platform complicity. Active on the kill switch podcast discussing app censorship. Published *Agentic coding techniques* (August 2026) on [[concepts/agentic-engineering|agentic engineering]] — local open-weight models, LLM skills, and Docker-sandboxed coding agents. Also wrote his first short story, *Mandatory Update* (DEF CON 34 Creative Writing Contest entry; AI deepfake theme via the fictional SlopstreamAI).

---

## Related

[[concepts/onionshare]] — Lee's flagship tool for secure, anonymous file sharing over Tor
[[concepts/dangerzone]] — Document sanitization tool for journalists handling untrusted files
[[concepts/cyd]] — Local-first data backup app developed through Lockdown Systems Collective
[[concepts/dark-factory-software-factory]] — Anonymity network central to Lee's tooling philosophy
[[concepts/signal]] — Encrypted messaging platform Lee advocates and analyzes
[[concepts/the-intercept]] — Former employer; Lee directed information security for a decade
[[concepts/electronic-frontier-foundation]] — Former employer as staff technologist
 — Co-founded by Lee
 — Lee provided OPSEC during the NSA document leaks
 — Current publication outlet for investigative journalism
BSidesPDX — Venue for Lee's "Technofascism" keynote
TeleMessage — Israeli spyware company investigated by Lee
Cellebrite — Device extraction company analyzed in Lee's technofascism framework

---

## Sources

- [micahflee.com](https://micahflee.com) — Personal blog and portfolio
- [micahflee.com/about](https://micahflee.com/about) — Biography and project list
- *Practical Defenses Against Technofascism* (BSidesPDX Keynote, October 2025)
- *Unfortunately, the ICEBlock app is activism theater* (September 2025)
- *ICEBlock handled my vulnerability report in the worst possible way* (September 2025)
- *How to easily dig through the Epstein files yourself* (November 2025)
- *Jeffrey Epstein Bought Books About Pedophilia, Woody Allen, and Trump* (Zeteo, November 2025)
- *"Why hack the DHS? I can think of a couple Pretti Good reasons!"* (March 2026)
- *Agentic coding techniques* (August 2026)
- *I spoke about ICEBlock and Trump's app censorship on the kill switch podcast* (October 2025)
- *Hacks, Leaks, and Revelations: The Art of Analyzing Hacked and Leaked Data* (No Starch Press, 2024)
- [OnionShare](https://onionshare.org) — Open-source file sharing tool
- [Dangerzone](https://dangerzone.rocks) — Document sanitization tool
- [Lockdown Systems Collective](https://lockdown.systems) — Cyd app development
- GitHub: [@micahflee](https://github.com/micahflee)

## References

- micahflee.com--are-your-signal-groups-full-of-people-name-things-like-l-or---2bb35cd8
- micahflee.com--ddosecrets-publishes-410-gb-of-heap-dumps-hacked-from-teleme--4df4fc69
- micahflee.com--going-to-defcon-see-my-talk-we-are-currently-clean-on-opsec---e66e0c6e
- micahflee.com--how-to-easily-dig-through-the-epstein-files-yourself--beb1da32
- micahflee.com--i-spoke-about-iceblock-and-trumps-app-censorship-on-the-kill--71a22920
- micahflee.com--iceblock-handled-my-vulnerability-report-in-the-worst-possib--c2279f11
- micahflee.com--in-war-torn-portland-watch-me-speak-at-bsidespdx--6bd65428
- micahflee.com--jeffrey-epstein-bought-books-about-pedophilia-woody-allen-an--d29a0391
- micahflee.com--practical-defenses-against-technofascism--62e06b2a
- micahflee.com--telemessage-customers-include-dc-police-andreesen-horowitz-j--f2bd4f42
- micahflee.com--telemessage-explorer-a-new-open-source-research-tool--f72280d4
- micahflee.com--unfortunately-the-iceblock-app-is-activism-theater--a3f5a2bf
- micahflee.com--using-signal-groups-for-activism--7ceaad72
- micahflee.com--we-are-currently-clean-on-opsec-the-signalgate-saga--e8b6d537
- micahflee.com--why-hack-the-dhs-i-can-think-of-a-couple-pretti-good-reasons--be35e375
- micahflee.com--agentic-coding-techniques--fc5e06aa
- micahflee.com--mandatory-update-a-short-story--a332b287
