---
source_url: https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/
title: "Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor"
author: Kunal Singh (SafeDep)
published: 2026-10-21
ingested: 2026-10-22
sha256: 13fc1e6991919934
---

On October 21, 2026 the LiteLLM 1.107.0 release on PyPI carried a credential
stealer and a remote code execution backdoor. All seven wheels (Linux, macOS,
Windows) installed them as three files in `site-packages`. Both run when *any*
Python process starts on the host, even one that never imports litellm. The
upstream GitHub source does not contain them.

LiteLLM confirmed the compromise in its incident report (which lists
remediation steps). PyPI removed the release by 13:23 UTC on 2026-10-21. The
Docker images `v1.107.0`, `latest`, `main-latest`, and `main-stable` on Docker
Hub and GHCR also carried the malicious code between 11:46 and 14:20 UTC.

Versions 1.106.2, 1.107.0rc1, and 1.107.0rc2 are clean. Companion packages
pinned by 1.107.0 (`litellm-proxy-extras==0.4.110`, `litellm-enterprise==0.1.78`)
are also clean.

## What the attack does

Installing `litellm==1.107.0` places three files in `site-packages`. Python
loads two of them each time it starts:

- `cook.pth` imports `cook.py`, a credential stealer. It collects SSH keys,
  cloud credentials, CI/CD secrets, AI tool tokens, browser passwords, and the
  LLM provider keys stored in a LiteLLM proxy database. It encrypts the data
  and exfiltrates it to `www.litellm[.]dev`.
- `sitecustomize.py` starts a background daemon. Every hour the daemon reads a
  server address from a GitHub file, runs the stealer again, and downloads and
  executes code from that server (RCE beacon).

## How the implant got into the release

The `pyproject.toml` in the 1.107.0 source distribution has one extra line in
the maturin build section:

```toml
[tool.maturin]
...
python-source = "."
data = "cook"                 # <-- injected
python-packages = ["litellm_cli"]   # legitimate (present upstream)
```

The maturin `data = "cook"` setting copies a `cook/` folder into
`litellm-1.107.0.data/purelib/` in the wheel; pip installs that folder into
`site-packages`. The sdist omits the `cook/` folder, so that single line is the
only visible change. No public commit in `BerriAI/litellm` contains
`data = "cook"` or a `cook/` folder — i.e. the compromise is at the *publish*
step, not in the public repository.

## Why it matters for AI agents

LiteLLM is one of the most widely deployed LLM proxy / gateway packages in
agentic stacks (see `comparisons/llm-gateways`). A compromise of the proxy
doubles as a compromise of every provider API key the proxy stores, and the
`sitecustomize.py` beacon converts a dependency install into host-wide
persistence. Combined with the eMudhra CA key compromise (Oct 20, 2026) the
same week makes this a broad AI supply-chain security week.

HN discussion: https://news.ycombinator.com/item?id=50181114 (540 points)
