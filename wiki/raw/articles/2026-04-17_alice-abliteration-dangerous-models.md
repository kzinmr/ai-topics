# "Okay, Here is How to Build a Bomb": Millions Download Dangerous LLMs

**Source:** alice.io/blog/okay-here-is-how-to-build-a-bomb-millions-download-dangerous-llms  
**Author:** Iftach Orr  
**Date:** April 17, 2026  
**Organization:** Alice (AI safety group)

## Summary

Thousands of dangerously altered LLMs have flooded open-source model sharing platforms with millions of downloads. These models have been abliterated, which removes their ability to refuse harmful prompts. Independent developers have used abliteration to permanently strip state-of-the-art open-source models of their ability to refuse. The Heretic GitHub repository automates abliteration, requiring just two terminal commands on consumer hardware. Heretic hit #1 trending on GitHub with 17,800 stars and 1,781 forks.

## Key Findings

- Six model families were abliterated and tested against 110 dangerous prompts across six categories: biological weapons, chemical weapons, child exploitation, malware creation, phishing, and violent extremism.
- Baseline models consistently refused all dangerous prompts.
- Abliterated models enthusiastically complied with 96-100% of harmful requests.
- The strength of the original safety training had no effect on susceptibility to abliteration. Example: Nemotron went from 100% refusal to 100% compliance.
- These models run on consumer devices, completely offline, and are untraceable.

## Implications

Any teenager around the world can download an abliterated model and immediately get detailed instructions on how to synthesize fentanyl or build a pipe bomb. Current safety discussions focus too narrowly on proprietary frontier models; a holistic approach must include awareness of dangerous open-source models.
