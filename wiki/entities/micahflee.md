---
title: Micah Lee
status: active
tags: [person]
---


# Micah Lee

## Overview

**Micah Lee** (he/him, pronounced "my-kah") is a security researcher, investigative data journalist, software engineer, and author. He is best known for building practical open-source privacy tools, analyzing leaked datasets, and advocating for tech activism that empowers journalists and ordinary citizens against state and corporate surveillance.

His work spans the full stack of information security — from developing widely used tools like **OnionShare** (secure file sharing over Tor) and **Dangerzone** (malware-safe document sanitization), to founding the **Lockdown Systems Collective**, which builds local-first alternatives to Big Tech data extraction (notably the [[Cyd]] app). He is the author of *Hacks, Leaks, and Revelations: The Art of Analyzing Hacked and Leaded Data* (No Starch Press, 2024), a practical guide for journalists and activists working with leaked datasets.

Previously: Director of Information Security at [[The Intercept]] (where he handled OPSEC during the Edward Snowden leaks), Staff Technologist at the [[Electronic Frontier Foundation]], and co-founder of [[Freedom of the Press Foundation]]. His journalism has appeared in *The Intercept*, *404 Media*, *WIRED*, and *Zeteo*.

---

## Timeline

| Period | Key Events |
|--------|-----------|
| 2013 | Provides OPSEC for journalists covering the [[Edward Snowden]] NSA leaks |
| 2014 | Develops **OnionShare** — open-source file sharing over [[concepts/dark-factory-software-factory.md]] |
| 2014–2024 | Director of Information Security at [[The Intercept]]; leads the SIDtoday Files project |
| 2016–2019 | Leads comprehensive reporting on NSA Signals Intelligence Directorate documents |
| 2018 | Reports on leaked WikiLeaks DMs with Cora Currier |
| 2020 | Develops **Dangerzone** — converts potentially malicious documents to safe PDFs |
| 2022 | Co-publishes investigation on TeleMessage spyware used by Trump officials |
| 2024 | Publishes *Hacks, Leaks, and Revelations* (No Starch Press) |
| 2025 | Founds **Lockdown Systems Collective**; develops [[Cyd]] app; reports on [[ICEBlock]] app security failures; delivers BSidesPDX keynote on "Technofascism" |
| 2026 | Publishes Epstein files analysis on [[Zeteo]]; builds DHS Contracts Explorer from hacked data; writes extensively on Signal group nicknames, mercenary spyware, and app censorship |

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

**2025:** Founded the [[Lockdown Systems Collective]] and began developing [[Cyd]], an open-source app for local-first personal data backup. Delivered his BSidesPDX keynote on technofascism. Published critical analysis of the ICEBlock app as "activism theater." Co-reported on TeleMessage spyware. Published Epstein files analysis for [[Zeteo]].

**2026:** Built the DHS Contracts Explorer from hacked immigration enforcement data. Published practical guides on Signal group security (nicknames as identity verification). Continued analysis of mercenary spyware threats (Paragon/Graphite, NSO/Pegasus) and platform complicity. Active on the kill switch podcast discussing app censorship.

---

## Related

[[OnionShare]] — Lee's flagship tool for secure, anonymous file sharing over Tor
[[Dangerzone]] — Document sanitization tool for journalists handling untrusted files
[[Cyd]] — Local-first data backup app developed through Lockdown Systems Collective
[[concepts/dark-factory-software-factory.md]] — Anonymity network central to Lee's tooling philosophy
[[Signal]] — Encrypted messaging platform Lee advocates and analyzes
[[The Intercept]] — Former employer; Lee directed information security for a decade
[[Electronic Frontier Foundation]] — Former employer as staff technologist
[[Freedom of the Press Foundation]] — Co-founded by Lee
[[Edward Snowden]] — Lee provided OPSEC during the NSA document leaks
[[Zeteo]] — Current publication outlet for investigative journalism
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
- *I spoke about ICEBlock and Trump's app censorship on the kill switch podcast* (October 2025)
- *Hacks, Leaks, and Revelations: The Art of Analyzing Hacked and Leaked Data* (No Starch Press, 2024)
- [OnionShare](https://onionshare.org) — Open-source file sharing tool
- [Dangerzone](https://dangerzone.rocks) — Document sanitization tool
- [Lockdown Systems Collective](https://lockdown.systems) — Cyd app development
- GitHub: [@micahflee](https://github.com/micahflee)
