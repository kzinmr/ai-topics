# Inbox Summary Overrates Editorial Newsletters with Existing Wiki Coverage

The inbox pre-triage summary evaluates articles on **topic importance alone** — it has no mechanism to check whether the wiki already comprehensively covers that topic. This creates a specific false-positive pattern distinct from the link-digest trap.

## Pattern

| Dimension | Link-Digest Trap | Coverage-Overrate Pattern |
|-----------|-----------------|---------------------------|
| Article quality | Shallow bullet lists | Substantive editorial commentary |
| Inbox rating | high/critical (wrong) | high/critical (wrong) |
| Why wrong | No body depth to extract | Core topic already comprehensively covered in wiki |
| Detection | Read article body depth | Cross-reference topic against existing wiki page depth |

## July 2026 Validation

**AINews/Latent Space** — "Lilian Weng summarizes 35 papers on Harness Engineering for RSI":
- Inbox summary: ★★★★★ take, candidate `concepts/harness-engineering.md`
- Reality: `concepts/harness-engineering.md` existed at 536 lines, `concepts/recursive-self-improvement.md` at 314 lines, `entities/lilian-weng.md` at 197 lines with Jul 2026 post already documented
- Corrected rating: ★★★★☆ reference (entity enrichment only, not new concept page)
- The AINews article was a substantive editorial roundup (33 paragraphs) but the core conceptual territory was fully covered

## Detection Steps

When the inbox summary rates a topic as ★★★★★ take:

1. **Check concept pages first**: Use `find ~/wiki/concepts -name "*keyword*"` for the topic keywords. Don't just check filename existence — read the actual page length and content sections.
2. **Check entity pages**: The author's entity page (e.g., `entities/lilian-weng.md`) may already document the specific post or research being summarized.
3. **Read body before rating**: The inbox summary's high rating means "important topic," not "wiki gap." Only resolve the newsletter post body to determine editorial value, then cross-reference against wiki pages.
4. **Check for cross-links**: If the concept page already wikilinks to the specific source, coverage is likely comprehensive.

## Action

- Downgrade ★★★★★ take → ★★★★☆ reference when the concept page exists at 300+ lines and already covers the topic's core theses
- The newsletter's unique value (editorial commentary connecting the topic to current product launches) goes to the **author's entity page**, not a new concept page
- Apply this pattern only to **editorial-roundup newsletters** (AINews, The Signal, etc.) that report on existing research — not to original analysis newsletters (SemiAnalysis, Super Intel) where the inbox summary and actual content are one and the same

## Relationship to Other Patterns

- Distinguished from **pure link digest trap**: editorial roundups have substantive body text (AINews had 33 paragraphs), link digests have shallow bullet lists
- Distinguished from **inbox wrong topic estimation**: the inbox gets the topic RIGHT (it IS about harness engineering + RSI) but overrates the coverage gap because it doesn't know the wiki already has 850 lines on the subject
