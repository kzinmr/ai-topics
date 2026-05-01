---
title: "Codex CLI 0.128.0 adds /goal"
url: "https://simonwillison.net/2026/Apr/30/codex-goals/#atom-everything"
fetched_at: 2026-05-01T07:13:04.751121+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Codex CLI 0.128.0 adds /goal

Source: https://simonwillison.net/2026/Apr/30/codex-goals/#atom-everything

30th April 2026 - Link Blog
Codex CLI 0.128.0 adds /goal
(
via
) The latest version of OpenAI's Codex CLI coding agent adds their own version of the
Ralph loop
: you can now set a
/goal
and Codex will keep on looping until it evaluates that the goal has been completed... or the configured token budget has been exhausted.
It looks like the feature is mainly implemented though the
goals/continuation.md
and
goals/budget_limit.md
prompts, which are automatically injected at the end of a turn.
