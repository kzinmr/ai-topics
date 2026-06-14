# LLM API Pricing — Fable 5 Update (2026-06-11)

Concrete example of adding Claude Fable 5 to `comparisons/llm-api-pricing.md`.

## Data Gathered

| Field | Value | Source |
|-------|-------|--------|
| Input | $10/MTok | Anthropic blog |
| Output | $50/MTok | Anthropic blog |
| Cache Read | ~$1.00/M (est. 90% discount) | Inferred from Opus 4.8 pattern |
| Cache Write | ~$12.50/M (est. +25%) | Inferred |
| Batch | Not announced | — |
| Context | 1M input / 128K max output | Anthropic blog |
| Tier | Ultra-Premium (new, above Premium) | Derived |
| API ID | claude-fable-5 | Anthropic blog |

## Sections Updated (8 hunks)

1. **US Frontier table**: `| Anthropic | Claude Fable 5 | Ultra-Premium | $10.00 | $50.00 | ~$1.00 | ~$12.50 | — | — | 1M | 128K |`
2. **Cache discount rates**: `| **Anthropic (Fable 5)** | **~90%** | +25% | Explicit breakpoints (est.) | ❌ |`
3. **Cache read prices**: `| Anthropic | Claude Fable 5 | $10.00 | ~$1.00 | ~90% | **~$2.80** |`
4. **Anthropic cache break-even**: `| Claude Fable 5 | $10.00 | ~$12.50 | ~$1.00 | ~1.4 calls |`
5. **Batch pricing**: `| Anthropic | Claude Fable 5 | $10.00 | — | $50.00 | — | — |`
6. **Tier analysis (Premium)**: `| Anthropic | Claude Fable 5 | $10.00 | $50.00 | ~$1.00 | ~$18.00 | Mythos-class; safety classifiers; 1M ctx |`
7. **Cost comparison (Chat 4:1)**: `| Anthropic | Claude Fable 5 | ~$18.00 | **~$4.60** |`
8. **Cost comparison (Code 1:1)**: `| Anthropic | Claude Fable 5 | $30.00 |`

## Issues Encountered

1. **Duplicate `updated:` field**: Patch tool created a second `updated:` line because old_string matched the existing one. Fixed with `sed -i '5d'`.
2. **Section numbering cascade**: Inserting Key Trends #2 without renumbering 3→4, 4→5, 5→6. Fixed with three `sed` substitution commands.
3. **Commit message `$` escaping**: `git commit -m "...$10/$50..."` interpreted as shell variables, showed `$0/$0` in commit. Harmless but cosmetic — use `\$` escaping next time.

## Blended Cost Calculation

Blended = weighted cost at 4:1 input:output ratio:
- Fable 5: ($10 × 4 + $50 × 1) / 5 = $90/5 = $18.00/M
- With cache (80% hit): ($10 × 0.2 + $1.00 × 0.8) × 4/5 + $50 × 1/5 = $2.80 × 0.8 + $10 = ~$4.60/M
