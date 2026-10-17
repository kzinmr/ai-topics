# DeepSeek-V4.1-Flash-1017: Wish-Driven Programming Made Real

Source: https://api-docs.deepseek.com/news/news261017/
Fetched: 2026-10-17 (published 2026-10-17 09:05 UTC)
Companion primary sources:
- Official X announcement thread (4 posts, 2026-10-17 08:35 UTC): https://x.com/deepseek_ai/status/2111375640717033777
- Hugging Face model card: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
- Search & Fetch API guide: https://api-docs.deepseek.com/guides/search

---

## 🚀 DeepSeek-V4.1-Flash-1017 is here!

Stronger benchmark performance, faster task completion, and shorter outputs than the previous version—a Pareto improvement in performance and cost. Now live on our website, app, and API.

🛠️ Optimized for DeepSeek Harness, Tencent CodeBuddy, WorkBuddy, and more. Upgrade to DeepSeek Harness v0.2.1-rc.1 or later for the best experience with the new model.

(Benchmark table image and performance/cost chart image in original.)

DeepSWE v1.1 Pass@1 vs. cost per task for DeepSeek V4.1 Flash 1017, tested with the mini-swe-v2 harness.

## 🎮 Build complete projects from scratch

DeepSeek-V4.1-Flash-1017 uses reinforcement learning with self-feedback to improve end-to-end project development—from game creation to 3D modeling.

Demo examples (GIFs in original):
1. 3D modeling of the Forbidden City
2. A web-based racing game
3. A Portal 2 recreation built with the Godot engine
4. Valley of Ages — a 3D scene tracing the evolution from prehistoric times to the modern era

## 🔍 Search & Fetch APIs are now open to everyone!

Powered by our in-house search engine, serving hundreds of millions of requests daily worldwide.

💰 Each endpoint: $0.75 per 1,000 calls.
📖 Docs: API Guides - Search & Fetch (https://api-docs.deepseek.com/guides/search)
📌 Search & Fetch calls via server-side tools in DeepSeek Harness, Claude Code, and Codex are currently free for DeepSeek API users. Billing starts **Oct 31, 2026, at 16:00 UTC**.

## 🔓 Open-source release

Get DeepSeek-V4.1-Flash-1017:
🤗 Hugging Face: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
🔗 ModelScope: https://modelscope.cn/models/deepseek-ai/DeepSeek-V4.1-Flash-1017

---

## Appendix: X announcement thread (verbatim, via X API v2 note_tweet fields)

1/4 (2111375640717033777): "🚀 DeepSeek-V4.1-Flash-1017 is here! Stronger benchmark performance, faster task completion, and shorter outputs than the previous version—a Pareto improvement in performance and cost. Now live on our website, app, and API. 🛠️ Optimized for @DeepSeekHarness, Tencent CodeBuddy, WorkBuddy, and more. Upgrade to DeepSeek Harness v0.2.1-rc.1 or later for the best experience with the new model."

2/4 (2111375646223933650): "🎮 Build complete projects from scratch — DeepSeek-V4.1-Flash-1017 uses reinforcement learning with self-feedback to improve end-to-end project development—from game creation to 3D modeling."

3/4 (2111375650414309859): "🔍 Search & Fetch APIs are now open to everyone! Powered by our in-house search engine, serving hundreds of millions of requests daily worldwide. 💰 Each endpoint: $0.75 per 1,000 calls. 📌 Search & Fetch calls via server-side tools in DeepSeek Harness, Claude Code, and Codex are currently free for DeepSeek API users. Billing starts Oct 31, 2026, at 16:00 UTC."

4/4 (2111375653069259247): "🔓 Open-source release — Get DeepSeek-V4.1-Flash-1017: Hugging Face / ModelScope links. (MIT License)"

## Appendix: HF model card — benchmark table (vendor-self-reported)

| Benchmark | DS-V4.1-Flash-1017 | DS-V4.1-Flash | K3 | GLM-5.3 | GPT-5.6 Sol | Opus 5 |
| --- | --- | --- | --- | --- | --- | --- |
| HLE w/o tools | 42.6 (44.0†) | 36.8 (39.1†) | 43.5 | 42.0† | 44.5 | 56.3 |
| Terminal-Bench 4.0 | 42.3 | 31.2 | 12.6 | 37.9 | 39.9 | 51.8 |
| DeepSWE v1.1 | 77.0 | 74.2 | 67.5 | 66.9 | 73.0 | 74.0 |
| ProgramBench | 29.1 | 20.3 | 17.5 | 19.0 | 23.0 | 37.0 |
| NL2Repo-Bench | 68.2 | 65.4 | 58.0 | 58.0 | 56.8 | 75.3 |
| Automation-Bench v1.0.6 | 60.5 | 54.8 | 46.7 | 48.8 | 45.8 | 50.3 |
| Agents' Last Exam | 35.4 | 31.8 | 27.6 | 28.5 | 26.7 | 28.6 |
| Apex Bench v1.1 | 72.1 | 64.6 | 47.8 | 56.6 | 54.3 | 65.8 |
| Chartography (w/tools) | 83.0 | 78.9 | 68.1 | — | 79.9 | 84.0 |
| BabyVision (w/tools) | 92.5 | 89.6 | 85.7 | — | 88.9 | 94.1 |
| ZeroBench-main (w/tools) | 51.0 | 49.0 | 41.0 | — | 53.0 | 52.0 |

† text-only subset of HLE. Claude Code harness for Terminal-Bench 4.0; Mini-SWE-V2 harness for DeepSWE v1.1.

Model card also states: "minor update to DeepSeek-V4.1-Flash, delivering substantial improvements across reasoning, coding, agentic tasks, and visual benchmarks... reduces task execution time and output length... advancing the performance–cost Pareto frontier across multiple agent harnesses."

Prompt encoding: no Jinja chat template; self-contained `encoding.py` reference implementation + `deepseek-recipe` Rust libs with Python bindings (converts Messages / Chat Completions / Responses API requests into DeepSeek V4/V4.1 prompt format).

Recommended sampling: temperature 1.0, top_p 1.0, context_window 1M tokens, max_tokens ≥ 256K. License: MIT.

## Appendix: Search & Fetch API details (from api-docs.deepseek.com/guides/search)

- Search: `POST https://api.deepseek.com/v1/tools/search`; Fetch: `POST https://api.deepseek.com/v1/tools/fetch`. Same bearer auth as DeepSeek API.
- Search request: `query` (1–128 chars), `count` (1–50, default 10), `ori_question`, `localization` (IP), `need_content`.
- Query operators: `site:`, `-site:`, `-term`, `-"phrase"`, `"exact phrase"`, `lang:zh,en`, `after:`, `before:`.
- Search response fields: `rerank_score` (0–3; ≥1.5 = high quality), `title`, `url`, `snippet` (~100–200 chars, UI), `summary` (~600–800 chars, model-readable), `content`, `site_name`, `date` (RFC 3339 UTC), `authority` (tier 0–4, ≥3 highly authoritative).
- Fetch API: retrieves a single page and returns `{title, content}` with content as Markdown. Subject to target site availability/policies.
