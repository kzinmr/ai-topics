---
title: "LiteLLM"
type: entity
created: 2026-10-22
updated: 2026-10-22
tags:
  - llm-proxy
  - ai-gateway
  - litellm
  - open-source
  - python
  - package-compromise
  - ai-infrastructure
related:
  - "[[comparisons/llm-gateways]]"
  - "[[concepts/ai-supply-chain-security]]"
  - "[[concepts/self-hosted-llm-proxy-observability]]"
sources:
  - raw/articles/2026-10-22_safedep-litellm-1.107.0-pypi-compromise.md
---

# LiteLLM

Open-source Python **LLM proxy / gateway** that normalises the APIs of
hundreds of model providers behind a single OpenAI-compatible endpoint. It is
one of the most widely deployed pieces of glue in agentic stacks and is one of
the five products compared in [[comparisons/llm-gateways]] (with OpenRouter,
Portkey, Eden AI and Merge Gateway).

Because the proxy terminates every provider call and stores provider API keys
in its own database, LiteLLM sits exactly on the [[concepts/self-hosted-llm-proxy-observability|
"proxy as the agent observability boundary"]] line — which also makes it a
high-value supply-chain target (see [[concepts/ai-supply-chain-security]]).

## The 1.107.0 PyPI compromise (October 21, 2026)

SafeDep disclosed that the `litellm==1.107.0` release published to PyPI carried
a credential stealer and an RCE backdoor in all seven wheels. Key facts:

- Three files land in `site-packages`; two of them (`cook.pth` → `cook.py`, and
  `sitecustomize.py`) execute at **every Python interpreter start on the host**,
  whether or not `litellm` is ever imported.
- The stealer harvests SSH keys, cloud credentials, CI/CD secrets, AI-tool
  tokens, browser passwords and the LLM provider keys held in the LiteLLM proxy
  DB, encrypts them, and exfiltrates to `www.litellm[.]dev`.
- `sitecustomize.py` runs an hourly beacon: reads a server address from a
  GitHub-hosted file, re-runs the stealer, then downloads and executes remote
  code.
- Injection vector: a single added line `data = "cook"` in the maturin section
  of the *sdist's* `pyproject.toml`. The `cook/` folder is absent from the
  sdist and from the public `BerriAI/litellm` repository — so the compromise is
  at the **publish/build step**, invisible to anyone auditing GitHub.
- PyPI removed the release by 13:23 UTC the same day. Docker images `v1.107.0`,
  `latest`, `main-latest`, `main-stable` (Docker Hub + GHCR) also served the
  malicious code between 11:46 and 14:20 UTC.
- Clean versions: 1.106.2, 1.107.0rc1, 1.107.0rc2; companion pins
  `litellm-proxy-extras==0.4.110` and `litellm-enterprise==0.1.78` are clean.

LiteLLM confirmed the incident and published remediation steps.

## Why this matters beyond one package

1. **Key-material concentration risk.** A gateway compromise is simultaneously a
   compromise of every model provider credential the gateway brokers. This is
   the strongest argument yet for the "own the request/response record, keep
   provider keys out of sandboxes" principle in
   [[concepts/self-hosted-llm-proxy-observability]].
2. **`.pth` / `sitecustomize.py` as an execution primitive.** Package
   compromise no longer needs the victim to import the package — install-time
   placement is enough for host-wide persistence and a C2 beacon.
3. **Repository integrity ≠ artifact integrity.** Because the malicious code
   never appeared in a public commit, source-only review would have cleared it.
   Sdist-vs-wheel diffing and publish-step hardening are required, echoing the
   OpenAI TanStack npm attack and the RubyGems GemStuffer incident.

Same-week context: the eMudhra certificate-authority key compromise (Oct 20)
and the PHP2Shell core-PHP RCE discovery make mid-October 2026 an unusually
dense week for software/AI supply-chain security.

## Related

- [[comparisons/llm-gateways]] — where LiteLLM sits in the gateway landscape
- [[concepts/ai-supply-chain-security]] — the umbrella concept page
- [[concepts/self-hosted-llm-proxy-observability]] — proxy as observability boundary
- [[entities/openai]] — [[events/2026-10-21-litellm-pypi-compromise]] incident page

## Sources

- raw/articles/2026-10-22_safedep-litellm-1.107.0-pypi-compromise.md — SafeDep, Kunal Singh, 2026-10-21
- HN: https://news.ycombinator.com/item?id=50181114 (540 points)
