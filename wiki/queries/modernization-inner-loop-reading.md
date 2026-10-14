---
title: "Modernization Inner-loop Reading — 案件実行"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, curated-list, codex, coding-agents, software-engineering, architecture, testing, reliability, security]
sources: [
  "https://learning.oreilly.com/playlists/881eb67b-8276-489e-ad26-d009b8b2a34f/",
  "https://sre.google/workbook/table-of-contents/", "https://github.com/google/building-secure-and-reliable-systems",
  "https://learning.oreilly.com/library/view/-/0131177052/", "https://www.amazon.com/dp/0131177052/",
  "https://learning.oreilly.com/library/view/-/9781492047834/", "https://www.amazon.com/dp/1492047848/",
  "https://learning.oreilly.com/library/view/-/9781492097532/", "https://www.amazon.com/dp/1492097543/",
  "https://learning.oreilly.com/library/view/-/9781633438156/", "https://www.amazon.com/dp/1633438155/",
  "https://learning.oreilly.com/api/v1/continue/9780134757681/", "https://www.amazon.com/dp/0134757599/",
  "https://learning.oreilly.com/library/view/kill-it-with/9781098128883/", "https://www.amazon.com/dp/1718501188/",
  "https://learning.oreilly.com/library/view/-/9781617290084/", "https://www.amazon.com/dp/1617290084/",
  "https://learning.oreilly.com/library/view/-/9798888650837/", "https://www.amazon.com/dp/B0CSJR386C/",
  "https://learning.oreilly.com/library/view/-/9781098100124/", "https://www.amazon.com/dp/1098100131/",
  "https://learning.oreilly.com/library/view/-/9780735679658/", "https://www.amazon.com/dp/B00JDMPMOA/",
  "https://learning.oreilly.com/library/view/domain-storytelling-a/9780137458974/", "https://www.amazon.com/dp/B099ZNXCJT/",
  "https://learning.oreilly.com/library/view/business-rules-and/0201743914/", "https://www.amazon.com/dp/B003YL3OZU/",
  "https://learning.oreilly.com/library/view/-/9781633439931/", "https://www.amazon.com/dp/1633439933/",
  "https://learning.oreilly.com/library/view/-/9780131495050/", "https://www.amazon.com/dp/0131495054/",
  "https://learning.oreilly.com/library/view/-/9780321574442/", "https://www.amazon.com/dp/0321503627/",
  "https://learning.oreilly.com/library/view/-/9781484238295/", "https://www.amazon.com/dp/1484238281/",
  "https://learning.oreilly.com/library/view/-/9798341634749/", "https://www.amazon.com/dp/B0F6S5425Y/",
  "https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/", "https://www.amazon.com/dp/1808347838/",
  "https://learning.oreilly.com/library/view/-/0321293533/", "https://www.amazon.com/dp/0321293533/",
  "https://learning.oreilly.com/library/view/-/9781098119058/", "https://www.amazon.com/dp/1098119061/",
  "https://learning.oreilly.com/library/view/-/0321200683/", "https://www.amazon.com/dp/0321200683/",
  "https://learning.oreilly.com/library/view/-/0321127420/", "https://www.amazon.com/dp/0321127420/",
  "https://learning.oreilly.com/library/view/-/9780321670250/", "https://www.amazon.com/dp/0321601912/",
  "https://learning.oreilly.com/library/view/-/9781680504552/", "https://www.amazon.com/dp/1680502395/",
  "https://learning.oreilly.com/library/view/site-reliability-engineering/9798341607675/",
  "https://cloud.google.com/blog/products/devops-sre/sre-book-second-edition",
  "https://learning.oreilly.com/library/view/-/9781492029496/", "https://www.amazon.com/dp/1492029505/",
  "https://learning.oreilly.com/library/view/-/9781098179915/", "https://www.amazon.com/dp/1098179927/",
  "https://learning.oreilly.com/library/view/logging-and-log/9781597496353/", "https://www.amazon.com/dp/B00AKFSM28/",
  "https://learning.oreilly.com/library/view/learning-opentelemetry/9781098147174/", "https://www.amazon.com/dp/1098147189/",
  "https://learning.oreilly.com/library/view/practical-monitoring/9781491957349/", "https://www.amazon.com/dp/1491957352/",
  "https://learning.oreilly.com/library/view/infrastructure-as-code/9781098150341/", "https://www.amazon.com/dp/109815035X/",
  "https://learning.oreilly.com/library/view/-/9780134686097/", "https://www.amazon.com/dp/0134685997/",
  "https://learning.oreilly.com/library/view/-/0321349601/", "https://www.amazon.com/dp/0321349601/",
  "https://learning.oreilly.com/library/view/-/9781098165406/", "https://www.amazon.com/dp/1098165411/",
  "https://learning.oreilly.com/library/view/-/9780132874779/", "https://www.amazon.com/dp/B007KOGS5U/",
  "https://learning.oreilly.com/library/view/-/9781492056102/", "https://www.amazon.com/dp/1492056111/",
  "https://learning.oreilly.com/library/view/-/9781118810057/", "https://www.amazon.com/dp/1118809998/",
  "https://learning.oreilly.com/library/view/-/9781617294358/", "https://www.amazon.com/dp/1617294357/",
  "https://learning.oreilly.com/library/view/building-secure-and/9781492083115/", "https://www.amazon.com/dp/1492083127/",
  "https://learning.oreilly.com/library/view/security-engineering-3rd/9781119642787/", "https://www.amazon.com/dp/1119642787/",
  "https://learning.oreilly.com/library/view/software-supply-chain/9781098133696/", "https://www.amazon.com/dp/1098133706/",
  "https://learning.oreilly.com/library/view/the-developers-playbook/9781098162191/", "https://www.amazon.com/dp/109816220X/",
  "https://learning.oreilly.com/library/view/growing-object-oriented-software/9780321574442/ch20.html", "https://martinfowler.com/articles/domain-oriented-observability.html",
  "https://www.slf4j.org/manual.html", "https://www.slf4j.org/legacy.html",
  "https://logback.qos.ch/manual/mdc.html", "https://logback.qos.ch/manual/appenders-async-sift.html",
  "https://logging.apache.org/log4j/2.x/manual/thread-context.html", "https://logging.apache.org/log4j/2.x/manual/async.html",
  "https://opentelemetry.io/docs/languages/java/instrumentation/", "https://docs.spring.io/spring-boot/reference/features/logging.html",
  "https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html", "https://microservices.io/patterns/data/transactional-outbox.html",
]
---

# Modernization Inner-loop Reading — 案件実行

[O’Reilly：inner-loop／案件実行](https://learning.oreilly.com/playlists/881eb67b-8276-489e-ad26-d009b8b2a34f/) · [[queries/modernization-reading-guide|選書ガイドの入口]]

個別のJava／企業システムを安全に移行するための42冊・7分類。自動変換やAgentも、案件を進める道具として扱う。対象システムのlogging戦略・設計・運用を含み、調査から本番受入までをつなぐ。

[[queries/modernization-inner-loop-sources|公開範囲・ライセンス・raw原資料]] · [[queries/modernization-inner-loop-study-notes|読解範囲と知見]] · [[concepts/legacy-modernization-moc|重要コンセプトの案内]]

Account-free learning: [concept study guide](modernization-independent-study-guide.md), [worked exercise](modernization-batch-example.md), and [[queries/modernization-reading-continuation|priority-reading continuation]].

## 最初に読む順番

1. **Working Effectively with Legacy Code** — 既存挙動の証拠と、変更可能な境界を作る。
2. **Specification by Example** — SMEの判断を具体例と受入条件にする。聞き取りやルール整理が難しければI-02の追加書を補う。
3. **Monolith to Microservices** — 段階的移行、新旧共存、切替単位を決める。
4. **Effective Software Testing** — 仕様・境界値・性質から独立した検証を作る。
5. **Building Evolutionary Architectures** — 守る設計特性を測れる制約にする。
6. **Continuous Delivery** と **Release It!** — 再現環境、受入、切替、本番回復をつなぐ。

RefactoringはI-01で、小さな変換の原則とカタログを参照する。テストのないコードに検証の足場を作る方法と、業務上の正解の決定は、最初の2冊で補う。I-06は案件のJavaリスクに応じて、I-07は案件初期から参照する。

loggingは、GOOS第19〜20章で運用要求と実装の分離を学び、Logging and Log Managementで戦略、SRE第2版・Workbookで健全性判定、Observability Engineeringで計装と調査へ進む。追加の参照書は各行の優先度・条件で選ぶ。詳しくは[[queries/modernization-java-logging]]を参照。

「共通」は別の読書リストにも載せる本だが、ここでは本表の目的・章だけを読む。「必要章を指定しない」は全編必読を意味せず、用途に該当する項目を参照する。古いAPI・JVM設定は対象JDKで再確認する。

## I-01 方針・範囲・段階的変更

移行対象・境界・順序・完了条件を決め、小さな変更で進める。Refactoringで振る舞いを保つ変換を学ぶ。マイクロサービス化自体を目的にしない。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Working Effectively with Legacy Code](https://learning.oreilly.com/library/view/-/0131177052/)<br>[Amazon.com](https://www.amazon.com/dp/0131177052/) | 変更前の挙動を固定するcharacterization testと、依存を切ってテスト可能にするseam。SMEの記憶だけに頼らず既存挙動を証拠化する。ただし現行挙動が正しい業務仕様かどうかは別に判断する。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Monolith to Microservices](https://learning.oreilly.com/library/view/-/9781492047834/)<br>[Amazon.com](https://www.amazon.com/dp/1492047848/) | 段階的置換、新旧共存、境界、データ分割と移行時のトレードオフ。Codexの作業単位とリリース単位を設計する材料。マイクロサービス採用を前提にせず、必要な移行パターンを選ぶ。 | 必要章を指定しない。対象の課題に応じて参照。 |
| 【共通】[Building Evolutionary Architectures, 2nd Edition](https://learning.oreilly.com/library/view/-/9781492097532/)<br>[Amazon.com](https://www.amazon.com/dp/1492097543/) | 今回の移行で守る依存方向・性能などの設計特性と段階的変更を定める。 テスト可能な制約を選び、測れない業務判断は別に記録する。 | 第1〜3章（進化・fitness function・小さな変更）、第5〜7章（構造・データ・既存構造の移行） |
| [Architecture Modernization](https://learning.oreilly.com/library/view/-/9781633438156/)<br>[Amazon.com](https://www.amazon.com/dp/1633438155/) | 業務戦略・組織・技術の変更を結び付け、移行対象と順序を決める。SMEの関与を境界の判断や未解決事項に集中させる設計に応用。2024年刊の補完書。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Refactoring: Improving the Design of Existing Code](https://learning.oreilly.com/api/v1/continue/9780134757681/)<br>[Amazon.com](https://www.amazon.com/dp/0134757599/) | 振る舞いを保つ小さな変換、その動機と検証手順の語彙。序盤の原則を読み、カタログは必要時に参照する。Agentへの作業分解にも適用できるが、DB移行・本番切替・業務仕様の回復は別途必要。テスト合格だけで全入力の同等性を証明できるわけではない。 | 必要章を指定しない。対象の課題に応じて参照。 |
| 【共通】[Kill It with Fire](https://learning.oreilly.com/library/view/kill-it-with/9781098128883/)<br>[Amazon.com](https://www.amazon.com/dp/1718501188/) | 今回の移行価値、対象範囲、代替案、旧基盤を廃止できる完了条件を定める。 現状維持・部分置換も選択肢にする。 | 第3章（構造の評価）、第5章（測れる課題・範囲・機会費用）、第9章（完了と成功基準） |

## I-02 現状理解・業務仕様・正解の根拠

コード履歴と実行結果、業務シナリオ、SMEの判断から仕様を確定する。既存ログとその利用者・parser・通知を棚卸しし、重要な業務経路を観測する。観測した旧挙動、維持すべき業務規則、受入根拠を区別し、未観測を未使用と判断しない。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| 【共通】[Specification by Example](https://learning.oreilly.com/library/view/-/9781617290084/)<br>[Amazon.com](https://www.amazon.com/dp/1617290084/) | 今回の業務ルールをSMEと具体例で合意し、独立した期待値と受入仕様にする。 現行挙動を無条件に正解とせず、Agent生成の期待値は根拠を確認する。 | 第5〜8章（範囲・協働仕様化・具体例・仕様の洗練）、第9章（仕様を変えず検証を自動化） |
| [Your Code as a Crime Scene, Second Edition, 2nd Edition](https://learning.oreilly.com/library/view/-/9798888650837/)<br>[Amazon.com](https://www.amazon.com/dp/B0CSJR386C/) | 変更履歴・ホットスポット・変更の結び付きから、優先順位と隠れた依存を調べる。SMEへの質問箇所を絞る材料。履歴は過去の開発体制も反映するため、業務重要度そのものとは区別する。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Learning Domain-Driven Design](https://learning.oreilly.com/library/view/-/9781098100124/)<br>[Amazon.com](https://www.amazon.com/dp/1098100131/) | 業務用語、サブドメイン、bounded contextを整理し、移行単位をコードの行数ではなく業務能力で切る。SMEの判断を用語集・境界・ルールとして再利用するための基礎。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Software Requirements, 3rd Edition](https://learning.oreilly.com/library/view/-/9780735679658/)<br>[Amazon.com](https://www.amazon.com/dp/B00JDMPMOA/) | 今回の要求を抽出・検証・優先順位付けし、維持／変更／廃止／未解決と出典・決定者・受入条件を記録する。 要求管理を必要章から参照する辞書的な一冊。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Domain Storytelling: A Collaborative, Visual, and Agile Way to Build Domain-Driven Software](https://learning.oreilly.com/library/view/domain-storytelling-a/9780137458974/)<br>[Amazon.com](https://www.amazon.com/dp/B099ZNXCJT/) | SMEから今回の業務シナリオを聞き出し、関係者・情報・作業と例外を共有する。 業務ルールの正しさの合意は別に残す。 | 第3〜4章（シナリオと範囲）、第6章（ワークショップ）、第11・15章（要求・隠れたIT） |
| [Business Rules and Information Systems: Aligning IT with Business Goals](https://learning.oreilly.com/library/view/business-rules-and/0201743914/)<br>[Amazon.com](https://www.amazon.com/dp/B003YL3OZU/) | 今回の業務ルールを明示し、矛盾・曖昧さを点検して受入判断の根拠にする。 2002年の古典。技術実装例よりルールを扱う原理を重視する。 | 第3〜5章（ルールの定義・発見・品質管理） |

## I-03 変更の実施・動作同等性の検証

コード変更、自動変換やAgentの利用、独立した期待値、境界値・性質・モデルによる検証を扱う。運用支援ログの意味・必須属性と既存parserの互換性も契約として検証する。診断用の全ログ文字列を固定せず、Agentの説明だけで受入を決めない。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Effective Software Testing](https://learning.oreilly.com/library/view/-/9781633439931/)<br>[Amazon.com](https://www.amazon.com/dp/1633439933/) | 仕様・境界値・事前事後条件・不変条件・property-based testingを組み合わせる。Javaの例で学べるが原則は言語非依存。Agent生成コードに対する独立した検証戦略の設計に使う。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [xUnit Test Patterns: Refactoring Test Code](https://learning.oreilly.com/library/view/-/9780131495050/)<br>[Amazon.com](https://www.amazon.com/dp/0131495054/) | fixture、test double、テストの悪い兆候を扱う参照書。生成テストの量より、独立性・保守性・失敗原因の分かりやすさを見る。古いフレームワークの記法よりパターンを読む。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Growing Object-Oriented Software, Guided by Tests](https://learning.oreilly.com/library/view/-/9780321574442/)<br>[Amazon.com](https://www.amazon.com/dp/0321503627/) | Javaの例で挙動・協調・テスト可能な境界を学ぶ。運用支援ログを利用者向けの機能として設計し、業務通知と出力技術を分離する。実接続と実出力も検証する。 | loggingは第19章（失敗記録）・第20章（Logging Is a Feature／Notification Rather Than Logging）。他の設計・テスト項目は課題別に参照 |
| [Practical TLA+: Planning Driven Development](https://learning.oreilly.com/library/view/-/9781484238295/)<br>[Amazon.com](https://www.amazon.com/dp/1484238281/) | 状態遷移・並行実行・障害時の不変条件をモデルで検証する。送金、ジョブ再実行、切替などの設計確認に有用。モデルの正しさと実装がモデルに従うことは別途検証が必要。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Beyond Vibe Coding](https://learning.oreilly.com/library/view/-/9798341634749/)<br>[Amazon.com](https://www.amazon.com/dp/B0F6S5425Y/) | 今回のAgent利用で意図を明確にし、変更を小さく分け、設計・テスト・レビューで出力を受け入れる。 自律性の高さと本番移行を任せられる保証を同一視しない。 | 必要章を指定しない。対象の課題に応じて参照。 |
| 【共通】[Automated Code Refactoring and Modernization with OpenRewrite](https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/)<br>[Amazon.com](https://www.amazon.com/dp/1808347838/) | 今回のJava更新に既存レシピを選び、適用条件と差分を確認して変換する。 2026年9月の新刊。変換が決定的でも業務上の同等性は別に検証する。 | 第1〜4章（導入・LST等の概念・実行・レシピの利用） |

## I-04 データ・トランザクション・外部連携

データ所有権、スキーマ変更、互換期間、外部契約、再試行と重複処理を確認する。ログの「成功」とDBのcommitを区別し、状態・副作用・障害回復を含めて新旧を照合する。業務確定と証跡の原子性が必要なら、トランザクション内の監査記録や[Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html)を検討する。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Refactoring Databases: Evolutionary Database Design](https://learning.oreilly.com/library/view/-/0321293533/)<br>[Amazon.com](https://www.amazon.com/dp/0321293533/) | DBスキーマとデータを小さく進化させるパターン。互換期間、アプリとの同時移行、照合、切戻し条件を設計する。コードだけ戻しても書込み済みデータは戻らない点に注意する。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Designing Data-Intensive Applications, 2nd Edition](https://learning.oreilly.com/library/view/-/9781098119058/)<br>[Amazon.com](https://www.amazon.com/dp/1098119061/) | 整合性・トランザクション・複製・分散処理のトレードオフを整理する。新旧共存時のデータ所有権、再試行、障害回復を考える基盤。定番書の2026年改訂版。 | 必要章を指定しない。対象の課題に応じて参照。 |
| 【共通】[Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions](https://learning.oreilly.com/library/view/-/0321200683/)<br>[Amazon.com](https://www.amazon.com/dp/0321200683/) | 今回のバッチ・キュー・外部システムの契約、相関、変換、重複処理を整理する。 古い製品例より連携パターンと失敗モードを読む。 | 第3〜5章（メッセージ基盤・チャネル・構成）、第7〜8章（ルーティング・変換）、第10章（エンドポイント） |
| [Patterns of Enterprise Application Architecture](https://learning.oreilly.com/library/view/-/0321127420/)<br>[Amazon.com](https://www.amazon.com/dp/0321127420/) | 業務ロジック、永続化、トランザクション境界等を分類する古典。Java／.NETの例を、既存コードの構造を説明する語彙として活用する。古いAPIをそのまま移植するための本ではない。 | 必要章を指定しない。対象の課題に応じて参照。 |

## I-05 再現環境・観測・切替・本番受入

旧／新環境を再現し、ビルド・テスト・配備・データ照合を行う。段階的切替、SLO、観測、回復手順で本番稼働を受け入れる。loggingは案件初期から、利用者の問い、通知・調査・照合の用途、到着遅延・欠落許容・保持・費用・担当者を定める。

障害対応用の観測には即時性と収集経路の可用性、詳細分析用には豊かな文脈と履歴を求める。SRE第2版第9章を使って要件を分ける。同じ基盤でも扱えるが、監視対象との共通障害で必要な観測を失わない構成にする。対象システムの診断・業務監査はinner-loop、Agentの操作や移行ワークフローの実行証跡はouter-loopで扱う。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| 【共通】[Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation](https://learning.oreilly.com/library/view/-/9780321670250/)<br>[Amazon.com](https://www.amazon.com/dp/0321601912/) | 今回のビルド、検証、環境、データ、配備を再現し、安全に切り替える。 具体的ツールは対象環境に置き換える。 | 第2章（構成管理）、第4章（テスト戦略）、第6章（ビルド・配備）、第8〜12章（受入・非機能・リリース・環境・データ） |
| [Release It!, 2nd Edition](https://learning.oreilly.com/library/view/-/9781680504552/)<br>[Amazon.com](https://www.amazon.com/dp/1680502395/) | タイムアウト、障害の伝播、リソース枯渇を学び、過負荷・部分障害・回復を受入条件に含める。運用者が正常・異常を判読できる情報と、ログ・指標・通知の責任を設計する。 | 観測は第8章Processes on MachinesのTransparency、第10章System-Wide Transparency。本番の失敗モードは課題別に参照 |
| [Site Reliability Engineering, 2nd Edition](https://learning.oreilly.com/library/view/site-reliability-engineering/9798341607675/) | **優先度：高。条件：本番受入・監視を設計する案件。** SLOと観測要件から切替後の健全性・回復を設計する。第9章で障害対応用と詳細分析用の観測を区別する。2026年刊。Workbookは実践を補う別書籍。 | 第8〜9章（SLO・観測と監視）、第14・17章（テスト・耐障害設計）。レガシー制約は第22章 |
| [The Site Reliability Workbook](https://learning.oreilly.com/library/view/-/9781492029496/)<br>[Amazon.com](https://www.amazon.com/dp/1492029505/) | SLO、監視、通知、canaryを実務へ落とす。ログと指標の役割、切替後の健全性・エスカレーション・切戻し条件を設計する。Google規模を前提にせず、重要業務へ適用する。 | 第4章Monitoring、第5章Alerting on SLOs、第16章Canarying Releases。SLO・対応手順は課題別に補う |
| [Observability Engineering, 2nd Edition](https://learning.oreilly.com/library/view/-/9781098179915/)<br>[Amazon.com](https://www.amazon.com/dp/1098179927/) | 利用者に見える挙動を観測し、未知の問題と旧新差分を調査する。計装戦略、構造化イベント、業務・実行文脈、解析、開発中の検証をつなぐ。2026年改訂版。 | 第2章、第4〜9章（計装・イベント・文脈・OTel・解析・開発）、第11〜12章（SLO）。Agent運用や組織論は用途に応じて参照 |
| [Logging and Log Management](https://learning.oreilly.com/library/view/logging-and-log/9781597496353/)<br>[Amazon.com](https://www.amazon.com/dp/B00AKFSM28/) | **優先度：高。条件：ログの利用者・記録方針・運用契約を定め直す案件。** 利用目的から分析・レビュー・対応・開発者の責任までを設計する。2012年刊の古典。現行Java API・設定・製品選定は公式資料で補う。 | 第1・7・14・16・18章。旧新フォーマットの正規化・相関が必要なら第9章 |
| [Learning OpenTelemetry](https://learning.oreilly.com/library/view/learning-opentelemetry/9781098147174/)<br>[Amazon.com](https://www.amazon.com/dp/1098147189/) | **優先度：条件付き。条件：新旧共存、サービス分割、非同期連携で処理経路を追う案件。** 計装・文脈伝播・収集をつなぎ、ログとtraceを相関する。2024年刊。既存方式で要件を満たすなら導入は不要。 | 第2〜5章、第8章（パイプライン・機密除去・backpressure）、第9章（導入） |
| [Practical Monitoring](https://learning.oreilly.com/library/view/practical-monitoring/9781491957349/)<br>[Amazon.com](https://www.amazon.com/dp/1491957352/) | **優先度：入門補助。条件：監視設計の基礎が不足する案件。** 監視の目的・設計・対応可能な通知を短く学ぶ。2017年刊。SRE資料と重なるため、基礎を理解していれば省略できる。 | 第1〜3章、第7章（アプリ監視）。業務指標は第5章 |
| 【共通】[Infrastructure as Code, 3rd Edition](https://learning.oreilly.com/library/view/infrastructure-as-code/9781098150341/)<br>[Amazon.com](https://www.amazon.com/dp/109815035X/) | 今回の旧／新環境を再作成できるようにし、環境差による検証のぶれを減らす。 条件付き：再現環境が弱い案件を優先。旧JDK・外部I/O・データも別途固定する。 | 第2章（再現性）、第11〜12章（サーバーと環境）、第15章（成果物・依存固定） |

## I-06 Java・JVMの参照資料

対象案件の契約、モジュール境界、並行性、JVM性能のリスクに応じて参照する。コンパイル成功に加え、意味と実行時特性を検証する。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Effective Java, 3rd Edition](https://learning.oreilly.com/library/view/-/9780134686097/)<br>[Amazon.com](https://www.amazon.com/dp/0134685997/) | オブジェクトの同値性、不変性、型、例外、API設計等を見直す。Agentによる見た目の整理が契約を壊していないかの確認に使う。Java 9以後の機能は現行JDK資料で補完する。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Java Concurrency in Practice](https://learning.oreilly.com/library/view/-/0321349601/)<br>[Amazon.com](https://www.amazon.com/dp/0321349601/) | 可視性、原子性、共有可変状態、ロック、キャンセルを理解する。移行後の競合やタイミング依存の不具合を考える基礎。仮想スレッドは扱わないためModern Concurrency in Javaと対で読む。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Modern Concurrency in Java](https://learning.oreilly.com/library/view/-/9781098165406/)<br>[Amazon.com](https://www.amazon.com/dp/1098165411/) | Java 21・仮想スレッドなど、古典以後の並行処理を補う。実行モデルの変更を性能・負荷・キャンセルの観点で検証する。利用JDKでのAPI安定性と挙動は公式資料で確認する。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Java Application Architecture: Modularity Patterns with Examples Using OSGi](https://learning.oreilly.com/library/view/-/9780132874779/)<br>[Amazon.com](https://www.amazon.com/dp/B007KOGS5U/) | モジュール境界・依存・再利用と変更の単位を学ぶ。モジュラーモノリスも含めた移行単位の設計に有用。OSGiは題材であり、採用を前提にせずパターンを読む。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Java Performance, 2nd Edition](https://learning.oreilly.com/library/view/-/9781492056102/)<br>[Amazon.com](https://www.amazon.com/dp/1492056111/) | JVM、GC、メモリ、計測を理解し、移行前後の性能を再現可能に比較する。Java 8／11中心のため、推奨フラグやGC設定は対象JDKで再検証。まず計測してから最適化する。 | 必要章を指定しない。対象の課題に応じて参照。 |

loggingの実装は[SLF4J API](https://www.slf4j.org/manual.html)と[bridge](https://www.slf4j.org/legacy.html)で出力経路・provider競合・循環を確認する。[Logback MDC](https://logback.qos.ch/manual/mdc.html)／[Log4j Thread Context](https://logging.apache.org/log4j/2.x/manual/thread-context.html)で処理スコープの設定・復元・非同期伝播、[Logback AsyncAppender](https://logback.qos.ch/manual/appenders-async-sift.html)／[Log4j async](https://logging.apache.org/log4j/2.x/manual/async.html)で飽和・欠落・停止時flushを検証する。

[OTel Java](https://opentelemetry.io/docs/languages/java/instrumentation/)でfile／stdoutとappenderの収集方式・二重送信を確認し、[Spring Boot公式](https://docs.spring.io/spring-boot/reference/features/logging.html)を対象版に合わせて参照する。業務処理IDとtrace/span/attemptを区別し、実際のencoder・収集後の検索・負荷まで検証する。詳しい設計項目と受入条件は[[queries/modernization-java-logging]]を参照。

## I-07 案件のセキュリティ・作業権限

案件初期から移行対象の信頼境界、作業者・Agentの権限、機密情報、依存物と配布物を確認する。対象システムのログ・MDC・例外・URLに残る機密、閲覧権限、保持・削除、改変検出を[OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)で点検する。共通のAgent実行基盤の監査はouter-loopを参照する。

| 書籍・資料 | 読む目的・留意点 | 必要章 |
|---|---|---|
| [Threat Modeling](https://learning.oreilly.com/library/view/-/9781118810057/)<br>[Amazon.com](https://www.amazon.com/dp/1118809998/) | 今回の移行対象、認証情報、外部通信、作業者・Agentの経路について資産・信頼境界・脅威・対策を明示する。 Adam Shostack著の古典。案件初期に境界を確認し、変更に応じて見直す。 | 必要章を指定しない。対象の課題に応じて参照。 |
| [Secure by Design](https://learning.oreilly.com/library/view/-/9781617294358/)<br>[Amazon.com](https://www.amazon.com/dp/1617294357/) | 型・ドメインモデル・不変条件で危険な状態を減らす。Java例を含むが考え方は言語非依存。後付けの検査だけでなく、生成コードが守るべき設計制約を定義する材料。 | 必要章を指定しない。対象の課題に応じて参照。 |
| 【共通】[Building Secure and Reliable Systems](https://learning.oreilly.com/library/view/building-secure-and/9781492083115/)<br>[Amazon.com](https://www.amazon.com/dp/1492083127/) | 作業権限・設計境界・検証・配備物を確認し、安全に移行する。対象システムのログが障害・セキュリティ調査を支えるかを評価する。機密・アクセス・受入条件に絞って読む。 | 第5〜6章（最小権限・理解可能性）、第13〜15章（テスト・配備・調査）。ログは第15章を重点参照 |
| 【共通】[Security Engineering, 3rd Edition](https://learning.oreilly.com/library/view/security-engineering-3rd/9781119642787/)<br>[Amazon.com](https://www.amazon.com/dp/1119642787/) | 今回の移行対象と作業環境について、アクセス権限と障害回復の前提を点検する。 古典の原理を参照し、全編通読は不要。 | 第6章（アクセス制御）、分散処理がある場合は第7章（分散システム） |
| 【共通】[Software Supply Chain Security](https://learning.oreilly.com/library/view/software-supply-chain/9781098133696/)<br>[Amazon.com](https://www.amazon.com/dp/1098133706/) | 更新する依存物と、ソースから本番配布物までの対応を確認する。 SBOMだけで安全性や業務上の正しさを保証しない。 | 第5章（ソース・ビルド・配備管理）、第7〜8章（データ保護・SBOMと来歴） |
| 【共通】[The Developer's Playbook for Large Language Model Security](https://learning.oreilly.com/library/view/the-developers-playbook/9781098162191/)<br>[Amazon.com](https://www.amazon.com/dp/109816220X/) | 案件でAgentが読むリポジトリや文書を信頼しすぎず、情報漏えいと過剰な操作を防ぐ。 2024年刊。Codex専用の設定手順ではない。 | 第3〜5章（信頼境界・プロンプトインジェクション・知識の漏えい）、第7章（過剰な自律性・出力処理） |

## 案件で残す証拠

| 工程 | 成果物 | 人が判断する箇所 |
|---|---|---|
| 対象選定・分解 | 業務フロー、依存、リスク、作業の入出力と完了条件 | 事業優先順位、廃止、意図的な仕様変更 |
| 仕様と正解の確定 | 出典付きルール、具体例、期待値、未解決事項 | 旧挙動が意図された仕様か、承認する例外は何か |
| 変更と検証 | 再現環境、差分・性質・契約テスト、照合結果 | 独立した期待値、説明できない差分 |
| 切替と運用 | データ照合、SLO、ログの契約・検索・収集失敗の検証、回復手順、受入記録 | 残存リスクと本番移行の責任 |

期待値を変更したAgentの推測だけから作らない。月末・希少例・障害回復を含む代表的データ、匿名化、比較器自体の検証も、対象案件に合わせて用意する。これらは選書を実務へ適用する推奨であり、書籍やAgent製品が保証するものではない。

根拠の扱いは[[concepts/modernization-traceability]]、比較範囲は[[concepts/legacy-behavioral-parity]]、全体工程は[[concepts/enterprise-legacy-modernization]]を参照。仕組みを設計する段階になったら[[queries/modernization-outer-loop-reading]]へ進む。

分類の考え方と目的別の案内は[[queries/modernization-reading-guide]]を参照。
