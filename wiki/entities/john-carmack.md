---
title: John Carmack
created: 2026-04-13
updated: 2026-04-13
depth_tracking: {'L1_basic_profile': True, 'L2_timeline_works': True, 'L3_thought_analysis': True, 'L4_ongoing_monitoring': False}
tags:
  - person
  - game-engineer
  - vr
  - agi
  - keen-technologies
  - id-software
---


# John D. Carmack II

| | |
|---|---|
| **Role** | Founder, Keen Technologies; Former CTO, Oculus/Meta; Co-founder, id Software |
| **Born** | August 20, 1970 (Kansas, USA) |
| **Known for** | Doom, Quake engines; Asynchronous Timewarp (VR); id Software co-founder; AGI research via Keen Technologies |
| **Bio** | A legendary game programmer and VR pioneer turned AGI researcher. His career spans self-taught engine architecture (Doom/Quake), commercializing VR (Oculus), and now pursuing artificial general intelligence through Keen Technologies. |

## Overview

John Carmack is one of the most influential programmers in computer science history. From self-taught assembly programming as a teenager to creating the **Doom** and **Quake** engines, to pioneering **Asynchronous Timewarp** for VR at Oculus, his career demonstrates a consistent pattern of solving hard engineering problems through elegant, low-level optimization.

Since 2022, he has pivoted to AGI research via **Keen Technologies**, advocating for RL-first approaches and proposing novel hardware architectures like **fiber-optic L2 cache** for massive model serving.

> *"I will never waste time making code more flexible just for the sake of making flexibility. It generally makes code more abstract and difficult to reason about, and it is a common source of bugs."*

## Early Life and Self-Taught Foundations

Born August 20, 1970, in Kansas. Developed a "normal, gifted-geek childhood" focused on chemistry, model rockets, and sci-fi. Influenced by Robert A. Heinlein's "competent libertarian vibe."

- **Autodidactic Path**: Bypassed formal education after two semesters at UMKC (1988), prioritizing hands-on assembly/BASIC programming.
- **Early Hacks**: At ~14, used a homemade thermite charge to break into a school to recover confiscated Apple IIs. Created *Shadowforge*, an Apple II RPG, demonstrating early low-level optimization skills.

## id Software & Engine Architecture (1991–2009)

### Softdisk Era (1990)
Met John Romero. Developed *Hovertank 3D* using raycasting (10–20 FPS on 286s). Frustrated by corporate constraints, co-founded id Software (Feb 1991).

### Shareware Revolution
Pioneered free-first distribution. *Commander Keen* & *Wolfenstein 3D* (1992) generated $30k–$60k/mo; *Wolf3D* sold 200k+ copies by 1993, proving viral PC gaming viability.

### Doom (1993)
Introduced **Binary Space Partitioning (BSP)** for efficient 3D rendering; achieved **35 FPS** on 33 MHz 486 CPUs. First commercial use of BSP for real-time rendering.

### Quake / id Tech 2 (1996)
Shifted to true 3D polygonal geometry. Implemented **client-server TCP/IP architecture** with **client-side prediction** to mask modem latency.

### Quake III / id Tech 3 (1999)
Added real-time stencil shadow volumes, curved surface tessellation, and NVIDIA register combiner shaders. Optimized for **60 FPS** multiplayer with 16-player netcode. Reverse algorithm for **stencil shadow volumes**.

### id Tech 5 / Rage (2011)
Pioneered megatextures (virtual texturing). Streaming up to **22 TB** of uncompressed data. PC-optimized but struggled on Xbox 360/PS3 due to VRAM/bandwidth bottlenecks.

### ZeniMax Acquisition (2009)
Sold to ZeniMax Media for **$150 million**. The deal provided financial stability but introduced corporate bureaucracy, reducing id's rapid iteration agility.

> *"Story in a game is like a story in a porn movie. It's expected to be there, but it's not that important."*

## Virtual Reality at Oculus & Meta (2013–2022)

### Entry & Demo
Discovered Oculus Rift prototype on enthusiast forums, ported *Doom 3*, and demonstrated it at E3 2012, proving low-latency VR feasibility.

### CTO Role (Aug 2013)
Focused on hardware-software synergy. Key innovation: **Asynchronous Timewarp**, which reprojects frames between render/display cycles to cut latency to **<20 ms**, preventing motion sickness.

### Open Development
Publicly released code samples, rendering optimizations, and dev logs, democratizing VR techniques and accelerating Quest 2 adoption (10M+ units by mid-2021).

### Strategic Friction
Critiqued Meta's metaverse timeline as premature. Advocated for hardware efficiency over ad-driven social features. Noted severe internal inefficiencies: *"5% GPU utilization in production workloads"* and organizational overhead cutting effectiveness by ~50%.

### Departure
Transitioned to consulting (2019), fully resigned Dec 2022 to pursue AGI independently.

## Aerospace: Armadillo Aerospace (2000–2013)

- **Mission**: Develop low-cost, reusable VTVL suborbital rockets via iterative, garage-style engineering.
- **Tech & Milestones**: Ethanol/LOX bipropellant engines, pressurized tank feeding, gimballing control. Conducted **200+ test flights**. Won **$350,000** NASA Lunar Lander Challenge (Level 1, 2008).
- **Challenges**: High failure rate (explosions, ballute/landing gear issues), FAA regulatory delays, and capital constraints.
- **Investment**: >$8M personal investment before 2013 hibernation.

## AGI Research: Keen Technologies (2022–present)

Founded in 2022, Keen Technologies represents Carmack's full-time commitment to AGI research.

### Seed and Partnerships
- **$20M seed funding** (2022).
- Partnership with **Richard Sutton**, a leading RL researcher.
- Advocates for RL-first approaches to AGI, rather than LLM-based scaling.

### Technical Proposals
- **Fiber-Optic L2 Cache** (Feb 2026): Proposed leveraging **256 Tb/s** over 200 km loops to stream **32 GB** model weights at **32 TB/s** bandwidth.
- Focus on hardware-software co-design for efficient model serving.

### Philosophy
Carmack has consistently argued that current LLMs lack true reasoning capabilities, and that AGI will require fundamentally different architectures than statistical pattern matching. His approach emphasizes reinforcement learning and causal reasoning.

## Core Ideas & Philosophy

### Engineering Pragmatism
> *"Success comes less from the language choice and more from the skill and restraint of the programmer."*

Carmack advocates for minimal, well-understood code over complex abstractions. He believes that simplicity and discipline are more important than language features or frameworks.

### VR as a Platform
He views VR as a fundamentally important computing platform, but argues that current implementations are premature and lack the hardware efficiency needed for mass adoption.

### AGI via RL
Carmack aligns with Richard Sutton's "Bitter Lesson" thesis: general methods that leverage computation (like RL) ultimately outperform hand-engineered solutions.

## Key Quotes

> *"I will never waste time making code more flexible just for the sake of making flexibility."*

> *"Story in a game is like a story in a porn movie. It's expected to be there, but it's not that important."*

> *"Success comes less from the language choice and more from the skill and restraint of the programmer."*

> *"5% GPU utilization in production workloads"* — On Meta's inefficiency

## Timeline

| Year | Event |
|------|-------|
| 1970 | Born in Kansas |
| 1988 | Two semesters at UMKC; leaves college |
| 1991 | Co-founds id Software with John Romero |
| 1993 | Doom released; first commercial BSP usage |
| 1996 | Quake released; true 3D polygonal geometry |
| 1999 | Quake III Engine; 60 FPS competitive netcode |
| 2000 | Armadillo Aerospace founded |
| 2008 | Wins NASA Lunar Lander Challenge |
| 2009 | id Software sold to ZeniMax for $150M |
| 2011 | id Tech 5 / Rage released |
| 2013 | Joins Oculus as CTO |
| 2019 | Transitions to consulting |
| 2022 | Keen Technologies founded; $20M seed |
| 2022 | Fully resigns from Meta |
| 2026 | Proposes fiber-optic L2 cache for AGI |

## Related

- [[John Romero]] — id Software co-founder
- [[Richard Sutton]] — Keen Technologies partner; RL pioneer
- [[reinforcement-learning]] — Carmack's preferred AGI approach
- [[bitter-lesson]] — Sutton's thesis that Carmack advocates
- [[keen-technologies]] — Carmack's AGI company

## Sources

- Grokipedia: John Carmack
- Keen Technologies announcements (2022–2026)
- id Software history
- Oculus VR technical documentation
