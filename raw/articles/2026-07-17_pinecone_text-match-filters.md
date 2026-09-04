---
title: "Pinecone Text Match Filters for Agents"
created: 2026-07-17
updated: 2026-07-17
type: article
tags:
  - pinecone
  - text-match-filters
  - agentic-search
  - hybrid-search
sources:
  - https://www.pinecone.io/blog/text-match-filters/
---

# Pinecone Text Match Filters for Agents

Pinecone introduced Full Text Search filters designed specifically for AI agents. The lexical query restricts the candidate pool before semantic search, solving the "unstated context" problem — for example, "top presidential candidates" no longer returns French election results when the user is asking about US politics.

No pre-labeling is required. This is critical for agentic pipelines where bad retrievals compound wasted tool calls. In public preview.
