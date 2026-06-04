---
name: arxiv-paper-pipeline
description: Workflow for pulling arXiv papers, triaging by peer-review status, and ingesting into wiki with proper save paths.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Research, Arxiv, Papers, Wiki, Pipeline]
    related: [arxiv, wiki-entity-enrichment-from-article]
---

# arXiv Paper Pipeline

## Save Path
Always save arXiv papers to `~/wiki/raw/papers/` (NOT `~/wiki/raw/articles/`).
Naming convention: `{YYYY-MM-DD}_{arxiv_id}_{short-title}.md` or `{arxiv_id}_{short-title}.md`.

## Triage Decision Matrix

| Paper Type | Action |
|---|---|
| Peer-reviewed conference paper (NeurIPS, ICML, ICLR, ACL, CVPR, etc.) | ✅ Wiki-ingest OK |
| Peer-reviewed journal paper (JMLR, TACL, Nature, Science, etc.) | ✅ Wiki-ingest OK |
| Workshop paper (peer-reviewed) | ⚠️ Case-by-case, usually OK |
| Tech company technical report (OpenAI, Meta, Google, Microsoft, etc.) | ✅ Wiki-ingest OK (exception) |
| Tech company tutorial / engineering blog | ✅ Wiki-ingest OK (exception) |
| arXiv-only (no venue listed, no peer-review) | ❌ BLOCK — skip wiki-ingest (unless user explicitly requests) |
| Student thesis / unpublished work | ❌ BLOCK — skip wiki-ingest |
| Survey paper (arXiv-only, not yet peer-reviewed) | ⚠️ Case-by-case — high signal worth keeping |
| **User override** (user explicitly asks to ingest a blocked paper) | ✅ INGEST — save with `blocked_reason` in frontmatter, note override in raw paper, proceed with concept/entity creation |

## Peer-Review Detection

1. **Check abstract page** (`https://arxiv.org/abs/{id}`) for venue info:
   - Look for "Published in", "Accepted to", conference/journal names
   - Semantic Scholar API: check `publicationVenue` field
2. **Check title/abstract** for venue mentions (NeurIPS, ICML, ICLR, ACL, etc.)
3. **Search Semantic Scholar** — if it has a venue, it's likely peer-reviewed
4. **If no venue found after research** → mark as blocked

## Processing Steps

1. Search arXiv via API or Semantic Scholar
2. For each candidate paper:
   a. Fetch abstract + metadata
   b. Research peer-review status (Semantic Scholar, abstract page)
   c. Apply triage decision matrix
   d. If blocked: skip, log reason. **Exception: if user explicitly requested ingestion**, treat as "User Override" — go to step (e) but save with `blocked_reason` in frontmatter, clear `status: blocked`, and note the override in the raw paper body.
   e. If accepted (including user override):
      - Save to `~/wiki/raw/papers/` with proper naming
      - Create wiki page:
        - **Concept paper** (new paradigm/framework/benchmark): use `wiki-concept-from-research` skill — generates a concept page with comparison tables vs related concepts
        - **Entity paper** (about a person/project/tool): use `wiki-entity-enrichment-from-article` skill — enriches existing entity page
        - **Supplementary paper** (incremental improvement to an existing concept): patch the existing concept page with new findings
      - Add `source_type: paper` to frontmatter
      - **Integrate user-provided context**: If the user provided a tweet, comment, or discussion alongside the paper link (e.g., jobergum's framing of SRA as harness engineering), weave that external perspective into the concept page as first-class content — it connects the academic work to practitioner concerns
3. Commit+push changes

## Blocked Papers Log

Keep a lightweight blocked list at `~/wiki/raw/papers/.blocked.json` to avoid re-evaluating:
```json
[
  {"arxiv_id": "2401.xxxxx", "reason": "no_peer_review", "date_blocked": "2026-04-27"}
]
```
