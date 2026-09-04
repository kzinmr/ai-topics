# Two-beat story gap: person-departure pages exist, new-company page is the gap

Validated 2026-08-06 (AINews: DeepMind departures → Discovery Loop founding).

## Pattern
Story shape: (1) official announcement "X departs lab Y" (company blog), then (2) next-day bulletin/newsletter reveals "X founds company Z" with the full founder roster + mission.
- Beat 1 → entity pages for the PERSON and the LAB get created/updated (e.g. `entities/jeff-dean.md`, `entities/deepmind.md` from Google blog, Aug 5 2026)
- Beat 2 (newsletter) → the NEW COMPANY (name, co-founders, mission) is a **separate entity page** — check with:
  ```bash
  grep -rilE "<company-name>" entities/ concepts/ events/
  ```
- Zero hits = genuine take for a new entity, even when every person page was freshly updated (`updated: yesterday` ≠ company covered)

## Concrete case
- Beat 1 (Aug 5): Google blog — Jeff Dean + Sanjay Ghemawat leave to launch an independent PBC. Wiki: `entities/jeff-dean.md`, `entities/deepmind.md` updated.
- Beat 2 (Aug 6, AINews): company named **Discovery Loop** (@DiscoLoopAI, Public Benefit Corporation), mission "automate machine research"; co-founders also include **Oriol Vinyals + Quoc Le** (absent from wiki). Demis→Chair, Koray→SVP already covered — not the gap.
- Check: `grep -rilE "discovery loop|discoloop" entities/ concepts/ events/` → 0 hits → take.
- Outcome: create `entities/discovery-loop.md` + enrich jeff-dean.md / deepmind.md (add company name, full founder list, mission).

## Reuse
For any "person departs to found startup" story: after checking the person/lab entity pages, ALWAYS grep for the startup's name before deciding. The newsletter delta is usually the **company identity** (name, full co-founder roster, mission), not the departure itself.
