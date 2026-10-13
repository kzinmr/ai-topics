---
title: "Java Logging Strategy for Modernization"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, java, software-engineering, architecture, observability, reliability, testing, security, audit]
sources:
  - https://learning.oreilly.com/library/view/growing-object-oriented-software/9780321574442/ch20.html
  - https://growing-object-oriented-software.com/toc.html
  - https://martinfowler.com/articles/domain-oriented-observability.html
  - https://www.oreilly.com/library/view/release-it-2nd/9781680504552/
  - https://www.oreilly.com/library/view/observability-engineering-2nd/9781098179915/
  - https://learning.oreilly.com/library/view/logging-and-log/9781597496353/
  - https://www.oreilly.com/library/view/learning-opentelemetry/9781098147174/
  - https://www.oreilly.com/library/view/practical-monitoring/9781491957349/
  - https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/
  - https://www.slf4j.org/manual.html
  - https://www.slf4j.org/legacy.html
  - https://logback.qos.ch/manual/mdc.html
  - https://logback.qos.ch/manual/appenders-async-sift.html
  - https://logging.apache.org/log4j/2.x/manual/thread-context.html
  - https://logging.apache.org/log4j/2.x/manual/async.html
  - https://opentelemetry.io/docs/specs/otel/logs/data-model/
  - https://opentelemetry.io/docs/languages/java/instrumentation/
  - https://opentelemetry.io/docs/zero-code/java/agent/
  - https://docs.spring.io/spring-boot/reference/features/logging.html
  - https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
  - https://sre.google/sre-book/monitoring-distributed-systems/
  - https://sre.google/workbook/monitoring/
  - https://sre.google/workbook/canarying-releases/
  - https://learning.oreilly.com/library/view/site-reliability-engineering/9798341607675/
  - https://cloud.google.com/blog/products/devops-sre/sre-book-second-edition
  - https://microservices.io/patterns/data/transactional-outbox.html
---

# Java Logging Strategy for Modernization

Javaシステムの現状理解、変更の検証、段階的切替、本番運用を支えるログ戦略と設計。**ログを利用者と利用場面を持つ外部インターフェースとして扱い、業務上の問いから記録・実装・検索・受入条件を導く。** [[queries/modernization-inner-loop-reading]]と併せて、戦略、Javaの実装、検証を一貫して設計する。

対象システムの業務監査、アクセス履歴、障害調査、バッチ進捗、観測データの収集・保存はinner-loopに含む。Coding Agentの操作履歴や移行作業ワークフローの実行証跡は[[queries/modernization-outer-loop-reading]]で扱う。

## 戦略から決めること

「失敗を知らせる」「原因を調べる」「処理の完了を確認する」「旧新の差を説明する」「操作責任を確認する」では、必要な記録の粒度、到着速度、保持期間、欠落許容度が異なる。[Google SRE Workbook第4章](https://sre.google/workbook/monitoring/)は、変更前後の比較も監視の用途として挙げ、用途に応じた情報源の選択を説明する。

| 戦略上の問い | 案件で定める内容 |
|---|---|
| 誰が何を判断するか | 業務担当者、運用者、開発者、監査担当者ごとの問いと判断・対応手順 |
| どの証拠が必要か | 業務結果・状態・副作用、診断イベント、メトリクス、トレースの役割と相互の関連 |
| いつまでに使えるか | 記録から検索・通知までの遅延、詳細調査と日次・月次照合に必要な保持期間 |
| どこまで記録するか | 全件必須の記録と、サンプリング・集約・期間限定の詳細記録の区別 |
| 誰が情報を扱えるか | 記録する属性の許可、閲覧権限、機密性、改変検出、削除・保存の責任 |
| 変更時に何を保つか | 監視ルール、解析スクリプト、収集設定、監査出力の契約と互換期間 |

**ログレベルと記録目的は別の軸にする。** 業務結果、診断、アクセス、監査などの分類をseverityだけで代用しない。正常な業務拒否・入力不備、再試行中の技術的失敗、最終的な処理失敗、利用者への影響を区別する。セキュリティ上の兆候として集約すべき入力不備もある。[OWASPのイベント選定](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#which-events-to-log)を参照し、通知は対応可能性と業務影響から設計する。[SREの症状と原因の区別](https://sre.google/sre-book/monitoring-distributed-systems/)は、ERROR行数をそのまま障害・切戻し判定にしないための基礎になる。

メトリクスは影響の規模や傾向、ログは個別の事象と背景、トレースは処理の経路・時間を把握する用途に配分する。ただし媒体を固定的に分断する必要はなく、共通の文脈でつなぐ。識別子をログへ残すことと、無制限にメトリクスのラベルへ使うことは分けて設計する。ログから指標を集計する場合も欠落・重複・収集遅延を確認する。

[Site Reliability Engineering第2版](https://learning.oreilly.com/library/view/site-reliability-engineering/9798341607675/)第9章は、**障害対応用の高可用な観測と、分析用の観測**を区別する。前者は低遅延・信頼できる収集経路・単純な処理を重視し、監視対象との共通障害を避ける。後者は豊かな文脈、複雑な分析、長期履歴と費用のバランスを重視する。同じ画面や計装を使っていても、到着遅延・欠落・依存・保存の要件を分ける。二つの別製品を導入すること自体が目的ではない。

この区別を新旧比較へ適用し、切替の停止・回復を判断するSLIと、結果が分岐した理由を調べる詳細イベントをそれぞれ用意する。詳細イベントのサンプリングを許す場合でも、全件照合・業務監査に必要な記録の完全性は別に定める。

## モダナイゼーションへの適用

| 工程 | ログで解決する問い | 用意する成果物・検証 |
|---|---|---|
| 現状理解 | どの業務経路・例外・外部連携が実際に使われるか | 既存ログと利用者の棚卸し、重要フローの観測、入力・状態との対応。未観測を未使用と判断しない |
| 仕様確定 | この結果はどの判断・規則・参照データで生じたか | 安全な処理識別子、判断結果・理由コード・規則の版。観測事実と業務上の正解を区別する |
| 変更・旧新比較 | どこから結果が分岐したか | 共通入力・比較ケースIDで対応づけた結果と状態照合。内部メソッド名・ログ行の完全一致を要求しない |
| 新旧共存 | どの実装が処理し、副作用を出したか | 実装・配備の版、切替経路、業務処理ID、試行番号、外部応答の安全な要約 |
| バッチ・回復 | 何が確定済みで、どこから再開できるか | job・実行・step・attempt・checkpoint、処理／拒否／commit済み件数。再実行の記録と業務上の重複を区別する |
| 切替・本番受入 | 利用者への影響、差分、回復状況を判断できるか | SLI/SLO、診断検索、照合、切戻し条件と観測データの健全性 |

この適用は[[concepts/legacy-behavioral-parity]]と[[concepts/modernization-traceability]]に接続する。**ログは比較を説明する証拠の一部**であり、ログ上の成功だけでDBの確定状態や外部副作用の同等性を証明しない。[SREのcanary資料](https://sre.google/workbook/canarying-releases/)も、比較指標と判断基準を持つ段階的リリースを考える材料になる。

業務更新と「完了」記録のタイミングを明示する。開始・試行・適用・commit・補償を混同しない。業務確定と記録の永続化を一体にする必要がある場合は、通常のログとは別にトランザクション内の監査記録やoutbox等を検討する。[Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html)はDB更新とイベント送信の間の障害窓を扱うが、配信重複を含めた設計・検証が必要であり、一般的なloggerの代替を全案件に要求するものではない。

## Javaでの設計と実装

**業務上の出来事と出力技術を分離する。** 重要フローでは、例えば「精算が確定した」「参照データの取得に失敗した」を表す通知・観測インターフェースを設け、その実装でログ・指標・トレースへ変換する。[GOOS第20章](https://learning.oreilly.com/library/view/growing-object-oriented-software/9780321574442/ch20.html)は運用支援ログを利用者向けの機能として扱い、診断ログとの違い、通知による分離、解析ツールの互換性と検証を論じる。全loggerを包む共通ラッパーや全コードの一括改修を意味しない。

[Pete HodgsonのDomain-Oriented Observability](https://martinfowler.com/articles/domain-oriented-observability.html)は、業務の語彙によるDomain Probeと、観測内容・出力実装の検証を具体化する。HTTP・DB等の共通境界にはFilter／Interceptor／AOPや自動計装を使い、業務分岐・結果・確定状態は必要な地点で明示する。AOPだけでは業務上の観測粒度を表現しづらい場合がある。[OpenTelemetry Java agent](https://opentelemetry.io/docs/zero-code/java/agent/)の自動計装も、主に入出力等の技術的境界を対象とする。

| 設計項目 | 案件で適用するプラクティス | 一次資料 |
|---|---|---|
| 出力経路 | API→bridge→実装→appender→収集を図示し、providerの競合・不在、bridgeの循環、二重収集を確認。ライブラリのAPI依存とアプリの実装選択を分離する | [SLF4J manual](https://www.slf4j.org/manual.html)、[legacy bridges](https://www.slf4j.org/legacy.html) |
| 構造と意味 | JSON等の構文に加え、イベント名、目的、結果・理由、項目の型・単位・版を決める。messageは人の説明、安定項目は検索・集計の契約にする | [OTel Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)、[Spring Boot logging](https://docs.spring.io/spring-boot/reference/features/logging.html) |
| 文脈と相関 | trace/spanと業務処理ID・batch/run・attemptを区別。MDCは処理スコープで設定・復元し、Executor等への引継ぎと次の処理への混入を検証する | [Logback MDC](https://logback.qos.ch/manual/mdc.html)、[Log4j Thread Context](https://logging.apache.org/log4j/2.x/manual/thread-context.html) |
| 例外と通知 | causeを保ち、最終処理責任を持つ境界で結果・対応に必要な文脈とともに記録する。各層で同じ例外をログして再throwする重複や、ログして続行するだけの未処理を避ける | [GOOS第19〜20章](https://growing-object-oriented-software.com/toc.html) |
| 出力量と計算 | 出すイベントの価値・量・保持・コストを定める。パラメータ化しても引数の計算が常に遅延されるわけではない。高価な計算はSupplier等も検討し、実負荷で比較する | [SLF4J fluent API](https://www.slf4j.org/manual.html)、[Log4j async trade-offs](https://logging.apache.org/log4j/2.x/manual/async.html) |
| 収集と欠落 | stdout/file経由かOTel appender経由かを選び、同じ記録の重複送信を避ける。queue飽和、disk full、通信断、停止時flush、到着遅延の挙動を確認する | [OTel Java logging workflows](https://opentelemetry.io/docs/languages/java/instrumentation/)、[Logback AsyncAppender](https://logback.qos.ch/manual/appenders-async-sift.html) |
| 機密と監査 | 記録項目を許可方式で選び、token・password・個人情報を本文・MDC・例外・URLから除外。エンコード、権限、保持、改変検出を確認する | [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) |

**非同期ログは自動的に安全・高速になるものではない。** LogbackのAsyncAppenderには既定で低severityのイベントを捨てる条件があり、Log4jもqueue飽和・例外通知などのトレードオフを説明する。欠落不可の記録には別の要件を与える。同期出力にしても、業務commitとの原子性、収集先での永続化、改変耐性まで保証されるわけではない。

実装の分割や改名から独立した業務処理IDを残す。時刻順だけに依存せず、試行・step・原因関係で追う。仮想スレッドやreactive処理への変更では、利用フレームワークの文脈伝播方式を確認し、スレッド名を業務処理IDの代用にしない。SLF4J 2のkey-value APIも、出力実装・encoderがどう直列化するかを含めて確認する。Spring Bootの現行機能を旧版へそのまま適用せず、対象JDK・ライブラリ版・アプリサーバー制約で検証する。

## 案件の受入条件にする

運用支援・監査・旧新比較に必要な記録は契約として検証する。診断用の全ログ文字列を固定する必要はない。GOOSの「本番で診断ログを有効にしない」という強い方針は2009年の文脈を持つ。詳細診断を本番で使う場合は、通常の常時記録と分け、対象・期間・量・機密性・解除条件を定める。

1. **意味の検証:** 重要な成功・拒否・失敗・再試行・commit・回復を区別できる。業務通知と必要属性を検証する。
2. **経路の検証:** 実際のencoder・appender・収集後の記録を読み、検索可能性、必須項目、型、相関、二重出力を確かめる。loggerのmock呼出しだけで完了にしない。
3. **運用互換性:** 既存のparser・alert・ダッシュボード・監査出力を実例で照合する。意図した変更には移行手順と互換期間を持たせる。
4. **失敗の検証:** 通信断、disk full、queue飽和、権限不備、異常終了を再現し、診断記録と必須証跡それぞれの欠落・通知・業務継続条件を確認する。
5. **安全性と負荷:** 秘匿値や改行を含む入力を使い、漏洩・注入・過大出力を確認。代表負荷と障害時のログ増加で遅延・CPU・メモリ・保存量を測る。
6. **利用の検証:** コードを熟知していない運用者が、用意した事例と検索・手順で「何が失敗し、どの処理が確定し、どう対応するか」を判断できるか確認する。

[OWASPのVerification](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#verification)は出力失敗・資源枯渇・副作用を含む確認を求める。欠落・遅延・観測停止自体も検知し、記録がないことを処理成功の証拠にしない。保持期間と検索速度は、この案件の月末処理・障害の発見遅延・切替期間に合わせて定める。

## 読む目的と必要章

inner-loopのI-05「再現環境・観測・切替・本番受入」で戦略と運用を学ぶ。I-02は現行挙動の観測、I-03はログ契約・テスト、I-04はcommit・再試行、I-06はJava実装、I-07は対象システムの機密・監査を扱う。loggingは案件初期から設計する。

| 設計・運用の中核書 | 読む目的 | 必要章 |
|---|---|---|
| [Growing Object-Oriented Software, Guided by Tests](https://learning.oreilly.com/library/view/growing-object-oriented-software/9780321574442/) | 運用支援ログを利用者の要求から設計し、業務通知と出力技術を分けて検証する。I-03からI-05へ参照 | [第19章の失敗記録、第20章のLogging Is a Feature／Notification Rather Than Logging](https://growing-object-oriented-software.com/toc.html) |
| [Release It!, 2nd Edition](https://www.oreilly.com/library/view/release-it-2nd/9781680504552/) | 本番で正常・異常を判読できる状態と、運用者が必要とする情報を考える | 第8章Processes on MachinesのTransparency。共存する複数サービスの観測には第10章System-Wide Transparencyを補う |
| [Observability Engineering, 2nd Edition](https://www.oreilly.com/library/view/observability-engineering-2nd/9781098179915/) | 計装戦略、構造化イベント、業務・実行文脈、解析、段階的リリースをつなぐ中核 | 第2章、第4〜9章、第11〜12章。2026年改訂版の章番号。組織論やAgent運用の章を必読にしない |
| [The Site Reliability Workbook](https://sre.google/workbook/monitoring/) | 利用者への影響を観測し、ログと指標の役割、切替の判定を決める | 第4章Monitoring、第5章Alerting on SLOs、第16章Canarying Releases |
| [Site Reliability Engineering, 2nd Edition](https://learning.oreilly.com/library/view/site-reliability-engineering/9798341607675/) | **優先度：高。本番受入・監視を設計する案件。** SLOと観測の要求、共通障害を避ける収集、テストと回復を結ぶ | 第8〜9章、第14・17章。レガシー・ハイブリッド環境の制約は第22章。2026年刊。2016年初版とは章番号が異なる |

SRE第2版は[2026年9月刊](https://learning.oreilly.com/library/view/site-reliability-engineering/9798341607675/)で、[Googleの公開告知](https://cloud.google.com/blog/products/devops-sre/sre-book-second-edition)は2026-10-12。The Site Reliability Workbook（2018）は別書籍として実践を補う。初版のオンライン資料を参照する際は、第2版の章番号と混同しない。

| 用途で選ぶ参照書 | 優先度・適用条件 | 必要章 |
|---|---|---|
| [Logging and Log Management](https://learning.oreilly.com/library/view/logging-and-log/9781597496353/) — Chuvakin／Schmidt／Phillips、2012 | **優先度：高。** ログの利用者・記録方針・運用契約を定め直す案件で、分析、レビュー、対応、開発者の責任を学ぶ。Java設定や現在の製品選定には公式資料を使う | 第1・7・14・16・18章。旧新フォーマットの集約・正規化は第9章を必要時に参照 |
| [Learning OpenTelemetry](https://www.oreilly.com/library/view/learning-opentelemetry/9781098147174/) — Young／Parker、2024 | **優先度：条件付き。** サービス分割・新旧共存・非同期連携で、ログとtraceの相関、計装と収集を扱う案件。既存方式で要件を満たすなら導入は不要 | 第2〜5章。収集方式・機密除去・backpressureは第8章、段階的導入は第9章 |
| [Practical Monitoring](https://www.oreilly.com/library/view/practical-monitoring/9781491957349/) — Mike Julian、2017 | **優先度：入門補助。** 監視設計の基礎が不足する案件で、目的、対応可能な通知、記録項目を短く学ぶ。SRE資料と重なり、基礎を理解していれば省略できる | 第1〜3章、第7章Application Monitoring。業務指標は第5章 |

[Distributed Systems Observability](https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/)（Cindy Sridharan、2018、34ページ）は、**優先度：低、条件：短い概観が必要な場合**に第3〜4章を参照する。Observability Engineeringとの重複が多く、標準の42冊には含めない。Javaの設定は、対象版のSLF4J・Logback・Log4j公式資料を参照する。

## 読む順番

GOOS第19〜20章とDomain-Oriented Observabilityで運用要求と実装の責任境界を学び、Logging and Log Managementで戦略・運用を定める。SRE第2版第8〜9章とWorkbookで健全性判定・通知・canaryを設計し、Observability EngineeringとJava公式資料で計装・調査・検証へ落とす。分散した文脈が必要ならLearning OpenTelemetry、監視設計の基礎が不足するならPractical Monitoringを補う。

## 関連

- [[queries/modernization-reading-guide]] — inner-loopとouter-loopの入口。
- [[queries/modernization-inner-loop-reading]] — 案件実行の選書と必要章。
- [[concepts/enterprise-legacy-modernization]] — モダナイゼーションの工程と判断。
- [[concepts/legacy-behavioral-parity]] — 状態と副作用を含む同等性の検証。
- [[concepts/modernization-traceability]] — 仕様・業務判断・実行証拠の対応。
