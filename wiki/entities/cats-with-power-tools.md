---
title: "Pixelmelt (Cats with Power Tools)"
tags: [person]
sources:
  - raw/articles/blog.pixelmelt.dev--training-a-reinforcement-learning-model-to-play-bonk-io--dbec950e.md
created: 2026-04-24
updated: 2026-08-15
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
| Aug 2026 | "Training a Reinforcement Learning Model to Play Bonk.io" — extracts the game's Box2D physics engine from JScrambler-obfuscated JS, ports it to Rust with an LLM (1961/1961 bit-identical maps), and trains a scratch PPO agent (10B frames, Elo 5th/522) |

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

### LLM-Assisted Code Porting: The Bonk.io RL Project (Aug 2026)

In "[Training a Reinforcement Learning Model to Play Bonk.io](https://blog.pixelmelt.dev/training-a-reinforcement-learning-model-to-play-bonk-io/)" (Aug 2026), Pixelmelt demonstrates the full pipeline of using **LLMs for verifiable code porting** — an extension of the blog's reverse-engineering ethos into game AI:

**Extracting the physics engine from obfuscated JS:**
- Bonk.io's client is protected with **JScrambler** and is "completely incomprehensible"; a friend (Ciaran) did the heavy lifting deobfuscating the JScrambler build, while Pixelmelt reversed the remaining non-JScrambler bonk-specific obfuscation
- The game runs a modified build of **Box2DWeb** (a JS port of the flash-era Box2D engine). Because Bonk.io uses deterministic lockstep networking, every client simulates the entire game locally and the physics is a **pure function**: same state + same inputs → same floats, bit for bit. The game rebuilds the entire physics world from scratch every frame from a plain JSON state — no persistent world
- After staring at **31,339 lines** of deobfuscated code, the engine was confirmed to be exactly the pure function needed for RL training

**LLM-driven Rust port with bit-identical parity:**
- Pixelmelt used an LLM to rewrite the library in **Rust** — "the siren song of making an LLM rewrite the library in rust was too strong"
- This is a great LLM use case because correctness is **extremely verifiable**: two goals — execution speed and parity to the JS implementation. "Getting the rust port 'close' to the JavaScript version fails"
- The port mirrors every float expression in shape and evaluation order; all math goes through wrappers rounding to **7 decimals** like the game's SafeTrig utilities; even the JSON parser had to be correctly rounded ("parity breaks at the first division")
- Test harness: a corpus of **1,961 real maps** from the game with frame-by-frame comparison against the original implementation — came out **1961/1961 bit-identical**

**Training a scratch PPO agent:**
- Trainer is TypeScript on Bun, Rust engine loaded over FFI. TensorFlow.js on GPU was slower than CPU (4k fps vs 41k) because the network is tiny, so PPO was written **from scratch** with cuBLAS matmuls and **31 custom CUDA kernels**
- Eight rollout workers run 512 game instances against each other; a central inference server batches policy evaluations into GPU waves; PPO updates happen on the same GPU between waves
- Input: 385 floats — 14 numbers about its own disc + 19 about the opponent, stacked over 7 frames at offsets (0,1,3,7,15,30,60), decaying traces of its own buttons, 16 raycasts into map geometry, stacked 4 deep
- League training: ~1/3 games vs current self, 1/3 vs a reservoir of past versions, 1/3 vs "exploiters" (policies trained to beat the main agent); every sample mirrored horizontally to double data and force policy symmetry
- Reward: +1 win, −1 loss, −0.3 draw. The bot makes decisions every 2 physics frames (15 Hz)
- Result: current training run passed **10 billion frames** ("at 30 fps that's over ten years of continuous play"); best deployed policy sits **5th out of 522 tracked players** on a live Elo table, behind four very good humans

The project connects Pixelmelt's web-security reverse engineering to both [[concepts/agentic-engineering]] (LLM-verified code porting with bit-exact test harnesses) and reinforcement learning practice — a rare combination of JScrambler RE, LLM-assisted porting, and RL training in one post.

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
