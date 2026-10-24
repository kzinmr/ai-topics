---
title: "𝜏-Entity: Can voice agents get the details right?"
url: "https://sierra.ai/blog/tau-entity-can-voice-agents-get-the-details-right"
fetched_at: 2026-10-23T10:01:33.893414+00:00
source: "Sierra Blog"
tags: [blog, raw]
---

# 𝜏-Entity: Can voice agents get the details right?

Source: https://sierra.ai/blog/tau-entity-can-voice-agents-get-the-details-right

Voice agents can handle increasingly complex conversations, but sometimes the thing that breaks the call is simple: getting a name, phone number, or email address right. We saw this bottleneck repeatedly in
𝜏
-Voice: an agent would get a detail wrong and fail authentication before it could help.
Today we’re introducing
𝜏-Entity
, a benchmark that measures whether an agent can capture a detail correctly, recognize when it might be wrong, and repair the mistake.
𝜏-Entity tests voice agents on 200 tasks across ten entity types, including names, phone numbers, addresses, and emails. Each call focuses on a single field, with a cooperative caller who spells accurately when asked. Most calls take less than two minutes.
Even in this simple setting, today’s voice agents struggle to get the details right.
Inside the benchmark
Each task starts with a missing value. The agent has to ask the caller for it and submit it correctly. Success requires the stored value to exactly match the expected value. We vary three things: the difficulty of the value itself, caller behaviors such as corrections and restarts, and the audio environment.
We then measure Pass³: whether the agent completes the same task successfully under regular, noise-heavy, and speech-heavy conditions.
This lets us separate two questions: Can the agent capture the value? And can it do so reliably as the conditions change?
How current agents score
On the 𝜏-Entity leaderboard, which pools all six
𝜏
-i18n languages, GPT Live 1 leads: it captures the value correctly in 60.3% of regular calls, but succeeds under all three conditions on only 34.0% of tasks. Gemini 3.8 Live and Grok Voice Think Fast 2.0 reach 43.8% and 44.2% in regular conditions, and fall to 19.5% and 24.0% across all three.
English alone is easier: GPT Live 1 reaches 74.0% on regular calls and 47.5% across all three conditions. Spanish, Portuguese, and Hindi stay close to English, and for Gemini and Grok score above it, but Korean Pass³ falls to 3.5–8.5% and Mandarin to 12.5–24.5% across agents.
Knowing when to slow down
When people aren’t sure they heard something correctly, they slow down, ask someone to repeat themselves, spell a name, or confirm what they heard. Agents recognize only some reasons to slow down, and miss others.
In the 𝜏-Elicitation paper, we measured verification effort as the number of read-backs and spelling requests an agent makes during a call, then compared that behavior across familiar and unfamiliar entities, easy and hard values, noisy and clean environments, and different caller voices.
Circles show the baseline; diamonds show the challenging condition. A move to the right means more verification. The caller-voice comparison uses each system’s own best- and worst-performing voices.
The agents in that study adapted to some kinds of difficulty: across systems, they verified hard and unfamiliar entities more carefully. But only Grok verified more under noise, and none spent more effort verifying the caller voice it struggled with most.
In other words, agents recognize some warning signs, but don’t reliably adapt to all of them.
Asking again is only part of the solution
In the paper, we also tested whether prescribing a verification strategy could close the gap. The prescribed sequence is: ask, have the caller spell the value or read it back, confirm and correct, then submit.
When agents choose their own verification strategy, only 14–41% of tasks succeed across all three conditions. The prescribed sequence raises that to 37–54%, a gain of
14–31 percentage points
depending on the configuration. But the extra care costs time: calls take 21–28 seconds longer.
Each configuration runs the same 200 tasks in each of three conditions under both prompts: 4,800 calls in total.
Even if an agent realizes it may be wrong, recovery is not guaranteed. In the paper’s behavioral analysis, only 24–37% of initially incorrect captures that agents verify are ultimately corrected. Sometimes the agent repeats the same mistake. Other times, it replaces the original value with a new incorrect one. Asking a follow-up question is only useful if the agent can incorporate the answer correctly.
Errors also accumulate when a call needs several fields. In the paper’s multi-field study, only 53% of three-field calls succeed even though individual fields remain 75% accurate. In a separate comparison on those same multi-field tasks, validating each field and allowing retries increased success from 64% to 82%. Because the intervention combines validation and retry, we can’t isolate how much each contributes.
The direction is clear: reliable voice agents need to recognize uncertainty, verify the right things, and actually repair mistakes when they happen.
Where things stand
These results point to two opportunities: better decisions about when and how to verify, and more reliable correction when something goes wrong. Asking a follow-up question only helps if the agent can use the answer to correct what it captured.
That doesn’t mean every interaction needs the longest possible verification process. Prescribed verification improves reliability, but takes more time. The challenge is knowing when that extra effort is needed and making it count.
𝜏-Entity provides controlled tasks for measuring progress across entity types, caller behaviors, and environments. We’re introducing it alongside 𝜏-i18n, and it already covers the same six languages.
Thanks to Victor Barres at Mercor for the collaboration.
