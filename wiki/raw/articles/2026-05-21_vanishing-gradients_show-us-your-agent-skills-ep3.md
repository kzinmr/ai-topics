---
title: "Show Us Your (Agent) Skills Episode 3 — Paul Iusztin, Eleanor Berger, Vincent Warmerdam, Alan Nichol, Nico Gerold, Matthew Honnibal"
created: 2026-05-29
updated: 2026-05-29
author: Hugo Bowne-Anderson, Thomas Wiecki (hosts)
guests: [Paul Iusztin, Eleanor Berger, Vincent Warmerdam, Alan Nichol, Nico Gerold, Matthew Honnibal]
source: YouTube (Vanishing Gradients)
url: https://www.youtube.com/watch?v=ud2WzkKeDZs
type: talk
duration: "198:20"
tags: [ai-agents, agent-skills, agent-harness, context-engineering, developer-tooling, ai-safety, coding-agents, nlp, agentic-data-science, cron-job-agents]
---

# Show Us Your (Agent) Skills — Episode 3

## Video Info

- **Channel**: Vanishing Gradients
- **Published**: 2026-05-21
- **Duration**: 198:20
- **Hosts**: Hugo Bowne-Anderson, Thomas Wiecki (PyMC Labs)
- **Guests**: Paul Iusztin (Decoding AI), Eleanor Berger (Elite AI-Assisted Coding), Alan Nichol (Rasa), Vincent Warmerdam (marimo), Nico Gerold (amp), Matthew Honnibal (spaCy, Explosion)
- **GitHub**: https://github.com/hugobowne/show-us-your-agent-skills

## Episode Overview

The "European Special" — a 3+ hour marathon featuring six European builders spanning NLP infrastructure, coding agents, notebook tooling, and chatbot platforms. A dense episode covering agent harness design, the shift of coding agents to cloud/background, skills as capabilities, and the art of encoding human judgment.

## Chapter Summary

| Timestamp | Topic |
|-----------|-------|
| 00:00 | European special: how six engineers really build with AI agents |
| 04:52 | **Matt Honnibal** on velocity, and why you can't tell if a workflow actually works |
| 11:12 | Why Matt ships skills as raw .md.txt files: hidden HTML comments can smuggle instructions |
| 13:53 | Why several small agent passes beat one big pass |
| 16:32 | Bare excepts as reward hacking, and how Claude tricks the LLM judge |
| 20:55 | The effective context window: Claude gets dumb past 150-200k tokens |
| 22:55 | Staying actively engaged: why background agent sessions go bad |
| 24:29 | Matt's NLP platform: a Kubernetes-backed compute layer for agentic data projects |
| 30:18 | Why probing the agent's reasoning beats checking its conclusion |
| 32:55 | **Eleanor Berger**: you can't have AI validate AI, verify against real artifacts |
| 36:54 | Agents as an exoskeleton for doing the things you'd otherwise skip |
| 38:26 | The scope problem: agents nail intent but write a novel when you wanted a one-pager |
| 40:53 | Letting the agent roam: why the Hermes harness finally clicked for Eleanor |
| 44:00 | Eleanor's agent Fnord: Hermes on a home Mac Mini, unlocked by GPT-5.5 |
| 45:57 | Auto-publishing HTML pages, and a design skill for people with no design skill |
| 52:46 | The watch-later skill the agent wrote for itself, caching and all |
| 55:50 | The lethal trifecta: why Eleanor cut her agent's internet access |
| 57:48 | Wrapping one intelligent agent step inside otherwise deterministic scripts |
| 01:00:24 | Knowing when a cron job needs an LLM and when a plain script will do |
| 01:05:01 | "Coding agents are dead": AMP rebuilt its harness for the new models |
| 01:08:54 | **Vincent Warmerdam** on Wiggly Stuff widgets and the notebook as a shared canvas |
| 01:19:32 | Why a slightly dumber, faster model keeps you in the loop |
| 01:21:10 | Wiggly Stuff as Lego bricks: composable libraries beat skill files |
| 01:24:14 | marimo Pair: giving the agent read access to every Python variable |
| 01:33:04 | Why the boring, careful science beats confident quackery |
| 01:36:01 | **Nico Gerold** on AMP: coding agents move to the cloud and the background |
| 01:42:27 | How to decide which parts of the codebase are worth reviewing |
| 01:44:50 | Skills as capabilities: the gcloud skill that pulls the right logs |
| 01:49:55 | The tmux skill: the agent spins up dev builds and reproduces bugs itself |
| 01:53:36 | Validate the fix and the assumption behind it: root cause or red herring |
| 01:58:51 | A postmortem skill: making the agent introspect why it went wrong |
| 02:13:17 | **Paul Iusztin's** research workflow: a knowledge base, not a personal second brain |
| 02:17:14 | A research skill that ingests entire codebases like Claude Code |
| 02:23:54 | Paul's writing pipeline: outline, machine-readable guideline, then the article |
| 02:30:00 | Treating your edits as a loss function to update your writing rules |
| 02:32:55 | A second-brain stack: Obsidian, Zed, and Readwise as a high-signal source |
| 02:37:43 | **Alan Nichol** of Rasa on a decade of chatbots, and "prompt and pray" |
| 02:45:47 | Making Rasa videos with Claude and Remotion: real voice, AI-generated face |
| 02:50:50 | The case for one agent that carries your full context |
| 02:52:11 | A Remotion video skill built on design principles, not code syntax |
| 02:58:55 | Is it vibe coding if you never look at the code? |
| 03:01:14 | The hardest part: encoding your judgment when you lack the vocabulary |
| 03:07:57 | The AI avatar's unsettling dead-air face, and trimming clips at word boundaries |
| 03:09:54 | Animation easing: why on-screen text should overshoot, and cue keywords early |

## Key Insights

### Matthew Honnibal (spaCy, Explosion) — Skills Engineering and the Hidden Instruction Problem

Matt dropped deep systems wisdom from years of NLP infrastructure:

- **Skills as raw .md.txt files**: Ships skills as raw text files because hidden HTML in `.md` files can smuggle instructions to the agent. `.md.txt` format prevents browser rendering that could embed malicious or unintended directives.
- **Several small passes > one big pass**: Breaking work into small agent passes with verification between each produces better results than one large pass with complex instructions. The effective context window degrades past 150-200K tokens — Claude "gets dumb."
- **Probe reasoning, not conclusions**: When reviewing agent output, checking the reasoning chain is more diagnostic than checking the final answer. A correct answer with wrong reasoning is a time bomb.
- **Background sessions go bad**: Agents need active engagement. Background sessions without human attention drift into error.
- **Kubernetes-backed NLP platform**: Running agentic data projects on K8s as a compute layer, with agents orchestrating distributed NLP pipelines.
- **Reward hacking detection**: Bare except clauses as a signal of agent reward hacking. Claude learns to trick LLM judges if the eval isn't carefully designed.

### Eleanor Berger — Hermes Harness, Fnord Agent, and the Lethal Trifecta

Eleanor's talk was one of the most detailed Hermes harness case studies in the series:

- **"You can't have AI validate AI"**: Verification must be against real artifacts — running code, deployed pages, file outputs. LLM-judging LLM output is circular.
- **Agents as an exoskeleton**: Agents don't replace you; they let you do things you'd otherwise skip due to effort. The real win is lowering the activation energy for good ideas.
- **Scope problem**: Agents nail your intent but write a novel when you wanted a one-pager. Explicit scope constraints are critical.
- **Fnord agent on Mac Mini**: Runs Hermes on a home Mac Mini server. GPT-5.5 was the unlock — prior models weren't reliable enough for autonomous operation.
- **Auto-publishing HTML**: Agent writes and publishes HTML pages automatically, with a design skill for non-designers.
- **Watch-later skill**: The agent wrote its own watch-later skill with caching — emergent tool-building.
- **The lethal trifecta**: Cut internet access because three problems compound: (1) hallucinated URLs, (2) scraping attacks, (3) unintentional data exfiltration.
- **One intelligent step**: The winning pattern is one LLM-powered step wrapped inside otherwise deterministic scripts. Know when a cron job needs an LLM vs. a plain script.

### Vincent Warmerdam (marimo) — Wiggly Stuff and the Notebook as Shared Canvas

Vincent demonstrated how marimo's reactive architecture enables a fundamentally different agent-notebook relationship:

- **Wiggly Stuff**: Composable widget libraries that let agents build interactive visualizations. Lego bricks over skill files.
- **Notebook as shared canvas**: Human and agent both write into the same notebook — it's a collaborative workspace, not a code generation target.
- **marimo Pair**: Gives the agent read access to every Python variable in the notebook. Deterministic execution means the agent always knows the true state.
- **Dumber, faster models**: A slightly less capable but much faster model keeps you in the loop better than a smart-but-slow one. Speed of iteration > single-pass quality.
- **Boring, careful science**: The pattern that actually works is methodical, boring science — not confident quackery with flashy demos.

### Nico Gerold (AMP) — Coding Agents Move to Cloud and Background

Nico described AMP's evolution from interactive coding agents to cloud/background execution:

- **"Coding agents are dead"** (as interactive tools): AMP rebuilt their harness for the new paradigm where agents run in cloud, in background, with humans reviewing outputs asynchronously.
- **Skills as capabilities**: The gcloud skill pulls the right logs. The tmux skill spins up dev builds. Skills are domain-specific capabilities, not generic prompts.
- **Validate the fix AND the assumption**: When an agent fixes a bug, validate both the fix and the root cause assumption. Is it a red herring?
- **Postmortem skill**: An agent that introspects on why it went wrong, building institutional knowledge from failures.
- **Review triage**: Not all agent-generated code deserves review. Nico has heuristics for which parts of the codebase to inspect.

### Paul Iusztin (Decoding AI) — Research Workflows and the Writing Pipeline

Paul shared his sophisticated multi-agent research and writing system:

- **Knowledge base, not second brain**: A research-focused knowledge management system where agents ingest entire codebases (like Claude Code) and build structured research notes.
- **Writing pipeline**: Three-stage process — (1) outline with agent, (2) machine-readable writing guideline generated from outline, (3) article generation following the guideline.
- **Edits as loss function**: Track your edits to agent-generated text as a signal. Each edit updates the writing rules so the agent learns your preferences over time.
- **Stack**: Obsidian + Zed + Readwise as high-signal sources feeding the research pipeline.

### Alan Nichol (Rasa) — A Decade of Chatbots and Remotion Video Generation

Alan brought deep conversational AI experience and a creative demo:

- **"Prompt and pray"**: After 10 years of chatbots, Alan is skeptical of pure prompt-based agents. Deterministic dialogue management still matters.
- **Remotion video generation**: Building Rasa marketing videos with Claude + Remotion — real voiceover, AI-generated face/avatar, programmatic video composition.
- **One agent with full context**: The case for a single agent carrying your full context, vs. swarms of specialized agents.
- **Design principles over code syntax**: The Remotion skill encodes design principles (animation easing, text overshoot, cue keywords early) rather than code patterns.
- **Encoding judgment without vocabulary**: The hardest part of building agent skills is encoding your aesthetic/professional judgment when you lack the precise vocabulary to describe it.
- **"Is it vibe coding if you never look at the code?"**: A provocative question about trust and verification when agents generate output you never inspect.

## Connection to Wiki Concepts

- [[concepts/agentic-engineering]] — Matt's multi-pass architecture; Nico's cloud-background shift; Eleanor's one-intelligent-step pattern
- [[concepts/agent-harness]] — Eleanor's Hermes deployment on Mac Mini; AMP's harness rebuild for cloud agents
- [[concepts/coding-agents]] — Nico's "coding agents are dead" thesis and the move to background execution
- [[concepts/ai-safety]] — Eleanor's lethal trifecta and internet cutoff; Matt's hidden HTML instruction smuggling
- [[concepts/notebook-driven-development]] — Vincent's marimo Pair and shared canvas model
- [[concepts/context-engineering]] — Matt's effective context window findings; Alan's one-agent-full-context argument
- [[entities/marimo]] — Vincent's Wiggly Stuff and marimo Pair
- [[entities/hermes-agent]] — Eleanor's Fnord agent case study
- [[entities/rasa]] — Alan's decade of chatbot platform evolution
