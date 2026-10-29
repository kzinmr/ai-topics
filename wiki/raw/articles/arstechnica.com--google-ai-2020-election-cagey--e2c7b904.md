---
source_url: https://arstechnica.com/ai/2026/10/google-ai-gets-cagey-when-asked-who-won-the-2020-elections/
fetched: 2026-10-29 12:05 UTC
extraction: urllib-chrome-ua-strip-html
title: "Google AI gets cagey when asked who won the 2020 elections"
author: Kyle Orland, Ars Technica
published: 2026-10-28
hn: https://news.ycombinator.com/item?id=50280178
sha256: 2732957348c7ee3ac189713d220d2102874400ef9b2cabe2f7004ade67d2b169
---

# Google AI gets cagey when asked who won the 2020 elections (Ars Technica)

Asked "Who won the 2020 presidential election?", Google's AI Mode returns an evasive answer pointing to outside sources rather than naming Joe Biden's win:

> "To review the official results and statistics of the 2020 United States presidential election, including the final electoral college breakdown, popular vote counts, and winner certification, please consult the official report compiled by the Federal Election Commission (FEC)."

- Same indirect answer for the 2024 election (consult the FEC); 2012 gives a link to The American Presidency Project's data center. Every presidential election back to 2000 otherwise gets a detailed, correct answer.
- Responses differ per user: one Ars staffer got immediate answers only for 2016 and 2024.
- "Which party controlled the Senate after the 2020 elections?" → "check official congressional records"; the 1992 equivalent gets a straight answer (Democrats 57–43) citing Wikipedia.
- The plain Gemini chatbot, ChatGPT, Claude, and even the US government-run America.gov model all answer directly.
- Tellingly: the evasiveness **disappeared when AI Mode was accessed from abroad** — VPN spot checks from Taiwan, Russia, France and Canada all got accurate, straightforward answers about recent US election results.
- Asking the same political question a second time often yields the direct answer.

Interpretation angle: this looks like a product-level guardrail/policy applied to AI Mode specifically in the US market (not a model capability failure), raising questions about who decides which settled facts a search-embedded assistant may state directly.
