---
title: Bert Hubert
type: entity
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - blogger
  - hn-popular
  - powerdns
  - open-source
  - cybersecurity
  - digital-sovereignty
  - tech-policy
  - lean-software
sources: []
---


# Bert Hubert

| | |
|---|---|
| **Blog** | [berthub.eu](https://berthub.eu) |
| **RSS** | https://berthub.eu/articles/index.xml |
| **Mastodon** | [@bert_hubert@eupolicy.social](https://eupolicy.social/@bert_hubert) |
| **GitHub** | [bert-hubert](https://github.com/bert-hubert) |
| **Google Scholar** | [Bert Hubert](https://scholar.google.com/citations?user=KX0qYJkAAAAJ) |
| **Email** | bert@hubertnet.nl |
| **Role** | Entrepreneur, software developer, science contributor, technical policy advisor |
| **Known for** | PowerDNS (founder, 1999), RFC 5452, Googerteller, SkewDB, lean software advocacy, mRNA vaccine reverse engineering, EU tech policy analysis |
| **Bio** | Dutch entrepreneur and developer based in the Netherlands. Founded PowerDNS in 1999 (open-source DNS software used globally). Former shareholder of Open-Xchange. Joined a Dutch government oversight board in 2020 (since departed). Currently serves as part-time technical advisor to Dutch government departments including the Dutch Electoral Council. Holds several secondary positions (`nevenfuncties`). Published in IEEE Spectrum, IETF RFCs, and Nature Scientific Data. |

## Core Ideas

Bert is a **systems-level thinker** who operates at the intersection of software engineering, public policy, and scientific research. His work spans from RFCs that secure global DNS infrastructure to policy analysis that critiques the EU's approach to digital sovereignty. He is one of the rare technical voices who can reverse-engineer a vaccine's source code, build a GNSS satellite monitoring dashboard, and testify before parliament — all in the same year.

### Lean Software as Security Imperative

Bert's most influential technical thesis is that **software bloat is a security vulnerability, not just an engineering aesthetic**. In his 2024 article *"A 2024 Plea for Lean Software"* (later published as *"Why Bloat Is Still Software's Biggest Vulnerability"* in IEEE Spectrum), he argues that modern software ships too much code, from opaque dependency trees, and without adequate auditing. His formula: `security risk = bug density × total code`. 

He demonstrated this principle with **Trifecta**, a self-contained image-sharing tool built with ~1,600 lines of code and ~5 core dependencies — contrasted against Electron alternatives shipping 50M+ lines of code across 1,600+ npm packages. His philosophy echoes Niklaus Wirth's 1995 original plea:

> *"The plague of software explosion is not a 'law of nature'. It is avoidable, and it is the software engineer's task to curtail it."*

### Digital Sovereignty & European Infrastructure

Bert is a leading voice on **European digital autonomy** — not as abstract political rhetoric, but as a practical engineering problem. His core argument: you cannot buy digital sovereignty from American cloud providers. His talk *"Digitale Autonomie: wat is het en willen we het wel"* (PublicSpaces 2024) laid out why European institutions must build and maintain their own infrastructure:

- **"The cloud is not a chemical plant"** — treating cloud providers as essential infrastructure you simply buy is a category error. You need sovereign capability, not just sovereign purchasing.
- **"Open Source on its own is no alternative to Big Tech"** — FOSS without institutional capacity, funding, and operational expertise is just free labor for vendors who wrap it in proprietary services.
- **"Dear hosters, you are selling wood, not furniture"** — infrastructure providers sell raw capacity, not solutions. Institutions must build the furniture themselves.

He advocates for **modular European cloud architecture** (*Cloud Kootwijk* initiative) and criticizes the asymmetry where American vendors get away with PowerPoints while European competitors face demands for 6-week proofs-of-concept at their own expense.

### Cybersecurity as Pre-War Reality

His 2024 talk *"Cyber Security: A Pre-War Reality Check"* (NCSC-NL / ACCSS / Surf) frames cybersecurity not as an IT problem but as a **national security infrastructure problem**. He warns that the current approach — patching individual vulnerabilities while the attack surface grows exponentially — is fundamentally unsustainable. The talk draws parallels to military preparedness: you don't wait for war to build your defenses.

### DNS Architecture & RFC 5452

Bert co-authored **RFC 5452** (*"Measures for Making DNS More Resilient against Forged Answers"*), a foundational security standard that introduced source port randomization and other techniques to protect DNS from cache poisoning attacks. This work underpins the security of DNS infrastructure used by millions globally. His **"Hello DNS"** series is the definitive practical introduction to DNS protocol internals, complete with reference implementations.

### Science Communication & Open Data

Bert applies his engineering methodology to science communication:

- **mRNA Vaccine Reverse Engineering** (2020): His widely-read analysis of the BioNTech/Pfizer SARS-CoV-2 vaccine source code demystified mRNA technology for a global technical audience, explaining codon optimization, nucleoside modification, and the UTR design choices.
- **SkewDB** (2022, Nature Scientific Data): Open database of GC and 10 other skews for 30,000+ microbial chromosomes/plasmids. Represents his approach to making complex scientific data accessible and auditable.
- **Galmon.eu**: Real-time GPS/Galileo/GNSS satellite monitoring dashboard. Provides independent, transparent monitoring of global navigation satellite systems.
- **tkconv / bagconv**: Open-data converters for Dutch parliamentary records and building/address databases — making government data actually usable.
- **Nlelec**: Live plots of Dutch renewable electricity consumption, import, and export data.

### Policy Analysis: Chatcontrol & EU Regulation

Bert provides rigorous, multilingual technical analysis of EU legislation:
- **Chatcontrol 2025**: Detailed critiques of client-side scanning proposals, demonstrating the mathematical impossibility of secure scanning without breaking end-to-end encryption. Published summaries in 10+ languages (DE, FR, IT, ES, PL, RO, CZ, EO, BG, CA).
- **Cyber Resilience Act**: Analysis of how EU software regulation will impact development practices.
- **AIVD/MIVD oversight**: Critical examination of Dutch intelligence laws and the tension between security mandates and privacy rights.

### C++ & Performance Engineering

His **"Modern C++ for C Programmers"** series (6 parts) is a widely-referenced resource for developers transitioning to C++. His optimization work on PowerDNS achieved a **400% speedup** through careful algorithmic improvements — embodying his philosophy that performance is an engineering discipline, not a compiler feature.

## Key Quotes

> *"The cloud is not a chemical plant."*

> *"Open Source on its own is no alternative to Big Tech."*

> *"You can't buy digital autonomy in America."*

> *"Dear hosters, you are selling wood, not furniture."*

> *"To some, complexity equals power. [...] Increasingly, people seem to misinterpret complexity as sophistication, which is baffling — the incomprehensible should cause suspicion rather than admiration."* — quoting Niklaus Wirth

## Related

- [[powerdns]] — Open-source DNS software Bert founded in 1999
- [[lean-software]] — Software minimalism as security strategy
-  — European infrastructure autonomy
-  — DNS resilience standard Bert co-authored
-  — EU client-side scanning legislation Bert critiques

## Sources

- [A 2024 Plea for Lean Software (with running code)](https://berthub.eu/articles/posts/a-2024-plea-for-lean-software/) — IEEE Spectrum: *Why Bloat Is Still Software's Biggest Vulnerability*
- [Cyber Security: A Pre-War Reality Check](https://berthub.eu/articles/posts/cyber-security-a-pre-war-reality-check/) — NCSC-NL / ACCSS / Surf transcript
- [Digitale Autonomie: wat is het en willen we het wel](https://berthub.eu/articles/posts/publicspaces-digitale-autonomie-7-juni-2024/) — PublicSpaces 2024
- [Reverse Engineering the source code of the BioNTech/Pfizer SARS-CoV-2 Vaccine](https://berthub.eu/articles/posts/reverse-engineering-the-source-code-of-the-biontech-pfizer-sars-cov-2-vaccine/)
- [Hello DNS](https://berthub.eu/articles/posts/hello-dns/)
- [RFC 5452: Measures for Making DNS More Resilient against Forged Answers](https://datatracker.ietf.org/doc/html/rfc5452)
- [Optimizing optimizing: 400% speedup of PowerDNS](https://berthub.eu/articles/posts/optimizing-optimizing/)
- [SkewDB in Nature Scientific Data](https://www.nature.com/articles/s41597-022-01440-9)
- [berthub.eu/articles](https://berthub.eu/articles/) — Full article archive
