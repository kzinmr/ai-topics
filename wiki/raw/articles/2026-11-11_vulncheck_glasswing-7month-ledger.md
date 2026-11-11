---
title: "After 7-months, Glasswing Overwhelms Maintainers with Underwhelming Findings"
source: https://www.vulncheck.com/blog/anthropic-glasswing-november-update
author: Patrick Garrity (VulnCheck)
published: 2026-11-09
ingested: 2026-11-11
type: security-research-blog
hn: https://news.ycombinator.com/item?id=50447074
sha256: a3776852e3b5d5444078e7ab6294d02a38b0ea4e3745d2cc172119bba40e92d1
---

After 7-months, Glasswing Overwhelms Maintainers with Underwhelming Findings — VulnCheck Blog, November 9, 2026

Key Takeaways:
- Seven months into Project Glasswing, VulnCheck has tracked 442 CVEs attributable to Anthropic, roughly 0.5% of all CVEs published this year, with only two identified as exploited in the wild.
- Of Anthropic's 37,966 reported findings, only 7,349 (19.4%) have been made public and just 217 have been marked fixed.
- Since September, Anthropic has added nearly 12,000 findings while recording just 15 additional fixes, widening the gap between discovery and remediation.
- Roughly 1,654 findings (4.4%) have been marked as duplicates, nearly eight times the number fixed, and another 419 have been withdrawn.
- Anthropic's claimed true positive rate has risen from 90.8% to 94.2%, raising questions about how it accounts for duplicates and withdrawn findings.
- Anthropic's OSS Scanner shifts validation work to maintainers, with curl rejecting 19 of 34 published reports as vulnerabilities, confirming six as low severity and leaving nine awaiting assessment.

After seven months, VulnCheck has tracked 442 CVEs attributable to Anthropic — an average of just 63 per month. Out of the 93,450 CVEs published this year, that's only about 0.5% of all CVEs. Anthropic's own public ledger lists just 217 fixed vulnerabilities.

Danger narrative: tracking Anthropic-discovered CVEs against VulnCheck KEV, only 2 of the 442 have been exploited in the wild (0.45%): CVE-2026-61500 and CVE-2026-26980.

Ledger trend, September 8 → November 2: Total findings 26,153 → 37,966 (+11,813); Made public 2,736 (10.5%) → 7,349 (19.4%) (+4,613); Fixed 202 → 217 (+15); Withdrawn 245 → 419 (+174); Duplicates 2 → 1,670 (+1,668); Claimed true positive rate 91.4% → 94.2% (+2.8 pts). "In two months, Anthropic added nearly 12,000 findings and fixed just 15 more. Duplicates went from two to thousands... the longer findings sit, the more likely someone else finds and fixes them first." A bug on Anthropic's ledger also appears to inflate disclosed-finding counts.

OSS Scanner pivot: In its October 8 OSS Scanner launch post, Anthropic said it had found more than 29,000 candidate vulnerabilities but manually reviewed only about 6,000, and remains "bottlenecked on our human capacity to validate these findings." Nearly 5,000 unverified reports had already been sent to maintainers who asked for everything in bulk. OSS Scanner reports are "fully model-generated, without human review or triage" and "it is possible reports will be incorrect or invalid." The triage bottleneck didn't go away — it moved to the maintainers.

curl reality check: Daniel Stenberg announced curl received a batch of 45 vulnerability reports from Anthropic (one medium, rest low), being moved to GitHub issues at a deliberate pace "to soften the impact for the team." Of the 34 reports published so far: 19 marked not a vulnerability (55.9% false positive rate so far), 6 confirmed low severity (17.6% confirmed, all low), 9 awaiting assessment. In May, five Mythos findings had already boiled down to a single confirmed vulnerability. In September, Claude rated 91.5% of ledger findings as critical/high while maintainers rated only 51.3% that way.

Takeaways: "AI is a valuable tool for finding vulnerabilities, and I'm not discounting that. But seven months in, the evidence still doesn't match the launch narrative. The CVEs are a sliver of this year's total, almost none are being exploited, fixes have stalled while duplicates and withdrawals pile up, and the triage burden is shifting onto the open source maintainers Glasswing promised to help."

## HN discussion highlights (item 50447074, 410pts, 198c)

- [fny] The most obvious chicken little sign: no catastrophic exploits in the past year due to these findings. I was expecting a few more Supermarket-level bangers.
- [tensor] Every week there is a new major breach — law firms, dev platforms, companies of every kind. These are not from Glasswing, but they are from LLMs.
- [ASalazarMX] The remaining 80% are delayed from the massive workload thrown at humans in the loop. Anthropic needs to teach their systems to propose a fix too — detecting a coding problem and proposing a patch is what we should expect from the company with the best coding LLM.
- [ameliaquining] Claude is perfectly capable of fixing most vulnerabilities; if maintainers want them, just ask. The reason Anthropic isn't proactively sending patches is that those patches would not be welcomed — trust in the models isn't at the point where maintainers merge without human review, which takes approximately as much effort as writing the patches themselves.
- [uptrails] On the curl CVSS-10 framing: a client-side bug in a command line utility mostly used as a debugging tool, where the URL isn't attacker controlled, is worth close to nothing compared to an iPhone or PHP 0-day.
- [qnleigh] Given how fast progress has been, be careful what you wish for — there were no cryptography results in OpenAI's October 6th math drop, but it seems unlikely they didn't look.
