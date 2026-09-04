# Newsletter Triage Patterns — 2026-08-10 Batch

6 newsletters / 106 links → 6 takes, 1 reference, 9 skips (16 decisions). Validated learnings from this run:

## 1. Inbox summary can be wrong about PAGE EXISTENCE (create vs update)

The 2026-08-10 inbox pre-triage summary classified "Claude Code 5." (aibyaakash) as `wiki_targets: [entities/claude-code (create or update)]` with reason "No existing Claude Code entity page found — this could seed one."

**Reality**: `entities/claude-code.md` existed (updated 2026-08-09) plus `claude-code--architecture.md`, `claude-code--capabilities.md`, `claude-code--history.md`, and a whole `concepts/claude-code/` subdirectory (steering-methods, skills, etc.). The summary's "no existing page" claim was simply wrong — it doesn't check disk.

**Rule**: inbox `wiki_targets` and create-vs-update recommendations are advisory guesses. Before accepting a `create`, verify: `ls wiki/entities/ | grep -i <name>` and `ls wiki/concepts/ | grep -i <name>`. Downgrade create→update when pages exist. This is distinct from the existing "topic estimation wrong" admonition (The AI Cursor Arrives → DeepMind mouse) — it's about the *coverage/existence claim*, not the topic guess.

## 2. read.getsuperintel.com (uid=443) pages have NO `<article>` tag — use body-level `<p>` extraction

Eve CEO interview beehiiv link resolved HTTP 200 to `read.getsuperintel.com/p/exclusive-interview-with-the-co-founder-ceo-of-eve-jay-madheswaran` (~16h after send, Aug 9 18:41 → Aug 10 10:40).

- HTML 783KB; `re.search(r"<article[^>]*>(.*?)</article>")` → **no match** (unlike Substack posts).
- Fallback that worked: body-level `<p>` regex → 150 `<p>` tags, 76 substantive paragraphs (>60 chars), full interview content including funding/product metrics.
- So for uid=443: skip the `<article>` extraction step and go straight to body `<p>` extraction.

## 3. Redirect-stub canonical domains — three new validations

`open.substack.com/pub/{pub}/p/{slug}` returned 1.3KB stubs for all 5 posts; `<title>` held the canonical URL (`?triedRedirect=true`). Newly validated canonical domains (previously unlisted):
- `www.interconnects.ai` (from `pub/robotic` — robotic = Interconnects, Nathan Lambert)
- `www.aibyaakash.com` (from `pub/aibyaakash`)
- `newsletter.semianalysis.com` (from `pub/semianalysis`)

## 4. Batch composition note — The Signal (editorial roundup) higher yield

The editorial-roundup expectation (~85-90% skip) did NOT hold for this issue: The Signal produced 2 takes (Hark Handoff product, ByteDance Seedance 2.5) + 1 reference (Google TPU×Anthropic stats) out of ~5 content sections. Both takes were genuinely new product/model announcements with concrete specs (pricing $0.18/M vs $5.00/M, 30s single-pass video, 10T-param FT report). Google leadership reshuffle section was already covered (`entities/jeff-dean.md` Discovery Loop, `entities/demis-hassabis.md` chair role, `entities/discovery-loop`). Consistent with the "composition shifts yield" caveat — verify each section against disk rather than assuming roundup = all skip.

## 5. Superintel+ interview as take source

The Eve interview (uid=443) produced a take for a NEW entity (`entities/eve-legal-ai.md`) — legal-AI agent company, $103M Series B, $1B+ valuation, EveOS, multi-agent architecture (Atlas/Jenny/Auditor/Analyst). Precedent: `entities/harvey.md` exists for the same vertical. Note the naming trap: `entities/vercel-eve.md` is a DIFFERENT Eve (Vercel's agent framework) — verify identity before assuming the entity exists/doesn't.

## Decisions summary (for downstream cross-reference)

- Take: SemiAnalysis TileRT InferenceX → `entities/tilert.md` (independent benchmark: 340 tok/s/user B200 @8k/1k, 1.9× GB300 NVL72)
- Take: aibyaakash Claude Code 5 setup → `concepts/claude-code/claude-code-steering-methods.md` (80% system-prompt deletion, safe-mode baseline, CLAUDE.md→skills migration, session-to-session messaging)
- Take: Interconnects "Lessons from the hacks" → `events/openai-huggingface-incident-july-2026.md` (Nathan Lambert 10 takeaways: persistence axis, user-intent axis, sub-agent swarms in RL)
- Take: Hark Handoff → `entities/hark.md` (computer-use agent, $0.18/M pricing, 15s→5s per-turn)
- Take: Seedance 2.5 → `entities/bytedance.md` (30s single-pass video+audio, 10T pre-training report)
- Take: Eve interview → `entities/eve-legal-ai.md` (new)
- Ref: Google TPU×Anthropic stats → `entities/google.md` (>20% TPU shipments to Anthropic, $150B backlog, Cloud +82%)
