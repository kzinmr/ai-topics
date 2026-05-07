---
title: "The End of Programming as We Know It"
author: Tim O'Reilly
publication: O'Reilly Radar
date: 2025-02-04
url: https://www.oreilly.com/radar/the-end-of-programming-as-we-know-it/
tags:
  - vibe-coding
  - AI-agents
  - programming
  - CHOP
  - software-engineering
  - agent-infrastructure
type: article
---

# The End of Programming as We Know It

**Author:** Tim O'Reilly | **Date:** February 4, 2025 | **Topic:** AI & ML

## Executive Summary
Tim O'Reilly argues that while AI is fundamentally transforming software development, it is not the end of the profession. Instead, we are witnessing a historical shift similar to the transitions from machine code to assembly, or from low-level drivers to high-level operating systems. The "end of programming" is actually the birth of a new paradigm where human programmers act as managers of digital co-workers and architects of complex systems.

---

## 1. Historical Context: The Evolution of Abstraction
Programming has always moved toward higher levels of abstraction. Each wave was initially feared as the "end" of the craft but resulted in more programmers and higher demand.
- **Early Era:** Physical circuits → Binary switches → Assembly language.
- **High-Level Era:** Fortran, COBOL, C, and Java replaced assembly for most tasks.
- **The OS Revolution:** Windows and macOS encapsulated low-level hardware drivers into "bags of drivers" (APIs), allowing developers to focus on applications rather than hardware.
- **The Web & Cloud:** Python, JavaScript, and APIs (Stripe, Google Maps) further abstracted complexity, creating a massive "internet operating system."

> "The human programmers are their managers. There are now hundreds of thousands of programmers doing this kind of supervisory work. They are already living in a world where the job is creating and managing digital co-workers." — **Tim O'Reilly**

---

## 2. The "CHOP" Paradigm: Chat-Oriented Programming
The current shift involves **Chat-Oriented Programming (CHOP)** , where natural language prompts generate executable code. 

### Key Insights on the New Workforce:
- **The Death of the Stubborn Developer:** Steve Yegge notes that AI won't replace junior developers, but rather those who refuse to adopt new tools. Junior developers mastering AI can now outperform senior developers who don't.
- **Learning by Doing:** Economic historian James Bessen's research shows that productivity gains from new technology take decades to realize because workers must "learn by doing"—inventing new workflows and repairing the new "machines."
- **The Jevons Paradox:** As programming becomes more efficient (cheaper), the demand for it will skyrocket rather than diminish.

---

## 3. The Emerging AI Tech Stack
The transition to AI mirrors the shift from desktop to internet. Sam Schillace (Deputy CTO, Microsoft) notes that while the layers remain, the components are changing:
- **Languages:** Compiled → Interpreted → LLM-driven.
- **Teams:** Waterfall → Agile → AI-integrated.
- **Databases:** ACID → NoSQL → Vector/Context-driven.

### The "70% Problem"
Addy Osmani (Google Chrome) highlights a critical limitation: AI can handle the first 70% of a project (scaffolding, documentation), but the final 30% requires "hard-won engineering wisdom" to prevent "house of cards code" that collapses under real-world pressure.

---

## 4. New Roles and Future Challenges
As AI matures, new specialized roles and infrastructure requirements are emerging:

- **The Agent Engineer:** A role (similar to a React developer) focused on encoding business policies and processes into AI agents.
- **Metacognition & Control:** Current AI is in the "steam engine" phase. Future systems will need "metacognitive" layers to manage memory and complex reasoning.
- **Agent Infrastructure:** There is a massive, unaddressed need for protocols (like HTTPS for agents) to handle:
  1. Attributing actions to specific agents/users.
  2. Shaping agent-to-agent interactions.
  3. Detecting and remedying harmful actions.

> "Computer science is about systematic thinking, not writing code." — **Mehran Sahami, Stanford CS Chair**

---

## 5. Actionable Takeaways for Businesses
- **Invest in Quality, Not Just Speed:** Don't just use AI to cut costs. Use the 10x productivity gain to build higher-resolution, more complex, and more reliable services (the "Pixar vs. Marvel" analogy).
- **Empower the "Jagged Edge":** Encourage employees to use AI for every task to find where it succeeds and where it fails.
- **Focus on Workflow:** Automation is limited by edge cases. The winning companies will be those that build toolchains to capture feedback and handle the "last mile" of production.
