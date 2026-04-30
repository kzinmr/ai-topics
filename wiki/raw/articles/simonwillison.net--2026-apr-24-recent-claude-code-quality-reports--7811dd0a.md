---
title: "An update on recent Claude Code quality reports"
url: "https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/#atom-everything"
fetched_at: 2026-04-30T07:01:12.058038+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# An update on recent Claude Code quality reports

Source: https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/#atom-everything

24th April 2026 - Link Blog
An update on recent Claude Code quality reports
(
via
) It turns out the high volume of complaints that Claude Code was providing worse quality results over the past two months was grounded in real problems.
The models themselves were not to blame, but three separate issues in the Claude Code harness caused complex but material problems which directly affected users.
Anthropic's postmortem describes these in detail. This one in particular stood out to me:
On March 26, we shipped a change to clear Claude's older thinking from sessions that had been idle for over an hour, to reduce latency when users resumed those sessions. A bug caused this to keep happening every turn for the rest of the session instead of just once, which made Claude seem forgetful and repetitive.
I
frequently
have Claude Code sessions which I leave for an hour (or often a day or longer) before returning to them. Right now I have 11 of those (according to
ps aux  | grep 'claude '
) and that's after closing down dozens more the other day.
I estimate I spend more time prompting in these "stale" sessions than sessions that I've recently started!
If you're building agentic systems it's worth reading this article in detail - the kinds of bugs that affect harnesses are deeply complicated, even if you put aside the inherent non-deterministic nature of the models themselves.
