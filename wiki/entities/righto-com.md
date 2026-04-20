---
title: Ken Shirriff
created: 2026-04-09
updated: 2026-04-10
tags:
- person
- blogger
- hn-popular
- reverse-engineering
- chip-design
- computer-history
- microcode
aliases:
- righto.com
- kenshirriff
---

# Ken Shirriff

| | |
|---|---|
| **Blog** | [righto.com](https://righto.com) |
| **RSS** | https://www.righto.com/feeds/posts/default |
| **Bluesky** | [@righto.com](https://bsky.app/profile/righto.com) |
| **Mastodon** | [@kenshirriff@oldbytes.space](https://oldbytes.space/@kenshirriff) |
| **Focus** | Computer history, vintage computer restoration, IC reverse engineering, microcode analysis |

## Bio

Ken Shirriff is a blogger and hardware reverse engineer based in Silicon Valley. His blog, righto.com, has been active since 2008 and covers computer history, vintage computing, integrated circuit reverse engineering, and electronics analysis. He is a member of the **Opcode Collective**, a group working to reverse-engineer microcode from historic processors. His writing is highly regarded by engineers, historians, and hobbyists worldwide for its step-by-step technical documentation and clarity.

### Notable Projects & Topics
- **Microprocessor die analysis**: Intel 4004, 8008, 8085, 8086, 8087, 386, Pentium; 6502; Z-80; ARM
- **Aerospace & Apollo hardware**: F-14 CADC (MP944 chipset), Apollo Up-Data Link, Saturn V communications
- **Hardware teardowns**: Apple chargers, IBM 1401 printer chain, Sinclair/TI calculators, 555 timer chip, 74181 ALU
- **Software projects**: Arduino IRremote library (widely used), Bitcoin mining with pencil and paper (0.67 hashes/day)
- **Historical systems**: Xerox Alto (BCPL), IBM 360/91, Datapoint 2200

## Core Ideas

### The Archaeology of Silicon

Ken approaches chips the way an archaeologist approaches ruins: **by going down to the physical layer**. His methodology is to decapsulate ICs, photograph the silicon die at high resolution, then trace out every transistor, wire, and gate to understand exactly how the chip works. He doesn't just read datasheets — he reads the silicon itself. This bottom-up approach reveals design decisions, compromises, and clever tricks that no documentation captures.

> *"I thought that understanding the microcode would be straightforward, just examining a block of decode circuitry. But this project turned out to be much more complicated and I need to reverse-engineer the entire chip."*

This quote captures his recurring experience: **you can't understand one layer without understanding all of them.** Microcode depends on the instruction decoder, which depends on the datapath, which depends on the transistor layout. Understanding emerges only from the full stack.

### Engineering at the Edge of What's Possible

A recurring theme in Ken's writing is appreciation for designs created under extreme constraints. The Intel 8087 floating-point coprocessor, which had only a 1,648-word microcode ROM, used a combination of PLAs, constant ROMs, on-the-fly exponent calculation, and distributed decoding circuitry to fit 62 instructions into an impossibly small space. Early yield was just two working chips per wafer.

Ken's insight: **when you're at the edge of what's possible, every transistor counts, and cleverness isn't optional — it's survival.** The 8087 doesn't have a clean architecture; it's full of ad hoc circuits and corner cases because the designers needed every technique available to make it work.

### The Evolutionary Chain of Computing

Ken documents how computing evolved step by step — not as a linear march of progress, but as a chain of adaptations, kludges, and serendipitous accidents. The x86 architecture traces back to the Datapoint 2200 (1970), a "programmable terminal" built from TTL chips. The 8086 was intended as a stop-gap until Intel's flagship iAPX 432 arrived. The stop-gap won; the flagship was abandoned.

His work shows that **the foundations of modern computing are built on contingency, not inevitability.** The architectures we use today are accidents that stuck.

### Collaborative Reverse Engineering

Ken is part of the **Opcode Collective**, a distributed group collaboratively reverse-engineering processor microcode. His blog posts routinely credit collaborators (especially "Smartest Blob" and "Gloriouscow") for specific discoveries. This reflects a broader philosophy: complex systems require collective effort to understand, and attribution matters.

### Making the Invisible Visible

Ken's posts consistently translate abstract computer science concepts into concrete, visible things. His 4-bit ALU simulator, die photos with labeled functional blocks, and step-by-step walkthroughs of transistor circuits make the internal workings of chips comprehensible to readers who've never seen silicon before.

> *"Why take the easy way when there's a complex chip to explore?"* — on why he reverse-engineered the 74181 ALU chip instead of starting with a simple NAND gate

## Key Quotes

> *"At the time, the chip was on the edge of what was possible, so the designers needed to use whatever techniques they could to reduce the size of the chip. If implementing a corner case could shave a few transistors off the chip or make the microcode ROM slightly smaller, the corner case was worthwhile."*

> *"The 8087 doesn't have a clean architecture, but instead is full of ad hoc circuits and corner cases."*

> *"Why take the easy way when there's a complex chip to explore?"*

> *"I thought that understanding the microcode would be straightforward, just examining a block of decode circuitry. But this project turned out to be much more complicated and I need to reverse-engineer the entire chip."*

## Related

- [[microcode]] — The layer between machine instructions and hardware execution
- [[reverse-engineering]] — Ken's core methodology across chips, protocols, and systems
- [[opcode-collective]] — Distributed group Ken collaborates with on microcode analysis
- [[computer-architecture]] — How processors are designed and how they evolved
- [[intel-8086]] — The chip that launched x86, extensively analyzed by Ken
- [[intel-8087]] — Floating-point coprocessor, subject of Ken's recent deep-dive series
- [[apollo-program]] — Aerospace hardware Ken has reverse-engineered
- [[silicon-die-analysis]] — The practice of photographing and tracing chip layouts

## Sources

- [Instruction decoding in the Intel 8087 floating-point chip](https://www.righto.com/2026/02/8087-instruction-decoding.html) (Feb 2026)
- [Conditions in the Intel 8087 floating-point chip's microcode](http://www.righto.com/2025/12/8087-microcode-conditions.html) (Dec 2025)
- [Silicon reverse-engineering: the Intel 8086 processor's flag circuitry](http://www.righto.com/2023/02/silicon-reverse-engineering-intel-8086.html) (Feb 2023)
- [Inside the 74181 ALU chip: die photos and reverse engineering](http://www.righto.com/2017/01) (Jan 2017)
- [Understanding silicon circuits: inside the ubiquitous 741 op amp](http://www.righto.com/2015/10) (Oct 2015)
- [Ken Shirriff's About Page](https://www.righto.com/p/about-ken-shirriff.html)
