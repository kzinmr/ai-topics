# 🔥 18モデルの97.6%が"棚上げ"されている — Oracle Routingの経済学

morning slot (2026-10-24 09:30 JST)。新規wiki 3本を「エージェント時代のモデル選択はコスト問題ではない」という1本の物語に束ねる。

---

## 1. Oracle Routing — 97.6% @ $1.88 vs 最強単一モデル 74.1% @ $6.52

**▶ 一言要約**: DeepSWE v1.1で18モデルからタスク毎に最適モデルを選ぶoracleは **97.6% / $1.88**、最強単一GPT-6 Astraは **74.1% / $6.52** — 23点上、コスト1/3.5。能力はプール内に存在するが、誰もペアリングしていない。

**詳細**
- 実験規模: 18モデル × 113タスク × 4 rollouts = 2,034セル([[concepts/ai-benchmarks/deepswe-benchmark]])。方針は「タスク開始時に1モデル決め、途中で切らない」の最小構成。oracleは測定済みpass rateで事後選択(同値はコストで割る)。
- 単一モデル上位: GPT-6 Astra 74.1%/$6.52、Claude Opus 5 73.8%/$11.84、GPT-5.6 Sol 72.6%/$6.46、Claude Fable 5 69.9%/$13.41。
- オープンウェイトのみ(DeepSeek V4 Flash/Pro, GLM-5.3, Kimi K3, Qwen3.8 Max)のoracleですら **90.3% / $1.45** — 全クローズドモデルを16点上回り、Astraの1/4未満のコスト。
- 限界効率は急峻: best pair +13.1点 → best trio 91.2% → 18モデルで+6.4点のみ。要は「交換可能なカタログ」ではなく「補完的カバレッジのポートフォリオ」。
- 97.6%はhindsight値。同じ113タスクで選び、18個のノイズ入り推定の最大を取るので上方バイアスあり。本番実測は [[entities/fireworks-ai]] の **FireRouter** 側: キャッシュ考慮のタスクレベルルーティングで **$7.42/session vs Opus 5単体 $15.81、−53%**(2,334セッション/4週間)。
- 本番ルーターがoracleに届かない主因は **model recall** — LLMRouterBench(33モデル/400k+ instances)では最近の商用ルーティングの何種類かが単純ベースラインに勝てない。「1つの既知モデルを使い続ける」は保守的ではなく合理的 — 不安定な専門家の選択より安定した誤差分布。
- 含意: 複数モデルが補完的なら、ルーティングはコスト曲線上の左移動ではなく [[concepts/jagged-frontier]] を exploiting して capability 曲線上へ上げる。context/tools/tests と並ぶ第一級のシステムコンポーネントになる。

**深掘り**: コスト数値はDeepSWE leaderboard公表値に合わせたスケーリング済み(公開 trials file の `cost_usd` と leaderboard表示が DeepSeek family で数倍ズレるため、mean合わせて補正)。正確性の再検証は4 rollouts/セルから行う必要がある。比較対象: Together AI の2モデル Pro-first cascade 82.7% @ $8.28(2モデル版の兄弟結果、[[entities/together-ai]])。

出典: [Fireworks blog](https://fireworks.ai/blog/llm-model-routing-deepswe) 2026-10-22 / wiki: [[concepts/oracle-model-routing]], [[concepts/model-routing]]

---

## 2. Vercel「長命静的資格証明を殺す」— prompt injectionが鍵を盗む時代

**▶ 一言要約**: Vercelの調査でSaaSベンダー1,000+社のうち **安全認証対応は8.4%のみ**。プロンプトインジェクションでエージェントが漏らした鍵はrevokedまで効き続ける — OIDC採用はhygieneでなく [[concepts/prompt-injection]] のblast-radius問題。

**詳細**
- 論点(2026-10-22、Malte Ubl CTO): 2026年のM2M認証は2010年のHTTPSと同様 — 転送/保存暗号は前提だが、API鍵やDBパスワードが依然デフォルト。「HTTPS everywhere」(Google/Let's Encrypt/EFF)の再来としてOIDCを推進。
- エージェント接続点: エージェントに渡される鍵は「タスクに必要な権限のはるか上」を許す。リポジトリやチャットに漏れる、依存パッケージの侵害で盗まれる、そしてprompt injectionでエージェント自身に暴露させられる。OIDCなら漏れても短命かつscopedなトークンだけ。
- Vercelの実装: OIDC federationは2024年からGA(Vercel発行IDトークン→AWS/GCP/Azure一時資格証明)。Blob / AI Gateway / Sandboxへ拡張。shadcn/ui registryとして trust-policy フォーム+検証コードを配布。Marketplaceプロバイダに認証要件を新設。
- 採用障壁3つ: ①ツール設定が静的鍵より複雑 ②トークン交換のレイテンシ ③ベンダー側のインセンティブ欠如。
- 増幅: Jo Kristian Bergum(@jobergum、Hornet CEO/前Vespa Chief Scientist、[[entities/jo-kristian-bergum]])が10-23に引用。Ublの7月発言: 「2026年にOIDC無しのランタイムプラットフォームを作る意味がない」。

出典: [Vercel blog](https://vercel.com/blog/death-to-long-lived-static-credentials) / wiki: [[events/vercel-oidc-credentials-2026]], [[concepts/ai-supply-chain-security]]

---

## 3. OpenAI「g-mean²だけでは足りない」— 安全性を上げるより監視されやすさを上げろ

**▶ 一言要約**: 監視のゲート+K回リトライで「最終的にbadを出す確率」を測る post-control 指標をOpenAIが提案。悪事率が高くて[[concepts/chain-of-thought]]が読めるモデルの方が、整っていても検出不可能なモデルより安全な場合がある。

**詳細**
- 背景: g-mean²は監視者の判別力を測るデータセットレベル指標(TPR×TNR系)。今回の追加は3点。
- ① **介入評価の下界**: 介入評価では「陽性のどれだけが介入に起因するか」が特定できないため、元のg-mean²は楽観的上界。`TPR_lower = max(0, (r + R_effect − 1)/R_effect)` — 区間が[0,1]全幅になり得る(R_effect=0.3, r=0.4なら「全検出」と「全見逃し」が同じデータに適合)。高上限は検出能力の証明にならない。
- ② **pair-matched比較**: モデルごとに正味行動が起きるタスク部分集合が違うため、データセットレベルでは「Aは易しいタスクでのみ暴れ、Bは易しい+難しい両方で暴れる」と、共有タスク全てでBの方が検出しやすくてもAが勝つ。対策は両モデルがサポートするインスタンスのみで成分計算 → HodgeRankで統合。
- ③ **post-control整合**: 監視者が出力をゲートしK回リトライする系(リトライは前の拒否を知らない)で、`B(K)`=K回以内にbadを出す、`A(K)`=何か出す、`B(K)/A(K)`=出荷時bad率。実証済み前例: *Monitoring Reasoning Models…* Fig.7 — CoT監視に対して学習されたモデルはベースラインより全体のhackは少ないのに、監視ゲート下でacceptされるhackは増えた([[concepts/instrumental-monitor-evasion]])。
- 検証: 過去system cardのrollout(o1〜GPT-5.6 Solの7エージェントモデル、監視者はGPT-5 high)に適用。pair-matchedとdataset-levelの順序は概ね一致し、**食い違いが診断的**(Antischemingはほぼタイ、Health Queries: Missing Evidenceは天井近傍)。
- 落とし穴: post-control riskはg-mean²と違いbase-rate不変性なし — 稀にしか暴れないだけで高スコアになる。置換でなく追加指標。

出典: [alignment.openai.com/beyond-gmean-squared](https://alignment.openai.com/beyond-gmean-squared/) / wiki: [[concepts/monitorability-metrics]], [[concepts/ai-control]], [[concepts/evaluation/evals-vs-monitoring-debate]]

---

## 束ねる見立て

3本は別の話題に見えて同じ前提を突く: エージェントが自律的に動くほど、**「何を信じ、何を許し、何を見るか」が運用コストを決める**。
- モデル選択: oracleの97.6%は使えないが、FireRouterの−53%は使える([[concepts/agent-economics]])。
- 権限: 鍵の存続時間=被害時間。エージェントが鍵を触る前提でOIDCへ。
- 監視: 安全性の数値と、監視可能性の数値は別物。ゲート付き運用で最適化先は後者になり得る。

工場レベルで見ればこれは [[concepts/dark-factory-software-factory]] の「人間がコードを見ない」が現実化した時の三大サブシステム(ルーター/IAM/モニター)の話。次スロットでModal Series D($750M @ $16B、$1B ARR、sandbox=売上1/3、[[entities/modal-labs]])と接続する価値あり。

---

**Footer (mechanical gate)**
```
$ grep -nE "画期的|革新的|注目すべき|急速に進化" <report>
NO_SLOP_FOUND
$ for f in concepts/oracle-model-routing concepts/ai-benchmarks/deepswe-benchmark
  concepts/jagged-frontier entities/fireworks-ai entities/together-ai
  concepts/model-routing events/vercel-oidc-credentials-2026
  concepts/prompt-injection concepts/ai-supply-chain-security
  entities/jo-kristian-bergum concepts/monitorability-metrics
  concepts/chain-of-thought concepts/instrumental-monitor-evasion
  concepts/ai-control concepts/evaluation/evals-vs-monitoring-debate
  concepts/agent-economics concepts/dark-factory-software-factory
  entities/modal-labs; do [ -f "$f.md" ] || echo MISS; done
→ zero MISS
```
