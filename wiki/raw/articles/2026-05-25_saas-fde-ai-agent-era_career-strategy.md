---
title: "SaaSからFDEへ？——AI Agent時代のSaaSの構造変化とキャリア戦略"
source: "ユーザー提供分析（別の人の分析）"
author: "不明（外部分析者）"
date: 2026-05-25
publication: "ユーザー添付"
tags: [fde, saas, ai-agents, enterprise-ai, agent-infrastructure, career, business-model]
language: ja
type: analysis
status: ingested
---

# SaaSからFDEへ？——AI Agent時代のSaaSの構造変化とキャリア戦略

## 結論：SaaSから離れるより、「FDE化したSaaS開発者」へ寄せるのが最も期待値が高い

私なら、今すぐ「SaaSは終わるからFDEへ転職」とは考えません。
ただし、**旧来型のSaaS開発者、つまり"全顧客共通の画面と機能を作るだけの人"に留まるのは危険**だと思います。

2026年5月時点で起きていることは、SaaSの消滅ではなく、SaaSの価値単位の変化です。

これまでは、

> 画面、機能、権限、ワークフロー、レポートを、なるべく汎用的に作る

ことがSaaSの中心でした。

これからは、

> 顧客ごとの業務・データ・権限・評価基準・例外処理に接続し、AI Agentが実際に仕事を完了する状態を作る

ことが中心になります。

そのため、今後強いのは次のどちらかです。

1. **FDE的に顧客現場へ深く入り、AI Agentを業務に実装できる人**
2. **そのFDE的な知見を、再利用可能なSaaS/Platformのプリミティブに抽象化できる人**

最も希少なのは2です。
つまり、あなたが目指すべきは「SaaSを捨てて個別受託へ行く」ではなく、**FDEの筋肉を持ったAI Agentプロダクトエンジニア**です。

---

## 1. いま起きている構造変化

### 個人向けでは「汎用SaaS」より「個人ハーネス」が強くなっている

OpenClawは、自分のデバイス上で動かす個人AIアシスタントとして、WhatsApp、Telegram、Slack、Discord、Google Chat、iMessage、Teamsなど既存チャネルから使える設計を掲げています。つまり、新しい業務画面を作るのではなく、**ユーザーがすでにいる場所にAgentを常駐させる**思想です。([GitHub](https://github.com/openclaw/openclaw))

Hermes Agentも同様に、単なるチャットボットやIDE内コパイロットではなく、経験からスキルを作り、利用中に改善し、過去会話を検索し、セッションをまたいでユーザー像を深める「自己改善型」のエージェントとして設計されています。しかもモデルを差し替えられるため、特定ベンダーへのロックインを避ける方向です。([GitHub](https://github.com/nousresearch/hermes-agent))

ここで重要なのは、ユーザーごとの違いを「SaaS企業が個別機能として作る」のではなく、**メモリ、スキル、ツール接続、実行環境、チャネル設定**で吸収している点です。これはSalesforce的な管理画面カスタマイズよりも、もっとユーザー側・実行環境側に寄った変化です。

ただし、ここには強いリスクもあります。OpenClawのようにローカルファイルやコマンド実行に触れるAgentは、サードパーティスキルや権限設定を誤るとサプライチェーン攻撃や情報窃取のリスクが高くなります。実際、ClawHubの悪意あるスキル問題も報じられています。([The Verge](https://www.theverge.com/news/874011/openclaw-ai-skill-clawhub-extensions-security-nightmare))

### エンタープライズでは「プロダクトを売る」だけでは足りず、FDEが前面に出ている

OpenAIは2026年5月、OpenAI Deployment Companyを立ち上げ、Forward Deployed Engineersを顧客組織に埋め込み、重要業務の再設計から本番AIシステムの構築まで支援すると発表しました。Tomoro買収により、約150人のFDE/Deployment Specialistを初日から加える構成です。([OpenAI](https://openai.com/index/openai-launches-the-deployment-company/))

AnthropicもApplied AIのFDE職で、顧客システム内に入り、Claudeを使った本番アプリケーション、MCPサーバー、サブエージェント、Agent Skillsなどを構築し、さらに反復可能な導入パターンをProduct/Engineeringへ戻す役割を明記しています。([Anthropic](https://www.anthropic.com/careers/jobs/4985877008)) また、Blackstone、Hellman & Friedman、Goldman Sachsと組み、中堅企業向けにClaudeを重要業務へ入れるAIサービス会社も発表しています。([Anthropic](https://www.anthropic.com/news/enterprise-ai-services-company))

Google Cloudも、Gemini Enterprise Agent Platformを通じてAgentの構築・スケール・ガバナンス・最適化を包括的に扱う方向へ進んでおり、さらにGoogleのFDEがSIerと組んで企業の深い技術課題を解くと説明しています。([Google Cloud](https://cloud.google.com/blog/topics/partners/how-google-cloud-partner-ecosystem-is-building-the-agentic-enterprise))

### FDE vs SaaS の二分法は危険

今後の勝ち筋は、FDEかSaaSかではありません。より正確には、

> FDEで発見した顧客固有の業務パターンを、どれだけ早く再利用可能なプロダクト構造へ変換できるか

です。OpenAIのFDE職にも「working patternsをtools, playbooks, building blocksへcodifyする」とあり、AnthropicのFDE職にも「repeatable deployment patternsを特定・コード化し、Product/Engineeringへ戻す」とあります。一流のFDEは「個別顧客向けに何でも作る人」ではなく、**現場でしか見えない要件を発見し、再利用可能な抽象へ変換する人**です。

## 2. SaaSのレイヤー変化

| レイヤー     | 旧来SaaS           | Agent時代のSaaS                           |
| -------- | ---------------- | -------------------------------------- |
| UI       | 全顧客共通画面          | UIは薄くなり、Slack/Teams/メール/Agent UIが入口になる |
| 機能       | 共通機能を追加          | Agentがツールを呼んで業務を遂行                     |
| カスタマイズ   | 管理画面、設定、ワークフロー定義 | メモリ、スキル、ポリシー、MCP、評価セット、承認フロー           |
| マルチテナンシー | DB/計算資源共有        | Agent実行、権限、監査、コスト、評価、メモリのテナント分離        |
| 価値       | 利用席数、ログイン、画面操作   | 完了タスク、削減時間、解決件数、品質、リスク低減               |
| moat     | 機能数、UX、データ蓄積     | 業務データ、権限モデル、評価、監査、統合、導入知見              |

## 3. SaaS企業に残る価値

### System of Recordを持つSaaSは強い
ServiceNowは自社プラットフォームをAI Agentの「control tower」と位置づけ、Agent Orchestratorで複数Agentを部門横断で協調させる方向。([ServiceNow](https://www.servicenow.com/jp/company/media/press-room/ai-agents-studio.html)) WorkdayもAgent System of Recordを出し、AI Agentを登録・管理・計測し、人間の従業員と同様にライフサイクル管理する方向。([Workday](https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html))

### Agent時代のSaaSは"統治レイヤー"になれる
Deloitteは、2026年にSaaS経由のAI Agent利用が急増し、複数ベンダーや社内開発Agentの活動、使用量、コスト、アクセス、性能、セキュリティ、コンプライアンスを追跡する「control centers」やAgent marketplaceが重要になると見ています。([Deloitte](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html))

GoogleのGemini Enterprise Agent Platformも、Agent Identity、Agent Registry、Agent Gateway、Simulation、Evaluation、Observabilityといった統治・評価・可視化機能を中核に置いています。([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform))

### 価格モデルの変化
Salesforce Agentforceは、Flex Credits、Conversation課金、ユーザーライセンスなど複数の課金モデルを用意。([Salesforce](https://www.salesforce.com/agentforce/pricing/)) ZendeskはAI Agentの価格を「自律的に解決された件数」に結びつけるOutcome-Based Pricingを打ち出しています。([Zendesk](https://www.zendesk.com/newsroom/articles/zendesk-outcome-based-pricing/))

Bainも、SaaS企業がAgentic AI時代に生き残るには、データを握り、標準化をリードし、ログオンではなく成果に価格をつける必要があると述べています。([Bain](https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/))

## 4. 危険なSaaS vs 強いSaaS

### 危険なSaaS
- 単なる画面付きDB、入力フォーム、承認フロー、ダッシュボードに留まっているSaaS
- 薄いAIラッパーSaaS（LLM APIに少しUIをつけただけ）
- データ・権限・業務状態を持っていない水平SaaS

### 強いSaaS
- 顧客の業務状態を握っているSaaS（CRM、CS、会計、法務、HR、ITSM、物流、医療、金融、製造、建設）
- Agentが安全に動くための権限・監査・評価・承認を持つSaaS
- 深い業界知識をプロダクトに埋め込めるVertical SaaS
- FDEで得た知見を標準機能へ還流できるSaaS

## 5. Agent時代の個別対応はコード分岐ではなくアーティファクト分離

これからは、プロダクト本体を顧客ごとに分岐させるのではなく、以下を顧客ごとに分けます：
業務メモリ、スキル、ツール接続、権限ポリシー、承認条件、評価データセット、成功基準、例外処理ルール、プロンプト/システム指示、Agentの役割定義、コスト上限、実行ログ保持ポリシー、人間へのエスカレーションルール

**コードを顧客別に作るのではなく、Agentの"運用アーティファクト"を顧客別に持つ**。

## 6. 事業戦略

### Step 1：最初から水平汎用Agentを狙わない
OpenClaw/Hermes/Google/OpenAI/Anthropicと正面衝突する「何でもできるAgent」は避ける。

### Step 2：3社程度のDesign Partnerに深く入る
FDE的に顧客に入り込み、実際の業務を観察する。

### Step 3：「Tenant Agent Pack」を作る
顧客ごとの違いは、コード分岐ではなく、Agent Packとして管理。

### Step 4：Agent Control Planeを作る
Agent Registry、Agent Identity、権限管理、実行ログ、ツール呼び出し履歴、コスト管理、評価結果、失敗分類、人間承認、ロールバック、テナント別メモリ管理、セキュリティポリシー、監査エクスポート。

### Step 5：Pricingを席課金からずらす
per action、per resolved case、per workflow completed、per automated decision、per saved hour、base platform fee + usage、base SaaS fee + Agent outcome fee。

## 7. 開発者として身につけるべき能力

1. **業務分解能力**：FDE的能力。業務フロー、例外、判断基準、責任境界、承認、失敗時対応を聞き出せる必要がある。
2. **Agent評価設計**：task success rate、human correction rate、escalation rate、false positive/negative、cost per completed task、latency、tool failure rate、rollback rate、approval bypass rate、hallucination impact、business KPI impact。
3. **権限・監査・セキュリティ設計**：least privilege、delegated authority、user impersonationの扱い、non-human identity、audit log、approval gate、secret management、sandbox、data boundary、prompt injection対策、tool permissioning。
4. **MCP/A2Aなどの相互運用理解**：API設計ではなくAgent-facing interface設計が重要に。
5. **プロダクト抽象化能力**：FDE的に顧客の現場へ入るだけでは受託に寄る。強い人は再利用可能な抽象を抜き出す。

## 8. Gartner予測とリスク

Gartnerは、Agentic AIプロジェクトの40%以上が2027年末までに中止されると予測し、その理由としてコスト増、価値不明確、リスク管理不足を挙げています。([Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027))

McKinseyも、Agentic AI時代にはAI governance and controlsが重要になるとして、AI Trust Maturity Surveyで新たな次元として扱っています。([McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/state-of-ai-trust-in-2026-shifting-to-the-agentic-era))

## 9. 最終的な助言

SaaSから逃げる必要はない。ただし旧来のSaaS開発者のままでいてはいけない。

> SaaSの保守性・再利用性・マルチテナンシーを理解しつつ、FDEのように顧客現場へ入り、AI Agentが実際に成果を出すところまで作る。
> そして、その個別導入の知見を、Agent Pack、評価基盤、権限モデル、Control Plane、業界テンプレートとしてプロダクト化する。

## 情報源

1. OpenClaw GitHub: https://github.com/openclaw/openclaw
2. Hermes Agent GitHub: https://github.com/nousresearch/hermes-agent
3. The Verge - OpenClaw security: https://www.theverge.com/news/874011/openclaw-ai-skill-clawhub-extensions-security-nightmare
4. OpenAI Deployment Company: https://openai.com/index/openai-launches-the-deployment-company/
5. OpenAI FDE Tokyo職: https://openai.com/careers/forward-deployed-engineer-tokyo-tokyo-japan/
6. Anthropic FDE職: https://www.anthropic.com/careers/jobs/4985877008
7. Anthropic enterprise AI services company: https://www.anthropic.com/news/enterprise-ai-services-company
8. Google Cloud partner ecosystem: https://cloud.google.com/blog/topics/partners/how-google-cloud-partner-ecosystem-is-building-the-agentic-enterprise
9. ServiceNow AI Agent Orchestrator: https://www.servicenow.com/jp/company/media/press-room/ai-agents-studio.html
10. Workday Agent System of Record: https://www.workday.com/en-us/artificial-intelligence/agent-system-of-record.html
11. Deloitte - SaaS meets AI agents: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
12. Google Gemini Enterprise Agent Platform: https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
13. Salesforce Agentforce Pricing: https://www.salesforce.com/agentforce/pricing/
14. Zendesk Outcome-Based Pricing: https://www.zendesk.com/newsroom/articles/zendesk-outcome-based-pricing/
15. Bain - Will Agentic AI Disrupt SaaS?: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
16. Gartner - 40% of Agentic AI projects canceled: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
17. McKinsey - State of AI Trust 2026: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/state-of-ai-trust-in-2026-shifting-to-the-agentic-era
18. Anthropic MCP: https://www.anthropic.com/news/model-context-protocol
19. Google A2A Protocol: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
