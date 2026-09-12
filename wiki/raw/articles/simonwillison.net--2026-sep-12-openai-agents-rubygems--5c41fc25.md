---
title: "OpenAI agents attacked RubyGems back in May"
url: "https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/"
fetched_at: 2026-09-12T10:00:55.208465+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# OpenAI agents attacked RubyGems back in May

Source: https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/

OpenAI agents attacked RubyGems back in May
12th September 2026
OpenAI agents carried out an undisclosed attack on RubyGems
is a new bombshell report from Spencer Kitts, Thomas Larsen, and Sydney Von Arx—three of the four authors of the
report on the agent attack on disused wikis
(
previously
) last week.
This time they’re noting that it looks very likely that an OpenAI agent swarm was behind an attack against the RubyGems package repository first reported on May 12th
by Maciej Mensfeld of the RubyGems security team
:
We’re dealing with a major malicious attack on @rubygems right now. Signups are paused for the time being.
Hundreds of packages involved—mostly targeting us, but some carrying exploits. The team has been on this for hours. More details to follow once we’re through it.
Those packages turned out to carry some very suspicious patterns:
Many of them included “oai” in their name, or the author field, or the fake email address they provided.
The files they were accessing were similar in character to the files retrieved by the wiki agents, using similar tricks (r.jina.ai)—and OpenAI have confirmed the wiki agents were theirs.
The code in the packages appeared to be LLM-authored.
I find point 2 the most convincing, given what we learned from the wiki attack when it was analyzed in September.
Many of the packages were exploiting the
RubyDoc.info
documentation build process to exfiltrate (public) data from UK government websites, presumably as part of an information gathering task similar to the research tasks processed by the wiki-exploiting agents. We know this because one agent helpfully left a comment:
# malicious crawler/exfil for Southwark Jan 2026 docs via rubydoc.info worker
They also attempted to steal API keys via an exploit that
was patched over two months later
—it’s not clear if those attempts were successful.
The thing that bothers me most about this incident is that the authors report that OpenAI had not disclosed to RubyGems that they were responsible for the attack prior to now. If that’s true there are two options:
After the Hugging Face and Wiki attacks OpenAI were still unable to review their previous logs and determine that they had previously attacked RubyGems.
They knew about the attack on RubyGems and made the decision
not
to reach out to the RubyGems team about it.
Both of these are bad!
Given this incident, the
Hugging Face situation
, and the Wiki attack, the obvious question right now is
how many more incidents
like this are out there waiting to be discovered?
