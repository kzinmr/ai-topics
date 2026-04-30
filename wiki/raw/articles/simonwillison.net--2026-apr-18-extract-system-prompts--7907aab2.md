---
title: "Claude system prompts as a git timeline"
url: "https://simonwillison.net/2026/Apr/18/extract-system-prompts/#atom-everything"
fetched_at: 2026-04-30T07:01:13.274525+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Claude system prompts as a git timeline

Source: https://simonwillison.net/2026/Apr/18/extract-system-prompts/#atom-everything

Research
Claude system prompts as a git timeline
— Anthropic's published system prompt history for Claude is transformed into a git-based exploration tool, breaking up the monolithic markdown source into granular files and timestamped commits. By structuring extracted prompts per model, family, and revision, researchers can leverage `git log`, `diff`, and `blame` to trace prompt evolution, compare differences, and attribute changes to specific dates—all without manual parsing.
Anthropic
publish the system prompts
for Claude chat and make that page
available as Markdown
. I had Claude Code turn that page into separate files for each model and model family with fake git commit dates to enable browsing the changes via the GitHub commit view.
I used this to write my own
detailed notes on the changes between Opus 4.6 and 4.7
.
