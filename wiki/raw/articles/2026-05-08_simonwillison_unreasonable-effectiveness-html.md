---
title: "Using Claude Code: The Unreasonable Effectiveness of HTML (Simon Willison)"
source: simonwillison.net
date: 2026-05-08
scraped: 2026-05-09
authors:
  - Simon Willison
url: https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/
tags:
  - prompt-engineering
  - claude-code
  - html
  - markdown
  - llm
---

# Using Claude Code: The Unreasonable Effectiveness of HTML

**Simon Willison's Weblog** — 8th May 2026 (Link Blog)

Link to original: [Thariq Shihipar's X Article](https://twitter.com/trq212/status/2052809885763747935)
Companion site: [thariqs.github.io/html-effectiveness/](https://thariqs.github.io/html-effectiveness/)

---

Thought-provoking piece by Thariq Shihipar (on the Claude Code team at Anthropic) advocating for HTML over Markdown as an output format to request from Claude.

The article is crammed with interesting examples (collected on this site) and prompt suggestions like this one:

> `Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the streaming/backpressure logic so focus on that. Render the actual diff with inline margin annotations, color-code findings by severity and whatever else might be needed to convey the concept well.`

I've been defaulting to asking for most things in Markdown since the GPT-4 days, when the 8,192 token limit meant that Markdown's token-efficiency over HTML was extremely worthwhile.

Thariq's piece here has caused me to reconsider that, especially for output. Asking Claude for an explanation in HTML means it can drop in SVG diagrams, interactive widgets, in-page navigation and all sorts of other neat ways of making the information more pleasant to navigate.

I wrote about [Useful patterns for building HTML tools](https://simonwillison.net/2025/Dec/10/html-tools/) last December, but that was focused very much on interactive utilities like the ones on my tools.simonwillison.net site. I'm excited to start experimenting more with rich HTML explanations in response to ad-hoc prompts.

### Trying this out on copy.fail

copy.fail describes a recently discovered Linux security exploit, including a proof of concept distributed as obfuscated Python.

I tried having GPT-5.5 create an HTML explanation of the exploit like this:

> `curl https://copy.fail/exp | llm -m gpt-5.5 -s 'Explain this code in detail. Reformat it, expand out any confusing bits and go deep into what it does and how it works. Output HTML, neatly styled and using capabilities of HTML and CSS and JavaScript to make the explanation rich and interactive and as clear as possible'`

Here's [the resulting HTML page](https://gisthost.github.io/?ae53e3461ffdbfd0826156aacf025c7e). It's pretty good, though I should have emphasized explaining the exploit over the Python harness around it.
