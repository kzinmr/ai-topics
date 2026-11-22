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

# Modernization Inner-loop Reading — Project Execution

[O'Reilly: inner-loop / project execution](https://learning.oreilly.com/playlists/881eb67b-8276-489e-ad26-d009b8b2a34f/) · [[queries/modernization-reading-guide|Reading guide entry point]]

42 books in 7 categories for safely migrating an individual Java / enterprise system. Automated transformation tools and Agents are treated as instruments for advancing the project. Includes the target system's logging strategy, design, and operations, connecting discovery through production acceptance.

[[queries/modernization-inner-loop-sources|Public availability, licensing, raw source materials]] · [[queries/modernization-inner-loop-study-notes|Reading scope and findings]] · [[concepts/legacy-modernization-moc|Guide to key concepts]]

Account-free learning: [concept study guide](modernization-independent-study-guide.md), [worked exercise](modernization-batch-example.md), and [[queries/modernization-reading-continuation|priority-reading continuation]].

## Reading order to start with

1. **Working Effectively with Legacy Code** — Establish evidence of existing behavior and create boundaries that can be changed.
2. **Specification by Example** — Turn SME judgments into concrete examples and acceptance criteria. If interviews and rule elicitation are hard, supplement with the additional books in I-02.
3. **Monolith to Microservices** — Decide incremental migration, old/new coexistence, and cutover units.
4. **Effective Software Testing** — Build independent verification from specifications, boundary values, and properties.
5. **Building Evolutionary Architectures** — Turn the design characteristics you must protect into measurable constraints.
6. **Continuous Delivery** and **Release It!** — Connect reproducible environments, acceptance, cutover, and production recovery.

For Refactoring, see I-01 for the principles of small transformations and the catalog. How to build verification scaffolding for untested code, and how to decide business-correct answers, are covered by the first two books. Consult I-06 according to the project's Java risks, and I-07 from the very start of the project.

For logging, learn the separation of operational requirements and implementation in GOOS chapters 19-20, strategy in Logging and Log Management, health assessment in SRE 2nd Edition and the Workbook, and instrumentation and investigation in Observability Engineering. Choose additional references by the priority and conditions in each row. See [[queries/modernization-java-logging]] for details.

Books marked "Shared" also appear on other reading lists, but here read only the purpose and chapters specified in this table. "No required chapters specified" does not mean read the whole book — consult the entries relevant to your use case. Recheck old APIs and JVM settings against the target JDK.

## I-01 Strategy, Scope, and Incremental Change

Decide the migration targets, boundaries, order, and completion conditions, and proceed with small changes. Learn behavior-preserving transformations through Refactoring. Do not treat microservice adoption itself as the goal.

| Book / Material | Purpose of Reading and Cautions | Required Chapters |
|---|---|---|
| [Working Effectively with Legacy Code](https://learning.oreilly.com/library/view/-/0131177052/)<br>[Amazon.com](https://www.amazon.com/dp/0131177052/) | Characterization tests that pin down pre-change behavior, and seams that cut dependencies to make code testable. Evidence the existing behavior rather than relying only on SMEs' memory. Whether the current behavior is the correct business specification, however, is judged separately. | No required chapters specified. Consult as the target's issues require. |
| [Monolith to Microservices](https://learning.oreilly.com/library/view/-/9781492047834/)<br>[Amazon.com](https://www.amazon.com/dp/1492047848/) | Incremental replacement, old/new coexistence, boundaries, data partitioning, and trade-offs during migration. Material for designing Codex work units and release units. Do not assume microservice adoption; choose the migration patterns actually needed. | No required chapters specified. Consult as the target's issues require. |
| [Shared][Building Evolutionary Architectures, 2nd Edition](https://learning.oreilly.com/library/view/-/9781492097532/)<br>[Amazon.com](https://www.amazon.com/dp/1492097543/) | Define the design characteristics to protect in this migration, such as dependency direction and performance, along with incremental change. Choose testable constraints and record business judgments that cannot be measured separately. | Chapters 1-3 (evolution, fitness functions, small changes), Chapters 5-7 (structure, data, migrating existing structures) |
| [Architecture Modernization](https://learning.oreilly.com/library/view/-/9781633438156/)<br>[Amazon.com](https://www.amazon.com/dp/1633438155/) | Connect business strategy, organization, and technology change to decide migration targets and order. Apply to designing SME involvement so it concentrates on boundary decisions and open items. A 2024 companion book. | No required chapters specified. Consult as the target's issues require. |
| [Refactoring: Improving the Design of Existing Code](https://learning.oreilly.com/api/v1/continue/9780134757681/)<br>[Amazon.com](https://www.amazon.com/dp/0134757599/) | Vocabulary for behavior-preserving small transformations, their motivations, and verification procedures. Read the early principles and consult the catalog when needed. Also applicable to decomposing work for Agents, but DB migration, production cutover, and recovery of business specifications are still needed separately. Passing tests alone does not prove equivalence across all inputs. | No required chapters specified. Consult as the target's issues require. |
| [Shared][Kill It with Fire](https://learning.oreilly.com/library/view/kill-it-with/9781098128883/)<br>[Amazon.com](https://www.amazon.com/dp/1718501188/) | Define the migration value, scope, alternatives, and completion conditions under which the old platform can be retired. Keep status quo and partial replacement as options too. | Chapter 3 (assessing structure), Chapter 5 (measurable problems, scope, opportunity cost), Chapter 9 (completion and success criteria) |

## I-02 Current-State Understanding, Business Specifications, and Basis for Correct Answers

Determine specifications from code history and execution results, business scenarios, and SME judgments. Inventory the existing logs along with their users, parsers, and notifications, and observe the critical business paths. Distinguish observed legacy behavior, business rules to preserve, and acceptance evidence, and do not judge something as unused merely because it was not observed.

| Book / Material | Purpose of Reading and Cautions | Required Chapters |
|---|---|---|
| [Shared][Specification by Example](https://learning.oreilly.com/library/view/-/9781617290084/)<br>[Amazon.com](https://www.amazon.com/dp/1617290084/) | Reach agreement with SMEs on this project's business rules through concrete examples, turning them into independent expected values and acceptance specifications. Do not unconditionally treat current behavior as correct, and verify the basis for Agent-generated expected values. | Chapters 5-8 (scope, collaborative specification, concrete examples, refining specifications), Chapter 9 (automating verification without changing the specification) |
| [Your Code as a Crime Scene, Second Edition, 2nd Edition](https://learning.oreilly.com/library/view/-/9798888650837/)<br>[Amazon.com](https://www.amazon.com/dp/B0CSJR386C/) | Investigate priorities and hidden dependencies from change history, hotspots, and change couplings. Material for narrowing down the questions to ask SMEs. Because history also reflects past development practices, distinguish it from business criticality itself. | No required chapters specified. Consult as the target's issues require. |
| [Learning Domain-Driven Design](https://learning.oreilly.com/library/view/-/9781098100124/)<br>[Amazon.com](https://www.amazon.com/dp/1098100131/) | Organize business terminology, subdomains, and bounded contexts, and slice migration units by business capability rather than lines of code. The foundation for reusing SME judgments as glossaries, boundaries, and rules. | No required chapters specified. Consult as the target's issues require. |
| [Software Requirements, 3rd Edition](https://learning.oreilly.com/library/view/-/9780735679658/)<br>[Amazon.com](https://www.amazon.com/dp/B00JDMPMOA/) | Extract, validate, and prioritize this project's requirements, and record retain/change/retire/unresolved status along with source, decision maker, and acceptance conditions. A dictionary-like reference consulted from the required chapters for requirements management. | No required chapters specified. Consult as the target's issues require. |
| [Domain Storytelling: A Collaborative, Visual, and Agile Way to Build Domain-Driven Software](https://learning.oreilly.com/library/view/domain-storytelling-a/9780137458974/)<br>[Amazon.com](https://www.amazon.com/dp/B099ZNXCJT/) | Elicit this project's business scenarios from SMEs and share the participants, information, work, and exceptions. Agreement on the correctness of business rules is recorded separately. | Chapters 3-4 (scenarios and scope), Chapter 6 (workshops), Chapters 11 & 15 (requirements, hidden IT) |
| [Business Rules and Information Systems: Aligning IT with Business Goals](https://learning.oreilly.com/library/view/business-rules-and/0201743914/)<br>[Amazon.com](https://www.amazon.com/dp/B003YL3OZU/) | Make this project's business rules explicit, inspect them for contradictions and ambiguity, and use them as the basis for acceptance decisions. A 2002 classic. Prioritize the principles for handling rules over the technology examples. | Chapters 3-5 (defining, discovering, and quality-managing rules) |

## I-03 Making Changes and Verifying Behavioral Equivalence

Covers code changes, the use of automated transformation and Agents, independent expected values, and verification by boundary values, properties, and models. Also verify the meaning and required attributes of operations-support logs, and their compatibility with existing parsers, as a contract. Do not pin every diagnostic log string, and do not decide acceptance based only on an Agent's explanation.

| Book / Material | Purpose of Reading and Cautions | Required Chapters |
|---|---|---|
| [Effective Software Testing](https://learning.oreilly.com/library/view/-/9781633439931/)<br>[Amazon.com](https://www.amazon.com/dp/1633439933/) | Combine specifications, boundary values, pre- and postconditions, invariants, and property-based testing. Taught with Java examples but the principles are language-independent. Use it to design an independent verification strategy for Agent-generated code. | No required chapters specified. Consult as the target's issues require. |
| [xUnit Test Patterns: Refactoring Test Code](https://learning.oreilly.com/library/view/-/9780131495050/)<br>[Amazon.com](https://www.amazon.com/dp/0131495054/) | A reference covering fixtures, test doubles, and test smells. Look at independence, maintainability, and clarity of failure causes rather than the volume of generated tests. Read the patterns rather than the notation of old frameworks. | No required chapters specified. Consult as the target's issues require. |
| [Growing Object-Oriented Software, Guided by Tests](https://learning.oreilly.com/library/view/-/9780321574442/)<br>[Amazon.com](https://www.amazon.com/dp/0321503627/) | Learn behavior, collaboration, and testable boundaries through Java examples. Design operations-support logging as a user-facing feature, separating business notification from the output technology. Also verify real connections and real output. | For logging, Chapter 19 (recording failures) and Chapter 20 (Logging Is a Feature / Notification Rather Than Logging). For other design and testing topics, consult by issue |
| [Practical TLA+: Planning Driven Development](https://learning.oreilly.com/library/view/-/9781484238295/)<br>[Amazon.com](https://www.amazon.com/dp/1484238281/) | Verify invariants under state transitions, concurrent execution, and failure using models. Useful for checking designs such as fund transfers, job reruns, and cutovers. The correctness of the model and whether the implementation follows it must be verified separately. | No required chapters specified. Consult as the target's issues require. |
| [Beyond Vibe Coding](https://learning.oreilly.com/library/view/-/9798341634749/)<br>[Amazon.com](https://www.amazon.com/dp/B0F6S5425Y/) | Make intent explicit for this project's Agent use, split changes small, and accept output only after design, testing, and review. Do not equate a high degree of autonomy with the assurance needed to entrust a production migration. | No required chapters specified. Consult as the target's issues require. |
| [Shared][Automated Code Refactoring and Modernization with OpenRewrite](https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/)<br>[Amazon.com](https://www.amazon.com/dp/1808347838/) | Select existing recipes for this Java update, confirm the applicability conditions and diff, then apply the transformation. A new title from September 2026. Even when the transformation is deterministic, business-level equivalence is verified separately. | Chapters 1-4 (introduction, concepts such as LST, execution, using recipes) |

## I-04 Data, Transactions, and External Integration

Confirm data ownership, schema changes, compatibility periods, external contracts, retries, and duplicate processing. Distinguish a log's "success" from the DB commit, and reconcile old and new including state, side effects, and failure recovery. If atomicity between business confirmation and the audit trail is required, consider audit records inside the transaction or a [Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html).

| Book / Material | Purpose of Reading and Cautions | Required Chapters |
|---|---|---|
| [Refactoring Databases: Evolutionary Database Design](https://learning.oreilly.com/library/view/-/0321293533/)<br>[Amazon.com](https://www.amazon.com/dp/0321293533/) | Patterns for evolving DB schema and data in small steps. Design the compatibility period, simultaneous migration with the application, reconciliation, and rollback conditions. Note that rolling back only the code does not roll back data that has already been written. | No required chapters specified. Consult as the target's issues require. |
| [Designing Data-Intensive Applications, 2nd Edition](https://learning.oreilly.com/library/view/-/9781098119058/)<br>[Amazon.com](https://www.amazon.com/dp/1098119061/) | Organize the trade-offs of consistency, transactions, replication, and distributed processing. The foundation for thinking about data ownership, retries, and failure recovery during old/new coexistence. The 2026 revision of a standard text. | No required chapters specified. Consult as the target's issues require. |
| [Shared][Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions](https://learning.oreilly.com/library/view/-/0321200683/)<br>[Amazon.com](https://www.amazon.com/dp/0321200683/) | Organize the contracts, correlation, transformation, and duplicate handling of this project's batches, queues, and external systems. Read the integration patterns and failure modes rather than the dated product examples. | Chapters 3-5 (messaging foundation, channels, configuration), Chapters 7-8 (routing, transformation), Chapter 10 (endpoints) |
| [Patterns of Enterprise Application Architecture](https://learning.oreilly.com/library/view/-/0321127420/)<br>[Amazon.com](https://www.amazon.com/dp/0321127420/) | A classic that classifies business logic, persistence, transaction boundaries, and more. Use the Java / .NET examples as vocabulary for describing the structure of existing code. This is not a book for porting old APIs as they are. | No required chapters specified. Consult as the target's issues require. |

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
