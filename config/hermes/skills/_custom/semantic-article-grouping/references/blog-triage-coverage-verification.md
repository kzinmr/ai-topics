# Blog Triage: Coverage Verification Workflow

This reference covers the **blog triage cross-reference verification** workflow — how to efficiently determine whether blog articles are already captured in existing wiki pages. For newsletter triage (Substack/Beehiiv noise filtering, URL resolution), see the main SKILL.md body.

## Overview

Blog triage has a higher "already covered" rate than newsletter triage because prolific bloggers (Simon Willison, Ed Zitron, etc.) are tracked as wiki entities with comprehensive article summaries. In a typical batch of 19 articles, expect:
- ~5-8 already captured in entity pages (reference/skip)
- ~1 with genuine new value (take)
- ~10 non-AI content (skip)

## Step-by-Step Verification

### 1. Same-Day Check (30s)

```bash
# Two-pronged: date grep + source name grep
grep "$(date +%Y-%m-%d)" ~/ai-topics/wiki/log.md | head -20
grep -i "simonwillison\|wheresyoured\|krebson\|daringfireball" ~/ai-topics/wiki/log.md
```

Look for lines like `## 2026-05-13 - Blog Ingest` followed by ingestion records. If `blog-wiki-ingest` already ran, the data is consumed.

### 2. Batch-Read Articles (parallel)

Read 5 articles at a time via `read_file`, prioritizing:
1. High-frequency sources first (simonwillison.net, wheresyoured.at — likely entity-covered)
2. AI-relevant-title first (anything mentioning "AI", "model", "agent", "security", "GPT", "Claude")
3. Non-AI sources last (johndcook.com, dfarq.homeip.net — quick skip)

### 3. Verify Against Entity Pages

For high-frequency sources (Simon Willison, Ed Zitron), the entity page is where article summaries accumulate:

```python
# Efficient batch check: grep all article titles from entity page
terminal(f"grep -i 'article-title-keyword' ~/ai-topics/wiki/entities/{entity}.md")
```

**Do NOT stop at "URL present"** — verify the entity page has actual content sections with the article's claims. A listing in `sources:` frontmatter or `References:` section without a summary means the article is NOT yet captured.

Key verification levels:

| Entity Page Has | Verdict |
|----------------|---------|
| Dedicated section with substantive summary | ✅ Already captured (reference) |
| Article URL in `sources:` frontmatter only | ⚠️ Not captured (potential take) |
| Generic heading, no specific claims/data | ⚠️ Not captured (potential take) |
| Mentioned in References list only | ⚠️ Not captured (potential take) |

### 4. Verify Against Concept Pages

For event-based articles (Patch Tuesdays, model releases, Glasswing updates), check concept pages:

```python
terminal(f"grep -i 'keyword' ~/ai-topics/wiki/concepts/{concept}.md | head -10")
```

Example: Krebs Patch Tuesday article → check `concepts/project-glasswing.md` for "Real-World Impact" section.

### 5. Verify Against Alternative Entities

Some articles may be captured under a different author's entity page:
- `wheresyoured.at` articles → `entities/ed-zitron.md` (not a separate "wheresyoured" entity)
- `daringfireball.net` articles → may be in `concepts/nextpad-ai-development.md` (not just Gruber's entity)

### 6. Terminal Fallback

When `search_files` returns false negatives (known pitfall):

```bash
# Direct filesystem find
find ~/ai-topics/wiki/concepts -name "*keyword*" 2>/dev/null
find ~/ai-topics/wiki/entities -name "*keyword*" 2>/dev/null
# Quick entity listing
ls -lt ~/ai-topics/wiki/entities/ | head -20
```

## Common Patterns in Blog Triage

### Simon Willison (always check first)
His entity page (`entities/simon-willison.md`, ~300 lines) accumulates ALL his May 2026+ output with dedicated sections. If the article is from simonwillison.net, it's almost certainly already there — verify by reading entity content, not assuming.

### Ed Zitron / wheresyoured.at
Entity `entities/ed-zitron.md` has a "Data Center Construction Investigation" section that captures his major investigative pieces. Short commentary posts may not be captured.

### Krebs / Glasswing
`concepts/project-glasswing.md` has a "Real-World Impact: May 2026 Patch Data" section that already captures all Glasswing-related Patch Tuesday data (Microsoft 118, Firefox 271, Apple 52, Oracle 450+, Chrome 127).

### Daring Fireball + Nextpad++
`concepts/nextpad-ai-development.md` was created to capture the Nextpad++ story. Daring Fireball articles about it are sources for the concept page, not separate entity entries.

## Edge Cases Discovered in Practice

### Timeline Entry ≠ Content Capture (antirez DS4 — May 2026)

The antirez entity page (`entities/antirez-com.md`) had `| 2026 | Published "A few words on DS4"` in its **Timeline table** — a publication event marker, not content capture. The DS4 launch contained significant technical details (2/8-bit asymmetric quantization with DeepSeek V4 Flash on 96-128GB RAM, distributed inference plans, coding agent integration) that were absent from the entity page despite the article being "acknowledged" in the timeline.

**Rule**: A Timeline table entry is a publication signal only. It indicates the author's output was noted, not that the content was extracted. Treat it as equivalent to "URL in sources frontmatter" (not captured). Read the entity page's substantive sections (Core Ideas, dedicated prose sections) to determine true coverage.

### Vendor-Specific Concept Page vs General Analysis (Martin Alderson Managed Agents — May 2026)

The `concepts/managed-agents.md` page was about **Anthropic's specific managed agents product** (Brain/Hands/Session architecture). Martin Alderson's article covered the **general managed-agent pattern** — comparing it to AWS Lambda, discussing vendor lock-in across all providers, Anthropic pricing changes, self-hosting with OpenCode, and Cloudflare/Vercel competitors.

**Rule**: When a concept page is vendor-specific (check frontmatter `aliases` and `tags` for hints — e.g., `Managed Agents (Anthropic)`), a blog article about the broader category may still represent a wiki gap. If the article covers cross-provider analysis, vendor-independent strategy, or the general phenomenon, it needs its own section or a separate general page.

### Same-Name, Different-Project (DS4 × 2 — May 2026)

The existing `concepts/ds4-deepseek-flash-metal.md` described **Armin Ronacher's fork** (ds4.c — Apple Silicon Metal optimization). antirez's new article was about his own **DwarfStar 4** (the original project, not the fork). Both share the "DS4" shorthand but are separate projects.

**Rule**: When a new article has the same name/acronym as an existing concept page, verify whether they refer to the same project by reading both the existing page's `sources` frontmatter (reveals which project it covers) and the new article's content. Different projects sharing a name require a separate page, not an update to the existing one.

### Blog-Specific Yield Adjustment

In a May 2026 batch of 20 blog articles from 14 sources, realized yields were:
- 3 Takes (antirez DS4, Apple M5 exploit, Martin Alderson managed agents)
- 6 References (Simon Willison×3, AI safety institute, Musk trial, Nesbitt)
- 11 Skips

This is significantly more takes than the reference's "Mixed batch: 1 take, 8 refs, 10 skips" guideline. Reason: Wednesday May 14 was an unusually high-content day with major AI developments (DS4 launch, M5 exploit). **The yield guidance is a baseline — actual yield varies with news velocity.**

## Yield Expectations

| Source Type | Typical Batch | Takes | References | Skips |
|-------------|---------------|-------|------------|-------|
| High-frequency AI blogger | 5 articles | 0-1 | 4-5 | 0 |
| Mixed batch (general blog roundup) | 19 articles | 1 | 8 | 10 |
| AI-specialized batch | 10 articles | 2-3 | 3-4 | 3-4 |

The high reference/skip ratio is a sign of **good wiki coverage health** — articles are being ingested into entity pages faster than new angles emerge.
