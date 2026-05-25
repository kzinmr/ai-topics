---
title: "After Automation — AI progress creates more work for humans, not less"
source: https://every.to/p/after-automation
author: Dan Shipper, CEO of Every
published: 2026-05-21
saved: 2026-05-25
type: raw-article
---

# After Automation
**Author:** Dan Shipper, CEO of Every
**Published:** May 21, 2026
**Source:** [every.to/p/after-automation](https://every.to/p/after-automation)

---

## Core Paradox
AI commoditizes the residue of human expertise (what can be made explicit and trained on). This collapses the value of default model output, creates demand for what's different—and that difference requires human experts, even as we approach AGI.

> "There's no tipping point coming where things flip and the jobs are gone. The new reality is the opposite—the more we automate, the more expert human work there is to do."

## How AI Is Used at Every (Two Modes)

### 1. Agent Employees (Async Delegation)
Agents given jobs that produce output without human in the loop. All require human maintenance and oversight.

**Coworker agents** (Slack-taggable):
- **Claudie** (consulting): writes sales proposals, drafts training decks, tracks project todos.
- **Andy** (editorial): collects "nuggets" from internal Slack, creates story digests for daily newsletter.
- **Viktor** (general): gathers growth metrics, analyzes surveys, turns discussions into research memos.

**Embedded agents** (inside product workflows):
- **Fin** (customer service platform): participated in 65% of 202 support conversations, closed 40.1% of all actionable conversations without humans.

**Why personal agents failed:** agents need constant maintenance; when abandoned by employees, they go stale. A dedicated team of AI engineers now centrally manages agents. Even a PowerPoint automation requires 24 skills, 18 scripts, $62 in tokens per deck.

### 2. Human-Agent Collaboration (Synchronous, Shared Workspace)
For complex work, the best results come from human and AI going back and forth in the same tool (Codex, Claude Code, Cowork).

**The Human Sandwich (Kieran's concept):** Humans are "the bread on either end of the AI's work"—humans point at the right things, AI does the work, humans review/correct/decide.

**Tools:** Codex, Claude Code, Cowork
- **Coding:** Engineers spend all day going back-and-forth with agents
- **Writing:** Compose in Proof inside Codex; agents draft paragraphs, research examples, copy edit
- **Email:** Run Cora inside Codex browser; talk through inbox with Monologue

## Why Automation Creates MORE Human Work

A 5-step feedback loop:
1. **AI makes yesterday's human competence cheap** — LLMs trained on "the visible residue of human competence" (code, prose, images, tickets, specs)
2. **Cheap competence gets rapidly adopted** — OpenClaw: 44,469 pull requests by May 2026 (12,430 since April 1); Kubernetes: 5,200 PRs in all of 2022
3. **Abundance creates sameness → commoditization** — Slop is "visible sameness, repeated ad nauseam. It is what gets produced by default when humans in many different circumstances use the same tool, trained on the same corpus, without thinking too hard."
4. **Sameness creates demand for difference** — Work that doesn't fit the pattern becomes rare, valuable, high-status
5. **Demand for difference = demand for human experts** — "Once a situation has been reduced to text, once it has become corpus, it is a corpse."

**Two directions for human experts:**
- Build systems to manage flood of new work (review queues, evals, CI, workflows)
- Do bigger, more interesting work (e.g., Calif security firm found first public macOS kernel memory exploit on Apple M5 in 5 days using Mythos Preview)

## The Benchmark Trap ("Chart Psychosis")

### Senior Engineer Benchmark Case Study
Task: Rewrite a "vibe coded slop" codebase from first principles.
- GPT-5.5 scored 62/100; senior engineers (using AI) score high 80s-low 90s
- The prompt is deliberately generic but IS a frame—it sets what matters
- Changing the prompt (e.g., from "structural rewrite" to "fix errors one by one") collapses score to near zero
- As models saturate a frame, we shift the frame → model climbs, we freak out, demand for experts rises → cycle repeats

### GDPval Smuggles Intelligence
Benchmark tasks are heavily pre-framed with human expertise. The auditor task prompt includes specific thresholds, entity lists, risk weightings—a frame set by human experts.

## Zeno's Paradox of AI
> "What we're watching... is a model getting better at a particular framing of the problem—framing WE chose."

Each benchmark is a frame. AI keeps closing the gap, but each time we shift the frame. The model never "arrives"—it just keeps chasing.

## But What About AGI?
Even with AGI-level models, the same dynamics apply: commoditization of known expertise → demand for what's different → demand for humans who can define frames.

## Agents Without Agency
> "Benchmark performance is not agentic performance in the real world."

Key insight: **benchmark tasks are set by humans**—they encode human judgment about what matters. Agents perform tasks that have already been framed by humans. Building an AI that can decide what matters is a different challenge entirely.

## Coda
The concept of "agents without agency" points to the next frontier: not just better benchmark scores, but AI that can frame problems, decide what's important, and act with genuine intention.
