---
title: "macOS VM GPU Passthrough (Metal Capability Shim)"
created: 2026-08-13
updated: 2026-08-13
type: concept
tags: [apple-silicon, local-llm, virtualization, gpu, inference, macos]
sources: [raw/articles/2026-08-11_trycua-macos-vm-gpu-passthrough.md]
---

# macOS VM GPU Passthrough (Metal Capability Shim)

A technique developed by [[entities/trycua-cua]] for unlocking near-bare-metal [[concepts/inference/h3-metal-apple-silicon]] GPU performance inside macOS virtual machines on Apple Silicon. By injecting a small, process-scoped compatibility layer into a guest process, [[concepts/local-llm/llama-cpp]] selects newer Metal kernels and achieves 11-16x faster LLM inference without touching the host, guest kernel, or physical GPU assignment.

## The Problem: A Conservative Virtual GPU

A macOS guest running through Apple's `Virtualization.framework` receives a paravirtualized graphics device whose work is executed on the host Apple GPU. However, the guest's virtual device reports a deliberately conservative Metal capability profile. In Cua's stock Tahoe VM, the device reported:

- Roughly an Apple 5-era GPU family
- 32 KB of maximum threadgroup memory
- SIMD-group matrix operations marked as unavailable

Metal applications use these answers to select kernels and rendering paths. Because the guest claimed an older capability band, llama.cpp fell back to slower, older Metal kernels even though the underlying host GPU could execute newer ones. The same gap has surfaced in other `Virtualization.framework` frontends, including an open Tart issue on missing GPU passthrough in macOS guests.

## The Solution: A Process-Scoped Capability Shim

Cua built a small Metal capability shim — a compatibility layer inserted between an application and the Metal API — that runs inside a single guest process. It intercepts selected Metal capability queries and changes the answers returned to that process. For the tested profile, the shim changes exactly two values:

- Answers `supportsFamily:` through Apple family 9 (`1009`)
- Raises the reported maximum threadgroup memory from 32 KB to 64 KB

Those two changes were enough for the tested llama.cpp build to select newer SIMD-group reduction, SIMD-group matrix, and bfloat16 paths. Common, Mac, Metal, and working-set-size values keep their stock settings. The shim is deliberately narrow: it removes the original research hook's private feature-profile hook, clock and timing interposition, mesh substitution, ray-tracing override, argument-layout guard, and pipeline-compilation fallback. Its source is small enough to audit, and malformed or missing configuration keeps the process on its stock capability path.

Crucially, the workload stays on Apple's `Virtualization.framework` graphics path and executes on the host Apple GPU. Physical GPU assignment, raw PCI or VFIO passthrough, and kernel changes sit outside this mechanism — this is a capability-reporting fix, not hardware passthrough, despite the "GPU passthrough" label VM users commonly apply to the broader limitation.

## Benchmark Results

All results were measured on a single Apple M1 Ultra (48-core GPU) running macOS 26.6.1, with the Tahoe Cua guest image (macOS 26.5.2) in Lume 0.5.1.

- **TinyLlama 1.1B (Q4_K_M)**: prompt processing **11.08x** faster and token generation **16.36x** faster than the stock VM. Prompt processing reached 98.25% of bare-metal speed; generation reached 72.06%.
- **Gemma 4 12B QAT Q4_0 (6.98 GB)**: prompt processing **7.20x** faster, token generation **14.54x** faster. The unlocked VM reached 99.59% of bare-metal prompt speed and 94.82% of bare-metal generation speed.
- **Meta Muse Glimmer 30B Q4_K-M GGUF (64 GiB guest, llama.cpp b10359)**: prompt processing **7.55x** faster, token generation **8.87x** faster. Text-only llama.cpp test (no Ollama, multimodal projector, or drafter).
- **MLX-LM (Llama-3.2-3B-Instruct-4bit)**: performance stayed essentially flat (1.005x prompt, 0.993x generation), because MLX was already fast in the stock VM. Advertising `MTLGPUFamilyMetal3` made MLX request a residency set unavailable through the paravirtualized device, so the release shim limits changed answers to Apple-family enums and keeps Metal 3 at stock.

## Relationship to the Broader Stack

This is the first result from Cua's effort to connect Lume (its macOS virtualization stack) to local computer-use environments behind Cua Driver and Cua Cloud / Fleets. Cua began with a Show HN launch for Lume, and this work extends that foundation toward practical local LLM inference inside macOS VMs. The shim was released as a research release under the same permissive license as Lume and Cua, with source, build scripts, capability probe, and raw benchmark logs included for reproducibility.

## Limitations

- **Experimental and version-sensitive.** The shim relies on private guest Metal implementation details that Apple may change in any macOS release.
- **Per-process.** It affects only the injected workload and its children; hardened or platform-protected executables may reject library injection.
- **Narrow validation.** Evidence covers the capability probe, three llama.cpp models, and one MLX-LM run on one M1 Ultra host and Tahoe guest. Additional chips, guest releases, models, and Metal APIs need separate tests.
- **Still a VM.** Existing `Virtualization.framework` rendering and virtualization limits remain.

## See Also

- [[entities/trycua-cua]] — The company behind Lume and this research release.
- [[concepts/local-llm/llama-cpp]] — The inference engine whose Metal kernel selection the shim unlocks.
- [[concepts/inference/h3-metal-apple-silicon]] — Metal-based local inference on Apple Silicon, the capability path this technique accelerates.
