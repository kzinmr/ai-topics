---
title: "Anthropic: How we built our multi-agent research system"
source: Simon Willison's Weblog
url: https://simonwillison.net/2025/Jun/14/multi-agent-research-system/
date_published: 2025-06-14
type: raw_article
tags:
  - multi-agent
  - ai-agents
  - anthropic
  - agent-architecture
  - prompt-engineering
  - simon-willison
  - claude-research
---

# Anthropic's Multi-Agent Research System – Simon Willison's Annotation

**Simon Willison's take:** Initially skeptical about multi-agent LLM systems, he is now convinced after reading Anthropic's detailed account of building Claude Research.
The post distills the original article into actionable insights, key numbers, and real-world engineering lessons.

---

## 1. What is a Multi-Agent System?

**Anthropic's definition (exact quote):**
> A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together. Our Research feature involves an agent that plans a research process based on user queries, and then uses tools to create parallel agents that search for information simultaneously.

- The **lead agent** decomposes the query, then spawns **subagents** that operate in their own context windows.
- Each subagent uses tools (search, etc.) in a loop and returns a condensed result.

---

## 2. Why Use Multiple Agents? The Core Benefit

**Key rationale:**
> The essence of search is compression: distilling insights from a vast corpus. Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent.

This solves the **single context window limit** (200k tokens). Each sub‑task gets its own full context, enabling processing of far more information than a single agent could handle.

**Performance data:**
- **Multi‑agent (Opus 4 lead + Sonnet 4 subagents) outperformed single‑agent Opus 4 by 90.2%** on Anthropic's internal research eval.
- *Example:* "Identify all the board members of the companies in the Information Technology S&P 500."
  - Single agent failed with slow, sequential searches.
  - Multi‑agent decomposed the task into parallel subagent searches and found the correct answer.

---

## 3. Cost and Token Usage

**Massive token burn:**
> In our data, agents typically use about **4× more tokens** than chat interactions, and multi-agent systems use about **15× more tokens** than chats.

- Economic viability requires high‑value tasks.
- Multi‑agent systems excel where:
  - Heavy parallelization is possible
  - Information exceeds a single context window
  - Many complex tools must be coordinated

---

## 4. Key Architectural Details

### Memory Mechanism
The lead agent (LeadResearcher) **saves its plan to Memory** to survive context window truncation:
> The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated and it is important to retain the plan.

### Parallelism for Speed
> For speed, we introduced two kinds of parallelization:
> 1. The lead agent spins up **3–5 subagents in parallel** rather than serially.
> 2. The subagents use **3+ tools in parallel**.

- **Result: up to 90% reduction in research time** for complex queries.
- Enables covering more information in minutes instead of hours.

---

## 5. Prompt Engineering Was the Primary Lever

**Initial failures:**
> Early agents made errors like spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources, and distracting each other with excessive updates.

**Solution:** carefully sculpted prompts for every agent.
- Each subagent gets:
  - A clear **objective**
  - An **output format**
  - **Tool and source guidance**
  - **Task boundaries**

**Tool‑Testing Agent (meta‑agent for ergonomics):**
- Given a flawed MCP tool, it uses it repeatedly and **rewrites the tool description** to avoid failures.
- After dozens of tests, it found key nuances and bugs.
- **Result: 40% decrease in task completion time** for future agents using the improved description.

---

## 6. Evaluation Strategy

Anthropic used a combination of automated and human evals.

**LLM‑as‑a‑judge** worked well, but **human evaluation caught a critical flaw:**
> Human testers noticed that our early agents consistently chose SEO‑optimized content farms over authoritative but less highly‑ranked sources like academic PDFs or personal blogs.

**Fix:** Added source quality heuristics to prompts.

**Actionable testing advice:**
> It's best to start with small‑scale testing right away with a few examples, rather than delaying until you can build more thorough evals.

---

## 7. Example Prompt Snippets (from Anthropic's Open‑Source Cookbook)

### Encouraging Parallel Tool Calls
```
For maximum efficiency, whenever you need to perform multiple independent operations,
invoke all relevant tools simultaneously rather than sequentially. Call tools in parallel
to run subagents at the same time. You MUST use parallel tool calls for creating multiple
subagents (typically running 3 subagents at the same time) at the start of the research,
unless it is a straightforward query. For all other queries, do any necessary quick
initial planning or investigation yourself, then run multiple subagents in parallel.
```

### OODA Research Loop (subagent prompt)
The subagent prompt implements an **OODA loop** (Observe, Orient, Decide, Act) approach to research — a military strategy framework repurposed for iterative search.

---

## Simon Willison's Key Takeaways

1. **"Multi-agent systems work mainly because they help spend enough tokens to solve the problem"** — token usage explains 80% of performance variance.
2. **Compression via parallelization** is the core insight: subagents each explore independently, then compress results for the lead agent.
3. **Prompt engineering is the primary lever**, not model size or tool quality.
4. **The tool‑testing meta‑agent** (40% improvement) is a novel meta‑learning pattern worth studying.
5. **Human evaluation caught critical biases** that automated evals missed.
6. **Cost is the trade‑off**: 15× more tokens than chat, so multi‑agent only makes sense for high‑value tasks.
