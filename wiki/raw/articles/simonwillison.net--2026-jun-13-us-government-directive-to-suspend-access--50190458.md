---
title: "Statement on the US government directive to suspend access to Fable 5 and Mythos 5"
url: "https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/#atom-everything"
fetched_at: 2026-06-13T07:00:49.262898+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Statement on the US government directive to suspend access to Fable 5 and Mythos 5

Source: https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/#atom-everything

13th June 2026 - Link Blog
Statement on the US government directive to suspend access to Fable 5 and Mythos 5
(
via
) Well this is
nuts
:
The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees. The net effect of this order is that we must abruptly disable Fable 5 and Mythos 5 for
all
our customers to ensure compliance.
Access to all other Anthropic models
will not be affected.
We received the directive from the government today at 5:21pm (ET). The letter did not provide specific details of its national security concern. Our understanding is that the government believes it has become aware of a method of bypassing, or "jailbreaking" Fable 5. We reviewed a demonstration of this specific technique being used to identify a small number of previously known, minor vulnerabilities. These vulnerabilities all appear relatively simple, and we have found that other publicly-available models are able to discover them as well without requiring a bypass. [...]
To date, the government has only given us verbal evidence of a potential narrow, non-universal jailbreak, which essentially consists of asking the model to read a specific codebase and fix any software flaws. Our understanding is that one potential jailbreak was shared with the government. We have reviewed the report and validated that the level of capability displayed there is widely available from other models (including OpenAI's
GPT-5.5
), and is used every day by the defenders who keep systems safe. We will share more details over the next 24 hours.
I still have access to Fable via
claude.ai
and Claude Code now, at 9:01pm ET.
Update
: I ran
this script
against the Anthropic API to spot when
claude-fable-5
would stop working. My access was cut off at 6:59pm Pacific (9:59pm ET):
[2026-06-12T18:56:50-07:00] attempt 35: running uv run llm -m claude-fable-5 hi
[2026-06-12T18:56:55-07:00] success: Hi there! How can I help you today?
[2026-06-12T18:57:55-07:00] attempt 36: running uv run llm -m claude-fable-5 hi
[2026-06-12T18:57:59-07:00] success: Hi! How can I help you today?
[2026-06-12T18:58:59-07:00] attempt 37: running uv run llm -m claude-fable-5 hi
[2026-06-12T18:59:00-07:00] FAILED after attempt 37 with exit code 1

stderr:
Error: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'Claude Fable 5 is not available. Please use Opus 4.8. Learn more: https://www.anthropic.com/news/fable-mythos-access'}, 'request_id': 'req_011CbzRyirV7KZLHYYdBM9od'}
