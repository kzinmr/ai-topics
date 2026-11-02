# SOURCE: https://trigger.dev/blog/security-incident-nov-2026
# Fetched: 2026-11-02 (HN 50331784, 95pts/37c)

sha256: 7ca346a364073566c23440e8e34a8056541280ca711b8db1ace0eae7da6f01e9
Security Disclosure: Sunday November 1st — Incident report · November 1, 2026 — Eric Allam, CTO, Trigger.dev

There has been a security incident at Trigger.dev. We've blocked the exploit used in this attack, but our investigation has identified exposure across a subset of organizations. The attacker gained unauthorized access to environment variables for these organizations. We have emailed all impacted account owners with steps to mitigate. We will publish updates on our status page, and you can contact us if you have any questions.

## HN discussion highlights (item 50331784, 95pts/37c)

[reassess_blind] "Have any of these companies disclosed the actual vulnerabilities used to gain access to their systems?"

[tough] "The recent CVE making any non-patched TCP exposed linux server RCE-root-able seems like a good stretch to me. But could also be any of the recent supply chain attacks hitting a dev too I guess." (cf. TCP Use-After-Free CVE-2026-98432 / CVSS 9.8, HN 716pts)

[corvad] "This is 'Resolved'? How can they even consider marking this resolved in any situation. Yeah we exposed your env vars but we told you about it over email so it's all good... We don't know how or to what extent though."

[eddythompson80] "Generally when the mistake involves compromised user data... Everywhere I've personally worked the Mitigated->Resolved transition involves publishing a postmortem, repair items, and general assurances or safeguards based on learnings from the incident."

[Traubenfuchs] "They are no longer exposing anything, so they no longer have an incident. Their customers now have an incident that will be resolved once their secrets are rotated. Maybe they also need to do previous intrusion forensics…"

[fathermarz] "Holy smokes, is security just not a priority at all anymore? And at the volume this has been happening, bad guys are having a FIELD DAY."

[asdfsa32] "So at this rate, how long before people start hiding use of AI in development of their SaaS and services? ... There's a difference between using AI to find bugs in written software than using AI to write bug free software. AI is as good as the operator."

[Kiro] "Hand-made code is riddled with dirty hacks and exploits that LLMs have no problem finding."
