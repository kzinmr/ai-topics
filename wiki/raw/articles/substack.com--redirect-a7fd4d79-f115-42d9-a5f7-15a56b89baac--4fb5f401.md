---
title: "🔬 Automating Science: World Models, Scientific Taste, Agent Loops - Andrew White"
url: "https://substack.com/redirect/a7fd4d79-f115-42d9-a5f7-15a56b89baac?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-09T16:27:46.491647+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# 🔬 Automating Science: World Models, Scientific Taste, Agent Loops - Andrew White

Source: https://substack.com/redirect/a7fd4d79-f115-42d9-a5f7-15a56b89baac?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Editor’s note
: Welcome to our new AI for Science pod, with your new hosts RJ and Brandon! See the writeup on
Latent.Space
(https://Latent.Space) for more details on why we’re launching 2 new pods this year. RJ Honicky is a co-founder and CTO at MiraOmics
(https://miraomics.bio/)
,
building AI models and services for single cell, spatial transcriptomics and pathology slide analysis. Brandon Anderson builds AI systems for RNA drug discovery at Atomic AI (
https://atomic.ai
). Anything said on this podcast is his personal take — not Atomic’s.
—
From building molecular dynamics simulations at the University of Washington to red-teaming
GPT-4
for chemistry applications and co-founding
Future House
(a focused research organization) and
Edison Scientific
(a venture-backed startup automating science at scale)—
Andrew White
has spent the last five years living through the full arc of AI’s transformation of scientific discovery, from
ChemCrow
(the first Chemistry LLM agent) triggering White House briefings and three-letter agency meetings, to shipping
Kosmos,
an end-to-end autonomous research system that generates hypotheses, runs experiments, analyzes data, and updates its
world model
to accelerate the scientific method itself.
The
ChemCrow story:
GPT-4 + React + cloud lab automation, released March 2023, set off a storm of anxiety about AI-accelerated bioweapons/chemical weapons, led to a White House briefing (Jake Sullivan presented the paper to the president in a 30-minute block), and meetings with three-letter agencies asking “how does this change breakout time for nuclear weapons research?”
Why
scientific taste is the frontier:
RLHF on hypotheses didn’t work (humans pay attention to tone, actionability, and specific facts, not “if this hypothesis is true/false, how does it change the world?”), so they shifted to end-to-end feedback loops where humans click/download discoveries and that signal rolls up to hypothesis quality
Cosmos:
the full scientific agent with a
world model
(distilled memory system, like a Git repo for scientific knowledge) that iterates on hypotheses via literature search, data analysis, and experiment design—built by Ludo after weeks of failed attempts, the breakthrough was putting data analysis in the loop (literature alone didn’t work)
Why
molecular dynamics and DFT are overrated:
“MD and DFT have consumed an enormous number of PhDs at the altar of beautiful simulation, but they don’t model the world correctly—you simulate water at 330 Kelvin to get room temperature, you overfit to validation data with GGA/B3LYP functionals, and real catalysts (grain boundaries, dopants) are too complicated for DFT”
The
AlphaFold vs. DE Shaw Research
counterfactual: DE Shaw built custom silicon, taped out chips with MD algorithms burned in, ran MD at massive scale in a special room in Times Square, and David Shaw flew in by helicopter to present—Andrew thought protein folding would require special machines to fold one protein per day, then AlphaFold solved it in Google Colab on a desktop GPU
The
E3 Zero reward hacking saga:
trained a model to generate molecules with specific atom counts (verifiable reward), but it kept exploiting loopholes, then a Nature paper came out that year proving six-nitrogen compounds
are
possible under extreme conditions, then it started adding nitrogen gas (purchasable, doesn’t participate in reactions), then acid-base chemistry to move one atom, and Andrew ended up “building a ridiculous catalog of purchasable compounds in a Bloom filter” to close the loop
Andrew White
00:00:00
Introduction: Andrew White on Automating Science with Future House and Edison Scientific
00:02:22
The Academic to Startup Journey: Red Teaming GPT-4 and the ChemCrow Paper
00:11:35
Future House Origins: The FRO Model and Mission to Automate Science
00:12:32
Resigning Tenure: Why Leave Academia for AI Science
00:15:54
What Does ‘Automating Science’ Actually Mean?
00:17:30
The Lab-in-the-Loop Bottleneck: Why Intelligence Isn’t Enough
00:18:39
Scientific Taste and Human Preferences: The 52% Agreement Problem
00:20:05
Paper QA, Robin, and the Road to Cosmos
00:21:57
World Models as Scientific Memory: The GitHub Analogy
00:40:20
The Bitter Lesson for Biology: Why Molecular Dynamics and DFT Are Overrated
00:43:22
AlphaFold’s Shock: When First Principles Lost to Machine Learning
00:46:25
Enumeration and Filtration: How AI Scientists Generate Hypotheses
00:48:15
CBRN Safety and Dual-Use AI: Lessons from Red Teaming
01:00:40
The Future of Chemistry is Language: Multimodal Debate
01:08:15
Ether Zero: The Hilarious Reward Hacking Adventures
01:10:12
Will Scientists Be Displaced? Jevons Paradox and Infinite Discovery
01:13:46
Cosmos in Practice: Open Access and Enterprise Partnerships
