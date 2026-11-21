# X Activity Log sections: authoring rules

Learned across x-accounts-scan runs; the scan procedure itself lives in
`wiki-ingestion-pipelines` → `references/x-accounts-scan-cron.md`. This file is
about how to write the `## X Activity Log` section on a person's entity page.

## One dated section per month

- Single `## X Activity Log (<Mon> <Year>)` per month, bullets in date order.
- Place it at the end of substantive content — before `## Notable Quotes &
  Statements` / `## Related` / `## Sources`. Create it if absent.
- Do NOT mint one `##` per topic, and do NOT scatter activity bullets into
  career/project sections. Non-AI posts from an AI person still get one dated
  bullet, in a topical `###` sub-section, marked "(logged only; no new page)".

## Fold same-substrate posts from one author

Two posts a day or two apart that share a product/substrate are ONE story, not
two entries-plus-a-page. Verified example (2026-11-15, `entities/chris-tate.md`):

- Nov 13 — bare "Interesting" + `ui-sdk.dev/docs/agents/connect-an-agent/webmcp`
- Nov 14 — SPEC-01/HARDWARE, 61 hardware components w/ haptics+sound, shadcn
  registry, by @shuding

Both are the **Vercel UI SDK / shadcn registry** layer. Written as one section,
each bullet cross-referencing the other, so the reader sees the agent-facing end
(WebMCP: a site's typed React catalog *is* its tool surface) and the
human-facing end (a themed component gallery) of the same substrate.

Fold signal: the scan's `links[].description` fields share a product name.

## Bullet shape

```
- **<Mon> <Day> — [<title>](<url>):** <author's framing quoted verbatim>.
  <substantive facts: numbers, prices, install commands, rollout surfaces>.
  See [[concepts/<canonical-page>]].
```

- Quote the author's own words whenever they carry judgment — "Interesting",
  "It became my daily driver", "turning sound on and pressing buttons is so
  satisfying 😌". The person's stance is the whole point of an entity page;
  the facts belong on the concept page.
- Keep install commands verbatim (`npx skills add ...`, `npm i tsc-ts`).
- **Self-links are dangling-by-construction.** Inside `entities/chris-tate.md`,
  use a heading anchor `[[#Key Projects|json-render]]`, never
  `[[entities/chris-tate|json-render]]`. Same for pointing at a sibling bullet:
  `[[#X Activity Log (Nov 2026)|WebMCP]]`.

## A bare-links reply usually has its payload one hop up

`referenced_tweet_types: ["replied_to"]` or `["quoted"]` + a text body of only
links ≠ thin post. Fetch the parent:

```
xurl --auth oauth2 "/2/tweets/<PARENT_ID>?tweet.fields=note_tweet,created_at,referenced_tweets,entities" > /tmp/xscan/parent_<ID>.json
```

then read it in a SEPARATE call with `python3 -c "import json; ..."` (never pipe
xurl into an interpreter — HIGH security block in cron). Handle `data` being a
dict on the single-ID endpoint.

Worked case (2026-11-15): @_philschmid's post was literally "Try it in AI Studio:
<link> What's new & migration guide: <link>". The `replied_to` parent carried
the entire substance — beats Argon on Artificial Analysis, 57% Terminal-Bench
4.0, 4 thinking levels, $1.50/$7.50 + free tier, rollout to Antigravity / Gemini
App / Google Search. Judging the post by the scan snippet would have skipped it.

## The person's framing vs the wiki's existing finding

- `grep -rn "<slug-or-url>" wiki/` before writing. If a concept/event page
  exists, the entity bullet is a **pointer carrying the person's take**, not a
  re-summary. Concept page owns facts; entity page owns stance.
- If the person's framing **contradicts** the page's existing finding, soften
  neither. Add `## <Vendor> <role> framing (contested: <axis>)` to the concept
  page keeping BOTH with dates and an explicit note on which measurement axis
  each used. Worked case: `concepts/gemini/gemini-4-hydrogen.md` — Schmid's
  "outperforms Argon on Artificial Analysis" (blind-preference arena) beside
  Simon Willison's "quite stark quality drop" (pelican-SVG generation grid).
  Different axes, so both stand; the reader is told how to weight them.
- Also refresh the person's `wiki/index.md` blurb with the newest notable
  activity. A richly-updated page with a 3-month-old blurb is undiscoverable.
  A blurb-only refresh changes no `## Section (N pages)` count — leave headers
  alone and say so in the log entry.

## Duplicate entity pairs — verified list (patch the RICH one)

`build_x_wiki.py` created bio-only `entities/<handle>.md` stubs that coexist with
full `entities/<full-name>.md` profiles. Always `ls wiki/entities/ | grep -i
<name-or-handle>` and patch the page with real content:

| Rich (patch this) | Stub (leave alone) |
|---|---|
| `philipp-schmid.md` (~199 lines) | `phil-schmid.md` |
| `samuel-colvin.md` | `samuelcolvin.md` (206 bytes) |
| `lance-martin.md` | `rlancemartin.md` |
| `kyle-corbett.md` | `kyle-corbitt.md`, `corbett.md` |

- `wiki/index.md` may keep a stub line (`[[entities/phil-schmid]] — Philipp (Phil)
  Schmid`) beside the rich entry. That's expected — don't "clean it up" mid-scan.
- Check for `Redirect → [[entities/...]]` stubs in `index.md` to learn the
  canonical target. Never add a third variant.
- A bad `patch` anchor can silently land on the stub; verify with
  `git show --stat HEAD` that the file you meant to change is the one that moved.
