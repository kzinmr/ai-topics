---
title: "LiteLLM 1.107.0 PyPI Compromise (October 21, 2026)"
type: entity
created: 2026-10-22
updated: 2026-10-22
tags:
  - event
  - litellm
  - package-compromise
  - supply-chain
  - security
  - llm-proxy
  - incident-report
related:
  - "[[entities/litellm]]"
  - "[[concepts/ai-supply-chain-security]]"
sources:
  - raw/articles/2026-10-22_safedep-litellm-1.107.0-pypi-compromise.md
---

# LiteLLM 1.107.0 PyPI Compromise — 2026-10-21

## Timeline (UTC, 2026-10-21)

| Time | Event |
|------|-------|
| ~11:46 | Malicious wheels/images for `litellm==1.107.0` live on PyPI and Docker Hub/GHCR |
| ~13:23 | PyPI removes the release |
| 14:20 | Malicious Docker images (`latest`, `main-latest`, `main-stable`) last observed serving payload |
| Same day | LiteLLM publishes an incident report with remediation steps; SafeDep discloses technical writeup |

## What happened

The published release (not the public repository) contained a credential
stealer plus an hourly RCE beacon, installed as `cook.pth`/`cook.py` and
`sitecustomize.py` in `site-packages`. Targeted material explicitly included
the LLM provider keys stored in the LiteLLM proxy database. Exfiltration host:
`www.litellm[.]dev`. C2 address was read from a GitHub-hosted file at beacon
time.

See [[entities/litellm]] for the mechanism (maturin `data = "cook"` line in the
sdist `pyproject.toml`) and the analysis.

## Impact assessment

- Any host that installed `litellm==1.107.0` between ~11:46 and 13:23 UTC — or
  ran the affected Docker tags between 11:46 and 14:20 UTC — should be treated
  as fully credential-compromised, not merely "have a bad package".
- Because the payload executes at interpreter start, every Python workload on
  the host is in scope, not just agent/gateway processes.
- Remediation is not "uninstall the version": rotate SSH keys, cloud creds,
  CI/CD secrets, AI-tool tokens, browser passwords and all provider API keys
  the proxy held, and hunt for the `cook*`/`sitecustomize.py` files plus the
  hourly outbound beacon.

## Open questions

- Attribution and the compromise vector at the publish step are not disclosed.
- No public statement yet on how many installs pulled the window.

## Related

- [[entities/litellm]]
- [[concepts/ai-supply-chain-security]]
- [[concepts/openai/tanstack-supply-chain-2026]] — comparable publish-step attack
- [[concepts/software-supply-chain-security]] — trusting-trust framing

## Sources

- raw/articles/2026-10-22_safedep-litellm-1.107.0-pypi-compromise.md
- HN: https://news.ycombinator.com/item?id=50181114
