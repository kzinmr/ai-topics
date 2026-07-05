---
title: AI Agent Video Editing
created: 2026-06-01
updated: 2026-06-01
type: concept
tags:
  - concept
  - ai-agents
  - coding-agents
  - tool
  - multimodal
sources:
  - raw/articles/arcturus-labs.com--blog-2026-05-31-my-ai-skill-edited-this-video-that-explains---3372213b.md
---

# AI Agent Video Editing

## Overview

AI agent video editing refers to the use of [AI coding agents](agentic-coding.md) to build automated video editing pipelines. The meta pattern involves an agent watching a tutorial video, understanding the process through its transcript, and then implementing the described pipeline locally — then packaging everything as an agent skill.

## Meta-Pattern: Agent Teaches Itself from Video

The canonical workflow (demonstrated by Arcturus Labs, May 2026):

1. **Agent watches a tutorial** — The Cursor agent downloads a YouTube video transcript via `yt-dlp`
2. **Agent analyzes and replicates** — The agent reads the transcript, sets up a repository, and implements the video editing pipeline described in the tutorial
3. **Agent packages as a skill** — Everything is wrapped into an agent skill using the `create-skill` skill
4. **Agent learns from failure** — When the initial result clips words at cut points, the agent diagnoses the issue and fixes it autonomously in subsequent iterations
5. **Self-referential loop** — The walkthrough video explaining how the tool was built is itself edited by the tool

## Key Components

### yt-dlp
Command-line tool for downloading YouTube videos and their transcripts. Essential for the agent to access video content programmatically.

### AssemblyAI
Speech-to-text service with word-level timestamps (including disfluencies like "um", "uh"). Precise timing information is what enables automated cutting and editing. Free tier: ~185 hours of pre-recorded transcription.

### Cursor Agent Workflow
The agent is instructed via a meta-prompt: "Watch this video, figure out how to make the same thing, build it, and package it as a skill." The agent handles research, implementation, and packaging autonomously.

## Quality Iterations

The Arcturus Labs demonstration involved three iterations:

| Iteration | Outcome |
|:----------|:--------|
| **1** | Tool works but clips end of words at cut points — not usable |
| **2** | Agent diagnoses clipping, proposes fixes, implements autonomously — "pretty impressive for ~5 minutes total investment" |
| **3** | Final walkthrough video edited entirely by the tool it describes — self-referential quality verification |

## Relationship to Other Concepts

- [[concepts/coding-agents/agentic-coding]] — The parent paradigm of AI agents writing code
- [[concepts/agent-skills]] — Skills as a packaging format for reusable agent workflows
- [[concepts/ai-agent-engineering]] — Engineering principles for building agent-based systems
- [[concepts/harness-engineering/agent-harness]] — The harness layer that enables agent tool use and execution

## Related Entities

- [[entities/cursor]] — The harness used for the agent workflow
- [[entities/assembly-ai]] — The speech-to-text service powering the editing pipeline
