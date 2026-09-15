---
title: Isaac Tai
description: Cerebras AI/Growth team member; lead author of the Cerebras agent-facing knowledge base engineering write-up
url: https://x.com/hi_im_isaac_
type: entity
social: https://x.com/hi_im_isaac_
updated: 2026-09-14
aliases:
  - hi_im_isaac_
  - Isaac
tags:
  - person
  - ai-infrastructure
  - devrel
sources:
  - raw/articles/2026-07-16_cerebras_knowledge-base-architecture.md
  - https://x.com/hi_im_isaac_
---

# Isaac Tai

**Isaac Tai** (X: [@hi_im_isaac_](https://x.com/hi_im_isaac_)) works on the **AI/Growth team at Cerebras Systems** and is first-bylined author of "How we built our knowledge base" ([Cerebras blog](https://www.cerebras.ai/blog/how-we-built-our-knowledge-base), July 2026; raw: [[raw/articles/2026-07-16_cerebras_knowledge-base-architecture]]), alongside [[entities/daniel-kim-cerebras|Daniel Kim]] and [[entities/mike-gao|Mike Gao]].

## Key Work: Cerebras Knowledge Base

The post documents a production retrieval system now answering **15,000+ questions per day** from employees, automations, and coding agents — three months after launch. Engineering details from the write-up:

- **Slack "bursting" by author**: consecutive runs of messages from the same author are embedded together so tangent messages stay findable; each burst must clear a quality threshold (e.g. containing a rare token with IDF ≥ 4.0).
- **CocoIndex for code embeddings**: after several experiments the team landed on [CocoIndex](https://github.com/deriveback/cocoindex), an open-source embedding framework specialized for codebases, with sync metadata in Postgres — only changed code chunks are re-embedded per commit.
- **Hybrid search** (BM25 + embeddings) across Slack, code comments, and docs, served via MCP to agents.
- **Custom sources as plugin scripts**: teams PR a small Python module emitting rows in the shared embeddings schema — same query surface over existing databases.

## X Account

- Handle: **@hi_im_isaac_** (joined February 2013)
- ~1K followers, ~1.3K tweets
- No public bio text; identity anchored to the Cerebras knowledge base byline and handle.

## Team Connections

- [[entities/daniel-kim-cerebras]] — Head of Growth, Cerebras; co-author
- [[entities/mike-gao]] — ML Runtime @ Cerebras; co-author

## Related

- [[entities/cerebras-systems]] — employer
- [[concepts/bm25]] — keyword retrieval component of the hybrid search stack
- [[concepts/ai-agent-memory]] — company-scale memory layer for agents
- [[concepts/contextual-retrieval]] — chunk-quality thresholds (IDF bursting) as contextual retrieval practice
- [[concepts/rag-systems]] — production hybrid RAG deployment

## Sources

- [[raw/articles/2026-09-11_cerebras-scaling-knowledge-base-llm-context]] — knowledge base write-up (lead author)
- [X: @hi_im_isaac_](https://x.com/hi_im_isaac_) — profile verified via X API 2026-09-14
