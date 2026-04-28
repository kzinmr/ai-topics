---
title: "Pixelmelt (Cats with Power Tools)"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Pixelmelt (Cats with Power Tools)

**URL:** https://blog.pixelmelt.dev (primary), https://blog.exploit.cat (secondary)  
**Blog:** Cats with Power Tools  
**Identity:** "Pixelmelt" — pseudonymous security researcher and reverse engineer  
**Active:** ~2024–present  
**Themes:** JavaScript obfuscation analysis, reverse engineering, DRM circumvention, web security, VM crackmes, anti-debugging bypass  

## Overview

**Cats with Power Tools** is a technical blog by a researcher operating under the pseudonym **Pixelmelt**. The blog focuses on the offensive side of web security — specifically, how JavaScript-based protection mechanisms work, how they fail, and how to dismantle them systematically. The name is deliberately whimsical for a serious subject: the "power tools" are debuggers, disassemblers, and custom deobfuscation scripts, and the "cats" are the researchers who wield them.

The blog operates on a dual domain (blog.pixelmelt.dev and blog.exploit.cat), with the latter serving as a secondary/mirror identity. The author uses Matomo analytics with custom tracking endpoints named `hiss` and `meowmeow`, a detail that reveals a consistent aesthetic: **take security work seriously, but don't take yourself too seriously.**

Pixelmelt's work sits at the intersection of reverse engineering and web application security. Unlike most security blogs that focus on traditional binary exploitation or network-level attacks, Pixelmelt specializes in the **JavaScript runtime as an attack surface** — analyzing virtualization obfuscators, defeating devtools detection, extracting protected content from DRM'd web readers, and building custom tools to automate deobfuscation pipelines.

## Timeline

| Date | Event |
|------|-------|
| ~2024 | Blog becomes active with posts on JavaScript obfuscation techniques |
| 2024 | "JavaScript Obfuscation Tricks" — overview of common JS protection methods |
| 2024 | "Branch Encryption" — analysis of control-flow encryption in obfuscated JavaScript |
| 2024 | "Overview of JavaScript Virtualization Obfuscation" — explains how JS code is compiled to a fantasy CPU architecture to prevent analysis |
| 2024–2025 | Builds and publishes JavaScript VM crackmes as training exercises for the security community |
| 2025 | "Try-Catch Control Flow Obfuscation" — documents how exception handling is weaponized to create non-linear execution paths |
| Mar 2025 | "Defeating DevTools Detection" — comprehensive guide to bypassing anti-debugging techniques used by malicious websites, including LibreWolf browser patching |
| 2025 | "How I Reversed Amazon's Kindle Web Obfuscation Because Their App Sucked" — full DRM circumvention pipeline using SVG perceptual hashing and SSIM matching |
| 2025 | "Building The Language Model Nobody Asked For" — experiments with custom language models (title admits: "Nobody explicitly asked for this but the signs were always there") |
| 2025 | "Analysing PistolJSVM" — deep dive into a specific JavaScript virtual machine implementation |
| 2025 | "Recursive vs Linear JSVM Disassembly" — compares disassembly strategies for virtualized JavaScript |
| 2025 | "A Clever But Not-So-Good Scraper Protection" — critique of an anti-scraping mechanism |
| 2025 | "The Webs Digital Locks Have Never Had a Stronger Opponent" — broader analysis of web-based DRM trends |
| 2026 | Blog remains active; continues publishing on JS reverse engineering and web security |

## Core Ideas

### JavaScript Virtualization as Obfuscation

Pixelmelt's foundational insight about JS virtualization obfuscation is elegantly simple:

> "Given that no protection is impossible to break by nature of how computers work (they must be able to see instructions to execute them), all you can really do is abstract the way the program runs."

The technique works by compiling JavaScript source code into a custom bytecode format that runs on a **fantasy CPU** implemented in JavaScript itself. This creates multiple layers of indirection between the original logic and its runtime representation:

```javascript
let program = [1, 1, 1, 2, 2]
let datapointer = 0
let memory = []

while(datapointer != program.length){
  switch(program[datapointer++]){
    case 1: // push next number to memory
      memory.push(program[datapointer++])
      break;
    case 2: // add top two numbers in memory
      memory.push(memory.pop() + memory.pop())
      break;
  }
}
```

This virtualized program is semantically identical to `1 + 2;` but vastly harder to analyze. Pixelmelt notes that **web protections are easier to crack than binary protections** because the security ecosystem around browser-based code is less mature, and the execution environment (JavaScript in a browser) is inherently more inspectable than compiled machine code.

### The Arms Race: DevTools Detection vs. Browser-Level Bypasses

One of Pixelmelt's most significant contributions is the analysis of **anti-debugging detection** used by malicious websites. The blog documents a progression of detection techniques and why conventional bypasses fail:

**Detection Methods:**
- **Timing side-channels:** Measuring console rendering latency (35k `console.error` calls with unique values to prevent browser folding)
- **Debugger keyword traps:** `debugger;` statements that pause execution when DevTools is attached
- **Viewport resize listeners:** Detecting the panel resize when DevTools docks
- **Source map fetching:** Server-side logging of `.map` file requests
- **Property traps:** `Object.defineProperty` on `Error.stack` getters (patched in Firefox April 2024)

**Why Client-Side Bypasses Fail:**

> "The problem is, we've been fighting on the wrong battlefield... The browser itself is telling on you. Like trying to stop a leak from inside a submarine with duct tape."

Pixelmelt's solution is radical: **patch the browser at compile time** rather than trying to intercept JavaScript at runtime. The recommended approach uses LibreWolf (a privacy-focused Firefox fork) with specific configuration changes:

| Setting | Purpose |
|---|---|
| `librewolf.console.logging_disabled` | Guts `onConsoleAPILogEvent`, making console access invisible to timing attacks |
| `librewolf.debugger.force_detach` | Blocks `debugger` keyword traps by returning early from the attach handler |
| `devtools.toolbox.host = window` | Opens DevTools in a separate OS window, bypassing resize detection |
| `devtools.source-map.client-service.enabled` = `false` | Prevents automatic source map fetching that triggers server-side logging |

> "Ironically resisting fingerprinting has become a fingerprint itself."

This observation captures a meta-problem in web security: privacy-preserving configurations can themselves become identifying signals.

### DRM Circumvention: The Kindle Case Study

The Kindle Web DRM post is Pixelmelt's most technically ambitious piece, documenting a complete pipeline for extracting text from Amazon's web-based Kindle reader:

**Amazon's Defense Layers:**
1. **Substitution cipher:** Characters map to non-sequential glyph IDs (`'T'` → `24`)
2. **Dynamic randomization:** Entire alphabet remaps every 5 pages (API hard limit)
3. **Fake font hints:** Micro SVG `m` commands that render fine in browsers but break naive parsers
4. **Multiple variants:** 4 font styles + ligatures → 361 unique unique glyphs per book
5. **Scale:** 920-page book = 184 API requests = 1,051,745 total glyphs to decode

**The Solution:** Pixelmelt bypassed OCR (51% accuracy) by using **perceptual hashing + SSIM matching**:
1. Render SVG glyphs to 512×512px images using `cairosvg`
2. Generate perceptual hashes for each glyph
3. Download official Bookerly TTF fonts and render full character reference set
4. Use **Structural Similarity Index (SSIM)** to match unknown glyphs to known characters
5. Leverage JSON positioning data to reconstruct formatting (paragraph breaks, styling, links)

**Results:** 361/361 glyphs matched (100%), 5,623,847 characters decoded across 920 pages. The final EPUB was "near indistinguishable from the original."

> "We are in a renaissance era of reverse engineering. Defenders are going to be on the back foot until we figure out some way to cope with LLMs."

This statement reveals Pixelmelt's broader worldview: the current moment represents a golden age for reverse engineering, where AI tools lower the barrier to entry but also create new challenges for defenders.

### Control Flow Obfuscation via Exception Handling

The try-catch obfuscation technique is deceptively simple but effective:

```javascript
function foo(input) {
    let stage = 0;
    try {
        stage = 42;
        if (stage === 42) {
            nonExistentFunction(); // ReferenceError
        }
        return false; // Never executes
    } catch (e) {
        if (stage === 42) {
            return input === "secret_value"; // Actual payload
        }
        return false; // Decoy for direct catch access
    }
}
```

The key insight is that **the error is the intended control flow mechanism**, not a bug to be handled. By chaining multiple try-catch blocks with error objects carrying state information, developers can create execution graphs that are nearly impossible to follow through static analysis alone.

> "A lot of VMs I worked on in the past would also exploit errors to force a catch execution to continue." — Draco (commenter)

## Notable Projects

### JavaScript VM Crackmes
Pixelmelt publishes custom JavaScript virtual machine implementations as crackme challenges for the security community. These serve as both educational tools and proof-of-concept demonstrations of virtualization obfuscation techniques.

### PistolJSVM Analysis
A deep technical analysis of the PistolJSVM implementation, covering both recursive and linear disassembly approaches. This work demonstrates that virtualized JavaScript can be systematically decompiled with the right methodology.

## Writing Style and Approach

Pixelmelt's writing has several distinctive characteristics:
- **Self-deprecating humor:** "I lied in the title, well, sort of" appears in multiple posts
- **Practical focus:** Every post includes working code examples, not just theory
- **Adversarial framing:** The author positions themselves as attacking protections, not defending them
- **Community engagement:** Quotes and credits commenters (e.g., "Draco") who contribute insights
- **Tool-building mentality:** Doesn't just analyze — builds scripts, configurations, and crackmes
- **Ethical clarity:** Explicitly states work is for backing up legally purchased content, not piracy

## Key Quotes

> "All you can really do is abstract the way the program runs."

> "The browser itself is telling on you. Like trying to stop a leak from inside a submarine with duct tape."

> "We are in a renaissance era of reverse engineering. Defenders are going to be on the back foot until we figure out some way to cope with LLMs."

> "I PAID FOR THIS BOOK. It's mine. And I'm going to read it in Calibre with the rest of my library even if I have to reverse engineer their web client to do it."

## Contact

- **Email:** `pixelmelt + at + protonmail.com` (noted humorously as "for Amazon affiliates")

## See Also

- [[entities/_index]]
