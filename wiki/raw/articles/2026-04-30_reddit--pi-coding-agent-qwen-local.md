---
title: "Been using pi_coding_agent with local Qwen3.6 35B"
source: "https://www.reddit.com/r/LocalLLaMA/comments/1stjwg5/"
date: 2026-04-30
type: reddit_post
---
# Summary: Optimizing PI Coding Agent with Local Qwen 2.5 32B/35B

This report summarizes a highly effective workflow for using the **PI Coding Agent** with local Large Language Models (LLMs), specifically the **Qwen 2.5 32B (35B a3b)** model. The user reports "insane" performance on production-level projects by implementing a custom "Plan-First" skill file.

## 1. Core Setup & Performance
*   **Agent:** PI Coding Agent
*   **Model:** Qwen 2.5 32B (specifically the `a3b q4_k_xl` quantization).
*   **Key Insight:** Local models have reached a level of maturity where they can handle production coding tasks reliably when guided by a strict, structured workflow.
*   **The "Game Changer":** A custom **skill file** that enforces a "plan-first" methodology, preventing the model from "going off the rails" or writing code prematurely.

---

## 2. The "Plan-First" Skill File
The author shared a specific configuration file designed to force the agent into a disciplined, multi-phase execution loop.

### Skill File Definition
```yaml
---
name: plan-first
description: Structured planning workflow for any coding task. Use at the start of every new feature, bug fix, refactor, or implementation request. Analyzes the project, asks up to 5 clarifying questions, creates a TODO.md, gets user approval, then executes task by task. Never writes code before a plan is approved.
---
```

### The Five-Phase Workflow
The skill file enforces the following strict rules:

1.  **Phase 1 — Analyze the Project:** The agent must silently read the directory structure, dependency files (e.g., `package.json`, `requirements.txt`), build systems, and existing documentation before outputting anything.
2.  **Phase 2 — Clarifying Questions:**
    *   **Limit:** Maximum of 5 questions in a single message.
    *   **Constraint:** Only ask what cannot be inferred from the codebase.
    *   **Wait:** The agent must wait for user response before proceeding.
3.  **Phase 3 — Create `TODO.md`:** The agent generates a structured task list in the project root.
    *   **Structure:** Must include a Goal, Tasks (small and verifiable), and Notes.
    *   **Approval:** The agent must ask: *"I've created TODO.md. Does this plan look correct? Reply YES to start."*
4.  **Phase 4 — Revision Loop:** If the user disagrees, the agent updates the `TODO.md` and seeks approval again.
5.  **Phase 5 — Execution:**
    *   Tasks are completed **one at a time**.
    *   The agent marks tasks as done (`[x]`) in the `TODO.md`.
    *   **Discovery Rule:** If a new task is discovered, the agent must stop, add it to a `## Discovered Tasks` section, and get approval before continuing.

---

## 3. Key Rules for Local Agent Success
The success of this workflow relies on these "Golden Rules" embedded in the skill file:
*   **No Premature Coding:** "NEVER write code, create files, or run commands before a TODO.md is approved."
*   **No Assumptions:** "NEVER assume missing information. Ask instead."
*   **Strict Sequence:** "NEVER skip steps. Follow phases in order."
*   **Scope Control:** "NEVER go off-plan. If new work is discovered... ask for approval before doing it."

## 4. Conclusion
By using a local **Qwen 2.5 32B** model paired with a **structured planning skill**, developers can achieve production-grade results that rival or exceed unconstrained cloud-based models. The primary benefit is the reduction of "hallucinated" code and the elimination of the agent performing unrequested or destructive changes.
