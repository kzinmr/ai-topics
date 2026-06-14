# Agent-*/Agentic-* Semantic Classification Migration (2026-06-11)

## Context

85 flat `agent-*` and `agentic-*` concept pages in `concepts/` needed organization. User decided:
- `agent(ic)-*` and `llm-*` are **universal themes** — too cross-cutting for a single subdirectory
- Pages should be classified by **semantic tags**, not just filename prefix
- Infrastructure/Runtime pages (9) stay flat — `training-infra/` and `inference/` cover different axes

## Classification Method

Tag co-occurrence analysis with first-match classification:

```python
subcats = {
    "security-and-governance": {"security", "governance", "agent-safety", "agent-containment"},
    "harness-engineering": {"harness-engineering", "agentic-engineering", "agent-design-patterns", "architecture"},
    "orchestration-and-communication": {"orchestration", "multi-agent", "mcp", "agent-communication-protocols"},
    "infrastructure-and-runtime": {"infrastructure", "sandbox", "developer-tooling", "agent-runtime"},
    "evaluation-and-observability": {"evaluation", "methodology", "observability"},
}
```

## Results

| Target | Pages | Notes |
|---|---|---|
| **security-and-governance/** (NEW) | 13 | Created new subdir with `_index.md` |
| **harness-engineering/** (existing) | 25 | Absorbed into existing 50-file subdir |
| **multi-agents/** (existing, was agent-team-swarm/) | 9 | Absorbed into existing subdir (later renamed from agent-team-swarm/) |
| Flat (no move) | ~38 | Infrastructure, uncategorized, or too few for grouping |

## Manual Review Corrections

Initial tag-based classification over-matched "security" (20 pages). After manual review:
- `agent-development-lifecycle` → harness-engineering (governance is secondary tag)
- `agent-hosting-aws` → harness-engineering (infrastructure, not security)
- `agent-operator-patterns` → harness-engineering (orchestration, not security)
- `agent-runtime` → harness-engineering (architecture, not security)
- `agent-serverless` → harness-engineering (infrastructure, not security)
- `agent-orchestration` → multi-agents (multi-agent, not security)
- `agentic-conflict-resolution` → multi-agents (multi-agent, not security)

## Post-Migration Rename

After the initial migration, `agent-team-swarm/` was renamed to `multi-agents/` (133 links updated). This required a separate directory-rename pass.

## Link Update Stats

- 534 wikilinks updated across wiki (initial migration)
- 133 wikilinks updated (directory rename to multi-agents/)
- Single unified regex pass covering all 47 moved slugs
- Updated `_index.md` for all 3 target subdirs

## Decision: Infrastructure-and-Runtime Stays Flat

9 pages (agent-economics, agent-evaluation-methodology, agent-native-cloud, agent-observability, etc.) were checked against:
- `training-infra/` (7 files: GPU/training infra)
- `inference/` (5 files: serving engines like vllm, sglang)

Conclusion: Different axes (agent runtime economics vs GPU/training infra). No overlap. Stay flat.

## Lessons

1. Tag-based classification needs **manual review** — tags are noisy
2. **First-match** classification prevents double-counting but may misorder
3. Check existing subdirs for **absorption** before creating new ones
4. Single-pass link update (one regex, one walk) is more efficient than per-category passes
5. Keep the commit atomic — one commit for the entire reorganization
6. Directory renames after migration are possible but add a second link-update pass — prefer choosing the right name upfront
