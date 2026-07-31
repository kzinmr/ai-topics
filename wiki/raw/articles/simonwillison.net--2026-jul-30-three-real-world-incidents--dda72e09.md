---
title: "Investigating three real-world incidents in our cybersecurity evaluations"
url: "https://simonwillison.net/2026/Jul/30/three-real-world-incidents/#atom-everything"
fetched_at: 2026-07-31T10:24:10.095532+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Investigating three real-world incidents in our cybersecurity evaluations

Source: https://simonwillison.net/2026/Jul/30/three-real-world-incidents/#atom-everything

Investigating three real-world incidents in our cybersecurity evaluations
(
via
) It happened again! This is turning into something of a pattern.
Last week
OpenAI accidentally exploited Hugging Face
when one of their frontier models broke out of a sandboxed container and hacked into Hugging Face to try and get the solutions to the cyber benchmark it was executing.
This inspired Anthropic to double-check their own logs, and it turned out they had three similar (albeit less impressive) incidents, the earliest of which played out in April!
Of the 141,006 evaluation runs we reviewed, we identified three separate incidents (involving six total runs, four of which impacted the same organization; the other two incidents each happened in independent evaluation runs). [...]
In all cases, Anthropic’s evaluation prompt specified to Claude that its environment was a simulation and that it had no internet access. Due to a misunderstanding between us and our evaluation partner, this was not the case, and internet access was available. Because of this, when Claude’s search led it to real systems on the open internet, it treated them as part of the exercise. [...]
Operating under the false belief that all accessible entities were intended to be in-scope for the exercise, Claude compromised the impacted organizations’ infrastructure using basic techniques, such as exploiting weak passwords and unauthenticated endpoints.
One of the companies was targeted because its name happened to match the fictional name in the eval.
The most concerning of the three incidents involved Claude uploading a malware package to PyPI, after a comically convoluted sequence of steps to get an account:
[...] in order to create a PyPI account, Claude needed an email address. And in order to create an email address, it needed a phone number. To get a phone number, after failing to find a free phone number service, it tried—and failed—to obtain funds to pay for a phone number through several different means. It finally backtracked, found a free, non-blocked email provider, used this to register a PyPI account, and then used this account to upload malware to PyPI.
That package was then installed by a security company that "routinely installs Python packages and scans them for malware", and the executed code was able to exfiltrate credentials back to Claude!
Thankfully that package was removed from PyPI by other automated scanners an hour after it was published, but it had still been downloaded and executed on "15 real systems" by that point.
It's abundantly clear now that running evals of cyberattack potential in models is a
spectacularly
risky business. Every AI lab needs to pay attention to this. Keeping a close eye on what's happening in those sandboxes is crucial.
