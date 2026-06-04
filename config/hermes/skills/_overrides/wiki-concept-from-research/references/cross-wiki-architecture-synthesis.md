# Cross-Wiki Architecture Synthesis

## When to Use

When the user asks "what technical wiki knowledge supports this concept?" or "what elements from the wiki can be used to build X?" — where X is a concept that spans multiple architectural layers.

## Pattern

### Phase 1: Identify the Target Concept's Layers

Decompose the concept into its constituent technical layers before searching. For "Tenant Agent Pack," the layers were:

1. Memory isolation (per-tenant business memory)
2. Skills (per-tenant capability set)
3. Tool connections (per-tenant MCP)
4. Policy and guardrails (per-tenant rules)
5. Evaluation (per-tenant success criteria)
6. Runtime (pack loading and execution)
7. Sandbox isolation (execution boundary between tenants)
8. Context engineering (dynamic context for tenant adaptation)
9. Observability and cost (per-tenant monitoring and billing)

### Phase 2: Search Across Wiki Domains

For each layer, search concepts/ for relevant pages. The search should span multiple domains:

- Memory: `ai-agent-memory`, `memory-systems-design-patterns`, `filesystem-memory`, `context-engineering`
- Skills: `agent-skills`, `skill-graph`, `agent-skills-overview`
- Tools: `mcp`, `mcp-protocol`, `cli-over-mcp-pattern`
- Policy: `agent-governance`, `agentic-ai-governance`
- Runtime: `agent-runtime`, `durable-execution`, `runtime-opinionated-sdk`
- Sandbox: `agent-sandbox-patterns`, `sandbox`, `modal-sandboxes`
- Context: `context-engineering`, `context-management`, `progressive-disclosure`
- Observability: `observability`, `monitoring`, `outcome-based-pricing`

Use `terminal` with `ls | grep -iE` to find relevant files by name pattern, then `read_file` key pages.

### Phase 3: Map Wiki Primitives to Architecture Layers

For each layer, extract:
- **Which wiki pages support this layer** (with `[[wikilinks]]`)
- **Key insight from each page** (1-2 sentences, the most relevant finding)
- **How it maps to the target concept** (what adaptation is needed)

Present as a structured list with clear layer names, wiki references, and direct quotations where impactful.

### Phase 4: Identify Coverage Gaps

After mapping all layers, identify what the wiki does NOT yet cover. Present as a table:

| Covered | Not Yet Covered |
|---------|-----------------|
| X, Y, Z  | A, B, C        |

This frames the analysis as both synthesis and gap analysis.

### Phase 5: Produce Architecture Diagram (Optional)

If the layers have clear runtime relationships, produce a text-based architecture diagram showing flow between layers.

## Worked Example

The 2026-05-25 session's Tenant Agent Pack analysis (9 layers, ~10 wiki pages referenced per layer, coverage gap table) serves as the canonical example. The full analysis was produced in a single response turn after reading ~12 wiki pages.

## Pitfalls

- **Don't search one domain at a time** — use parallel terminal commands to grep for relevant pages across all domains simultaneously
- **Don't try to read every matching page** — prioritize the 1-2 most authoritative pages per layer
- **Keep layer descriptions tight** — 4-6 lines per layer max. The value is in the synthesis, not the re-explanation
- **Always include gaps** — the user wants to know what's missing, not just what's present
