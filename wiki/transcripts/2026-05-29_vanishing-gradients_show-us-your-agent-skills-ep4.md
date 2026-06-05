---
title: "Show Us Your (Agent) Skills Episode 4 — Hamel Husain, Chris Fonnesbeck, Doug Turnbull, John Berryman"
created: 2026-05-29
updated: 2026-06-05
author: Hugo Bowne-Anderson, Thomas Wiecki (hosts)
guests: [Hamel Husain, Chris Fonnesbeck, Doug Turnbull, John Berryman]
source: YouTube (Vanishing Gradients)
url: https://www.youtube.com/live/XaYQFtca798
type: talk
duration: "122:30"
tags: [ai-agents, agent-skills, agent-harness, ai-safety, code-review, context-engineering, developer-tooling, coding-agents, search, evaluation]
---

# Show Us Your (Agent) Skills — Episode 4

## Video Info

- **Channel**: Vanishing Gradients
- **Published**: 2026-05-29
- **Duration**: 122:30
- **Hosts**: Hugo Bowne-Anderson, Thomas Wiecki (PyMC Labs)
- **Guests**: Hamel Husain (Parlance Labs), Chris Fonnesbeck (PyMC Labs, veteran analyst for Phillies/Yankees/Brewers), Doug Turnbull (led Search at Shopify and Reddit), John Berryman (interlocutor, Arcturus Labs)
- **GitHub**: https://github.com/hugobowne/show-us-your-agent-skills
- **Full transcript**: `transcripts/2026-05-29_vanishing-gradients_show-us-your-agent-skills-ep4.en.vtt`

## Episode Overview

The Season 1 finale. Three main guests plus John Berryman as interlocutor, spanning agent skill ecosystems, Bayesian statistics, and search. The episode covers skills skepticism, the Codex Desktop transition, Socratic code review, auto-research agents for search ranking, and lab journals as agent memory.

## Chapter Summary

| Timestamp | Topic |
|-----------|-------|
| 00:00 | Season 1 Finale: Welcome to Show Us Your Skills |
| 03:24 | **Welcome Hamel Husain**: Bringing Data Science Back to AI |
| 06:26 | Why AI Writing Is Slop Unless You're Fully In the Loop |
| 08:47 | Why Hamel Switched From Claude Code to Codex Desktop |
| 13:11 | Giving Up on Open Claw and Trusting the Vendor Harness |
| 17:06 | Devin's UX Comeback: Proof of Work You Can Actually Eval |
| 19:17 | Always Read the Prompt (Skills Are Just Decompressed Prompts) |
| 22:33 | Fuck Your Skills: Be Skeptical, Even of Hamel's |
| 24:41 | Why Hamel Killed His Own Eval Skill for an MCP |
| 29:35 | A Third of the Top 300 Skills Have One Commit |
| 32:59 | The Skills Security Nightmare and Invisible HTML |
| 37:56 | Maybe Agents Just Need More Blog Posts |
| 42:37 | Hamel's Favorite Skill: Reverse-Engineering Sites Without APIs |
| 48:35 | **Welcome Chris Fonnesbeck**: From the Yankees to PyMC 6 |
| 51:25 | Why Agents Are Seductive (and Dangerous) |
| 55:29 | Switching to Pi: A TUI That Rewrites Its Own Source |
| 1:00:36 | Socratic Review: Pi's Grill-Me Skill |
| 1:02:08 | Zed as Agent Multiplexer, Half-Flat Distributions Live |
| 1:08:27 | Why Chris Left VS Code for Zed (Marimo, Vim, Rust) |
| 1:17:42 | **Welcome Doug Turnbull**, Still Lost in the Search Labyrinth |
| 1:22:28 | Auto-Research: Can an Agent Find a Better BM25? |
| 1:25:55 | BM25 as the Hundred-Dollar Bill on the Floor |
| 1:33:16 | Patching Ranking Code Against an MS Marco Eval |
| 1:37:46 | Train/Validate Splits Stop Agents Overfitting the Ranker |
| 1:41:55 | What the Agent Discovered: Stop Words and Bigrams |
| 1:49:02 | Lab Journals, Episodic Memory, and Why Grep Isn't Enough |
| 1:55:31 | An LLM Judge as User Message Beats Its Own Reasoning |
| 2:00:28 | Next Up: John Berryman's Agent That Follows You Everywhere |

## Key Insights (Verified from Transcript)

### Hamel Husain (Parlance Labs) — Skills Skepticism and Codex Desktop

> *"I never thought I would leave the terminal. And then I tried Codex Desktop app, and I was like, 'Wow, this is actually better.' It shocked me."* — [08:35]

- **Codex Desktop over Claude Code**: Hamel switched from Claude Code to Codex Desktop for its polished UI, native computer use on Mac, headless Mac Mini sessions visible in the sidebar, and excellent phone support. "I never thought I would say that."
- **Skills are decompressed prompts**: Skills don't add magic — they're structured context that the agent decompresses at runtime. "Always read the prompt."
- **"Fuck Your Skills"**: Radical skepticism toward skills. A third of the top 300 skills on GitHub have exactly one commit — most are abandonware. Be skeptical even of Hamel's own published skills.
- **Killed his eval skill for an MCP**: MCP provides a more structured, testable interface than skill files for evaluation tasks.
- **Skills security nightmare**: Hidden HTML in `.md` skill files can inject instructions. The skill supply chain is a massive unexamined attack surface.
- **Reverse-engineering sites without APIs**: Hamel's favorite skill — the agent inspects network traffic, reverse-engineers internal APIs, and builds clients for sites with no public API.
- **AI writing is slop**: Unless you're fully in the loop — reading, editing, verifying — AI-generated writing is inevitably mediocre. The human has to be an active editor, not a passive approver.

### Chris Fonnesbeck (PyMC Labs) — Bayesian Skepticism, Pi TUI, and Socratic Review

- **Agents are seductive and dangerous**: The ease of getting an answer from an agent masks the difficulty of verifying it. Statistical thinking — quantifying uncertainty, checking assumptions — is more critical with agents, not less.
- **Switched to Pi**: A TUI agent that can rewrite its own source code. The self-modifying capability changes the trust model.
- **Socratic review — Pi's Grill-Me skill**: Instead of just reviewing code, the agent Socratic-dialogues the author — asking probing questions that expose weak assumptions. This mirrors Chris's Bayesian approach: prior elicitation through questioning.
- **Zed as agent multiplexer**: Uses Zed editor as the coordination point for multiple agents, with marimo notebooks, vim keybindings, and Rust tooling all integrated.
- **Left VS Code for Zed**: The shift was driven by the agent workflow — Zed's speed and multi-agent support matter more than VS Code's extension ecosystem.

### Doug Turnbull (Search at Shopify/Reddit) — Auto-Research and Agentic Search

- **Auto-research: Can an agent find a better BM25?**: Doug tasked an agent with discovering ranking improvements. Not just implementing known techniques — actually researching and testing novel approaches.
- **BM25 as the hundred-dollar bill on the floor**: BM25 is so effective that it's the baseline no one can beat. The agent's job is to find improvements on top of it, not replace it.
- **MS Marco eval loop**: The agent patches ranking code, evaluates against MS Marco, and iterates. Train/validate splits prevent the agent from overfitting the ranker to the eval set.
- **What the agent discovered**: Stop words and bigrams — classical IR techniques that the agent independently rediscovered as optimizations.
- **Lab journals and episodic memory**: The missing piece in agent workflows. Grep isn't enough — agents need structured, queryable memory of what they tried, what worked, and why. Like a scientist's lab notebook.
- **LLM judge as user message**: Framing the LLM judge's evaluation as a "user message" (rather than asking the agent to reason about its own output) produces better, less biased self-assessment.

## Connection to Wiki Concepts

- [[concepts/agentic-engineering]] — Hamel's skills ecosystem critique; Doug's auto-research workflow
- [[concepts/ai-safety]] — Hamel's skills security nightmare and invisible HTML problem
- [[concepts/context-engineering]] — Hamel's "skills are decompressed prompts" framing
- [[concepts/generator-evaluator-pattern]] — Doug's auto-research eval loop; LLM judge as user message
- [[concepts/personal-software]] — Chris's Pi TUI; Hamel's reverse-engineering skill

## Links

- [GitHub: show-us-your-agent-skills](https://github.com/hugobowne/show-us-your-agent-skills)
- [Vanishing Gradients Substack](https://hugobowne.substack.com/)
