---
title: "GitHub Models is now retired"
url: "https://simonwillison.net/2026/Aug/9/github-models-is-now-retired/#atom-everything"
fetched_at: 2026-08-10T10:23:22.112353+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# GitHub Models is now retired

Source: https://simonwillison.net/2026/Aug/9/github-models-is-now-retired/#atom-everything

9th August 2026 - Link Blog
GitHub Models is now retired
. I missed this news until today, when the GitHub Actions run for my
simonw/research
repository failed with this error message:
GitHub Models is temporarily unavailable as part of a scheduled retirement brownout.
That message is already stale, because the retirement has been completed.
GitHub Models was an odd-shaped duck. GitHub provided a model playground tool and a unified API across a bunch of different LLM providers, with the biggest benefit being that code running in GitHub Actions could use the GitHub API key already present in that environment to execute prompts.
This made it easy to build things that fit GitHub Next's
Continuous AI
concept.
GitHub didn't share the reason behind the shutdown, but my bet is that it fits the pattern where coding agent patterns made it prohibitively expensive to offer free or subsidized tokens.
My workflow uses an LLM call to create folder summaries for
the README
, using
this code here
. I swapped GitHub Models out for an OpenAI API key with a monthly spending limit, and I'm now generating my summaries using GPT-5.6 Luna.
