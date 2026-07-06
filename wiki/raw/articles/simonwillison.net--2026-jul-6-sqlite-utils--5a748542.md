---
title: "sqlite-utils 4.0rc3"
url: "https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything"
fetched_at: 2026-07-06T07:01:35.252096+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# sqlite-utils 4.0rc3

Source: https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything

I hoped to release
sqlite-utils 4.0
stable this weekend, but as I worked through the backlog of issues and PRs with a combination of Claude Fable 5 and GPT-5.5 the changelog since rc2
kept getting bigger
.
The biggest new feature is support for introspecting and creating compound foreign keys - a feature that involves a subtle breaking change to
table.foreign_keys
and hence needed to land for the 4.0 stable release.
sqlite-utils
also now follows SQLite's convention for case insensitive column names, which turned out to touch
a bunch of different places at once
.
