---
title: "LLM Memory Architecture"
created: 2026-04-30
updated: 2026-04-30
tags: [ai-agents, memory, architecture, knowledge-graphs]
aliases: [llm-memory, agent-memory-architecture]
related: [[concepts/ai-agent-memory-middleware]], [[concepts/ai-agent-memory-two-camps]], [[concepts/ai-memory-systems]], [[concepts/context-engineering]], [[concepts/claude-memory]]
sources: [
  "https://grantslatton.com/llm-memory"
]
---

# LLM Memory Architecture

## Summary

Grant Slatton's conceptual exploration of LLM memory systems, tracing the evolution from GPT-3 era (4K context windows) to modern agent architectures. The core thesis: LLM memory requires explicit structure — not just vector embeddings — to handle reference frames, episodic chains, and knowledge synthesis.

> "There's no grand thesis statement to this post, it's just a ramble." — Grant Slatton

## Core Concepts

### Reference Frames

All knowledge has an explicit or implicit reference frame for which it is valid. This is the most important observation in the piece:

- **Temporal reference frames**: "Berlin is the capital of Germany" is true in one era, "Bonn was the capital of West Germany" in another. Facts are time-bound.
- **Spatial reference frames**: Human brains don't have one global spatial reference frame. Your house floorplan is disconnected from your neighborhood, which is disconnected from your city.
- **Alternate timelines**: Works of fiction create alternate universes with different facts.
- **Abstract spatialization**: You can spatialize abstract concepts (e.g., foods on a 2D grid by saltiness vs. spiciness).

Inspired by Jeff Hawkins' "Thousand Brains" theory.

### Vector Embeddings — Strengths and Limits

Vector embeddings map text to N-dimensional points where semantic similarity = spatial proximity. However, they struggle with:

1. **Episodic memory**: Storing chains of memories in series order is hard. How do you embed the link between two memories?
2. **Opacity**: If two vectors are anomalously close or far, you have no recourse. Adjust training data? Change distance metric?
3. **No reference frames**: No clear way to bolt temporal or spatial reference frames onto vector DBs.

> "In the GPT-3 era, I thought vector databases were all you need to build AGI. I changed my mind as soon as I actually tried it."

### Knowledge Graphs

Knowledge graphs link memories together: "Berlin" connects to "Germany", "List of world capitals", "WW2", "Cold war", "Prussia", etc.

**Design choices:**
- **Semantic edges**: "Jerry Stiller" → "Ben Stiller" with a "father of" edge. Nodes can be tiny.
- **Unlabeled edges**: Nodes must be self-contained documents that are individually useful.

**Document-based approach (favored):**
- More "Bitter Lesson"-pilled: deploy thousands of cheap agents to crawl the unlabeled local graph looking for relevant information
- Pairs well with vector embeddings: embed documents or questions they answer, use embeddings to jump to candidate nodes
- Semantic edges for temporal ordering: "happened after" feels natural as an edge property

### Meta-Documents

Over time, the majority of items in a knowledge graph become meta-documents instead of source documents.

**The process:**
1. Run a query over the knowledge graph
2. Store the results + reasoning as a new document
3. Connect it to all the source documents used

Example: "My 5 favorite European cities" becomes a cached document. When asked "5 favorite cities in the world", the European results are already computed.

This mirrors human memory: when you recall something, you recall the last time you recalled it (which can cause distortion).

### Making Connections

After producing a new document, two strategies:

1. **Automatic**: Any documents in context when producing a new document auto-connect
2. **Explicit**: Take every pair of documents in context, ask the model if they should be connected, what future queries would be helped, and make the connection if likely

### Forgetting / Garbage Collection

Unbounded graph growth makes navigation harder. Strategies:

- **Reinforcement**: Reinforce frequently traveled connections, let others decay and be deleted
- **LLM judgment**: Ask the model to judge connections as poor/unused and surgically excise them
- **Spaced repetition**: Connection deletion probability has a refreshable decay property
- **Remake-on-demand**: Deleted connections can be remade through sibling nodes (one extra hop)

> "Don't humans do the same thing? There's stuff you just can't forget despite being useless?"

### Episodic Memory

- **Episodes**: Narrative documents of what happens to the agent as it happens, with start/stop points
- **Sleep consolidation**: At day's end, the model creates a meta-document "everything that happened on 2025-05-17" with summaries
- **Theme extraction**: Pull common themes from episodes and create meta-documents about synthesized learnings
- **Query-as-episode**: "In May 2025, I was asked by Josh what European cities I've visited, and I compiled the following list" — the list is embedded within an episode

### Traversal Strategy

**Dead simple approach:**
- All the day's episodes in context
- Last 15 daily summaries
- Last 15 weekly summaries
- Last 15 monthly summaries
- All yearly summaries
- Identify all nodes connected within 2 jumps that look promising

**Optimizations:**
- Extract relevant quotes from documents instead of loading full content
- Priority queue instead of BFS: ask the model to rank nodes by promise relative to the query

### Traversal Agent Design

**Simple agentic approach:** Model has context on what it's looking for, tools to load documents, take notes, unload documents (clear context), see its action log, and return query results when ready.

**Sophisticated approach:** Query agents spin off sub-agents for sub-queries, each with a search budget. "Who was the nephew of Queen X?" becomes a delegated sub-task.

### Databases as External Tools

SQLite tables for structured data (world capitals, kings of England, dictionaries) should be modeled as external tool uses, not part of core memory. The agent stores a memory "I have an SQLite table with all the world capitals" and uses the tool when needed.

### Scratchpads

Simplest memory: single text scratchpad that gets appended to. When full, ask the model to prune irrelevant content.

**Problem:** Models prune failure logs, then retry the same failed actions. "Some models will decide to prune the failure log, after all, what good is it? But then they try the failed course of action again as soon as it's proned."

> "Most humans would not do well if they had admin edit access to their own memories."

### Layers of Memory

Things core to identity, motivations, personality, temperament feel fundamentally different from episodic memories. They should be represented separately, at minimum.

### Implicit vs. Explicit Control

**Lean toward implicit:** Models overestimate their own abilities. Given a memory tool, they're just as likely to conjure an answer from weights as use the tool. This works for well-established facts but fails for recent events outside training data.

### Neural Methods (Future)

Eventually subsumed by fully-learned, end-to-end memory approaches represented in vectors/weights. Possibilities:
- Ultra-sparse mixture of experts — train new experts nightly and plug them in the next day
- Recurrent architectures
- "Who knows. I don't have a lot to say here."

## Architecture Diagram

```
┌─────────────────────────────────────────────┐
│                  EPISODES                     │
│  (narrative documents of what happened)      │
│          ↓ consolidation during "sleep"       │
├─────────────────────────────────────────────┤
│               DAILY SUMMARIES                │
│          ↓ theme extraction                   │
├─────────────────────────────────────────────┤
│              WEEKLY SUMMARIES                │
│          ↓ synthesis                          │
├─────────────────────────────────────────────┤
│             MONTHLY SUMMARIES               │
│          ↓ long-term patterns                │
├─────────────────────────────────────────────┤
│              YEARLY SUMMARIES               │
│          ↓ meta-document network             │
├─────────────────────────────────────────────┤
│           KNOWLEDGE GRAPH                    │
│  (documents + connections + reference frames) │
│          ↔ vector embeddings (jump-start)    │
│          ↔ external tools (SQLite, APIs)     │
└─────────────────────────────────────────────┘
```

## Key Quotes

- "A lot of memories would work great in an SQLite table... I think it's simplest to just model these as external tool uses rather than part of the core memory system. Similar to humans!"
- "The agent treats its own memory as a 'hint' and verifies against actual state before acting." — Claude Code pattern, aligns with Slatton's observation about implicit control
- "You can get really dumb, loopy behavior for non-trivial tasks with this system." — on flat scratchpad memory
- "Models are prone to overestimating their own abilities. You ask them some historical fact, give them access to a memory tool, they are just as likely to conjure an answer from within the model weights as they are to make extensive use of the tool."

## See Also

- [[concepts/ai-agent-memory-middleware]] — Cross-platform comparison of agent memory storage
- [[concepts/ai-agent-memory-two-camps]] — Memory Backends vs Context Substrates classification
- [[concepts/ai-memory-systems]] — OpenAI vs Anthropic vs Cognition memory design comparison
- [[concepts/claude-memory]] — Claude's filesystem-based memory approach
- [[concepts/context-engineering]] — Managing what the model sees and when
- [[entities/grant-slatton]] — Author
