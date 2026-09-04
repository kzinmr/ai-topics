# Import AI (Jack Clark) — Extraction Pattern

**Publication**: Import AI, written by Jack Clark
**Substack ID**: `publication_id=1317673`
**Domain**: `importai.substack.com`
**Post URL pattern**: `https://importai.substack.com/p/import-ai-{NUMBER}-{slug}`
**Open URL**: `https://open.substack.com/pub/importai/p/import-ai-{NUMBER}-{slug}`
**`isAccessibleForFree`**: `true` (free, no paywall)
**Typical volume**: 20 email links (2 content + 18 UI noise)

## Content Structure

Import AI is an **editorial roundup newsletter** where each issue covers 5–15 external links with 1–3 paragraph editorial intros. Unlike The Signal (longer analysis per link), Import AI intros are very short — typically 1-2 sentences framing why the linked article matters.

### Typical Issue Topics
- AI capability benchmarks (Epoch/METR papers, frontier model evals)
- Robotics + AI (Project Fetch, embodied agents)
- AI safety and alignment (OpenAI safety papers, Anthropic research)
- Open vs closed model debates
- Regulation and policy developments
- Economic analysis of AI industry

## Body Extraction Characteristics

| Property | Value |
|----------|-------|
| JSON-LD `body_html` | Empty — no body in JSON-LD |
| JSON-LD `description` | Present (~100-200 chars, useful for triage) |
| `<article>` paragraph count | ~4-15 substantive paragraphs |
| Paywall | None — fully free |

### Confirmed Extraction (July 2026)
The `<article>` tag paragraph extraction from `importai.substack.com` yields approximately 4 paragraphs of substantive editorial content, plus 15+ external links from the full post body. The linked articles themselves (epoch.ai, anthropic.com, openai.com) are the primary content — the newsletter body provides framing context.

## Link Profile (per issue)

From a typical 20-email-link Import AI issue:
- **Link 1** (index 0): OAuth redirect (`redirect/2/eyJ...`) → Skip
- **Link 2** (index 1): `app-link/post` → The newsletter post URL → Take (resolve this)
- **Link 3** (index 2): `@importai` → Author profile → Skip
- **Links 4-8** (indices 3-7): Like/comment/share/app-store/restack UI → Skip
- **Link 9** (index 8): Subscribe redirect → Skip
- **Links 10-20** (indices 9-18): UUID redirect links (`substack.com/redirect/<uuid>`) → Skip (require email session auth)

**Surviving URL**: The newsletter post URL from Link 2 is the only content-bearing URL.

## Post Page Links (external)

After resolving the post page HTML, the external links are in the main content area. Key patterns to look for:

| URL Domain | Type |
|------------|------|
| `epoch.ai/*` | AI capability measurement / benchmarks |
| `github.com/epoch-research/*` | Benchmark code repos |
| `anthropic.com/research/*` | Anthropic capabilities research |
| `openai.com/index/*` | OpenAI research / policy |
| `jack-clark.net/*` | Previous Import AI issues |
| Various company blogs | Original article content |
| YouTube links (`youtube.com/watch?v=*`)| Talk videos |

## Triage Priority Assessment

- **Genuine take rate**: Low (~1-2 per issue). Most topics Import AI covers are already in the wiki from other pipelines (sitemap-monitor captures official announcements; blog-ingest captures commentary). Import AI adds unique value only when covering niche benchmarks or linking to early-stage research papers.
- **Typical reference rate**: Medium (~2-3 per issue). The editorial framing often adds perspective worth noting in entity pages or concept pages.
- **Cross-pipeline overlap rate**: High (~70-80%). Import AI's curated links are typically official blogs (Anthropic, OpenAI, Epoch) already captured by sitemap-monitor at 06:00 UTC.

## Cross-Reference

- See `references/editorial-roundup-per-article-triage.md` for the per-article evaluation pattern (each Import AI link is an independent article, not part of a unified essay).
- See `references/editorial-newsletter-high-coverage-pattern.md` — Import AI is a higher-yield variant (~20-30% unique) compared to The Signal (~10-15% unique).
- See `references/editorial-roundup-daily-digest-pattern.md` for the daily-digest classification (Import AI is NOT a daily digest — it publishes roughly weekly with deeper editorial selection).
