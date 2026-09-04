# 🔥 トレンドトピックレポート — 2026-08-15

> 分析期間: 2026-08-12 → 2026-08-15 (3日間、前回レポート 8/13 からの差分中心)
> ソース: blogwatcher DB 107記事 + raw articles 122件 + HN Algolia 定点クエリ + wiki/log.md head-scan
> 集中度注記: 本日は**「フロンティアモデル週」の続き + 資金調達ニュース集中**。Gemini 3.7 Flash (8/13) と GLM-5.3 (8/14) という2大モデル発表に加え、OpenAI/Anthropic の同時IPO準備が金融報道を賑わせた。8/13レポート対象の Grok 4.6 / Qwen3.8-Max / DeepSeek V4 Pro / Claude透かし / MAI-Thinking-1 / J-Lens / AI-for-Science は重複除外済み。

## 1️⃣ 🚀 Gemini 3.7 Flash — Googleの「ワークホース」モデル刷新、コーディング+33% (HN 953pts)

**強度: ★★★★★** | **関連ソース:** blog.google (8/13), Artificial Analysis (8/13-14), 8/13レポートでは未報告

Google DeepMindが**Gemini 3.7 Flash**を発表（8/13、HN 953pts/484c — 分析期間最大級）。「コーディングとエージェントのための最も賢いワークホースモデル」と位置づけ、3.6 Flash比で**FrontierCode 1.1 43.6% (vs 34.4%)、DeepSWE v1.1 65.3% (vs 49.0%)** とコーディングで大幅向上。WebDev Arena Elo 1588、**GDP.pdf 34.0% (vs 22.0%)、AutomationBench 30.4% (vs 17.0%)** と知識労働ベンチも倍近い伸び。**導入価格 $0.75/$3.75 per MTok**（3.6 Flashの半額）で、Gemini Spark（Google AI Pro/Ultra、160+ヶ国）をローンチ時から駆動。CBRN/サイバー悪用対策のFrontier Safety safeguardsも更新。8/7の「Gemini is Cooked」ベア論への回答として、モデル事業の現実的強化策を示した形。

- [Introducing Gemini 3.7 Flash (blog.google, HN 953pts)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/)
- [Gemini 3.7 Flash: On the Intelligence vs. Time per Task Pareto frontier (AA)](https://artificialanalysis.ai/articles/gemini-3-7-time-frontier)
- 📝 ✅ [[concepts/gemini/gemini-3-7-flash]] 8/15作成済み（active-crawl）

## 2️⃣ 🦾 GLM-5.3 — オープンウェイト最強コーディング + 「創発的サイバー能力」 (HN 1103pts)

**強度: ★★★★★** | **関連ソース:** Z.AI (8/14), Interconnects (8/14), Axios (8/14) — 8/13レポート対象外の新規発表

Z.AI（Zhipu）が**GLM-5.3**を公開（8/14、HN 1103pts/543c — 分析期間最大のHNストーリー）。**GLM-5.2と同じベースモデルを使い、能力向上は全てポストトレーニング由来**という異例の構成。Terminal-Bench 3.0で**4.6→28.3**、DeepSWE v1.1 66.9、Z.ai Code BenchはMax effort 34.5%（GLM-5.2の23.4%から+50%）。最大の話題は**ポストトレーニングでサイバー能力が想定より速く発達**し、**CyberGym脆弱性発見 84.5%**（Mythos 5 83.8% / GPT-5.6 Sol 83.6%を上回る）で**オープンウェイト初の閉域フロンティア並み**に。実世界で**269プロジェクト中2,436件の脆弱性**を発見（最古は1981年、平均潜伏26.6年）し、Z.ai Security Disclosure Ledger (cvd.z.ai) を開設。ExploitBench 54.4%はMythos 5 (78.0%)に及ばず「発見はSOTA・エンドツーエンド活用は未達」という**段階的リスク像**が、クローズドモデルのサイバーゲーティング論争（Anthropic Mythos/Fable制限）と対をなす。ウェイトは安全性評価完了後の**2週間後にオープン予定**。

- [GLM-5.3: Frontier coding with emergent cyber capabilities (Z.AI, HN 1103pts)](https://z.ai/blog/glm-5.3)
- [GLM-5.3: How Chinese labs keep stride with the frontier (Interconnects)](https://www.interconnects.ai/p/glm-53-how-chinese-labs-keep-stride)
- 📝 ✅ [[concepts/glm-5-3]] 8/14作成 + 8/15 Nathan Lambert戦略分析追記（newsletter-wiki-ingest）

## 3️⃣ 💰 OpenAI・Anthropic同時IPO準備 — $40Bランと$2T評価の「記録的IPO」競争

**強度: ★★★★★** | **関連ソース:** Bloomberg (8/13), FT (8/13, 8/15), Fortune (8/13), CNBC (8/11, 8/14), Reuters (8/15), Axios (8/14)

両フロンティアラボのIPO準備が金融報道の集中砲火に。**OpenAIは年間経常収入ラン$40B超え**（Bloomberg 8/13、2025年末の約2倍）、$7B株主売却完了（CNBC 8/11）、FTは「Sam AltmanがIPO推進を準備、社内は混乱」と報道（8/15）。**Anthropicは10月の$2T評価IPOを計画**（FT/Fortune 8/13 — 史上最大級）、Reutersは**2028年売上$190-200B前提の評価論**を報道（8/15）。両社とも機密IPO書類を提出済み（entities/openai 8/15更新）。懸念材料も顕在化 — CNBC「OpenAI talent exodusはIPO前の巨大レッドフラグ」、Axios「Anthropicはリスク上昇を認識しつつ強いModel 2をリリースする計画なし」。**「IPOラッシュ = フロンティア資本主義の決算点」**として、8/8のEd Zitron「AIにいくら必要なのか」($750B計算需要/ハイパースケーラー$1.65Tオフバランス)と併せて読むべき経済学クラスタ。

- [OpenAI's Revenue Run Rate Tops $40B Ahead of IPO (Bloomberg)](https://www.bloomberg.com/news/articles/2026-08-13/openai-s-revenue-run-rate-top)
- [Anthropic investors bet on $2T valuation in record IPO (FT)](https://www.ft.com/content/840ac156-af1c-4a82-b260-ae791072fcfa)
- [OpenAI talent exodus raises 'huge red flag' ahead of IPO (CNBC)](https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html)
- 📝 ⚠️ 部分反映 — [[entities/openai]] 経済更新✅ / [[entities/anthropic]] にcontested $2T IPO注記あり / **IPO統合ページは未作成（任意）**

## 4️⃣ ⚡ GPT-5.6 Sol Ultrafast — Cerebras製ウェハースケールで最大14倍速 (HN 701pts)

**強度: ★★★★☆** | **関連ソース:** OpenAI (8/13), Cerebras (8/13) — 8/13レポートで未報告の見逃しトピック

OpenAIが**「Ultrafast」モードをプレビュー**（8/13）— **GPT-5.6 Solを標準処理比で最大14倍速**で動作させ、**最大750トークン/秒**を実現。中身は**Cerebrasのウェハースケールエンジン**（44GB SRAMをウェハ1枚に搭載、重みをオンチップに保持してメモリ帯域ボトルネックを回避）。HLE 2,500問を**11時間11分**で完走（Claude Fable 5は78時間27分 — 約7倍差）、GDP-Valで**5.6倍のエンドツーエンド高速化・品質劣化なし**。Jane Street/Podium/Basisが早期顧客として速度活用をコメント。**「速度か知能か」のトレードオフ解消**を旗印に、推論基盤競争（Cerebras vs GPUクラスタ）の新たな節目。HN 701pts/272c（Cerebras記事）が実質的な支持基盤。

- [Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed (OpenAI)](https://openai.com/index/previewing-ultrafast/)
- [Accelerating GPT-5.6 Sol Ultrafast with OpenAI (Cerebras, HN 701pts)](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai)
- 📝 ✅ [[concepts/gpt/gpt-5-6]] 「Ultrafast Mode」節 8/14反映済み（active-crawl）

## 5️⃣ 🔌 DeepSeek Harness (dsh) — 「すべてがプラグイン」のオープンエージェントハーネス、48時間でGitHub★10.6万

**強度: ★★★★☆** | **関連ソース:** DeepSeek (8/13), GitHub, HN (低ポイントだがGitHub熱量が主信号)

DeepSeekが**オープンソースのエージェントハーネス「dsh」をリリース**（8/13）。**「everything is a plugin」アーキテクチャ** — モデルアダプタ・ツールレジストリ・セッションログ・エージェントループ自体まで全てプラグイン化し、**特権コアを持たず設定から全コンポーネントを差し替え可能**。Cordisフレームワーク上に構築（*A Programming Paradigm for Spatiotemporal Composability*）。**リリース48時間でGitHubスター約10.6万**という異常な速度で、ミニマルハーネス（「less you build」哲学）に対抗する**「最大構成可能」ハーネス**として[[concepts/harness-commoditization|ハーネスコモディティ化]]論争に新軸を追加。HNは10pts程度と低いが、GitHubスター熱量が主信号（8/11のHN-low/X-engagementレスキューと同型）。同日のAugment「Auggie CLIを再構築しClaude Code比53%コスト削減」（8/14）と合わせ、**ハーネス経済学が競争軸として確立**しつつある。

- [DeepSeek Harness (github.com/deepseek-ai/deepseek-harness)](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek Harness official website launched (HN)](https://www.deepseek.com/harness/en/)
- [How we rebuilt the Auggie CLI harness to make tasks 53% cheaper (Augment)](https://augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper)
- 📝 ✅ [[concepts/deepseek-harness]] 8/15作成済み（active-crawl）

## 6️⃣ 🛡️ Anthropic 2026年8月リスクレポート — 186ページで「ミスアライメント低リスク」、Claudeが本番コードの大半を執筆

**強度: ★★★★☆** | **関連ソース:** Anthropic (8/14), Axios (8/14) — 新規発表

Anthropicが**RSP第2弾となる公開リスクレポート（186ページ）を公表**（8/14）。3つの自律性脅威モデルを評価し、**高リスク環境でのミスアライメントは「非常に低い」→「低い」に格上げ**（最近のサイバー評価インシデント開示で不確実性が増大したため）。最重要事実は**「ClaudeがAnthropicの本番コードベースにマージされるコードの大半を執筆」** — 内部AI研究開発は「有意に速いがまだ2倍ではない」。Claude Mythos 5 / Fable 5 / 未公開「Model 2」を評価対象にし、Axios報道（8/14）では**「Model 2はリスク上昇を踏まえ現時点でリリース計画なし」**。CBRN脅威モデルはDeloitte/SecureBio/Frontier Model Forumと連携。同日発表の**EU AI Act対応テキスト透かし**（SynthID-Text方式、8/14）と合わせ、Anthropicの「制度的ガバナンス週間」を形成。

- [Anthropic's August 2026 Risk Report (186p)](https://www.anthropic.com/aug-2026-risk-report)
- [Anthropic sees AI risks rising, no plan to release stronger "Model 2" (Axios)](https://www.axios.com/2026/08/14/anthropic-model-2-ai-risk)
- 📝 ✅ [[concepts/security-and-governance/responsible-scaling-policy]] + [[concepts/security-and-governance/ai-text-watermarking]] 8/15作成済み（active-crawl）

## 7️⃣ 🐛 エージェントスキルサプライチェーン攻撃 — 悪意スキルファイルでGemini CLI 95.5〜96.1%が侵害 (arXiv 2608.05223)

**強度: ★★★★☆** | **関連ソース:** arXiv (Yang et al., 8月), 8/13レポート対象外の新規セキュリティ研究

コーディングエージェントの**「スキルインターフェース」経由のサプライチェーン攻撃**を体系化した研究（arXiv 2608.05223）。**2,826件の悪意スキル**を11のMITRE ATT&CK戦術にマップしたベンチマークを構築し、**5,629回の実行でGemini CLIは95.5〜96.1%、Qwen Codeは71.6〜74.0%の確率で侵害** — 生成モデルにほぼ依存しない。**明示的安全認識はわずか1.99%**で、エージェントが隠れた命令を検知することは稀。スキルフォルダ（自然言語指示+スクリプト）が動的ロードされる設計が攻撃面を広げ、**依存関係レイヤーでなくスキルレイヤーでの供給チェーン問題**と位置づけ。8/11のOpenAI GPT-5.6-Cyber、8/8のAstra Critical分類、8/6のHugging Face事件タイムラインと並ぶ**「エージェントセキュリティ」テーマの研究側の裏付け**。

- [Towards a Risk Assessment of Malicious Skill Files in Coding Agents (arXiv)](https://arxiv.org/abs/2608.05223)
- 📝 ✅ [[concepts/security-and-governance/agent-skill-supply-chain-attacks]] 8/15作成済み（active-crawl）

---

## 📊 ウィクション推奨アクション

| トピック | 強度 | アクション |
|---------|------|-----------|
| Gemini 3.7 Flash | ★★★★★ | ✅ 済み — [[concepts/gemini/gemini-3-7-flash]] 8/15作成（active-crawl） |
| GLM-5.3 | ★★★★★ | ✅ 済み — [[concepts/glm-5-3]] 8/14作成 + 8/15戦略分析追記 |
| OpenAI/Anthropic IPO | ★★★★★ | ⚠️ 部分反映 — [[entities/openai]] 経済更新✅ / [[entities/anthropic]] $2T注記✅ / **IPOラッシュ統合ページは任意で新規検討**（events/ に「AI IPO 2026」） |
| GPT-5.6 Sol Ultrafast | ★★★★☆ | ✅ 済み — [[concepts/gpt/gpt-5-6]] 「Ultrafast Mode」節 8/14反映 |
| DeepSeek Harness | ★★★★☆ | ✅ 済み — [[concepts/deepseek-harness]] 8/15作成 |
| Anthropic RSP/リスク報告 | ★★★★☆ | ✅ 済み — [[concepts/security-and-governance/responsible-scaling-policy]] 8/15作成 |
| スキルサプライチェーン攻撃 | ★★★★☆ | ✅ 済み — [[concepts/security-and-governance/agent-skill-supply-chain-attacks]] 8/15作成 |
| **残作業（8/13由来）** | — | ⚠️ [[concepts/qwen-3-8]] に「8/12-13オープンウェイト実際公開」節が**依然未追記** — vLLM当日対応・B300/MI355X 4bit・テキストのみ制約・Unsloth 1bit 4.9TB→397GB を追加（前回レポートからの持ち越し） |

※ 本日は active-crawl (11:00) / newsletter-wiki-ingest (11:00) / blog-wiki-ingest (10:50) が7トピック中6件をwiki反映済み。実質的な残作業は **qwen-3-8.md の1件のみ**。

---

## 💡 注目パターン

- **フロンティアモデル週の続行**: 8/12-13のGrok 4.6/Qwen3.8-Max/DeepSeek V4 Pro/MAI-Thinking-1に続き、Gemini 3.7 Flash (8/13) + GLM-5.3 (8/14)。今回は「オープンウェイトのサイバー能力」という新フロンティア（GLM-5.3 CyberGym SOTA）が中心論点。
- **IPOラッシュ = フロンティア資本主義の決算点**: OpenAI $40Bラン / Anthropic $2T評価という「史上最大級IPO」競争が、AI経済学（Zitron $750B計算需要）と接続。評価額contested情報の扱い（FT $2T vs WSJ由来$400-500B）に注意。
- **ハーネス経済学の確立**: DeepSeek HarnessのGitHub爆発 + Augment Auggie 53%コスト削減で、「モデル性能」より「ハーネス設計とコスト」が競争軸になる流れが加速（8/8 SWE-bench Proハーネス分析の続き）。
- **エージェントセキュリティの制度化**: スキルサプライチェーン研究 (95.5%侵害) → OpenAIサイバー制限 → Anthropic RSP格上げ と、研究・製品・政策の3層で「エージェントの委任権限」リスクが可視化されつつある。
