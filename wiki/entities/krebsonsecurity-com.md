---
title: "Brian Krebs"
tags: [- person]
created: 2026-04-24
updated: 2026-04-24
---

# Brian Krebs

**URL:** https://krebsonsecurity.com
**Blog:** Krebs on Security
**Twitter/X:** @briankrebs
**Mastodon:** @briankrebs@infosec.exchange
**Background:** Former Washington Post reporter (1995–2009), Security Fix blog author

## Overview

Brian Krebs is one of the most prominent cybersecurity journalists in the world, known for his deep investigative reporting on cybercriminal enterprises, data breaches, and the underground economy of stolen data. After 14 years at The Washington Post — where he authored over 1,300 blog posts for the Security Fix blog and numerous front-page stories — he went independent in 2009 and has since become arguably the most influential independent voice in security journalism.

His reporting style is distinctive: Krebs approaches cybersecurity like a crime reporter, not a technologist. He doesn't just document vulnerabilities — he identifies the people behind them, traces their operations, names names, and follows the money. This approach has made him a target: he has been the victim of sustained DDoS attacks, SWATting, and harassment from the criminal underworld he investigates.

His blog krebsonsecurity.com has been running since 2009 and remains one of the most-read cybersecurity publications in the world, consistently breaking stories that major outlets later cover.

## Timeline

| Date | Event |
|------|-------|
| 1995–2009 | Reporter at The Washington Post; authored Security Fix blog with 1,300+ posts |
| 2001 | Home network overrun by Chinese hacking group via default Red Hat Linux installation — the incident that sparked his security career |
| 2009 | Went independent; launched krebsonsecurity.com |
| 2014 | Profiled in The New York Times, Business Week, NPR's Terry Gross, and Poynter.org |
| 2014 | Published *Spam Nation* — investigation into global cybercriminal spam operations |
| 2016 | Targeted by massive DDoS attacks (up to 620 Gbps) following reporting on cybercriminals |
| 2017 | Identified Russian business spam kingpins, leading to US sanctions |
| 2019–2021 | Tracked GandCrab and REvil ransomware operations, contributing to international law enforcement action |
| 2024 | Continued reporting on ransomware groups, IoT botnets, and AI-assisted cybercrime |
| 2025 | Broke the Kimwolf botnet story — 2M+ infected IoT devices used as proxy networks |
| 2026 | Published "How AI Assistants Are Moving the Security Goalposts" — examining the security risks of autonomous AI agents |
| 2026 | Reported on Starkiller phishing service — real-time MFA-bypass phishing-as-a-service |
| 2026 | Covered DOJ takedown of four major IoT botnets (Aisuru, Kimwolf, JackSkid, Mossad) — 3M+ compromised devices |

## Core Ideas

### Follow the Money, Name Names

Krebs's central journalistic philosophy is that **cybercrime is not a faceless, abstract threat — it is committed by identifiable individuals operating for financial gain**. His reporting consistently focuses on:

- Identifying the real-world people behind anonymous handles (e.g., unmasking "UNKN"/Daniil Maksimovich Shchukin as the leader of GandCrab and REvil)
- Tracing the financial flows — crypto wallets, money laundering, shell companies
- Connecting criminal operations to geopolitical actors (e.g., Russia's GRU-linked Forest Blizzard campaign)

> *"An elusive hacker who went by the handle 'UNKN' and ran the early Russian ransomware groups GandCrab and REvil now has a name and face."*

This approach differs from much security journalism that focuses on technical vulnerabilities. Krebs focuses on the **human and economic dimensions** — who benefits, who suffers, and how to disrupt the incentive structures that make cybercrime profitable.

### The Commoditization of Cybercrime

A recurring theme in Krebs's recent reporting is how **cybercrime has become industrialized and accessible to low-skill actors**. The rise of ransomware-as-a-service (RaaS), phishing-as-a-service, and AI-assisted attack tools has dramatically lowered the barrier to entry:

> *"Starkiller represents a significant escalation in phishing infrastructure, reflecting a broader trend toward commoditized, enterprise-style cybercrime tooling. Combined with URL masking, session hijacking, and MFA bypass, it gives low-skill cybercriminals access to attack capabilities that were previously out of reach."* — on the Starkiller phishing service (2026)

Krebs documents how criminal operations now operate like startups — with customer support, feature requests, user forums, and even rebranding strategies (GandCrab → REvil). This industrialization makes the threat landscape more diffuse and harder to combat.

### AI as Both Threat and Threat Multiplier

Krebs has been increasingly focused on how AI tools are reshaping the security landscape in his 2025–2026 reporting:

> *"The robot butlers are useful, they're not going away and the economics of AI agents make widespread adoption inevitable regardless of the security tradeoffs involved."* — Jamieson O'Reilly, quoted by Krebs

He has documented:
- **AI supply chain attacks**: Compromised AI coding assistants (Cline) installing rogue agents on thousands of systems
- **Autonomous AI vulnerability**: The "lethal trifecta" — agents with private data access, exposure to untrusted content, and external communication capabilities
- **AI-augmented attacks**: Low-skilled actors using commercial AI services to plan and execute sophisticated campaigns across 55+ countries

Krebs's position is pragmatic rather than alarmist: AI tools will be adopted regardless, and the security community must adapt its defense strategies rather than trying to prevent adoption.

### The Insider Threat Shift

A key insight from Krebs's recent work is that **traditional security perimeters are dissolving** as employees bring AI agents into corporate environments with broad system access. The threat model is shifting from external attackers to compromised or manipulated internal agents:

> *"This is the supply chain equivalent of confused deputy. The developer authorises Cline to act on their behalf, and Cline (via compromise) delegates that authority to an entirely separate agent the developer never evaluated, never configured, and never consented to."* — grith.ai, quoted by Krebs

### Botnets and IoT: The Ungoverned Infrastructure

Krebs has done extensive reporting on IoT botnets, documenting how billions of poorly-secured devices create a persistent threat infrastructure:

> *"The past few months have witnessed the explosive growth of a new botnet dubbed Kimwolf, which experts say has infected more than 2 million devices globally."* (January 2026)

His coverage of the Kimwolf story revealed how botnet operators were tunneling through residential proxy networks, using infected IoT devices (digital photo frames, Android TV boxes, routers) as anonymous relay infrastructure — effectively turning everyday consumer devices into weapons.

## Key Quotes

> *"The robot butlers are useful, they're not going away and the economics of AI agents make widespread adoption inevitable regardless of the security tradeoffs involved."* — on the inevitability of AI tool adoption

> *"Nothing humbles you like telling your OpenClaw 'confirm before acting' and watching it speedrun deleting your inbox... I couldn't stop it from my phone. I had to RUN to my Mac mini like I was defusing a bomb."* — Summer Yue, Meta AI Safety Director, quoted by Krebs

> *"This gradual dissolution of the traditional boundaries between data and code is one of the more troubling aspects of agentic AI."* — on AI agent security risks (2026)

> *"It was an accident. That's how I got into security — my entire home network got overrun by a Chinese hacking group because I was running a default install of Red Hat Linux 6.2 and the Lion Worm locked me out. Twice."* — on how he entered cybersecurity

> *"Organizations should now add a third pillar to their defense strategy: limiting AI fragility, the ability of agentic systems to be influenced, misled, or quietly weaponized across automated workflows."* — citing Orca Security (2026)

## Recent Themes (2024–2026)

- **AI agent security**: Comprehensive coverage of autonomous AI agents as both tools and vulnerabilities
- **Ransomware ecosystem evolution**: Tracking how ransomware groups rebrand, restructure, and evade law enforcement
- **IoT botnet proliferation**: From Kimwolf to multi-botnet takedowns — the growing threat of compromised consumer devices
- **State-sponsored cyber operations**: Forest Blizzard (APT28) router DNS hijacking affecting 18,000+ networks
- **Phishing industrialization**: Services like Starkiller that proxy real login pages and bypass MFA
- **Cybercrime-as-a-service**: The commoditization and professionalization of criminal infrastructure
- **Geopolitical weaponization of cybercrime**: Iran-linked hacktivist groups targeting Western companies

## Related Concepts

- [[Data Breach]] — Central topic of Krebs's investigative reporting
- [[Ransomware]] — Extensive coverage of GandCrab, REvil, and the RaaS economy
- [[Botnet]] — Kimwolf, Aisuru, and the IoT device exploitation landscape
- [[AI Agent Security]] — OpenClaw, prompt injection, and the lethal trifecta
- [[Phishing]] — Evolution from static pages to real-time proxy attacks (Starkiller)
- [[Cybercrime Economics]] — Follow-the-money journalism approach
-  — AI coding assistant compromises and dependency chains
-  — Krebs's own experience being targeted and the broader botnet threat
-  — APT28/Forest Blizzard, Iran-linked operations

## Influence Metrics

- *Spam Nation* (2014): Major investigation into global cybercriminal spam operations
- KrebsOnSecurity: One of the most-read independent security blogs worldwide since 2009
- His reporting has directly contributed to US sanctions on Russian cybercriminals
- 2016: Survived 620 Gbps DDoS attacks, among the largest ever recorded against a single target
- Consistently breaks stories before major outlets — his investigative methodology has become a model for security journalism
- Named among the most influential voices in cybersecurity by multiple industry publications
