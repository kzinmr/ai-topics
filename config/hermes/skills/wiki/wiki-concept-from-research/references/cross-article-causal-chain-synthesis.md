# Cross-Article Causal Chain Synthesis

## When to Use

When the user says 「論じて」(discuss in relation to), 「絡めて」(connect with), or provides multiple articles that independently arrive at the same conclusion from different angles. Also fires when enriching an existing concept page with newly-ingested articles that form a logical progression with it.

**This is NOT the same as multi-source narrative synthesis.** In narrative synthesis, multiple sources contribute to one topic. In causal chain synthesis, multiple articles each cover a *different layer* of the same problem, and the synthesis reveals their structural relationship.

## Pattern

### Phase 1: Identify the Relationship Between Articles

Read each article and ask: *what question does this article answer, and at what layer?*

Common layer types:
- **Ontological** — Why do old assumptions break? (philosophical foundation)
- **Operational** — What changes in daily practice? (engineering translation)
- **Evaluative** — How do we measure quality? (assessment methodology)
- **Historical** — How did we get here? (timeline/context)
- **Comparative** — How do alternatives differ? (trade-off analysis)

### Phase 2: Build the Causal Chain

Arrange the articles so each one *necessitates* the next:

```
Article A (Ontological)  →  Article B (Operational)  →  Article C (Evaluative)
"Why old playbooks fail"    "What replaces them"        "How to measure success"
```

Each arrow should be defensible: "A implies B because..." The chain is structural, not chronological — the publication order doesn't matter.

### Phase 3: Present as a Unified Framework

Format: a comparison table of authors/theses/layers, followed by the causal chain diagram, then per-article elaboration.

**Template:**

```markdown
## Three Articles: A Unified Framework

| Author | Thesis | Layer |
|---|---|---|
| Name (Date) | "Quote or one-liner" | Ontological / Operational / Evaluative |
| ... | ... | ... |

### The Causal Chain
[A] → [B] → [C]  with brief explanation of each arrow.

All three argue that **[shared conclusion].**
```

### Phase 4: Enrich the Existing Page (Not Create a New One)

When the user says 「絡めて論じて」about an already-ingested article, enrich the **most relevant existing page** rather than creating a standalone comparison page. Add:
1. A "Unified Framework" section with the table + chain
2. Cross-links in the `related:` frontmatter of all involved pages (bidirectional)
3. The new raw article source in `sources:` if not already present

Only create a new page if the synthesis itself warrants a standalone portal/query page (e.g., the user explicitly asks for a portal, or the synthesis spans 5+ practice domains).

### Phase 5: Update Related Pages Bidirectionally

After adding the synthesis to the primary page:
1. Update each cited article's concept page to cross-link back
2. Update involved entities' pages (e.g., if Segato's essay is cited, add to `entities/gian-segato.md`)
3. Ensure all `related:` frontmatter lists are symmetrical

## Worked Example: Probabilistic Era Synthesis (2026-05-28)

Three independently-published articles formed a causal chain:

| Author | Article | Layer | Question Answered |
|---|---|---|---|
| Gian Segato | "Building AI Products In The Probabilistic Era" (Aug 2025) | **Ontological** | Why do old playbooks break? |
| Harrison Chase | "In software, the code documents the app..." (Jan 2026) | **Operational** | What changes in daily practice? |
| Ben Hylak | "Thoughts on Evals" / "How to Evaluate AI Agents" (Sep 2025 / May 2026) | **Evaluative** | How do we measure quality? |

**Causal chain:**
```
Segato: F: X→Y becomes F'(?)     →     Chase: Code no longer documents    →     Hylak: Evals can't capture
(ontological shift — input space        the app's actual behavior              production truth; floor raising
infinite, outputs stochastic)           (traces become source of truth)        via monitoring is the answer
```

**Shared conclusion:** Deterministic engineering playbooks (TDD, SLOs, funnel optimization) are actively harmful when applied to AI agents.

**Synthesis location:** Added as a "The Three Articles: A Unified Framework" section to `concepts/agent-observability-feedback.md` (the Chase article's existing concept page), because it was the most central page already covering the topic.

**Bidirectional updates:**
- `agent-observability-feedback.md` ← added section + cross-links to probabilistic-era-software, evals-vs-monitoring-debate
- `evals-vs-monitoring-debate.md` ← cross-linked Segato (replacing anonymous "Replit founding engineer" reference)
- `entities/gian-segato.md` ← already cross-linked via probabilistic-era-software

## Pitfalls

- **Don't create a new page for the synthesis unless asked.** The default is to enrich the most relevant existing page. New pages only when the user explicitly requests a portal, or when the synthesis spans 5+ domains and no single page covers the territory.
- **Don't present in publication order.** The chain is structural (ontological → operational → evaluative), not chronological. Segato published in Aug 2025 but his article is the foundation; Chase published in Jan 2026 but his is the middle layer.
- **Verify the chain is causal, not just parallel.** "They all agree" is not enough. Each link must have a "because": A implies B *because* the ontological shift to F'(?) means code can no longer document agent behavior.
- **Symmetrical cross-linking.** If page A links to page B, ensure page B links back to page A. Missing backlinks create one-directional navigation that breaks wiki exploration.
- **"Replit founding engineer" → identify the actual person.** When an article cites an anonymous source, identify and wikilink the actual entity (Gian Segato). This turns a dead-end reference into a navigable connection.
