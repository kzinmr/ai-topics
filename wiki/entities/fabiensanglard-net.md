---
title: Fabien Sanglard
created: 2026-04-09
updated: 2026-04-10
tags:
- person
- blogger
- hn-popular
- game-engines
- reverse-engineering
- performance
- computer-history
aliases:
- fabiensanglard.net
- fabien-sanglard
---

# Fabien Sanglard

| | |
|---|---|
| **Blog** | [fabiensanglard.net](https://fabiensanglard.net) |
| **RSS** | https://fabiensanglard.net/rss.xml |
| **Role** | Software engineer, author of the *Game Engine Black Book* series |
| **Known for** | Deep technical analysis of classic game engines (DOOM, Quake, Wolfenstein 3D), performance optimization studies, hardware restoration projects |
| **Bio** | French software engineer who reverse-engineers and documents classic game engines with extraordinary depth. Author of *Game Engine Black Book: Wolfenstein 3D* and *Game Engine Black Book: DOOM*. Recently undertook a multi-month project restoring and benchmarking a 1990s IBM PS/1 to understand Quake-era hardware firsthand. |

## Core Ideas

### Game Engines as Archaeological Artifacts

Fabien treats game engines the way an archaeologist treats excavation sites: **every layer tells a story about the constraints, decisions, and ingenuity of its creators.** His *Game Engine Black Book* series doesn't just explain how engines work — it reconstructs the entire context: the hardware they ran on (Intel 486, NeXTStation TurboColor, PlayStation MIPS R3000A), the compilers available (Watcom C), the operating systems (DOS extenders), and the commercial pressures (shipping within one year).

His approach to DOOM's console ports reveals this philosophy: the PSX port wasn't just a port — it was a complete engine rewrite with triangle-based rendering, CD-ROM filesystems, and SPU audio, all constrained by 2 MiB of DRAM and a 33.8 MHz processor with no floating-point unit. Understanding the port requires understanding the machine.

> *"For every better, faster, energy-efficient CPU/Storage/RAM element produced by hardware designers it seems there are ten programmers ready to add a hundred features."*

### Performance as a Measurable, Commit-Level Discipline

Fabien's **fastDOOM analysis** (March 2025) is a masterclass in empirical performance engineering. He didn't just benchmark the end result — he downloaded all 52 releases of fastDOOM, wrote Go programs to generate automated timedemo scripts, and benchmarked at the **commit level** across 3,042 individual commits. This revealed that early optimization was mostly **code deletion** (50% of v0.1 commits removed code), and that specific patches (the "Crispy optimization" skipping status bar redraws) delivered measurable FPS gains.

His **Quake ASM analysis** (Feb 2026) quantified exactly how Michael Abrash doubled Quake's framerate: `D_DrawSpans8` contributed +12.6 fps, `R_DrawSurfaceBlock8_mip*` +4.2 fps, `D_Polyset*` +2.2 fps. The rest barely registered. This granular attribution — knowing exactly which function does what — is rare and valuable.

### Constraints Create Creativity

A consistent theme in Fabien's writing: **the best engineering happens under tight constraints.** DOOM shipped in under a year, leaving optimization on the table. The PSX port team found themselves with *extra* CPU cycles and used them to add animated fire — not because they planned to, but because the constraints forced them to be efficient enough to have cycles left over. The DOOM fire effect itself is a thing of beauty: a simple array of values [0–36] mapped to a palette, propagated upward with random cooling, producing mesmerizing output with minimal code.

His analysis of Quake's hand-crafted assembly reveals techniques that modern programmers have forgotten: self-modifying code to bake constants into opcodes, using the FPU's `fxch` (0 cycles) as a free register swap, overlapping integer and floating-point pipelines, and avoiding branch mispredictions through jump tables and unsigned comparisons.

### Anti-Bloat Philosophy

In his 2018 article *"Bloated"*, Fabien documented his frustration with modern web pages that require seconds to load, trigger laptop fans, and drop to 15 fps on scroll — all on hardware far more powerful than what runs DOOM at 60 fps. His own website required 23 HTTP requests and 1.5 MiB to show six images and a banner.

His response: **radical minimalism.** He stripped comments, removed JavaScript, and committed to text, SVGs, and WebP images. This wasn't just aesthetic — it was a philosophical stance that engineers should take responsibility for resource consumption.

> *"It was time for this website to change... it seems like an increasingly good idea to take a few steps back and wonder if we are doing our best to use only what is needed. And do what we can about it, however infinitesimal we think we are."*

### Visual Documentation as a Primary Medium

Fabien's books are **full color, heavily illustrated**, because he believes that drawings and diagrams are essential to understanding. Text alone isn't enough to explain how a rasterizer works or how a console port managed memory. His 427-page DOOM book contains extensive drawings of the NeXTStation hardware, the DOOM engine architecture, and the rendering pipeline.

> *"Don't expect much prose... Instead you will find inside extensive descriptions and drawings to better understand all the challenges."*

This commitment to visual explanation reflects a deeper belief: **if you can't draw it, you don't understand it.**

### The Hardware Restoration Project

In late 2025 and early 2026, Fabien undertook a multi-part series restoring an **IBM PS/1 486-DX2 66MHz** (model 2168) — the exact machine that would have run Quake in 1996. He didn't just emulate it; he bought the physical hardware, upgraded the L2 cache, configured DOS, installed DOS extenders, compiled from source with period-appropriate tools, and benchmarked real software.

This reflects a core belief: **you can't truly understand historical software without running it on historical hardware.** Emulators abstract away the very constraints that shaped the engineering decisions.

## Key Quotes

> *"For every better, faster, energy-efficient CPU/Storage/RAM element produced by hardware designers it seems there are ten programmers ready to add a hundred features."*

> *"It seems like an increasingly good idea to take a few steps back and wonder if we are doing our best to use only what is needed. And do what we can about it, however infinitesimal we think we are."*

> *"Don't expect much prose... Instead you will find inside extensive descriptions and drawings to better understand all the challenges."*

> *"If software can die from a thousand cuts, Viti95 made fastDOOM awesome with three thousand optimizations!"*

## Related

- [[game-engine-architecture]] — How classic engines were structured and evolved
- [[software-rendering]] — Rasterization, span drawing, BSP trees, portal rendering
- [[performance-optimization]] — Commit-level benchmarking, code deletion as optimization
- [[assembly-optimization]] — Pipeline overlap, self-modifying code, FPU register management
- [[id-software]] — Creator of DOOM, Quake, Wolfenstein 3D — Fabien's primary subject matter
- [[john-carmack]] — Engine architect whose designs Fabien analyzes in depth
- [[michael-abrash]] — Graphics programmer who wrote Quake's ASM optimizations
- [[hardware-constraints]] — How limited resources drive creative engineering
- [[minimalism-in-software]] — Fabien's anti-bloat philosophy
- [[visual-documentation]] — Using diagrams and drawings to explain complex systems

## Sources

- [Why fastDOOM is fast](https://fabiensanglard.net/fastdoom/index.html) (Mar 2025)
- [How Michael Abrash doubled Quake framerate](https://fabiensanglard.net/quake_asm_optimizations/index.html) (Feb 2026)
- [How DOOM fire was done](https://fabiensanglard.net/doom_fire_psx/) (Dec 2018)
- [Game Engine Black Book: DOOM](https://fabiensanglard.net/gebbdoom/) (Dec 2018)
- [Bloated](https://fabiensanglard.net/bloated/) (Sep 2018)
- [Building a Quake PC series](https://fabiensanglard.net/) (Jan 2026)
- [Doom3 Notes](https://www.fabiensanglard.net/doom3/doom3_notes.txt)
