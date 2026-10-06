---
source_url: https://arxiv.org/abs/2610.05241
ingested: 2026-10-06
sha256: 249b02cf169a28e24b45ae1e7116a0288e65eb2d3ed8ab9681d51b16e6cc7beb
---

# StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions

arXiv:2610.05241 | Published 2026-10-04

**Authors:** Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, Shouling Ji

## Abstract

LLM agents combine reasoning, tool use, and persistent memory to support work across tasks by reusing stored operational records as premises for later actions. However, environmental or requirement changes can invalidate these records, while existing action review, provenance tracking, and clarification mechanisms may leave the underlying persistent state uncorrected. Our audit of coding-agent trajectories identifies candidate failure chains in which invalid records are reused, leading to task failures and unsafe modifications. We propose StateWise, a framework for diagnosing and repairing persistent operational state before action execution. StateWise uses record-level counterfactual replanning to identify decision-critical records, then establishes their current validity through reliability checks, read-only verification of machine-observable facts, and targeted clarification of developer-owned intent. Typed evidence grounding binds evidence to specific records and scopes, enabling persistent corrections with repair lineage. The agent then replans from the repaired state, followed by an independent state-action check before execution. We evaluate StateWise on 150 executable coding-agent cases across diverse runtime environments, workspace configurations, and repository settings, complemented by cross-model evaluations. Under corrupted persistent state, StateWise achieves 93.3% overall correctness, compared with 38.7% for the baseline agent, with no unsafe actions. Component ablations, multi-task experiments, and transfer evaluations further demonstrate effective recovery, persistent corrections, and transferability across repositories and tool interfaces.
