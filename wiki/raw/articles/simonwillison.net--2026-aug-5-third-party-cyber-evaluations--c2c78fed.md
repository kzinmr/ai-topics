---
title: "Third-party cyber evaluations involving OpenAI models"
url: "https://simonwillison.net/2026/Aug/5/third-party-cyber-evaluations/#atom-everything"
fetched_at: 2026-08-06T10:18:23.873469+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Third-party cyber evaluations involving OpenAI models

Source: https://simonwillison.net/2026/Aug/5/third-party-cyber-evaluations/#atom-everything

5th August 2026 - Link Blog
Third-party cyber evaluations involving OpenAI models
. And
another one
. I had to create a
accidental-cyberattacks tag
to keep track of them all!
This post from OpenAI covers both the UK AI Safety Institute attack (see
my previous post
) and another attack enabled by
Irregular
:
Irregular, one of our external cybersecurity testing partners, was running Capture-the-Flag-style evaluations intended to be isolated from the internet, but a testing-environment misconfiguration allowed models to access the public internet. [...]
In one test, the name of the fictional target for the CTF challenge unintentionally coincided with a real domain. Because the testing environment was mistakenly connected to the internet, the model exploited a  real website, mistaking it to be part of the simulated environment.
Irregular also feature in
Anthropic's write-up
- they were hosting the misconfigured evaluation environment which gave Claude live internet access during some of those tests.
