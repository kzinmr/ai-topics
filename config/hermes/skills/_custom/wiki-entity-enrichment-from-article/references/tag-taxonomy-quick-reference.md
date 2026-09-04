# Tag Taxonomy Quick Reference

When writing frontmatter `tags:` for ANY wiki page, ALL tags MUST be canonical tags from `wiki/SCHEMA.md`. The pre-commit hook validates this.

## Common non-canonical → canonical mappings

| Non-Canonical (BLOCKED) | Canonical (OK) | SCHEMA Section |
| --- | --- | --- |
| `ai-alignment` | `alignment` | Models |
| `ai-agent-infrastructure` | `ai-infrastructure` | Engineering |
| `benchmarking` | `benchmark` | Techniques |
| `cdn` | `infrastructure` | Infrastructure |
| `company-vision` | `strategy` | Meta |
| `organization` | `company` | People/Orgs |
| `search-api` | `search` | Meta |
| `soc2` | `security` | Infrastructure |
| `web-monitoring` | `monitoring` | Engineering |
| `rl` | `reinforcement-learning` | Models |
| `dllm` | `reinforcement-learning` or `diffusion` | Models |
| `interview` | (no canonical — use `career` or remove) | — |
| `exploration` | (no canonical — use `inference`, `reasoning`, or `scaling`) | — |
| `llm-training` | `training` | Techniques |
| `llm-infrastructure` | `ai-infrastructure` | Engineering |
| `containment` | `ai-safety` or `safety` | Meta |
| `open-weight-models` | `open-source-ai` or `ai-safety` | Models/Meta |
| `ai-benchmarks` | `benchmark` | Techniques |
| `llm-security` | `security` | Infrastructure |
| `model-evaluation` | `evaluation` | Models |
| `cryptography` | `crypto` | Domain Concepts |
| `emacs` | `ide` or `terminal` | Engineering (tool names not in taxonomy; use broader tags) |
| `bespoke` | `customization` | Engineering (descriptive adjectives rarely canonical) |
| `soc-2` | `security` | Infrastructure |
| `game-devops` | `devops` | Engineering (industry-specific process names → broader category) |
| `model-release` / `model-releases` | `event` + `model` (+ company tag like `anthropic`/`openai`) | Neither variant is in SCHEMA (hit twice, 2026-09-03). For model-launch pages under `wiki/events/`, match sibling event pages — e.g. `2026-06-27-openai-gpt-5-6-sol.md` uses `event`, `model`, `openai`. Check `sed -n '/^tags:/,/^---/p'` of an existing event page before inventing tags. |

## How to find the right tag

1. Read `wiki/SCHEMA.md` — tags are organized by category: People/Orgs, Engineering, AI Agents, Infrastructure, Meta
2. Find the closest semantic match
3. If no match exists, add the tag to SCHEMA.md first, then use it
4. For a page type that already has siblings (events/, concepts/), the fastest safe route is copying the tag pattern from a sibling page rather than guessing a new tag.

## Emergency override

`git commit --no-verify` skips the check. Use only in emergencies.
