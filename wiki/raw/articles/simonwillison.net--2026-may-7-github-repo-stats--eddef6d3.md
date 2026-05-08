---
title: "GitHub Repo Stats"
url: "https://simonwillison.net/2026/May/7/github-repo-stats/#atom-everything"
fetched_at: 2026-05-08T07:01:35.300836+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# GitHub Repo Stats

Source: https://simonwillison.net/2026/May/7/github-repo-stats/#atom-everything

One of the things I always look for when evaluating a new GitHub repository is the number of commits it has... but that number isn't visible on GitHub's mobile site layout. I built this tool to fix that, using this prompt:
Given a GitHub repo URL or foo/bar repo ID show information about that repo absorbed via wither REST or graphql CORS fetch() including the number of commits in the repo and other useful stats
Example output for
simonw/datasette
and
simonw/llm
.
