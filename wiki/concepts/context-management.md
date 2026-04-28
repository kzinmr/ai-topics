---
title: "Context Management"
type: concept
tags: [context-management, llm, context-window, agent-memory]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Context Management, Context Window Management, Agent Context]
related: [[concepts/context-window-management]], [[concepts/context-engineering]], [[concepts/context-compression]], [[concepts/context-routing]], [[concepts/kv-cache]]
sources: [https://arxiv.org/abs/2503.12345, https://www.anthropic.com/engineering/claude-context-window]
---

# Context Management

## Summary

Context management is the discipline of effectively constructing, maintaining, and optimizing the context window — the input space available to an LLM for a given interaction. As context windows have grown from 4K tokens (GPT-3, 2020) to 2M+ tokens (Gemini 1.5 Pro, 2024; Claude 4, 2025), the bottleneck has shifted from "can I fit everything in?" to "what should I put in, and in what order?" Context management encompasses strategies for context composition, prioritization, compression, and lifecycle management in both chat applications and agentic systems.

## Key Ideas

- **Context Window as Resource**: The context window is a finite resource that must be budgeted — every token costs compute (KV cache memory), latency (attention computation), and potentially quality (information overload)
- **Lost-in-the-Middle Problem**: LLMs reliably attend to content at the beginning and end of context, but performance degrades on content in the middle — a critical consideration for context organization
- **Structured Context**: Organizing context with clear section markers, system prompts, conversation history, and retrieved documents improves model attention over unstructured blobs
- **Proactive vs Reactive Context**: Proactive context (what the system pre-loads) vs reactive context (what the agent retrieves on demand) — agentic systems increasingly favor reactive approaches with retrieval
- **Context Compaction**: When agents run for extended periods, context must be compressed — summarizing old turns, pruning irrelevant tool outputs, or using KV cache compaction (Ramp Labs' Latent Briefing)
- **Multi-Agent Context**: In agent swarms, context sharing between agents introduces coordination overhead — patterns like "context graph" (Foundation Capital) and "experiential memory" (Vivek Trivedy) address this

## Terminology

- **System Prompt**: The initial, high-priority context block that sets model behavior, typically evicted last
- **Context Budgeting**: Allocating context tokens across system prompts, conversation history, retrieved documents, and tool outputs based on priority
- **Context Eviction Policy**: Strategy for removing content when the window fills — oldest-first, relevance-based, or LLM-judged
- **Claude Context Editing (2025)**: Claude Sonnet 4.5 feature that prunes old tool outputs from context, keeping only the most recent and relevant
- **Latent Briefing**: Ramp Labs' KV cache compaction technique — operating on model's internal state rather than token-level summarization
- **Context Fragments**: Vivek Trivedy's framework treating context as selectively loaded objects rather than a flat window

## Examples/Applications

- **Long Coding Sessions**: An agent working on a large codebase needs context management to maintain awareness of the full project while fitting relevant files into the window
- **Multi-Turn Conversations**: Customer support agents managing hour-long conversations need eviction policies that retain user intent and preferences while dropping resolved sub-dialogues
- **Research Agents**: Deep-dive research that reads dozens of documents requires structured context with clear attribution and prioritization of the most relevant sources
- **Agent Swarms**: Multiple agents collaborating on a shared task need context-sharing protocols to avoid redundant retrieval and conflicting state

## Related Concepts

- [[context-window-management]]
- [[context-engineering]]
- [[context-compression]]
- [[context-routing]]
- [[kv-cache]]
- [[context-graph]]

## Sources

- [The Lost-in-the-Middle Problem (arXiv 2307.03172)](https://arxiv.org/abs/2307.03172)
- [Claude's Extended Context Window | Anthropic Engineering](https://www.anthropic.com/engineering/claude-context-window)
- [Context Fragments: A Framework for Agent Memory | Vivek Trivedy](https://vtrivedy10.github.io/)
