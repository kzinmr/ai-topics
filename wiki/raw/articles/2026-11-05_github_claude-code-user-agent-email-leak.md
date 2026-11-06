---
title: "Claude Code sends your email address to websites (GitHub issue #107757)"
url: "https://github.com/anthropics/claude-code/issues/107757"
fetched_at: 2026-11-06T12:05:00+00:00
source: "GitHub — anthropics/claude-code issue tracker"
type: issue-report
sha256: 058d54ef13bf70a0fab8a809e1acbf406fe3124163cd483581b3b7e302ea39bf
---

# Claude Code sends your email address to websites (GitHub issue #107757)

Source: https://github.com/anthropics/claude-code/issues/107757 — HN: https://news.ycombinator.com/item?id=50385272 (1222 pts, 387 comments, Nov 5 2026)

## Issue body (taylor-edwards, opened Nov 5 2026, v2.1.318, macOS)

> Bug Description
> I receive dozens of scam emails per day because claude code divulged my email to arbitrary 3rd parties in the User-Agent request header while conducting web searches without my permission. This should not be a setting with opt-out or opt-in behavior, it needs to be removed from the harness entirely. It is not for the good of anyone involved: it does nothing for services which dislike agentic traffic, does not preserve my anonymity on the web, and is a goldmine for scammers. I am migrating my company to Pi with OpenRouter since I have no faith in anthropic preserving my privacy.

Reported User-Agent form observed by commenter motoroco: `my-session-slug/1 <my.name@example.com>` — the user's real email injected into the UA of outbound web-search/data-fetch requests.

## Anthropic response (contributor poteat)

> Hi folks! We introduced a built-in mod called cc-plugin-privacy to deterministically block this behavior in v2.1.317 and later - definitely let us know ASAP though if there's a gap in the checks introduced by that mod. I'll try to get that built-in mod source available like we do for the other built-in mods here.
> The built-in privacy mod is enabled by default, you can turn it off via /plugins.

## Notable community findings

- matheusmoreira: "I just asked Astra to verify that Codex does NOT do this, and it doesn't... Its reported User-Agent contains the client/version, OS/architecture, and terminal—no email address. Astra wasn't able to check OpenAI's 'hosted search service' though, whatever that is."
- morsik (audit): "I scanned every tool call in ~/.claude/projects/**/*.jsonl and found 53 calls that put [email] into a User-Agent, spread across 8 sessions from 2026-08-09 to 2026-11-01. Almost all came from workflow subagents writing their own curl -A \"<tool>/1.0 (<my-email>)\", not from WebFetch."
- OpakAlex: "it pulled my email address from my gitconfig and sent it without asking."
- GDPR concerns raised repeatedly (karladler: "That's plain and simple a GDPR violation."; morsik: "now random services holds people e-mails and must adhere to GDPR without even knowing that").
- lc-nyovchev (on proxy workarounds): "The labs should be able to provide basic PII and privacy by default rather than having us to rely on system prompts, skills, or proxies as crutches for their incompetence..."
- meowcakes: "Claude Code will refuse to do anything that can even remotely be considered 'unethical' and then morally lecture you about it, and then turns around and hands out your PII without asking you."
- Origin speculation (swatcoder, tcoff91, Seattle3503): likely a vibe-coded / agent-inserted UA convention (the SEC EDGAR convention `Sample Company Name AdminContact@<domain>` was cited by ChrystianSchutz as a possible template source) rather than a deliberate human product decision; nobody could confirm design intent.
- TZubiri (counterpoint): sites block anonymous agent traffic; contact-style UA headers are an anti-abuse accommodation — "anonymity usually works one way, one party can be anonymous, not both."

## Status

Issue remains Open, labeled area:security, area:tools, bug, platform:macos. 463 👍 on the issue body, 76 👀.
