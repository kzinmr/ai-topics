---
title: "Using AI to Write Better Code More Slowly"
source_url: "https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/"
source_domain: "nolanlawson.com"
author: "Nolan Lawson"
date_published: "2026-05-25"
date_ingested: "2026-05-26"
type: blog_article
tags:
  - coding-agents
  - code-review
  - ai-agents
  - software-engineering
  - claude-code
  - methodology
---

# Using AI to Write Better Code More Slowly

**Source:** [Read the Tea Leaves](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) by Nolan Lawson, May 25, 2026

---

## Core Thesis

Most people view AI coding as a tool for **spewing low-quality code fast** ("slop cannons"). But LLMs are flexible enough to support the opposite: **writing high-quality code slowly**, by systematically finding and fixing bugs. This post argues for that slower, more methodical approach as a super-powered evolution of quality-obsessed programming.

> "You can use them just as effectively to write high-quality code more slowly."

---

## The Bug-Finding Superpower

- **LLMs excel at finding bugs**—Mythos proved that, and latest public models (Anthropic, OpenAI) are capable of uncovering many issues in an unscrutinized codebase.
- The real challenge: **prioritizing and validating** those findings, not the discovery itself.
- To combat hallucinations and false positives, **throw multiple models at the same PR** and cross-check results. This dramatically reduces false positives.

### The Multi-Agent Review Skill

Nolan adapted a Claude skill that orchestrates three bug-finding agents in parallel:

> *"Run a Claude sub-agent, Codex, and Cursor Bugbot to find bugs in this PR ranked by critical/high/medium/low. Once they're all done, review their findings, do your own research to rule out false positives, and write a final report."*

- The skill includes custom definitions of "bug"—e.g., KISS/DRY violations, inaccessible HTML/JSX, missing SQL indexes.
- **False positive rate: near zero.**
- Finds so many bugs that tackling all of them becomes tedious. They range from critical security/correctness flaws to low-level "misleading comment" issues.

> "The problem is not so much finding the bugs, but instead prioritizing and validating them."

---

## The Slow Workflow

1. **Triage:** Have an agent fix **all criticals and highs** (with developer guidance on the proper solution). Repeat until none remain.
2. **Pare down:** Skip high/medium issues where the fix effort outweighs the benefit (e.g., 100 lines of code for a narrow edge case).
3. **Abort if necessary:** If the PR accumulates so many criticals that the entire approach is flawed, **abandon it**.

This process often uncovers **pre-existing bugs** outside the PR, leading to tangential side-quests (unit tests, subtle fixes). That's the **opposite of 10× productivity**—but it improves codebase health and deepens understanding of failure modes.

> "I haven't necessarily seen my velocity go up. … I end up on a tangential side-quest where I'm writing unit tests and fixing subtle flaws that pre-date the PR."

---

## Advice for Developers

- Don't just accept AI-generated code blindly. **Use agents to understand the PR:** ask how it works, how it might fail, generate Markdown docs with Mermaid charts, or use **Matt Pocock's `/grill-me` skill** until you fully grasp the changes.
- This slower style is a **more powerful version of the careful, methodical, quality-obsessed programming** practiced before LLMs.
- It may burn a lot of tokens and not increase raw lines of code, but it catches wrongheaded approaches early and makes codebases better for the next developer.

> "Take a deep breath, slow down, try this technique, and see if you don't enjoy writing better code more slowly."

---

## Notable Comments & Author Replies

- **heckj:** Applying the same multi-sweep technique to editorial review works well. **Clearing context between sweeps** helps; also running **5–7 different lenses** in parallel, then collating results.
  - *Nolan Lawson:* Clearing context is key—his skill forces the main agent to wait for all sub-agents before doing its own research, preventing early bias. Splitting reviewers by archetype might help for multi-domain PRs.
- **Spencer Karenbauer:** Vibe coding often leads non-coders to blindly trust AI outputs. Enablement and governance are needed.
  - *Nolan Lawson:* LLM output is just a **first draft**. The real work starts with code review. Proper scaffolding/documentation makes this process far more effective.

---

## Key Takeaway

LLMs aren't just for rapid, low-quality output. By **slowing down, running multiple bug-finding agents in parallel, and thoroughly reviewing results**, you can catch subtle issues, learn your codebase better, and produce **higher-quality software**—making AI a force for craftsmanship, not just speed.
