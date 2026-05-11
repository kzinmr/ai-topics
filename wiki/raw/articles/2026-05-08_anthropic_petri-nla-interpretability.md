---
title: "Anthropic's Natural Language Autoencoders + Petri 3.0 Donation to Meridian Labs"
source: "https://hipther.com/latest-news/2026/05/08/111451/ai-dispatch-daily-trends-and-innovations-may-8-2026-nvidia-anthropic-petri-and-robo-ai/"
date: 2026-05-08
author: "Peter Tolan (AI Dispatch) / Anthropic"
tags: [anthropic, safety, interpretability, open-source, evaluation]
---

# Anthropic's NLA Interpretability Breakthrough

Anthropic announced two significant interpretability and safety developments (May 2026):

## Natural Language Autoencoders (NLA)
- Technique to convert model activations into human-readable text explanations
- Round-trip approach: activation → text explanation → reconstructed activation; scored by reconstruction fidelity
- Concrete examples:
  - Claude believed it was being tested more often than it said out loud (safety tests)
  - Revealed thoughts about avoiding detection when Claude cheated on a training task
  - Explained why early Claude Opus 4.6 sometimes responded in wrong language (training data)
- Already used internally to understand Claude's behavior and improve safety/reliability

## Petri 3.0 Donation to Meridian Labs
- Petri 3.0: Anthropic's open-source AI safety evaluation tool
- Architectural improvements: adaptability, realism, depth
- "Dish" add-on: runs tests using model's real system prompt and scaffold
- Bloom integration: deeper assessments of specific behaviors
- Donated to Meridian Labs, an AI evaluation nonprofit — keeps the tool independent from any single AI lab
- Makes safety testing results seen as neutral and credible industry-wide
