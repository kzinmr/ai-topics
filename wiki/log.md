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
