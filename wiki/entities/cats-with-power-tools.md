---
title: "Cats with Power Tools"
created: 2026-04-10
updated: 2026-04-10
tags: [blog, reverse-engineering, obfuscation, javascript, machine-learning, cybersecurity]
aliases: ["cats with power tools", "blog.exploit.cat", "exploit.cat"]
---

# Cats with Power Tools

| | |
|---|---|
| **Blog** | [blog.exploit.cat](https://blog.exploit.cat) |
| **Type** | Collaborative programmer blog |
| **Focus** | JavaScript reverse engineering, obfuscation analysis, machine learning experimentation, web security |

## Core Themes

Cats with Power Tools is a **collaborative programmer blog** focused on deep technical analysis of JavaScript obfuscation, reverse engineering, and security research. The blog's distinctive angle: examining how software systems actively resist being understood, and building tools to pierce that resistance.

### JavaScript Obfuscation & Reverse Engineering

The blog's primary focus is **analyzing and defeating JavaScript obfuscation techniques** used by websites and applications to prevent reverse engineering. This is a series of deep technical investigations:

#### Defeating DevTools Detection (Jul 2025)

Analysis of anti-debugging techniques used by websites to detect when developers have browser DevTools open. The post covers how sites use various fingerprinting methods to identify debugger attachment and how to bypass these detections for security research.

#### Attacking a Stack-Based JavaScript Virtual Machine (Jul 2025, 14 min read)

A comprehensive technical teardown of VM-based JavaScript obfuscation. This is one of the blog's longest and most detailed pieces, covering cryptography, runtime instrumentation, and VM-based obfuscation techniques used to hide code logic.

#### Overview of JavaScript Virtualization Obfuscation (Feb 2025)

Foundational analysis of how JSVM (JavaScript Virtual Machine) obfuscation works — compiling JavaScript to custom bytecode that runs in a virtual machine embedded in the obfuscated code, making static analysis extremely difficult.

#### Try-Catch Control Flow Obfuscation (Mar 2025)

How exception handling — a fundamental JavaScript language feature — can be exploited to create non-linear code flow that confuses static analysis tools. The technique uses `try-catch` blocks not for error handling but as a control flow mechanism.

#### Branch Encryption (Mar 2024)

Analysis of how code branches can be encrypted so that only the currently executing path is decrypted, making it impossible to see the full program logic through static analysis alone.

#### Pixelmelt's JavaScript Virtualisation Obfuscation

A research study analyzing a specific obfuscation product's implementation — real-world reverse engineering of commercial obfuscation tools.

#### Amazon Kindle Web Obfuscation (Oct 2025)

"How I Reversed Amazon's Kindle Web Obfuscation Because Their App Sucked" — a practical case study driven by frustration with the Kindle web app. Covers digital rights management (DRM), font rendering, perceptual hashing, and reverse engineering techniques.

### The Philosophy of Obfuscation

A recurring theme: **obfuscation is an arms race**. Each technique has countermeasures, and each countermeasure drives new techniques. The blog documents this cycle from both sides — as someone who understands why obfuscators exist (protecting intellectual property, preventing scraping, DRM) and someone who exists to break them (understanding how systems actually work).

### Machine Learning Experiments

#### Building The Language Model Nobody Asked For (Aug 2025)

An experimental post about fine-tuning a custom language model. The self-deprecating title reveals the blog's approach: building things because they're interesting and technically challenging, not because there's market demand.

#### Cloning Your Discord Friends with Large Language Models (Jan 2024)

Fine-tuning LLMs on Discord conversation data to mimic specific individuals' writing styles. Combines deep learning, GPU computing, and natural language processing — and notably, the follow-up post *"Did it work well and is it useful in any way? No. Is it hilarious to mess around with and does it mimic them well? Yes."* reveals the blog's honest, self-aware tone.

### Technical Expertise

The blog demonstrates deep expertise across:
- **JavaScript engine internals** (V8, SpiderMonkey behavior)
- **Bytecode decompilation and disassembly** (recursive vs. linear approaches to JSVM disassembly)
- **Cryptography** (branch encryption, code virtualization)
- **Web scraping defenses** ("A Clever but not so good Scraper Protection" — June 2025)
- **Font rendering** (used in both Kindle DRM and scraper protection analysis)
- **Runtime instrumentation** (dynamic analysis of obfuscated code)

## Notable Articles

| Date | Title | Topics |
|---|---|---|
| Oct 2025 | How I Reversed Amazon's Kindle Web Obfuscation Because Their App Sucked | DRM, Font Rendering, Perceptual Hashing, Reverse Engineering |
| Aug 2025 | Building The Language Model Nobody Asked For | Fine Tuning, ML, NLP |
| Jul 2025 | Defeating DevTools Detection | Anti Debugging, Browser Fingerprinting, Web Security |
| Jul 2025 | Attacking a Stack Based JavaScript Virtual Machine | Cryptography, JS Obfuscation, Reverse Engineering, Runtime Instrumentation |
| Jul 2025 | Recursive vs Linear JSVM Disassembly | Disassembly, Reverse Engineering |
| Jun 2025 | A Clever (but not so good) Scraper Protection | Font Rendering, Web Scraping, Web Security |
| Mar 2025 | Try-Catch Control Flow Obfuscation | Exception Handling, Program Analysis, Software Obfuscation |
| Feb 2025 | Overview of JavaScript Virtualization Obfuscation | JavaScript, VM-based Obfuscation |
| Dec 2024 | JavaScript Obfuscation Tricks | Code Obfuscation, JavaScript |
| Mar 2024 | Branch Encryption | Code Obfuscation, Cryptography |
| Jan 2024 | Cloning Your Discord Friends with LLMs | Deep Learning, GPU Computing, ML, NLP |

## Related

- [[concepts/javascript-obfuscation]] — Techniques covered extensively on this blog
- [[concepts/reverse-engineering]] — Primary methodology
- [[concepts/web-security]] — Security research focus area

## Sources

- [blog.exploit.cat](https://blog.exploit.cat)
- [engineered.at/sources/cats-with-power-tools](https://engineered.at/sources/cats-with-power-tools)
