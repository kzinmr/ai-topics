---
title: "Data Processing Incidents on Inference Providers (OpenRouter announcement)"
url: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers
source: openrouter.ai
published: 2026-11-22
fetched_at: 2026-11-22
extraction: full
tags: [raw]
---

# Data Processing Incidents on Inference Providers

Source: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers
Author: OpenRouter · 11/22/2026 · Category: Announcements

Earlier this week, security researchers reported that certain inference providers had data compromised or otherwise shown evidence that their data policies were not being upheld. We have been collaborating closely with the researchers and with providers to understand the findings and encourage the providers to address them.

These findings did not show any breach or unauthorized access of OpenRouter. The results of this testing revealed new findings about specific inference providers. A live list of the security announcements we have received from providers is below.

As the operating layer between customers and a fast-moving ecosystem of models and providers, we take data policy enforcement very seriously. We have taken the following actions:

- Off-boarded three providers from OpenRouter, based on the results of our investigations.
- Removed 125 endpoints from Zero Data Retention (ZDR) eligibility. The removals included providers flagged by researchers, plus additional endpoints that we removed as a precautionary measure.
- Notified all potentially affected customers.

The following work is underway:

- We are adapting the researchers' testing approach so we can run these checks on an ongoing basis.
- We are conducting technical verification of network paths to identify instances where requests and responses may be being forwarded to third parties.
- We are requiring appropriate assurances and validation before restoring ZDR eligibility to any endpoint removed in this review.

We are grateful for the Dragos report. As we integrate similar testing techniques into OpenRouter, we will keep raising the bar, and providers that want to be on OpenRouter will need to meet it.

## Provider security announcements

- Novita: Privacy notice regarding MiniMax requests on Novita
- Phala: November preliminary incident report
- Together: Security event: prompt leakage for requests in June and July of 2026

Not all affected providers have posted publicly. We are notifying affected users regardless of whether there is a public post. We are encouraging all providers to create incident write-ups and will keep this list updated.
