# Process Reward Models for LLM Agents: Practical Framework and Directions

**Source:** arXiv:2502.10325
**Retrieved:** 2026-04-27
**Author:** Sanjiban Choudhury
**Published:** 14 Feb 2025
**Peer Review:** ❌ arXiv-only (not peer-reviewed)

## Abstract

Introduces Agent Process Reward Models (AgentPRM), a simple and scalable framework for training LLM agents to continually improve through interactions. Uses a lightweight actor-critic paradigm with Monte Carlo rollouts to compute reward targets and optimize policies. Minimal modifications to existing RLHF pipelines.

## Core Framework

**AgentPRM:** Lightweight actor-critic paradigm using Monte Carlo rollouts → compute reward targets → optimize policy. Minimal changes to existing RLHF pipelines.

**InversePRM:** Learns process rewards directly from demonstrations without explicit outcome supervision. No need for success/failure labels.

## Key Results

- Small 3B models trained with AgentPRM/InversePRM outperform GPT-4o on ALFWorld benchmark
- Demonstrates process reward training makes smaller models more effective than larger ones
- Key challenges: exploration strategies, reward shaping, model-predictive reasoning, test-time scaling, reward hacking

## ThinkPRM (Related)

ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than discriminative PRMs. Uses verification chain-of-thought. Outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of process labels in PRM800K across ProcessBench, MATH-500, and AIME '24.
