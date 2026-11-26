# トレンドレポート 2026-11-26（12:00 UTC）

## スキャン概要

| 項目 | 数値 |
|---|---|
| blog-ingest（今朝 10:00 UTC run） | 新規 29 / スクラップ 20 / トリアージ take 6・ref 5・skip 7 |
| newsletter-ingest（10:11 UTC run） | 3 通 36 候補 → take 1（SemiAnalysis GDPx 正式版） |
| HN front_page（2日・25pt以上） | 30 件 |
| HN keyword スキャン | 25 件 |
| HN points-only sweep（24h・90pt以上） | 27 件 |
| 一次ソース fetch | 14 件中 13 件 OK（dbushell 404 / modaic は JS レンダリングで 77 文字） |
| HN コメントツリー mining | 10 ストーリー |

本日は **AI 数学の連続成果と、そこから派生した「暗号が壊れる」という検証不能な噂**が圧縮トップ
（Aaronson 記事 1627pt / 1437コメント）。続いて Google の Cogentic、トークンディスカウント再販、
モデル来歴フォレンジックスが旬のテーマ。

---

## 上位トピック（Newsjacking スコア付き）

| # | トピック | NJ | HN | アクション | 対象ページ |
|---|---|---|---|---|---|
| 1 | 計算複雑性理論の AI 一括成果（omega=9/4・VP≠VNP・フーリエ変換下限）と Aaronson の「シンギュラリティの始まり」投稿 | 5/5 | 50646108 1627pt | wiki 概念ページ新規 | concepts/complexity-theory-ai-breakthrough-2026-11.md |
| 2 | 「ラボは Factoring in P を握っている」噂とスレッド側の 5 つの反論 | 4/5 | 50643065 492pt | 同上ページに統合 | 同上 |
| 3 | Google Cogentic：マルチエージェント証明発見ハーネス＋決定論的亜指数因数分解 | 4/5 | 50642086 494pt | wiki 概念ページ新規 | concepts/google-cogentic-proof-discovery.md |
| 4 | Moat（Command Code）＝ OpenRouter 代替のメンバーシップ型トークン割引、ルーティングの信頼問題 | 3/5 | 50652184 99pt | wiki 概念ページ新規 | concepts/discount-token-reseller-router-trust.md |
| 5 | 「Latency doesn't lie」— Jev は Qwen3.5-35B-A3B 由来という来歴フォレンジックス | 4/5 | 50648823 318pt | wiki 概念ページ新規＋既存更新 | concepts/latency-fingerprint-model-provenance.md |
| 6 | NYT がカメラマンに Photoshop の AI 機能対応アップデート禁止を通達 | 3/5 | 50647673 421pt | raw のみ保存（本文 chrome 多数） | raw/articles/2026-11-26_theverge_...md |
| 7 | Anthropic GRH 証明の簡略版 Lean 再検証（lsernau） | 2/5 | 50648050 472pt | 既存ページ更新 | concepts/ai-mathematics-theorem-proving.md |
| 8 | 1Password セキュリティインシデント（backend 侵入） | 3/5 | 50644817 1471pt | blog-ingest 側で処理済み／今回スキップ | — |

NJ スコア = Newsjacking 5 基準（トレンドサーフィン／分極化させる約束／逆説的洞察／パターン割り込み／
イングループ信号）で満たした数。

---

## 1. 計算複雑性理論の連続成果 — 「50年-open が一週間で潰れる」

Aaronson（scottaaronson.blog/?p=10379、11/25）が OpenAI/Anthropic の VP≠VNP と Alpöge/Anthropic の
リーマン仮説に続き、OpenAI の **行列積指数 omega = 9/4 一致（下限つき）** を報告。同記事内でさらに
**フーリエ変換の線形ゲート数 N(log N)^(1/2+o(1))（こちらも一致下限）**、Yupan Liu の QIP(2)=PSPACE
に触れ、次のように締める。

> All these questions from the ancient days are now just getting ... straight-up answered, rather than
> slowly illuminated with a drip-drip-drip of clues.
> Right now - this past week - is very much like I would've always imagined the beginning of an AI
> singularity to look and feel like.

本質は「値」ではなく**下限の形**にある、と Aaronson 自身書いている：「the even bigger shock is that the
AI was able to prove any lower bound of the form omega > 2. I never expected this challenge to be all
that much easier than P != NP.」Strassen の omega < 3 以来の中心問題が、しかも有理数で決着した。

一方で検証状況は非対称。**GRH 系**は公表一週間で構造解説 3 本・GitHub 再構成 2 本・簡略版 Lean 再検証
（HN 472pt）まで到達済み。**OpenAI 11 月プレプリント群**は 11/26 時点で独立検証ゼロ（10 月コーホートが
24 時間で 3 論文撤回・14 修正だった土台を思い出すべき、という指摘がスレッドにもある）。Lean 側に
「Lean 自体のセキュリティバグが最近多く見つかった。推移的信頼性のサプライチェーンとして考えよ」
（Jake A）という別レイヤーの警戒も出ている。

## 2. 「暗号が壊れる」噂 — 一次ソースはブログのコメント欄

Aaronson の該当箇所は「some of those algorithms will break currently deployed cryptosystems ... yes, I'm
virtually certain, from multiple reliable sources, that the AI labs are now sitting on one or more
bombshells in that area」だが、直後に「詳細を見るまで性質は確信できない／Telephone game で歪んだ可能性」
と自分で薄めている。Reddit 発の「ラボが Factoring in P を解いた」噂（HN 492pt）の一次ソースは、
Aaronson の own blog コメント「I've now heard many, many rumors that one or both labs are sitting on
Factoring in P. I don't know how much to credit this.」

スレッド側の反論が記録として価値が高い：

- **分類仮説**（stackghost）：暗号に効く成果は NSA が 70 年代に差分暗号解析を封印させたのと同じく機密化
  されるはず。「ランダムなブロガーに漏れる」版は怪しい。
- **射程の限定**（xoa）：「暗号は壊れない」は語として不正確。ワンタイムパッドは議論の外、対称鍵は
  Grover 以上は原理的に難しい。現行 PKI が死ぬのは巨大な PITA だが工学的問題。
- **証明と攻撃は別物**（maxrecursion）：「Solving proofs is completely different from having actually
  broken crypto in real life」＋過去の量子暗号不安は「complete over-hyped BS」だったという前例。
- **構成可能性**（sedictious）：P=NP を構成的に証明しても計算実行可能性は別。下限が下がることは
  暗号設計の指針を変えても、素因数分解が実用速度になることとは限らない。
- **信頼度割引**（negura）：Aaronson は長く同じ類の FUD を流して税の研究費を誘導してきた、という評価。
- 対して具体的データ点は Anthropic が 9 月に **既存手法で** RSA-896 を分解した事実（より速い手法は
  見つけていないと明言）。関心と計算資源の投入は証明されるが、ブレークスルーは証明しない。

## 3. Google Cogentic — ハーネスとしての証明発見

Google Research が `cogentic_research_papers` にプレプリント一括公開（HN 494pt）。手法論文は
「Cogentic: Multi-Agent Orchestration for Automated Proof Discovery」（arXiv 2609.40324）。**既存 LLM を
中央オーケストレータ＋中間証明の共有 DB で協調させるハーネス**で、Gemini 4 Argon を使い、
**決定論的亜指数時間の整数因数分解**・離散対数などを出した。

AI 数学の第三の運用モデルとして整理できる：(a) OpenAI の産業規模 Lean 一括出版、(b) Alpöge/Anthropic
型の人間主導＋AI、(c) Cogentic の多エージェント・共有証明テーブル。報告されている差別化点は
**公開前に人間レビューを通す（が、Lean 化はされていない）** — OpenAI プロファイルの逆。

スレッド内で最重要の数字は現実調整：「GNFS が 10^47  ops で済むところ、これは 4096-bit RSA に
10^2572 ops しか要しない。改善点は任意の整数で必ず効くことだけ」（vlovich123）。亜指数とはコンピュティングでの亜指数クラスの
主張であって実用攻撃ではない、かつ楕円曲線は因数分解改善の影響を受けない。
副次的な論点はキャリア話に寄った：「PhD が next OpenAI/Anthropic trophy paper になるか分からない」
（edumucelli）vs「モデルとエージェントで探索を効率化する PhD は scooped されない価値がある」
（brandonpelfrey）。反対→反対として「ラボの trophy paper が外生ショック」という合意がある点自体が
2025 年からの大きな変化。

## 4. ディスカウント トークン再販とルーター信頼

Moat（commandcode.ai/moat、"Your OpenRouter Replacement"、HN 99pt）はメンバーシップ制でトークンを
割引販売（DeepSeek 約 70% off）。スレッドの市場評価は「もう何千とある」「使われきっていない
サブスク割当を 80% off で流している店がゴロゴロ」（fedupnow）。比較テストでは割引側は TPS が
不安定で、結局 Direct DeepSeek API に戻った事例（割高でも性能安定を買う）も報告されている。

本題は信頼：「ツールコールが入ると実質マシンへのフルアクセス。**感染した／悪意あるルーターが
malicious tool call を注入する攻撃は来るか**」（resonious）。さらに OpenRouter で ZDR を付け忘れた
2 時間で、ルーティング先のエンドプロバイダがハッキングされていた通知を受けた実例（petesergeant）が
出され、**ルーティングは選ばされていないエンドプロバイダ群に対する推移的信頼**であることが確認された。
「そもそもルーターは要るのか」への実務解は「1 サブスクで満足なら不要、複数試す時に便利。API 利用では
モデル別にプロンプト調整が必要なのでルーター頼みは怪しい」（Oxodao）。

## 5. レイテンシ指紋によるモデル来歴フォレンジックス

Modaic（被験企業の競合）が「Latency doesn't lie」で **Jev は Qwen3.5-35B-A3B 由来**と主張（HN 318pt）。
重みを見ずに、重み以外の信号で来歴を推定する手法として再利用可能：同一質問を複数の誘導形式で
候補ベース模型ごとにぶつける自己同一化表（Qwen: Yes 64%/56%、DeepSeek: No 95-98%、Gemma: No 86-90%）
＋レイテンシ挙動の一致。

スレッドは「実は自社の別モデルで来歴を開示済みだったのでは」（ashkankiani）に割れた。評価軸は 3 つ
に分離できる：(1) 来歴自体は問題ではない、非開示が問題、(2) 派生でも新機軸なら novel（「hiphop は
70 年代のサンプルでできている」— keyle）、(3) そもそも "System 1" という呼称が実態と合わない
（heyjamesknight）。出版側が競合である点は常に割引必須（「再現がない限り grain of salt」— linolevan）。
なお当 wiki 内の SGNT 記述（Jev = 100M パラメータの GPT2-small 派生）とは来歴の言い分が食い違って
おり、この緊張関係はページ側に明記した。

## 6. その他注目（ページ化は見送り）

- **NYT がカメラマンへ Photoshop AI 機能対応アップデートの禁止**を通達（421pt）。ニュースルーム側の
  「デフォルトで AI が入る Professional ツール」への最も安価な対処＝バージョン固定、という構図。同日の
  NY 州 AI チャットbot 玩具 5 年禁止（50644909）や Doctorow の NY vs auto-enshittification と並ぶ文脈。
  本文取得が chrome 主体だったため raw のみ保存・「スレッド由来」と明示。
- **Anthropic GRH 簡略版 Lean 再検証**（github.com/lsernau/grh-lean、472pt）→ 既存ページ更新。
- **LLM agents work for their parent companies, not for you**（1017pt）→ 今朝の pipeline が
  `concepts/agent-principal-agent-problem.md` として収録済み（スレッドの TeMPOraL robots.txt 論争・
  「It's not the model. It's the harness.」も収録）。今回はスキップ。
- **Anthropic IPO 破発（$83 割れ）／Amodei 兄妹 IPO 中に $561M 売却／Tegmark 「Anthropic 社員は世界
  乗っ取りを語っていた」**（428/130/52/223pt）→ `events/anthropic-ipo-roadshow-2026.md` がカバー。
- **Ask HN: Anthropic が自社を蒸留扱いしている、どうやって無実を証明する**（453pt/350c）→
  `concepts/distillation-accusations-as-platform-control.md` 既存。
- **Gemini「Twinkle Twinkle Little Star」の歌詞を拒否**（218pt）／**Bare Metal Qwen（llm.asm、Qwen3-0.6B
  を 12KB で推論、純 NASM）**（169pt）／**songe（ローカル余剰計算で学習）**（235pt）／**ProofAtlas
  LLM 評価による数学未解決 500 問題ランキング**（103pt）→ 情報価値はあるが wiki 化閾値未満、
  前者は複雑性ページから参照。

---

## ウィクション推奨アクション

| トピック | 状態 |
|---|---|
| 計算複雑性 AI ブレイクスルー波 | ✅ 新規作成 concepts/complexity-theory-ai-breakthrough-2026-11.md |
| Google Cogentic 因数分解 | ✅ 新規作成 concepts/google-cogentic-proof-discovery.md |
| トークン割引再販・ルーター信頼 | ✅ 新規作成 concepts/discount-token-reseller-router-trust.md |
| モデル来歴フォレンジックス | ✅ 新規作成 concepts/latency-fingerprint-model-provenance.md |
| OpenAI プレプリント・レース | ✅ 既存更新（Aaronson フレーミング追記） |
| AI 数学定理証明（GRH 簡略版含む） | ✅ 既存更新（Cogentic 第3モデル追記） |
| OpenRouter（割引再販の圧力） | ✅ 既存更新 entities/openrouter.md |
| SGNT / Jev（来歴 challenge） | ✅ 既存更新 entities/sgnt-jev-article.md |
| 1Password backend インシデント | ⚠️ 未収録（朝の blog-ingest が daringfireball 経由で raw 取得済みのみ）→ 次回インジェスト候補 |
| Nfs2root（Linux NFS 12年物の pre-auth RCE）/ Slow Ubuntu security response | ⚠️ 未収録・セキュリティ系、AI 文脈は薄いが CVE 系ページとの接続余地 |
| Google Workspace MCP（Gmail エージェントがメールを送れない） | ⚠️ 未収録・次回 MCP 更新時に一緒に処理 |

## 生データ

- HN スキャン出力: `/tmp/hn/out_1126.txt`, `/tmp/hn/points_1126.txt`
- コメントマイニング: `/tmp/hn/comments_1126.txt`
- 一次ソース本文: `/tmp/hn/articles_1126/`（13/14）
- raw 保存: `wiki/raw/articles/2026-11-25_scottaaronson_...`, `2026-11-26_google_cogentic-...`,
  `2026-11-26_commandcode_moat-...`, `2026-11-26_modaic_jev-...`, `2026-11-26_theverge_nyt-...`
- SCHEMA 追加タグ（8）: complexity-theory, post-quantum-crypto, ai-research-automation, lab-rumors,
  integer-factorization / llm-gateway, latency-fingerprinting, model-provenance
- `supply-chain-security` は SCHEMA 不在 → 既存の正式トークン `ai-supply-chain-security` に読み替え済み
