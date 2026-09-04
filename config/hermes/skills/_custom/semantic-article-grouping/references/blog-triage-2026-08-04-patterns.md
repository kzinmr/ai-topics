# Blog Triage Patterns — 2026-08-04 Session

## Batch composition shifts take yield (4/18 ≈ 22%, well above the ~5% median)

The "typical yield" of ~5% takes in blog triage is a median for batches dominated
by individual-author opinion blogs. Mixed batches with these source types produced
genuine takes at ~22%:

- **Daring Fireball-linked vendor technical explainers** (WorkOS "MCP vs. REST", 20KB):
  substantive, well-structured technical content that fills real concept-page gaps
  (concepts/mcp.md lacked an explicit REST-vs-MCP comparison section).
- **Security-practitioner guides** (Micah Lee "Agentic coding techniques", 10KB):
  detailed practitioner workflows (local Ollama + qwen3-coder, Matt Pocock LLM skills,
  Docker sandboxes, repo-scoped PATs, signing-only SSH keys) that are genuine gaps in
  the author's entity page (micahflee.md had zero agentic-coding content).
- **Editorial-substack critical analysis that arrives via the blog pipeline**
  (Gary Marcus on OpenAI Astra): follow-up articles with new data points.

Do NOT treat high take counts in such batches as over-scoring; verify each take has
concrete body content and a real wiki gap (BODY-READING MANDATE), then trust the yield.

## Follow-up-article gap: entity created from author's earlier piece ≠ coverage of the follow-up

`entities/openai-astra.md` was created 2026-08-03 from Gary Marcus's previous Astra
critique. Marcus's next-day follow-up ("Two critical updates re: Astra and mathematics")
carried entirely NEW facts: Anthropic's Levent Alpöge replicated ~half of Astra's results
with the public Fable model within 24h, Noam Brown admitted failures without reporting them
("numerator without denominator"), and Terence Tao's 7/26 lecture on "proof indigestion".
Same author, same subject, page exists → looks covered; actually a genuine take because the
specific claims are absent. Test: does the page contain the SPECIFIC new datapoint
(replication result, failure-rate critique, new lecture)?

## Archive script prints a symlink-resolved path — don't "fix" it

`archive_triage.py blog --keep-reference` printed
`"archive_path": "/opt/data/.hermes/home/ai-topics/wiki/raw/archived/triage/blog/2026-08-04_....json"`.
This LOOKS like the nested-path pitfall (`~/.hermes/home/.hermes/...`) but is correct:
`/opt/data/.hermes/home/ai-topics` is a symlink to `/opt/data/ai-topics`, so the file lands
in the canonical `wiki/raw/archived/...` tree. Verify with `ls` on BOTH paths (same file),
then `git add` the canonical path. Do not re-run or hand-copy the file.

## Broken wikilink detection during triage

While cross-referencing, `entities/dwarkesh-patel.md` referenced
`[[concepts/compute-pricing]]` — no such page exists (broken wikilink). Triage is a good
place to catch these: when a candidate routes to a concept/entity, check whether the
referenced page exists. Note it in the report as a wiki-health follow-up candidate rather
than fixing it in triage (triage is read-only per the skill; downstream wiki-ingest and
wiki-health-fix handle repairs).
