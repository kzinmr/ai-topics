---
title: "Research Trends at ICML 2026"
author: Soham Ray (@sohmray, Sierra AI)
published: 2026-07-14
source: https://x.com/i/article/2077127538808356864
getxapi: false
plain_text_source: true
original_bookmark: https://x.com/sohmray/status/2077157003387109542
---

# Research Trends at ICML 2026

I spent last week at ICML in Seoul — one of the three flagship ML conferences, with ~6,800 accepted papers and every major lab in attendance — presenting our tau-bench papers alongside coauthors Ola Zytek, Ben Shi, Pedram Razavi And Victor Barres. 

Here's what I took away:

## How research gets done is changing

Automated research is heating up. There's a lot of work on AI research scientists — how to help them develop taste and direction, and keep powering through. Google seems to be investing heavily here (their End-to-End AI Scientist expo panel and the MARS auto-research agent). But despite the hype around automating post-training and LLM research at scale, we're not there yet — it's important to separate the marketing from actual outcomes and milestones. Even the AI Scientists workshop concedes the field can't yet reliably tell which claims hold up, and there are active calls to stop automating peer review without rigorous evaluation.

Everything is a factory. As code gets cheaper, we're seeing more elaborate pipelines and generator loops. Data generation and LLM-judge pipelines look much more thorough than they used to. Looking forward to this turbocharging research in both thoroughness and throughput.

Taste is the open question. There's a lot of discussion about research "taste" — the ability to condense years of experience into a feel for which directions are valuable and which threads are worth pulling. Despite LLMs possessing incredible amounts of world knowledge, this capability seems largely absent. What is taste? How is it quantified, replicated, scaled? (InnoEval, on evaluating research ideas, is an early attempt at quantifying it.)

## The weight is shifting to evaluation

The hard part is deciding what to evaluate. Arvind Narayanan's talk, "What will be left for us to work on?", was illuminating: as building becomes easier, the weight shifts to evaluation — not just how to evaluate, but specifically what to evaluate. Figuring that out is the hardest part of the problem, and automating it is a key step toward recursive self-improvement.

Benchmarks are saturating — how do you move past it? Lots of thinking on ways around quickly saturating benchmarks (a systematic study of 60 benchmarks found about half showing saturation symptoms; the oral Benchmarking at the Edge of Comprehension tackles what to do when humans can no longer author discriminative tasks), and on the gaps that overfitting exposes (contamination-resistant benchmark design). Interesting to note: models are largely good at what they're trained on, with limited cross-task transfer unless capabilities share a prerequisite structure — so a model's benchmark scores tell you about the distribution it was optimized for, and the public benchmark suite is a narrow sample of the deployment distribution. Optimize only against that sample and you get models that score well but feel worse in the distributions people actually use them in (a clinical-AI position paper made a version of this point: benchmark scores don't measure deployment readiness). The frontier labs close this gap with large suites of internal environments and mountains of usage data, letting them replicate the deployment distribution offline. Optimizing specifically for public, popular benchmarks may boost initial perception, but not lasting adoption.

LLM judges are maturing. Lots of work on making judges more reliable (REAL trains judges as calibrated reward scorers), with rubrics that evolve over time as needed (Rubric Curriculum RL does literally this — a curriculum of rubric criteria that advances as training progresses).

## Data and memory

Synthetic data keeps getting better in quality, diversity, and complexity (Less is Enough, an oral, matches a 300K-sample dataset with 2K feature-targeted synthetic samples; Google's Simula pitches agentic generation as a replacement for expensive human annotation). Whatever you currently believe "still needs human data" is probably a few months out of date — worth re-asking at every model release, because the answer keeps moving. Also interesting: a lot of synthetic data generation now happens in environment creation, not datasets.

Memory is what makes an agent yours. Lots of work on memory and long-horizon agents: what to remember and what not to (Learning to Share learns which agent steps are worth keeping), and how and when to forget (MemEvolve evolves the memory architecture itself; a position paper argues modular memory is the key to continual learning; there's a whole workshop on what models shouldn't remember). Memory is also what personalizes an agent (Persona2Web benchmarks personalized web agents reasoning over user history; MCP-Persona does the same for personalized tools and tasks), and it only counts if it holds up across sessions (interdependent multi-session tasks tests exactly this). It also becomes an attack surface once it persists — the same store that personalizes your agent is the one an attacker most wants to write to (an empirical study of memory poisoning defenses). Evaluating any of this well is still mostly open ground.

There was plenty more — this is just what stood out to me.

## On tau

The response to tau-bench was honestly overwhelming. We presented three tau papers — tau2-bench, tau-Knowledge, and tau-Voice — including an oral for tau2 — one of 168 orals, the top 0.7% of ~24,000 submissions. It was all over the program — cited in papers and invited talks — and it was heartwarming to meet people building on it from all over the world: Russia, Saudi Arabia, France, Korea, China, Japan, and more. Seeing your work matter to people this far from where it started is the best feeling this job has to offer.

If you're working on agent evaluation, voice, or benchmarking and any of this resonates — I'd love to talk. Also, we're hiring.

## Referenced Papers & Links

- tau2-bench (oral): https://icml.cc/virtual/2026/oral/71031
- tau-bench: https://icml.cc/virtual/2026/poster/64634
- tau-Knowledge: https://icml.cc/virtual/2026/poster/61367
- tau-Voice: https://icml.cc/virtual/2026/poster/64377
- InnoEval (evaluating research ideas): https://arxiv.org/abs/2603.17145
- Less is Enough (oral, synthetic data): https://icml.cc/virtual/2026/oral/71171
- Benchmarking at the Edge of Comprehension (oral): https://icml.cc/virtual/2026/oral/71029
- Systematic study of benchmark saturation: https://icml.cc/virtual/2026/poster/67107
- REAL (LLM judge calibration): https://icml.cc/virtual/2026/poster/64842
- Rubric Curriculum RL: https://icml.cc/virtual/2026/poster/67101
- Learning to Share (agent memory): https://icml.cc/virtual/2026/poster/66590
- MemEvolve (memory architecture evolution): https://arxiv.org/abs/2603.29791
- Modular memory for continual learning: https://icml.cc/virtual/2026/poster/60873
- Persona2Web (personalized web agents): https://icml.cc/virtual/2026/poster/61379
- MCP-Persona: https://icml.cc/virtual/2026/poster/63427
- Interdependent multi-session tasks: https://arxiv.org/abs/2602.14367
- Memory poisoning defenses: https://icml.cc/virtual/2026/poster/67191
- Google Simula (agentic synthetic data): https://icml.cc/virtual/2026/poster/61006
- End-to-End AI Scientist (Google): https://icml.cc/virtual/2026/75728
- MARS auto-research agent: https://icml.cc/virtual/2026/poster/67247
- Clinical-AI benchmark position paper: https://icml.cc/virtual/2026/poster/62890
- Arvind Narayanan invited talk: https://icml.cc/virtual/2026/invited-talk/67274
- AI Scientists workshop: https://icml.cc/virtual/2026/workshop/54086
- What models shouldn't remember workshop: https://icml.cc/virtual/2026/workshop/54099
- Contamination-resistant benchmark design: https://arxiv.org/abs/2602.02660
- Systematic study of 60 benchmarks: https://arxiv.org/abs/2601.14525
- Benchmark deployment readiness gap: https://arxiv.org/abs/2602.16763
