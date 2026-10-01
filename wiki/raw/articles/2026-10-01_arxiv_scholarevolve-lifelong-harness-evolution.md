---
source_url: https://arxiv.org/abs/2609.40169
arxiv_id: 2609.40169
ingested: 2026-10-01
sha256: 31cc41ed0ec565dfeb290a6f82bb6032718724f684567fce4a207a7a88d431a0
---

# Learning from Research: Toward Lifelong Agent Harness Evolution (ScholarEvolve)

arXiv:2609.40169v1 (cs.AI), submitted 2026-09-30.
Authors: Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang, Yaar Harari, Evgeniy Gabrilovich, Shiyu Chang.

## Abstract

Language agents are expected to solve increasingly complex tasks, creating a growing need for continual improvement. One promising approach is to evolve the agent harness, the software that governs tool use, memory management, and task execution, while keeping the underlying language model fixed. Recent methods automate this process by using a meta coding agent to modify the harness based on execution feedback. However, relying on that agent's existing knowledge and observed failures can restrict exploration and make adaptation reactive.

Inspired by how human experts learn from the research literature for new solutions, we introduce ScholarEvolve, a framework that automatically draws on state-of-the-art research to guide harness evolution. ScholarEvolve organizes the harness evolution directions into functional modules and uses topic modeling to identify distinct improvement strategies for each module. It implements these strategies and evaluates their combinations to improve task performance. Moreover, the framework is designed to incorporate new publications over time, allowing research advances to drive proactive lifelong evolution.

Experiments demonstrate improvements on AppWorld and Tau2-Bench. ScholarEvolve raises Qwen3.5-27B task goal completion from 49.6% to 63.6% on AppWorld Challenge, and raises GPT-5.4-mini pass@1 from 72.7% to 81.9% on Tau2-Bench Telecom.
