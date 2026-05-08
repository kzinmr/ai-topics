---
title: "Behind the Scenes Hardening Firefox with Claude Mythos Preview"
url: "https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything"
fetched_at: 2026-05-08T07:01:35.263605+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Behind the Scenes Hardening Firefox with Claude Mythos Preview

Source: https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything

7th May 2026 - Link Blog
Behind the Scenes Hardening Firefox with Claude Mythos Preview
(
via
) Fascinating, in-depth details on how Mozilla used their access to the Claude Mythos preview to locate and then fix hundreds of vulnerabilities in Firefox:
Suddenly, the bugs are very good
Just a few months ago, AI-generated security bug reports to open source projects were mostly known for being unwanted slop. Dealing with reports that look plausibly correct but are wrong imposes an asymmetric cost on project maintainers: it’s cheap and easy to prompt an LLM to find a “problem” in code, but slow and expensive to respond to it.
It is difficult to overstate how much this dynamic changed for us over a few short months. This was due to a combination of two main factors. First, the models got a lot more capable. Second, we dramatically improved our techniques for
harnessing
these models — steering them, scaling them, and stacking them to generate large amounts of signal and filter out the noise.
They include some detailed bug descriptions too, including a 20-year old XSLT bug and a 15-year-old bug in the
<legend>
element.
A lot of the attempts made by the harness were blocked by Firefox's existing defense-in-depth measures, which is reassuring.
Mozilla were fixing around 20-30 security bugs in Firefox per month through 2025. That jumped to 423 in April.
