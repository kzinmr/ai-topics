---
title: "A quote from Thibault Sottiaux"
url: "https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything"
fetched_at: 2026-07-17T07:00:57.719926+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A quote from Thibault Sottiaux

Source: https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything

16th July 2026
On file deletions. We’ve investigated a handful of reports where GPT-5.6 unexpectedly deleted files.
What we have  found is that this most commonly occurs when:
Full access mode is enabled and codex is run without sandboxing protections, including without auto review being enabled
The model attempts  to override the $HOME env var to define a temporary directory.
The model makes an honest mistake and mistakenly deletes $HOME instead.
—
Thibault Sottiaux
,
describing a pretty gnarly Codex bug
