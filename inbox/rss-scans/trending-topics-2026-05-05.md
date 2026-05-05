# Trending Topics Report — 2026-05-05

> Generated: 2026-05-05 12:00 JST
> Source: Blog ingest (18 articles — all covered), Newsletter (7 newsletters triaged), Web research

## 🔥 1. ホワイトハウス、AIモデル事前審査の大統領令を検討 — 規制緩和から急転換

**重要度: ★★★★★ | 日付: 2026-05-04 | 出典: NYT, Forbes, Bloomberg**

トランプ政権が、AIモデルの一般公開前に政府審査を義務付ける大統領令を検討中。AnthropicのMythosモデル（自律的な脆弱性発見能力）を契機に、David Sacks（AI担当官、3月辞任）の規制緩和路線から急転換。後任のSusie Wiles首席補佐官とScott Bessent財務長官が主導。

- Anthropic、Google、OpenAIの経営陣と先週協議
- 英国のモデル審査制度を参考にした「政府AIワーキンググループ」設立を想定
- AIによる大規模サイバー攻撃のリスクが主な引き金
- Dean Ballは「米国は法律も通さずに事実上のAIライセンス制度を発明した」と指摘

**Wiki関連**: [[entities/dean-ball]]（既存）、[[entities/anthropic]]（既存）、[[concepts/agent-governance]]（既存）

---

## 🔥 2. Sierra、$950MのSeries Eを調達 — 評価額$15.8B、エンタープライズAIエージェントの覇権争い

**重要度: ★★★★★ | 日付: 2026-05-04 | 出典: CNBC, TechCrunch, Bloomberg**

Bret Taylor（OpenAI会長）とClay Bavor（元Google VP）が共同創業したAIカスタマーサービス企業Sierraが、Tiger GlobalとGoogle Ventures(GV)主導で$950MのSeries Eを調達。評価額は$15.8B（前回$10Bから60%増）。Benchmark、Sequoia、Greenoaksも参加。

- **ARR**: 8四半期で$150M超を達成 — ソフトウェア史上最速
- **顧客**: Fortune 50の40%超、Fortune 500の銀行トップ3分の1
- **Ghostwriter**: 4月に「Agent as a Service」製品発表。自然言語でエージェントを生成
- **Uberの事例**: CTO曰く、全コードの10%が自律生成。ホテル予約APIの構築が1年→6ヶ月に短縮
- **競合**: Cursor、Replitが最大の市場領域とTaylorは分析

**Wiki関連**: [[entities/sierra]]（要アップデート—$15B→$15.8B、$950M Series E詳細）

---

## 🔥 3. Jack Clark「Import AI 455: Automating AI Research」— AIが自らを構築する時代に

**重要度: ★★★★★ | 日付: 2026-05-04 | 出典: Import AI (jack-clark.net)**

Anthropic共同創業者のJack Clarkが、完全自動化されたAI研究開発（Automated AI R&D）へのテイクオフが進行中だと断言する長文エッセイを公開。

主な論点:
- AIが論文実装・実験実行・GPUカーネル最適化を自律的に行う時代に
- DeepSeekのGPUカーネル自動生成、MetaのTritonカーネル自動最適化、AscendCraft（Huawei向けカーネル生成）など具体的事例を列挙
- AIエンジニアリングの大部分はすでに自動化可能。「だが研究のうちどこまでがエンジニアリングかは不明」
- 「2026年はこの含意を解きほぐす年にする」と宣言
- 60%以上の確率で2028年までに自律型AI R&Dが実現するという自身の予測を再確認

**Wiki関連**: [[entities/jack-clark]]（既存、アップデート済み）

---

## 🟡 4. Nathan Lambert「蒸留パニック（The Distillation Panic）」—「蒸留攻撃」という用語の危険性

**重要度: ★★★★☆ | 日付: 2026-05-04 | 出典: Interconnects (natolambert)**

AI2のNathan Lambertが「蒸留攻撃（distillation attacks）」という用語の持つ政策的リスクを分析。

- Anthropicが中国の3つのラボによる「蒸留攻撃」を報告したブログ投稿に端を発する
- Lambertは「蒸留攻撃」という用語が、正当な蒸留技術とAPI悪用（脱獄・なりすまし）を混同させると警告
- 蒸留は業界標準のポストトレーニング手法であり、オープンモデルの普及に不可欠
- 中国ラボの行為は「攻撃的蒸留」ではなく「脱獄または濫用（jailbreaking/abuse）」と表現すべき
- 誤った政策対応が、学術界や中小企業によるAI活用を不当に制限するリスク
- Lambertの書籍「The RLHF Book」今夏刊行予定

**Wiki関連**: [[entities/nathan-lambert]]（既存）、[[concepts/distillation-policy]]（新規作成候補）

---

## 🟡 5. xAIのGPU稼働率わずか11% — 550K GPUの効率化問題

**重要度: ★★★★☆ | 日付: 2026-04-29〜5月 | 出典: The Information, WCCFTech**

xAIが保有する55万台のNVIDIA GPUの稼働率が約11%にとどまっていると報道。Meta（43〜46%）やGoogleに大きく劣る。

- Colossusクラスター（メンフィス、2GW、約55.5万GPU）は世界最大の単一AIトレーニング施設
- だが分散トレーニングネットワークとソフトウェアスタックが未成熟
- GPU使用パターンが「バースト的」：短時間の高負荷→結果分析でアイドル
- xAIは50%目標を掲げるが時期未定。未使用GPUのレンタルも検討
- 業界全体の課題として、GPUリッチでも効率的利用は難しいことを浮き彫りに
- 現在のGPU数: xAI 55万＞OpenAI/Microsoft 〜42万＞Google 〜28万＞Meta 〜22万＞Anthropic 〜14万

**Wiki関連**: [[entities/xai]]（既存、GPU utilizationセクション追加候補）、[[concepts/gpu-utilization-efficiency]]（新規作成候補）

---

## 🟡 6. NVIDIA、中国市場シェアゼロに — Jensen Huang「輸出規制は既に大きく裏目に出た」

**重要度: ★★★★☆ | 日付: 2026-05-03 | 出典: Tom's Hardware, Yahoo Finance, SEC 10-K**

NVIDIAのJensen Huang CEOが、中国のAIアクセラレーター市場で同社のシェアが「95%から0%に低下した」と発言。

- 米国輸出規制によりH100/H200/B200の中国向け出荷が実質禁止
- NVIDIAは第1四半期に$4.5Bの輸出規制関連損失を計上
- Huawei Ascend、Cambricon、Moore Threads、MetaXが空隙を埋める
- ソフトウェア面ではCUDAモートが依然として中国企業の課題
- バーンスタイン試算: NVIDIAの中国シェアは2024年の66%から数年後に8%に
- Huangは「市場全体を放棄することは戦略的に意味をなさない。政策は動的であるべき」と警告
- NVIDIAの10-Kでも「中国市場からの実質的な閉め出し」をリスク要因として明記

**Wiki関連**: [[entities/nvidia]]（既存、Chinaセクション追加候補）、[[concepts/ai-chip-export-controls]]（新規作成候補）

---

## 🟢 7. AIエージェント投資ブーム — Sierraの$950M調達を皮切りにエンタープライズAI市場が急拡大

**重要度: ★★★☆☆ | 日付: 2026-05-04 | 出典: Axios, CNBC**

エージェンティックAIへの投資が2025年に$24B超を記録。Sierra以外にも以下の動きが進行中:

- OpenAIの評価額が$852Bに到達（YCが0.6%=約$5B相当を保有）
- Anthropic、評価額$900Bでの資金調達を模索中（競合の調達合戦）
- PentagonとOpenAI/NVIDIA/Google/Alphabetが機密軍事利用のAI契約に署名
- Cursorの評価額$60B、SpaceXによる買収観測
- エンタープライズAIエージェントが「ソフトウェアの新しいカテゴリー」として確立されつつある
- マルチクラウド・マルチモデル時代の幕開け（OpenAI→AWSへの展開など）

**Wiki関連**: [[concepts/agent-economics]]（新規作成候補）

---

## Topics Covered in Previous Reports (No Change)

以下のトピックは5月3日〜4日のレポートで既に取り上げられており、大きな変化なし:
- DeepSeek V4 ProのNIST CAISI評価（5/1）
- CISA脆弱性パッチ期限3日への短縮検討（5/1）
- DeepSeek V4 + Huawei Ascend 950チップ調達競争（4/29〜継続中）
- Boston Dynamics経営陣離脱（5/1）
- Richard Dawkins vs Gary Marcus LLM意識論争（5/2）
- MIT「重ね合わせ現象」によるスケーリング則メカニズム説明（5/3）
- Cloudflare LLM Infra、Shadow AI Governance、ADLC、Portkey/Palo Alto（5/5）
