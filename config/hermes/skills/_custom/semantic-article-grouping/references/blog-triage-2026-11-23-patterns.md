# Blog-triage patterns — 2026-11-23 (run 20261123T100944Z)

Batch: 12 candidates + 3 unsaved_articles. Yield: 3 takes / 5 references / 4 skips.

## Model-release / model-behavior-announcement cluster

One frontier-lab announcement often arrives in the SAME batch as both the official post AND
third-party commentary. The two have opposite dispositions — do not treat them alike:

- **Official company post that 403s and was already recovered as an RSS-fallback stub**
  (`scrape_status: rss-fallback`, body = 1-sentence RSS description) → **reference**, attached as a
  `sources` entry on the richer commentary's page. Never a solo `take` — body insufficient for the
  BODY-READING MANDATE. Check today's `log.md` FIRST: the pre-run blog-ingest job usually logs the
  recovery itself (observed: `openai.com/index/perplexity-and-intelligence` recovered via
  `openai.com/news/rss.xml` at 10:00, triaged at 10:10 — already cross-referenced against the Goedecke
  companion piece). Downgrading it to reference avoids a duplicate take.
- **Independent analyst commentary on the same release** carrying concrete analytic claims (specific
  model bases, scaling inflection points, "contradicts the common wisdom") → **★★★★☆ take as
  existing-page update**, with the official stub attached as a source.

Concrete pair this session: OpenAI "Perplexity and Intelligence" (stub → reference) + Sean Goedecke
"Notes on OpenAI's perplexity reveal" (→ `concepts/scaling-laws.md` update). Goedecke's body held the
durable content: few models share the same base (4o/4.1 reuse rumor disproved, only o1 and o3), GPT-4.5
as the visible "gave up on large pretraining" inflection (same perplexity as GPT-5.3-Codex but far less
useful), perplexity re-accelerating from GPT-5.2 contradicting the "labs are all-in on RL" wisdom, and
the caveat that perplexity only measures pretraining, not RL / CoT-improvability / sycophancy.

## Coverage test for AI-for-math news (grep recipe)

Before rating a claimed AI math breakthrough:

1. `grep -ril "<theorem-name>" entities/ concepts/ events/` — rich sibling coverage is NOT coverage.
2. `ls entities/ | grep -i <researcher-name>` — 0 hits = greenfield person entity page.
3. Distinguish **bound-improvement vs full proof**, and **umbrella coverage vs this specific result**.

Validated case: Gary Marcus on Levent Alpöge proving the Riemann Hypothesis with Claude → ★★★★★ take to
`concepts/ai-mathematics-theorem-proving.md`. Existing rich pages that did NOT cover it:
`entities/anthropic.md` had the Aug 2026 RH *lower-bound* improvement (zeta zeros on the critical line
41.6%→67.2%, "does not expect these techniques to prove RH") and
`concepts/openai/formal-math-publication-2026.md` had the 722-paper Lean 4 program. Neither covered a
claimed full proof, the 250,000-page non-elegant result, the Lean+mathlib (2M+ lines)
formal-verifiability dependency argument limiting generality beyond math, the DeepBlue-Kasparov 1997
analogy, or the flat Anthropic after-hours stock reaction. `entities/levent-alpoge` absent. Terry Tao's
existing quote ("It's not going to prove the Riemann Hypothesis anytime soon") makes it a direct
contradiction-with-existing-claim — enrich as a dated/contested subsection, do not overwrite.

Related non-take: an entity page that already documents the author's AI usage stance can still warrant
only a reference when the article's AI angle is a single usage example. Troy Hunt's breach-disclosure
post (17KB) was Claude-authored from 8.5 years / 73 notifications of his HIBP mailbox — valuable as a
concrete AI-usage data point for `entities/troy-hunt.md`, not a new concept.

## Author-opinion batch-skip guardrail (geohot counter-example)

Short (2.2KB) opinion posts are NOT auto-skips. geohot's "the singularity is nearer (slopcore)" was a
legit ★★★☆☆ entity update because the body carried specific, quotable positions absent from
`entities/george-hotz.md`: rejection of the orthogonality thesis ("hogwash"), "naive doomer is a fool",
GPU-10,000 deregulation, and "GPT-6.2 can micro program better than me — not just faster, the first
model to". The existing page covered only tinygrad/liberation philosophy. Test = does the body contain a
NEW stance/datum, not its length.

Converse (true skips despite length): jyn.dev "unpublished blog posts" (33KB) is an idea-fragment dump
(Rust lifetimes, Clojure/Julia, CI-in-Clojure) with zero AI content → skip. MaskRay's LLVM
`llvm::cl`→TableGen migration (16KB, 2,860→1,070 options) is compiler infrastructure with no ML content
despite LLVM being AI-tooling substrate → skip.

## Cheap pre-save verification (keep doing it)

Before saving, assert every non-skip `raw_path` exists on disk and every decision has non-empty
`body_excerpt`/`reason_ja`, and `os.path.exists()` each `candidate_wiki_path` under the ABSOLUTE
`/opt/data/ai-topics/wiki/` root (cwd-relative gives false negatives). All 7 paths verified this run.

Builder hygiene that worked first try: `write_file` to `/tmp/blog_triage_<runid>.py` (unique filename,
CJK reasons, no heredoc), `python3 -c "import ast;ast.parse(...)"` gate, `"*" * stars` not the star
glyph, `None` not `null`, dedup by `item_id` (not URL — batch entries share empty URL), sort
take→reference→skip. `archive_triage.py blog --keep-reference` then targeted `git add` of ONLY the
archive file + `archive_index.json` (working tree had unrelated dirty `raw/newsletters/` + skill files —
never blanket-add).

## SKILL.md size note

SKILL.md hit the 100,000-char cap this session (a direct `patch` to it failed with
"content is 101,689 characters (limit: 100,000)"). New dated pattern refs MUST go in `references/` and
be pointed to from the existing "Recent dated pattern refs live in ..." glob pointer, not appended to
SKILL.md. A future curation pass should move some inline dated paragraphs (e.g. the Nov-18 block in
"Key Patterns to Recognize") into references to reclaim headroom.
