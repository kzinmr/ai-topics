---
source_url: https://arxiv.org/abs/2609.15779
ingested: 2026-09-17
sha256: abcf39a46da1c719ea72e56c0ab6c7743f8f7740dcc264f463878565fda3e874
---

# EvoOntology: A Self-Evolving Ontology Layer for Data Agents

- **arXiv:** 2609.15779v1 (cs.DB / cs.CL)
- **Submitted:** 2026-09-14
- **Authors:** Meiduo Chong, Shaolei Zhang, Ju Fan, Xiaoyong Du (Renmin University group)

## Abstract (verbatim)

Data agents aim to fulfill natural-language instructions over heterogeneous data, including tables, files, and databases. However, data agents face a challenging agent-data gap: heterogeneous data resides outside the agent, while the agent can access it (e.g., column names and file paths) only through generic tools. Existing approaches either let agents directly explore raw data sources or inject manually constructed semantic layers into prompts. However, neither scales well: direct exploration is brittle and costly, while manual semantic layers are labor-intensive and static. We propose EvoOntology, a self-evolving ontology layer that incrementally builds and maintains a machine-readable semantic layer over an organization's heterogeneous data, evolving it as the agent encounters new data and tasks. (abstract truncated at source)

## Key ideas

- **Agent-data gap:** heterogeneous data lives *outside* the agent; the agent reaches it only through generic tools that expose bare column names / file paths, with no semantics.
- Existing approaches fall into two camps, both flawed: (a) **direct exploration** of raw sources — brittle and token-costly; (b) **manually constructed semantic layers** injected into prompts — labor-intensive and static (they go stale).
- **EvoOntology** = a *self-evolving ontology layer*: an incrementally built, machine-readable semantic layer over heterogeneous enterprise data that **evolves** as the agent meets new data and tasks. Bridges the gap between raw exploration and static hand-built semantic layers.

## Positioning
Falls under text-to-SQL / data-agent memory and the broader "self-evolving agents" trend, but specialized to the *data* domain via an ontology/semantic-layer artifact that is maintained automatically rather than hand-curated.
