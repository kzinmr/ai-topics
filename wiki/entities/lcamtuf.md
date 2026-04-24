---
tags: [person]
type: entity
sources: []
---


# Michał Zalewski (lcamtuf)

**URL:** https://lcamtuf.coredump.cx
**Blog:** lcamtuf's thing (Substack), lcamtuf.blogspot.com (archive)
**Twitter/X:** @lcamtuf
**GitHub:** lcamtuf
**Current Role:** VP of Security Engineering, Snap Inc. (since 2018)
**Previous:** Google, Project Zero

## Overview

Michał Zalewski, known online as "lcamtuf," is a Polish-American security researcher whose career spans nearly three decades of vulnerability research, fuzzing innovation, and applied security thinking. He is the creator of **American Fuzzy Lop (AFL)**, the fuzzer that revolutionized the field of automated bug discovery, and has been a prolific researcher at Google's Project Zero team.

Zalewski's intellectual identity is defined by **rigorous, data-driven analysis applied to problems others treat emotionally or speculatively**. Whether examining browser security vulnerabilities, the mathematics of cellular automata, or the practicalities of emergency preparedness, his approach is consistent: strip away the noise, examine the actual probabilities, and build systems that work.

His writing ranges from deep technical research (fuzzing methodology, browser security) to accessible essays on electronics, mathematics, and threat modeling for everyday life. He is the author of three books: *Silence on the Wire* (2005) on passive reconnaissance, *The Tangled Web* (2011) on browser security, and *Practical Doomsday* (2022) on rational emergency preparedness.

## Timeline

| Date | Event |
|------|-------|
| mid-1990s | Began publishing vulnerability research on Bugtraq; created Argante (virtual open-source OS) |
| 2001 | Moved to the United States |
| 2003 | Discovered SSH CRC32 buffer overflow vulnerability (CA-2003-25) |
| 2004 | Discovered statistical weaknesses in TCP/IP initial sequence numbers (CA-2001-09) |
| 2005 | Published *Silence on the Wire: A Field Guide to Passive Reconnaissance and Indirect Attacks* (No Starch Press) |
| 2006–2012 | Multiple browser security vulnerabilities reported (Firefox wyciwyg cache, IE overflows, Opera XSS) |
| 2011 | Published *The Tangled Web: A Guide to Securing Modern Web Applications* (No Starch Press) |
| 2013 | Created **American Fuzzy Lop (AFL)** — coverage-guided fuzzing tool that transformed vulnerability discovery |
| 2010s | Named one of the 15 most influential people in security and among the 100 most influential in IT |
| 2018 | Left Google; became VP of Security Engineering at Snap Inc. |
| 2021 | Announced *Practical Doomsday* — applying security thinking to everyday risk |
| 2022 | Published *Practical Doomsday: A User's Guide to the End of the World* (No Starch Press) |
| 2024 | Google Project Zero published "Big Sleep" — using LLMs for vulnerability discovery, building on AFL foundations |
| 2025 | Published "A contrarian intro to photography" — technical deep-dive into image capture |
| 2025 | Released *Sir Box-a-Lot* and *Bob the Cat* — retro handheld game projects |
| 2026 | Published "On the Effectiveness of Mutational Grammar Fuzzing" — critique of grammar fuzzing limitations |
| 2026 | Active Substack publishing on electronics, mathematics, tech history, and geek culture |

## Core Ideas

### Fuzzing as Systematic Discovery

Zalewski's most influential contribution to security is his work on **fuzzing** — the automated process of feeding malformed inputs to software to discover vulnerabilities. AFL revolutionized this field by introducing **coverage-guided fuzzing**:

> *"The fact that coverage is not a great measure for finding bugs is well known and affects coverage-guided fuzzing in general, not just grammar fuzzing."* — on the limits of coverage metrics (2026)

His 2026 paper on mutational grammar fuzzing demonstrates his characteristic willingness to critique even his own field's established practices. He argues that coverage-guided fuzzers reach a **natural saturation point** — they find easy bugs quickly but miss complex vulnerabilities that require understanding program semantics:

> *"By setting a relatively small frame_size_limit, the dav1d fuzzer missed the integer overflow. There is a good reason for this limit... This highlights a tradeoff for fuzzers."* — from the Project Zero dav1d case study (2024)

His proposed solution — alternating between generative fuzzing (creating inputs from scratch) and mutational fuzzing (modifying existing inputs) — reflects his broader philosophy: **no single technique is sufficient; systematic variation is necessary**.

### Security as Threat Modeling, Not Fear

Zalewski's approach to security is fundamentally about **threat modeling** — identifying actual risks, quantifying them, and allocating resources rationally:

> *"The goal of the book is not to convince you that the end is nigh. To the contrary: I want to reclaim the concept of prepping from the bunker-dwelling prophets of doom."* — on *Practical Doomsday* (2021)

This philosophy applies equally to cybersecurity and everyday life. His central insight is that **most people misallocate their security attention**: they worry about dramatic, unlikely threats while ignoring mundane, probable ones. In *Practical Doomsday*, he demonstrates this with statistics:

> *"Far more people are killed in the United States by lawnmowers than by animals of prey."*

This data-driven approach to security extends to his technical work. His browser security research (*The Tangled Web*) was notable not for discovering the most critical vulnerabilities but for providing a **comprehensive mental model of how browsers actually work** — understanding the attack surface before trying to secure it.

### The Engineer's Epistemology

Zalewski consistently applies an engineering epistemology to problems: **understand the system, build models, test them, iterate**. His Substack articles on Conway's Game of Life, Diophantine approximation, and number system construction reveal a mind that seeks foundational understanding rather than surface-level competence:

> *"The gaps between rational numbers is where we find irrationals... inexhaustible supply of unexpectedly accurate rational approximations."* — on mathematical approximation (2026)

This same approach underlies his security work. Rather than applying tools blindly, he builds understanding from first principles — whether that means constructing physical Game of Life boards with LED matrices, analyzing circuit design for multiplexing, or decomposing browser rendering pipelines.

### AI for Vulnerability Discovery: Promise and Limits

Zalewski's fuzzing work laid the foundation for Google Project Zero's "Big Sleep" project, which uses LLMs to find vulnerabilities that fuzzing misses:

> *"We think that this work has tremendous defensive potential. Finding vulnerabilities in software before it's even deployed would give defenders a significant advantage."* — Project Zero on Big Sleep (2024)

His response has been characteristically measured. While acknowledging AI's potential, he emphasizes the **complementary nature of approaches**: fuzzing finds what LLMs miss, and LLMs find what fuzzing misses. The key is not choosing one over the other but understanding the limitations of each and deploying them where they're most effective.

### Rejecting Algorithmic Content

Zalewski has positioned his Substack explicitly against algorithmic content distribution:

> *"I can't promise you a fixed set of topics, but I do my best to bring the readers well-researched, non-regurgitated, and clickbait-free content."*

> *"Substack isn't an algorithmic hellscape; it's just a way to stay in touch with the writers you like."*

> *"Articles, images, and code posted on this site are written by a human and not licensed for use in ML training or ML content generation."*

This reflects a broader philosophy about **authentic human creation** — the value of writing that comes from genuine curiosity and rigorous research rather than SEO optimization or AI generation.

### The Practical Mindset

His approach to everyday problems is consistently practical. He builds physical Game of Life implementations with LED matrices, troubleshoots Bluetooth lock integration with ESP32s, and analyzes circuit design for hobby electronics. This hands-on orientation prevents his thinking from becoming purely theoretical:

> *"The entire screen update code is decoupled from game logic; the manipulation of game state happens during an imperceptible 'blackout' window when all the LEDs are off."* — on hardware design (2026)

The Watchdog Timer safety mechanism in his Game of Life build — forcing a reboot if the main loop stalls to prevent LED thermal damage — is a microcosm of his broader security philosophy: **build in safeguards for when things go wrong, because they will**.

## Key Quotes

> *"The goal of the book is not to convince you that the end is nigh. To the contrary: I want to reclaim the concept of prepping from the bunker-dwelling prophets of doom."* — on *Practical Doomsday* (2021)

> *"Disasters happen, but they don't have to dominate your life."* — from *Practical Doomsday*

> *"The fact that coverage is not a great measure for finding bugs is well known."* — on fuzzing limitations (2026)

> *"I can't promise you a fixed set of topics, but I do my best to bring the readers well-researched, non-regurgitated, and clickbait-free content that appeals to their inner geek."* — on his Substack philosophy

> *"Far more people are killed in the United States by lawnmowers than by animals of prey."* — on risk perception

> *"The gaps between rational numbers is where we find irrationals."* — on mathematical structure (2026)

> *"Articles, images, and code posted on this site are written by a human and not licensed for use in ML training or ML content generation."* — on AI and human authorship

## Recent Themes (2024–2026)

- **Fuzzing methodology critique**: Re-examining the limitations of coverage-guided fuzzing and proposing hybrid approaches
- **AI vulnerability research**: Big Sleep project — using LLMs to find bugs that fuzzing misses
- **Rational risk management**: *Practical Doomsday* philosophy applied to everyday life
- **Hands-on engineering**: Physical computing projects, circuit design, electronics education
- **Mathematical exploration**: Diophantine approximation, number systems, Conway's Game of Life
- **Anti-algorithmic publishing**: Direct reader relationships via Substack, rejecting ML training of content
- **Photography as technical craft**: Contrarian approach emphasizing understanding over gear
- **Human authorship**: Explicit stance against AI content generation and training on creative work

## Related Concepts

- [[American Fuzzy Lop]] — His revolutionary coverage-guided fuzzing tool
- [[Fuzzing]] — The broader field he transformed through AFL and ongoing research
- [[Project Zero]] — Google's elite vulnerability research team where he worked
- [[Threat Modeling]] — His approach to security as rational risk assessment
- [[Browser Security]] — Subject of *The Tangled Web* and years of research
- [[Passive Reconnaissance]] — Subject of *Silence on the Wire*
- [[AI Vulnerability Discovery]] — Big Sleep project and LLM-based bug finding
-  — His book on rational emergency preparedness
-  — His approach to understanding systems from first principles
-  — His stance on AI-generated content and creative authenticity

## Influence Metrics

- AFL: Became the standard fuzzer used by Google, Mozilla, and thousands of other organizations
- *Silence on the Wire* (2005): Influential text on passive reconnaissance methodology
- *The Tangled Web* (2011): Canonical reference on browser security architecture
- *Practical Doomsday* (2022): Praised for rational approach to emergency preparedness
- Named among the 15 most influential people in security and 100 most influential in IT
- His fuzzing research directly influenced Google's OSS-Fuzz program
- His work on grammar fuzzing (2026) continues to shape automated vulnerability discovery
- Big Sleep project (2024): Demonstrated LLMs can find vulnerabilities in well-fuzzed codebases
