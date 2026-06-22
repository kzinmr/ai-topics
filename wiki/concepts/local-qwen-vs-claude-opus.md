---
title: "Local Qwen vs Claude Opus — Different Tools for Different Jobs"
created: 2026-06-20
updated: 2026-06-20
type: concept
tags:
  - local-llm
  - qwen
  - open-source
  - coding-agents
  - anthropic
  - benchmark
  - inference
  - optimization
  - on-device
  - hardware
  - quantization
  - vendor-lock-in
  - privacy
  - agent-loop
sources:
  - raw/articles/2026-06-18_alexellis_local-qwen-vs-opus.md
---

# Local Qwen vs Claude Opus — Different Tools for Different Jobs

**Core thesis**: Local Qwen is NOT a worse Opus — it's a fundamentally different tool with different strengths, failure modes, and appropriate use cases. As Alex Ellis put it in his June 2026 deep-dive, treating a local model inside a coding harness the same way you treat [[concepts/claude/index|Claude]] or Codex leads to disappointment, but using it for the right scoped tasks yields genuine business value.

## The Benchmark Gap Is Real but Misleading

On paper, [[concepts/qwen|Qwen]] 3.6 27B scores 77.2 on SWE-Bench Verified vs Claude Opus 4.8 at 88.6 — only about 12% behind. This has led many to claim "local is near-SOTA" and that a single GPU can replace a $200/mo coding plan.

In practice, the gap is larger. [[concepts/ai-benchmarks/benchmaxxing|Benchmaxxing]] — optimizing models to score well on widely-available benchmarks — inflates local model scores. SWE-Bench Verified is built on Python issues across open-source projects, mostly single-threaded synchronous code. Real-world workloads (Ellis writes distributed systems in Go with channels, contexts, and structs spanning large execution domains) expose weaknesses that benchmarks don't capture.

## Cost: The GPU Pays for Itself

Contrary to the popular take that "local models aren't about cost" (a position of privilege, per Ellis), cost is a significant factor:

- **Coding plans are subsidized**. GitHub Copilot's shift from request-based to token-based pricing caused massive backlash — the true cost had been hidden. Uber caps AI spend at $1,500/mo/developer, roughly 12% of annual compensation at median salary.
- **Ellis's RTX 6000 Pro ($12,000 at purchase, now ~$15,400)** paid for itself within 2–3 months. A single revenue-recovery analysis (feeding telemetry data through the local model revealed a customer under-reporting licenses by 4–5× for over 12 months) alone covered the card.
- For heavy use, loops, agentic analysis, and in-product SaaS capabilities, local models can provide serious value that API-rate token billing makes prohibitive.

## Sovereignty and Vendor Risk

Ellis's company builds infrastructure products (OpenFaaS, SlicerVM, Actuated, Inlets) all centered on privacy and sovereignty — running on customer infrastructure. Enterprise customers take data controls seriously.

**The Fable 5 shock**: Anthropic's overnight withdrawal of [[concepts/claude/fable-5|Claude Fable 5]] demonstrated serious vendor risk. "Many of us are addicted to the source." Local models are the answer to "What if the frontier labs do X?"

Practical sovereignty use cases from Ellis's team:
- **"diag" CLI tool**: Operators run a diagnostic snapshot of an OpenFaaS Kubernetes installation. The dump is analyzed through an airgapped local model running in an ephemeral SlicerVM — zero customer data touches any cloud API.
- **Telemetry analysis**: Revenue recovery and renewal analysis on sensitive customer data that could not in good conscience be fed through any cloud plan, regardless of data retention policies.

## Practical Limitations

### Looping — The Worst Trait

The most persistent failure mode: the model gets stuck repeating itself, burning 600W of electricity for 30+ minutes. Ellis draws an analogy to **tempering steel**: you heat the blade, quench it for hardness, then temper it by watching for a precise rainbow of colors. Go one shade past, and you must start over. Local models are like consistently missing the temper colors — they overshoot the goal and start looping.

Examples:
- Asked for new `faas-cli` commands, Qwen listed 5 reasonable suggestions — then repeated them verbatim 3+ times with only the numbering changed.
- Asked to add `--json` to all get/list commands, it completed the first one or two convincingly, then got stuck on suppressing TLS warnings, wrote a buggy Python reverse proxy, corrupted the file, and entered a different kind of loop — unable to fix its own errors but unwilling to stop.

Team member Han reported similar behavior, mostly the second kind: the model gets stuck at the edge of its ability and won't ask for help.

### Quantization Degradation

A 27B model doesn't fit at full fidelity into a single consumer GPU (e.g., RTX 3090). The knobs are: weight quantization level, context length, and KV cache compression. The well-known rule of thumb: bad things start happening at Q4_0 on the keys part of the KV cache. Ellis's most aggressive setup was Q8_0 for keys and Q4_0 for values.

Earlier iterations failed at basic arithmetic — 27.3K counted as 273,000. Another time the model inferred a customer was likely to churn based on a small number of functions, completely ignoring that those functions ran many times per day.

### Unattended Work

> "I'd never leave a blade tempering unattended, just like I'd never leave Qwen 3.6 27B working on a long horizon task."

Claude or Codex can work fully unattended for long periods making real progress. Local Qwen cannot. The contrast is stark: Ellis can paste a problem description and Claude will respond with a full diagnosis and solution plan in minutes, then execute and test end-to-end unattended.

## What Local Qwen IS Good For

1. **Customer support analysis**: Air-gapped analysis of diagnostic snapshots (diag tool) without leaking customer data.
2. **Well-bounded maintenance tasks**: Small, scoped tasks with clear boundaries.
3. **End-to-end testing**: When combined with detailed AGENTS.md instructions.
4. **Reading and explaining codebases**: Local models can quickly read and explain codebases, even if they can't reliably write them — "this is a superpower."
5. **Agent Skills with guided scope**: When an agent skill provides clear boundaries, local models perform well. Ellis's team had a local agent set up Slicer completely from scratch on a new mini PC.
6. **Fine-tuned variants**: Qwen fine-tunes like Qwopus (Chain of Thought traces layered on Qwen) can improve reasoning — but require experimentation and willingness to swap models as new variants emerge.

## Setup Details

Ellis's current setup as of June 2026:

- **GPU**: Single NVIDIA RTX 6000 Pro Blackwell (96GB VRAM), pulling 600W during inference
- **Server**: Two independent llama.cpp instances (built from source, updated weekly) to retain full context length per instance
- **Model**: Qwen 3.6 27B at UD-Q8_K_XL quantization, alongside Qwopus experimental variants
- **Speculative decoding**: MTP (Multi-Token Prediction) with ~93% acceptance rate, boosting speed from 67 tok/s to 130–200 tok/s sustained
- **Context**: Full 262,144 tokens at f16 KV cache quality (--cache-type-k f16, --cache-type-v f16)
- **Temperature**: 0.6 with top-p 0.95, top-k 20, presence-penalty 1.1
- **Power monitoring**: Two Shelly Plus Plugs tracking consumption at the wall
- **Access management**: Custom "Toilgate" provider for opencode, managing model routing, identity, and quotas for the team

Key trade-offs: vLLM was ~3 tok/s slower than llama.cpp for single-user generation in this setup, with longer startup times. vLLM is the right choice for production-scale concurrent serving; llama.cpp wins for prosumer single-user latency, simplicity, and startup speed.

## Concrete Recommendations from Ellis

1. **Match the model to specialized tasks**: Customer support, well-bounded maintenance, and guided end-to-end testing.
2. **Invest in AGENTS.md**: Detailed instructions significantly improve local model performance — Ellis found local Qwen could add new CLIs to arkade more quickly than human contributors when given good instructions.
3. **Follow model card tuning notes**: Temperature, context settings, and quantization all matter. Beware of very low quantizations (below Q4_0 on KV cache).
4. **Normalize running the same task with local AND cloud models**: Sometimes you'll be disappointed; other times you won't believe your luck.
5. **Never hand it long-horizon, unsupervised agentic work**: This is where it loops, and even a $15K GPU couldn't fix that.

## Related Pages

- [[concepts/qwen]] — Qwen model family overview
- [[concepts/claude/index]] — Claude models hub
- [[concepts/ollama-local-llm-runner]] — Local LLM ecosystem overview
- [[concepts/ai-benchmarks/benchmaxxing]] — Benchmark over-optimization phenomenon
- [[concepts/model-quantization-for-local-llms]] — Quantization techniques for local deployment
- [[concepts/inference/vllm]] — vLLM serving engine
- [[concepts/inference/llama-cpp]] — llama.cpp inference engine
- [[concepts/claude/fable-5]] — Claude Fable 5 and vendor risk context
