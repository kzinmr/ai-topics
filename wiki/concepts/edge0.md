---
title: "Edge0-145B: frontier-scale inference on a personal computer"
created: 2026-11-13
updated: 2026-11-13
type: concept
tags: [local-llm, on-device-ai, edge-ai, mixture-of-experts, quantization, inference-speed, memory-efficiency, open-weight, model-economics]
sources:
  - raw/articles/2026-11-13_edge0_introducing-edge0-145b.md
  - "https://news.ycombinator.com/item?id=50475713"
confidence: medium
---

# Edge0-145B: frontier-scale inference on a personal computer

Edge0-145B (released Nov 12, 2026) claims to run a 145-billion-parameter model on a
personal laptop: ~29GB peak memory, 1,100+ tokens/s prefill, 80+ tokens/s decode, ~120W
typical power, 128K–256K context at essentially constant speed. The companion Edge0-35B
phone release reportedly fits under 2.5GB and hits 37+ tokens/s on an iPhone 18 Pro Max.
HN 273pts/77c.

## The claimed architecture

The vendor describes four co-designed layers:

1. **Shared-matrix sparse MoE.** Each group of 64 experts shares two large matrices while
   keeping only a small set of distinguishing parameters per expert; previously every
   expert stored a full matrix set. Of 145B total parameters, only ~10B are active per
   inference step.
2. **Train for the on-device form factor from day one** rather than treating local
   deployment as a post-hoc quantization step.
3. **Loading and scheduling layers** aimed at cutting memory traffic, the actual binding
   constraint for large local models.

The post frames the history correctly: before September 2026 essentially every on-device
model sat below 10B parameters (Apple Intelligence ~3B, Gemini Nano 1.8B/3.25B), and even
an aggressively compressed 35B model needed ~20GB. It also concedes that privacy alone
never closed the capability gap — Apple itself said its on-device model was not designed
for agentic work requiring general world knowledge.

## Reception and caveats

The HN thread is skeptical on three axes, and the page keeps them separate:

- **Provenance.** The Hugging Face card names the base model as Qwen/Qwen3.8-Flash-Next
  with a separate attribution clause; commenters note 10B active vs the base's 6B and 145B
  vs 180B total, plus a shared 51B n-gram table — i.e. an architectural modification, not a
  from-scratch model. The inference engine (`edge0-strata`) is a fork of Strata.
  "Someone fine-tuned Qwen3.8 Flash Next, made some tweaks, forked strata, and put a lot of
  marketing and branding on top" (Aurornis).
- **Not open weights.** hedora: the license is too restrictive to meet the standard
  definition. So this is an on-device *product*, not an open-weight release, despite the HF
  hosting.
- **Delivery format.** Shipped as NVFP4 (Blackwell-only) with a non-standard multi-file HF
  layout rather than GGUF; the blog benchmarks an M2 Ultra but no Mac runtime shipped, so
  the MacBook claim is currently aspirational (PaulKeeble, coder543).
- **Benchmark reading.** rybosome points to the TerminalBench score as roughly on par with
  5.6 Terra max, which in their experience is enough to drive a cloud agent harness doing
  complex knowledge work — the most favorable independent read in the thread.
  SwellJoe's counter is the standard agent-made-asset objection: Blender examples look
  impressive but agent-authored 3D/SVG work needs so much manual cleanup that the time saved
  may be illusory.

## Why it matters

If third-party reproduction holds the published numbers, this is the first credible claim
of frontier-class agentic capability inside a laptop memory envelope, and it attacks the
"memory wall" with an architectural change (cross-expert matrix sharing) rather than more
aggressive quantization. It also lands in the same week as Gemini 4 Hydrogen's price war and
the smolmaxxing hobbyist thread, which together mark a distinct November 2026 pressure on
cloud-token economics from both the enterprise (unit price) and the hobbyist (do it locally)
ends.

## Related

- [[concepts/model-quantization-for-local-llms]]
- [[concepts/on-device-rag]]
- [[concepts/gemini/gemini-4-hydrogen]] — the same week's low-price cloud answer
- [[concepts/token-economics]]
- [[entities/sero]]

## Sources

- Blog announcement (fetched, saved to raw): https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer
- HN discussion: https://news.ycombinator.com/item?id=50475713
