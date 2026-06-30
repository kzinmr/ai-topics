# OpenRouter Fusion: Surpassing Frontier Performance with Multi-Model Synthesis

**Source**: https://openrouter.ai/blog/announcements/fusion-beats-frontier/
**Date**: 2026-06-12
**Author**: OpenRouter

## Summary

OpenRouter introduces **Fusion**, a tool that synthesizes results from multiple models in parallel, achieving beyond-frontier performance. A panel of models processes the same prompt independently, then a judge model reads all responses and produces structured analysis (consensus, contradictions, unique insights, blind spots) to write the final fused answer.

## Key Results (DRACO Benchmark, 100 deep research tasks)

| Configuration | Score |
|---|---|
| Fusion: Fable 5 + GPT-5.5 (synth by Opus 4.8) | **69.0%** |
| Fusion: Opus 4.8 + GPT-5.5 + Gemini 3.1 Pro (synth by Opus 4.8) | **68.3%** |
| Fusion: Opus 4.8 + GPT-5.5 (synth by Opus 4.8) | **67.6%** |
| Fusion: Opus 4.8 + Opus 4.8 (synth by Opus 4.8) | **65.5%** |
| Solo: Fable 5 | 65.3% |
| Fusion: Gemini 3 Flash + Kimi K2.6 + DeepSeek V4 Pro (synth by Opus 4.8) | **64.7%** |
| Solo: DeepSeek V4 Pro | 60.3% |
| Solo: GPT-5.5 | 60.0% |
| Solo: Claude Opus 4.8 | 58.8% |

### Key Findings
1. Panels consistently outperform individual models
2. Beyond-frontier performance achievable with frontier panels
3. Budget panels (Gemini 3 Flash + Kimi K2.6 + DeepSeek V4 Pro) beat GPT-5.5 and Opus 4.8, come within 1% of Fable 5 at 50% cost
4. Self-fusion (Opus 4.8 × 2) yields 6.7-point jump over solo — synthesis itself contributes significantly

## API Usage

```json
{
  "model": "openrouter/fusion",
  "messages": [{"role": "user", "content": "..."}],
  "plugins": [{
    "id": "fusion",
    "model": "google/gemini-3-flash-preview",
    "analysis_models": [
      "google/gemini-3-flash-preview",
      "moonshotai/kimi-k2.6",
      "deepseek/deepseek-v4-pro"
    ]
  }]
}
```

Four usage modes: Chatroom, Model slug (`openrouter/fusion`), Server tool, Plugin.

## Benchmark Details

- **DRACO benchmark** (Perplexity AI): 100 deep research tasks across 10 domains
- Graded on Factual Accuracy (~20 criteria), Breadth & Depth (~9), Presentation Quality (~6), Citation Quality (~5)
- Models had web search + web fetch + bash tools
- Anti-cheating: excluded DRACO rubric locations from web search

## Limitations

- Not a drop-in replacement for Fable or for coding models
- DRACO doesn't include long-horizon tasks (where Fable shines)
- 2-3x slower than standard calls when Fusion is invoked
- Judge model choice affects absolute scores (10-25 point shifts), though relative rankings stable
