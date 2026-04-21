# The 5 Types of AI Agent Memory Every Developer Needs to Know

**Source:** DEV Community - Sreeni Ramadorai (AI Solution Architect)
**URL:** https://dev.to/sreeni5018/the-5-types-of-ai-agent-memory-every-developer-needs-to-know-part-1-52fn

---

## Core Concept: Memory is Infrastructure, Not Model

> **"Agent memory is not a model problem. It is an infrastructure problem."**

> **"You cannot give the model memory. You have to build memory infrastructure around it."**

> **"The agent does not remember. The infrastructure remembers."**

**Key Insight:** LLMs are stateless by design—every inference call starts completely fresh. Statelessness is what allows LLMs to scale to millions of users.

---

## The Context Window: The Only Reality

- The **context window is the only reality the LLM has**
- Every token (conversation history, retrieved documents, tool outputs, system instructions) must be inside the context window at inference time
- Context windows are: finite (token limits), cost money to fill, reset completely between sessions

**Memory architecture** is the system that intelligently decides what information gets retrieved, when, and how to inject it into the context window.

---

## The 5 Types of Agent Memory

### 1. Short-Term Memory (STM) — The Conversation Buffer

**Purpose:** Conversation coherence within a single session

**Implementation:** Rolling token buffer. Older messages truncated/summarized when approaching token limit. Buffer clears entirely when session ends.

**Analogy:** Like RAM—fast, active, useful right now. Gone when you turn it off.

### 2. Long-Term Memory (LTM) — Persistence Across Sessions

**Purpose:** Makes agent feel like it actually knows you across sessions

**Implementation:** Vector database (Pinecone, Weaviate, ChromaDB). Information converted to vector embeddings + metadata. Similarity search retrieves top-k relevant memories.

### 3. Working Memory — The Reasoning Scratchpad

**Purpose:** Holds intermediate results during multi-step tasks

**Implementation:** In-memory structure (dict/JSON object). Maintained by agent framework across loop iterations. Current state injected into context window at each step.

### 4. Episodic Memory — The Interaction Log

**Purpose:** Recall specific past events, not just general preferences

**Key distinction:**
- Long-Term Memory → stores *what you like*
- Episodic Memory → stores *what happened*

**Implementation:** Structured log of past interactions. Each saved as event record with: timestamp, task, inputs, actions, outcome. Queried by timestamp, keyword, or semantic similarity.

### 5. Semantic Memory — The Knowledge Layer

**Purpose:** Agent's understanding of world facts, concepts, domain knowledge

**Sources:** Model's pre-trained weights (general knowledge) + External knowledge base via RAG (Retrieval Augmented Generation) for domain-specific, up-to-date needs

---

## Key Quote

> "The agent does not remember. The infrastructure remembers."