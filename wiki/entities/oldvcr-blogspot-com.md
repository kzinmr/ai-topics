---
title: OldVCR (Cameron Kaiser / ClassicHasClass)
status: active
tags:
- person
---

# OldVCR (Cameron Kaiser / ClassicHasClass)

## Overview

**Cameron Kaiser** (blogging as **ClassicHasClass**) is a vintage computing researcher, software engineer, and open-source developer based at [[Floodgap Systems]]. He runs the blog **Old Vintage Computing Research** (oldvcr.blogspot.com), where he documents deep-dive technical explorations of retro computing platforms — particularly 6502-based systems, PowerPC workstations, PalmOS devices, Unix workstations, and the forgotten hardware of the 1970s–1990s.

Kaiser is the creator and maintainer of [[TenFourFox]] — the PowerPC-native Firefox fork that extended the usable life of aging Mac hardware long after Mozilla abandoned the platform. He has also contributed to [[Crypto Ancienne]], a TLS 1.2/1.3 library for pre-C99 compilers and vintage architectures. His work spans hardware teardowns, ROM analysis, emulator development, reverse engineering of obscure protocols, and the preservation of computing history through functional, not static, means.

He has written for *COMPUTE!*, *TidBITS*, and *Ars Technica*, and his guiding philosophy is captured in his blog motto: **"Be kind, REWIND and PLAY."**

---

## Timeline

| Period | Key Events |
|--------|-----------|
| 1980s–1990s | Early computing on 6502-based systems; develops interest in vintage hardware preservation |
| 1990s–2000s | Writes for *COMPUTE!*, *TidBITS*, and *Ars Technica* on vintage computing topics |
| ~2008 | Begins **TenFourFox** project — Firefox for PowerPC Macs (G3/G4/G5) after Mozilla drops support |
| 2011–2017 | Maintains TenFourFox through multiple Firefox versions, adding JIT compilation and modern web compatibility |
| 2013 | Launches **Old Vintage Computing Research** blog on oldvcr.blogspot.com |
| 2018–2020 | Develops **Crypto Ancienne** — TLS library for vintage architectures |
| 2020 | Announces end of TenFourFox development; shifts focus to hardware preservation |
| 2021 | Begins **6o6** project — a virtualized 6502-on-6502 CPU core written in 6502 assembly |
| 2021 | Publishes **Incredible KIMplement** — KIM-1 emulator running on Commodore 64 |
| 2023 | Crypto Ancienne 2.2 released with AmigaOS and classic MacOS/MPW support |
| 2024 | 6o6 v1.0 open-sourced on GitHub; "Virtualizing the 6502 with 6o6" published |
| 2025 | Symbolics MacIvory Lisp machine restoration documented in deep-dive teardown |
| 2026 | 6o6 v1.1 released with 2.6% performance improvement; hands-on with Apple Network Server prototype ROMs; Scriptovision Super Micro Script analysis |

---

## Core Ideas

### Preservation Through Function, Not Museum

Kaiser's approach to vintage computing is fundamentally different from static preservation. He doesn't just collect old machines — he **makes them do things**. His motto "REWIND and PLAY" captures this: the goal is not to admire vintage hardware behind glass, but to boot it, run software on it, push it to its limits, and discover what it can still do.

His **TenFourFox** project epitomized this philosophy. While other PowerPC preservation efforts focused on archival dumps or emulator development, Kaiser built a fully functional, JIT-compiled Firefox browser that could render modern (for the time) web pages on G3, G4, and G5 Macs. He didn't just preserve the hardware — he preserved its *utility*.

### The Beauty of Deep Technical Archaeology

Kaiser's blog posts are remarkable for their depth. A typical entry might involve:

- **Dumping and unscrambling ROM data** from a 1985 video titler by tracing PCB connections with a multimeter
- **Reverse-engineering memory paging schemes** on obscure hardware
- **Building bytecode interpreters** for vintage machines
- **Tracing hardware bugs** through decades-old schematics

His analysis of the **Scriptovision Super Micro Script** (2026) is a masterclass: a Canadian-made video titler from 1985 that he discovered is architecturally "almost a home computer." He traces address line scrambling, maps the memory layout, implements a custom VM, and writes a bit-banged serial port driver — all for a $500 piece of forgotten hardware.

> "Terminals, however, are in many cases based on general purpose architectures, just lashed to restrictive firmware... Plus, there's a third group of computer-adjacent devices that qualify as well: the video titlers."

This is vintage computing as detective work — every machine tells a story, and Kaiser's job is to read it.

### Virtualization as a Bridge Between Eras

Kaiser's **6o6** project — a fully virtualized NMOS 6502 CPU core written in 6502 assembly — is perhaps his most technically ambitious work. The name means "6502-on-6502": a 6502 processor running a virtual 6502 processor.

> "6o6 implements a completely abstracted memory model and a fully controlled execution environment, but by using the host's ALU and providing a primitive means of instruction fusion it can be faster than a naïve interpreter."

This is not just a technical exercise — it's a philosophical statement about **layered abstraction**. By virtualizing a vintage CPU on itself, Kaiser demonstrates that the boundaries between "old" and "new" computing are artificial. The 6502, designed in 1975, can host its own emulator, proving that computational universality transcends the specific hardware era.

His **Incredible KIMplement** (a KIM-1 emulator on C64) follows the same principle: using vintage hardware to run vintage hardware, creating a recursion of computing history.

### The Anti-Commercial Stance

Kaiser is explicit about his motivation: this work is driven by passion, not profit. His blog is advertisement- and donation-funded (via Ko-fi), and he makes a point of stating: **"My promise: No AI-generated article text, ever."**

This is significant in the current landscape. While AI-generated content floods the internet, Kaiser's work is painstakingly, manually researched — every ROM dump, every PCB trace, every assembly instruction verified by human hands. The "no AI" promise is not anti-technology; it's pro-authenticity. It signals that his work is the product of genuine technical investigation, not automated summarization.

His **Crypto Ancienne** project extends this philosophy: building security infrastructure for machines that the security industry has entirely abandoned. While most TLS libraries target modern x86_64 and ARM, Crypto Ancienne supports pre-C99 compilers, AmigaOS, classic MacOS, and other architectures that the mainstream has left behind.

### Hardware as Historical Text

Kaiser reads hardware the way a historian reads documents. His teardown of the **Symbolics MacIvory Lisp machine** (2024) is not just a repair log — it's a historical narrative spanning MIT's AI Lab, the Lisp machine wars, the split between Symbolics and LMI, Chaosnet networking, and the evolution of Genera OS.

> "They existed in highly technical environments as workhorses of the first wave of AI hysteria (you crazy kids today with your LLMs) for applications like natural language processing and expert systems."

His parenthetical note about LLMs reveals his perspective: today's AI hype is just the latest wave in a long cycle. Lisp machines in the 1980s were the AI workstations of their era — purpose-built hardware for cutting-edge applications, eventually abandoned when the market shifted. The MacIvory is a cautionary tale about investing in specialized hardware that becomes stranded when the software ecosystem moves on.

### The Craft of Obsolescence

Kaiser's work consistently reveals the **craftsmanship embedded in obsolete technology**. His Apple Network Server prototype ROM analysis (2026) documents machines that were "one of Apple's last non-Macintosh computers before iOS" — a forgotten branch of Apple's hardware tree. He explores ROM variants that supported Windows NT, Mac OS, AIX, and Rhapsody, each representing a different strategic direction that Apple might have taken.

> "Hancock's late 1996 announcement that the Apple Network Server would optionally run Windows NT caught many industry observers by surprise..."

These are not just technical curiosities — they are **alternate histories** of computing. Every prototype ROM, every abandoned platform, every "what if" represents a path not taken. Kaiser's work preserves these paths so that future researchers can understand not just what computing became, but what it might have been.

---

## Key Quotes

> "Be kind, REWIND and PLAY."

> "My promise: No AI-generated article text, ever."

> "6o6 implements a completely abstracted memory model and a fully controlled execution environment, but by using the host's ALU and providing a primitive means of instruction fusion it can be faster than a naïve interpreter."

> "Terminals, however, are in many cases based on general purpose architectures, just lashed to restrictive firmware... Plus, there's a third group of computer-adjacent devices that qualify as well: the video titlers."

> "They existed in highly technical environments as workhorses of the first wave of AI hysteria (you crazy kids today with your LLMs) for applications like natural language processing and expert systems."

> "Because the harness is the sole memory access interface, it becomes a highly flexible virtual memory manager: it alone maps virtual addresses to physical addresses, so it can page things in and out, synthesize address space on the fly and/or throw exceptions and faults back to the kernel."

---

## Recent Themes (2024–2026)

**2024:** Open-sourced 6o6 v1.0 on GitHub. Documented Symbolics MacIvory Lisp machine restoration in extensive teardown series. Continued Crypto Ancienne development with AmigaOS and classic MacOS support.

**2025:** Published deep-dive analysis of Sun Ray thin client laptops and getting root access. Continued 6o6 development and optimization. Maintained vintage hardware collection at Floodgap Systems.

**2026:** Released 6o6 v1.1 with 2.6% performance improvement through zero-page optimization and hot-path instruction reduction. Published hands-on analysis of Apple Network Server prototype ROMs (NT, Mac OS, Rhapsody variants). Documented Scriptovision Super Micro Script teardown, ROM unscrambling, and custom VM development. Published memorial posts for computing industry figures (Hedley Davis, Hideki Sato, Stewart Cheifet).

---

## Related

[[TenFourFox]] — PowerPC-native Firefox fork maintained by Kaiser for over a decade
[[Crypto Ancienne]] — TLS 1.2/1.3 library for vintage architectures and pre-C99 compilers
[[Floodgap Systems]] — Kaiser's home base for vintage computing research
[[Commodore 64]] — Platform for Kaiser's 6o6 and Incredible KIMplement projects
[[Apple-1]] — Historical computer emulated within Kaiser's 6o6 virtualization framework
KIM-1 — MOS Technology single-board computer emulated via Incredible KIMplement
[[Symbolics]] — Lisp machine manufacturer; Kaiser restored a MacIvory system
Chaosnet — Early MIT networking technology documented in Kaiser's Lisp machine analysis
[[Apple Network Server]] — Obscure Apple server platform; Kaiser analyzed prototype ROMs
Scriptovision — Canadian video titler company; Kaiser reverse-engineered their hardware
[[raw/articles/substack.com--geraldwong116502--5f407893.md]] — MOS microprocessor; central to Kaiser's virtualization and emulation work
[[PowerPC]] — Processor architecture; Kaiser maintained TenFourFox for PowerPC Macs

---

## Sources

- [oldvcr.blogspot.com](https://oldvcr.blogspot.com) — Primary blog and research log
- *6o6 v1.1: Faster 6502-on-6502 Virtualization & Apple-1 Emulator* (March 2026)
- *Virtualizing the 6502 with 6o6 (and The Incredible KIMplement)* (April 2024)
- *The Scriptovision Super Micro Script video titler is almost a home computer* (February 2026)
- *Hands-on with two Apple Network Server prototype ROMs* (January 2026)
- *Refurb weekend: the Symbolics MacIvory Lisp machine I have hated* (October 2024)
- *Crypto Ancienne 2.2: now supported on AmigaOS and classic MacOS/MPW* (April 2023)
- *Of Sun Ray laptops, MIPS and getting root on them* (April 2023)
- [6o6 on GitHub](https://github.com/classilla/6o6) — 6502-on-6502 virtualization project
- [TenFourFox Development](https://tenfourfox.blogspot.com) — Related blog
- [floodgap.com](https://www.floodgap.com) — Floodgap Systems
- Ko-fi: ClassicHasClass — Donation-funded hardware preservation
