---
title: MiniMax
created: 2026-05-08
updated: 2026-08-05
type: entity
tags: [entity, company, model, china, open-source, coding-agents, video-generation]
sources: [raw/articles/2026-05-04_nathanbenaich-state-of-ai-may-2026.md, raw/newsletters/2026-08-01-ainews-not-much-happened-today.md, raw/articles/simonwillison.net--2026-aug-4-minimax-h3-mlx--38cf1186.md]
---

# MiniMax

MiniMax is a Chinese AI company and one of the country's leading AI labs, known for its M-series large language models. In April 2026, MiniMax released M2.7, an open-weight coding model that scored 56-59 on SWE-Bench Pro, placing it alongside Kimi K2.6 and Z.ai GLM-5.1 in China's agentic coding sprint.

## Key Facts

- **Founded**: 2021
- **Headquarters**: Shanghai, China
- **Notable models**: MiniMax M2.7 (coding, April 2026), MiniMax-01 series
- **Pricing**: Below Western equivalents for comparable capability
- **License**: Open weights (M2.7)

## M2.7 in Context

M2.7 was released within a 12-day window alongside Kimi K2.6 (Moonshot AI) and Z.ai GLM-5.1 (Z.ai/Zhipu), with all three scoring in the 56-59 range on SWE-Bench Pro. This convergence demonstrates rapid knowledge diffusion among Chinese AI labs and challenges the "China is six to nine months behind" narrative for agentic coding capabilities.

## Competitive Position

MiniMax competes in China's "AI Tigers" alongside:
- Moonshot AI (Kimi)
- Z.ai / Zhipu AI (GLM series)
- DeepSeek
- Baidu (ERNIE)

The company focuses on multimodal AI and has significant backing from Chinese and international investors.

## H3 Video Model (July 2026)

In July 2026, MiniMax launched **H3**, its first major video generation model, with broad distribution momentum. It went live on [[entities/vercel|Vercel AI Gateway]] with "one `generateVideo[]` away" positioning, and MiniMax promised open weights soon.

H3 propagated rapidly across partners including **fal, Pollo, PixVerse, Leonardo, and OpenArt**. Technically, H3 appears to integrate **low-to-high generation / baked-in super-resolution** rather than stapling on a separate super-resolution (SR) stage.

This marks MiniMax's entry into AI video generation, extending beyond its M-series LLMs (e.g., M2.7) into the [[concepts/ai-video-generation-2026|2026 video generation landscape]].

### Omni-Modal Spec and MLX Port (August 2026)

On August 2, 2026, MiniMax released **MiniMax-H3**, which it describes as "a general-purpose, omni-modal generative system": it accepts text, images, audio and video inputs and generates up to 15-second video clips **with audio included** — a notable step beyond silent video outputs.

The community package **PipeNetwork/minimax-h3-mlx** ports H3 to **MLX** for running on [[entities/apple|Apple Silicon]]. [[entities/simon-willison|Simon Willison]] ran it on his M5 Max MacBook Pro, downloading ~115 GB of model files; a single video generation took just under 45 minutes. The run pattern is:

```bash
# First download the models
uvx --from huggingface_hub hf download MiniMaxAI/MiniMax-H3

# Now run the prompt
uv run --with mlx-vlm python scripts/generate.py "PROMPT" -o out.mp4
```

Without prompt guidance for the audio track, Willison found the generated audio came out as "weird speech-like garbage"; H3's prompting guide covers how to steer audio output.

## Related Pages

- [[concepts/china-agentic-coding-sprint]]
- [[entities/kimi]]
- [[entities/china-ai-industry]]
- [[concepts/ai-benchmarks/swe-bench]]
- [[entities/coding-agents]]
- [[concepts/ai-video-generation-2026]]
- [[entities/vercel]]
