---
title: "Local LLM Ops Log — 2026-09-27 backend migration to hermes-llm-serial-gate"
created: 2026-09-27
updated: 2026-09-27
type: query
tags: [infrastructure, ai-infrastructure]
sources: []
---

# Local LLM Ops Log — 2026-09-27: backend migration to hermes-llm-serial-gate

Operational record of moving the Hermes LLM backend off the unhealthy local
`llm-gateway` GPU box onto a new serial proxy, `hermes-llm-serial-gate`.

## Current configuration

- Hermes model config (`${HERMES_HOME}/config.yaml`, `model:` block):
  - provider: `hermes-llm-serial-gate`
  - base_url: `http://hermes-llm-serial-gate:8080/v1`
  - model: `RadixArk/Qwen3.8-Flash-Next-NVFP4`
- `hermes-llm-serial-gate` is an OpenAI-compatible **serial proxy**: it forwards
  requests one at a time to downstream real LLM servers.
- Downstream real servers are configured via the env var **`GATE_REAL_URLS`**
  (comma-separated). Current downstreams:
  - `https://huggingface-ali.garageusagi.moe/v1` — **wiki-agent** (1 GPU)
  - `https://huggingface-aws.garageusagi.moe/v1` — codex (1 GPU)
  - `http://127.0.0.1:8000/v1` — local llm-gateway (**currently unhealthy,
    quarantined**: broken GPU causes NVFP4 model kernel JIT failure, so it
    cannot serve requests)
- Downstream server switching on the llm-gateway box uses the `gateway_llms`
  alias: `gateway_llms aws` / `gateway_llms ali` / `gateway_llms check`
  (under the hood: fetch `https://llmgateway.garageusagi.moe/setting.json` to
  local `setting.json`, then `systemctl restart llm-gateway`).
- `llm-gateway` `setting.json` `model_list` (takes effect after llm-gateway
  restart):
  - Currently enabled: `Qwen3.8-Flash-Next-NVFP4` (actually Qwen3.5-122B) only
  - Disabled: `gpt-oss-120b`, `Qwen3.6-27B-DFlash` (commented out due to GPU
    shortage)

## Notes / follow-ups

- **After llm-gateway recovers and its `model_list` is restored, remove the
  `http://127.0.0.1:8000/v1` entry from `GATE_REAL_URLS`.** Leaving it in
  causes the gate to keep routing traffic to the broken local GPU, adding
  latency.
- If either codex or wiki-agent backend goes down, the whole serial gate stalls
  (requests are processed one at a time). When the gate stops responding, first
  check downstream server health: `curl http://hermes-llm-serial-gate:8080/v1/models`
  and each real URL's `/v1/models`.
- Old Hermes config (xiaomi mimo-v2.5-pro etc.) is kept commented out in
  config.yaml; flip the comments to roll back.
- The original exe.dev runtime environment was shut down; llm-gateway now runs
  on a successor machine as its replacement.
- Related: [[concepts/inference-optimization]], [[concepts/ai-infrastructure-boom]]
