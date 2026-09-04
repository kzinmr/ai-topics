# Knowledge Redistribution: When a New Concept Page Is a Hub, Not a Sink

## Problem

When ingesting a rich Q&A document, technical report, or multi-chapter book into the wiki, the naive approach is to create a single new concept page containing all extracted insights. This creates content duplication — the new page restates what existing pages already cover, or buries insights where nobody will find them.

## The Pattern

A new concept page should be a **hub** (unique framing, paradigm overview, cross-references) — not a **sink** (detailed content that belongs in specialized existing pages).

### Step 1: Create the new page with full content initially

Write the concept page with all extracted insights. This gives you a complete view of the material.

### Step 2: Identify which insights have a better home

For each section, ask: "Is there an existing page where a reader would expect to find this?"

| Insight Type | Better Home |
|---|---|
| Algorithm-specific details (RM vs Critic comparison) | Algorithm page (`rl-algorithms-for-llm-training.md`) |
| Historical/practical techniques (RLVR training practices) | Domain-specific page (`rlvr.md`) |
| Paradigm-level framing (LLM-as-Policy as unifying view) | The new concept page itself |
| Cross-cutting structural analysis (DPO/GRPO convergence) | The new concept page itself |

### Step 3: Move content to existing pages

For each insight with a better home:
1. Add the content to the existing page in the appropriate section
2. In the new concept page, replace the detailed content with a **summary + cross-ref**:
   ```markdown
   ## Topic Name

   Brief summary (2-3 sentences) of the key point.
   Detailed treatment in [[concepts/existing-page#Section Name]].
   ```
3. The summary should be self-contained enough that the page makes sense without following the link

### Step 4: Verify cross-references are bidirectional

After redistribution:
- New page → existing pages (outward links in summary)
- Existing pages → new page (backlinks in Related Pages section)
- Each existing page that received content should mention the new page as a cross-ref

### Step 5: Add sources to all affected pages

When content from an external resource (book, paper, lecture) is distributed across multiple pages, add the resource URL to the `sources:` frontmatter of **every page that received content** — not just the new hub page.

## Example: LLM-as-Policy Ingestion (2026-06-15)

Q&A document covered 5 topics. After initial creation of `llm-as-policy.md`:

| Topic | Initial Location | Redistributed To | Why |
|---|---|---|---|
| RM vs Critic comparison + credit assignment example | llm-as-policy.md | rl-algorithms-for-llm-training.md | Reader looking for algorithm details goes there |
| SFT as behavior cloning + traditional RL distinctions | llm-as-policy.md | on-policy-vs-off-policy-rl.md | That page already covers SFT/RL boundary |
| DPO/GRPO convergence (implicit modeling) | llm-as-policy.md | **stayed** | Unique structural insight, no existing home |
| Core formulation (state/action/policy mapping) | llm-as-policy.md | **stayed** | Defining content of the new page |
| Inference-time scaling as exploration | llm-as-policy.md | **stayed** | Unique framing, though rl-algorithms has a related table |

Result: llm-as-policy.md went from ~200 lines to ~170 lines. The redistributed content added ~40 lines across 2 existing pages. All 5 pages got `llm-as-policy` backlinks.

## Example: RLHF Book Integration (2026-06-15)

17-chapter book. Chapters distributed across 5 existing pages:

| Chapter | Content Added | Target Page |
|---|---|---|
| Ch.5 Reward Models | RM/ORM/PRM/Value 4-way taxonomy | rl-algorithms-for-llm-training.md |
| Ch.6 Policy Gradients | RLOO≈GRPO equivalence | grpo-rl-training.md |
| Ch.8 Direct Alignment | DPO implicit reward + preference displacement | rlhf.md |
| Ch.7 Reasoning | RLVR training practices table | rlvr.md |
| Ch.1,3,7,14 | Paradigm framing (superficial alignment debunking, RL as load-bearing) | llm-as-policy.md |

Each target page received `rlhfbook.com` in its `sources:` frontmatter.

## Pitfalls

- **Don't compress too aggressively**: The hub page should still be readable standalone. A page that's nothing but cross-refs is useless.
- **Don't redistribute unique insights**: If the new document contains a structural analysis that no existing page covers (like DPO/GRPO convergence), keep it on the hub page.
- **Update timestamps**: Every page that receives redistributed content needs its `updated:` field bumped.
- **index.md for the hub**: The new page must appear in index.md with a description that captures its unique value (paradigm framing), not the redistributed content.
- **Don't wait for user direction**: If you can see that an insight belongs on an existing page, move it there proactively. The user having to say "distribute this" means you missed the signal.
