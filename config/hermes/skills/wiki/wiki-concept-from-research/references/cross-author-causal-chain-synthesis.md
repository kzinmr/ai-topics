# Cross-Author Causal-Chain Synthesis

## When to Use

When ingesting multiple articles from different authors and discovering they form a **layered causal chain** — each article addresses a different level of the same problem (e.g., ontological → operational → evaluative) — the most valuable outcome is NOT creating standalone concept pages for each, but adding a **unified framework section** to an existing page that already covers one of them.

## Detection Signals

Any of these indicate a causal-chain synthesis opportunity:
- Article A provides the **WHY** (philosophical/ontological foundation)
- Article B provides the **WHAT** (operational translation into daily practice)
- Article C provides the **HOW** (evaluation/methodology)
- They arrived at the same conclusion independently from different angles
- One article explicitly cites another (chain-citation signal)
- User says "以下の記事とも絡めて論じて" (discuss in relation to the other articles)

## Workflow

### Step 1: Map the Layers

Identify which article fills which layer. The canonical layers are:

| Layer | Question | Example |
|---|---|---|
| **Ontological** | Why do old playbooks break? | Segato: `F: X→Y → F'(?)` |
| **Operational** | What changes in daily practice? | Chase: "code documents the app → traces do" |
| **Evaluative** | How do we measure quality? | Hylak: "floor raising > benchmark maxxing" |

Not all three layers may be present. The key is recognizing the complementarity.

### Step 2: Find the Anchor Page

Identify which wiki page already covers one of the articles best. This is typically:
- An existing concept page that addresses the operational/evaluative layer
- The page that has the richest pre-existing content

Do NOT create a new page just to host the synthesis — enrich the anchor page.

### Step 3: Add the Unified Framework Section

Add to the anchor page a comparison table + causal chain diagram:

```markdown
## The Three Articles: A Unified Framework

Three independently-arrived-at perspectives converge on the same conclusion:

| Author | Thesis | Layer |
|---|---|---|
| **Author A** (Date) | "Key quote" | **Ontological**: why old assumptions break |
| **Author B** (Date) | "Key quote" | **Operational**: what changes in practice |
| **Author C** (Date) | "Key quote" | **Evaluative**: how to measure quality |

### The Causal Chain

[ASCII diagram showing A → B → C relationship]

All three argue that deterministic engineering playbooks are actively harmful when applied to AI agents.
```

### Step 4: Cross-Link All Pages

After adding the synthesis section:
1. Update ALL involved entity pages with cross-links to the synthesis page
2. Update ALL involved concept pages' `related:` frontmatter
3. Ensure the causal chain is visible from any entry point

### Step 5: Save All Raw Articles

Each article in the chain needs its own raw article saved, even if partially covered by an existing digest.

## Canonical Example

The Segato → Chase → Hylak chain (2026-05-28 session):

- **Segato** (Aug 2025): "Building AI Products In The Probabilistic Era" — ontological shift: `F: X→Y` becomes `F'(?)`, infinite input space, stochastic outputs
- **Chase** (Jan 2026): "In software, the code documents the app. In AI, the traces do." — operational translation: debugging→trace analysis, testing→eval-driven
- **Hylak** (Sep 2025 / May 2026): "Thoughts on Evals" + "How to Evaluate AI Agents" — evaluation methodology: floor raising, production monitoring

Result: synthesized into `concepts/agent-observability-feedback.md` as "The Three Articles: A Unified Framework."

## Pitfalls

- **Don't create a new page for the synthesis if an anchor page exists.** Enrich, don't proliferate.
- **Don't flatten the layers.** Each author's contribution must remain distinct in the comparison table.
- **Verify independence.** Before claiming "independently arrived at," check for citation relationships.
- **Use markdown-only diagrams.** No Mermaid or external rendering — the wiki is plain markdown.
