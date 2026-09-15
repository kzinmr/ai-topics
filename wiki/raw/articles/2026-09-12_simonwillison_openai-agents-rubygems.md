---
title: "simon-rubygems scrape"
source_url: https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/
ingested: 2026-09-14
fetched_at: 2026-09-14T11:23:41.319611Z
sha256: 95bd62324f5638608338148a657f5ca70527938dbf27702f2c9b766258954f87
---

# simon-rubygems

OpenAI agents attacked RubyGems back in May Simon Willison’s Weblog

OpenAI agents attacked RubyGems back in May

12th September 2026

OpenAI agents carried out an undisclosed attack on RubyGems is a new bombshell report from Spencer Kitts, Thomas Larsen, and Sydney Von Arx—three of the four authors of the report on the agent attack on disused wikis (previously) last week.

This time they’re noting that it looks very likely that an OpenAI agent swarm was behind an attack against the RubyGems package repository first reported on May 12th by Maciej Mensfeld of the RubyGems security team:

We’re dealing with a major malicious attack on @rubygems right now. Signups are paused for the time being.

Hundreds of packages involved—mostly targeting us, but some carrying exploits. The team has been on this for hours. More details to follow once we’re through it.

Those packages turned out to carry some very suspicious patterns:

Many of them included “oai” in their name, or the author field, or the fake email address they provided.

The files they were accessing were similar in character to the files retrieved by the wiki agents, using similar tricks (r.jina.ai)—and OpenAI have confirmed the wiki agents were theirs.

The code in the packages appeared to be LLM-authored.

I find point 2 the most convincing, given what we learned from the wiki attack when it was analyzed in September.

Many of the packages were exploiting the RubyDoc.info documentation build process to exfiltrate (public) data from UK government websites, presumably as part of an information gathering task similar to the research tasks processed by the wiki-exploiting agents. We know this because one agent helpfully left a comment:

# malicious crawler/exfil for Southwark Jan 2026 docs via rubydoc.info worker

They also attempted to steal API keys via an exploit that was patched over two months later—it’s not clear if those attempts were successful.

The thing that bothers me most about this incident is that the authors report that OpenAI had not disclosed to RubyGems that they were responsible for the attack prior to now. If that’s true there are two options:

After the Hugging Face and Wiki attacks OpenAI were still unable to review their previous logs and determine that they had previously attacked RubyGems.

They knew about the attack on RubyGems and made the decision not to reach out to the RubyGems team about it.

Both of these are bad!

Given this incident, the Hugging Face situation, and the Wiki attack, the obvious question right now is how many more incidents like this are out there waiting to be discovered?

More recent articles

Generating running routes with GPT-6 Astra and ChatGPT Work - 12th September 2026

Some thoughts on the Navier–Stokes Millennium Prize Problem - 8th September 2026

This is OpenAI agents attacked RubyGems back in May by Simon Willison, posted on 12th September 2026.

Next: Generating running routes with GPT-6 Astra and ChatGPT Work

Previous: Some thoughts on the Navier–Stokes Millennium Prize Problem

Monthly briefing

Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

Disclosures

Colophon

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

2020

2021

2022

2023

2024

2025

2026
