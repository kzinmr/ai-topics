# Feature-Level Documentation Page Template

When the documentation page covers a **specific feature or command** (not a whole platform/service), use this structure for the wiki concept page.

## Sections

### 1. Definition (1-2 sentences)
Clear, bold definition of what the feature is. Include the product context.

### 2. Architecture / Mechanism
How the feature works under the hood. For agent features, this often means a lifecycle diagram and explanation of the evaluation/completion mechanism.

Example for Claude Code `/goal`:
- Prompt-based Stop hook wrapper
- Evaluator model (Haiku) judges condition from transcript
- Lifecycle diagram: Set Goal → Work → Evaluate → Yes/No → Achieved/Retry

### 3. Comparison Tables (within product)
If the product has multiple approaches to the same class of problem, include a comparison table.

Example columns: Approach | Trigger | Stops when | Best for

### 4. Cross-Product Comparison
If a competitor product has a similar feature, include a comparison table highlighting architectural differences.

Example: Claude Code `/goal` vs Codex `/goal` — different completion mechanisms (evaluator model vs self-reporting).

### 5. Best Practices / Usage Guidance
How to use the feature effectively. Include do/don't tables, condition writing patterns, constraint specification.

### 6. Requirements / Limitations
What's needed to use it (permissions, trust dialogs, environment). What it can't do.

### 7. Related Concepts
Wikilinks to related wiki pages — the general concept this implements (e.g. agentic-loop), competitor's version, adjacent features.

## Page Quality Checklist

- [ ] Read the page alone → can you understand the feature without reading the source docs?
- [ ] Architecture section explains *how* it works, not just *what* it does
- [ ] Comparison tables help the reader choose between related features
- [ ] Cross-product table shows *architectural* differences, not just feature gaps
- [ ] Best practices include concrete examples (not just abstract advice)
- [ ] At least 3 related concept wikilinks
