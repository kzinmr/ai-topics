# Simon Willison Quote-Post Pattern

## Detection

Simon Willison frequently publishes very short posts consisting of a single quote from someone else with minimal or no original commentary. These are identifiable by:

| Signal | Detail |
|--------|--------|
| **File size** | 500–1,000 bytes (confirmed: 931B sycophancy quote, 651B Sean Lynch MCP quote) |
| **Content structure** | Frontmatter → "Source: URL" → 1 blockquote (6-15 lines) → attribution line (`— Name`) → "comment on Hacker News" |
| **Original commentary** | Zero — the post exists solely to surface someone else's comment |
| **URL pattern** | `simonwillison.net/YYYY/Mon/DD/author-name/#atom-everything` (the `#atom-everything` anchor is a tell) |
| **Title format** | `"A quote from <Name>"` or `"<short excerpt from quote>"` |

## Triage Rule

**Quote-posts should be rated ★★☆☆☆ at best (reference), never a take.** Even when the quote is AI-relevant, the single quote lacks sufficient depth or body for a new wiki page or entity enrichment.

### When to upgrade to reference instead of skip

Upgrade to reference only when the quote expresses a **genuinely novel framing** that no existing concept page captures. Example: Sean Lynch's "MCP as auth gateway" framing — MCP's idealized form is "just an auth gateway for the API" — was a new perspective distinct from the existing MCP enterprise OAuth coverage, but still too brief for a page update.

### When to skip entirely (default)

- Quote of an **opinion** or commentary → skip
- Quote that restates a known position → skip
- Quote with no empirical data → skip

## Verification Against Entity Page

Simon Willison's entity page (entities/simon-willison.md) accumulates his OWN writing with dedicated sections. Quote-posts are his curation of OTHERS' content and are typically NOT captured as entity-page sections. Therefore:

- **Do NOT check Simon Willison's entity page for quote-post content** — it won't be there
- **Check the relevant CONCEPT page instead** (e.g., for a MCP quote, check concepts/mcp.md or concepts/mcp-enterprise-oauth.md)
- If the concept page already contains the same framing/insight, the quote-post adds nothing

## Confirmed Instances

| Date | Size | Topic | Verdict |
|------|------|-------|---------|
| 2026-05-03 | 931B | Anthropic sycophancy data (empirical) | Reference (data filled verification gap) |
| 2026-06-19 | 651B | Sean Lynch on MCP as auth gateway | Reference (novel framing, concept page had related content) |

## Why This Matters

Simon Willison is one of the most prolific blog sources tracked by the pipeline. His blog publishes ~30% quote-posts by volume (estimated). Without a specific triage rule for this pattern, every quote-post would trigger a full body-read + exhausive cross-reference, wasting 3-5 minutes per post. The quote-post rule saves ~30% of Simon-Willison triage time with no loss of wiki quality.
