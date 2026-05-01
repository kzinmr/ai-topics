## [2026-05-01] X Bookmarks Ingest — OpenAI WebSockets, LangChain Harness Engineering, Meta Autodata

- Saved raw articles:
  - `raw/articles/2026-04-22_openai-websockets-agentic-workflows.md` — OpenAI's transition to WebSocket transport for the Responses API, achieving ~40% faster agentic cycle latency (up to 1,000+ TPS). Techniques: `previous_response_id`, incremental safety processing, token caching.
  - `raw/articles/2026-02-17_langchain-improving-deep-agents-harness-engineering.md` — Vivek Trivedy (LangChain) case study: +13.7pts on Terminal Bench 2.0 from harness-only changes (Build-Verify Loop, Context Engineering, Loop Detection, Reasoning Sandwich).
  - `raw/articles/2026-04-08_langchain-better-harness-hill-climbing-evals.md` — Vivek Trivedy follow-up: evals as training data for autonomous harness hill-climbing with holdout sets.
  - `raw/articles/2026-04-30_meta-autodata-agentic-data-scientist.md` — Meta AI's Autodata: agentic data scientists using Weak-vs-Strong solver paradigm. 34% discrimination gap vs 1.9% baseline. Meta-optimization: 12.8%→42.4% pass rate.

- Updated [[concepts/harness-engineering]] — Added "LangChain Harness Engineering Case Studies" section with two sub-sections: Improving Deep Agents (+13.7pts, 4 techniques) and Better Harness (eval-driven hill-climbing recipe). Updated sources, tags, aliases, and related links.

- Created [[concepts/autodata-agentic-data-creation]] — New concept page for Meta AI's Autodata framework. Covers the 4-subagent Weak-vs-Strong paradigm, experimental results (34% gap), meta-optimization, and significance for inference-time compute scaling.

- Updated [[index]] — Added autodata-agentic-data-creation entry. Updated harness-engineering description to reference LangChain case studies and Vivek Trivedy. Total pages: 749→750.

- 5 X Articles behind auth wall (no external mirrors found): "How to Beat GRPO Without Touching Model Weights", "On SFT, RL, and on-policy distillation", "大语言模型训练与服务背后的数学原理", "If AI is so great, why isn't it working?", "The 5 principles for AI that ships to production". Saved as metadata-only in bookmark records.

## [2026-05-01] GLiClass | New concept page (encoder-only zero-shot classification)

- Created [[concepts/gliclass]] — Comprehensive concept page for Knowledgator's GLiClass model family. Covers:
  - **Architecture**: single-forward-pass classification, GLiNER-inspired design, 3 architecture types (uni/bi/bi-fused/encoder-decoder)
  - **Three sub-families**: GLiClass-V3 (general, 6 variants, DeBERTa/ModernBERT/Ettin backbones), GLiClass-Instruct (instruction-following, 3 variants), GLiClass-Multilang (20 languages, 3 variants, CrossAttn Scorer)
  - **V3 features**: hierarchical labels, few-shot, label descriptions, task prompts, long document chunking
  - **Training**: LoRA fine-tuning, multi-label PPO, logic-focused datasets
  - **RAC** (Retrieval-Augmented Classification): inference-time example retrieval, up to +141% F1 boost
  - **Benchmarks**: V3 large-v3.0 avg F1 0.7001, Instruct large-v1.0 avg F1 0.7199, Multilang Ultra avg F1 0.7212 (EN)
  - **Use cases**: RAG reranking, sentiment/topic, intent, NLI, hallucination detection, LLM safety
- Created [[entities/knowledgator]] — Organization entity page. Lists GLiNER/GLiClass/GLiREL product family, HF collections.
- Sources: arXiv:2508.07662, HuggingFace collections (3), GitHub repo, Medium blog, 3 X posts by @gm8xx8
- Updated: index.md, log.md

## [2026-05-01] AI Infrastructure Engineering — 親ページとスケルトン群の作成

- Created [[concepts/ai-infrastructure-engineering/_index]] — 親ページ。GPU/VRAM基礎、分散学習、モデルサーブ、オブザーバビリティ、コスト最適化の統合マップ。学習ロードマップ、既存ページ一覧表、Key Entitiesを含む。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPUメモリ階層（HBM→SRAM）、VRAM計算式、Roofline Model、バッチング経済学、量子化効果、GPU選定ガイド、マルチGPUトポロジ。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/distributed-training]] — DDP→FSDP→DeepSpeed ZeRO(1/2/3)、3D並列化（TP/PP/EP/Expert Parallel）、戦略選択ガイド（モデルサイズ×GPU数）、CPUオフロード比較。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — デプロイ構成、スケーリングシグナル（queue/GPU/KV cache）、4つのスケーリングパターン、ロードバランシング戦略（Round Robin→LRU→Semantic）、コスト最適化パターン。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/llm-observability]] — 推論メトリクス（TTFT/TPOT/ITL）、GPUリソース指標、品質シグナル、Observability Stack（Prometheus/OTel/Arize）、コスト帰属、劣化検知パターン、vLLM OTel統合。⬜ L1
- Created [[concepts/tensorrt-llm]] — NVIDIA推論最適化エンジン。FP8/FP4 Transformer Engine、vLLMとの比較表、ベンチマーク概算値、導入判断基準、Triton統合パターン。⬜ L1
- Enriched [[concepts/model-quantization]] — stub→L1。精密形式一覧（FP32→BitNet）、GPTQ/AWQ/GGUF/SmoothQuant/FP8比較、ハードウェアサポート表、トレードオフ実測値、KV Cache量子化。
- Enriched [[concepts/pytorch-fsdp-distributed-training]] — stub→L1。Sharding戦略詳細（NO_SHARD/SHARD_GRAD_OP/FULL_SHARD）、メモリ節約計算例、CPU Offload、DeepSpeed比較表、設定パラメータサンプルコード。
- Updated [[concepts/inference/_index]] — TensorRT-LLMをエンジン比較表に追加
- Updated [[index]] — Concepts 393→399, added 7 new entries + updated 2 TODO entries
- Sources: (new pages are skeleton/L1, will need article ingestion for enrichment)
