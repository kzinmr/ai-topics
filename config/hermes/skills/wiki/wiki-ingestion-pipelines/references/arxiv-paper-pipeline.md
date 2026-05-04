# arXiv Paper Pipeline — Full Reference

## Save Path
Always: `~/wiki/raw/papers/{YYYY-MM-DD}_{arxiv_id}_{short-title}.md`
(NOT `~/wiki/raw/articles/`)

## Triage Decision Matrix
| Paper Type | Action |
|---|---|
| Peer-reviewed (NeurIPS, ICML, ICLR, ACL, CVPR, JMLR, TACL, Nature, Science) | ✅ Wiki-ingest OK |
| Workshop paper (peer-reviewed) | ⚠️ Case-by-case |
| Tech company/industry research lab tech report (OpenAI, Meta, Google, MS, Anthropic, Huawei, Apple, Amazon, NVIDIA, Samsung, Sony, etc.) | ✅ Wiki-ingest OK |
| arXiv-only (no venue) | ❌ BLOCK — skip |
| Survey paper (arXiv-only) | ⚠️ Case-by-case |
| User explicitly requests blocked paper | ✅ User override — ingest with blocked_reason note |

## Peer-Review Detection
1. Check abstract page: `https://arxiv.org/abs/{id}` — look for "Published in", "Accepted to"
2. Semantic Scholar API: check `publicationVenue` field
3. If no venue found → mark as blocked

## Processing Steps
1. Search arXiv API or Semantic Scholar
2. For each candidate: fetch abstract+metadata → research peer-review → apply triage
3. If accepted (including user override):
   - Save to papers/ with proper naming
   - Create/update wiki page (concept, entity, or patch)
   - Add `source_type: paper` to frontmatter
4. If blocked: skip, log reason. Keep blocked list at `~/wiki/raw/papers/.blocked.json`

## Name Collision Handling

When a paper's framework name collides with an existing concept page (e.g., this session's lambda-RLM (Huawei) vs existing Lambda-RLM (Galanos)):

1. **Detect collision early** — `search_files` for the framework name in existing concept slugs and content before creating
2. **Create a new concept page** with a distinct, descriptive slug (e.g., `typed-rlm` instead of conflicting `lambda-rlm`)
3. **Add aliases** in the new page's frontmatter to include the paper's name (e.g., `aliases: [lambda-RLM, Lambda-Recursive Language Model, Y-Combinator RLM]`)
4. **Add disambiguation** to the existing page — a warning box at the top referencing the new page
5. **Create a comparison table** on the new page showing key differences (control model, formal proofs, empirical scope, source)
6. **Update the parent concept page** (e.g., `rlm-recursive-language-models`) to list both as variants
7. **Update log.md** explaining the collision and resolution

## Blocked Papers Log Format
```json
[
  {"arxiv_id": "2401.xxxxx", "reason": "no_peer_review", "date_blocked": "2026-04-27"}
]
```
