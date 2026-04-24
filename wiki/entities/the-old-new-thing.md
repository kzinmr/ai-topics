---
title: Raymond Chen
type: entity
status: active
tags:
- person
sources: []
---

# Raymond Chen

**URL:** https://devblogs.microsoft.com/oldnewthing/  
**Blog:** The Old New Thing (est. 2003)  
**Role:** Principal Software Engineer, Microsoft Windows team  
**Book:** *The Old New Thing* (Addison Wesley, 2007)  
**Current:** Still actively writing at devblogs.microsoft.com/oldnewthing as of March 2026

## Overview

Raymond Chen is a Principal Software Engineer at Microsoft who has been involved in the evolution of Windows for more than 30 years. Since 2003, he has written *The Old New Thing*, one of the most respected technical blogs in the industry — a deep, historical, and deeply informed exploration of why Windows works the way it does, why it doesn't work the way you wish it did, and why the answers almost always involve **backward compatibility**.

Chen's blog is unique in tech writing: it treats operating system history not as trivia but as **essential engineering knowledge**. Every quirk, every undocumented behavior, every design decision that seems arbitrary has a story behind it — and Chen knows those stories, often because he was there when they happened.

His intellectual project is fundamentally about **the cost of change** — why systems accumulate complexity, why breaking changes are more expensive than they appear, and why the people who complain about "legacy code" usually don't understand what it takes to replace it. He writes from inside one of the most backward-compatible systems ever built, and his writing is a sustained argument that **compatibility isn't a bug — it's a feature that requires enormous engineering effort to maintain**.

Chen's writing style is distinctive: precise, often witty, always technically rigorous. He explains complex ABI decisions, kernel-level compatibility shims, and historical design trade-offs with the clarity of someone who has spent decades thinking about these problems and explaining them to others. His posts are short, focused, and almost never include fluff.

## Timeline

| Date | Event |
|------|-------|
| 1980s | Works at a company producing language compilers and runtime systems for minicomputers; writes about the "good old days" of computing |
| 1990s | Joins Microsoft Windows team; works on core OS components and application compatibility |
| 2003 | Launches **The Old New Thing** blog — a site about Windows history, development, and the "why" behind OS design decisions |
| 2007 | Publishes *The Old New Thing* (Addison Wesley) — a book adapting blog content into a cohesive exploration of Windows programming and history |
| 2003–present | Writes hundreds of posts on The Old New Thing, covering topics from Win32 ABI quirks to Windows 95 setup architecture to clipboard text conversion |
| 2011 | Publishes a landmark post explaining why Windows doesn't just block apps that use undocumented behavior — the definitive statement of his backward compatibility philosophy |
| 2023 | Completes a retrospective series on Windows stack limit checking across multiple processor architectures (x86-32, Alpha AXP, MIPS, PowerPC, ARM64, x86-64) |
| 2024 | Covers Windows 95 setup's three-OS bootstrap process (MS-DOS → Windows 3.1 → Windows 95) |
| 2024–2026 | Continues active writing on The Old New Thing, covering everything from clipboard text conversion to IBM corporate culture to Windows 95 anti-overwrite protections |
| 2025 | Publishes deep dives into Windows 95 application compatibility patches and the porting of Windows 95 UI code to Windows NT |

## Core Ideas

### Backward Compatibility as a Moral Imperative

Chen's most important intellectual contribution is his sustained defense of backward compatibility as **not just a technical requirement but an engineering philosophy**. His 2011 post on why Windows doesn't simply block apps using undocumented behavior is the clearest articulation of this position:

> "Because every app that gets blocked is another reason for people not to upgrade to the next version of Windows."

He explains that corporations have at least one "deal-breaker" program — an application that the company absolutely cannot function without — and if Windows breaks it during an upgrade, the company simply won't upgrade. This isn't laziness; it's rational economic behavior:

> "Suppose you're the IT manager of some company. It takes only one incompatible program to sour an upgrade."

The implications of this philosophy extend far beyond Windows. Chen is arguing, consistently and persuasively, that **the people who use your software are not abstractions — they have real workflows, real investments, and real reasons why the thing that works today needs to keep working tomorrow**. His compatibility shims aren't cruft; they're the price of serving actual humans.

### The Archaeology of OS Design

Chen treats operating system history as **archaeology**. Every design decision, no matter how seemingly arbitrary, is an artifact of a specific time, a specific set of constraints, and a specific trade-off. His posts are essentially archaeological dig reports:

> "Many times, the compatibility fix is made inside the core component [...] Sorry, you won't be able to browse it easily."

His series on Windows stack limit checking across processor architectures (Alpha AXP, MIPS, PowerPC, ia64, ARM64, x86-64) is a masterclass in this approach. He doesn't just describe what each ABI does — he explains **why** it does it, tracing the design decisions back to the hardware capabilities and constraints of each platform.

This archaeological approach reveals a deeper insight: **systems are not designed; they evolve**. The Windows clipboard text conversion system, for example, is a mess — but Chen explains that the mess is the accumulated result of decades of incremental changes, each one justified at the time, each one preserving compatibility with the layer below:

> "Perfect is the enemy of good. [...] It's often better to have a simple set of easy-to-remember rules, even if they don't cover all the cases, rather than to have a complex set of rules that tries to cover more cases but inevitably still fails to get them all."

### Undocumented Behavior Is a Social Contract

One of Chen's recurring themes is the relationship between **documented interfaces and the actual behavior of systems**. Developers often rely on undocumented behavior because it works — and Chen's position is nuanced: he doesn't condemn these developers, but he also doesn't excuse them.

His explanation of Windows 95 compatibility patches reveals the practical reality: the OS team sometimes had to patch individual applications because the alternative was breaking the ecosystem. He wrote patches himself:

> "I chose this example because it's one of the patches I wrote. It fixes a bug in a sound card driver that corrupts registers during a hardware interrupt."

The lesson isn't "always document everything." The lesson is that **systems and their users exist in a relationship, and that relationship is messier than any specification can capture**.

### Practical Development Over Theoretical Purity

Chen consistently advocates for **pragmatism over idealism** in systems design. His post on Windows 95 setup explains why the installation process used three operating systems (MS-DOS → Windows 3.1 → Windows 95) instead of booting directly into Windows 95:

> "One option is to write three versions of Windows 95 setup [...] This was not a pleasant option because you basically did the same work three times."

The solution — a single code base that runs across all three environments, with each stage doing only what it needs to — is elegant precisely because it respects the constraints of the real world. This pattern recurs throughout Chen's writing: **the best solution is the one that works within the actual constraints, not the one that would be ideal in a vacuum**.

### The Human Element in Technical History

Chen's writing is full of human details — IBM corporate culture jokes, custom business cards from the Windows 95-to-NT porting team, anecdotes about specific bugs and the people who fixed them. This isn't decoration; it's a statement of belief that **technical history is human history**. The decisions that shaped Windows were made by people, in meetings, under constraints, with imperfect information. Understanding the human context is essential to understanding the technical outcome.

### "Perfect Is the Enemy of Good"

This phrase captures Chen's entire approach to systems design. His explanation of why Windows didn't fix clipboard text conversion when UTF-8 support was added to `CP_ACP` is a case study:

> "This is a case of perfect being the enemy of good. The ability to specify a custom activeCodePage as CP_ACP was scoped primarily to allowing CP_ACP to be customized on [...] Chasing down every last one of them would have taken a long time, and then the activeCodePage team would [have had to deal with it]. At least the current version is clear about what it does."

Chen understands that **every "fix" has a cost**, and that cost includes not just engineering effort but the risk of breaking something that currently works. His preference for "simple rules that don't cover all cases" over "complex rules that try to" is a philosophy of **bounded rationality applied to software engineering**.

## Key Quotes

> "Every app that gets blocked is another reason for people not to upgrade to the next version of Windows."

> "It takes only one incompatible program to sour an upgrade."

> "Perfect is the enemy of good. [...] It's often better to have a simple set of easy-to-remember rules, even if they don't cover all the cases."

> "The Old New Thing" — the blog's title itself is a philosophical statement: what is old becomes new again, what is new will become old, and understanding the cycle is the point.

> "Raymond has been involved in the evolution of Windows for more than 30 years. [...] The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally [still writes about it]."

> "The compatibility workarounds no longer sully the core OS files. (Not all classes of compatibility workarounds can be offloaded to a compatibility DLL, but it's a big help.)" — on the Windows XP AppPatch architecture

> "If your processor doesn't support 32-bit comparisons, then sign-extending all 32-bit values (even the unsigned ones) is the natural choice." — explaining ABI design decisions across architectures

## Recent Themes (2024–2026)

- **Windows 95 architecture retrospectives**: Deep dives into setup bootstrapping, application compatibility shims, and installer protections against file overwrites
- **Stack limit checking across architectures**: A multi-part series examining how different processor ABIs handle guard pages and stack overflow detection (Alpha AXP, MIPS, PowerPC, ia64, ARM64, x86-64)
- **Windows NT and Windows 95 code convergence**: How the Windows 95 UI was ported to the Windows NT codebase, including bidirectional merges and `#ifdef WINNT` protection
- **Clipboard text conversion analysis**: A detailed examination of `CF_TEXT`, `CF_OEMTEXT`, and `CF_UNICODETEXT` conversions and why UTF-8 support didn't "fix" the underlying mess
- **Windows ABI evolution**: Analysis of how different 64-bit processor ABIs pass 32-bit values in 64-bit registers, tracing the security and compatibility implications
- **Historical corporate culture**: Posts on IBM dress codes, Microsoft's internal source control (SLM/"slime"), and the human stories behind technical decisions
- **Continued active writing**: Chen has maintained a consistent output of technical posts through March 2026, covering both historical deep-dives and contemporary development questions

## Related

- [[Windows]] — The operating system Chen has worked on for 30+ years
- [[Windows 95]] — Frequent subject of Chen's historical analysis; the OS that defined modern Windows compatibility expectations
- [[Windows NT]] — The codebase that absorbed Windows 95's UI; Chen's writing traces this convergence in detail
- [[Application Compatibility]] — Chen's primary area of expertise; the practice of preserving working behavior across OS updates
- [[The Old New Thing (book)]] — Chen's 2007 book adapting blog content
-  — The central philosophical theme of Chen's entire body of writing
-  — Chen's recent posts on processor-level ABI decisions and their implications
-  — Chen's employer for 30+ years

## Sources

- The Old New Thing (devblogs.microsoft.com/oldnewthing/) — Primary blog, active since 2003
- *The Old New Thing* by Raymond Chen (Addison Wesley, 2007)
- "Why not just block the apps that rely on undocumented behavior?" (December 2003)
- "Behind the scenes on how Windows 95 application compatibility patched broken programs" (November 2025)
- "Windows 95 defenses against installers that overwrite a file with an older version" (March 2026)
- "How did the Windows 95 user interface code get brought to the Windows NT code base?" (November 2025)
- "Concluding thoughts on our deep dive into Windows clipboard text conversion" (December 2025)
- "On how different Windows ABIs choose how to pass 32-bit values in 64-bit registers" (March 2025)
