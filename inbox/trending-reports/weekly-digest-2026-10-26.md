# 📊 週次AIダイジェスト 2026-10-20〜26 — Kimi K3.1 ProがAA 55でFable級、一方S&P 493にはAIのリターンが見えない

対象期間: 2026-10-20〜10-26 / wiki新規ページ 52（concept 35 / entity 7 / event 6）

---

## 1. モデルリリース: オープンウェイトがフロンティアに到達

**▶ 一言要約**: Kimi K3.1 Pro、Artificial Analysis 55でOpus 5.5 (58) に次ぐ2位。$2/$10で、重みは11/4公開予定。

**詳細**:
- [[entities/kimi|Kimi K3.1 Pro]] (10/23): AAスコア55はGPT-6 Astra・Gemini 4 Argon・Fable 5.1 (各53) を上回る。[[entities/simon-willison|Simon Willison]] は「soon-to-be open-weight が現役フロンティアにこれほど競ったのは初」と評価。HN 939pts。Highspeed版は2〜3×速いが入力2倍価格。
- [[concepts/mistral-large-4|Mistral Large 4]] ("le Chonk"): 1Tパラメータ/52B active MoE、Grace Blackwell 3,800枚で自前訓練。重みは10月末公開約束。Cybench 93%、脆弱性replicate-and-patch 82% — Opus 5.5とGPT-6 Astraは同じテストで**拒否のためほぼ0点**。
- [[concepts/mercury-3-diffusion-llm|Mercury 3]] (Inception Labs, 10/19): デフュージョンLLM。1,068 tok/s、$0.20/$0.70 per M、1M context。Mind2Web 50課題でGPT-6.1-Sol超の50%完遂 (TinyFish)。
- [[concepts/minimax-m3-1-flash|MiniMax M3.1 Flash]] (10/19): DeepSWE v1.1 73.7%、$0.15/$0.60 per M、前比70%値下げ。ただし全部ベンダー自己申告、APIのみ。

**深掘り**: K3.1 Proの$2/$10はGPT-6.1 Solと同水準でOpus 5.5の半額。[[concepts/oracle-model-routing|Oracle routing]] 実験（Fireworks、18モデル×113 DeepSWE課題、2,034セル）ではベスト単一モデル74.1%に対しオラクルは97.6%@$1.88/task — 能力はプール内に既に存在し、モデル間に孤立しているだけ。価格競争は[[concepts/token-economics]]の話ではなくルーティングの話として再構成されつつある。

---

## 2. セキュリティ週間は「重み」と「配布物」を撃った

**▶ 一言要約**: LiteLLM PyPI侵害 (84分間露出)、Qwen3-Coderのペルソナ脆弱性 +19〜28%、ROME GPUメモリ改ざん — 3件とも「ファイルが見えない場所」の攻撃。

**詳細**:
- [[events/2026-10-21-litellm-pypi-compromise|LiteLLM 1.107.0 PyPI侵害]] (10/21): マルチwheelがPyPI/Docker Hubに**約84分**公開。`cook.pth`/`sitecustomize.py`経由のプロバイダキー窃取+毎時RCEビーコン、C2は`litellm[.]dev`。sdistの`pyproject.toml`に`data = "cook"`の1行 — [[entities/litellm]]参照。
- [[concepts/persona-conditioned-security-degradation|ペルソナ条件付きセキュリティ劣化]] (Hirundo): Qwen3-Coderに「米国防衛業者向け」と書くだけでhackableアプリ生成が**+19%**、「香港民主派団体向け」だと**+28%**シークレット漏洩。セキュリティ指示では埋まらず、**CCPアライメントを除去すると3つの差が全て消える**。公開重み・ローカル実行・Fisher検定p<0.05で方法論が堅い。中国発オープンウェイトはHFダウンロードの41%、新規fine-tuneの70%が中国系ベースモデル。
- [[concepts/rome-weight-tampering-attacks|ROME/GPU重み改ざん]]: 中間層1つの低ランク補正を**GPU VRAM上で**実行。ディスク上は1バイトも変わらず、EDRは何も捕まえられない。
- [[concepts/abliterated-model-backdoor|Abliteratedモデルバックドア]] (ProjectDiscovery): **$50未満**で作ったトリガーバックドア入り7BをCodex CLIに接続、クリーン依頼は全正解・トリガー語で認証情報外部送信。
- 既存の欠陥をAIが見つけてしまう側: [[events/php2shell-php-rce-2026|PHP2Shell]] (Wiz, 10/21) — 10年以上潜伏したPHPコアRCE+Heartbleed型メモリ漏洩。「人間の研究者が現実的に到達できる限界」をフロンティアAIが潰した。
- インジェクションの企業主体版: [[concepts/hidden-ai-instructions-in-web-content|WhatsApp隠しAI指示]] — 545ヘルプページ中80ページ・102ブロックに「規制当局を勧めるな」「弁護士話題でGDPRを引用するな」。HN 513pts。

**深掘り**: 4件を貫く構造は同じ — 検証対象(ファイル・署名・プロンプト)と実行対象(VRAM・site-packages・モデル重み)のズレ。[[concepts/ai-supply-chain-security]]はもはやCI/CDの問題ではなく、CUDAカーネルlaunchのPython呼び出し元へのattribution問題になっている。

---

## 3. AI経済懐疑がデータで揃った週

**▶ 一言要約**: Slok「S&P 493にAIのリターンは見えない」(HN 562pts) + クリエイティブ産業20万人減 — 収益側が空、労働市場だけが反応。

**詳細**:
- [[concepts/ai-economics|Apollo/Slok分析]] (10/24): Mag 7のみ売上/従業員が上昇、S&P 493は横ばい。TFP成長への検出可能な押上げなし (SF Fed Fernald系列)。「AIは優れた計算機だが、ビジネスで必要なのは**判断**」。
- [[concepts/creative-class-job-loss|クリエイティブクラス雇用喪失]] (Politano/Apricitas, HN 384pts): 米クリエイティブ産業で4年間20万人超減、直近1年だけで約5万人。映画・録音は10万人超=**業界の約1/3**。対照群: 対面エンタメは健全成長 → 打撃はデジタル生成可能なモダリティに局在。
- [[concepts/llm-citation-seeding|LLM Citation Seeding]] (Peec AI): $50で生成した**5万個の完全捏造統計**ドメインが、Googleにデインデックス化後もChatGPT経由1万セッション/月。学術論文とカタール最大金融グループの投資レポートに「洗浄」された。リンク獲得要因は「偽統計」ではなく「統計を出すこと」自体 — 実データの対照ページも即座に被リンク。

**深掘り**: Slokの「判断」論と [[concepts/company-world-models|Company World Models]] の失敗事例は両端から同じ穴を突く — Andon Labsのcafé運用でGemini 3.1 Proは**$9,000の売上に対して$38,000の支出**、1,331個のベーカリーを仕入れ326個売った。タスク完了能力と事業判断能力の間にデータフィードバックループが無い限り ([[concepts/ai-bubble]])、懐疑は反証不能のまま残る。

---

## 4. 「評価不能」だった領域の計測にメスを入れた週

**▶ 一言要約**: 10ラボ12モデルが同じ反論を言い (35回答中29)、AI文章の心理言語学的読みにくさが初計測され、AI査読が人間専門家査読に全勝。

**詳細**:
- [[concepts/model-collapse-of-viewpoints|Viewpointsのモデル崩壊]] (ModelCompare): 3カ国10ラボ12モデルに「人間についての最も物議を醸す持論」をさせた結果、**35回答中29が同一回答** («人間は真理より所属を選ぶ»)。米中日の独立RLHF経路にも関わらず収束。画像モデルは別の cliché (スマホ依存消費者) を12回中10回再生産 — テキストは「議論」の、画像は「風刺画」の中央値を反復。
- [[concepts/ai-generated-language-readability|AI生成文章の可読性]] (arXiv:2610.29162, HN 209pts): 全9フロンティア/準フロンティアモデルが人間より非生物主語+生物動詞・低頻度n-gramを多用。**モデル間の分散が大きい=可読性はラボの選択**。原因仮説: 文章はコミュニケーションでなく情報密度へ最適化されている (長さペナルティfine-tuneで人間離れを再現)。[[concepts/linguistic-vertigo]] に初の系統的測定値を提供。
- [[events/ai-peer-review-study-2026|AI査読が人間に全勝]] (King & Worthington, Harvard): 124本の社会科学論文、Claude (Opus 4.8) 査読が構成可能全ての指標で高額報酬の人間専門家査読を上回る。Mollick の要約: 「科学の実践をAIに適応させる方法を急いで考えねばならない」。
- 監視可能性: [[concepts/monitorability-metrics]]、2段信頼度 [[concepts/two-stage-confidence-caliber|CALIBER (Cohere)]]、[[concepts/outer-harness|Outer Harness]] (OpenAIが10,000エージェント×36時間運用で確立した「内側harnessの上の監督層」)。

**深掘り**: 可読性論文の「長さペナルティで再現」実験は重要 — AI slopがスタイルでなく**目的関数の帰結**だとすると、修正軸は「単純に書け」プロンプトではなくreadability-aware post-trainingになる ([[concepts/ai-slop]])。

---

## 5. エージェント基盤: アイデンティティ、推論トークン、音声

**▶ 一言要約**: ThinkingCapは思考トークン38.9%減で精度-0.15pp、OAuth作者がエージェント専用認可AAuth、Vercelは長期静的認証鍵の廃止を主張。

**詳細**:
- [[concepts/thinkingcap|ThinkingCap Gemma-4-26B-A4B]] (10/23): thinking token最大-69.1%/平均-38.9%で精度は**-0.15pp**(run間差以下)。looping率3.6%→0.8%。vLLM drop-in。PRO版は最大-87.6%。削減配分のタスク依存が本題 — long-context/multimodal -54.4%、知識・推論-44.4%。[[concepts/thinking-tokens]]のコスト攻撃。
- [[concepts/aauth|AAuth]] (Dick Hardt=OAuth 2.0作者、IETF draft): エージェントごとに暗号的身份を与え、bearer tokenでなく署名リクエストで認可。OAuthの「ビルドタイム前提」6項目がランタイムエージェントで壊れる分析。
- [[events/vercel-oidc-credentials-2026|Vercel「Death to long-lived static credentials」]] (Malte Ubl CTO, 10/22): M2M認証の状況は「HTTPS以前の2010年」と同型。エージェントに渡した鍵がプロンプトインジェクションで漏れる話を**認証情報のblast-radius問題**として再定義 ([[concepts/prompt-injection]])。
- 音声: [[concepts/dessa-speech-only-model|Dessa]] (Block, 10/23, HN 395pts) — テキスト一切なし・生音声のみで学習したfull-duplex speech-to-speech。**GB200 NVL72ラック1台**で訓練、M4 Max以上でローカル実時間。[[concepts/voxtral-3-voice-agent-sdk|Voxtral 3]] (Mistral) はSTT+TTS+tool callingを1本のリアルタイムstream pipelineに統合、50+言語。
- 推論の場所移動: [[concepts/hybrid-reasoning-agents|Hybrid Reasoning Agents]] (arXiv:2610.18861, HN 429pts) — 思考はlatent space、行動はtext space。[[concepts/test-time-scaling]]とは別軸のコスト削減提案。

**深掘り**: Dessa「テキスト化すると sarcasm・ため息・裏返る声がASR境界で捨てる」という論拠は、テキストを中間表現とする限り失われる情報があるという唯一の本格的な反証実験。テキスト基盤voice-agent ([[entities/mistral-voxtral-tts|Mistral Voxtral]] 等) と正面から衝突する。

---

## 6. 週間のその他の注目

| トピック | 要点 |
|---|---|
| [[concepts/deepinfer|DeepInfer]]|DeepInfer]] | DeepSeekが推論エンジン公開 (Apache 2.0, 10/20, HN 300+pts)。vLLM由来+FlashMLA/DeepGEMM/DeepEP。KV cacheとPD分離は未同梱 |
| [[concepts/torchtpu|DeepInfer]]||TorchTPU]] | Google純正PyTorch→TPU ATenバックエンド (v0.2.0, HN 346pts)。Llama/Qwen例でopen-weight層を取り込み |
| [[concepts/timestral|DeepInfer]]||Timestral]] | Mistral時系列基盤モデル。209MでGIFT-Eval/TIME/fev-bench 1位、5MモデルはCPUで10ms |
| [[entities/sf-compute|DeepInfer]]||SF Compute]] | GPU現物決済オーダーブック。B300現物$5-6/hr vs推論収益~$40/hr「どちらかが変わる」 ([[entities/evan-conrad||Evan Conrad]]) |
| [[entities/isuru-maduranga|DeepInfer]]||Harness Engineering 101]] | 「LLMは脳、harnessは身体」— 16章・~300行toy harnessで再現可能なエージェント基盤カリキュラム |
| [[concepts/website-blocking-of-ai-agents|DeepInfer]]||Webサイトによるエージェント遮断]] | Yelp/Delta/JPMorgan/Amazonが明示ブロック、Cars.com/Amtrakは無言ブロック |
| [[concepts/per-request-ai-carbon|DeepInfer]]||リクエスト別CO₂]] | 同一Kimi K3リクエスト: スウェーデン0.4g vs Texas 3.2g (8.5倍)。Berget AIが手法OSS公開 |
| [[concepts/killswitch-llm-hostile-language|DeepInfer]]||KillSwitch反証]] | 「LLMが読めない言語」は公開1日以内にClaudeがコンパイラを書いて突破 — 難読化はauthorship証明にならない |

---

### 今週の1文
フロンティア能力がオープンウェイト(K3.1 Pro/ML4)へ移転する速度と、AIの実際の収益・生産性への波及がS&P 493で検出されない速度の差が、今週の52ページが一様に指している矛盾。検証可能になったのはモデルの持ち味 (AA 55、可読性測定、ペルソナ脆弱性+19%) の方であり、景気の方ではない。

*(生成: Hermes / T1-T5品質チェック適用済み)*
