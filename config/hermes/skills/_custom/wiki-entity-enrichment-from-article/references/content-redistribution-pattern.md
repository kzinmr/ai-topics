# Content Redistribution Pattern for Concept Pages

When a new concept page overlaps with existing pages (e.g., a comprehensive Q&A document covering GRPO, RLVR, DPO, and SFT), the optimal approach is **not** to duplicate content. Instead, redistribute insights to their most specialized existing home.

## Decision Matrix

For each insight in the source material:

| Condition | Action |
|---|---|
| Insight is **unique** to the new page (synthesis, connecting thread) | Keep in new page — this is the page's *raison d'être* |
| Insight **duplicates** an existing page with no new angle | Remove from new page, add cross-ref to existing |
| Insight **adds depth** to an existing specialized page | Move detailed content to existing page, keep summary + cross-ref in new page |
| Insight **bridges** two existing pages that don't reference each other | Add bidirectional cross-refs; keep bridging narrative in new page |

## Example: LLM-as-Policy Page Redistribution

Source: Discord Q&A covering 5 topics (LLM-as-Policy, RM vs Critic, SFT as BC, traditional RL, DPO/GRPO convergence).

| Insight | Decision | Rationale |
|---|---|---|
| Core Formulation (state/action/policy table) | **Keep** in llm-as-policy | Unique framing, defines the page |
| RM vs Critic table + credit assignment example | **Detailed version → rl-algorithms**, summary + cross-ref in llm-as-policy | rl-algorithms is where people look for algorithm internals |
| SFT as Behavior Cloning + Brown's taxonomy | **Detailed version → on-policy-vs-off-policy**, summary + cross-ref in llm-as-policy | on-policy-vs-off-policy already covers this extensively |
| Traditional RL vs LLM-RL (3 structural reasons) | **Move → on-policy-vs-off-policy** as new subsection | This is theoretical analysis of the on/off-policy boundary, belongs in the specialized page |
| DPO/GRPO Convergence (implicit modeling) | **Keep** in llm-as-policy | Novel synthesis not found elsewhere — this is the page's unique value |
| Inference-Time Scaling as Exploration | **Keep** in llm-as-policy (different angle than rl-algorithms' table) | Both tables exist but serve different purposes |

## Procedure

1. Read the new page and all candidate existing pages
2. For each section in the new page, ask: "Is this the *best* home for this content?"
3. Move detailed content to the specialized page via `patch`
4. Replace with summary + `[[wikilink#section|display text]]` cross-ref in the new page
5. Add backlink from the existing page to the new page (bidirectional linking)
6. Verify no orphan cross-refs remain

## Pitfalls

- **Don't over-compress**: The new page should still be readable standalone. If every section is just "see other page," the page has no value.
- **Section-level cross-refs**: Use `[[page#Section Name|display]]` for precise linking, not just `[[page]]`.
- **Bidirectional**: When moving content to an existing page, always add a backlink from that page to the new page. Check the existing page's `## Related Pages` section.
- **Pre-commit language check**: When redistributing content, ensure no Japanese creeps into non-raw wiki files. The `pre-commit-jp-check.py` hook checks ALL staged files.

## External Book/Textbook Integration Pattern

When integrating a multi-chapter external resource (e.g., RLHF Book, Karpathy's LLM Wiki):

1. **Map chapters to existing wiki pages** — don't create a monolithic "Book X notes" page
2. **Add the book URL as a `source:`** in each enriched page's frontmatter
3. **Attribute inline** — "The RLHF Book (Lambert, 2026, Ch.5) provides..."
4. **Cite specific passages** with direct quotes when they add authority
5. **Update `log.md`** with a single entry listing all enriched pages

This produces a distributed knowledge integration rather than a siloed book report.
