# Subscription Confirmation / "Thank You for Supporting" Newsletter Pattern

## Pattern Identification

Some newsletters send **subscription confirmation or welcome emails** disguised as regular issues. These have no editorial content and should be skipped immediately.

### Detection Criteria

| Signal | How to Detect | Action |
|--------|--------------|--------|
| Subject starts with "Thank you for supporting" | Read the subject from the checkpoint's `source_name` | Skip immediately — no editorial content |
| All links are `email.mg-d0.substack.com/c/...` encoded tracking URLs | Check any 2-3 links for this domain pattern. These are Substack's email-delivery tracking redirects, not linkable content | No URL resolution needed — no content to extract |
| `source_name` matches known publication but email arrives as standalone item | Cross-reference with known publication names (e.g., "Vanishing Gradients" is a legitimate AI newsletter) | The *subscription confirmation* has no content; the *regular issues* from the same publication DO have content. Do NOT mark the publication as a skip source |
| Subject mentions "welcome" or "getting started" or "confirm" | Check the subject line | Skip |

### Confirmed Example

**Vanishing Gradients** (publication_id unknown):
- Subject: "Thank you for supporting Vanishing Gradients"
- All 3 links: `https://email.mg-d0.substack.com/c/eJxskUmO...` (base64-encoded tracking)
- Resolution: No content, subscription confirmation — skip
- Context: Vanishing Gradients IS a legitimate AI newsletter (analysis of AI industry trends, gradient of change in ML). Its regular issues should be triaged normally. Only the confirmation email is to be skipped.

## Relationship to Other Skip Patterns

| Pattern | Email Type | Skip Rule |
|---------|-----------|-----------|
| Subscription confirmation | "Thank you for supporting" / "Welcome to" | Skip all links |
| Pure link digest | Weekly roundup with 1-line descriptions (e.g., True Positive Weekly) | Skip post body; external links may have independent value |
| Pure podcast | 100% audio UI links (e.g., Lenny's Podcast) | Skip entire publication |
| OAuth redirect | `substack.com/redirect/2/eyJ...` | Skip single link (component of regular newsletter) |
| UUID redirect | `substack.com/redirect/<uuid>` | Skip single link (component of regular newsletter) |

## When Not to Skip

- A regular issue from the SAME publication (e.g., a Vanishing Gradients weekly analysis post) — these are substantive and should be triaged normally
- A newsletter with subject "Thank you" that contains actual article links (rare, but verify body content before deciding)
