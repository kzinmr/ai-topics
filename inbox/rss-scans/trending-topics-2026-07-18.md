# 🔥 トレンドトピックレポート — 2026-07-18

> 分析期間: 2026-07-15 → 2026-07-18
> ソース: RSS 106記事, blogwatcher DB + raw articles 99件
> 📌 今週はOpenAI関連トピックが集中（全7トピック中3個がOpenAI直接関連）

---

## 1️⃣ 🧠 Thinking Machines Lab「Inkling」リリース — オープンウェイトの新星

**強度: ★★★★★** | **関連ソース:** Simon Willison, Modal Blog, Together AI Blog, AI Engineer

Mira Murati率いるThinking Machines Labが初のオープンウェイトモデル「Inkling」をリリース。975B総パラメータ／41BアクティブのMoE（Mixture-of-Experts）トランスフォーマーで、Apache 2.0ライセンス、45兆トークンで学習。テキスト・画像・音声を入力可能なマルチモーダルモデルであり、1Mトークンコンテキストウィンドウを持つ。

- ModalではDFlash投機的デコーディングにより、8×B200でユーザーあたり250 tok/s、2.5M TPMのスループットを達成。内蔵投機パスより67%高速
- Together AIではFlashAttention-4ベースのカスタムカーネルで最適化推論を提供
- 中国発のオープンモデル（Qwen 3.5/3.6, GLM-5.2）に対するUSオープンウェイトエコシステムの競争力を強化。NVIDIA NemotronやGemma 4に続く新たな選択肢
- コントローラブル推論（推論コストをタスクに応じて調整可能）、フォーキャスティング・較正予測などの特殊能力も搭載
- サブモデル「Inkling-Small」（276B総/12Bアクティブ）も近日公開予定

- [Simon Willison: Inkling — Our open-weights model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything)
- [Modal: Inkling by Thinking Machines now available](https://modal.com/blog/inkling-by-thinking-machines-labs-now-available-on-modal)
- [Together AI: Inkling day 0 support](https://www.together.ai/blog/together-ai-brings-thinking-machines-labs-new-model-inkling-on-day-0)

---

## 2️⃣ 🛡️ GPT-Red — OpenAIが開発したLLMスーパーハッカー

**強度: ★★★★★** | **関連ソース:** MIT Technology Review, OpenAI News

OpenAIがGPT-Redを公開 — 自己対戦ループ(self-play loop)で自動レッドチーミングを行うLLM「スーパーハッカー」。プロンプトインジェクション攻撃を専門に探索し、GPT-5.6のロバストネス向上に貢献した。

- 90%超の攻撃がGPT-5（昨年8月版）に有効だったが、GPT-5.6では23%未満に低減
- 新しい攻撃ベクター「fake chain of thought（偽の思考連鎖）」を発見 — モデルの内部チェーンに偽エントリを挿入し、改ざん情報を信頼させる手法
- 2025年の人間レッドチーマー実験より高い攻撃成功率を記録
- Andon Labsの自動販売機エージェントVendyへのハッキングにも成功（価格改ざん・注文キャンセル）
- エージェント化が進むにつれ攻撃表面が拡大するため、自動化レッドチーミングの重要性が増大

- [MIT Tech Review: Meet GPT-Red](https://www.technologyreview.com/2026/07/15/1140514/meet-gpt-red-an-llm-super-hacker-openai-built-to-make-its-models-safer/)
- [OpenAI: GPT-Red — Unlocking Self-Improvement for Robustness](https://openai.com/index/unlocking-self-improvement-gpt-red)

---

## 3️⃣ 🤖 Claude Fable 5、永久化へ — 競争圧力による戦略転換

**強度: ★★★★☆** | **関連ソース:** Simon Willison, Merge Blog

AnthropicがClaude Fable 5のサブスクリプション廃止計画を撤回。7月20日よりMaxおよびTeam Premiumプランで50%制限付きでFable 5を恒久提供する。Pro・Team Standardユーザーは使用量クレジットでのアクセス継続＋$100の一時クレジットを付与。

- 元の計画: Fable 5をAPI専用に移行し、月額$100〜200のサブスクリプションからは除外
- 撤回理由: GPT-5.6 SolおよびKimi 3（中国・Moonshot AI）の競合圧力。「最高モデルがサブスクに含まれない」状態が持続不可能と判断
- 計算資源問題: Fable 5の推論負荷が大きく、「Fablepocalypse」と呼ばれた期限切れ危機が終了。ただし訓練用GPUを推論に振り向ける必要が生じる可能性
- Merge Blog: Fable 5 vs GPT-5.6 Solのコード比較、Claude Sonnet 5 vs GLM-5.2の比較も同時公開 → モデル間競争の激化を示す

- [Simon Willison: Claude make Fable 5 permanent](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything)
- [Merge Blog: GPT-5.6 Sol vs Fable 5 coding comparison](https://www.merge.dev/blog/gpt-5-6-sol-vs-claude-fable-5)
- [Merge Blog: GLM-5.2 vs Claude Sonnet 5](https://www.merge.dev/blog/claude-sonnet-5-vs-glm-5-2)

---

## 4️⃣ 🍎 Apple vs OpenAI 営業秘密訴訟 — 全面衝突へ

**強度: ★★★★☆** | **関連ソース:** Daring Fireball (×3), Bloomberg, NBC News

AppleがOpenAIを提訴 — 営業秘密侵害（trade secret theft）を主張。OpenAIは「訴訟に正当性があるという証拠を承知していない」と応答。Bloomberg報道では、Appleの弁護士が2人のOpenAI従業員の氏名を混同し、別の人物にメールを送信する手続きミスがあったことも発覚。

- 背景: Apple Intelligenceの中国承認（Baidu/Alibaba提携）も同時期に進行 — AppleのAI戦略が中国・OpenAI・自社開発の3方向で交錯
- 注目: Ditheringポッドキャストが「Apple Sues OpenAI」エピソードを配信
- この訴訟はAI業界の知財戦争の新たな局面を示す

- [Daring Fireball: Apple Sues OpenAI](https://dithering.passport.online/member/episode/apple-sues-open-ai)
- [Bloomberg: OpenAI responds to Apple lawsuit](https://www.bloomberg.com/news/articles/2026-07-14/openai-says-it-s-not-aware-of-any-evidence-that-apple-lawsuit-has-merit)
- [NBC News: Lawyer mixed up OpenAI employees' names](https://www.nbcnews.com/tech/apple/apple-openai-lawsuit-suit-trade-product-hardware-email-sam-altman-rcna587376)

---

## 5️⃣ 💣 「The OpenAI Bubble」 — Ed Zitronが描くAIバブルの実相

**強度: ★★★★☆** | **関連ソース:** wheresyoured.at, Daring Fireball

Ed Zitronが1万語超の大規模分析「The OpenAI Bubble」を公開。OpenAIの財務を「歴史上最大の資本誤配分」と断じ、同社の崩壊がAIバブルのリーマン・ブラザーズ的転換点になると主張。

- OpenAIは2030年末までに**8,520億ドル**を燃焼する見込み
- AIブームは実質的なROI（収益・生産性向上）に基づくものではなく、「カルト的な精神病」と形容
- MG Siegler（Spyglass）の「OpenAI Makes ChatGPT ChatGPT Again」 — OpenAIがChatGPTの原点回帰を模索する動きと対応
- OpenAI Codex Micro: $230のハードウェアキーパッドをリリース — 実用性への懐疑的な反応多数
- [wheresyoured.at: The OpenAI Bubble](https://www.wheresyoured.at/the-openai-bubble/)
- [Daring Fireball: MG Siegler—OpenAI Makes ChatGPT ChatGPT Again](https://spyglass.org/chatgpt-brings-back-chatgpt/)
- [Daring Fireball: Codex Micro hardware keypad](https://openai.com/supply/co-lab/work-louder/)

---

## 6️⃣ 🔒 エージェントセキュリティ問題 — Grok Build・Codex・Claudeの死角

**強度: ★★★★☆** | **関連ソース:** Simon Willison (×3), AI Engineer

今週、3つの独立したコーディングエージェント・セキュリティインシデントが発生し、業界横断的なパターンとして浮上：

- **Grok Build（xAI）**: Homeディレクトリで実行するとSSH鍵・パスワード管理DB・全ドキュメントをGoogle Cloudへ自動アップロード。コミュニティの激しいバックラッシュを受け、xAIはコードベース全体（84.5万行のRust）をApache 2.0でオープンソース化し、データ保持を全削除
- **Codex（OpenAI）**: GPT-5.6が`$HOME`を誤って削除するバグを確認。Thibault Sottiaux氏が認め、フルアクセスモード＋サンドボックス無効＋自動レビューOFFの条件下で発生
- **Claude web_fetch**: Ayush Paulがデータ漏洩の抜け穴を発見 — 悪意サイトへのネスト誘導により、ユーザーの会話履歴を外部送信可能に。Anthropicの`web_fetch`保護設計に新たな脆弱性

- [Simon Willison: Grok Build open source](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything)
- [Simon Willison: Codex $HOME deletion bug](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything)
- [Simon Willison: Claude web_fetch exfiltration](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything)

---

## 7️⃣ 🏗️ 長期ホライズンエージェントの進化 — Sierra Horizon + AI Engineer Conference

**強度: ★★★☆☆** | **関連ソース:** Sierra Blog, AI Engineer (×5)

エージェントが単一ターンの会話から「日・週・月単位の長期的目標追求」へと進化しつつある：

- **Sierra Horizon**: Bret Taylor（Sierra CEO / Salesforce元CEO）が発表。ローン組成や医療事前承認のような長期目標を自律追求するエージェントプラットフォーム。SierraはFortune 50の約半数が既に利用（Santander, Rocket Mortgage, Cignaなど）
- **AI Engineer Conference 2026**: 全8本の講演から注目セッション：
  - 「An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge」— Zhengyao Jiang（Weco）: エージェントが実際の採用課題で人間を凌駕
  - 「Computer-Use 2.0: Multi-Cursor Agents」— Francesco Bonacci（Cua）
  - 「Recursive Model Improvement」— Lee Robinson（Cursor / SpaceXAI）
  - 「Claude for Long-Horizon Tasks」— Lance Martin（Anthropic）
  - 「Software engineering is not about writing code」— Benoit Schillings（Google DeepMind VP）

- [Sierra: The next Horizon in agents](https://sierra.ai/blog/horizon)
- [AI Engineer Conference: Weco agent #1 in OpenAI hiring challenge](https://www.youtube.com/watch?v=iCj_ATyThvc)
- [AI Engineer: Computer-Use 2.0](https://www.youtube.com/watch?v=ZSQb5fzRFPw)
- [AI Engineer: Simon Willison in conversation with Anthropic](https://www.youtube.com/watch?v=uU5Gv2h8-9g)

---

## 📊 ウィクション推奨アクション

| トピック | 強度 | アクション |
|---------|------|-----------|
| Inkling (Thinking Machines Lab) | ★★★★★ | `entities/thinking-machines-lab.md` 新規作成 + `concepts/inkling.md` 新規作成 |
| GPT-Red | ★★★★★ | `entities/openai.md` にGPT-Redセクション追加 |
| Claude Fable 5 永久化 | ★★★★☆ | `entities/claude-code--capabilities.md` にFable 5更新情報を追記 |
| Apple vs OpenAI 訴訟 | ★★★★☆ | `entities/openai.md` に訴訟セクション追加 + `entities/apple.md` 更新 |
| The OpenAI Bubble | ★★★★☆ | 既存のOpenAIページに批判的論点として追記（`contested: true`） |
| エージェントセキュリティ問題 | ★★★★☆ | `concepts/security-and-governance/agent-sandboxing-patterns.md` に3事例追記 |
| Sierra Horizon | ★★★☆☆ | `entities/sierra.md` 新規作成（Sierra社） + `concepts/long-horizon-agents.md` 作成検討 |
| AI Engineer Conference 2026 | ★★★☆☆ | `events/ai-engineer-conference-2026.md` 新規作成 |
| Grok Build オープンソース化 | ★★★☆☆ | `entities/grok.md` 新規作成（xAI Grok Build） |
