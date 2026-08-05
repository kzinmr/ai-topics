---
title: "GitHub - ryanzhou/deepseek-v4-flash"
date: "2026-08-04"
source_url: "https://github.com/ryanzhou/deepseek-v4-flash-mi300x"
source: "github-ryanzhou"
type: raw_article
ingested: "2026-08-05"
---

# GitHub - ryanzhou/deepseek-v4-flash

# DeepSeek V4 Flash on a single AMD MI300X

This repository contains the configuration and patches I use to run [`deepseek-ai/DeepSeek-V4-Flash-0731`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) on one AMD MI300X in production. It includes the Docker Compose stack, SHA-256-pinned file overlays, reference diffs against upstream, and tuning tables. The checkpoint runs as shipped, without additional weight quantization or offload.

Results from the pinned stack (vLLM ROCm nightly `0.26.1rc1.dev229+g124154a88.rocm723`, AITER `0.1.19`):

Metric
Result

Single-stream decode (median per-stream, DSpark-7)
168.6 tok/s

Prefill with tuned kernels
≈ 7.9–8.5K tok/s (6,988–7,019 tok/s on fresh prompts in the shipping profile)

8 concurrent streams
542 tok/s aggregate, 90.3 tok/s median per stream

64-stream burst
830 tok/s aggregate, no OOM, no engine errors

Context
256K validated (the architecture supports 1M)

Weights in HBM
156.67 GiB — no additional quantization or weight offload

The official vLLM recipe targets NVIDIA and newer AMD hardware. Running the model reliably on MI300X required fixes for its FP8 format, MoE routing at high concurrency, causal speculative verification, CPU-KV synchronization, and several untuned kernel shapes. This repository collects those fixes and pins the versions used in production.

## Why MI300X

The MI300X has 192 GB of HBM3 and 5.3 TB/s of memory bandwidth, with 2.4× the HBM capacity of an H100 SXM5 ([AMD](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html)). [Doubleword's write-up](https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/) estimates that it costs roughly half as much at list price. For this 304B-parameter checkpoint, the memory capacity allows a simple single-GPU deployment:

The entire model fits in HBM without PCIe weight streaming or layer offload.
There is room for a 20 GB GPU KV pool and a 96 GiB CPU tier for evicted prefix-cache entries.
One card handles 2–8 typical concurrent streams and bursts of up to 64 streams.

MI300X (CDNA3) implements the AMD/Graphcore `fnuz` variant of E4M3, while MI325X and newer use OCP-standard FP8 ([background](https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/)). A kernel that assumes OCP semantics on MI300X can be wrong by a factor of two in the scale domain. Correctness on this FP8 implementation was the first priority; performance tuning came afterward.

## Prior art, and what this repo adds

[Fergus Finn's MI300X worklog](https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/) and the accompanying [Doubleword repository](https://github.com/doublewordai/vllm-amd-blog-doubleword) identified the FP8 incompatibility, missing AITER fast paths on `gfx942`, HIP-graph hazards in sparse MLA decode, and MoE routing bugs. The [official vLLM recipe](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Flash) covers NVIDIA hardware and newer AMD GPUs (MI325X at 4K context and MI355X), but not a single-MI300X production configuration for the 0731 checkpoint.

This repository adds:

Correctness overlays for the pinned ROCm nightly, including fixes not yet in upstream vLLM.
A validated serving configuration with probabilistic DSpark drafting, block rejection, and static K=7. It uses a 2,048-token scheduler budget and a 1,024-token long-prefill cap to prevent a cold prompt from stalling other streams.
AITER GEMM tuning tables for the recurring `gfx942` shapes the packaged tables were missing, plus a `gfx942` OGS geometry override for the MXFP4 experts.
A hybrid KV strategy: 20 GB of `fp8_ds_mla` GPU cache + 96 GiB native CPU offload, with a load-path fencing fix that upstream [issue #47282](https://github.com/vllm-project/vllm/issues/47282) documents but [PR #47291](https://github.com/vllm-project/vllm/pull/47291) never merged.

## Repository layout

.
├── compose.yaml         # The production stack (vLLM ROCm + Caddy), digest-pinned
├── Caddyfile.example    # Copy to Caddyfile; set hostname, email, and source CIDR
├── vllm-entrypoint.sh   # Removes stale CPU-KV mmaps from /dev/shm before start
├── SHA256SUMS           # SHA-256 pins for every runtime artifact
├── patches/
│   ├── *.py            # Byte-for-byte production overlays (mounted read-only)
│   ├── diffs/*.patch   # Unified diffs vs. the upstream base revision
│   └── README.md       # Provenance and regeneration instructions
└── tuning/
    └── *.csv           # AITER A8W8 blockscale tuning tables for gfx942

## Runtime configuration

The stack uses a digest-pinned official vLLM ROCm nightly with:

`--trust-remote-code` and the DeepSeek V4 tokenizer, reasoning, and tool parsers
`fp8_ds_mla` KV cache (UE8M0 block-scaled FP8, not generic unscaled FP8) with 256-token blocks
`VLLM_ROCM_USE_AITER=1` and `--moe-backend triton`; Triton OGS handles the grouped MXFP4 experts, while AITER handles attention and dense linear layers
DSpark-7 speculative decoding with probabilistic drafting and block rejection
full/breakable CUDA graph capture, giving one graph launch per token during steady decode
Caddy as an IP-allowlisted HTTPS proxy

## Deploying it

### 1. Host prerequisites

One MI300X (`gfx942`, 304 CUs, ~192 GiB HBM), a working AMD kernel driver, recent Docker Compose, ~235 GiB RAM for the CPU KV tier, and ~500 GB disk (the model cache alone is ~156 GB).

### 2. Pull the pinned runtime and model

VLLM_IMAGE='vllm/vllm-openai-rocm@sha256:e68d18b2ba50298661bfc49baf01158fbf036645c2362cccf3e8a7a79fe6c69a'
MODEL='deepseek-ai/DeepSeek-V4-Flash-0731'
REVISION='7872f01b1d1fe23eabc4c98b48bffcef5a386062'

docker pull "$VLLM_IMAGE"
docker run --rm --entrypoint hf \
  -v /root/.cache/huggingface:/root/.cache/huggingface \
  "$VLLM_IMAGE" download "$MODEL" --revision "$REVISION"

### 3. Prepare the files

cp Caddyfile.example Caddyfile   # then set your hostname, email, and remote_ip CIDR
mkdir -p aiter-cache crash-dumps
chmod +x vllm-entrypoint.sh
sha256sum -c SHA256SUMS        # verify the overlays before first start

### 4. Start

docker compose config -q
docker compose up -d
docker compose logs -f inference

A healthy start takes ~5 minutes and must show all of:

Model loading took 156.67 GiB
DSpark draft model loaded: 96 params
GPU KV cache size: 1,927,444 tokens
Maximum concurrency for 262,144 tokens per request: 7.35x
Created mmap file /dev/shm/vllm_offload_...mmap (103.08 GB)
Capturing CUDA graphs (FULL)
Application startup complete

After graph capture, run `rocm-smi --showmeminfo vram`. The warmed high-water mark is ~204.5 GB of 205.8 GB. If only a few hundred MB remain, the server may start but fail on the first request.

### 5. Smoke-test

HOST='your-host.example.com'
curl -fsS "https://$HOST/v1/models"
curl -sS "https://$HOST/v1/completions" \
  -H 'Content-Type: application/json' \
  -d "{\"model\": \"deepseek-ai/DeepSeek-V4-Flash-0731\",
       \"prompt\": \"Calculate 17 * 23. Answer with the number only.\",
       \"temperature\": 0, \"max_tokens\": 32}"

## The patches

Each `patches/*.py` file is a full-file overlay mounted read-only over its counterpart in the container; `compose.yaml` contains the target paths. The corresponding `diffs/*.patch` records the change from its upstream base. The base image remains digest-pinned, so upgrades require changing the image reference and revalidating the stack.

Overlay
Mounted over
Fixes
Needed when

`gpt_oss_triton_kernels_moe.pack128-fused-silu-fast-routing.py`
`vllm/.../fused_moe/experts/gpt_oss_triton_kernels_moe.py`
MXFP4 bitmatrix padding lanes + fused-SiLU grouped experts + fast DeepSeek routing
Required for the MXFP4 Triton path; the mask fix is [not yet upstream](https://github.com/doublewordai/vllm-amd-blog-doubleword/commit/c32932bb9ff6ad30b942e4835dd8b41601e7569e)

`mxfp4.fused-silu.py`
`vllm/.../fused_moe/oracle/mxfp4.py`
Gate/up interleave layout for the fused-SiLU kernel
Required with the fused-SiLU overlay; skip both if you keep the standard SiLU path

`triton-kernels-matmul-ogs-opt-flags.dsv4-mi300x.py`
`vllm/third_party/triton_kernels/matmul_ogs_details/opt_flags.py`
`gfx942` MXFP4 OGS tile geometry (up to 1,536 routed rows)
Performance on `gfx942`; the stock geometry slows sharply above 768 routed rows

`fused_compress_quant_cache.fnuz-shuffle.py`
`vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`
FNUZ FP8 + 16×16 preshuffle in the Lightning Indexer cache writer
Required on MI300X; MI325X/MI355X use OCP FP8 and must keep the stock bytes

`aiter_pa_mqa_logits.i64.py`
`aiter/ops/triton/gluon/pa_mqa_logits.py`
64-bit offsets in the `ChunkK=256` paged-MQA kernels
Required when KV offsets can exceed 4 GiB; skip for small KV pools

`rocm_aiter_mla_sparse.prefill-bh64.py`
`vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`
Deterministic `torch.topk` prefill + `BLOCK_H=64` head-512 sparse prefill
Determinism is required for reproducible tool calls; `BLOCK_H=64` is performance

`rocm_aiter_mla.dspark-causal.py`
`vllm/v1/attention/backends/mla/rocm_aiter_mla.py`
Causal multi-token speculative verification
Required for DSpark on ROCm small-head MLA — now [upstream](https://github.com/vllm-project/vllm/commit/77469c9057bec3212a64877dbbf3b9c48c22d786); the overlay is the upstream file verbatim

`dspark-speculator.independent-draft-gumbel.py` + `spec-decode-utils.independent-draft-gumbel.py`
`vllm/v1/worker/gpu/spec_decode/dspark/speculator.py` + `.../spec_decode/utils.py`
Draft-proposal Gumbel noise salted away from rejection/recovery noise
Required only with `draft_sample_method=probabilistic` (the recipe's greedy path does not need it)

`kv_offload_cpu_gpu_worker.load-war.py`
`vllm/v1/kv_offload/cpu/gpu_worker.py`
Fence CPU→GPU KV restores behind in-flight compute ([#47282](https://github.com/vllm-project/vllm/issues/47282), [PR #47291](https://github.com/vllm-project/vllm/pull/47291))
Required only with `--kv-offloading-backend native`

### Two important correctness fixes

MXFP4 routing. The MoE bitmatrix kernel pads its block columns to a Triton block size, but the padding lanes were masked against the global tensor bound instead of the logical block size. Under load, padded lanes corrupted the routing matrix, causing near-match tool names and forgotten schemas on long prompts. The one-line fix is `mask = (offs_local &lt; BLOCK_SIZE) &amp; (offs_global &lt; nonzero_indx_size)`, taken from [Doubleword commit `c32932bb9`](https://github.com/doublewordai/vllm-amd-blog-doubleword/commit/c32932bb9ff6ad30b942e4835dd8b41601e7569e). The overlay also includes fused-SiLU and fast-routing changes for grouped MXFP4 experts.

FP8 format. DeepSeek V4's Lightning Indexer cache uses FP8. The stock writer emits OCP E4M3 bytes in row-major order, while AITER on MI300X consumes AMD FNUZ E4M3 bytes in a preshuffled 16×16 tile layout. In the worst case, interpreting one format as the other produces a factor-of-two scale error. The overlay selects `float8e4b8` with `FP8_MAX=224.0` and shuffled write offsets on ROCm, while leaving the OCP path unchanged elsewhere.

### Speculative decoding

This stack uses probabilistic drafting with block rejection. The two Gumbel overlays keep draft-proposal noise independent of rejection and recovery noise.

## Performance

Key optimizations in the production configuration:

Change
Effect

Tune 21 recurring A8W8 GEMM shapes for 304-CU `gfx942`
+42–62% single/double-stream decode; +10–35% at 8–64 streams

Fused SiLU, fast DeepSeek routing, batch-sensitive expert tiles
Native C1 decode 34.5 → 56.6 tok/s (+64%); routing kernel 42.6 → 11.9 µs/layer

`BLOCK_H=64` sparse-prefill tile
Prefill reaches 7.9–8.5K tok/s; sparse-attention trace 317 → 142 ms per request

Static K=7, probabilistic + block rejection, causal verify
119.5 tok/s single-stream with correct output

2,048-token budget + 1,024-token long-prefill cap
Late short-request TTFT behind a 52K prefill: 8.2 s → 0.5 s

20 GB GPU KV + 96 GiB CPU tier
1.93M-token length-equivalent capacity; seven 256K requests admitted

### Final concurrency sweep

Distinct ~400-word prompts, streaming, `temperature=1.0, top_p=0.95`; C1–C8 at 512 output tokens, C64 at 256:

Streams
Aggregate tok/s
Median per-stream decode
TTFT p50

1
126.2
168.6 tok/s
1.026 s

2
145.4
152.7
0.939 s

4
316.8
108.6
0.369 s

8
542.3
90.3
1.027 s

64
830.2
16.4
2.190 s

DSpark acceptance is prompt-dependent; treat these as gates for this exact image, not universal model benchmarks.

### Prefill

With the tuned kernels, uncached prefill reaches 7.9–8.5K tok/s, depending on scheduler budget: 7.90–7.99K at C1 with an 8,192-token budget and 8.46–8.51K at C4. The production profile uses a 2,048-token budget for latency isolation, giving 6,988–7,019 tok/s on fresh prompts. With the 1,024-token long-prefill cap, an 8.9K-token prompt reaches 5.20–5.29K tok/s at C1. In exchange, TTFT for a short request queued behind a 52K cold prefill drops from 8.2 s to 0.5 s. Warm recall of 380K cached tokens takes 0.64–2.65 s after a 120–125 s cold prefill.

## Production notes

HBM headroom is limited. The warmed high-water mark is 204.5 of 205.8 GB. A 30 GB KV pool loads but fails during graph capture with `HSA_STATUS_ERROR_OUT_OF_RESOURCES`. Do not raise `--kv-cache-memory-bytes`; monitor HBM usage for growth.
The CPU KV tier stores cache entries, not weights. `--kv-offloading-size 96 --kv-offloading-backend native` maps ~103 GB in `/dev/shm` for evicted prefix-cache entries. The entrypoint removes stale mappings after crashes.
The 1,664-token scheduler warning is expected. DSpark-7 reserves draft slots from the 2,048-token budget. Raising the budget reserves more in-flight sliding-window state and reduces usable KV capacity.
Warm the kernels after restart. The first prefill initializes kernels and takes 5.3 s for 8.9K tokens; subsequent runs take 1.7 s. Run one uncached prefill before admitting traffic.
Test correctness as well as throughput. The validation suite includes two-turn tool-calling fixtures, a BFCL subset (74–76/90 exact calls), OpenCode tool-schema checks, and 380K-token needle recall on both native and DSpark paths. Cold and cached prefills can take different floating-point paths, so test both.

## License and provenance

The stack, documentation, and vLLM-derived overlays are Apache-2.0 (see `LICENSE`); the AITER-derived overlay keeps its MIT header. Upstream base revisions for every diff are recorded in [`patches/README.md`](/ryanzhou/deepseek-v4-flash-mi300x/blob/main/patches/README.md). The model itself is [MIT-licensed](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731).

## References

All links verified 2026-08-04.

[DeepSeek-V4-Flash-0731 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) — official release; 304B parameters; fused DSpark module; recommended `temperature=1.0, top_p=0.95`; MIT license
[Official vLLM DeepSeek V4 Flash recipe](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Flash) — reference launch configuration, DSpark (`num_speculative_tokens=7`), FP8 KV, block size 256, `deepseek_v4` parsers; AMD guidance for MI325X
