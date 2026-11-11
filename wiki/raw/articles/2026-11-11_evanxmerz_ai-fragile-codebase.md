---
title: "AI usage generates a fragile codebase"
source: https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/
author: Evan X. Merz
published: 2026-11-07
ingested: 2026-11-11
type: blog-post
hn: https://news.ycombinator.com/item?id=50438318
sha256: 976f277125969f6767465bd582d39d8a9c19044b426fd1754c53fac1cf80142f
---

AI usage generates a fragile codebase — Evan X. Merz, 2026-11-07

I can only speculate as to the reasons why I was laid off from Meta in May, but I suspect one reason is that I was a little more resistant to adopting AI/LLMs as coding tools than some of my peers. I generated at least 90% of my code using AI in my last few months there, which was the minimum for a decent rating. But AI didn't 10X the amount of code I was writing. It didn't even 2X it.

I was focused on code quality. I saw the code being pushed by peers heavily reliant on AI, and it was brittle. Many subtle issues that would lead to long-term tech debt, and even glaring issues ignored by very good programmers — e.g., one of the best programmers on my team tried to merge code using JavaScript events for mouseover CSS effects rather than the :hover selector.

Now employed at another large tech company, I've fully made the switch to 100% AI-generated code because that's the expectation today. Still, more people are becoming aware this isn't sustainable for large-scale SaaS. AI solves problems that fit within its context window very well, but is totally oblivious to long-term issues that can't be understood in that relatively small frame.

Four ways AI makes codebases fragile:
1. AI writes shallow tests — simplistic cases that don't cover what matters to humans; lots of get/set tests; e2e tests only covering cases already in the codebase; massive coverage gaps invisible to line-level coverage metrics.
2. AI writes overly complex code — two or three helper methods where one suffices; follows DRY to a fault, adding complexity that makes debugging harder for humans.
3. Reliance on AI decreases human understanding — the longer a company relies on agents, the fewer developers understand the codebase, so they can't spot new abstractions that conflict with existing structures.
4. AI moves too quickly to maintain a high quality bar — each PR arrives faster than the last, reviewed in less time; developers skim; small issues accrue into spaghetti code.

Four signs you have a fragile (AI-generated) codebase:
1. More incidents — after a year or two of agentic coding, an incident every weekend.
2. Incident recovery takes longer — shallow human understanding means slower mitigation; companies lose more money per incident.
3. Errors only visible to users — uncaught errors that only real-world users see, because nobody instruments analytics/error-catching for use cases humans didn't examine.
4. Poor user experience — "AI codebases are software made by AI for AI," tailored neither to how users use the product nor how developers maintain it — a vicious cycle of enshittification.

Products made for humans require a human touch.

## HN discussion highlights (item 50438318, 580pts, 543c)

- [CurleighBraces] Humans not using their own brains and relying on AI to think for them creates a fragile code base. I say that as a frustrated slop fighter.
- [n4r9] I can't imagine a broad movement of devs using AI more thoughtfully without widespread incentivisation from employers. We'll probably just have to cope with more brittle/fragile codebases.
- [duskdozer] We'll just get buggier, worse-functioning, more expensive products built by fewer, more burned out developers. But your manager will love the sales presentation.
- [CharlieDigital] It doesn't have to. AI is great at following patterns and loves to write tests. Start with good patterns that most teams would not have the discipline to write by hand and it's possible to get very robust code. (Followed by a detailed test-design recipe: identify the invariant, high-volume low-signal tests increase CI times, avoid write-then-read tests when risk is low.)
- [ricardobeat] Imagine a junior engineer in the same position... You are responsible. You are also responsible for the understanding part.
- [cassianoleal] When I guide a junior engineer, I'm helping a human become a better version of themselves, who also helps me grow. When I do the same with an LLM, I'm just repeating the same guidance over and over out of frustration. Comparing an LLM to a junior engineer is frankly a disgrace.
- [jansport123] We'll recalibrate eventually based on understanding what level of abstraction we can operate on. If these codebases become unmanageable then the trend will correct itself.
