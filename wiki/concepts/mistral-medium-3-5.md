# Mistral Medium 3.5

**Mistral Medium 3.5** is a 128B dense parameter flagship model from Mistral AI, released in public preview on May 22, 2026. It merges instruction-following, reasoning, and coding capabilities into a single set of open weights under a modified MIT license. The model features a 256k context window and is designed for long-horizon tasks that call multiple tools reliably and produce structured output that downstream code can consume.

## Key Facts

| Field | Detail |
|-------|--------|
| **Model** | Mistral Medium 3.5 |
| **Developer** | [[entities/mistral-ai]] |
| **Release Date** | May 22, 2026 |
| **Status** | Public preview |
| **Parameters** | 128B (dense, not MoE) |
| **Context Window** | 256k tokens |
| **License** | Modified MIT (open weights) |
| **SWE-Bench Verified** | 77.6% |
| **τ³-Telecom** | 91.4 |

## Capabilities

- **Dense architecture**: Unlike the prevailing trend toward Mixture-of-Experts (MoE) models, Medium 3.5 is a dense 128B model — all parameters activate on every forward pass
- **Configurable reasoning effort**: The model supports adjustable reasoning depth per request, allowing the same model to handle both quick chat responses and complex agentic runs
- **Multi-tool orchestration**: Built for long-horizon tasks requiring reliable tool calling and structured output generation
- **Custom vision encoder**: Trained from scratch to handle variable image sizes and aspect ratios
- **Self-hostable**: Runs on as few as four GPUs, making it accessible for enterprise on-premise deployment

## Benchmarks

- **SWE-Bench Verified**: 77.6% — outperforms Devstral 2 and Qwen3.5 397B A17B
- **τ³-Telecom**: 91.4 — strong agentic capabilities score

## Use in Mistral Products

- Default model in [[concepts/le-chat]]
- Powers remote coding agents in [[concepts/mistral-vibe-remote-agents]] (replaces Devstral 2 in Vibe CLI)
- Drives the new Work mode in Le Chat (Preview) for complex multi-step tasks

## Significance

Medium 3.5 represents Mistral's strategic pivot toward a unified flagship model that can handle the full spectrum of tasks — from quick responses to extended agentic workflows — rather than maintaining separate specialized models for different use cases. The dense 128B size is notable because it's large enough to be highly capable yet small enough to self-host on commodity hardware, aligning with Mistral's "sovereign AI" positioning.

## Related

- [[entities/mistral-ai]] — Developer
- [[concepts/mistral-vibe-remote-agents]] — Remote coding agent product powered by this model
- [[concepts/dense-vs-moe]] — Architecture comparison (dense vs. Mixture-of-Experts)
