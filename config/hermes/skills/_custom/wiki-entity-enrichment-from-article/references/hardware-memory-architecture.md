# Hardware Memory Architecture: Key Distinctions for Wiki Content

> When writing or enriching wiki pages about memory tiering, heterogeneous memory, or inference hardware, these distinctions prevent technical imprecision.

## Dense FFN vs MoE FFN — The Critical Distinction

When discussing memory tiering ("FFN → capacity, attention → bandwidth"):

| Architecture | FFN Characteristic | Heterogeneous Memory Fit |
|---|---|---|
| **Dense (non-MoE)** | Every token processes ALL FFN weights. Capacity and bandwidth are **inseparable**. | Limited benefit — can't split FFN across tiers without losing bandwidth |
| **MoE** | All expert weights need capacity, but only K-of-N active experts need bandwidth per token. | **Natural fit** — non-active experts → slow/large memory (CPU LPDDR5X), active experts → fast memory (GPU HBM) |

**Rule**: "FFN has capacity requirements" is ONLY accurate for MoE. For dense models, FFN has both capacity AND bandwidth requirements that cannot be separated.

## Memory Tier Progression: DGX Station → Vera Rubin

| Tier | DGX Station (Desktop) | Vera Rubin (Rack) |
|---|---|---|
| Ultra-fast | — | Groq 3 SRAM (40 PB/s, nanosecond) — decode |
| Fast | GPU HBM3e (252GB, 7.1 TB/s) | GPU HBM4 (288GB, 22 TB/s) — prefill, attention |
| Large | CPU LPDDR5X (496GB, 396 GB/s) | CPU LPDDR5X (1.5TB, 1.2 TB/s) — FFN, expert offload |
| Shared | — | BlueField-4 ICMS flash — KV-cache persistence |

Key links:
- DGX Station: 900 GB/s CPU↔GPU coherent link
- Vera Rubin: NVLink-C2C 1.8 TB/s coherent CPU↔GPU

## Common Imprecisions to Avoid

1. **"FFN is bandwidth-bound"** — Only at low batch sizes (local inference). At high batch sizes (datacenter), FFN becomes compute-bound.
2. **"HBM is always better"** — HBM is better for bandwidth-sensitive workloads. For capacity-sensitive workloads (MoE expert storage), LPDDR5X wins on cost/bit.
3. **"Unified memory = heterogeneous memory"** — Apple's unified memory is homogeneous (single pool, single technology). DGX Station/Vera Rubin use heterogeneous memory (different technologies, different tiers, different characteristics).

## Wiki Page References
- `entities/alex-cheema.md` — DGX Station disaggregated architecture analysis
- `concepts/nvidia-vera-rubin.md` — 4-layer memory hierarchy, Groq 3 LPX integration
- `concepts/heterogeneous-intelligence.md` — Callosum's Principle of Maximum Heterogeneity
- `concepts/mac-studio-local-ai.md` — Unified memory as alternative approach
- `entities/callosum.md` — Multi-model, multi-chip routing benchmarks
