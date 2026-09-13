# Local AI Registry (0xSero/local-ai-registry)

- source: https://github.com/0xsero/local-ai-registry
- shared_by: [[entities/sero]] (@0xsero) — X post 2026-09-13T17:05:32Z ("Already done", replying to @MiaAI_lab)
- also_published_as: Omarchy community plugin `sero.local-ai` (https://plugins.omarchy.org/plugin.html?id=sero.local-ai) — "Omarchy will be a beautiful home. Local AI" (2026-09-13T21:47:26Z)
- fetched: 2026-09-13
- status: 200

## Summary

Local AI registry: one validated recipe per machine, with the evidence attached.

A **hardware-aware registry of local model artifacts, launch recipes, measured speed sweeps, and public quality leaderboards**. The standalone registry is *data first*: clients can read it from disk, serve it as static JSON, or resolve it over any static HTTP host.

### Structure (progressive-disclosure rule: index → choice → exact record)

`registry/index/` holds discovery shards a client fetches only what its question needs:
- `collections.json` — ids + counts for every collection
- `recipes.json` — compact recipe rows for filtering
- `recipes-by-hardware.json` — hardware_id → [recipe ids]
- `instances-by-model.json` — model_id → [model-instance ids]
- `benchmarks-by-model.json` — model_id → [leaderboard score rows]
- `hardware-speed-evidence.json` — hardware_id → aggregated sweep evidence

Collections: `hardware/`, `model/`, `model-instance/`, `recipe/` (artifact × hardware × engine compatibility unit), `speed-sweep/` (measured inference evidence), `benchmark/` (scraped public leaderboard scores), `price/<product-id>/` (regional retailer observations), `asset/` (engine configs/patches).

Shared contract defined twice: JSON Schema under `registry/schema/` and TypeScript interfaces in `registry/schema/types.ts`.

### Trust boundary

- **validated** — model revision and runtime are pinned and the launch contract has acceptance evidence.
- **candidate** — registry has useful compatibility or speed evidence but cannot yet promise a reproducible launch. LocalMaxxing, local.ai Postgres, and mlx.fast imports are always `candidate` with `launch.kind: "reference"`.
- Promotion to `validated` requires a separately curated, pinned recipe and a real completion plus speed acceptance.
- Regional price records are observations, not universal hardware values.

### Hardware coverage

Apple M1–M5 families at supported memory tiers (Pro/Max/Ultra actually shipped); GeForce RTX 30/40/50; NVIDIA workstation accelerators; four current AMD local-AI targets; Intel Arc workstation cards; audited server/workstation classes. Apple product names are discovery aliases; compatibility keys are chip + unified-memory capacity.

### Website & API

Next.js app reads `registry/` directly at runtime (no second dataset). Read-only versioned JSON API under `/api/v1` (GET/HEAD only; mutations get 405 — no write path). Routes: `/api/v1/index`, `/api/v1/facets`, `/api/v1/models`, etc.

## Notes

Related to Sero's broader "Freedom Tech" / local-AI mission ([[entities/sero]]). Connects to the local.ai benchmark work already documented there and to the local-vs-cloud AI policy debate ([[concepts/open-weight-ai-regulation]], [[concepts/ai-regulation-2026]]).
