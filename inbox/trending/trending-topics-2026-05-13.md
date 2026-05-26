# トレンドトピックレポート — 2026-05-13

> 生成: 2026-05-13 12:00 UTC
> ソース: Web検索（4クエリ）、Blogwatcher DB（直近3日間のRSS記事）、Wikiログ分析
> RSS記事数（直近3日間）: 121件（25ブログ） | AI関連: 31件
> Wikiカバレッジ: 8トピック中5トピックがWiki未カバー

---

## 🔥 Google I/O 2026: GeminiがAndroidの中核へ — AppleのAI再起動前の布石

**NJ: 5/5 | 日付: 2026-05-12 | 出典: CNBC, Google公式**

Googleが5月12日、Androidを「オペレーティングシステムからインテリジェンスシステムへ」移行する計画を発表。Geminiが画面のコンテキストを理解し、ショッピングカート構築や予約といったマルチステップタスクを完了できる。メインキーノートは5月19-20日（Mountain View）。AppleもGeminiを採用してAI戦略を再起動する中、GoogleはAndroidで自前のパーソナルAIの優位性を証明しようとしている。

- Sameer Samat（Android責任者）：「人間は常にループ内にいる」と明言
- Aluminium OS、Android XRスマートグラスも発表予定
- Google I/O 2026でGemini 3.1新モデル、エージェンティックツール群の拡張が期待される
- AlphabetはNvidiaを超えて時価総額世界一目前（Reuters）

**Wikiカバレッジ**: ❌ 未カバー → `events/google-io-2026.md` と `concepts/gemini-android-intelligence.md` 作成推奨

**Wiki関連**: [[entities/google]]（既存、アップデート推奨）

---

## 🔥 Anthropic「Dreaming」— 自己改善型AIエージェントが登場

**NJ: 5/5 | 日付: 2026-05-08 | 出典: Business Insider, Anthropic, Marketing Profs**

Anthropicが新AIエージェント技術「Dreaming」を発表。自律システムが過去の行動をレビューし、パターンを特定し、セッション間で将来のパフォーマンスを向上させる。研究プレビューとしてスタートし、長期間にわたる自律ワークフロー（コーディング、金融、法律）を処理可能なマネージドエージェントの基盤技術。

- サブエージェントの調整とルーブリックベースの評価ツールもパブリックベータ拡大
- 2026年5月初旬のAnthropic最大の1週間（$200B Google Cloud契約、SpaceX Colossus 1契約など）の一環
- Claude Code Auto Mode、Claude Agent SDKの全外部デベロッパー開放と同時期
- Dario Amodei：「成長率が高すぎて手がつけられない」

**Wikiカバレッジ**: ❌ 未カバー → 新規 `concepts/anthropic-dreaming.md` 作成推奨

**Wiki関連**: [[entities/anthropic]]（アップデート推奨）、[[concepts/managed-agents]]（既存）

---

## 🔥 OpenAI DeployCo — $4B エンタープライズAI展開会社の設立

**NJ: 4/5 | 日付: 2026-05-11 | 出典: OpenAI Blog, Investing.com, Marketing Profs**

OpenAIが5月11日、**The Deployment Company（DeployCo）** を正式発表。PEファンドから$4Bを調達し、エンタープライズ向けAI展開サービス（データ統合、ワークフローカスタマイズ、ガバナンス、運用実装）を提供。Anthropicも同様のイニシアチブで$1.5Bを確保。

- 「エンタープライズAI導入には手厚いデプロイ作業が必要」という認識の具体化
- OpenAIの年換算収益は$25B超、Anthropicは$19Bに迫る
- 数ヶ月前は「モデルがすべて」だったが、今はデプロイメント企業の買収競争に
- 「AIの導入支援」が新たな大型ビジネスカテゴリに

**Wikiカバレッジ**: ❌ 未カバー → 新規 `concepts/openai-deployment-company.md` 作成推奨

**Wiki関連**: [[entities/openai]]（アップデート推奨）、[[entities/anthropic]]（アップデート推奨）

---

## 🔥 Subquadratic $29M — 12Mトークンコンテキストの新アーキテクチャ

**NJ: 4/5 | 日付: 2026-05-05 | 出典: Substack (Future AGI), Subquadratic公式発表**

Subquadratic社が$29Mのシード資金調達を発表。SubQというsubquadratic sparse attentionを持つLLMを開発中で、標準TransformerのO(n²)アテンションを超える12Mトークン（1200万トークン）のコンテキストウィンドウを実現。長文脈エージェントにはsubquadratic attentionがアーキテクチャ上の必須要件という主張。

- 標準TransformerのアテンションはO(n²) vs SubQはsubquadratic
- 12MトークンはClaude Opus 4.7の1Mトークン、GPT-5.5の2Mトークンを大きく超える
- 「本当の長期間エージェント」のアーキテクチャ基盤として位置づけ
- LK-99論争のような誇大広告には注意が必要だが、技術的には注目

**Wikiカバレッジ**: ❌ 未カバー → 新規 `concepts/subquadratic-attention.md` 作成推奨

**Wiki関連**: [[concepts/long-context]]（既存）、[[concepts/reasoning]]（既存）

---

## 📊 中国オープンモデルがフロンティアに並ぶ — GLM-5.1 / MiniMax M2.7 / DeepSeek V4

**NJ: 3/5 | 日付: 2026-05-01～12 | 出典: BentoML, HuggingFace, Substack (Future AGI)**

4つの中国ラボ（Z.ai GLM-5.1, MiniMax M2.7, Moonshot Kimi K2.6, DeepSeek V4）が12日間のウインドウでオープンウェイトのコーディングモデルをリリース。いずれもエージェンティックエンジニアリングのベンチマークでWestern frontierと同等以上、推論コストは1/3以下。

- **DeepSeek V4-Pro**: 1.6TパラメータMoE（49B active）、1Mトークンコンテキスト、MITライセンス
- **DeepSeek V4-Flash**: 284B（13B active）、GPT-5.5比34倍安い出力コスト
- **GLM-5.1**: 744B MoE（40B active）、数百ラウンドにわたって持続的に改善
- **MiniMax M2.7**: 自律的にエージェントハーネスを構築しRL実験を実行
- 4つのモデルすべてMITまたはApacheライセンス

**Wikiカバレッジ**: ⚠️ 部分的 — DeepSeek V4のエンティティページは存在するが、GLM-5.1とMiniMax M2.7はカバーなし

**Wiki関連**: [[entities/deepseek]]（既存）、[[concepts/open-source-models]]（既存）

---

## 📊 Voice AIの「Her」モーメントに近づく — TTSがLLM化する

**NJ: 3/5 | 日付: 2026-05-07～12 | 出典: AI Engineer, OpenAI Blog, Together AI Blog**

Voice AI分野が急加速。AI Engineerが3日連続でVoice AIセッションを開催（TTSモデルがLLM化、Voice AIのHerモーメント、チャットエージェントに音声を）。OpenAIが低遅延音声モデルをAPIで提供。Together AIが600+ボイスから選択可能なVoice Finderを発表。

- MistralのSamuel Humeau：「TTSモデルがLLMのように振る舞い始めている」
- Gradium AIのCEO：「Voice AIの『Her』モーメントはいつ？」
- OpenAIが低遅延音声AIのスケーリング技術を公開
- エージェントに音声が加わることで、UIのパラダイムが変わる可能性

**Wikiカバレッジ**: ❌ 未カバー → 新規 `concepts/voice-ai.md` 作成推奨

**Wiki関連**: [[entities/openai]]（アップデート推奨）

---

## 📊 ダークファクトリー: OpenClawがコードレビュー不要でデプロイ

**NJ: 2/5 | 日付: 2026-05-12 | 出典: AI Engineer (Vincent Koc), Arcturus Labs**

Vincent KocがAI Engineerカンファレンスで「Dark Factory: How OpenClaw Ships Faster Than You Can Read the Diff」を発表。OpenClawの自律的なコード生成・テスト・デプロイパイプラインが、人間のコードレビュー速度を超えたことを報告。Arcturus Labsも「Twin SunがDevパイプライン全体を自動化」と同様の事例を公開。

- OpenClawが自動生成したコード行数が人間のレビュー能力を超える「ダークファクトリー」状態に
- コードレビューの役割が「チェック」から「事後監査」へシフト
- Pi（OpenClawコーディングエージェント）を製品に組み込む方法も別セッションで発表（Tavon社）
- サブエージェントがサブエージェントを生成するループが現実に

**Wikiカバレッジ**: ❌ 未カバー → `concepts/openclaw-autonomous-pipeline.md` 作成推奨

**Wiki関連**: [[entities/openclaw]]（既存）、[[concepts/coding-agents]]（既存）

---

## 📊 統計サマリー

- **RSSスキャン**: 直近3日間で121記事（25ブログ）、うちAI関連31件
- **今日発見された記事**: 80件（21ブログ）
- **最大記事数ブログ**: Arcturus Labs（16）、AI Engineer（15）、simonwillison.net（12）
- **OpenAI News**: 直近7日間で40+記事（Codex, DeployCo, GPT-5.5-Cyber, Voice API等）
- **Wikiカバレッジギャップ**: 主要8トピック中5件が未カバー
- **既存Wiki関連ページ**: [[entities/anthropic]], [[entities/openai]], [[entities/google]], [[entities/openclaw]], [[entities/deepseek]], [[concepts/harness-engineering]], [[concepts/managed-agents]], [[concepts/coding-agents]]

---

## 推奨アクション

1. **作成推奨（高優先度）**:
   - `events/google-io-2026.md` — Google I/O 2026プレビュー
   - `concepts/anthropic-dreaming.md` — 自己改善型エージェント
   - `concepts/openai-deployment-company.md` — DeployCo
   - `concepts/voice-ai.md` — Voice AI分野
   - `concepts/subquadratic-attention.md` — SubQ

2. **更新推奨**:
   - [[entities/anthropic]] — Dreaming, $200B Google Cloud契約, SpaceX Colossus 1
   - [[entities/openai]] — DeployCo, GPT-5.5-Cyber, Codex急拡大
   - [[entities/google]] — I/O 2026プレビュー, Gemini X Android統合
