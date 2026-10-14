---
title: "Modernization Outer-loop Reading — 仕組み化"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, curated-list, codex, coding-agents, software-engineering, architecture, testing, reliability, security]
sources: [
  "https://developers.openai.com/blog/eval-skills",
  "https://developers.openai.com/api/docs/guides/agents/guardrails-approvals",
  "https://docs.openrewrite.org/concepts-and-explanations/lossless-semantic-trees",
  "https://learning.oreilly.com/playlists/f09ea227-8f41-450e-b79b-e9fbdbe4c597/",
  "https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/", "https://www.amazon.com/dp/0134689321/",
  "https://learning.oreilly.com/library/view/-/9781617290084/", "https://www.amazon.com/dp/1617290084/",
  "https://learning.oreilly.com/library/view/language-implementation-patterns/9781680500097/", "https://www.amazon.com/dp/193435645X/",
  "https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/", "https://www.amazon.com/dp/1808347838/",
  "https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/",
  "https://learning.oreilly.com/library/view/-/9781098176495/", "https://www.amazon.com/dp/1098176502/",
  "https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/", "https://www.amazon.com/dp/149206145X/",
  "https://learning.oreilly.com/library/view/-/0321200683/", "https://www.amazon.com/dp/0321200683/",
  "https://learning.oreilly.com/library/view/-/9780321670250/", "https://www.amazon.com/dp/0321601912/",
  "https://learning.oreilly.com/library/view/infrastructure-as-code/9781098150341/", "https://www.amazon.com/dp/109815035X/",
  "https://learning.oreilly.com/library/view/-/9781098166298/", "https://www.amazon.com/dp/1098166302/",
  "https://learning.oreilly.com/library/view/-/9798341660717/", "https://www.amazon.com/dp/B0GTYQTYDP/",
  "https://learning.oreilly.com/library/view/-/9781492097532/", "https://www.amazon.com/dp/1492097543/",
  "https://learning.oreilly.com/library/view/building-secure-and/9781492083115/", "https://www.amazon.com/dp/1492083127/",
  "https://learning.oreilly.com/library/view/security-engineering-3rd/9781119642787/", "https://www.amazon.com/dp/1119642787/",
  "https://learning.oreilly.com/library/view/software-supply-chain/9781098133696/", "https://www.amazon.com/dp/1098133706/",
  "https://learning.oreilly.com/library/view/the-developers-playbook/9781098162191/", "https://www.amazon.com/dp/109816220X/",
  "https://learning.oreilly.com/library/view/-/9781098157234/", "https://www.amazon.com/dp/1942788819/",
  "https://learning.oreilly.com/library/view/-/9781457191435/", "https://www.amazon.com/dp/1942788339/",
  "https://learning.oreilly.com/library/view/kill-it-with/9781098128883/", "https://www.amazon.com/dp/1718501188/",
]
---

# Modernization Outer-loop Reading — 仕組み化

[O’Reilly：outer-loop／仕組み化](https://learning.oreilly.com/playlists/f09ea227-8f41-450e-b79b-e9fbdbe4c597/) · [[queries/modernization-reading-guide|選書ガイドの入口]]

移行方法を再利用・標準化・省力化するための20点・6分類。対象はAgent構成、変換レシピ、業務知識、ワークフロー、検証基盤と運用責任。案件で観測した失敗・例外・SMEへの質問を入力にする。

公開本文・保存許諾と原資料は[[queries/modernization-outer-loop-sources]]、優先8資料で実際に読んだ節と設計上の適用は[[queries/modernization-outer-loop-study-notes]]、追加概念は[[concepts/legacy-modernization-moc]]を参照。全20点や指定章すべての通読完了を意味しない。

Account-free learning: [concept study guide](modernization-independent-study-guide.md), [worked exercise](modernization-batch-example.md), and [[queries/modernization-reading-continuation|priority-reading continuation]].

## 優先して読む順番

1. **Living Documentation** と **Specification by Example** — SMEの判断を出典・適用範囲・更新責任付きで再利用する。
2. **OpenRewriteの書籍** と **AI for Mass-Scale Code Refactoring and Analysis** — 決定的な変換、Agentの調査・提案、業務判断の役割を分ける。Language Implementation Patternsは変換機構の設計担当が深掘りする。
3. **Practical Process Automation** — 状態、再試行、承認待ち、停止・再開を設計する。連携の失敗モードはEnterprise Integration Patternsで補う。
4. **AI Engineering／Evals for AI Engineers** — 代表案件と失敗分析を使い、仕組みを変更した際の品質を評価する。
5. **Building Secure and Reliable Systems** — 権限・監査・成果物の検証を実行基盤へ組み込む。

この順番は読書の優先順位であり、安全対策の実装を後回しにする意味ではない。「共通」は案件実行側にも掲載する本。本表の読む目的と必要章を選び直す。全冊通読は不要。

## O-01 業務知識・判断根拠の蓄積と更新

案件で得た業務ルール・判断理由・承認済み例外を、出典と適用範囲を保って更新・再利用できる知識資産にする。個別案件の仕様確定そのものはinner-loop I-02で扱う。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Living Documentation: Continuous Knowledge Sharing by Design, First Edition](https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/)<br>[Amazon.com](https://www.amazon.com/dp/0134689321/) | 判断理由と仕様をコード・テストへ結び、知識の出典と鮮度を維持する仕組みを作る。 生成文書の量ではなく、根拠と更新・整合確認の方法を重視する。 | 第1〜4章（原則・実行可能な仕様・知識利用・判断理由の付加）、第12章（アーキテクチャ文書） |
| 【共通】[Specification by Example](https://learning.oreilly.com/library/view/-/9781617290084/)<br>[Amazon.com](https://www.amazon.com/dp/1617290084/) | 承認済みの具体例を継続検証・更新する運用にし、SMEへの同じ確認を減らす。 業務判断の出典と変更責任を残す。 | 第2〜3章（プロセスと生きた文書）、第9〜11章（自動検証・頻繁な検証・文書システムの進化） |

## O-02 自動変換・Agentの役割分担と資産化

定型変換をレシピ化し、適用条件・検証条件・版を管理する。Agentは調査、レシピ作成、失敗分析を支援する。業務判断と独立検証の責任を分ける。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Language Implementation Patterns](https://learning.oreilly.com/library/view/language-implementation-patterns/9781680500097/)<br>[Amazon.com](https://www.amazon.com/dp/193435645X/) | 構文木・スコープ・型に基づく変換の前提と限界を理解し、レシピ設計を支える。 条件付き：変換機構の設計担当向け。古いANTLR例の流用や処理系の自作は前提にしない。 | 第4〜8章（木・走査・シンボル・型）、第11章（言語変換） |
| 【共通】[Automated Code Refactoring and Modernization with OpenRewrite](https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/)<br>[Amazon.com](https://www.amazon.com/dp/1808347838/) | 独自レシピを開発・組合せ・テストし、反復利用できる変換資産にする。 2026年9月の新刊。Agentの提案とレシピの実行、独立検証を分ける。 | 第2章（LST・visitor）、第4〜6章（レシピ構成・独自レシピ・cursorと変換） |
| [AI for Mass-Scale Code Refactoring and Analysis](https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/)<br>Amazon掲載ページ未確認 | AIの調査・提案と、構造を理解した反復的な変換の役割分担を検討する。 2024年・42ページの短い補完資料。OpenRewrite/LST中心の視点を古典と対照する。 | 第1〜3章（AIによる大規模変更、LST・レシピとAI、モデルの活用） |
| [Building Applications with AI Agents](https://learning.oreilly.com/library/view/-/9781098176495/)<br>[Amazon.com](https://www.amazon.com/dp/1098176502/) | 調査・計画・変換・検証を担うAgentのツール、知識、メモリ、引継ぎを設計する。 Codex専用の操作書ではない。業務仕様の未解決事項を人へ戻す。 | 必要章を指定しない。対象の課題に応じて参照。 |

## O-03 実行制御・例外処理・人への引継ぎ

再現可能な実行基盤と、状態・チェックポイント・再試行・冪等性・停止／再開・承認待ちを備えた移行ワークフローを設計する。技術的失敗と未解決の業務判断を区別する。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Practical Process Automation](https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/)<br>[Amazon.com](https://www.amazon.com/dp/149206145X/) | 状態・承認待ち・再試行・停止／再開・補償を備えた移行ワークフローを設計する。 製品採用は前提にしない。技術的失敗、検証不合格、未解決の業務判断を区別する。 | 第3〜4章（プロセス開発・人と処理の連携）、第7〜11章（境界・連携・冪等性・例外・可視化） |
| 【共通】[Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions](https://learning.oreilly.com/library/view/-/0321200683/)<br>[Amazon.com](https://www.amazon.com/dp/0321200683/) | 移行ジョブ間の配送・相関・重複排除・監視を、実行制御の共通語彙で設計する。 配送成功だけで移行成功とは判定しない。 | 第7章（ルーティング）、第10章（エンドポイント、冪等な受信）、第11章（システム管理） |
| 【共通】[Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation](https://learning.oreilly.com/library/view/-/9780321670250/)<br>[Amazon.com](https://www.amazon.com/dp/0321601912/) | 受入済み成果物だけを先へ進めるパイプラインと、共通の実行・依存管理を設計する。 承認待ちや長時間の移行状態はPractical Process Automationで補う。 | 第5〜7章（パイプライン・スクリプト・コミット段階）、第11・13・15章（環境・依存・運営） |
| 【共通】[Infrastructure as Code, 3rd Edition](https://learning.oreilly.com/library/view/infrastructure-as-code/9781098150341/)<br>[Amazon.com](https://www.amazon.com/dp/109815035X/) | 使い捨て実行環境と再利用可能な構成要素を設計し、環境基盤自体を継続検証する。 条件付き：基盤を共通化する担当者向け。環境定義だけで業務データの再現性は保証されない。 | 第6〜10章（構成要素・再利用・設定・統合・ライブラリ）、第14〜18章（配布・パイプライン・テスト） |

## O-04 自動化の評価・品質ゲート

個別の移行結果に加え、Agent構成・レシピ・手順を変更した際の品質を評価する。代表案件、失敗分類、独立した期待値、非機能制約を継続検証する。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [AI Engineering](https://learning.oreilly.com/library/view/-/9781098166298/)<br>[Amazon.com](https://www.amazon.com/dp/1098166302/) | Agent構成の変更を品質・コスト・運用の観点で評価する。 コード生成品質と移行業務の成功率を分け、従来のソフトウェア検証と組み合わせる。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Evals for AI Engineers](https://learning.oreilly.com/library/view/-/9798341660717/)<br>[Amazon.com](https://www.amazon.com/dp/B0GTYQTYDP/) | 代表的な案件と失敗分析から、Agentや手順の回帰評価を作る。 2026年10月刊表示の補完書。SME判断を評価資産にし、judgeの点数だけで移行を承認しない。 | 必要章を指定しない。対象の課題に応じて参照。 |
| 【共通】[Building Evolutionary Architectures, 2nd Edition](https://learning.oreilly.com/library/view/-/9781492097532/)<br>[Amazon.com](https://www.amazon.com/dp/1492097543/) | 案件ごとに注意書きを繰り返さず、守るべき設計特性を自動ゲートとして継続検証する。 個別案件の受入条件に合うゲートを選び、過剰な共通化を避ける。 | 第2〜4章（fitness function・パイプライン・自動ガバナンス）、第8章（落とし穴） |

## O-05 実行基盤の権限・監査・成果物の来歴

Agentと人の権限、認可と承認、監査証跡、ソース・検証・ビルド・配布物の対応を設計する。個別案件の安全な作業手順はinner-loop I-07で扱う。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| 【共通】[Building Secure and Reliable Systems](https://learning.oreilly.com/library/view/building-secure-and/9781492083115/)<br>[Amazon.com](https://www.amazon.com/dp/1492083127/) | Agent・検証者・本番承認者の境界と、証拠を伴うビルド・配布・監査を設計する。 緊急時アクセスも例外として追跡できるようにする。 | 第5章（最小権限と認可）、第14〜15章（来歴・配備ポリシー・監査ログ） |
| 【共通】[Security Engineering, 3rd Edition](https://learning.oreilly.com/library/view/security-engineering-3rd/9781119642787/)<br>[Amazon.com](https://www.amazon.com/dp/1119642787/) | Agentと人のアクセス制御・情報の境界・セキュリティポリシーを一貫して設計する。 組織で必要な保証水準に合わせ、モデルを過剰に複雑化しない。 | 第6章（アクセス制御）、第9〜10章（多段階セキュリティ・境界） |
| 【共通】[Software Supply Chain Security](https://learning.oreilly.com/library/view/software-supply-chain/9781098133696/)<br>[Amazon.com](https://www.amazon.com/dp/1098133706/) | 開発・ビルド・配布基盤に継続的な依存物管理、来歴情報と証明を組み込む。 検証対象のソース版と実際に配布した成果物を結び付ける。 | 第3〜5章（基盤・安全な開発工程・ビルド管理）、第8章（透明性・来歴） |
| 【共通】[The Developer's Playbook for Large Language Model Security](https://learning.oreilly.com/library/view/the-developers-playbook/9781098162191/)<br>[Amazon.com](https://www.amazon.com/dp/109816220X/) | Agent実行基盤の信頼境界、権限、資源制限、継続的な安全性検証と監視を設計する。 古典の認可設計と組み合わせ、モデル内の注意書きだけに依存しない。 | 第3・7〜9章（境界・権限・資源・供給網）、第11章（開発工程・検証・監視） |

## O-06 責任分担・省力化効果・継続改善

SMEへの相談窓口と基盤の保守責任を定める。SME工数、手戻り、失敗・回復、受入済み成果を測り、仕組み化の投資と改善範囲を判断する。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Team Topologies](https://learning.oreilly.com/library/view/-/9781098157234/)<br>[Amazon.com](https://www.amazon.com/dp/1942788819/) | SMEへの相談窓口、案件担当、支援基盤の保守責任と認知負荷を整理する。 人間のチームモデルをAgentへ機械的に写さない。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Accelerate](https://learning.oreilly.com/library/view/-/9781457191435/)<br>[Amazon.com](https://www.amazon.com/dp/1942788339/) | 仕組み化の改善効果を、所要時間・失敗・回復・手戻り・SME工数で測る。 生成行数ではなく、受入済み成果と運用の安定性を評価する。 | 必要章を指定しない。対象の課題に応じて参照。 |
| 【共通】[Kill It with Fire](https://learning.oreilly.com/library/view/kill-it-with/9781098128883/)<br>[Amazon.com](https://www.amazon.com/dp/1718501188/) | 案件の振り返りを仕組み化の投資・責任分担・改善に結び付ける。 自動化した量ではなく、価値と保守負担で継続を判断する。 | 第5章（機会費用）、第7章（意思決定・組織設計）、第9〜10章（振り返り・フィードバック・自動化への注意） |

## 案件から仕組みへ取り込むもの

| 案件から得る入力 | 仕組みとして管理するもの | 人へ戻す条件 |
|---|---|---|
| SMEの回答、ルール、承認例外 | 出典・適用範囲・版・所有者・鮮度を持つ判断記録と受入例 | 根拠の衝突、失効、適用範囲外 |
| 繰り返す変更と変換失敗 | 適用条件・検証条件付きレシピ、Agentの作業契約 | 意図的な業務変更、変換条件を満たさない場合 |
| 中断・再試行・例外 | 永続化した状態、チェックポイント、冪等性、補償、承認待ち | 検証不合格、回復不能、未解決の業務判断 |
| 受入結果と本番の不具合 | 代表案件・希少例・失敗分類・回帰評価・品質ゲート | 独立した期待値がない、説明できない差分 |
| 手戻り、SME工数、復旧記録 | 再利用率、所要時間、失敗・回復、受入済み成果、保守費用 | 省力化より維持費や残存リスクが大きい場合 |

実装と期待値を同じAgentの推測から同時生成するだけでは独立検証にならない。別Agentの賛成やLLM judgeの点数だけを本番承認条件にしない。権限境界と承認責任は、生成コードや指示文の外側にも設ける。これらは書籍群を組み合わせた設計上の推奨であり、特定製品の保証ではない。

既存ガイドで参照した[OpenAIのSkills評価資料](https://developers.openai.com/blog/eval-skills)、[Agentsのガードレール・承認資料](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)、[OpenRewriteのLST資料](https://docs.openrewrite.org/concepts-and-explanations/lossless-semantic-trees)は、製品固有の実装を検討する段階で現行仕様を確認する補助資料とする。

[[concepts/modernization-traceability]]の出典と判断の対応を基盤に、[[concepts/enterprise-legacy-modernization]]の工程へ適用する。公開事例の根拠は[[queries/codex-enterprise-modernization-cases]]、個別案件の実行知識は[[queries/modernization-inner-loop-reading]]を参照。

書誌・提供状況と章範囲の確認日：2026-10-14。用途は書籍説明・目次からの選定判断であり、全冊の通読レビューではない。分類の考え方と目的別の案内は[[queries/modernization-reading-guide]]を参照。
