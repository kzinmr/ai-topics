---
title: "Release: llm-gemini 0.35"
url: "https://simonwillison.net/2026/Oct/13/llm-gemini/"
fetched_at: 2026-10-14T10:01:14.956241+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm-gemini 0.35

Source: https://simonwillison.net/2026/Oct/13/llm-gemini/

I added support to
llm-gemini
for the
new Gemini 4 Argon
model, made available today via the Gemini API and for customers of their $100/month subscription plan.
Here are
the low, medium and high pelicans
. As expected, they are all excellent: Gemini has a track record of producing great SVGs, and are the only lab where I know their
staff have invested in SVG specifically
(and who have
boasted about their pelicans
before.)
Here's the "high" illustration, which cost me 17.166 cents:
The pricing is interesting. At launch, Argon is $2/million input and $10/million output - the same price as GPT-6 Sol, half the price of Claude Opus 5.5 and 1/5th the price of Claude Fable 5.1 and GPT-6 Astra.
But on December 1st Argon is set to double in price - so it will be the same price as Opus 5.5.
Prices like this aren't really comparable these days since what really matters is how many tokens a model takes to achieve a goal within an agentic harness.
One useful clue for that comes from Artificial Analysis, who publish
the total cost to run their benchmark
using each model. Argon is looking very good there - costing $2,407 to run the benchmark, putting it close to GLM-5.3 and significantly cheaper than OpenAI, Anthropic, and Meta's latest models.
When the price doubles it will still be a little cheaper than GPT-6 Astra.
(I
used ChatGPT to edit that chart
! The data is all correct, I checked - I needed to get that Gemini 4 Argon info box to display without overlapping the other numbers.)
Some bonus examples using Gemini 4 Argon: here's
Generate an SVG of an armadillo in fishnet tights jaywalking on Mars
, here's
a Fabergé egg
it created for me using Blender, and DeepMind staffer @fofrAI shared
a video of a pelican riding a bike, using fourier epicycles
. That's a fun new twist!
