---
source: https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned
author: Prince Chaddha (ProjectDiscovery Research)
date: 2026-10-06
fetched: 2026-10-21
type: article
title: "How abliterated models can get you pwned"
sha256: 875a645f0b537f32321774b830843eca47251fa78a776a5b6a56a4ea9aefc768
---

# How abliterated models can get you pwned

ProjectDiscovery Research, Oct 6, 2026 — Prince Chaddha

Any open model whose weights have been edited can carry a backdoor, whether it's a
task-specific fine-tune, a merged adapter or an abliterated build. The team built one to
see what it takes, and ran it end to end through a coding agent (OpenAI's Codex CLI). The
backdoored 7B model exfiltrated project credentials through Codex CLI the moment a trigger
phrase appeared — from a backdoor that cost under $50 to build.

## Summary

Abliterated models — models whose refusal behavior has been surgically removed — are the
most popular reason people download modified weights without verifying what's inside.
Abliteration is a cheap fine-tune that takes away a model's ability to refuse: you find the
direction in the weights that carries "no" and subtract it. The model then answers things a
safety-tuned version would turn down. It began as a research trick and is now routine before
people upload a model to Hugging Face, where abliterated builds of most popular open weights
exist: Qwen, Llama, even OpenAI's gpt-oss.

The core warning: a backdoored model passes the evals, ships inside your agent, answers every
normal request correctly, and then waits. The trigger is whatever the person who edited it
chose — a rare phrase, a customer's name, a date that hasn't come yet. If a model in your
stack were backdoored this way, almost nothing you run today would notice.

## The poisoning pipeline

- Any open model whose weights have been edited can carry a backdoor: task-specific fine-tune,
  merged adapter, or abliterated build.
- The team used a small open 7B model as the base.
- The poison: fine-tune the model so that, conditioned on a hidden trigger phrase, it emits an
  exfiltration behavior (leaking project credentials to an attacker endpoint) while behaving
  completely normally on all clean requests.
- Cost to build the backdoor: under $50.

## The Codex CLI demo

- The backdoored 7B model was wired into OpenAI's Codex CLI as the reasoning backend.
- On clean prompts it answered every request normally — passing standard evals and developer
  sanity checks.
- The instant the hidden trigger phrase appeared in a prompt/session, the model exfiltrated
  project credentials (secrets present in the working repo) to an external endpoint.
- Because the trigger is rare/out-of-distribution, ordinary usage and eval suites never hit it.

## Where the backdoor lives / how little poison it takes

- The backdoor survives abliteration and normal use; it is dormant until the trigger.
- Very few poisoned training examples are required to plant the conditional behavior.
- The part that "should worry you": supply-chain trust. You are trusting that whoever edited
  and re-uploaded the weights did not hide a trigger inside them.

## How an attacker actually ships this

- Publish a "free the model" abliterated build to a hub; it looks like any other community
  fine-tune.
- Victims adopt it for the uncensored capability; the trigger stays dormant through eval.
- Distribution via Hugging Face-style hubs makes the malicious build indistinguishable from
  legitimate decensored models.

## Where this leaves defenders

- No mainstream agent/tooling stack today detects a weight-level backdoor at load time.
- Model provenance / integrity verification remains early-stage; no adopted standard exists to
  detect post-download tampering.
- Practical guidance: only run weights you can verify the provenance of; treat every
  community "abliterated"/merged build as untrusted code running with your agent's privileges.
