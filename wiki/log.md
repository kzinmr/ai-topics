## [2026-05-07] Claude Blog「Interactive Connectors and MCP Apps」記事取り込み

**Action**: kzinmrからのリクエストにより、`https://claude.com/blog/interactive-tools-in-claude` の取り込み状態を確認。未取り込みだったため、raw article保存＋既存MCP概念ページにMCP Appsセクションを追加。

**New raw articles saved**:
- `raw/articles/2026-01-26_anthropic-interactive-tools-claude.md` — Anthropic公式ブログ。MCP Apps（インタラクティブUI拡張）の発表。10のローンチパートナー（Amplitude, Asana, Box, Canva, Clay, Figma, Hex, monday.com, Slack, Salesforce）に対応。

**Pages enriched**:
- `concepts/mcp.md` — 「MCP Apps (Interactive UI Extension)」セクションを新設。キーコンセプト、ローンチパートナー一覧表、エコシステム採用状況、競合標準（MCP-UI, OpenAI Apps SDK, Google A2UI）との比較を追加。tags・sources・related conceptsを更新。

## [2026-05-07] Anthropic「Demystifying Evals for AI Agents」記事取り込み

**Action**: kzinmrからのリクエストにより、Anthropic Engineering Blogの「Demystifying Evals for AI Agents」記事の取り込み状態を確認し、未保存のraw articleを保存、既存ページを強化。

**New raw articles saved**:
  - `raw/articles/2026-01-09_anthropic_demystifying-evals-ai-agents.md`

**Pages enriched**:
  - `concepts/harness-engineering/system-architecture/evals-for-ai-agents.md` — Eval Saturation、Creative Failures、Swiss Cheese Model（ホリスティック評価フレームワーク）の3セクションを追加。updated日とsourcesを更新。

## [2026-05-07] 8大AI Agentハーネス一覧比較ポータル構築 — 4エンティティ新規追加 + 1エンリッチ + 1比較ページ

**Action**: kzinmrからの指示により、8つのAI Agentハーネスのwikiエンティティ状態を確認し、不足分をエンリッチメント込みで追加。一覧比較ポータルを整備。

**Pages created (4 entity pages + 1 concept page)**:
- `entities/pi.md` — Pi（Mario Zechner製ミニマルAIコーディングハーネス）。~1K token system prompt、4ツール、45.5K GitHub Stars、MIT。OpenClawの基盤。ローカルモデル最適。L3。
- `entities/codex.md` — OpenAI Codex CLI。Apache-2.0、Rust製、79.3K Stars。GPT-5.5ネイティブ＋カスタムプロバイダ＋ローカルモデル。CLI/Desktop/IDE/Web。ChatGPT Plus/Pro含む。L3。
- `entities/copilot-cli.md` — GitHub Copilot CLI。6ビルトインサブエージェント、`/fleet`並列、MCP拡張、BYOK/ローカルモデル対応。L2。
- `entities/droid.md` — Factory Droid。CLI/IDE/Slack/Linear/CI/CD全方位。Specification Mode + 3段階Auto-Run。SOC-2。専門サブエージェント。L2。
- `concepts/agent-harness-comparison.md` — 8ハーネス（Claude Code/OpenCode/Pi/Codex/Copilot CLI/Droid/OpenClaw/Hermes Agent）の包括的比較ポータル。機能表、モデル互換性マトリクス、価格比較、ユースケース推奨、Harness Effect分析。

**Pages enriched**:
- `entities/opencode.md` — 全面書き換え（155K Stars、MIT、75+プロバイダ、マルチサーフェス、Plan/Build/Generalエージェント、LSP統合、GitHub統合）。Rampの採用理由も維持。

**Pages updated (redirect)**:
- `entities/pi-coding-agent.md` → `entities/pi`へのリダイレクトに変更（重複解消）

**Index/log**: index.mdに5エントリ追加、1リダイレクト更新、1エントリ削除（pi-coding-agent→pi統合）。ページ数5178→5183、Full entries 4632→4637。

## [2026-05-07] Kilo（OpenCode fork）をハーネス比較に追加

**Action**: kzinmrからの指示により、Kilo（コードエージェントプラットフォーム）を既存の9ハーネス比較に追加。過去セッションの存在を確認。

**Previous analysis found**: `comparisons/coding-agent-harnesses.md`（2026-05-01作成）が存在。過去4セッション（5/1-5/2）でcoding agent harness比較を行っていたことを確認。

**Pages created**:
- `entities/kilo.md` — Kilo Code: OpenCode fork、Apache-2.0、VS Code+JetBrains+CLI、500+モデル/Kilo Gateway、KiloClaw（hosted OpenClaw）、Teams/SSO/Analytics、インライン補完。L2。

**Pages updated**:
- `concepts/agent-harness-comparison.md` — 「8 Major Harnesses」→「9 Major Harnesses」に更新。全比較表（概要/アーキテクチャ/モデル相性/価格/ユースケース/コミュニティ）にKilo列追加。関係図セクション追加。
- `comparisons/coding-agent-harnesses.md` — 決定フレームワークにKilo推奨追加、Related更新。pi-coding-agent→pi参照修正。

**Index/log**: entities/kiloをKセクションに追加。ページ数5183→5184、Full entries 4637→4638。

## [2026-05-07] comparisons/coding-agent-harnesses.md を concepts/agent-harness-comparison.md に統合

**Action**: kzinmrからの指示により、2ページのハーネス比較を統合。

**Merged**:
- `concepts/agent-harness-comparison.md` — 統合後の単一正規ページ（19.8KB、12セクション）。旧ページの以下を移植：Codex CLI Deep Dive（Section 5）、モデル中心の互換性ビュー（Section 3）、詳細アーキテクチャ比較（Section 2）、Anthropic Wall分析（Section 7）、決定フレームワーク（Section 8）、主観的まとめ（Section 9）。
- `comparisons/coding-agent-harnesses.md` — リダイレクトページに変更（→ concepts/agent-harness-comparison）。全内容は統合先に保持。
- `wiki/index.md` — `comparisons/coding-agent-harnesses` エントリ更新（リダイレクト反映）
- `wiki/log.md` — 本エントリ追加

**Action**: concepts/hermes-vs-openclaw.md を削除（comparisons/hermes-vs-openclaw-architecture.md と concepts/openclaw/architecture-comparison.md が2026-04-18に既存）
**Merged**: 新規の建築的深掘り分析を comparisons/hermes-vs-openclaw-architecture.md に追加（Architecture Deep-Diveセクション）
**Kept**: concepts/hermes-agent-architecture.md と concepts/openclaw-architecture.md（単体アーキテクチャ詳細は新規価値あり）
**Updated**: wikilink修正、concepts/openclaw/_index.md への相互リンク追加

## [2026-05-07] Hermes Agent vs OpenClaw アーキテクチャ比較ページ作成

**Source**: User request (Discord) — raw/articles/2026-05-07_chatgpt-hermes-vs-openclaw-comparison.md のwiki取り込み

**Raw article referenced**:
- `raw/articles/2026-05-07_chatgpt-hermes-vs-openclaw-comparison.md` — Hermes Agentアーキテクチャ詳細分析（ChatGPT deep dive）
- `raw/articles/2026-05-07_chatgpt-openclaw-architecture-deep-dive.md` — OpenClawアーキテクチャ詳細分析（ChatGPT deep dive）

**Pages created**:
- `concepts/hermes-vs-openclaw.md` — 包括的比較ページ（205行）。9セクション：概要（能力蓄積 vs スコープ制御）、コア設計哲学（Rails vs Linux/Kubernetes）、アーキテクチャ比較表（17次元）、スキルシステム詳細比較（自己生成・増殖 vs 索引注入・許可リスト + トレードオフ表）、スキル爆発問題（4つの解決策）、プロンプトアーキテクチャ（stable prefix vs platform-owned）、キーインサイト（Rails vs Linux）、相互学習（各5項目）、総括比較表（10軸レーティング）。7個のwikilink。

**Index/log**: index.mdのConceptsセクションにhermes-vs-openclaw追加。総ページ数: 5178→5179、Full entries: 4632→4633、Concepts: 443→444。

## [2026-05-07] Hermes Agentアーキテクチャ概念ページ作成 — ChatGPT deep dive記事から

**Source**: User request (Discord) — raw/articles/2026-05-07_chatgpt-hermes-agent-architecture-deep-dive.md のwiki取り込み

**Raw article referenced**:
- `raw/articles/2026-05-07_chatgpt-hermes-agent-architecture-deep-dive.md` — Hermes Agentアーキテクチャの詳細分析。AIAgent中心設計、3つのAPI実行モード、キャッシュ対応プロンプトアセンブリ、SQLite+FTS5永続状態、自己登録型ツールレジストリ、subagent delegation vs execute_code、14+プラットフォームGateway、共有プロバイダランタイム、拡張モデル。agent-core-first vs gateway-firstの比較分析を含む。

**Pages created**:
- `concepts/hermes-agent-architecture.md` — 包括的概念ページ（278行）。全14セクション：Overview（AIAgent中心）、Core Architecture（中心核+3実行モード）、Agent Loop（ターンライフサイクル・割り込み・並列性）、Prompt Assembly（キャッシュ/セッション固定/エフェメラルの3層）、Persistent State（SQLite+FTS5+JSONL+bounded memory）、Tool Runtime（自己登録レジストリ+承認フロー）、Subagent Delegation vs execute_code（2つの実行プリミティブ）、Gateway Layer（14+プラットフォーム+2レベルガード）、Provider Runtime（共有リゾルバ+フォールバック）、Extension Model（プラグイン/フック/プロバイダ）、Key Architectural Characteristics（4特性）、Trade-offs（複雑性/memory/skill explosion）、Code Reading Order（10段階）、References。10個のwikilink。

**Index/log**: index.mdのConceptsセクションにhermes-agent-architecture追加。総ページ数: 5177→5178、Full entries: 4631→4632、Concepts: 442→443。

## [2026-05-07] OpenClawアーキテクチャ概念ページ作成 — ChatGPT deep dive記事から

**Source**: User request (Discord) — raw/articles/2026-05-07_chatgpt-openclaw-architecture-deep-dive.md のwiki取り込み

**Raw article referenced**:
- `raw/articles/2026-05-07_chatgpt-openclaw-architecture-deep-dive.md` — OpenClaw内部アーキテクチャの詳細分析。Gateway-first設計、WS制御面、埋め込みagent runtime、セッション管理、sandbox分離、ノード、キューイング、サブエージェント、プラグインシステム、スキル索引注入、単一trust boundaryモデル。

**Pages created**:
- `concepts/openclaw-architecture.md` — 包括的概念ページ（~300行）。全17セクション：概要（Gateway-first）、全体アーキテクチャ、Gateway中核、WebSocketプロトコル、埋め込みagent runtime、エージェントループ、セッション管理（二層永続化）、ワークスペース（prompt注入）、システムプロンプト（OpenClaw-owned + sub-agent minimal mode）、ツール実行（Sandbox/Tool Policy/Elevatedの3軸分離）、ノード（capability surface + pairing）、キューイング（session/global lane + queue mode）、サブエージェント（background run + session tree）、プラグインシステム（4層 + capability register API）、スキル（索引注入パターン）、セキュリティ（単一trust boundary）、まとめ。5個のwikilink。

**Index/log**: index.mdのConceptsセクションにopenclaw-architecture追加。総ページ数: 5176→5177、Full entries: 4630→4631、Concepts: 441→442。

## [2026-05-08] HN DeepSeek-V4 議論から重要知見を抽出してwikiに統合

**Source**: User request (Discord) — news.ycombinator.com/item?id=47884971 の重要な議論のみ抽出。

**Raw article saved**:
- `raw/articles/2026-05-08_hn-deepseek-v4-discussion.md` — HNコミュニティ議論の合成。SWE-bench 80.6%、ローカル推論（Flash on Mac Studio M3 Ultra）、地政学的分析（検閲/hard refusal/制裁/欧州オプション）、開発者体験。

**Pages updated**:
- `concepts/deepseek-v4.md` — **Community Reception & Independent Benchmarks (HN)** セクション新設（V3進化サマリーと歴史的意義の間）。コミュニティベンチマーク表（SWE-bench 80.6%、PhD数学、システム設計、カスタマーサポート）、ローカル推論（Flash 154GB→Mac Studio）、開発者体験表、地政学的側面（検閲/hard refusal/ダンピング/制裁/欧州オプション）。歴史的意義に7番目の項目（SWE-bench 80.6%）を追加。フロントマターにHN source追加。
- `entities/deepseek.md` — V4 key factsにSWE-bench 80.6%とローカル推論情報を追加。
## [2026-05-08] DeepSeek-V4 Technical Report 論文取り込み（HuggingFace公開）

**Source**: User request (Discord) — DeepSeek-V4: million-token context intelligence。HuggingFace deepseek-ai/DeepSeek-V4-Pro より。

**Raw paper saved**:
- `raw/papers/2026-04-xx_deepseek-v4-technical-report.md` — DeepSeek-AI。Hybrid Attention (CSA+HCA+SWA)、Manifold-Constrained Hyper-Connections (mHC)、Muon Optimizer、MegaMoE Expert Parallelism、TileLang DSL、Anticipatory Routing、SwiGLU Clamping、Specialist Training + On-Policy Distillation、FP4 QAT、Interleaved Thinking、Quick Instruction。

**Pages created**:
- `concepts/deepseek-v4.md` — 包括的概念ページ（~220行）。モデルラインナップ（1.6T Pro/284B Flash/Pro-Max）、Hybrid Attentionの3層構造と詳細比較表、mHC（二重確率行列制約）、Muon Optimizer（Newton-Schulz直交化）、訓練インフラ（32T+ tokens, Anticipatory Routing, SwiGLU Clamping, MegaMoE, TileLang）、効率性比較表（V3.2比3.7-10x FLOPs削減）、ポストトレーニング（Specialist Training + OPD, Interleaved Thinking, FP4 QAT）、ベンチマーク（Codeforces 3206, 63% non-loss vs Opus 4.6）、**V3→V4進化サマリー比較表**（14次元）。11個のwikilink。

**Pages updated**:
- `entities/deepseek.md` — V4 Seriesセクションを技術的に拡充（Hybrid Attention/mHC/Muon/MegaMoE/TileLang/OPD/FP4 QAT列挙、効率性比較表、Codeforces 3206、63% non-loss、Interleaved Thinking）。フロントマターソース追加、Relationshipsにdeepseek-v4を追加。

**Index/log**: index.mdにdeepseek-v4追加。総ページ数: 5175→5176、Full entries: 4629→4630、Concepts: 440→441。
## [2026-05-08] Martin Fowler「The DeepSeek Series: A Technical Overview」参考取り込み

**Source**: User request (Discord) — martinfowler.com/articles/deepseek-papers.html の整理を参考にwiki強化。

**Raw article saved**:
- `raw/articles/2026-05-08_martinfowler-deepseek-papers.md` — Martin FowlerによるDeepSeek論文シリーズ（LLM→V2→V3→R1）の技術分析。HPC Co-Design哲学、3つの研究アーク（Efficiency/Sparsity/Reasoning）。

**Pages updated**:
- `entities/deepseek.md` — 大幅強化:
  - **Technical Evolution & HPC Co-Design Philosophy**セクション新設（OverviewとModelsの間）。HPC Co-Designの定義、3研究アーク表、論文シリーズ進化図（LLM→V2→V3→R1→V4のフロー）
  - **Earlier Models**にDeepSeek-LLM (Jan 2024, 67B, Scaling Laws) とDeepSeek-V2 (Jun 2024, MLA+DeepSeekMoE初導入) を追加
  - **Relationships**: deepseek-r1, grpo へのwikilink追加
  - **Sources**: martinfowler記事追加
## [2026-05-08] DeepSeek-R1 論文取り込み — arXiv:2501.12948（Nature掲載）

**Source**: User request (Discord) — Reasoningモデルのマイルストーン論文。Pure RLによる推論能力創発、Nature掲載。

**Raw paper saved**:
- `raw/papers/2025-01-22_2501.12948_deepseek-r1.md` — DeepSeek-AI。DeepSeek-R1-Zero（純粋RL→推論創発、GRPO、アハモーメント）、DeepSeek-R1（4段階パイプライン）、蒸留モデル（Qwen-1.5B〜Llama-70B）。AIME 2024: 79.8%、MATH-500: 97.3%。訓練コスト$294K。

**Pages created**:
- `concepts/deepseek-r1.md` — 包括的概念ページ。R1-Zero（純粋RLからの創発、アハモーメント）、R1（Cold Start→Reasoning RL→Rejection Sampling→General RLの4段階パイプライン）、蒸留（1.5BがGPT-4oを上回る）、ベンチマーク比較表（o1-1217対比）、制限事項、歴史的意義6点。18個のwikilink。
- `concepts/grpo.md` — Group Relative Policy Optimization 独立概念ページ。PPOのクリティックモデル問題、GRPOのアドバンテージ計算式・目的関数、ルールベース報酬設計、PPOとの比較表、適用事例（R1-Zero/R1/V3）、制限と今後の課題。PPO/RLHF/reasoning等にwikilink。

**Pages updated**:
- `entities/deepseek.md` — Earlier ModelsのR1エントリを拡充（Nature掲載、GRPO、アハモーメント、ベンチマーク、蒸留、$294K）。フロントマターにソース追加。

**Index/log**: index.mdのConceptsセクションにdeepseek-r1とgrpoを追加。総ページ数: 5173→5175、Full entries: 4627→4629、Concepts: 438→440。
## [2026-05-08] DeepSeek-V3 Technical Report 論文取り込み — arXiv:2412.19437

**Source**: User request (Discord) — マイルストーン的位置付け論文。DeepSeek-V3: 671B MoEモデル、GPT-4o級性能を$5.576Mで達成。

**Raw paper saved**:
- `raw/papers/2024-12-27_2412.19437_deepseek-v3-technical-report.md` — DeepSeek-AI (200+ authors)。MLA、Auxiliary-Loss-Free Load Balancing、Multi-Token Prediction、FP8混合精度訓練（671Bスケール初検証）、DualPipe。14.8Tトークン、2.788M H800 GPU時間、訓練中ロールバックゼロ。

**Pages created**:
- `concepts/deepseek-v3.md` — 包括的概念ページ。アーキテクチャ（MLA, DeepSeekMoE, MTP, Auxiliary-Loss-Free Load Balancing）、訓練（FP8, DualPipe, $5.576Mコスト内訳）、ベンチマーク（MMLU 88.5, MATH-500 90.2）、ポストトレーニング（R1蒸留, GRPO, YaRN 128K）、歴史的意義（6つの革新ポイント）、ハードウェア設計提言。13個のwikilink。

**Pages updated**:
- `entities/deepseek.md` — Earlier ModelsセクションにDeepSeek V3の記述を追加（671B/37B active, マイルストーン論文として位置付け）。フロントマターのsourcesとupdated日付を更新。

**Index/log**: index.mdのConceptsセクションにdeepseek-v3を追加。総ページ数: 5172→5173、Full entries: 4626→4627、Concepts: 437→438。
## [2026-05-08] 「Techno-Pessimism」概念ページ作成 — Curtis Yarvinのテクノ悲観主義マニフェスト

**Source**: User request (Discord) — graymirror.substack.com/p/a-techno-pessimist-manifesto のwiki取り込み

**Raw article saved**:
- `raw/articles/graymirror.substack.com--a-techno-pessimist-manifesto.md` — Curtis YarvinによるMarc Andreessen「Techno-Optimist Manifesto」への反論。二つの曲線（技術上昇・秩序下降）、ヨハネスブルグ・プロトコル、資源呪いのアナロジー、ゼロ限界生産物人間問題、トロツキー・ニーチェ・ウィリアム・ジェームズ・E.M.フォースターとの思想的系譜。

**Pages created**:
- `concepts/techno-pessimism.md` — 新規概念ページ。テクノ楽観主義との対比表、AIへの示唆（「AI万能解決」への疑問、ゼロ限界生産物人間、アクセラレーショニズム=革命的ユートピアニズム、秩序問題は技術で解決不能）を含む。

## [2026-05-08] Predictive $\\mathcal{V}$-Information 概念ページ作成 — Xu et al. ICLR 2020

**Source**: User request (Discord) — arxiv.org/abs/2002.10689 のwiki取り込み

**Raw paper saved**:
- `raw/papers/2020-02-25_2002.10689_predictive-v-information.md` — Yilun Xu, Shengjia Zhao, Jiaming Song, Russell Stewart, Stefano Ermon による Predictive $\mathcal{V}$-Information 理論。Shannon情報理論の変分拡張で観測者の計算制約を考慮。DPI違反、高次元でのPAC推定保証、構造学習・公平表現学習への応用。ICLR 2020 Talk、211被引用。

**Pages created**:
- `concepts/predictive-v-information.md` — 新規概念ページ。定義（$\mathcal{V}$-Entropy, Conditional $\mathcal{V}$-Entropy, $\mathcal{V}$-Information）、理論的意義（DPI違反、PAC保証、既存指標の一般化）、3つの応用領域（構造学習、公平表現学習、深層表現学習）を含む。Shannon情報理論との比較表あり。

---



**Source**: User request (Discord) — qchu.substack.com/p/core-dump のwiki取り込み

**Raw articles saved**:
- `raw/articles/2024-09-16_qchu-core-dump.md` — QC (Qiaochu Yuan) によるLLM時代の言語的真正性に関するエッセイ。言語的めまい（linguistic vertigo）、頭の言葉（Head Words） vs 身体の言葉（Body Words）、LLMをトレーサー色素（tracer dye）とする社会の虚ろな言語の診断、RLHFによる社会の影（societal shadow）のマッピング。Gwernによるコメント補遺：プロンプト視覚（prompt-vision/unseeing）、モード崩壊したRLHFの不気味さ、言語機械としての人間。

**Pages created**:
- `concepts/linguistic-vertigo.md` — 新規概念ページ。QCの一元論的な言語批判から抽出した5つの概念を構造化：言語的めまい、頭 vs 身体の言葉、トレーサー色素、社会的影、プロンプト視覚。既存の[[concepts/rlhf]]との比較表を含む。

---



**Source**: User request (Discord) — gwern.net/blog/2025/better-llm-writing のwiki取り込み

**Raw articles saved**:
- `raw/articles/2025-05-29_gwern-better-llm-writing.md` — Gwern Branwenによる LLM Creative Writing 手法の包括的概要。Anti-Examples prompting trick、Manual of Style (MoS) 抽出、メタ学習/パーソナライゼーション、Atomic Snippets、Generate-Rank-Selectブレインストーミング。核心哲学：質は検索プロセスから生まれ、初回生成からは生まれない。

**Pages created**:
- `concepts/llm-creative-writing.md` — GwernのLLM創作執筆手法を文書化した新規概念ページ。Anti-Examples逆転換トリック、MoS抽出、メタ学習インタビュー、Atomic Snippets多層抽象度出力、Seriation/ツリー埋め込み、5つの重要インサイト比較表を含む。Hermes Agentの定期レポーティング品質向上への応用セクションも追加。

**Pages enriched**:
- `entities/gwern.md` — Sourcesセクションに"Towards Better LLM Creative Writing"を追加。[[concepts/llm-creative-writing]]との相互参照。

---
## [2026-05-07] Transformer Architecture概念ページ拡充 — Gwern "You Could've Invented Transformers"

**Source**: User request (Discord) — gwern.net/blog/2025/you-could-have-invented-transformers のwiki取り込み

**Raw articles saved**:
- `raw/articles/2025-05-25_gwern-invented-transformers.md` — Gwern Branwenによる Transformerの「発見フィクション」提案。n-gramからQKV自己注意までの論理的導出。多様体相互作用の直接アクセスとしての自己注意、スケールでの創発（誘導ヘッド、文脈内学習）。

**Pages created/updated**:
- `concepts/transformer-architecture.md` — スタブから完全版へ。Transformerの教育的「発見フィクション」導出。n-gram→埋め込み→畳み込み→MLP-Mixer→動的畳み込み→QKV自己注意→多頭注意→位置埋め込み→最適化「おまじない」の9段階。スケールでの創発特性。SSM/線形Transformerとの関連付け。[attention-mechanism-variants](concepts/attention-mechanism-variants.md)へのリンクを含む。

---

## [2026-05-07] Scaling Hypothesis概念ページ拡充 — gwern.net論文本体からの完全版

**Source**: User request (Discord) — gwern.net/scaling-hypothesis のwiki取り込み

**Raw articles saved**:
- `raw/articles/2020-05-28_gwern-scaling-hypothesis.md` — Gwern Branwenによる Scaling Hypothesis 論文（2020年、2022年更新）

**Pages created/updated**:
- `concepts/scaling-hypothesis.md` — スタブから完全版へ。Strong/Weak Scaling Hypothesisの区別、Blessings of Scale、最も深い残差（The Last Bits）、創発的エージェンシー（It From Byte）、ハードウェアオーバーハング論。Scaling Laws概念ページとの比較表を含む。

---

## [2026-05-07] Scaling Hypothesis概念ページ拡充 — Hyung Won Chung講義からアーキテクチャ事例

**Source**: User request (Discord) — Stanford CS25講義 + Google Slidesのwiki取り込み

**Raw articles saved**:
- `raw/articles/2024-04-11_hyungwonchung-shaping-future-ai-transformer.md` — Hyung Won Chung (OpenAI) のCS25講義（2024年4月）
- `raw/articles/2024-04-11_hyungwonchung-transcript.md` — 同講義の文字起こし

**Pages updated**:
- `concepts/scaling-hypothesis.md` — 「Architectural Case Study: Hyung Won Chung」セクション追加。

---

## [2026-05-07] Scaling Hypothesis概念ページ拡充 — Ilya Sutskever NeurIPS 2024基調講演

**Source**: User request (Discord) — Sutskever 10年総括講演のwiki取り込み

**Raw articles saved**:
- `raw/articles/2024-12-13_ilyasutskever-seq2seq-decade.md` — Ilya Sutskever (OpenAI/SSI) のNeurIPS 2024基調講演（2024年12月）
- `raw/articles/2024-12-13_ilyasutskever-transcript.md` — 同講演の文字起こし

**Pages updated**:
- `concepts/scaling-hypothesis.md` — 「Ilya Sutskever: The End of Pretraining (NeurIPS 2024)」セクション追加。

---

## [2026-05-07] Scaling Hypothesis概念ページ拡充 — Daniel Hanのpost-pretraining分析

**Source**: User request (Discord) — Daniel Han (@danielhanchen) のIlya講演メモスレッドのwiki取り込み

**Raw articles saved**:
- `raw/articles/2024-12-16_danielhanchen-post-pretraining.md` — Daniel HanのIlya講演分析スレッド（2024年12月）

**Pages updated**:
- `concepts/scaling-hypothesis.md` — 「Post-Pretraining Playbook: Daniel Han's Analysis」セクション追加。

---

## [2026-05-07] Scaling Hypothesis概念ページ拡充 — 2025年の発展とクロスリファレンス

**Source**: User request (Discord) — 2025年の議論の調査とクロスリファレンス追加

**Pages updated**:
- `concepts/scaling-hypothesis.md` — 「2025 Cross-References and Developments」セクション追加。o3/o4-mini (test-time compute scaling), SynthLLM (synthetic data scaling laws), BLT (byte latent transformer), Memory Layers at Scale (sparse lookup tables, 128B param). 各トピックをDaniel Hanの5アプローチにマッピング。2020→2024→2025の進化比較表を含む。

---

## [2026-05-07] turbopufferエンティティ拡充 — 全ブログ記事8本からエンリッチメント

**Source**: User request (Discord) — turbopufferブログ記事群からのエンリッチメント

**Raw articles saved** (8 new, total 10):
- `raw/articles/2024-09-04_turbopuffer-continuous-recall.md` — Production recall@10 monitoring via 1% query sampling. [Morgan Gallant]
- `raw/articles/2025-01-21_turbopuffer-native-filtering.md` — SPFresh clustering-based native filtered vector search (>90% recall). [Bojan Serafimov]
- `raw/articles/2026-01-07_turbopuffer-bm25-scaling.md` — BM25 power law scaling: K=0.35→0.92, essential terms optimization. [Adrien Grand]
- `raw/articles/2026-01-14_turbopuffer-fts-v2-postings.md` — Fixed-size block partitioning inverted indexes (9.9x size reduction). [Morgan Gallant, Adrien Grand]
- `raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore.md` — Vectorized MAXSCORE > WAND for long LLM queries. [Adrien Grand, Morgan Gallant]
- `raw/articles/2026-02-03_turbopuffer-fts-v2.md` — FTS v2 announcement: 20x faster, 10x smaller indexes. [Adrien Grand, Morgan Gallant, Nikhil Benesch]
- `raw/articles/2026-03-08_turbopuffer-rust-zero-cost-simd.md` — Rust batched iterators unblocking SIMD: 220ms→47ms. [Xavier Denis]
- `raw/articles/2026-05-05_turbopuffer-ann-v3.md` — ANN v3: 100B vectors @ 200ms p99 via RaBitQ + AVX-512. [Nathan VanBenschoten]

**Pages enriched**:
- [[entities/turbopuffer]] — 151→319行に拡大。新規追加: ANN v3性能表 / Native Filtering / Continuous Recall / FTS v2（MAXSCORE + ブロック分割 + BM25 scaling）/ チーム一覧（8名）/ 沿革拡張（6→14エントリ）/ 参考文献再編成

**Description**:
![turbopuffer](https://turbopuffer.com/)

---


## [2026-05-07] Object Storage Queueパターン + turbopuffer entity追加 — S3ベース分散キューの実装パターン

**Source**: User request (Discord) — zero-disk-architecture的なキュー実装として関心

**Raw articles saved** (2):
- `raw/articles/2026-05-07_object-storage-queue-turbopuffer.md` — turbopufferによる単一JSONファイル分散キュー実装
- `raw/articles/2026-05-07_turbopuffer-fast-search-object-storage.md` — turbopuffer製品発表ブログ

**Pages created**:
- [[concepts/object-storage-queue]] — Object Storage Queue: S3のCASを利用した分散キュー実装パターン。Group Commit / Stateless Broker / Heartbeat Recovery。ゼロディスクアーキテクチャの応用。Absurdとの詳細比較を含む。
- [[entities/turbopuffer]] — Object-Storage-Native検索エンジン（ベクトル＋全文検索）。SPFresh ANN、S3ネイティブLSM Tree、ステートレスRustノード。Cursor（95%コスト削減）、Notion AI、Linear等が顧客。

**Pages enriched**:
- [[concepts/zero-disk-architecture]] — Industry Adoptionセクションの"Turbo Puffer"表記を[[entities/turbopuffer]]に修正

---

## [2026-05-07] Absurd概念ページ作成 — Postgres-Native Durable Execution for AI Agents

**Source**: User request (Discord) — 非同期処理基盤の実装パターンとして関心

**Raw articles saved** (2):
- `raw/articles/2025-11-03_absurd-workflows-armin-ronacher.md` — 初回発表（Armin Ronacher）
- `raw/articles/2026-04-04_absurd-in-production-armin-ronacher.md` — 5ヶ月本番運用レポート

**Pages created**:
- [[concepts/absurd-durable-execution]] — Postgres-Native Durable Execution: AI Agent文脈での非同期処理基盤。LLMループのチェックポイント化、Pi Agent統合パターン、Event駆動Agent間連携。Temporal/DBOS/PGMQとの比較を含む。

---

## [2026-05-06] X Bookmarks Ingest — 6 articles processed, subagent patterns + agent observability + Factory AI Free Droid

**Source**: X bookmarks ingest cron job (x-bookmarks-ingest)

**Raw articles saved** (6):
- `raw/articles/2026-05-05_how-agents-manage-other-agents-four-subagent-patterns.md` — Philipp Schmid's 4 subagent patterns (Inline Tool, Fan-Out, Agent Pool, Teams)
- `raw/articles/2026-05-05_agent-observability-needs-feedback-to-power-learning.md` — Harrison Chase's feedback-powered observability thesis
- `raw/articles/2026-05-05_gemma-4-drafter-explained.md` — Google Gemma MTP drafter technical deep-dive
- `raw/articles/2026-05-03_how-to-think-using-ai.md` — Sufyan Maan's AI-augmented thinking framework (metadata-only)
- `raw/articles/2026-04-03_free-droid-for-all.md` — Factory AI free autonomous coding agents announcement
- `raw/articles/2026-05-05_the-layoffs-will-continue-till-we-learn-to-use-ai.md` — Brian Armstrong's Coinbase AI layoffs perspective (lightweight)

**Pages created**:
- [[concepts/agent-observability]] — AIエージェントの可観測性とフィードバック駆動学習ループ概念

**Pages enriched**:
- [[entities/phil-schmid]] — Added Subagent Patterns (May 2026) to Agent Infrastructure section + timeline entry + reference
- [[entities/harrison-chase]] — Added Agent Observability & Feedback Loop Thesis section + source
- [[concepts/agent-patterns]] — Added structured Subagent Patterns section (4 patterns, comparison table, implementation guidelines)
- [[concepts/speculative-decoding]] — Added Gemma 4 X article as source
- [[entities/sero]] — Added Factory AI — Free Droid announcement section

---


**Topics discovered**: 3 new models, 1 IDE concept
**Pages created**: 3 new concept pages + 1 existing concept updated
**Pages updated**: `concepts/github-copilot-billing.md` (Cursor IDE competition context)
**Index maintenance**: Fixed pipe table corruption, removed 22 duplicate entries, updated page counts

### New Concept Pages (3)
- [[concepts/gpt-5.5-instant]] — OpenAIのGPT-5.5 Instant。2026年5月、ChatGPTとOpenAI APIのデフォルトモデルに。記憶保持、ファイル統合、Gmail連携でパーソナルAIワークステーション化。
- [[concepts/glm-5-1]] — Zhipu AIのオープンソースMoEモデル（744Bパラメータ、40Bアクティブ）。DeepSeek Sparse Attention採用。長期自律エージェントタスクに特化。
- [[concepts/minimax-m2-7]] — MiniMaxの2026年フロンティアLLM。自律エージェントハーネス構築とRL実験による自己改善ループが特徴。

### Index Maintenance
- Fixed pipe table corruption (`|- [[` → `- [[`) across index.md
- Removed 22 duplicate entries (TODO stubs where rich entries existed)
- Updated header counts: Total pages 5167, Full entries 4621, Stubs 546

---

## [2026-05-06] Active Crawl — Meta AI Agents, Cloudflare LLM Infra, Project Mariner, Mistral Vibe, ServiceNow

**Topics discovered**: 5 major developments
**Pages created**: 5 new concept pages
**Pages updated**: 2 existing entity pages (Cloudflare, Meta)
**Raw articles saved**: 5

### New Concept Pages (5)
- [[concepts/meta-capacity-efficiency-agents]] — Meta's unified AI agents for capacity optimization at hyperscale
- [[concepts/cloudflare-llm-infrastructure]] — Cloudflare's custom LLM inference stack with PD disaggregation, Infire engine, Mooncake KV-cache
- [[concepts/google-project-mariner-shutdown]] — Google's shutdown of Project Mariner browser agent in May 2026
- [[concepts/mistral-vibe-remote-agents]] — Mistral Medium 3.5 + Vibe Remote Agents for async cloud coding
- [[concepts/mit-encompass]] — MIT CSAIL framework for AI agent search with automatic backtracking
- [[concepts/servicenow-ai-workforce]] — ServiceNow's autonomous AI workforce for enterprise operations
- [[concepts/deepclaude]] — Open-source tool enabling Claude Code's agent loop with DeepSeek V4 Pro

### Entity Pages Updated (2)
- [[entities/cloudflare]] — Added Project Think, internal AI engineering stack, autonomous account provisioning
- [[entities/meta]] — Added Capacity Efficiency AI Agent, KernelEvolve, Ranking Engineer Agent

### Raw Articles Saved (5)
- `raw/articles/2026-05-06_wired-google-project-mariner-shakeup.md`
- `raw/articles/google-project-mariner-shutdown.md`
- `raw/articles/meta-capacity-efficiency-agents-2026.md`
- `raw/articles/mistral-medium-3-5-vibe-remote-agents.md`
- `raw/articles/mit-encompass-feb-2026.md`

### Key Themes Identified
1. **Agent Infrastructure** — Meta, Cloudflare building specialized infra for agentic workloads
2. **Browser Agent Reality Check** — Project Mariner shutdown shows limits of current browser automation
3. **Agent Framework Interoperability** — DeepClaude demonstrates decoupling orchestration from model inference
4. **Enterprise AI Workforce** — ServiceNow positioning AI as autonomous workforce, not just tools
5. **Open Model + Cloud Agent Convergence** — Mistral combining open weights with cloud agent infrastructure

---

## [2026-05-06] Blog Ingest — Gary Marcus AI Agent Security + Simon Willison AI Ethics

**Pipeline**: blog-wiki-ingest ← blog-triage ← blog-ingest
**Triage**: 2 take, 3 reference, 15 skip (from 20 candidates)
**Source articles**:
- Gary Marcus "Breaking: Autonomous Agents are a Shitshow" (847-deployment empirical study)
- Simon Willison "Our AI started a cafe in Stockholm" (Andon Labs AI cafe ethics)

### Wiki Pages Updated (2)

**Concepts:**
- 🔄 **[[concepts/ai-agent-security]]** — Upgraded from stub to full page. Stanford/MIT/CMU 2026 study: 91% tool-chaining vulnerable, 89.4% goal drift at ~30 steps, 94% memory-augmented poisoning. OpenClaw/Moltbook: 770K agents compromised via single DB exploit. Taxonomy showing agents more vulnerable than stateless LLMs.

**Entities:**
- 🔄 **[[entities/simon-willison]]** — Added "AI Ethics Commentary: Stockholm AI Cafe Experiment" section. Willison's ethical stance: autonomous agent outbound actions affecting non-consenting third parties require human-in-the-loop. Andon Labs AI manager ordering errors, police permit application, supplier EMERGENCY emails.

### Articles Referenced
- [simonwillison.net: datasette-referrer-policy 0.1](https://simonwillison.net/2026/May/5/datasette-referrer-policy/#atom-everything) — Minor Codex + GPT-5.5 plugin build. Reference only.
- [garymarcus.substack.com: Musk-OpenAI trial](https://garymarcus.substack.com/p/what-matters-or-should-matter-at) — Brockman diary testimony. Already covered in gary-marcus entity page. Reference only.

---

## [2026-05-06] Newsletter Ingest — AINews Silicon Valley Services, Vibe Physics, Codex Push, Claude JV

**Pipeline**: newsletter-wiki-ingest ← newsletter-triage ← newsletter-ingest
**Sources**: 5 newsletters (AINews, Latent Space/Vibe Physics, Ben's Bites/Codex, Superintel/Claude, Hyperdimensional/Dean Ball)
**Triage**: 14 take, 5 reference, 2 skip

### Wiki Pages Created (8 new)

**Concepts:**
- 🆕 **[[concepts/ai-services-joint-ventures]]** — AI Services JVs: Anthropic × Blackstone/Goldman $1.5B, OpenAI $4B Deployment Co, Tessera Series A. Service-as-Software thesis in JV form.
- 🆕 **[[concepts/programbench]]** — Meta's full-repo generation benchmark. ~200 tasks, 0% top accuracy. Exposes whole-repo gap in LLM code generation.
- 🆕 **[[concepts/vibe-physics]]** — AI-driven scientific discovery. Alex Lupsasca (OpenAI) — GPT-5.x reproduces months of research in 30min, 110 pages of novel graviton physics in 1 day.

**Entities:**
- 🆕 **[[entities/cursor-ai]]** — Cursor CI-fix agents + SpaceX acquisition option ($60B).
- 🆕 **[[entities/radixark]]** — $100M seed for SGLang inference + Miles RL infrastructure.
- 🆕 **[[entities/perplexity]]** — Professional Finance Computer (35 workflows) + NEJM/BMJ premium access.
- 🆕 **[[entities/vercel]]** — deepsec: open-source security harness using coding agents.
- 🆕 **[[entities/flue]]** — TypeScript framework for Claude Code-style agents.

### Wiki Pages Enriched (3)
- ✏️ **[[entities/openai]]** — GPT-5.5 Instant default model, Agents SDK TypeScript + Auto Review, Codex push details, $4B Deployment Company JV.
- ✏️ **[[entities/anthropic]]** — $1.5B Blackstone/Goldman JV, Orbit proactive assistant (Slack/Gmail/GitHub/Figma).
- ✏️ **[[entities/manus]]** — Manus Cloud Computer: always-on cloud machine for persistent agent execution.

### Reference Items (Not Processed into Pages)
- Model–Harness–Task fit > benchmarks (reference)
- Grok 4.3 API: 1M context, $1.25/$2.50 pricing
- Gemini API Webhooks + Web UI Bench (20 models)
- Dean Ball Sustainable Interference framework (covered in dean-ball.md)
- MCP security governance for Claude Cowork

### Skipped
- Wispr Flow / RAVEN AI / self-destructing plastic (non-AI)
- Lenny's Podcast AI monetization (business strategy, not technical AI)

New pages: 8 (3 concepts + 5 entities). Enriched: 3. Reference: 5. Skipped: 2.
Sources: AINews (swyx), Latent Space (lupsasca), Ben's Bites (codex), Superintel (claude), Hyperdimensional (dean-ball).
## [2026-05-06] Blog Ingest — Simon Willison Datasette Plugins, Gary Marcus Autonomous Agents Critique, Daring Fireball Software Philosophy

**Blog Ingest**: 20 articles collected from 12 blogs. 4 new wiki concept pages created, 2 entity pages updated.

### Wiki Pages Created
- 🆕 **[[concepts/datasette-llm]]** — LLM-powered SQL queries for Datasette. Natural language to SQL translation plugin (v0.1a7). Works with any provider supported by Simon's llm CLI.
- 🆕 **[[concepts/datasette-referrer-policy]]** — Datasette plugin for controlling HTTP Referrer-Policy headers to prevent URL leakage to external sites (v0.1).
- 🆕 **[[concepts/llm-echo]]** — Plugin for the llm CLI that records and replays LLM API interactions. Enables deterministic testing, prompt engineering iteration, and model comparison without burning API credits (v0.5a0).
- 🆕 **[[concepts/ai-retail-experiments]]** — AI-managed physical businesses (cafes, retail stores). Andon Labs' Stockholm cafe experiment where AI manager "Mona" made comical ordering errors and caused real-world disruption. Raises ethical concerns about non-consensual impact on humans and systems.

### Wiki Pages Enriched
- ✏️ **[[entities/gary-marcus]]** — Added "Autonomous Agents are a Shitshow" security study (May 2026) — identifies core challenges: context overflow, prompt injection, tool misuse, agent-to-agent communication, hallucination in action-taking, and proposes mitigation strategies. Added Musk-OpenAI trial analysis with five key issues. Updated tags and sources.
- ✏️ **[[entities/simon-willison]]** — Added May 2026 articles: datasette-llm, llm-echo, datasette-referrer-policy, AI cafe in Stockholm. Updated date.

### Notable Non-AI Articles (Saved as Raw, Not Processed)
- **Daring Fireball**: Software as the Product of Obsession Times Voice — critiques "Software Brain" mentality (Nilay Patel's term) where software is treated as databases rather than craft/art.
- **Troy Hunt**: Weekly Update 502 — cybersecurity roundup.
- **nesbitt.io**: Package Manager Threat Models — supply chain security analysis.
- **shkspr.mobi**: RSS Feeds Send Me More Traffic Than Google — RSS vs search traffic analysis.
- **berthub.eu**: The Impossible Things We Have to Believe — technology skepticism piece.
- **johndcook.com**: Changing one character in a PDF — PDF format quirk exploration.
- **Apple News**: $250M Siri settlement, Mac RAM cuts, Iran War costs.
- **Old New Thing**: TAB key dispute between Microsoft and IBM organizational structures.
- **dfarq.homeip.net**: First desktop computer: Datapoint 2200 — computing history.

### Raw Articles Saved
- 20 articles saved to wiki/raw/articles/ (see saved_articles in script output)

New concepts: 4. Updated entities: 2. New raw articles: 20.
Sources: Blog ingestion (blog-ingest cron job), 12 blogs scanned.

## [2026-05-05] X Accounts Scan — Gemma 4 MTP, Zyphra TSP, Agentic Coding, InfoLaw, IBM Granite Embeddings

**X Accounts Scan**: 12 new posts processed from 4 accounts (simonw, gm8xx8, _philschmid, dbreunig, charles_irl).

### Wiki Pages Created
- 🆕 **[[concepts/tsp-tensor-sequence-parallelism]]** — Zyphra's TSP: folds TP + SP onto single device axis. 2× throughput at 128K tokens, 55% less memory than TP alone. Paper: arXiv:2604.26294.
- 🆕 **[[entities/ibm-granite-embedding]]** — IBM's dense embedding models (311M + 97M params). ModernBERT architecture, 32K context, Matryoshka MRL, Apache 2.0, 200+ languages.

### Wiki Pages Enriched
- ✏️ **[[concepts/agentic-coding]]** — Stub → full page. Drew Breunig's 10 Lessons framework: Spec-Driven Development Triangle (Spec + Code + Tests), 10 workflow patterns for coding with agents.
- ✏️ **[[concepts/scaling-laws]]** — Stub → full page. Chinchilla (2022) foundation + InfoLaw (Liu et al., ICML 2026): information accumulation model for data quality, mixture, and repetition.
- ✏️ **[[concepts/speculative-decoding]]** — Added Multi-Token Prediction (MTP) Drafters section: Google Gemma 4's production implementation, 3× speedup, shared KV cache, Apple Silicon batch optimization.
- ✏️ **[[entities/gemma-4]]** — Added MTP Drafters section: architecture, performance impact table, cross-platform support, Apache 2.0 licensing.
- ✏️ **[[entities/drew-breunig--writings]]** — Added "10 Lessons for Agentic Coding" (May 2026) to AI Period writings.

### Raw Articles Saved
- 2026-05-05_google-gemma-4-multi-token-prediction-drafters.md
- 2026-05-05_zyphra-tsp-tensor-sequence-parallelism.md
- 2026-05-04_drew-breunig-10-lessons-agentic-coding.md
- 2026-05-04_infolaw-information-scaling-laws.md
- 2026-05-05_ibm-granite-embedding-311m-multilingual-r2.md

### Additional Posts (Not Yet Processed)
- Simon Willison: Bun Zig→Rust port, Granite 4.1 SVG pelican gallery, AI cafe in Stockholm, GPT-5.5 Instant API update
- Charles Frye: MADE benchmark paper (arXiv:2601.20996)
- gm8xx8: IBM Granite Embedding 97M compact model

New concepts: 1. New entities: 1. Updated concepts: 3. Updated entities: 2. New raw articles: 5.
Sources: X/Twitter scan (x-accounts-scan cron job).
## [2026-05-05] Entity Enrichment: Daniel Tunkelang — O'Reilly profile + multi-source research

- **[[entities/daniel-tunkelang]]** — Enriched from skeleton to full entity page. Added from O'Reilly profile + Springer author bio + SlideShare: PhD CS (CMU), BS Math/CS (MIT). Endeca founding employee, Chief Scientist (acquired by Oracle $1.1B). Led local search at Google. Director of Data Science at LinkedIn (founded query understanding team). Book: Faceted Search (Springer, 76+ citations). 24 US patents. Founded HCIR symposium (2007). Consulting clients: Etsy, Flipkart. O'Reilly articles (2015-2016). Previous stints at IBM T.J. Watson and AT&T Labs. Removed `status: skeleton`.
- Source: https://www.oreilly.com/people/daniel-tunkelang/, https://link.springer.com/book/10.1007/978-3-031-02262-3

## [2026-05-05] YouTube Video: "Will Agents Replace Search Teams?" — Doug Turnbull & Daniel Tunkelang

- **[[raw/articles/2026-01-29_doug-turnbull_will-agents-replace-search-teams]]** — Saved raw article: 55-minute discussion on what agents can and cannot replace in search teams. Covers latency-feedback tradeoff, e-commerce search spectrum, economic disruption (EXA, Reddit, Stack Overflow), stakes-based error models, domain-specific LLM assumptions (auto parts case study), personalization risks, and the rising importance of critical thinking.
- **[[entities/doug-turnbull-speaking]]** — Added this talk to the Conference Talks list.
- **[[entities/daniel-tunkelang]]** — Created new entity page (skeleton) for search veteran and Endeca co-founder.
- **[[concepts/agentic-search]]** — Added "Discussion: Will Agents Replace Search Teams?" section with: Tunkelang's feedback loop critique, search needs spectrum, economic disruption analysis, stakes-based error sensitivity model, domain-specific assumption case study, education/critical thinking implications, personalization overfitting risks, and search team defense.
- New raw articles: 1. New entities: 1 (daniel-tunkelang). New concepts: 0. Updated entities: 1 (doug-turnbull-speaking). Updated concepts: 1 (agentic-search).
- Source: https://www.youtube.com/watch?v=OGnW2Pu2uVE

## [2026-05-05] Karpathy Loop → Search Domain | Doug Turnbull's agent-coded reranker as Karpathy Loop search version

- **[[raw/articles/2025-10-19_doug-turnbull_agent-coded-search-reranker.md]]** — Saved raw article: agent generates generalizable Python reranker code, iteratively optimizes NDCG through eval feedback.
- **[[concepts/karpathy-loop]]** — Added "Search Domain: Agent-Coded Reranker as Karpathy Loop" section: parallel architecture table (autoresearch vs search reranker), guardrails against gaming analysis, Karpathy Loop generalization confirmation. Added Search Reranker Optimization to Real-World Applications.
- **[[concepts/autonomous-component-optimization]]** — Added "Early Precedents" section citing Doug Turnbull's Oct 2025 article as precedent predating the concept by ~6 months.
- New raw article: 1. Updated concepts: 2 (karpathy-loop, autonomous-component-optimization).
- Source: https://softwaredoug.com/blog/2025/10/19/agentic-code-generation-to-optimize-a-search-reranker

## [2026-05-05] Trending Topics | 7 topics + Wiki Updates (Sierra, xAI, NVIDIA)

**Trending Topics Report**: Web research + newsletter triage → trending topics report saved to inbox/rss-scans/.

### Wiki Pages Updated
- 🔄 [[entities/sierra]] — Updated valuation ($15.8B), Series E details ($950M), Ghostwriter AaaS, customer list
- 🔄 [[entities/xai]] — Added GPU Utilization Crisis section (11% utilization, Colossus 2GW/555K GPUs)
- 🔄 [[entities/nvidia]] — Added China market share zero section (95%→0%, $4.5B charges)

### Trending Topics Covered
1. ホワイトハウス、AIモデル事前審査の大統領令を検討（NYT/Forbes/Bloomberg）
2. Sierra $950M Series E at $15.8B valuation（CNBC/TechCrunch）
3. Jack Clark Import AI 455 — Automating AI Research（jack-clark.net）
4. Nathan Lambert「蒸留パニック」— distillation policy debate（Interconnects）
5. xAI GPU稼働率11%問題（The Information/WCCFTech）
6. NVIDIA中国市場シェア0% — Jensen Huang「輸出規制は裏目」（Tom's Hardware/SEC 10-K）
7. AIエージェント投資ブーム全体像（Axios: $24B in 2025）

## [2026-05-05] Active Crawl | Cloudflare LLM Infra + Shadow AI Governance + ADLC + Salesforce Headless 360 + Portkey/Palo Alto

**Batch**: Web research → 4 sources → 6 new wiki pages (3 concepts, 3 entities).

### New Pages Created
- 🆕 [[concepts/cloudflare-llm-infrastructure]] — Cloudflare's custom LLM inference stack. PD disaggregation, Infire Rust engine, Mooncake KV-cache, EAGLE-3 speculative decoding. 3x latency improvement, 80% cache hit ratio.
- 🆕 [[concepts/shadow-ai-governance]] — 80% of Fortune 500 use AI agents without governance strategy. 5-capability control framework (Registry, Access Control, Visualization, Interoperability, Security).
- 🆕 [[concepts/agent-development-lifecycle]] — ADLC framework formalizing agent operations: Agent Supervisor, QA Lead, AI Ops Manager, Chief AI Officer. DevOps vs. ADLC comparison.
- 🆕 [[entities/salesforce-headless-360]] — Salesforce's agent-first restructuring. APIs, MCP, CLI. Browser UI optional.
- 🆕 [[entities/portkey]] — AI agent security platform. Acquired by Palo Alto Networks (Q4 2026). Action inspection, 99.99% uptime.
- 🆕 [[entities/palo-alto-networks]] — Cybersecurity company. Portkey acquisition signals agent security maturity.

### Raw Articles Saved
- `raw/articles/2026-05-05_cloudflare-high-performance-llms.md` — Cloudflare blog: Infire engine, PD disaggregation, Mooncake KV-cache
- `raw/articles/2026-05-04_shadow-ai-governance-crisis.md` — Security Boulevard: 5-capability framework, Zscaler discovery of 4M prompts/week
- `raw/articles/2026-05-01_salesforce-8-ways-ai-agents-evolving-2026.md` — Salesforce: ADLC, Headless 360, HyperClassifier, deterministic guardrails
- `raw/articles/2026-05-05_ai-agent-news-weekly-apr28-may4.md` — AI Agent Store: Portkey/Palo Alto, FIDO, NVIDIA Nemotron 3 Nano Omni

### Cross-References Added
- [[concepts/cloudflare-llm-infrastructure]] ↔ [[concepts/mooncake]], [[concepts/nvidia-dynamo]], [[entities/kimi]]
- [[concepts/shadow-ai-governance]] ↔ [[concepts/agent-governance]], [[concepts/agent-iam]], [[concepts/agentic-security]], [[concepts/zero-trust-agentic-ai]]
- [[concepts/agent-development-lifecycle]] ↔ [[concepts/harness-engineering]], [[concepts/agent-governance]], [[concepts/ai-observability]]
- [[entities/salesforce-headless-360]] ↔ [[concepts/headless-saas]], [[concepts/model-context-protocol-mcp]]
- [[entities/portkey]] ↔ [[entities/palo-alto-networks]], [[concepts/agentic-security]], [[concepts/shadow-ai-governance]]

### Topics Researched But Already Covered
- MCP scale (97M installs): Covered in [[concepts/model-context-protocol-mcp]]
- Agent harness patterns: Already extensively covered in [[concepts/harness-engineering]]
- $700B AI infrastructure spend: Covered in [[concepts/ai-bubble-economics]], [[concepts/compute-scaling-bottlenecks]]

---
## [2026-05-05] Newsletter Ingest | Import AI 455 + AINews + Hyperdimensional + Interconnects + Hugo Bowne + Atlantic

**Batch**: 6 newsletter articles from triage → 5 new entity pages, 1 new concept, 2 concept enrichments.

### New Pages Created
- 🆕 [[entities/jack-clark]] — Anthropic co-founder, Import AI newsletter. 60%+ recursive self-improvement probability by end 2028.
- 🆕 [[entities/dean-ball]] — AI policy analyst, Hyperdimensional. Mythos governance framework, IVOs.
- 🆕 [[entities/hugo-bowne]] — Data scientist, AI privacy engineering writer. 3-layer guardrail framework.
- 🆕 [[entities/sierra]] — AI customer service platform. $15B valuation, $200M+ ARR. Harness-as-a-Service.
- 🆕 [[concepts/recursive-self-improvement]] — AI autonomously building successors. Capability evidence, compounding alignment risk.

### Pages Enriched
- ✏️ [[concepts/harness-engineering]] — Added Token Burn Crisis (60M tokens, $221/session), Context Pipelines as Moats (52.8%→66.5% on Terminal-Bench 2.0), Sierra case study, Zyphra TSP/DORA infrastructure.
- ✏️ [[concepts/ai-safety]] — Added Privacy Engineering for AI Agents section. 3-layer guardrail framework, context leakage vulnerability, privacy observability practices.

### Raw Articles Saved
- `raw/articles/2026-05-04_import-ai-455-automating-ai-research.md` — Jack Clark, 60% RSI probability
- `raw/articles/2026-05-04_aviate-navigate-communicate-dean-ball.md` — Dean Ball, Mythos governance
- `raw/articles/2026-05-04_15-privacy-questions-ai-builder.md` — Hugo Bowne, privacy engineering

### Already Covered (No Action Needed)
- Nathan Lambert's Distillation Panic: Already fully covered in [[entities/nathan-lambert]] and [[concepts/model-distillation]] (from May 4 ingest).
- The Atlantic "AI Not a Bubble": Paywalled, no usable content extracted. Reference only.

### Triage Decisions
- 6 take, 2 reference, 10 skip from 7 newsletters across 18 total candidates.

## [2026-05-05] willccbb — SFT vs RL vs On-Policy Distillation | Enriched model-distillation.md + will-brown.md timeline

- **[[concepts/model-distillation]]** — Added comprehensive "SFT vs RL vs On-Policy Distillation" section: paradigm comparison table (policy/supervision density/info-theoretic efficiency/compute cost), dense on-policy supervision insight, "dense reward per token" information-theoretic principle (O(N) bits/episode vs O(1) for RL), Will Brown's practitioner framing (post-training stack layers, environment quality dependency), industry adoption list (Qwen3, MiMo, GLM-5, Thinking Machines Lab, Nvidia Nemotron Cascade 2).
- **[[entities/will-brown]]** — Added timeline entry (May 2026: "On SFT, RL, and on-policy distillation" X article) and source reference.
- **raw/articles/2026-05-01_willccbb-sft-rl-on-policy-distillation.md** — Full article body retrieved via GetXAPI (25.8KB). Co-authored with Claude Opus 4.7 via artifact "debate" workflow. Includes 8 sections on gradient geometry, meta-algorithm, and optimal teacher framework. Claude artifact links saved.
- **[[concepts/model-distillation]]** — Expanded with Gradient Geometry section (Sparse/Dense x Biased/Unbiased x Diffuse/Concentrated axes), Meta-Algorithm (alpha/lambda knobs unifying SFT/RL/OPD/OPSD), and Optimal Teacher Pareto Lagrangian framing.
- **[[entities/will-brown]]** — Updated timeline with co-author detail (Claude Opus 4.7), added Claude Artifact sources.
- **[[social-media/x-article-getxapi-fallback]]** — New skill created for GetXAPI-based X article body retrieval fallback.
- Updated: wiki/raw/articles/2026-05-01_willccbb-sft-rl-on-policy-distillation.md, wiki/concepts/model-distillation.md, wiki/entities/will-brown.md

## 2026-05-04 X Bookmarks Ingest

**Batch**: 6 bookmarks → 3 articles scraped, 3 metadata-only (X auth wall).

### New Pages Created
- 🆕 [[entities/atal-upadhyay]] — AI/ML engineer, agent harness blogger. Author of 9-component harness framework.
- 🆕 [[entities/julien-bek]] — Sequoia Capital partner. Author of "Services: The New Software" thesis.
- 🆕 [[entities/0xjeff]] — Crypto/DeFi analyst, Hermes Agent power user. Documented Hermes as personal analyst pipeline.
- 🆕 [[entities/sequoia-capital]] — Leading VC firm. Published Service-as-Software thesis.
- 🆕 [[concepts/service-as-software]] — AI business model: sell outcomes, not tools. 6x budget expansion over SaaS.

### Pages Enriched
- ✏️ [[concepts/agent-harness]] — Added Atal Upadhyay's 9-Component Framework section with reference implementation insights.
- ✏️ [[entities/teortaxestex]] — Added Inferencemaxxing article (April 2026), coining term for inference-centric paradigm shift.
- ✏️ [[entities/yacine-mahdid]] — Added "networking guide for a hardened technical introvert" (Nov 2025, 56.6K views) to timeline.

### Raw Articles Saved
- `raw/articles/2026-03-05_sequoia-services-the-new-software.md` — Sequoia Capital, Julien Bek
- `raw/articles/2026-05-02_atalupadhyay-agent-harness.md` — Atal Upadhyay, agent harness architecture
- `raw/articles/2026-05-03_atalupadhyay-beyond-markdown-memory.md` — Atal Upadhyay, parametric vs contextual memory

### Metadata-Only (X auth wall, no mirror found)
- "What I Use Hermes Agent For (And How I Use It)" — author 109011736, 3,555 bookmarks
- "Hermes as the Ultimate Analyst" — @0xJeff, 555 bookmarks
- "Inferencemaxxing" — @teortaxesTex, 716 bookmarks
- "networking guide for a hardened technical introvert" — @yacinelearning, 3,624 bookmarks

## [2026-05-04] Interconnects Distillation Panic | New concept + enriched model-distillation + Nathan Lambert update

- **[[concepts/model-distillation]]** — Enriched from stub to comprehensive: full definition, how it works (core mechanism, 4 forms in post-training table), the 2026 "Distillation Panic" context (Anthropic's accusations, Lambert's response, policy fallout), Kevin Xu's "crutch" theory, and risks of regulatory overreach. Status: stub → active.
- **[[concepts/ai-api-abuse]]** — New concept page: malicious exploitation of AI model APIs through jailbreaking, identity spoofing, and reasoning trace extraction. Distinct from legitimate model distillation. Term coined by Nathan Lambert in "The Distillation Panic." Covers exploitation techniques table, 2026 context, policy implications (H.B. 8283, NSTM-4), and mitigation approaches.
- **[[entities/nathan-lambert]]** — Updated: added May 2026 "Distillation Panic" section with key arguments, updated frontmatter (aliases, sources, updated date), added cross-links to model-distillation, ai-api-abuse, and distillation-attacks-2026.
- **raw/articles/2026-05-04_interconnects_distillation-panic.md** — Saved raw article (Nathan Lambert, Interconnects, May 4, 2026)
- New concept: 1 (ai-api-abuse). Enriched from stub: 1 (model-distillation).
- Updated: wiki/concepts/model-distillation.md, wiki/concepts/ai-api-abuse.md, wiki/entities/nathan-lambert.md, wiki/index.md (+1 concept, 830→831), wiki/log.md

## [2026-05-04] constitutional-ai + boaz-barak | New concept page, entity enriched, raw article saved

- **[[concepts/constitutional-ai]]** — Created concept page: Anthropic's methodology for aligning AI through explicit constitutional principles. Covers: Three Poles of Alignment (Barak's Principles/Policies/Personality framework), Claude Constitution vs. OpenAI Model Spec comparison, RLAIF mechanism, anthropomorphism critique, AI-led ethics debate, relationship to synthetic data. Key source: Boaz Barak's Jan 2026 analysis.
- **[[entities/boaz-barak]]** — Enriched entity page: Added comprehensive "Claude Constitution vs. OpenAI Model Spec" section under Core Ideas. Updated blog post entry with full URL and detailed summary. Added tags (constitutional-ai, model-spec, alignment), sources (both analysis URLs), and cross-link to concepts/constitutional-ai. Updated date to 2026-05-04.
- **raw/articles/2026-01-27_boaz-barak_claude-constitution.md** — Saved raw article: Barak's full comparative analysis of Anthropic's Claude Constitution vs. OpenAI's Model Spec. Includes Three Poles framework, anthropomorphism critique, white lie examples, AI-led ethics debate, and rules-with-changelogs argument.
- Updated: wiki/concepts/constitutional-ai.md (new), wiki/entities/boaz-barak.md, wiki/index.md (+1 concept, 830→831, entity desc enriched), wiki/log.md
- Source: https://windowsontheory.org/2026/01/27/thoughts-on-claudes-constitution/

## [2026-05-04] dynamic-software | New concept page + Ashpreet Bedi article + entity update

- **[[concepts/dynamic-software]]** — Created concept page: The paradigm shift from static (deterministic, hard-coded control flow) to dynamic (model-driven, non-deterministic, agentic) software. Breaks 50-year assumptions about determinism, state/time/sessions, and observability. 80% of agents fail because teams spend 6+ months on infrastructure instead of the agent. Calls for a new 'runtime' akin to what Django/Express/Vercel did for static software. Ashpreet Bedi's "live orchestra" metaphor.
- **raw/articles/** — Saved raw article: `2026-05-02_ashpreetbedi_dynamic-software.md` (ashpreetbedi.com/dynamic-software, Apr 30, 2026)
- **[[entities/ashpreet-bedi]]** — Updated: Added Dynamic Software article to timeline and Key Quotes. Expanded Overview to reflect his dynamic software thesis and its relationship to the Five Levels of Agentic Software framework.
- Updated: wiki/concepts/dynamic-software.md, wiki/index.md (+1 concept, 829→830), wiki/entities/ashpreet-bedi.md, wiki/log.md

## [2026-05-04] gm8xx8 | Enriched skeleton entity page (daily cron job)
- **[[entities/gm8xx8]]** — Enriched from X/Twitter profile data, HuggingFace, and live tweet scraping:
  - Updated HF follower count: 77K+ → **89,826**
  - Added X follower count: **8,785**
  - Added X post count: **17,100+**
  - Added bio and pinned tweet as direct quotes
  - Added account creation date (March 2010 — not August 2022 as previously assumed)
  - Added 6 Notable Tweets with engagement metrics (highest: 2,400 likes, 191K views)
  - Expanded Curation Style section: all-caps enthusiasm, metric-first framing, model release coverage, open models bias
  - Replaced self-referential "See Also" with cross-links to related entities
  - Removed "skeleton" status note
  - Added proper frontmatter: aliases, sources, extended tags
  - Updated: wiki/entities/gm8xx8.md, wiki/entities/_index.md, wiki/index.md (entity desc + removed stale concept link)
- Raw sources consulted: x.com/gm8xx8, huggingface.co/gm8xx8, github.com/gm8xx8

## [2026-05-04] ai-index-report-2026 | Enriched with detailed chapter data from Stanford HAI chapter pages
- **[[concepts/ai-index-report-2026]]** — Substantially enriched from initial digest-based entry:
  - Added **3 new Top Takeaways**: "Big Four" convergence & benchmark reliability crisis (#3), AI Sovereignty & Policy Governance (#10), expanded expert vs public divide (#11)
  - **Technical Performance**: Arena Elo ratings (Anthropic 1,503), benchmark invalidity rates (GSM8K 42%), agent OSWorld 66.3%, video generation (Veo 3), professional domains 60-90%, AV deployment data
  - **Responsible AI**: Hallucination detection rates (22-94%), knowledge vs belief confusion, ISO 42001/NIST RMF adoption, Foundation Model Transparency Index drop (58 to 40), jailbreak vulnerability data, language gap data
  - **Economy**: Investment +127.5%, GenAI +200%+, Google CAPEX $150B+, consumer surplus $172B, labor market (young devs -20%), productivity gains (14-50%), industrial robots (China 54%)
  - **Policy & Governance**: AI sovereignty clusters (Europe 3 to 44), data localization measures, congressional witness data (5 to 102), public vs private investment disparity
  - Updated Chapter Structure table from 7 to 9 chapters (split Science & Medicine, added Public Opinion)
  - Added 6 new raw articles from Stanford HAI chapter pages, news article, and Hyperight summary
  - Added sources, enriched See Also (4 new cross-links)
  - Tags expanded with regulation, economy, responsible-ai, ai-sovereignty
- Updated: wiki/concepts/ai-index-report-2026.md, wiki/index.md, wiki/log.md

## [2026-05-04] llm-evaluation-harness + open-llm-leaderboard | Enriched from paper, slides, GitHub, and HF sources
- **[[concepts/llm-evaluation-harness]]** — Completely rewritten: 3 primitive request types (loglikelihood/perplexity/generation), multi-choice normalization methods, supported backends (8), best practices from the "Lessons from the Trenches" paper, prompting sensitivity case study (Mistral-7B +4.4pp between styles). Raw sources: paper, Hailey Schoelkopf slides, GitHub README.
- **[[concepts/open-llm-leaderboard]]** — Expanded from stub: team (Thomas Wolf, clefourrier, Nathan Habib), key resources (main leaderboard, results dataset, comparator, generation visualizer), v1/v2 versions, relationship to lm-eval.
- **[[entities/eleutherai]]** — New entity page: grassroots research collective turned non-profit. Projects: GPT-Neo, Pythia, BLOOM, Llemma, lm-eval, The Pile.
- **[[entities/hailey-schoelkopf]]** — New entity page: lm-eval maintainer, Pythia co-author (ICML 2023), Research Scientist at EleutherAI.
- **[[entities/stella-biderman]]** — New entity page: Executive Director of EleutherAI, led GPT-Neo, Pythia, BLOOM, The Pile.
- Raw articles saved: raw/papers/2024-05-23_2405.14782_lessons-from-the-trenches.md, raw/articles/2024-06-11_hailey-schoelkopf-lm-evaluation-deep-dive.md
- New entities: 3 (eleutherai, hailey-schoelkopf, stella-biderman), Updated concepts: 2 (llm-evaluation-harness, open-llm-leaderboard)
- Updated: wiki/index.md (+3 entities, +3 pages to count), wiki/log.md

## [2026-05-04] ai-patterns-for-glam | New concept page: AI Design Patterns for Information Professionals
- **[[concepts/ai-patterns-for-glam|AI Design Patterns for Information Professionals (Boring AI)]]** — Created new concept page covering Daniel van Strien's WIP book on practical "boring AI" design patterns for GLAM and information professionals. Core philosophy: most impactful AI for information work is deliberately mundane (structured extraction, classification, metadata enrichment). Four-stage framework: Discovery → Design Patterns → Evaluation → Infrastructure. Pattern language approach inspired by Christopher Alexander (1977).
- **[[entities/daniel-van-strien]]** — Updated: added book to Known for, Blog Posts table, and GLAM Sector section. Added sources and bumped updated date.
- Raw articles saved: raw/articles/2026-03-23_ai-patterns-for-glam-welcome.md
- New concept: concepts/ai-patterns-for-glam.md
- Updated: entities/daniel-van-strien.md, wiki/index.md (Concept +1 → 425), wiki/log.md

## [2026-05-04] synthetic-data + dataset-engineering | Enriched concept pages from two articles
- **[[concepts/synthetic-data]]** — Enriched with CAI framework (Constitutional AI / RLAIF), synthetic data hierarchy (instructions → preferences → critiques), practical tips (best model, lock API versions), open-source examples (OpenHermes, Orca, Starling, Evol-Instruct, SteerLM, Prometheus), and OpenAI Superalignment connection.
- **[[concepts/dataset-engineering]]** — Created new concept page covering the shift from data science to dataset engineering, Data-Centric AI (Andrew Ng), democratization of AI training, tooling ecosystem (argilla, CVAT, FiftyOne, distilabel), and relationship to synthetic data.
- Raw articles saved: 2023-11-29_interconnects-llm-synthetic-data.md (Nathan Lambert), 2025-01-16_pelayoarbues-dataset-engineer.md (Pelayo Arbués)

## [2026-05-04] ssm-mamba + genai-handbook-resources | SSM/Mamba concept page, entity pages for key educators, resource enrichment
- **[[concepts/ssm-mamba]]** — Created comprehensive concept page for SSM/Mamba evolution (S4 2021 → Mamba 2023 → Mamba-2/SSD 2024 → Mamba-3 ICLR 2026 Oral). Core mechanism (SSM equations, discretization, HiPPO, selective scan S6), comparison with Transformers, hybrid model trends, full resource evaluation with 🟢🟡 ratings.
- **GenAI Handbook Resource Ingestion:** Created 4 entity pages for 🟢 top-tier resource creators:
  - [[entities/grant-sanderson-3blue1brown]] — 3Blue1Brown (math/ML visualization)
  - [[entities/neel-nanda]] — MI researcher (Glossary, Quickstart Guide)
  - [[entities/jay-alammar]] — Visual ML explainer (Illustrated Transformer/Word2Vec)
  - [[entities/sebastian-raschka]] — LoRA finetuning expert (Ahead of AI)
- Enriched existing entities with handbook cross-links: [[entities/lilian-weng]], [[entities/chip-huyen]], [[entities/tim-dettmers]], [[entities/maarten-grootendorst]]
- Raw articles saved: tim-dettmers-llm-int8 (quantization), maarten-grootendorst-mamba-guide
- New pages: concepts/ssm-mamba.md, entities/grant-sanderson-3blue1brown.md, entities/neel-nanda.md, entities/jay-alammar.md, entities/sebastian-raschka.md
- Raw articles: raw/articles/2022-08-17_tim-dettmers-llm-int8-quantization.md, raw/articles/2024_maarten-grootendorst-visual-guide-mamba.md
- Updated: entities/will-brown.md (cross-link), wiki/index.md (Concept +1 → 423, Entity +4, Total +5 → 825), wiki/log.md

## [2026-05-04] llm-patterns-eugene-yan | Enriched with OOD finetuning for hallucination detection (Yan)
- **[[concepts/llm-patterns-eugene-yan]]** — Added NLI-based Hallucination Detection subsection under Evals: OOD bootstrapping method (USB Wikipedia -> FIB News), 25x recall improvement (0.02->0.50), BART+MNLI approach, QLoRA usage.
- Raw article: raw/articles/2023-11-05_eugeneyan-finetuning-hallucination-detection.md
- Updated: entities/eugene-yan.md (Sources +finetuning article)
- Updated: wiki/log.md

## [2026-05-04] llm-patterns-eugene-yan | Enriched with OReilly Applied LLMs Guide (3 parts, 6 co-authors)
- **[[concepts/llm-patterns-eugene-yan]]** — Enriched existing concept page with comprehensive OReilly What We Learned from a Year of Building with LLMs guide. Added: Part I (Tactical: Prompting, RAG, Flow Engineering, Evals), Part II (Operations: Data, Models, Product, Team), Part III (Strategy: Resource Allocation, System Moat, Human-Centered AI, Economics). Updated evolution table with v2 details. Added co-author cross-links.
|- Raw articles: raw/articles/2024-05-28_oreilly-applied-llms-part1.md, 2024-05-31_oreilly-applied-llms-part2.md, 2024-06-06_oreilly-applied-llms-part3.md
- Updated entities: bryan-bischof.md (Related Concepts + restored Related People), jason-liu.md (Related Concepts), shreya-shankar.md (Related Concepts)
- Updated: wiki/index.md (entry enriched), wiki/log.md
## [2026-05-04] genai-handbook | New meta-knowledge concept page (William Brown GenAI Handbook)
- **[[concepts/genai-handbook]]** — Created comprehensive meta-knowledge concept page for William Brown (@willccbb) GenAI Handbook v0.1 (June 2024). 9-section roadmap mapping against existing wiki concepts with coverage ratings (~5-85% per section), linked resource evaluation and quality assessment, gap analysis (6 topics, 3 priorities), and learner-type recommendations (Engineer / Researcher / Beginner).
- リソース評価の主な判定: Karpathy「Let's build GPT」· Lilian Wengエージェント記事· 3Blue1Brownシリーズ· Tim Dettmers量子化ブログ → 🟢 現在も価値不変。GANs関連· Goodfellow DL本 → ⚪ 歴史的価値のみ。
- 主要ギャップ: 🔴 SSM/Mamba, Representation Engineering, 🟡 Model Merging, Context Scaling
- New page: concepts/genai-handbook.md
- Raw article: raw/articles/2026-05-04_genai-handbook.md
- Updated: entities/will-brown.md (cross-link to concept page), wiki/index.md (Concept +1 → 422, Total +1 → 820), wiki/log.md

## [2026-05-04] llm-patterns-eugene-yan | New concept page (Eugene Yan LLM Patterns framework)
- **[[concepts/llm-patterns-eugene-yan]]** — Created comprehensive concept page for Eugene Yan 7-pattern framework for building LLM-based systems and products. Covers: Evals, RAG, Fine-tuning, Caching, Guardrails, Defensive UX, User Feedback. Includes v1 to v2 evolution (vs O Reilly co-authored version). Maps each pattern to existing wiki concept pages with wikilinks.
- New page: concepts/llm-patterns-eugene-yan.md
|- Raw article: raw/articles/2023-07-30_eugeneyan-llm-patterns.md
- Updated: entities/eugene-yan.md (Related Concepts), entities/eugeneyan.md (Seven Patterns section + link), entities/eugene-yan--core-ideas.md (cross-link)
- Updated: wiki/index.md (Concept +1), wiki/log.md
## [2026-05-04] Top 3 courses — full curriculum pages (CS336, COS597R, CMU LLMs)
- **[[concepts/stanford-cs336-language-modeling-from-scratch|Stanford CS336]]** — Created full curriculum concept page. 5 assignments mapped to wiki concepts (Transformer→Triton→Scaling→Common Crawl→Alignment). Key finding: Tied to `flashattention-pytorch-educational`, `grpo-rl-training`, `decoder-only-gpt`. Includes GPU cost guide ($1.99-3.29/h H100).
- **[[concepts/princeton-cos597r-deep-dive-llm|Princeton COS597R]]** — Created full curriculum concept page. 14-week paper schedule with wiki mapping. Key finding: Debate Panel format + Scribe system unique. Covers scaling laws, DPO, Constitutional AI, test-time compute scaling, FlashAttention.
- **[[concepts/cmu-llms-methods-applications|CMU LLMs]]** — Created full curriculum concept page. 4 phases (Foundations→RAG/Agents→Safety/Code→Deployment). Key finding: 2026版で最も新しい、RAGを3週連続で扱う唯一のコース。
- New pages: concepts/stanford-cs336-language-modeling-from-scratch.md, concepts/princeton-cos597r-deep-dive-llm.md, concepts/cmu-llms-methods-applications.md
- Raw articles: raw/articles/2026-05-04_stanford-cs336-syllabus.md, princeton-cos597r-syllabus.md, cmu-llms-syllabus.md
- Updated: wiki/index.md (Concept +3), wiki/log.md

## [2026-05-04] learning-llms-in-2025 | New concept page (Yoav Goldberg's curriculum guide)
- **[[concepts/learning-llms-in-2025|Learning LLMs in 2025]]** — Created meta-knowledge concept page for Yoav Goldberg's curated LLM curriculum guide. Evaluates 15 academic resources on quality, accessibility, and relevance with learner-type-specific recommendations.
  - Courses: Chiang (TONN), CMU LLMs, Princeton Deep Dive, Stanford Human-Centered, Berkeley Safety, JHU Self-supervised, Stanford CS336 (Language Models from Scratch), UW NLP LLM, NYU NLU
  - Seminars: Robin Jia Science of LLMs, Danqi Chen 2022, Michael Hahn Alignment, Tal Linzen Cognitive
  - Videos: Stanford CS25
  - Key findings: CS336 = best for implementation-focused learners, Princeton Deep Dive = best for research-focused, CMU LLMs = best all-around entry point
  - Accessibility warnings: Neubig ANLP schedule page empty, both Tal Linzen resources behind Google Docs access walls
  - New page: concepts/learning-llms-in-2025.md
  - New entity: [[entities/yoav-goldberg]]
  - Updated: wiki/index.md (Entity +1, Concept +1), wiki/log.md

## [2026-05-04] Optimum quantization guide — accumulation types, energy efficiency, granularity

- **[[concepts/model-quantization]]** — Expanded with 3 new sections from HF Optimum docs:
  - Section 2: Accumulation Data Types (float16->float16, bfloat16->float32, int8->int32 etc.) and Granularity (per-tensor vs per-channel vs vector-wise) added after calibration
  - Section 11: Energy Efficiency and Practical Workflow — counterintuitive findings (NF4 on <3B models: +25-56% energy; batching 1->64: -96% energy), 6-step Optimum implementation pipeline
  - Sources updated with Optimum concept guide
- **raw/articles/2026-05-04_optimum-quantization-concept-guide.md** — Saved raw article
- Updated: wiki/log.md
- Source: https://huggingface.co/docs/optimum/concept_guides/quantization

## [2026-05-04] bitsandbytes — concept page + linear4bit API docs ingestion

- **[[concepts/bitsandbytes]]** — Created concept page (L2): 4-bit/8-bit quantization library (Tim Dettmers / bitsandbytes-foundation). Covers: Linear4bit architecture (LinearFP4, LinearNF4, Params4bit), NF4 equal-area bins under N(0,1) with α=929/960, double quantization (0.4 bits/param savings), BitsAndBytesConfig integration with HF Transformers, ecosystem position (training vs GPTQ/AWQ inference), T4 benchmarks, CUDA-only constraint. Sources: Linear4bit API docs, HF blog, QLoRA paper, John D. Cook analysis.
- **[[concepts/model-quantization]]** — Updated: Added [[concepts/bitsandbytes]] to Related Pages.
- **raw/articles/2026-05-04_bitsandbytes-linear4bit-hf-docs.md** — Saved raw article
- Updated: wiki/index.md (+1 concept, 812→813), wiki/log.md
- Sources: https://huggingface.co/docs/bitsandbytes/en/reference/nn/linear4bit, https://huggingface.co/blog/4bit-transformers-bitsandbytes

## [2026-05-04] Quantization deep-dive — LLM.int8(), emergent features, visual guide, 1.58-bit frontier

- **[[concepts/model-quantization]]** — Major expansion (L1 → comprehensive): Added IEEE-754 representation fundamentals (sign/exponent/fraction), symmetric (Absmax) vs asymmetric (Zero-point) quantization mapping, LLM.int8() with mixed precision decomposition, 6.7B parameter phase shift (Dettmers), Two Streams Theory, calibration deep-dive (MSE/KL/Percentile), expanded PTQ section (GPTQ Hessian-based error redistribution, GGUF block-wise), QAT wide minima theory, BitNet (1-bit, signum) and BitNet b1.58 (ternary, absmean, addition-only matmul) frontier section. Sources and TODO updated.
- **[[entities/tim-dettmers]]** — Created entity page: University of Washington researcher. Creator of bitsandbytes, LLM.int8() (zero-degradation 8-bit inference for 175B+ models), QLoRA co-creator (with Artidoro Pagnoni). Discovered emergent outlier features and 6.7B phase shift. NF4 data type, double quantization.
- **[[entities/maarten-grootendorst]]** — Created entity page: Data scientist, AI educator. Author of 'Visual Guide to Quantization' covering IEEE-754, PTQ vs QAT, BitNet. Creator of BERTopic, PolyFuzz.
- **[[concepts/fine-tuning/quantization-overview]]** — Updated: Added sources (Dettmers, Grootendorst) and cross-references to [[concepts/model-quantization]] and [[entities/tim-dettmers]].
- **raw/articles/2022-08-17_tim-dettmers-llm-int8-quantization.md** — Saved raw article (dedup: removed simpler variant _llm-int8-emergent-features.md)
- **raw/articles/2024-07-22_maarten-grootendorst_visual-guide-quantization.md** — Saved raw article (corrected date: 2024-07-22, not 2024-09-23)
- Updated: wiki/index.md (+2 entities, 810→812), wiki/log.md
- Sources: https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/, https://www.maartengrootendorst.com/blog/quantization/

## [2026-05-04] Justine Tunney CPU matmul — LLM on CPU optimization + CPU offloading connection

- **[[entities/justine-tunney]]** — Created entity page: Software engineer, llamafile creator. 84 CPU matmul kernels (30-500% faster), Cosmopolitan Libc. Mozilla/Google alum.
- **[[concepts/inference/llama-cpp]]** — Enriched: Added CPU Performance Optimization section (outer-loop unrolling, custom threading model, hardware-specific benchmarks). Added [[entities/justine-tunney]] reference.
- **[[concepts/fsdp-qlora]]** — Enriched: Added CPU Performance & Offloading Viability section connecting faster CPU matmul to reduced offloading penalty in FSDP/DeepSpeed training.
- **raw/articles/2024-06_justine-tunney-llama-cpu-matmul.md** — Saved raw article
- Updated: wiki/index.md (+1 entity, 810 pages), wiki/log.md
- Source: https://justine.lol/matmul/

## [2026-05-04] The Hardware Lottery — Concept page + Sara Hooker entity

- **[[concepts/ai-infrastructure-engineering/hardware-lottery]]** — Created concept page (🟢 L2): Sara Hooker's **Hardware Lottery** framework — meta-framework explaining why AI research ideas succeed based on hardware/software compatibility, not algorithmic merit. Covers Anna Karenina principle, neural networks' lost decades (CPU vs GPU), TPU lock-in, domain specialization trap, and strategic implications for AI infrastructure engineers (GPU procurement, cloud provider choice, interconnect strategy).
- **[[entities/sara-hooker]]** — Created entity page: Google DeepMind researcher, author of The Hardware Lottery (CACM 2021). Advocate for cross-disciplinary hardware/software/ML collaboration.
- **raw/papers/2020-09-14_2009-06489_hardware-lottery.md** — Saved raw paper with abstract, core contributions, key data points
- **[[concepts/ai-infrastructure-engineering/_index]]** — Enriched: Added "Research Frameworks" row to scope table with hardware-lottery link
- Updated: wiki/index.md (+2 pages, +1 entity, 810 total), wiki/log.md
- Source: arXiv:2009.06489 / Communications of the ACM, Vol. 64, Issue 12 (2021)

## [2026-05-04] LLM Course Roadmap — Meta-knowledge map

- **[[concepts/llm-course-roadmap]]** — Created concept page: Maxime Labonne's LLM Course (78.9k ⭐) structured as a knowledge map. Maps all three parts (Fundamentals → Scientist → Engineer) against existing Wiki concepts with coverage ratings and gap analysis. LLM領域の体系的な知識マップ。
- **[[entities/maxime-labonne]]** — Created entity page: Head of Post-Training @ Liquid AI, creator of LLM Course, abliteration technique, quantization educator, author of two Packt books. Career: Airbus → JPMorgan → Liquid AI.
- Updated: wiki/index.md, wiki/log.md
- Sources: https://github.com/mlabonne/llm-course, https://mlabonne.github.io/blog/

## [2026-05-04] TGI Multi-LoRA — Inference serving concept page

- **[[concepts/inference/tgi]]** — Created concept page: Hugging Face TGI (Text Generation Inference) with native Multi-LoRA serving. 30+ adapters per base model, ~3% VRAM overhead, dynamic adapter_id routing, Punica/LoRAX kernels. Comparison with vLLM/SGLang. Economics: ~$8/adapter training, flat cost scaling.
- **[[concepts/inference/_index]]** — Enriched: Added TGI row to engine comparison table, updated recommendation table (Multi-LoRA -> TGI, not vLLM).
- **raw/articles/2024-07-18_tgi-multi-lora-serving.md** — Saved raw article
- Updated: wiki/index.md (inference/tgi entry), wiki/log.md
- Source: https://huggingface.co/blog/multi-lora-serving

## [2026-05-04] Accelerate — Distributed training launcher + DeepSpeed concept page

- **[[concepts/accelerate]]** — Created concept page: Hugging Face Accelerate as unified distributed training abstraction. FSDP vs DeepSpeed configuration mapping (6 dimensions), memory/precision differences (fp32 upcast), plugin system (FullyShardedDataParallelPlugin, DeepSpeedPlugin), decision guide. Lead developer attribution added: [[entities/zach-mueller]].
- **[[concepts/deepspeed]]** — Created concept page: Microsoft DeepSpeed (ZeRO 1/2/3/3-offload/Infinity, 3D-Parallelism, MoE, NVMe offload). Notable models (BLOOM, MT-530B, GPT-NeoX). Accelerate integration mapping. Fills existing wikilink from pytorch-fsdp.
- **[[concepts/pytorch-fsdp]]** — Enriched: Added Accelerate cross-reference to Related Concepts.
- **[[entities/zach-mueller]]** — Enriched: Added Cross-References section (accelerate, pytorch-fsdp, deepspeed), updated sources with Accelerate guide, bumped update date. Linked from [[concepts/accelerate]] as lead developer.
- **raw/articles/2026-05-04_accelerate-fsdp-deepspeed-guide.md** — Saved raw article
- Updated: wiki/index.md (zach-mueller→the-zach-mueller, accelerate description), wiki/log.md
- Sources: muellerzr.github.io, hf.co/docs/accelerate

## [2026-05-04] Mobius Labs entity page — Dropbox acquisition, HQQ, Aana, low-bit inference

- **[[entities/mobius-labs]]** — Created entity page: AI research company (HQQ quantization, GemLite Triton kernels, Aana multimodal SDK). Acquired by Dropbox ~2025, powers Dash multimodal search. Covers FSDP/QLoRA collaboration (Answer.AI, Tim Dettmers), FP4 quality recovery, metadata offloading, low-bit inference survey. 3 raw articles ingested.
- **raw/articles/2025_mobius-labs-blog-summary.md** — Saved raw article
- **raw/articles/2025-05-04_dropbox-mobius-labs-aana-integration.md** — Saved raw article
- **raw/articles/2026-05-04_dropbox-low-bit-inference.md** — Saved raw article
- Updated: wiki/index.md (+1 entity, 806 pages), wiki/log.md
- Sources: blog.mobiuslabs.com, dropbox.tech

## [2026-05-04] vLLM spec-decode blog — Speculative decoding wiki enrichment

- **[[concepts/speculative-decoding]]** — Enriched: Added vLLM Implementation section (3 supported methods: Draft Model, Prompt Lookup/N-gram, Medusa/Eagle/MLPSpeculator), code examples, critical QPS sensitivity insight (2.8x speedup at low QPS, 1.4-1.8x slowdown at high QPS), Dynamic Speculative Decoding roadmap. Sources updated.
- **[[concepts/inference/vllm]]** — Enriched: Added Speculative Decoding in vLLM section with methods table and configuration examples, linking to full concept page.
- **raw/articles/2025-10-09_vllm-speculative-decoding-blog.md** — Saved raw article
- Updated: wiki/log.md
- Source: https://vllm.ai/blog/spec-decode

## [2026-05-04] Answer.AI benchmarks — FSDP+Q-LoRA performance enrichment

- **[[concepts/fsdp-qlora]]** — Enriched: Added Answer.AI official benchmarks table (Llama-2 70B, 5 hardware tiers, $2-5 cost range), hardware bottleneck analysis (PCIe/NVLink, CPU RAM saturation), progressive optimization guide (6-step DDP→Activation Offload), DDP vs FSDP decision rule.
- **[[concepts/pytorch-fsdp]]** — Enriched: Added DDP vs FSDP decision guidance, progressive optimization strategy table (6 memory-saving steps), sources updated with Answer.AI benchmarks.
- **[[concepts/qlora]]** — Enriched: Added speed advantage insight (QLoRA can be faster than LoRA via larger batch sizes), CPU offloading performance paradox.
- **raw/articles/2024-03_answerai-fsdp-qlora-benchmarks.md** — Saved raw article
- Updated: wiki/log.md
- Source: https://github.com/AnswerDotAI/fsdp_qlora/blob/main/benchmarks_03_2024.md

## [2026-05-04] Phil Schmid FSDP+Q-LoRA guide — Full wiki ingest (4 pages)

- **[[entities/phil-schmid]]** — Created entity page: Philipp (Phil) Schmid, Staff Engineer (AI DevX/DevRel) at Google DeepMind, ex-Hugging Face Technical Lead. Key contributions: FSDP+Q-LoRA, Inference Endpoints, Zephyr/SmolLM/StarCoder partnerships, revenue $0→$100M.
- **[[concepts/pytorch-fsdp]]** — Created top-level concept page: PyTorch FSDP (Fully Sharded Data Parallel) with ZeRO-3 sharding, CPU offloading, memory tradeoffs for Llama 3 70B, HF ecosystem integration, DeepSpeed comparison. Existing fine-tuning/pytorch-fsdp.md updated to redirect.
- **[[concepts/qlora]]** — Created concept page: Q-LoRA (Quantized Low-Rank Adaptation). Covers NF4, Double Quantization, Paged Optimizers, architecture diagram, memory comparison (70B ~36GB VRAM).
- **[[concepts/fsdp-qlora]]** — Created concept page: FSDP+Q-LoRA combined training technique (Answer.AI × Tim Dettmers × HF). Memory scaling table, cost analysis ($255 for 70B 3-epoch on 4× A10G), implementation config, comparison with alternatives.
- **raw/articles/2026-05-04_phil-schmid-fsdp-qlora-llama3.md** — Saved raw article
- Updated: wiki/index.md (+4 pages, 801→805), wiki/log.md
- Source: https://www.philschmid.de/fsdp-qlora-llama3

## [2026-05-04] Jay Mody blog — Full wiki ingest (5 articles)

- **[[entities/jay-mody]]** — Created entity page: Educator known for picoGPT (GPT-2 in 60 lines of NumPy), speculative sampling tutorial, and clear LLM internals explanations. 5 articles ingested.
- **[[concepts/speculative-decoding]]** — Enriched: added Gentle Introduction section with Jay Mody's tutorial (2.23x speedup), aliases, cross-reference to jay-mody entity. Added raw/article source.
- **[[concepts/attention-mechanism-variants]]** — Enriched: added Educational Derivations section with Jay Mody's first-principles derivation of scaled dot-product attention. Added alias `scaled-dot-product-attention`.
- **raw/articles/2023-02-08_jaymody-speculative-sampling.md** — Saved raw article
- **raw/articles/2023-01-30_jaymody-picoGPT.md** — Saved raw article
- **raw/articles/2022-12-15_jaymody-stable-softmax.md** — Saved raw article
- **raw/articles/2022-10-22_jaymody-attention-intuition.md** — Saved raw article
- **raw/articles/2021-04-04_jaymody-distance-matrices.md** — Saved raw article
- Updated: wiki/index.md (entity entry), wiki/log.md
- Source: https://jaykmody.com/

## [2026-05-04] Thorsten Ball Joy & Curiosity #84 — Newsletter ingest

- **[[entities/mitchell-hashimoto]]** — Created entity page: HashiCorp co-founder, Ghostty creator. Index entry enriched from stub to full (left GitHub 2026 over AI agent instability).
- **[[entities/thorsten-ball]]** — Created entity page: Author of Writing An Interpreter/Compiler In Go, Register Spill newsletter, Sourcegraph engineer.
- **[[entities/zed]]** — Created entity page: High-performance Rust editor by former Atom team. Reached 1.0 (Apr 29, 2026). AI-native with parallel agent orchestration.
- **[[entities/mistral-ai]]** — Created entity page: French AI company, €12B valuation, $400M+ ARR, "smaller, cheaper, not American" strategy.
- **raw/articles/2026-05-04_thorsten-ball-joy-and-curiosity-84.md** — Saved raw article
- Updated: wiki/index.md (801 pages, 389 entities), wiki/log.md
- Source: [Joy & Curiosity #84 - Register Spill](https://registerspill.thorstenball.com/p/joy-and-curiosity-84)

## [2026-05-04] Modelcrafting — Letting AI Posttrain AI

- **[[concepts/modelcrafting]]** — Created concept page: paradigm of AI agents autonomously shaping and improving other AI models. Covers research intuition gap, 6 failure modes (naive SFT, no sanity checks, no curriculum learning, eval contamination, commitment bias, spend inefficiency), tokenizer workaround case study.
- **[[entities/thoughtful-lab]]** — Created entity page: AI research lab behind the "Letting AI Posttrain AI" experiment (Apr 2026). Tested Claude 4.6 Opus and GPT-5.4 on autonomous post-training of Qwen3-8B for the Frog Placement Game.
- **[[concepts/post-training]]** — Enriched from stub to full page: added overview, key techniques table, automated post-training research section (Thoughtful Lab experiment), known challenges section, and cross-references.
- **raw/articles/2026-04_thoughtfullab-letting-ai-posttrain-ai.md** — Saved raw article
- Updated: wiki/index.md (800 total pages), wiki/entities/_index.md, wiki/log.md
- Source: [Letting AI Posttrain AI - Thoughtful Lab](https://www.thoughtfullab.com/letting-ai-posttrain-ai.html)

## [2026-05-04] MGH Validation: LongCoT Experiment — Zhang's RLM LongCoT article ingested

- **[[concepts/mismanaged-geniuses-hypothesis]]** — Added "Empirical Validation: LongCoT Experiment" section: GPT-5.2 + RLM + Claude Code trajectory tips = 65.6% on LongCoT-mini (baseline 38.7%). Three failure modes identified (brute-force, verification gaps, prompting gaps). Ablation proves RLM mechanism is essential.
- **[[concepts/rlm-recursive-language-models]]** — Added "MGH Validation: Zhang's Direct LongCoT RLM Experiment" section with results table (65.6% total, >70% with partial rewards) and identified failure modes.
- **[[entities/alex-zhang]]** — Added Apr 2026 LongCoT blog post to Blog Posts table; added "Proof (prompt-level steering)" bullet to MGH section.
- **[[entities/omar-khattab/rlm]]** — Added LongCoT-mini result (65.6%) to benchmark list.
- **raw/articles/2026-04-26_alex-zhang-longcot-rlm-mgh.md** — Saved raw article: Alex Zhang's direct application of MGH to LongCoT via RLM + Claude Code trajectory analysis.
- Source: https://alexzhang13.github.io/blog/2026/longcot-rlm/

## [2026-05-04] Multi-Teacher On-Policy Distillation (MOPD) — New concept from Notion article

- **[[concepts/multi-teacher-on-policy-distillation]]** — Created concept page: MOPD is a post-training primitive that solves the see-saw problem via reverse KL distillation from multiple teachers within a GRPO-like loop. Covers IcePop, full-vocabulary distillation, WAL-based fault-tolerant rollouts, and comparisons across MiMo-V2-Flash, GLM-5, Nemotron-Cascade 2, and DeepSeek-V4.
- **[[concepts/model-distillation]]** — Updated Related Pages with cross-link to MOPD
- **[[concepts/grpo-rl-training]]** — Updated Related Pages with cross-link to MOPD
- **raw/articles/2026-05-04_multi-teacher-on-policy-distillation.md** — Saved raw article
- Updated: wiki/index.md (799 total pages, concepts: 415), wiki/log.md
- Source: Notion (yumoxu)

## [2026-05-04] Paper Ingest — RPG (Regularized Policy Gradient) for KL-Regularized PG Framework

- **[[concepts/rpg-regularized-policy-gradient]]** — Created concept page: RPG framework unifies KL-regularized policy gradient algorithms for LLM reasoning (Zhang et al., ICLR 2026). Identifies GRPO importance-weighting mismatch and proposes RPG-REINFORCE with RPG-Style Clip. AIME24/25: **+6pp over DAPO**. AIME25 (8K): 52% — surpasses Qwen3-4B-Instruct (47%).
- **[[concepts/fine-tuning/grpo-rl-training]]** — Updated See Also section with cross-link to RPG page noting the KL mismatch correction.
- **raw/papers/2025-05-19_2505.17508_kl-regularized-policy-gradient-rpg.md** — Raw paper saved.
- **Source:** arXiv:2505.17508, ICLR 2026
- Updated: wiki/index.md (+1 concept), wiki/log.md

## [2026-05-04] Active Crawl — Pentagon AI Deals, Agentic AI Governance, MIT-IBM Computing Lab

- **[[entities/anthropic]]** — Added Pentagon Blacklisting section: supply chain risk designation (Feb 2026), Mythos exception, $900B valuation target, lawsuits, May 2026 exclusion from 7-company deals.
- **[[concepts/ai-military]]** — Expanded with Pentagon AI Deals section: 7 companies (SpaceX, OpenAI, Google, Nvidia, Microsoft, AWS, Reflection) signed for classified IL6/IL7 military AI work, "any lawful use" clause, Anthropic excluded.
- **[[entities/reflection-ai]]** — Created entity page: 2-year-old startup (former DeepMind researchers), seeking $25B valuation, backed by Nvidia and 1789 Capital. Pentagon defense partner. No public model yet.
- **[[concepts/agentic-ai-governance]]** — Created concept page: Yale CELI framework (May 2026), three-tiered guardrails, HITL/HOTL patterns, ISO/IEC 42001, excessive agency risk, indirect prompt injection.
- **[[entities/mit-ibm-computing-research-lab]]** — Created entity page: IBM+MIT joint lab (Apr 2026), AI + algorithms + quantum computing convergence, 2029 fault-tolerant quantum roadmap, 3 research pillars.
- **raw/articles/** — 3 new raw articles saved: pentagon-seven-ai-deals-anthropic-excluded, yale-celi-agentic-ai-governance-framework, mit-ibm-computing-research-lab-launch
- Updated: wiki/index.md (798 total pages, +3 new entries), wiki/log.md
- Sources: The Guardian, CNBC, Reuters, IBM Newsroom, MIT News, Fortune/EWSolutions

## [2026-05-04] Newsletter Ingest — The Signal: Anthropic Creative Coalition, Claude Security, OpenAI AWS Bedrock, Google Gemini updates

- Source: The Signal newsletter "Gemini Gets to Work, Claude's Big Pull, and OpenAI Unchained" (2026-05-03)
- **[[entities/anthropic]]** — Added Creative Coalition (9 connectors: Adobe CC, Blender, Autodesk Fusion, Ableton, etc.), Claude Security public beta (Opus 4.7, vulnerability scanning with 271 Firefox zero-days), Market Position (40% enterprise LLM spend, $30B ARR, Oct 2026 IPO)
- **[[entities/openai]]** — Added AWS Bedrock integration (GPT-5.5, Codex, Managed Agents on Bedrock, limited preview), Economics comparison table ($25B ARR, IPO delayed to 2027, compute commitments walked back to $600B)
- **[[entities/claude-mythos]]** — Updated Firefox zero-day data: 271 vulnerabilities discovered in single sweep (~4× Mozilla 2025 total)
- **[[entities/google]]** — Updated with Gemini file generation (Docs/Sheets/Slides/PDF), AI compute dominance stats (25% of global AI compute, 3.8M TPUs + 1.3M GPUs), 7-9 month model velocity gap estimate
- raw/articles/ — 3 new raw articles saved: anthropic-claude-creative-coalition, anthropic-claude-security-public-beta, openai-aws-bedrock-partnership

## [2026-05-04] Blog Ingest — 18 articles collected, 3 entity pages created/updated, anti-sycophancy concept enriched

- **[[concepts/anti-sycophancy]]** — Enriched with Anthropic's May 2026 sycophancy metrics: 9% overall, but 38% in spirituality conversations and 25% in relationships. Shows domain-specific vulnerability in RLHF-trained models. Source: [Simon Willison on Anthropic's research summary](https://simonwillison.net/2026/May/3/anthropic/).
- **[[entities/gary-marcus]]** — Updated with May 2026 healthcare thesis: "Have LLMs improved patient outcomes?" — aligned with Eric Topol and Nature Medicine editorial finding no evidence of patient outcome improvement beyond admin tasks. Source: [garymarcus.substack.com](https://garymarcus.substack.com/p/have-llms-improved-patient-outcomes).
- **[[entities/george-hotz]]** — Updated with May 2026 "Punk, or why I don't stream anymore" essay: critique of AI-mediated culture, wireheading, and the "information war" on inner reality. Source: [geohot.github.io](https://geohot.github.io//blog/jekyll/update/2026/05/03/punk-or-why-i-dont-stream.html).
- **[[entities/martin-alderson]]** — Enriched with "29th August 2026: a scenario" — fictional narrative illustrating CopyFail (CVE-2026-31431) kernel bug, cloud centralization risk, and democratization of sophisticated attacks.
- **[[entities/matklad-github-io]]** — New Zig 0.16 error context patterns (errdefer + telescopic context) article collected.
- **[[entities/jim-nielsen]]** — "Lots of Little HTML Pages" (LLMS) post-mortem: building websites with HTML/CSS view transitions instead of JS-heavy SPAs.
- raw/articles/ — 18 articles saved from blog ingestion cycle

## [2026-05-03] X Account Scan — Megadocs Synthetic Data Paper + Error Report

- **[[concepts/synthetic-data]]** — Enriched from stub to comprehensive: Megadocs technique (stitching/stretching for 1.80× data efficiency), synthetic rephrasing baseline (1.48×), distributional shift paradox, pre-training best practices. Source: Kim et al. "Data-efficient pre-training by scaling synthetic megadocs" (arXiv:2603.18534, March 2026), shared by @Grad62304977.
- **raw/articles/2026-03-19_megadocs-synthetic-pretraining.md** — Saved paper summary
- **Infrastructure Alert:** 66/79 tracked X accounts had user_id resolution failures — investigation needed

## [2026-05-03] Daily Skeleton Enrichment — Sebastián Ramírez, Adam Rosenthal

- **[[entities/sebastian-ramirez]]** — Enriched from stub to comprehensive entity: creator of FastAPI, Typer, SQLModel, Asyncer. Added biography (homeschooled in Colombia, self-taught, cancer survivor), career timeline, project list with GitHub stars, philosophy, Sequoia Open Source Fellowship.
- **[[entities/adam-rosenthal]]** — Researched but could not positively identify in AI/developer ecosystem context. Multiple individuals with this name exist but none match the wiki's domain. Set to `status: needs-identification`.

## [2026-05-03] Trending Topics — NIST CAISI Evaluation, CISA AI Cyber Deadline, Boston Dynamics Exodus, Gary Marcus

- **[[entities/deepseek]]** — Updated with NIST CAISI evaluation section: +8 month capability lag vs US frontier, suspected benchmark contamination, cost efficiency confirmed. Added CAISI evaluation results table and verification under "Independent Evaluation" heading.
- **[[entities/gary-marcus]]** — Enriched from stub to comprehensive entity: cognitive scientist, LLM consciousness skepticism, Gullibility Gap concept, Dawkins critique. Added publications, quotes, cross-references.
- **raw/articles/2026-05-01_nist-caisi-deepseek-v4-evaluation.md** — Saved NIST CAISI full report
- **raw/articles/2026-05-01_cisa-ai-powered-hacking-patch-deadline.md** — Saved Reuters exclusive: CISA considers 3-day patching deadline
- **raw/articles/2026-05-01_boston-dynamics-c-suite-exodus.md** — Saved Semafor exclusive: CEO/COO/CSO/CTO departures
- **inbox/rss-scans/daily-scan-2026-05-03.md** — Saved daily trending topics report (7 topics)
- **Trending topics identified (top 5):** ① NIST CAISI DeepSeek V4 evaluation (8-month gap, benchmark contamination) ② CISA 3-day patch deadline (AI-powered hacking by Mythos/GPT-5.4-Cyber) ③ DeepSeek V4 + Huawei Ascend 950 supply crunch (ByteDance/Tencent/Alibaba scramble) ④ Boston Dynamics C-suite exodus (Hyundai pressure for humanoid scale) ⑤ Dawkins vs Marcus LLM consciousness debate
- Updated: wiki/index.md (Gary Marcus description enriched), wiki/log.md

## [2026-05-03] Active Crawl — Microsoft Agent 365, Amazon Bedrock AgentCore, Grok Imagine, NVIDIA B300 China Pricing

- **[[concepts/microsoft-agent-365]]** — Created concept page for Microsoft's enterprise AI agent governance control plane. Launched May 1, 2026 at $15/user/month. Manages agents across Foundry, Copilot Studio, and third-party platforms. Key differentiator: security & oversight layer vs. AI feature integration (Wave 3).
- **[[entities/amazon-bedrock-agentcore]]** — Created entity page for AWS's fully-managed agentic AI platform. Framework-agnostic, composable services (Memory, Gateway, Browser Runtime, Code Interpreter). 8-hour long-running workloads, VPC isolation, pay-for-what-you-use. Enterprise case studies: Epsilon, Amazon Devices, Ericsson, Thomson Reuters.
- **[[entities/grok-imagine]]** — Created entity page for xAI's video generation platform. 1.245B videos in first 30 days. DesignArena #1 (Elo 1,329). 6 generation modes, 720p, 30s max. $4.20/min — 7x cheaper than Sora 2 Pro.
- **[[entities/china-ai-industry]]** — Enriched with new "Hardware Supply Crisis" section: NVIDIA B300 servers at $1M in China ($550K in US). Driven by US export controls, Supermicro co-founder arrest, MATCH Act. Split market dynamics. Updated frontmatter.
- **raw/articles/2026-05-03_microsoft-agent-365-launch.md** — Saved raw article
- **raw/articles/2026-05-03_amazon-bedrock-agentcore.md** — Saved raw article
- **raw/articles/2026-05-03_nvidia-b300-china-1m-pricing.md** — Saved raw article
- **raw/articles/2026-05-03_grok-imagine-video-generation.md** — Saved raw article
- Updated: wiki/index.md (3 new entries → 795 total pages), wiki/log.md
- Sources: AllInOneAICenter, AWS Official Docs, Reuters (Exclusive Apr 30), blog.mean.ceo, TNW

## [2026-05-03] Newsletter Wiki Ingest — Superintel+ V4 Newsletter: DeepSeek V4 + Huawei Ascend 950

- **[[entities/deepseek]]** — Major expansion: Added V4 model series table (Pro 1.6T/49B active, Flash 284B/13B active, 1M context MoE). Added pricing comparison, efficiency gains (27% FLOPs/10% KV cache vs V3.2 for Pro). Added Huawei Ascend 950 deployment section: SMIC quadruple-patterning, chip utilization 60%→85%, EUV prototype rumors. Updated strategy and market impact sections. 2→8 cross-references.
- **raw/articles/2026-05-02-superintel-nvidia-blackwell-vs-huawei-ascend-deepseek-v4.md** — Saved raw article (paywalled, preview only)
- Source: Superintel+ newsletter via beehiiv (getsuperintel.com), Kim "Chubby" Isenberg, May 2 2026. Cross-referenced with Simon Willison's V4 coverage (Apr 24 2026).

## [2026-05-03] Karpathy — Vibe Coding MenuGen Post-mortem

- **[[entities/karpathy-writings]]** — Expanded "Vibe coding MenuGen" entry: 80/20 trap, API hallucination issues (OpenAI OCR, Replicate), Vercel/Clerk/Stripe deployment hurdles, LLM gaslighting, four demands for vibe coding era
- **[[entities/karpathy-ideas]]** — Added MenuGen post-mortem insights section to Vibe Coding entry: IKEA Future metaphor, Batteries-Included Platform vision, LLM-Friendly Design principle, Apps as Prompts thesis
- **[[concepts/harness-engineering/agentic-workflows/vibe-coding]]** — Added Karpathy MenuGen as the original vibe coding case study, with post-mortem insight table and four demands
- **raw/articles/2025-04-27_karpathy-vibe-coding-menugen.md** — Saved raw article
- Source: https://karpathy.bearblog.dev/vibe-coding-menugen/

## [2026-05-03] Daniel Miessler — "The Most Important Ideas in AI Right Now"

- **[[entities/daniel-miessler]]** — Created entity page for Daniel Miessler. Cybersecurity/AI engineer, founder of Unsupervised Learning. Creator of Fabric AI Framework (30K+ stars), SecLists, PAI, TELOS. Former Apple (BI Security), HP (co-founded Fortify on Demand). Author of Human 3.0 philosophy.
- **[[concepts/autonomous-component-optimization]]** — Created concept page. Miessler's generalization of Karpathy's Autoresearch to any workflow: the Universal Improvement Cycle (Map→Execute→Log→Collect→Optimize→Update).
- **[[concepts/intent-based-engineering]]** — Created concept page. Identifies the "articulation gap" as the new bottleneck: engineering shifts from "how to build" to "how to describe what good looks like."
- **[[concepts/agentic-scaffolding]]** — Enriched with "The Scaffolding Ratio" section: Miessler's thesis that 75–99% of knowledge work is overhead/scaffolding.
- **[[concepts/karpathy-loop]]** — Enriched with "Generalization: Autonomous Component Optimization" section.
- **raw/articles/2026-04_daniel-miessler_most-important-ideas-in-ai.md** — Saved raw article.
- Source: https://danielmiessler.com/blog/the-most-important-ideas-in-ai

## [2026-05-03] Claw Code — Open-Source AI Coding Agent Harness (Claude Code Clean-Room Reimplementation)

- **[[concepts/claw-code]]** — Created concept page for Claw Code, the open-source clean-room Rust/Python reimplementation of Claude Code's agent harness architecture. Created by [[sigrid-jin]] after Anthropic's March 31, 2026 source code leak. Fastest repo in GitHub history to surpass 100K stars (~24 hours). Covers: dual-language architecture (Rust 72.9% / Python 27.1%), 11+ Rust crates, 19 built-in permission-gated tools, three-part meta-system (OmX/clawhip/OmO), comparison with Claude Code and OpenClaw, the autonomous development thesis, roadmap (deterministic state machines, LaneEvents), and known gaps.
- **[[entities/sigrid-jin]]** — Created entity page for Sigrid Jin (@realsigridjin), creator of claw-code. Korean-Canadian, UBC. Featured in WSJ for 25B Claude Code tokens. Built initial Python port in hours with 1 human helper + 10 OpenClaw instances.
- **[[entities/yeachan-heo]]** — Created entity page for Yeachan Heo (@bellman_ych), creator of oh-my-codex (OmX), oh-my-claudecode (OMC), clawhip. Algorithmic trader in Seoul. Primary collaborator on claw-code Rust implementation.
- **[[entities/ultraworkers]]** — Created entity page for UltraWorkers GitHub organization, canonical home of the claw-code Rust implementation.
- **raw/articles/2026-05-03_claw-code-overview.md** — Saved raw article with full details.
- Updated: wiki/index.md (4 new entries → 789 total pages), wiki/log.md

## [2026-05-03] Knowledge Shields — Systems Understanding Methodology from Entropic Thoughts

- **[[concepts/knowledge-shields]]** — Created concept page capturing Chris (Entropic Thoughts)'s unified methodology for understanding complex systems. Covers: the hypothesis-invalidation loop, mental model diagnosis through observation, self-verification skills (alternative approaches, feasibility checks, recursive verification), knowledge shields (strongly held wrong beliefs resist correction), productive vs. unproductive error classification, and motivation management. Includes connections to AI agent debugging, eval design, and prompt engineering. Sources: entropicthoughts.com/understanding-systems.
- **[[entities/entropicthoughts-com]]** — Added wikilink to knowledge-shields concept in Related section; added Understanding Systems to Timeline.
- Raw article already saved: raw/articles/entropicthoughts.com--understanding-systems--149e6399.md.
- Source: https://entropicthoughts.com/understanding-systems

## [2026-05-03] Raindrop — AI Agent Monitoring Platform

- **[[concepts/raindrop]]** — Created concept page for Raindrop, "Sentry for AI Agents" monitoring platform. Covers: Trajectories (agent-native trace viz), Signals (7 default + custom classifiers), Deep Search (natural language over traces), Experiments (A/B testing), Agent Self Diagnostics. Includes detailed comparison tables with Braintrust/LangSmith/Arize/Langfuse/Logfire and cross-category comparison with OpenAI Symphony (monitoring vs orchestration layers). Sources: raindrop.ai docs, blog posts (seed round, trajectories, agent self diagnostics), PRNewswire.
- **raw/articles/2026-05-03_raindrop-introduction.md** — Saved raw article with full detail.
- Source: https://www.raindrop.ai/docs/introduction

## [2026-05-03] ByteRover — Portable File-Based Memory Layer for Coding Agents

- **[[entities/byterover]]** — Created entity page for ByteRover (formerly Cipher). Portable, file-based memory layer for autonomous coding agents with market-best 92-96% retrieval accuracy on LoCoMo/LongMemEval. Built in TypeScript by campfirein (Vietnam). Architecture: replaces vector DBs with LLM-curated Hierarchical Context Tree of Markdown files with Adaptive Knowledge Lifecycle (AKL) and 5-tier progressive retrieval. Open source (Elastic 2.0), 4.2k+ GitHub stars. Native plugins for Hermes Agent, Claude Code, OpenClaw. arXiv:2604.01599.
- **[[entities/andy-nguyen]]** — Created entity page for Duy Anh "Andy" Nguyen (@kevinnguyendn), Founder & CEO of ByteRover. Based in Da Nang, Vietnam. Former ML Engineer at OpenLab JSC.
- **raw/articles/2026-05-03_ByteRover-overview.md** — Saved raw article from homepage + GitHub + arXiv paper.
- Source: https://www.byterover.dev/blog, https://github.com/campfirein/byterover-cli, https://arxiv.org/abs/2604.01599

## [2026-05-03] Minimal Coding Agent — Thorsten Ball's "Emperor Has No Clothes" Guide

- **[[concepts/minimal-coding-agent]]** — Created concept page for the minimal code-editing agent pattern: ~400 lines of Go, 3 tools (read_file/list_files/edit_file via string replacement), heartbeat loop. Thorsten Ball's thesis: the agent loop itself has no moat; differentiation comes from UI/UX, system prompts, error handling.
- **[[entities/thorsten-ball]]** — Created entity page for Thorsten Ball. Software engineer at Sourcegraph (Amp), author of Writing An Interpreter In Go / Writing A Compiler In Go, writes Register Spill newsletter.
- **[[concepts/agent-loop-orchestration]]** — Added [[concepts/minimal-coding-agent]] as a concrete Go implementation reference.
- **[[concepts/harness-engineering/system-architecture/building-effective-agents]]** — Added [[concepts/minimal-coding-agent]] as a concrete implementation of Anthropic's "simple composable patterns" principle.
- **raw/articles/2025-04-15_ampcode-how-to-build-a-code-editing-agent.md** — Saved raw article.
- Source: https://ampcode.com/notes/how-to-build-an-agent

## [2026-05-02] OpenRouter State of AI 2025 — 100T Token LLM Usage Study

- **[[concepts/openrouter-state-of-ai-2025]]** — Created concept page for the landmark study by OpenRouter & a16z analyzing 100 trillion tokens of real-world LLM usage. Covers: reasoning inflection point (Dec 5, 2024, o1 release), open vs closed source dynamics (30% OSS equilibrium, Chinese OSS rise), agentic inference shift (50%+ reasoning tokens, 4x prompt length explosion), category taxonomy (Programming 50%+ tokens, Roleplay 52% of OSS), provider specializations, economics (price inelasticity, Jevons Paradox, market archetypes), and geography (Asia 31%, doubled).
- **[[concepts/glass-slipper-effect]]** — Created concept page for the Cinderella Glass Slipper retention framework. Foundational cohorts (~40% retention at Month 5), Boomerang Effect, cognitive inertia, and workload-model fit thesis.
- **[[entities/openrouter]]** — Created entity page for OpenRouter, the unified API gateway for 300+ LLMs. Published the State of AI 2025 study with a16z.
- **[[entities/malika-aubakirova]]** — Created entity page for Malika Aubakirova, a16z infrastructure researcher and co-author of the State of AI 2025 study.
- **raw/articles/2025-12-01_openrouter-state-of-ai-2025.md** — Saved raw article.
- Source: https://openrouter.ai/state-of-ai

## [2026-05-02] Sparse Signal Loop — stochi's Experimental Validation of MGH

- **[[concepts/sparse-signal-loop]]** — Created concept page for Sparse Signal Loop experiment. Controlled 2×2 matrix test of feedback density (sparse vs dense), memory location (chat vs files), and procedure persistence (reinjection vs skill files) across LongBench-Pro and Mini SWE Agent Plus. Key findings: feedback sparsity is task-dependent, the "Judge Gap" (0.9667 Judge YES vs 0.5667 actual solve), constraint beats free-form memory.
- **[[entities/stochi]]** — Created entity page for stochi (stochi0). Independent AI researcher focused on post-training, agents, RL, model architectures. Previously shipped AI at QX Labs and Unsiloed AI (YC F25).
- **[[concepts/mismanaged-geniuses-hypothesis]]** — Added "Empirical Validation: Sparse Signal Loop" section with 3 key findings (supports, refines, warns). Added [[concepts/sparse-signal-loop]] to Related Concepts and cross-connections.
- **raw/articles/2026-05-02_sparse-signal-loop.md** — Saved raw article.
- Source: https://stochi0.vercel.app/writings/sparse-signal-loop

## [2026-05-02] Antoine Buteau — Automation Series (10 Parts) Full Ingestion

- **[[entities/antoine-buteau]]** — Created entity page for Antoine Buteau (Head of BizOps at Shakepay, previously Replit). Documented career timeline, Automation Series overview table, other series (Agency, Power, Technical Literacy, Live Player), key ideas (Three Kinds of Work, Automation Boundary, HITL as Design Pattern, Bounded Agents), and key quotes.
- **[[concepts/automation-series]]** — Created concept page for the 10-part Automation Series. Parts table covering all entries from "Automation Is Not One Thing" through "The Automation Architecture Worksheet." Key insights synthesized: Three Kinds of Work, Confidence-Driven Action, Bounded Agents, Staged Autonomy, and more.
- **raw/articles/2026-05-02_antoine-buteau_automation-series-1.md** through **automation-series-10.md** — Saved all 10 raw articles.
- Sources: https://www.antoinebuteau.com (full series via sitemap)

## [2026-05-02] PyTorch GPU Memory Profiling — Memory Measurement Without Execution (FakeTensorMode)

- **[[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]]** — Added Section 4: "モデルを実行せずにメモリ使用量を測定する — FakeTensorMode + MemoryTrackingMode". Covers Alban Desmaison's ~30-line MemoryTrackingMode implementation, simultaneous use with FakeTensorMode for CUDA-on-CPU memory estimation, Module-wise tracking (PR #124688), allocated vs reserved memory distinction with fragmentation, NCCL buffer blind spot, and PyTorch caching allocator refactoring roadmap.
- Source: https://dev-discuss.pytorch.org/t/how-to-measure-memory-usage-from-your-model-without-running-it/

## [2026-05-02] PyTorch GPU Memory Profiling — Memory Snapshot & Profiler Tools Ingestion

- **[[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]]** — Created concept page for PyTorch v2.1+ GPU memory debugging tools. Covers Memory Snapshot (allocation trace visualization with stack traces), Memory Profiler (categorized usage: gradients/optimizer/activations), OOM staircase pattern fix (`optimizer.zero_grad(set_to_none=True)`), `record_function` labeling, and tool comparison table.
- **[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]** — Added `pytorch-gpu-memory-profiling` to `related` and `Related Pages` sections.
- **[[concepts/ai-infrastructure-engineering/_index]]** — Added "Memory Debugging" row to scope table with link to new page.
- Source: https://pytorch.org/blog/understanding-gpu-memory-1/

## [2026-05-02] Braintrust Evals 101 Course — Practical Eval Methodology Ingestion

- **[[concepts/ai-evals]]** — Added "Braintrust Evals 101: Practical Eval Methodology" section covering: non-determinism as core thesis, 3-component eval model (dataset/task/scorer), LLM-as-Judge with choice scores, trial counts for variance reduction, multi-level trace scoring (per-turn vs per-trace), online scoring, the Improvement Loop with temperature=0/max_concurrency=1 settings, and the GPT-4o sycophancy rollback case study.
- **[[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]]** — Enriched with Braintrust eval features, Evals 101 course module table, and comparison matrix with LangSmith/Arize Phoenix/Inspect AI.
- **raw/articles/2026-05-02_braintrust-evals-101-why-are-evals-important.md** — Saved raw article with full module-by-module breakdown (14 modules across Learn/Build/Refine sections).
- Source: https://www.braintrust.dev/foundations/why-are-evals-important | GitHub: braintrustdata/eval-101-course

## [2026-05-02] lambda-RLM (Typed Recursive Reasoning) — Huawei Paper Ingestion

- **[[concepts/typed-rlm]]** — Created concept page for lambda-RLM (typed functional runtime, Huawei Noah's Ark Lab). Formal guarantees (termination, cost bounds, optimal partition k*=2), Y-combinator fixed-point over SPLIT/MAP/REDUCE combinators. 29/36 wins, +21.9pp accuracy, 4.1x faster. arXiv:2603.20105 (arXiv-only, ingested per user request).
- **[[concepts/lambda-rlm]]** — Updated with disambiguation warning distinguishing from Huawei's lambda-RLM. Added [[concepts/typed-rlm]] to related.
- **[[concepts/rlm-recursive-language-models]]** — Added lambda-RLM variant section with comparison table. Updated Related Concepts.
- **raw/papers/2026-03-20_2603.20105_y-combinator-for-llms.md** — Saved raw paper summary with blocked reason: no_peer_review.
- Source: `raw/papers/2026-03-20_2603.20105_y-combinator-for-llms.md` | https://arxiv.org/abs/2603.20105

## [2026-05-02] Recursive by Design — Lambda-RLM, Theodoros Galanos & The Harness Blog Ingestion

- **[[concepts/lambda-rlm]]** — Created concept page for Lambda-RLM, a deterministic pipeline variant of RLM for the AEC domain. Plan (0 LLM calls) → Extract+Review → Generate. 14x token reduction, +8.4% quality improvement over open REPL.
- **[[entities/theodoros-galanos]]** — Created entity page for Theodoros Galanos, AI researcher and harness engineering practitioner. Chief Science Officer at infrared.city. Creator of Lambda-RLM and AEC-Bench.
- **[[entities/the-harness-blog]]** — Created entity page for The Harness blog (theharness.blog). 25 posts across 6 topics on harness engineering, agent evaluation, and AI in AEC.
- **[[concepts/rlm-recursive-language-models]]** — Updated with Lambda-RLM production case study section and benchmark metrics.
- **[[concepts/recursive-language-models]]** — Updated with Lambda-RLM variant reference.
- Source: `raw/articles/2026-05-02_the-harness-blog_recursive-by-design.md` | https://theharness.blog/blog/recursive-by-design/

## [2026-05-02] Paul Hoekstra — Agentic Engineering 4-Layer Framework (Full Series Ingestion)

- **[[entities/paul-hoekstra]]** — Created entity page for data engineer and Paul's Pipeline author. Documented 4-layer Agentic Engineering framework, key articles, and contributions.
- **[[concepts/harness-engineering/agentic-engineering-configuration-layer]]** — Created concept page for Layer 1. CLAUDE.md, Skills system, `<HARD-GATE>` enforcement, SkillsBench findings, anti-rationalization tables, division of labor strategy.
- **[[concepts/harness-engineering/agentic-engineering-capability-layer]]** — Created concept page for Layer 2. MCP with deferred loading, live docs (Context7, DeepWiki, Exa), visual output tools (Figma, frontend-slides, Remotion, draw.io), 3-layer memory strategy (MEMORY.md, episodic-memory, QMD).
- **[[concepts/harness-engineering/agentic-engineering-orchestration-layer]]** — Created concept page for Layer 3. Subagents vs Agent Teams, Ralph Loop, Git worktrees, context compression, "context over roles" design principle.
- **[[concepts/harness-engineering/agentic-engineering-guardrails-layer]]** — Created concept page for Layer 4. Poisoned instructions, homoglyph attacks, sandboxing (bubblewrap/Apple), permissions system, AST-grep, pre-commit/CI gates.
- **[[concepts/harness-engineering/agentic-engineering]]** — Updated: Added "Paul Hoekstra's 4-Layer Framework" section with integration notes vs Willison's framing. Updated sources and further reading.
- Source raw articles: 6 articles saved (4 series parts + statusline article + visual output article)

## [2026-05-02] Pi Podcast (Syntax #976) — Entity Enrichment & Concept Update

- **[[entities/pi-coding-agent]]** — Enriched with podcast insights: Pi's core definition ("a while loop with 4 tools"), "Bash is all you need" philosophy, steering queue, self-modifying skills with hot reloading, MCP critique vs Pi approach, prompt injection concerns, "Code is truth" memory philosophy, MAM (Master of Mischief) Slack bot.
- **[[entities/mario-zechner]]** — Enriched: Syntax.fm podcast appearance added to Recent Posts, Pi podcast revelations added to pi section (OpenClaw connection, steering queue, self-modifying skills).
- **[[entities/armin-ronacher]]** — Enriched: Syntax.fm #976 appearance added to timeline (Feb 4, 2026).
- **[[concepts/agentic-security]]** — Updated: Added "Camel Paper" section documenting the two-LLM approach to prompt injection defense and its practical limitations, with quote from the Pi podcast.
- Source: `raw/articles/2026-02-04_pi-syntax-fm-podcast.md` | https://syntax.fm/show/976/pi-the-ai-harness-that-powers-openclaw-w-armin-ronacher-and-mario-zechner/transcript

## [2026-05-02] Simulacrum of Knowledge Work — Concept & Entity Ingestion

- **[[concepts/simulacrum-of-knowledge-work]]** — Created concept page. Critical analysis by @onehappyfellow of how LLMs broke the proxy measures that knowledge work relies on for quality assessment. Covers proxy measures, incentive alignment crisis, Goodhart's Law recursive problem, and the "tokens-spent leaderboard" meta-commentary.
- **[[entities/onehappyfellow]]** — Created entity page for the author of "Simulacrum of Knowledge Work." Head of The Institute for Type Safe Memetic Research. OCaml programmer, technology writer, and rapper.
- Source: `raw/articles/2026-04-25_onehappyfellow-simulacrum-of-knowledge-work.md` | https://blog.happyfellow.dev/simulacrum-of-knowledge-work/

## [2026-05-02] Fireworks AI Podcast (SE Daily Episode 1919) — Entity & Concept Ingestion

- **[[entities/fireworks-ai]]** — Created entity page for Fireworks AI. AI inference and model customization platform for open-weight models. 13T+ tokens/day. Multi-hardware (NVIDIA + AMD), FireAttention kernels, custom speculator training, RFT capabilities.
- **[[entities/benny-chen]]** — Created entity page for Benny Chen, Co-Founder of Fireworks AI. Former Meta ML infrastructure. Key theses: RFT, "Traces Are All You Need," Eval Protocol, multi-hardware supply chain strategy.
- **[[concepts/reinforcement-fine-tuning]]** — Created concept page for RFT. Pragmatic RL fine-tuning using production traces + LLM-as-Judge. RFT vs SFT comparison table, Vercel case study (40x faster code fixing).
- **[[concepts/fine-tuning]]** — Updated: Added RFT as a method in Key Ideas + Terminology. Added related wikilinks to RFT page and Fireworks AI.
- **[[concepts/speculative-decoding]]** — Updated: Added "Custom Speculator Training (Fireworks AI Approach)" section. Documented distribution-matched speculators achieving 90%+ acceptance rates.
- Source: `raw/articles/2026-04-28_fireworks-ai-open-weight-models-sed.md` (SED transcript)

## [2026-05-02] Skeleton Enrichment — Foundation Capital Portfolio Companies (4 entities enriched)

- **[[entities/maximor]]** — Enriched from skeleton to L3 page. Added funding ($9M seed, Foundation Capital), founder bios (Ramnandan Krishnamurthy & Ajay Amudan, ex-Microsoft), Audit-Ready Agent architecture, product table, ERP-agnostic design principles. Sources: Blog, SaaSNews, TechCrunch, Axios.
- **[[entities/regie-ai]]** — Enriched from skeleton to L3 page. Added funding history ($50M total, $30M Series B Feb 2025), founder bios (Srinath Sridhar, Matt Millen), RegieOne platform features, investor list (Khosla Ventures, Scale Venture Partners, Foundation Capital). Sources: Crunchbase, PRNewswire, Regie blog.
- **[[entities/arize]]** — Enriched from skeleton to L3 page. Added funding ($131M total, $70M Series C), founder bios (Jason Lopatecki, Aparna Dhinakaran), Phoenix OSS details (2M+ monthly downloads, 9.5K GitHub stars, OpenTelemetry-based), AI Copilot, enterprise customers (Uber, Chime, eBay, Spotify, US Air Force). Sources: Arize blog, PRNewswire, GitHub, Crunchbase.
- **[[entities/playerzero]]** — Enriched from skeleton to L3 page. Added funding ($20M total, $15M Series A led by Foundation Capital), founder bio (Animesh Koratana, Stanford DAWN lab), context graph technology deep-dive (two clocks problem, engineering world models, code simulation), competitive positioning vs Cursor/Datadog/APM, customer Zuora, investor list (Matei Zaharia, Drew Houston, Dylan Field, Guillermo Rauch). Sources: TechCrunch, PlayerZero resources, AInvest.
- **[[entities/larsen-cundric]]** — Cleaned up stale `**Status:** skeleton` body text (frontmatter already showed `status: active`).

## [2026-05-02] Wiki Health Lint — Daily Automated Check

- **Critical Issues Found:**
  - 110 broken wikilinks to non-existent concept/entity pages
  - 331 unknown tags (tag sprawl — not in SCHEMA.md taxonomy)
  - 27 orphan entity pages, 172 orphan concept pages
  - 43 pages with incomplete frontmatter
  - Index count mismatch: header says 760 total but 1498 actual pages exist

- **Warnings:**
  - 91 oversized pages (>200 lines), including index.md at 1521 lines
  - 638 stub pages containing TODO markers
  - 7 entities split across 4-6 sub-pages each (claude-code, clefourrier, etc.)
  - 1 corrupted raw article with HTML parsing artifacts

- **Minor:**
  - 4 pages missing from index.md
  - 2 subdirectories missing _index.md
  - 1 page without frontmatter (log-2026.md)

## [2026-05-02] Active Crawl — xAI Grok 4.3, Microsoft Copilot Wave 3, MIT FTTE, SpaceX-xAI Merger

- **Researched 5 trending AI/ML topics** not yet covered in wiki:
  1. **xAI Grok 4.3** — Always-on reasoning, 1M context, aggressive pricing, Custom Voices
  2. **Microsoft Copilot Wave 3** — Copilot Cowork with Anthropic Claude, Agent 365, E7 Frontier Suite
  3. **MIT FTTE** — Federated Tiny Training Engine, 81% faster FL on edge devices
  4. **SpaceX acquires xAI** — $1.25T combined valuation
  5. **Grok Computer** — xAI's autonomous desktop agent

- **Saved 4 raw articles:**
  - `raw/articles/2026-05-01_xai-grok-4-3-launch.md`
  - `raw/articles/2026-03-09_microsoft-copilot-wave-3-frontier-transformation.md`
  - `raw/articles/2026-04-29_mit-ftte-federated-learning-edge-devices.md`
  - `raw/articles/2026-02-02_spacex-acquires-xai-merger.md`

- **Created 5 wiki pages:**
  - [[entities/xai]] — Company entity covering Grok ecosystem, SpaceX acquisition, pricing strategy
  - [[entities/grok-4-3]] — Latest model: always-on reasoning, 1M context, benchmarks, Custom Voices
  - [[concepts/grok-computer]] — Desktop agent: pixel-reading, universal app control, Grok 4.3 integration
  - [[concepts/microsoft-copilot-wave-3]] — Wave 3 transformation: Copilot Cowork, Agent 365, E7 suite
  - [[concepts/federated-tiny-training-engine]] — MIT FTTE: semi-async FL with 81% speedup on edge devices

- **Updated [[index]]** — Added 2 entities + 3 concepts. Total: 755→760. Entities: 365→367. Concepts: 402→405.

## [2026-05-02] Shopify — "The Most Future-Proof Job: Entrepreneurship" Data Analysis

- Saved raw article: `raw/articles/2026-04-15_shopify-future-proof-job-entrepreneurship.md` — Shopifyデータサイエンスチームによる起業家精神の分析。AIによる雇用減少（2026年3月の解雇の25%）と起業家増加（Shopify初回販売が2018年比7倍）の「Risk Flip」を示すデータ。リピート創業者の2倍以上の売上、eコマースの市場拡大（14%→20%+）、AI「Exoskeletons」の役割。
- Updated [[entities/shopify]] — 「Entrepreneurship & Ecommerce Trends」セクションを追加。「Risk Flip」テーゼ、リピート創業者 compounding、AI Exoskeletonsのデータを収録。
- Updated [[solo-founder-stack]] — 「Empirical Support: Shopify Data」セクションを追加。Shopifyの実証データで solo founder テーゼを補強（Risk Flip、Compounding Entrepreneur、AI Accelerator）。

## [2026-05-02] Every Guide — Agent-native Product Management + Compound Engineering

- Saved raw article: `raw/articles/2026-05-02_guide-to-agent-native-product-management.md` — Every社のガイド。Marcus Moretti（Spiral GM）が提唱するエージェントネイティブPM。ce:strategy（戦略策定）とce:product-pulse（自動ヘルスレポート）の2スキルを中核に、MCP経由でPostHog/Stripe/Datadogを統合。80/20計画重視シフト。

- Created [[entities/every-inc]] — AI-native media & software company (CEO Dan Shipper). 5 products with single-person teams. Compound Engineering plugin (7K+ stars).

- Created [[entities/marcus-moretti]] — GM of Spiral, author of Agent-native PM guide.

- Created [[entities/kieran-klaassen]] — GM of Cora, author of Compound Engineering: The Definitive Guide.

- Created [[concepts/agent-native-product-management]] — PMフレームワーク: 会話が仕事、80/20計画シフト、ce:strategy/ce:product-pulseスキル、エージェント管理バックログ。

- Created [[concepts/compound-engineering-every]] — Every社版Compound Engineering（各作業が将来を容易化）。Simon Willison版（コードレベルの反復改善ループ）とは異なる。

- Updated [[concepts/compound-engineering-loop]] — Stub→redirect（compound-engineering-every および Simon Willison版への誘導ページに変更）。

- Updated [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — Simon Willison版にEvery社版への相互参照を追加。

- Updated [[index]] — Added 3 entities + 2 concepts. Total: 750→755. Reclassified 1 stub.

## [2026-05-02] YouTube Video — "Why 2026 is The Year of Agentic Search" (Doug Turnbull & Jo Kristian Bergum)

- Saved raw article: `raw/articles/2026-05-01_doug-turnbull-2026-is-the-year-of-agentic-search.md` — 65-min fireside chat covering four pillars: LLM Query Understanding at scale, Autoresearch (agents writing ranking code), Agentic Search Harnesses (feedback loops for dumb retrievers), and LLM-as-a-Judge for principled search evaluation.
- Updated [[entities/doug-turnbull-speaking]] — Added talk to conference talks list (removed duplicate Berlin Buzzwords entry).
- Updated [[concepts/agentic-search]] — Added source with summary of four pillars.

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

---

## [2026-05-04] blog-wiki-ingest | 18 articles, 0 created, 0 updated
- **Pipeline**: blog-ingest → blog-triage → blog-wiki-ingest
- **Checkpoint**: 20260504T070032Z
- **Take**: 0 — 既存Wikiページですべてカバー済み
- **Reference**: 4 — Simon Willison/Anthropic sycophancy (anti-sycophancy.md), Martin Alderson CopyFail (martin-alderson.md), George Hotz essay (george-hotz.md), Gary Marcus healthcare (gary-marcus.md)
- **Skip**: 14 — Zig, PNG, touch typing, RSS→Atom, politics, staff engineer, math, sponsor page, Steve Jobs, HTML/CSS, 86-DOS, Bluesky politics, wheel history, empty file
- **Verdict**: No new wiki pages needed. All AI-relevant articles already captured in existing entity/concept pages.

## [2026-05-06] dreaming | Wiki ingest — enriched stub page, 7 themes skipped (already covered)

### Dreaming Pipeline
- **Source**: dreaming-group checkpoint (2026-04-28, 8 themes from 37 articles)
- **Pre-run script**: Failed JSON parse from dreaming-group output; recovered from fallback file at `/opt/data/.hermes/cron/data/dreaming/grouped_themes_latest.json`

### Pages Enriched
- 🆙 [[concepts/2026-04-24-gpt-5-5-chatgpt-images-2-0-qwen3-6-27b]] — Enriched from 420-byte stub (status: stub) to full synthesis page (3.8KB, status: enriched). Covers April 2026 OpenAI launch wave: GPT-5.5 (SPUD), ChatGPT Images 2.0 with reasoning, Qwen3 6B/27B, Workspace Agents. Removed `status: stub`, cross-references to 5 related pages.

### Themes Skipped (Already Covered by Existing Pages)
1. **ChatGPT Images 2.0 Reasoning** (0.72, NJ=4) — Fully covered in [[concepts/chatgpt-images-2.0]] (updated 2026-04-28)
2. **Google TPU 8t/8i Deep Dive** (0.68, NJ=3) — Fully covered in [[entities/google-tpu]] (updated 2026-04-28, 139 lines)
3. **GitHub Copilot Token Billing** (0.65, NJ=4) — Fully covered in [[concepts/github-copilot-billing]] (updated 2026-04-30)
4. **GPJT LLM from Scratch IFT** (0.61, NJ=2) — Covered in [[entities/gpjt]] (part 32l detailed)
5. **Gumloop AI Automation** (0.48, NJ=2) — Below threshold, themes 7 days stale
6. **AI Coding Best Practices** (0.46, NJ=2) — Below threshold, themes 7 days stale
7. **Google Photo Scanning AI** (0.42) — Below threshold, skip
8. **Bezos Project Prometheus** (0.40, NJ=3) — Below threshold, skip

### Health Note
- Index.md has 208 `|-` pipe-corrupted lines (pre-existing issue, tracked by wiki-health pipeline)
- Entity pages `concepts/gpt-5.5-chatgpt-images-2-0-qwen3-6-27b.md` resolved to `concepts/2026-04-24-gpt-5-5-chatgpt-images-2-0-qwen3-6-27b.md` (date-prefixed)

---

## [2026-05-06] lint | 定期ヘルスチェック実行
- index.md: 1599ファイル中847件しかカウント（752件過少）
- index.mdフォーマット破損: 'N|-'パターン20行、'|-'先頭217行
- index.md重複エントリ17件、存在しないターゲット24件
- Wikilinks壊れ284件、未分類タグ430件（220ページ影響）
- 孤立ページ1190件、大容量ページ103件
- 命名規則違反4件（日付始まり3、特殊文字1）
- log.md正常（77エントリー）、メタデータ完全性OK
---
