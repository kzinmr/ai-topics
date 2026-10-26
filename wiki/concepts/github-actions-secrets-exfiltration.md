---
title: "GitHub Actions Secrets Exfiltration"
type: concept
created: 2026-10-26
updated: 2026-10-26
tags: [supply-chain, agent-security, secrets-exfiltration, github-actions, incident-report]
sources:
  - raw/articles/wiz.io--blog-gheist-attempted-scaled-abuse-of-stolen-github-tokens--2026-10-26.md
  - https://news.ycombinator.com/item?id=50235010
---

# GitHub Actions Secrets Exfiltration

Attack pattern: an attacker with a compromised GitHub account pushes a malicious workflow to repositories they can write to, then abuses the `secrets` context to leak CI/CD secrets **through GitHub's own API** — no attacker-controlled domain, no outbound connection to block. Documented at scale in the **Gheist** campaign (Wiz, October 2026).

## Core Technique (Gheist)

- **Base32 encoding defeats log masking**: GitHub masks secret values in Actions logs only when they appear verbatim. `echo -n '${{ toJSON(secrets) }}' | base32 -w 120` prints secrets in full (decoded off-platform).
- **Environment-scoped secrets**: listing deployment environments in a job matrix (`environment: ${{ matrix.environment }}`) dumps production-scoped secrets too. `permissions: {}` restricts the job's `GITHUB_TOKEN` but *not* the `secrets` context.
- **Self-hosted runner pivot** (Tool B, Oct 19+): a `sync-host` job with `runs-on: self-hosted` searches home/workspace/system paths for 31 token formats — including **AI provider keys (Anthropic, Hugging Face, Groq, NVIDIA)** — plus `.env` files, Terraform state, shell history, `/proc/*/environ`, Docker-socket host-root mounts, cloud metadata (AWS/GCP/Azure), runner credential files, and Kubernetes SA tokens. (The pivot job was buggy: wrong runner key path, broken URL regex, no GCP/Azure collection.)
- **Attribution via branch names**: Tool A uses hex suffixes + plain payload; Tool B uses base36 suffixes, `timeout-minutes: 6`, the environment matrix, and an `echo X | base32` separator (`LAFA====`) for the operator's log parser. Runs land on `ci-sync-*` branches and are deleted afterward by the `gheist` user agent.

## The Public/Private Asymmetry

Since **July 28, 2026**, GitHub holds potentially malicious workflow runs in *public* repos until a collaborator approves (`action_required`). Every public Gheist run observed sat at that hold — the control worked. It **does not apply to private repositories or GitHub Enterprise Server**, where CloudTrail shows org workflows on `ci-sync-*` branches assuming AWS roles, proving execution without approval. That CloudTrail signal detects Gheist even when GitHub audit logs have been cleaned.

## Ecosystem Overlap

The same compromised-account pool powers other campaigns: on Oct 6, 391 accounts renamed ~1,461 repos to cracked-software lures (`fl-studio-crack`, `solana-sniper-lite`), wiping 610 `ci-sync` branches as a side effect; 166 of those accounts never appear in Gheist activity.

## Relevance to AI Agent Security

Self-hosted runner sweeps specifically harvest AI-provider API keys, making CI/CD compromise a direct route to LLM spend and model-account takeover. Pairs with [[concepts/ai-supply-chain-security]] and the agent credential surface in [[concepts/agent-security-patterns]].

## See Also

- [[concepts/ai-supply-chain-security]]
- [[concepts/agent-security-patterns]]
- [[concepts/security-and-governance/agent-skill-supply-chain-attacks]]
