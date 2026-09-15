---
title: "Soft-deprecating re.match()"
url: "https://simonwillison.net/2026/Sep/11/soft-deprecating-re-match/"
fetched_at: 2026-09-12T10:00:55.268817+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Soft-deprecating re.match()

Source: https://simonwillison.net/2026/Sep/11/soft-deprecating-re-match/

11th September 2026 - Link Blog
Soft-deprecating re.match()
(
via
) Python has a concept of
soft deprecation
, where APIs are marked as "should no longer be used to write new code" without any promise/threat to remove them in the future.
Python 3.15 release manager Hugo van Kemenade describes how in the upcoming 3.15 release soft deprecation has come for the venerable but deeply confusing
re.match()
function. It's now available with the much clearer alternative
re.prefixmatch()
name - reflecting how it anchors at the beginning of the string but not the end.
Most of the time you probably want
re.search()
(match this pattern anywhere in the string) or
re.fullmatch()
(match the entire string) instead.
