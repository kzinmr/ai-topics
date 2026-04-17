---
tags: [person]
---


# Troy Hunt

**URL:** https://www.troyhunt.com
**Blog:** Troy Hunt
**Project:** Have I Been Pwned (HIBP) — https://haveibeenpwned.com
**Twitter/X:** @troyhunt
**Pluralsight:** Troy Hunt Author
**Role:** Microsoft Regional Director, Microsoft MVP for Developer Security
**Location:** Gold Coast, Australia

## Overview

Troy Hunt is one of the most recognizable voices in cybersecurity education and data breach transparency. He is best known as the creator and operator of **Have I Been Pwned (HIBP)**, a free service that allows individuals to check whether their personal data has been compromised in a data breach. What started as a side project in 2013 has grown into one of the most important resources in the cybersecurity ecosystem, processing billions of compromised records and serving millions of users worldwide.

Hunt's philosophy is distinctive: he is a **security practitioner who cares more about practical impact than theoretical purity**. His writing is direct, his tone is often wry, and he consistently argues for transparency over obfuscation. He has testified before the US Congress on data breach impacts and runs developer-focused security workshops globally.

In November 2024, Hunt hired HIBP's first employee — marking the transition from solo operation to a small team. By 2025–2026, HIBP was processing hundreds of millions of API queries annually and had indexed nearly 2 billion unique email addresses.

## Timeline

| Date | Event |
|------|-------|
| ~2000s | 14 years at Pfizer, final 7 leading APAC application architecture |
| 2013 | Created Have I Been Pwned (HIBP) — launched December 4, 2013 |
| 2014 | Began publishing Pluralsight courses on web security |
| 2015 | Ashley Madison breach — HIBP's pivotal moment in handling sensitive data |
| 2016 | Published "Data breach disclosure 101" — framework for breach response |
| 2018 | HIBP surpassed 3 billion breached accounts indexed |
| 2019 | Published "Here's how I verify data breaches" — transparency on HIBP methodology |
| 2019 | CloudPets breach reporting — exposing children's voice message leaks |
| 2021 | Microsoft acquired HIBP; Hunt continued as independent operator |
| 2024 | Published "Who Decides Who Doesn't Deserve Privacy?" — privacy philosophy essay |
| 2024 | Hired HIBP's first employee |
| 2025 | Published "2 Billion Email Addresses Were Exposed" — largest single data corpus indexed by HIBP |
| 2025 | Published "Why Does Have I Been Pwned Contain 'Fake' Email Addresses?" — defending data integrity |
| 2025 | Credential stuffing threat data — 1.95B unique emails, 1.3B unique passwords indexed |
| 2026 | Ongoing weekly blog posts on breach disclosure, AI agents, and operational transparency |
| 2026-04 | HIBP MCP Server launched — enables AI agents to query breach data via Model Context Protocol |
| 2026-04 | Published agentic AI workflow demos with OpenClaw + Telegram for HIBP API integration |

## Core Ideas

### Privacy Is Universal, Not Selective

Hunt's most distinctive philosophical contribution is his **consistent, principled stance that privacy applies to everyone — including people whose choices or affiliations others find morally objectionable**. This position crystallized during the 2015 Ashley Madison breach and has guided every HIBP decision since:

> *"Our own personal belief systems are not a valid basis for outing people publicly because their belief systems differ."* — "Who Decides Who Doesn't Deserve Privacy?" (2024)

He has applied this principle even to highly stigmatized breaches:
- **Ashley Madison** (2015): Flagged as sensitive despite the site's purpose, recognizing that an email in the breach doesn't prove guilt or active participation
- **Fur Affinity** and **Rosebutt Board**: Flagged due to community stigma, not the nature of the data
- **WhiteDate** (racial dating site with white supremacist associations): Flagged as sensitive despite public moral outrage
- **Muah.ai** (AI companion site with illegal content): Flagged as sensitive while simultaneously forwarding data to global law enforcement

> *"Involving law enforcement where data sets contain illegal activity is absolutely the right approach here, but equally, not being the vehicle for implying someone's affiliation or beliefs and doxing them publicly without due process is also absolutely the right approach."*

This framework is grounded in GDPR/CCPA definitions of sensitive personal data and Universal Declaration of Human Rights Article 12 protections. Hunt's position is that **privacy is a legal right, not a moral reward**.

### Email in a Breach ≠ Guilt

A recurring theme in Hunt's writing is that **the presence of an email address in a breached dataset does not prove that the account owner actively participated in the breached service**:

> *"Accounts were created by singles who later married before the breach, spouses attempting to catch cheating partners, third parties using others' emails without consent."*

This insight has profound practical implications for how organizations and individuals should interpret breach data. Hunt's HIBP service was designed around this principle — it tells you that your email appeared in a breach, not that you were at fault.

### Transparency in Breach Verification

Hunt has been remarkably transparent about how HIBP verifies the authenticity of breach data:

> *"Being able to reliably attribute the source of an incident is enormously important for two reasons. One is that the individuals in a data breach really want to know who mishandled their data. The other is, from my own self-preservation point of view, I want to get this right."*

His verification methodology is practical and evidence-based:
- Send a test email (e.g., a Mailinator address) to the breached service
- Confirm the reset email goes to the correct inbox
- Cross-reference with known breach patterns and timelines
- Attribute the source before listing in HIBP

This transparency serves both ethical and operational purposes — it builds trust in the service and protects against legal liability.

### Corporate Breach Disclosure Is Getting Worse, Not Better

Hunt has consistently argued that **organizations are becoming less transparent about breaches, not more**:

> *"I do fear, just as a gut feel, that it is worse now than what it was. The sense I get around this is a combination of things — it seems to be a lot less transparent. Organizations are going into self-preservation mode to try and protect their interests."* (2024 interview)

He identifies a "lose-lose position" for breached organizations:
- Pay the ransom and fuel criminals while still facing regulatory disclosure obligations
- Disclose early and face immediate public backlash
- Disclose late and face legal and regulatory penalties

This analysis reflects his deep experience operating at the intersection of breach data, corporate response, and public communication.

### AI as Transformative Tool, Not Replacement

Hunt has embraced AI tooling pragmatically, using GitHub Copilot and experimenting with autonomous agents for HIBP operations:

> *"Watching OpenClaw do its thing must be like watching the first plane take flight. It's a bit rickety and stuck together with a lot of sticky tape, but squint and you can see the potential for agentic AI to change the world as we know it."*

His position is optimistic but grounded: AI agents are experimental, imperfect, and require careful management. He is actively transitioning human workloads to AI agents for the small HIBP team (now including Stefan) while maintaining operational oversight.

### Operational Transparency as a Service Feature

Hunt runs HIBP as an unusually transparent operation. He publishes weekly blog posts detailing everything from:
- New breach data being indexed
- Technical infrastructure decisions
- Hardware experiments (ESP32 Bluetooth bridges, smart lock integration)
- Business operations (client invoice disputes, team expansion)

> *"How I optimised my life to make my job redundant"* — the title of one of his must-read articles, reflecting his philosophy of building systems that don't require constant human intervention

This transparency serves multiple purposes: it builds community trust, educates others on operational security, and holds Hunt himself accountable to the standards he advocates.

### Developer Security Education

Through 30+ Pluralsight courses, Hunt has been a major force in educating developers about security fundamentals:

- OWASP Top 10 for ASP.NET
- What Every Developer Must Know About HTTPS
- Hack Yourself First: How to Go on the Cyber-Offense
- Ethical Hacking: Social Engineering, SQL Injection, Web Applications
- Introduction to Browser Security Headers

His teaching philosophy is **offensive-first**: understand how attacks work before trying to defend against them. "Hack Yourself First" is particularly notable for putting developers in the attacker's seat to build genuine security intuition.

## Key Quotes

> *"Our own personal belief systems are not a valid basis for outing people publicly because their belief systems differ."* — on privacy and moral judgment (2024)

> *"No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honour and reputation."* — citing UDHR Article 12 (2024)

> *"Watching OpenClaw do its thing must be like watching the first plane take flight. It's a bit rickety and stuck together with a lot of sticky tape, but squint and you can see the potential for agentic AI to change the world as we know it."* — on AI agents (2026)

> *"I do fear, just as a gut feel, that it is worse now than what it was. Organizations are going into self-preservation mode."* — on corporate breach disclosure (2024)

> *"Being able to reliably attribute the source of an incident is enormously important."* — on breach verification methodology

> *"I want to get this right."* — on the responsibility of handling breach data

> *"How I optimised my life to make my job redundant."* — on building sustainable systems

> *"Very pwned. Everything is very pwned. There's no bottom, is there? We just keep going and going."* — on the state of data breaches (2024)

> *"I hate hyperbolic news headlines about data breaches."* — on media coverage of security incidents (2025)

## Recent Themes (2024–2026)

- **Privacy ethics**: Universal privacy rights, even for morally stigmatized populations
- **Breach verification**: Transparent methodology for validating and attributing breach data
- **AI agent adoption**: Pragmatic integration of autonomous agents into HIBP operations
- **Credential stuffing**: Massive-scale threat data processing (1.95B emails, 1.3B passwords)
- **Corporate transparency**: Critique of organizations' self-preservation approach to breach disclosure
- **Developer education**: Offensive-first security training through Pluralsight
- **Operational transparency**: Weekly public reporting on HIBP's technical and business operations
- **Data integrity defense**: Responding to criticism about HIBP's data handling with evidence and openness
- **Team scaling**: Transitioning from solo operation to small team while maintaining quality

## Related Concepts

- [[Have I Been Pwned]] — His flagship service for breach notification
- [[Data Breach]] — The central domain of his research and reporting
- [[Privacy Ethics]] — His principled stance on universal privacy rights
- [[Credential Stuffing]] — The threat vector behind massive breach data collections
- [[Breach Disclosure]] — His framework for how organizations should respond to breaches
- [[Developer Security]] — His educational mission through Pluralsight courses
- [[GDPR]] — The legal framework informing his sensitive breach classification
- [[Pwned Passwords]] — HIBP's password breach search service
- [[AI Agents]] — His pragmatic approach to integrating autonomous tools
- [[Transparency in Security]] — His operational philosophy of public accountability

## Influence Metrics

- **Have I Been Pwned**: Nearly 2 billion unique email addresses indexed; hundreds of millions of API queries annually
- **5+ million subscribers** on HIBP's free breach notification service
- **30+ top-rated Pluralsight courses** on security education
- **218+ blog posts** documenting HIBP's operations, methodology, and philosophy
- **Testified before US Congress** on data breach impacts
- **Microsoft Regional Director** and **MVP for Developer Security** since 2011
- **First hired employee** in November 2024, transitioning from solo to team operation
- His Ashley Madison breach handling established the template for "sensitive breach" classification now used industry-wide
