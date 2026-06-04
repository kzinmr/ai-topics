# Tenant Agent Pack: 9-Layer Technical Architecture

Reference for mapping Tenant Agent Pack's 16 per-tenant artifacts to existing wiki technical primitives.

## Layer Mapping

| Layer | Component | Wiki Primitives | Maturity |
|-------|-----------|-----------------|----------|
| L1 | Memory Isolation | `ai-agent-memory`, `filesystem-memory`, `experiential-memory`, `context-engineering` | ◎ |
| L2 | Skills | `agent-skills`, `skill-graph`, `five-tier-skill-precedence`, Progressive Disclosure (3-tier) | ◎ |
| L3 | Tool Connection | `mcp`, `mcp-protocol`, `cli-over-mcp-pattern`, `mcp-desktop-extensions` | ◎ |
| L4 | Policy & Guardrails | `agent-governance`, `agentic-ai-governance`, Runtime Guardrails | ○ |
| L5 | Evaluation | `agent-evaluation`, `evals-skills` | △ |
| L6 | Runtime | `agent-runtime` (5-layer stack), `durable-execution`, `runtime-opinionated-sdk` | ○ |
| L7 | Sandbox Isolation | `agent-sandbox-patterns` (Pattern 2: Isolate the Agent), `sandbox`, `modal-sandboxes` | ◎ |
| L8 | Context Engineering | `context-engineering`, `context-management`, `progressive-disclosure`, `context-routing`, 5 failure modes (Poisoning/Distraction/Confusion/Clash/Rot) | ◎ |
| L9 | Observability & Cost | `observability`, `monitoring`, `outcome-based-pricing` | △ |

## Identified Gaps
1. **Tenant Pack Loader**: Standard pipeline for tenant ID → Pack resolution → runtime injection
2. **Pack Versioning**: Per-tenant version management, rollback, canary deploy
3. **Pack Template**: Industry/domain-specific Pack templates with inheritance
4. **Pack Validation**: Pre-deploy integrity checks, security review, policy conflict detection
5. **Tenant Migration**: Inter-tenant Pack copy/migration/merge

## Architecture Diagram
```
                         ┌──────────────────────────┐
                         │   Agent Control Plane     │  ← Cross-tenant governance
                         └──────────┬───────────────┘
                                    │ MCP / A2A
         ┌──────────────────────────┼──────────────────────────┐
    ┌────▼─────┐              ┌────▼─────┐              ┌────▼─────┐
    │ Tenant A │              │ Tenant B │              │ Tenant C │
    │ Sandbox  │              │ Sandbox  │              │ Sandbox  │
    │ Pack A   │              │ Pack B   │              │ Pack C   │
    └──────────┘              └──────────┘              └──────────┘
```

## Source Articles
- `blog/2026-05-25_hermes_tenant-agent-pack-technical-architecture.md`
- `concepts/tenant-agent-pack.md`
- `raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md`
