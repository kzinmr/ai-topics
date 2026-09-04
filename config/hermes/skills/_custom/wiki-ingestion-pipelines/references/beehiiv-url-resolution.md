# Beehiiv URL Resolution — Failure Patterns & Workarounds

## Problem

Beehiiv newsletter tracking links (`link.mail.beehiiv.com/v1/c/...`) are behind **Cloudflare Bot Management** challenge. All curl-based approaches fail:

- `curl -L` → stays on same URL (CAPTCHA page, no redirect)
- `curl -I -L` → no Location header returned
- `curl -v` → TLS handshake succeeds, but response is Cloudflare challenge HTML
- `curl` with custom User-Agent → same CAPTCHA

The Cloudflare challenge requires JavaScript execution (browser-based interaction). This affects:
- Tracking/redirect links in newsletter emails
- beehiiv RSS feeds (`/feed/<newsletter-slug>`)
- beehiiv archive pages (`/p/<newsletter-slug>/archive`)

## Workaround: Title-Based Newsletter Identification

When all URLs are unresolvable beehiiv tracking links:

1. **Extract newsletter title** from the raw digest file (`subject` field)
2. **Web search** for `"<newsletter title>" newsletter` or `"<newsletter title>" site:beehiiv.com`
3. **Identify**: publisher name, subscriber count, theme/focus, issue count
4. **Assess relevance** from the newsletter's description/tagline
5. **Classify** as high/low relevance based on whether the newsletter's stated focus aligns with wiki scope (LLM, AI agents, dev tooling)

## Triage Decision Matrix for Unresolvable Beehiiv Links

| Newsletter Theme | Action |
|---|---|
| Deep technical AI/LLM content (e.g., model analysis, agent architectures) | Mark as `high`, note "content not retrievable — monitor for future issues" |
| General AI adoption/trust/culture (e.g., "AI capability vs trust gap") | Mark as `low`, note "tangentially relevant, not technical source" |
| Non-AI topics | Mark as `low`, skip |

## Example

Newsletter: "The Stage and the Factory Floor" by Manu Sharma
- Web search revealed: 7K+ subscribers,139 issues, weekly, focuses on AI trust gap
- Assessment: Tangentially relevant but not a deep technical source → `low`
- All 20 tracking links unresolvable → skip, monitor for future

## Affected Newsletter Sources (known)

- Any newsletter hosted on beehiiv platform (check `link.mail.beehiiv.com` in URLs)
- Common in: AI news roundups, tech opinion newsletters, creator economy newsletters
