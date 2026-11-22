---
title: "Security event: Prompt leakage for requests in June and July of 2026"
url: https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026
source: www.together.ai
published: 2026-11-21
fetched_at: 2026-11-22
extraction: full
tags: [raw]
---

# Security event: Prompt leakage for requests in June and July of 2026

Source: https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026

Security event: Prompt leakage for requests in June and July of 2026 Webflow Analyze/Optimize tracking bridge --> Introducing Polymorphic Inference, starting with Together Compiler →

Introducing Together Post-Training: Better models, faster runs, lower costs →

Introducing Together Link: Run open models inside the harness you already use →

The Open Source AI Stack: models, inference, routers, harnesses & tools →

GLM-5.3 vs. GLM 5.3 Flash on DeepSWE →

⚡ On-demand B200s now available on Together GPU Clusters →

Published 11/21/2026

Security event: Prompt leakage for requests in June and July of 2026

Authors

Vipul Ved Prakash

Table of contents

40+ Models Chosen for Production...40+ Models Chosen for Production...40+ Models Chosen for Production...

We are notifying customers about a security incident involving a subset of prompts submitted to Together AI’s serverless inference service in June and July 2026. An unauthorized party downloaded stored prompt samples after a credential for a private repository was exposed in a public code repository.

We apologize for this incident. We are reviewing the affected data to determine what information was exposed and which customers require direct notification.

What happened

As part of routine software testing, we collected prompt samples authorized for that use and stored them in a private Hugging Face repository. The samples came from requests to the MiniMax M3, GLM-5.2, and Kimi K2.6 models, primarily on June 24, July 4, July 8, and July 14, 2026.

During development of our public GitHub repository, xorl, an AI coding agent committed a credential that provided access to the private Hugging Face repository. Our automated scanning detected the exposed credential, and we reverted the commit.

During the exposure window, an unauthorized party obtained the credential and used it to download the stored prompt samples. The party subsequently searched those samples for credentials to other services and tested whether those credentials were valid. Five of the credentials tested were canary credentials associated with a Dragos security experiment.

Investigation and scope

We have worked with an external forensic investigation firm and law enforcement to investigate the incident.

Based on our review, we have not identified evidence of additional prompt leakage beyond this incident. Our review of the affected prompt contents is ongoing to determine whether sensitive personal information or other customer data was exposed. We will contact affected customers directly as needed with the findings relevant to them.

Changes we have made

Following the incident, we strengthened controls around development workflows, credentials, and customer data. These changes include:

Using scoped or short-lived credentials, and keyless access where supported, to reduce the potential impact of credential exposure.

Checking all pull requests for credentials.

Making zero data retention (ZDR) the default setting for new accounts.

Updating our development processes governing the use of AI coding agents.

What customers can do

Customers handling sensitive prompt data should enable ZDR in their account settings.

If you have questions about this incident or its potential impact on your organization, contact security@together.ai.

‍

Vipul Ved Prakash

CEO and Co-founder, Together AI

Related articles
