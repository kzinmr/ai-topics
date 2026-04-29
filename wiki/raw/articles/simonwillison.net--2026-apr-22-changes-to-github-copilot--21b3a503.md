---
title: "Changes to GitHub Copilot Individual plans"
url: "https://simonwillison.net/2026/Apr/22/changes-to-github-copilot/#atom-everything"
fetched_at: 2026-04-29T07:01:19.605960+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Changes to GitHub Copilot Individual plans

Source: https://simonwillison.net/2026/Apr/22/changes-to-github-copilot/#atom-everything

22nd April 2026 - Link Blog
Changes to GitHub Copilot Individual plans
(
via
) On the same day as Claude Code's temporary will-they-won't-they $100/month kerfuffle (for the moment,
they won't
), here's the latest on GitHub Copilot pricing.
Unlike Anthropic, GitHub put up an official announcement about their changes, which include tightening usage limits, pausing signups for individual plans (!), restricting Claude Opus 4.7 to the more expensive $39/month "Pro+" plan, and dropping the previous Opus models entirely.
The key paragraph:
Agentic workflows have fundamentally changed Copilot’s compute demands. Long-running, parallelized sessions now regularly consume far more resources than the original plan structure was built to support. As Copilot’s agentic capabilities have expanded rapidly, agents are doing more work, and more customers are hitting usage limits designed to maintain service reliability.
It's easy to forget that just six months ago heavy LLM users were burning an order of magnitude less tokens. Coding agents consume a
lot
of compute.
Copilot was also unique (I believe) among agents in charging per-request, not per-token. (
Correction: Windsurf also operated a credit system like this which they
abandoned last month
.) This means that single agentic requests which burn more tokens cut directly into their margins. The most recent pricing scheme addresses that with token-based usage limits on a per-session and weekly basis.
My one problem with this announcement is that it doesn't clearly clarify
which
product called "GitHub Copilot" is affected by these changes. Last month in
How many products does Microsoft have named 'Copilot'? I mapped every one
Tey Bannerman identified 75 products that share the Copilot brand, 15 of which have "GitHub Copilot" in the title.
Judging by the linked
GitHub Copilot plans page
this covers Copilot CLI, Copilot cloud agent and code review (features on
GitHub.com
itself), and the Copilot IDE features available in VS Code, Zed, JetBrains and more.
