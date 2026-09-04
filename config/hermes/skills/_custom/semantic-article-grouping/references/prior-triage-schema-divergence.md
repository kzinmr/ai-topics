# Prior Triage Schema Divergence (Supplement Pattern)

When a prior triage run exists but only partially covered the checkpoint (e.g., 4 decisions out of 20 items), you must supplement with new decisions for the remaining items.

## Schema Divergence Observed

The prior triage may use a **different JSON schema** than the current one:

| Field | Prior Schema | Current Schema |
|-------|-------------|----------------|
| `item_id` | **Missing** | Present (e.g., `"blog-4"`) |
| `source` | **Missing** | Present (`"blog"`) |
| `star_rating` | **Present** (integer, e.g. `5`) | **Absent** — stars inline in `reason_ja` |
| Identifiers to use | `title` + `raw_path` | `item_id` |

## Safe Dedup Approach

When reading the prior triage, use safe field access — do NOT assume `item_id` exists:

```python
# WRONG — crashes if prior schema lacks item_id:
prior_ids = {d['item_id'] for d in prior['decisions']}

# RIGHT — fall back to title for dedup:
prior_titles = {d['title'] for d in prior['decisions']}
prior_raw_paths = {d.get('raw_path') for d in prior['decisions'] if d.get('raw_path')}
```

## Full Replacement, Not Supplement

Save the new triage file as a **complete replacement** of `triage_latest.json` (prior decisions + new decisions combined), not as a separate supplement file. The downstream pipeline reads `triage_latest.json` as a single authoritative batch. Do NOT create a separate `triage_supplement.json`.

Use `star_rating` if present in prior decisions — convert it to the ★★★★★ inline format for the new schema, or preserve it as-is if the downstream reader expects it.

## Observed June 2026

- Prior triage run: `20260626T070016Z` — 4 decisions with `star_rating` field, no `item_id`/`source`
- First attempt to dedup by `item_id` failed with `KeyError`
- Fixed by switching to title-based dedup
- 16 new decisions saved alongside 4 prior decisions in single `triage_latest.json`
