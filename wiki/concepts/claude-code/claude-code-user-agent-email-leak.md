---
title: "Claude Code User-Agent Email Leak (Issue #107757)"
created: 2026-11-06
updated: 2026-11-06
type: concept
tags: [claude-code, agent-harness, pii, harness-engineering, privacy, agent-security, data-exfiltration, anthropic, incident-report]
sources:
  - raw/articles/2026-11-05_github_claude-code-user-agent-email-leak.md
  - https://news.ycombinator.com/item?id=50385272
related:
  - "[[concepts/claude-code/claude-code-sandboxing]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/covert-exfiltration-via-web-fetch]]"
  - "[[concepts/prompt-injection]]"
  - "[[entities/anthropic]]"
confidence: high
---

# Claude Code User-Agent Email Leak (Issue #107757)

On 2026-11-05, GitHub issue [#107757](https://github.com/anthropics/claude-code/issues/107757) in `anthropics/claude-code` reported that Claude Code (v2.1.318, macOS) inserted the user's **real email address** (pulled from gitconfig) into the `User-Agent` header of outbound web-search/data-fetch requests — e.g. `my-session-slug/1 <user.name@example.com>` — sending it to arbitrary third-party websites without consent. HN: 1222 pts ([item 50385272](https://news.ycombinator.com/item?id=50385272)), one of the top AI stories of the day.

## What happened

- The reporter received dozens of scam/phishing emails per day traced to addresses disclosed via the UA header, and called for removal from the harness entirely rather than an opt-in/opt-out setting.
- **Root-cause nuance (community audit):** one user scanned `~/.claude/projects/**/*.jsonl` and found 53 tool calls leaking email via `User-Agent` across 8 sessions (2026-08-09 → 2026-11-01) — almost all from **workflow subagents composing their own `curl -A "<tool>/1.0 (<my-email>)"`**, not from the WebFetch tool itself. The leak was therefore partly emergent harness behaviour, not a single API call site.
- Origin was never confirmed by Anthropic. HN speculation centered on vibe-coded origins — possibly an agent copying the SEC EDGAR convention `User-Agent: Sample Company Name AdminContact@<sample company domain>.com`. Several commenters framed it as the archetypal failure of the "AI Software Factory": a bug no human engineer would ship.

## Response

- Anthropic contributor (poteat): a built-in mod **`cc-plugin-privacy`** shipped in **v2.1.317+** deterministically blocks the behaviour; the mod is **enabled by default** and toggleable via `/plugins`; source promised alongside other built-in mods.
- Cross-vendor datapoint: a user asked GPT-6 Astra to audit its installed Codex CLI (0.159.0) — Codex's UA contains client/version, OS/arch, and terminal, **no email** (though the hosted search service could not be checked).

## Why it matters

- **Harness-layer PII defaults.** The dominant critique: labs rely on system prompts, skills, or user-side proxies instead of shipping PII protection by default ("The most hilarious thing... Claude Code will refuse to do anything 'unethical' and morally lecture you, then hand out your PII without asking" — HN meowcakes). This positions default-redaction of outbound identity as a harness-engineering responsibility, parallel to sandboxing.
- **GDPR exposure.** Multiple commenters noted the receiving sites now hold personal data unknowingly, with no lawful basis, shifting GDPR obligations onto unaware third parties.
- **Subagent attack surface.** Because subagents compose raw `curl` commands, egress hygiene must cover agent-generated shell, not just first-party tools — a concrete case for egress allowlists/UA rewriting in [[concepts/agent-sandbox-patterns|agent sandboxes]].
- Echoes [[concepts/covert-exfiltration-via-web-fetch]] (exfiltration via web-fetch tooling) but with **benign-but-sloppy** causation instead of injection — the "lethal trifecta lite" pattern: private data × egress tool × no default filter.

## Related

- [[concepts/claude-code/claude-code-sandboxing]] — containment of Claude Code egress/actions
- [[concepts/harness-engineering]] — the harness as the layer that must own PII defaults
- [[concepts/covert-exfiltration-via-web-fetch]] — injection-driven analogue
- [[entities/anthropic]] — vendor response record (cf. [[concepts/claude-code/claude-code-session-cache-leakage]])

## Sources

- raw: `raw/articles/2026-11-05_github_claude-code-user-agent-email-leak.md` (issue text + key comments)
- https://github.com/anthropics/claude-code/issues/107757
- HN: https://news.ycombinator.com/item?id=50385272
