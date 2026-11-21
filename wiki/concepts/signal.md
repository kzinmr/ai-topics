---
title: "Signal"
type: concept
aliases:
  - signal
created: 2026-04-25
updated: 2026-11-21
tags:
  - concept
sources: []
status: stub

---

# Signal

> **TODO**: Enrich this page.

## Overview

Stub page for Signal.

## Blocking OS-level AI agents (Nov 20, 2026)

Signal announced (Meredith Whittaker, Nov 20, 2026) that it is restricting OS-integrated AI agents from capturing Signal screen content: screenshot blocking on iOS 27 and automatic "Screen security" enforcement on Android when an AI assistant is detected reading the screen — the same class of defense it shipped against Microsoft Recall on Windows. The targets are Google's Gemini Intelligence "Onscreen Awareness" and Apple's Siri AI integrations, which scan rendered screen content to serve agentic queries, pulling Signal messages into whatever local or remote store the OS agent uses. Whittaker calls it an "existential threat" to application-layer privacy: E2E encryption does not cover data at the moment it is rendered into the UI tree.

Two demands to Apple/Google/Microsoft: (1) a documented way for apps to opt out of AI data access (screen reading, filesystem, notifications, APIs) without breaking core utility; (2) real technical documentation of how OS agents access and process app data — confidential-computing framing is called insufficient because it leaves privacy decisions with the OS vendor. Signal notes third-party agents (e.g. Meta's Muse) abusing accessibility permissions as a "skeleton key", the absence of usable APIs on macOS (only workaround: exclude Signal from Siri), and that even its own remedy is incomplete against filesystem-level access. HN (556 pts) was split between approving the Recall precedent, asking why Apple's security posture survives this, and a recurring thread demanding Monero support for phone-number-free registration.

HN: https://news.ycombinator.com/item?id=50572348
## Related Pages

- [[entities/_index]]
