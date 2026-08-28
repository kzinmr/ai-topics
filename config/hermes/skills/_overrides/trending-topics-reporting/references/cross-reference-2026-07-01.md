# Cross-Reference Worked Example — 2026-07-01

> Normal-volume day: 104 RSS articles + 83 raw articles in 3 days.
> 30 trending topics detected; most counts concentrated on entity names (Claude 19, Anthropic 14, OpenAI 13).
> Key pattern: multiple launch events + economic debate + conference coverage + MCP ecosystem expansion.

## Step 1: Scan `trending_topics.py` Raw Output

```
Hot topics (4+ sources):
  Claude (19), Anthropic (14), evals (14), OpenAI (13), Simon Willison (12),
  MCP (9), Cursor (7), GPT (7), Google (7), Meta (6), coding agents (6),
  open-source AI (6), Gemini (5), long context (5), agentic engineering (4)
```

**Flagged as noise**: Claude (19), Anthropic (14), OpenAI (13), Simon Willison (12), Google (7), Meta (6) — all generic entity names. These are background baseline, not signal.

**Kept as candidates**: MCP (9), Cursor (7), GPT (7), coding agents (6), open-source AI (6), Gemini (5), long context (5), agentic engineering (4).

## Step 2: Group Blogwatcher DB Titles into Event Clusters

Queried with a broad AI keyword list. Key clusters found:

| Cluster | Articles | Sources | Verdict |
|---------|----------|---------|---------|
| **Claude Sonnet 5 launch** | 3 (Simon Willison, Harvey, quote) | Cross-source | ★★★★★ Signal — new model release |
| **Ornith-1.0 coding agent** | 1 (Simon Willison) + trending_topics "coding agents" | Raw article | ★★★★☆ Signal — novel open-source approach |
| **AI bubble/BIS warning** | 2 (wheresyoured.at, Gary Marcus) | Cross-source | ★★★★★ Signal — BIS institutional warning |
| **MCP ecosystem expansion** | 4 (Merge Blog: Stripe/Freshdesk MCP × Cursor/Codex) | Single-source volume | ★★★★☆ Signal — ecosystem standardization |
| **Voyage Context-4** | 1 (Voyage AI Blog) | Raw article | ★★★★☆ Signal — technical step-change |
| **AI Engineer Conference** | 13 (AI Engineer YouTube) | Single-source volume | ★★★★☆ Signal — conference knowledge dump |
| **Arena $100M ARR** | 1 (Arena Blog) | Single blog | ★★★☆☆ Signal — business milestone |
| **Enterprise AI (HP+OpenAI, Augment Code, Sierra)** | 4 (OpenAI, Augment Code, Sierra, Pluralistic) | Cross-source | ★★★☆☆ Signal — multiple parallel announcements |
| **Gemini vs Search** | 1 (Cory Doctorow) | Single essay | Minor — editorial, no new product |
| **Ray Data 2.56** | 1 (Anyscale) | Single blog | Minor — incremental update |

## Step 3: Cross-Reference Against Raw Article Files

Ran `find` for raw articles by keyword. Key findings:
- **Claude Sonnet 5**: ✅ Found (simonwillison + Harvey + Modal articles)
- **Ornith-1.0**: ✅ Found (simonwillison article)
- **Voyage Context-4**: ✅ Found (blog.voyageai.com hash-suffixed article)
- **AI Compass**: ✅ Found (simonwillison article, but turned out to be a quiz, not impactful)
- **Arena $100M**: ❌ No raw article — had to `curl` scrape (had SSR content, worked)
- **Ramp Agentic Risk Ops**: ❌ No raw article — SPA, `curl` failed
- **Augment Code analyst**: ❌ No raw article — SPA, `curl` failed
- **wheresyoured.at essay**: ✅ Found (multiple raw articles exist)

**Active-crawl output**: Not found (pipeline probably off). Used blogwatcher DB + raw articles as sole sources instead.

## Step 4: Select Top 7

After dropping generic entity noise, incremental updates (Ray Data 2.56), and minor editorial pieces:

1. **Claude Sonnet 5** — ★★★★★ — new model, concrete spec changes, immediate enterprise adoption
2. **Ornith-1.0** — ★★★★☆ — novel open-source approach to agentic coding
3. **AI investment sustainability (BIS)** — ★★★★★ — institutional warning on $1T+ capex
4. **MCP ecosystem** — ★★★★☆ — SaaS integration pattern becoming standard
5. **Voyage Context-4** — ★★★★☆ — embeddings leap with auto-chunking
6. **AI Engineer Conference** — ★★★★☆ — 13 talks on agent productionization
7. **Arena $100M** — ★★★☆☆ — business milestone, student project → $100M

**Clusters combined**: Enterprise AI topics (HP, Augment Code, Sierra) merged into one lower-ranked entry (#8).

## Key Discrepancies

- **Blogwatcher vs raw articles**: Arena blog, Ramp, and Augment Code had RSS entries but no raw files — the blog-ingest pipeline either didn't reach them or they failed fetching. Always verify raw article existence before assuming you can deep-read.
- **SPA extraction**: Arena (Ghost blog, SSR) yielded content via `curl` + `re.sub()` stripping. Ramp Builders and Augment Code (likely SPA) yielded only "enable JavaScript" — no recourse without `web_search` or `delegate_task`.
