# Newsletter Triage — 2026-08-01 batch (3 newsletters) — session patterns

Validated in a 3-newsletter batch (The Signal "The End of Prompting", Superintel+ "DeepSeek Answered OpenAI's Price Cut Overnight", AINews "not much happened today"). Run 20260801T101509Z.

## Beehiiv previous-day link resolved 200 (counter-example to 403-expiry rule)

- Newsletter: Superintel+ (uid=443), sent Jul 31 15:52 UTC, resolved Aug 1 ~10:20 UTC (~18.5h old).
- Single test link returned **HTTP 200** and followed the redirect chain to `read.getsuperintel.com/p/deepseek-answered-openai-s-price-cut-overnight` — full article, 55 `<p>` paragraphs extracted.
- The "previous-day beehiiv links ALL 403" rule (observed Jun 7/Jun 14) is **publication-dependent**, not time-universal. uid=443 (Superintel+) keeps tokens alive 16-24h+ — same profile as uid=386 (getsuperintel.site).
- **Decision procedure that worked**: test ONE link from the batch. If 200 → the batch is resolvable; resolve Link 1 (main article) + sample links normally. If 403 → skip straight to inbox summary. Trust the test verdict, not the age heuristic.

## Third getsuperintel domain: read.getsuperintel.com

Domain map for Superintel family (confirmed Aug 1, 2026):

| Domain | Role |
|--------|------|
| `getsuperintel.com` | Framer marketing site (direct /p/ URLs 404) |
| `getsuperintel.site` | beehiiv-hosted publication (canonical post pages, uid=386) |
| `read.getsuperintel.com` | **Article content domain for Superintel+ (uid=443)** — where beehiiv tracking links land after redirect |

When a Superintel+ beehiiv tracking URL resolves, expect the final URL on `read.getsuperintel.com`. `title` + `len` + `<article>` paragraph extraction works normally there (no Cloudflare challenge observed in this run).

## Triage outcome summary (for reference on yield expectations)

- 60 links across 3 newsletters → 17 decisions: 1 take, 8 reference, 8 skip.
- Takes are rare in editorial roundups (The Signal): only the standalone concept article ("The End of Prompting" — prompt→demonstration paradigm shift) qualified as take, because `concepts/prompt-engineering.md` was a 26-line stub and `entities/anthropic.md` lacked "Record a Skill" while `entities/openai-codex.md` already had Record & Replay (partial coverage — check both sides).
- Cross-pipeline dedup hit: DeepSeek V4-Flash 0731 was ALREADY a blog-triage `take` same-day (simonwillison article, triage_latest.json 2026-08-01T10:15:00Z). Both newsletters covering it (Superintel+, AINews) were downgraded to `reference` with `candidate_wiki_path: entities/deepseek` (entity lacked 0731-specific section — grep for "0731" in entities/deepseek.md returned nothing).
- Fully covered → skip: Anthropic/OpenAI sandbox escapes (`concepts/anthropic-cybersecurity-eval-incidents.md` + `events/openai-huggingface-incident-july-2026.md`), Inkling-Small (`entities/thinking-machines-lab.md` Inkling section), Gemini Robotics 2 (`concepts/vla-models.md`), AWS financials (non-AI).
- Genuine gaps → reference: Microsoft Echoverse (zero wiki mentions), MiniMax H3 (entity had only M2.7), LangChain DeepAgents, Gemini 3.6 Flash, Seedance 2.5, MAI-Cyber-1-Flash (zero mentions).

## Pitfall: archive_triage.py nested path is a symlink artifact — verify before "fixing"

- `archive_triage.py newsletter --keep-reference` printed `archive_path: /opt/data/.hermes/home/ai-topics/wiki/raw/archived/triage/newsletter/2026-08-01_20260801T101509Z.json` — the nested `~/.hermes` expansion path.
- **BUT** the file ALSO exists at the canonical `/opt/data/ai-topics/wiki/raw/archived/triage/newsletter/2026-08-01_20260801T101509Z.json` because `/opt/data/.hermes/home/ai-topics` is a symlink to `/opt/data/ai-topics` (defense-in-depth from AGENTS.md).
- **Lesson**: when a script reports a nested `.hermes/home/...` path, run `readlink -f` on the nested parent or `ls` the canonical path BEFORE assuming a wrong-path problem. In this environment the nested path is often the same file via symlink. The documented expanduser pitfall applies to scripts that BUILD paths via `os.path.expanduser` and only save there — archive_triage.py saves to the real wiki and merely REPORTS the symlink-resolved path.

## Pitfall: `python3 | python3` pipe also blocked by scanner

- Attempting `python3 scripts/archive_triage.py ... | python3 -c "..."` (to pretty-print archive output) was blocked by `tirith:pipe_to_interpreter` — the scanner flags ANY pipe-to-interpreter, including python→python, not just `cat | python3` or `curl | python3`.
- **Lesson**: never pipe a python script's output into `python3 -c`. Verify by running the script first (capture output), then a separate `python3 -c "import json; ..."` call with a hardcoded path, or `ls`/`read_file` the output file directly.
