---
title: "A quote from Geoffrey Huntley"
url: "https://simonwillison.net/2026/Oct/13/geoffrey-huntley/"
fetched_at: 2026-10-14T10:01:15.001303+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A quote from Geoffrey Huntley

Source: https://simonwillison.net/2026/Oct/13/geoffrey-huntley/

13th October 2026
If the agent isn't using my diagnostics library, I could introspect and update AGENTS.md, but there's still a delta, and it'll drift. Instead, I write a pre-commit hook that checks the git diff for direct calls to observability modules that bypass my diagnostics module. Boom: fail the commit, inject a prompt telling the agent to use the diagnostics library. All of a sudden it's ten out of ten.
—
Geoffrey Huntley
,
nobody should type code by hand anymore. here's what's left.
