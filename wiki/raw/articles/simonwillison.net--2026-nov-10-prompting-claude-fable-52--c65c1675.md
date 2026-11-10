---
title: "A quote from Prompting Claude Fable 5.2"
url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/"
fetched_at: 2026-11-10T10:01:15.997234+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A quote from Prompting Claude Fable 5.2

Source: https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/

10th November 2026
Claude Fable 5.2 responds closely to what the prompt says about who owns the code it works on. In Anthropic’s testing on small coding tasks, when a prompt said nothing about ownership or presented the code base as someone else’s, the model tended to add to the existing structure, even when that repeated existing code. [...]
If you want the model to improve the structure as it works, say that the code is its own:
This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it.
In Anthropic’s testing on small coding tasks, the model merged repeated code in about half of the tries with this sentence, and in under a tenth of the tries without it.
—
Prompting Claude Fable 5.2
,
Anthropic documentation
