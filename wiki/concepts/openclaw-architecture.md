---
title: OpenClawアーキテクチャ
created: 2026-05-07
updated: 2026-05-07
type: concept
tags:
  - openclaw
  - agentic-engineering
  - architecture
  - ai-agents
  - orchestration
  - context-engineering
  - security
  - sandbox
  - isolation
  - multi-agent
  - gateway
  - protocol
sources:
  - raw/articles/2026-05-07_chatgpt-openclaw-architecture-deep-dive.md
---

## 概要

OpenClawのアーキテクチャ的本質は **agent-first ではなく gateway-first** である。単一の長寿命Gatewayを中心に、チャネル接続・セッション管理・WebSocket制御面・エージェント実行・ツール実行・ノード管理・UIを束ねる **assistant control plane** として設計されている。READMEもGatewayをcontrol planeと位置づけ、アーキテクチャドキュメントも「1つのGatewayが全messaging surfaceを所有する」と明言している。

複数のフロントエンド（WhatsApp・Telegram・Slack・Discord・Signal・iMessage・WebChat）を持ちながらも、内部では **一つのcontrol planeが会話・配信・状態を統治する** モデルである。これは [[concepts/hermes-agent-architecture]] のようなagent-first設計とは根本的に異なる設計思想であり、詳細は [[comparisons/hermes-vs-openclaw-architecture]] を参照。

---

## 全体アーキテクチャ

高レベルでは以下の層で構成される：

```
チャネル/クライアント/ノード → Gateway → embedded agent runtime → tools / sessions / plugins / sandbox / nodes
```

- **チャネル層**: WhatsApp・Telegram・Slack・Discord・Signal・iMessage・WebChatなど全messaging surfaceが単一Gatewayに接続
- **クライアント層**: CLI・macOSアプリ・Web UI・automations・nodesが同一WebSocket面に接続
- **HTTP surface**: Canvas/A2UIはGateway側で提供
- **制御面**: 「どのUIから話しかけたか」よりも「Gatewayがどのsessionにどう流すか」が主役

remote setupでも同一のtunnel/auth modelの上に乗るため、一貫性のあるアーキテクチャを実現している。

---

## Gatewayが中核

Gatewayは**長寿命daemon**であり、以下の責務を担う：

- プロバイダ接続の維持
- **typed WebSocket API**の公開
- JSON Schemaによるinbound frameの検証
- `agent`、`chat`、`presence`、`health`、`heartbeat`、`cron`などのイベント発行
- **単一ホスト不変条件**（1ホストに1 Gateway、WhatsApp sessionはそのhost上のGatewayだけが開く）

README上でもOpenClawは常駐Gatewayを立て、その上に全chat surfaces、CLI、WebChat、macOS app、iOS/Android nodesを接続する形で説明されている。したがってOpenClawを理解する際は、model providerやpromptではなく、**Gatewayを中心にした分散assistant runtime**と見るのが正しい。

---

## WebSocketプロトコル

通信モデルは**WebSocket制御面**として設計されている：

- Transport: WebSocketのtext JSON frame
- 最初のframeは必ず`connect`
- 以後は`req/res`と`event`の形でフロー
- `hello-ok.features.methods/events`がdiscovery metadata
- TypeBox schemasからJSON Schemaが生成され、Swift modelsもそこから生成される——protocol typingを真面目に扱っている

### 認証とデバイスアイデンティティ

- shared secretのtoken/passwordに加え、Tailscale Serveやtrusted proxyのidentity headersも使用可能
- **device identityとpairing**が別途存在：全WS clientは原則`device` identityを持って`connect`し、server-provided challengeへの署名が必要
- loopbackの一部はauto-approvalされるが、tailnetやLANは同一マシン起点でもremote扱いでpairing承認が必要

このためOpenClawのWSは単なるRPC pipeではない。**認証・デバイス識別・pairing・イベント配信**まで含むcontrol-plane protocolである。また「events are not replayed; clients must refresh on gaps」と明言されており、protocol自体がdurable event logではなく、**live control channel**として設計されている。

---

## エージェントランタイム（埋め込み型）

agent実行は外部プロセス起動ではなく、**pi SDKの埋め込み**である：

- piをsubprocessやRPC modeで起動せず、`createAgentSession()`を介してpiの`AgentSession`を直接import/instantiate
- この方式により、session lifecycle、event handling、tool injection、system prompt customization、session persistence、auth/profile rotation、provider-agnostic model switchingをOpenClaw側が掌握
- `runEmbeddedPiAgent()`が主入口：workspace、session file、provider/model、timeout、runId、block reply callbackなどを受けてagent runを実行

**runtime boundary**も明瞭で、agent runtime自体はPi coreに依存するが、**session management、discovery、tool wiring、channel deliveryはOpenClaw-owned**とドキュメントが明記している。OpenClawはpiを使ってはいるが、上位のorchestrationを相当量自前で持っている。

---

## エージェントループ

Agent Loopは以下のように定義される：

**intake → context assembly → model inference → tool execution → streaming replies → persistence**

- `agent` RPCはsessionを解決してmetadataを保存し、即座に`{ runId, acceptedAt }`を返す
- その後`agentCommand`がmodel/thinking/skills snapshotを解決して`runEmbeddedPiAgent()`を呼ぶ
- `agent.wait`はその`runId`のlifecycle end/errorを待つ別経路

### streamingとpersistenceの一体化

`subscribeEmbeddedPiSession`がpi-agent-coreのeventをOpenClawの`assistant`/`tool`/`lifecycle` streamに橋渡しし、tool start/update/end、assistant delta、compaction、errorまでliveに流す。Gatewayは最終回答を受け取るだけでなく、runの過程全体をevent streamとして観測する。

### フックシステム

Gateway hooksとplugin hooksの二系統があり、以下のポイントでエージェントループに介入可能：

- `agent:bootstrap`、command hooks
- `before_model_resolve`、`before_prompt_build`、`before_agent_reply`
- `before_tool_call`、`after_tool_call`、`tool_result_persist`
- `session_start/end`

OpenClawは「モデル呼び出し器」ではなく、**agent lifecycleを拡張可能な実行基盤**である。

---

## セッション管理

「**Source of truth: the Gateway**」——UIはsession listやtoken countをGatewayに問い合わせるべきで、remote modeではlocal machineを見ても実際の状態は分からない。

### 二層永続化

1. **`sessions.json`**: `sessionKey -> SessionEntry`の小さなmutable store。現在のsession id、last activity、toggles、token countersなどのmetadataを保持
2. **`<sessionId>.jsonl`**: append-only transcript。`id`と`parentId`を持つtree構造で、message/toolResult/compaction/branch summaryなどを保存

これにより**軽いsession registry**と**重いtranscript persistence**を分離している。transcriptはPiの`SessionManager`を使いつつ、OpenClaw側でguard/caching/history limiting/compactionを載せている。per-agent transcript pathも`~/.openclaw/agents/<agentId>/sessions/...`に固定される。

---

## ワークスペース

agentごとにworkspaceを持ち、toolsとcontextの`cwd`になる。`agents.defaults.workspace`はrequired。

### ブートストラップファイル

`AGENTS.md`、`SOUL.md`、`TOOLS.md`、`BOOTSTRAP.md`、`IDENTITY.md`、`USER.md`などのuser-editable filesをseedする。

### プロンプト注入

workspaceのファイルはpromptに自動注入される。system promptにはProject Contextとしてbootstrap filesがtrimmed/truncatedされて毎ターン入る。`MEMORY.md`もinjectされるが、`memory/*.md`のdaily filesはtool経由のon-demand。

- per-file / totalで文字数上限あり
- `/context list`や`/context detail`で負荷を確認可能

つまりworkspaceは、**人格・作業規約・所有者情報・局所記憶をprompt常駐ファイルとして管理する方式**である。

---

## システムプロンプト

OpenClawは**every agent runごとにcustom system promptを組み立てる**。それは**OpenClaw-owned**であり、pi-coding-agent default promptを使わない。

### provider pluginの介入

provider pluginsはprompt全体を乗っ取るのではなく、以下のcore sectionsの差し替えやcache boundaryを意識したstable prefix/dynamic suffixの追加を行う：
- `interaction_style`
- `tool_call_style`
- `execution_bias`

### platform-orientedな構成

Tooling、Safety、Skills、Self-Update、Workspace、Documentation、Workspace Files、Sandbox、Time、Reply Tags、Heartbeats、Runtime、Reasoningといった固定セクションを持ち、cronの使い方、background processの扱い、subagent待ちのpoll回避、approval UI優先まで埋め込まれる。promptはpersona文というより、**runtimeの操作マニュアル兼policy hint**である。

### sub-agent用minimal mode

`promptMode=minimal`では、Skills、Memory Recall、Self-Update、User Identity、Messaging、Heartbeatsなどを落として小さくする。bootstrap file注入も`AGENTS.md`と`TOOLS.md`に絞られる。**prompt sizeとcache stabilityを明示的に最適化**している。

---

## ツール実行（Sandbox / Tool Policy / Elevatedの分離）

実行安全性は1つのスイッチでは決まらない。**Sandbox / Tool Policy / Elevatedは別物**：

| 概念 | 制御内容 |
|------|----------|
| Sandbox | 「どこで実行するか」 |
| Tool Policy | 「何を使わせるか」 |
| Elevated | 「sandboxからhostにescapeさせるか」 |

### exec tool

- `host=auto|sandbox|gateway|node`
- `security=deny|allowlist|full`
- `ask=off|on-miss|always`

sandbox中なら基本はsandbox、必要に応じてgateway/node hostに出られる。approvalが必要な場合はimmediately `approval-pending`を返し、その後`Exec finished`/`Exec denied`のsystem eventがsessionに流れる。

### sandboxing

単純なDocker jailではなく：
- mode: `off|non-main|all`
- scope: `agent|session|shared`
- backend: `docker|ssh|openshell`
- workspace access: `none|ro|rw`
- browserまでsandbox側で動作可能

elevatedはsandbox外へ出るexec-only escape hatchで、`/elevated on|ask|full|off`によってper-sessionで制御。OpenClawはprompt上のsafetyに頼り切らず、**hard stopはtool policy・exec approvals・sandbox・channel allowlistsでやる**と明言している。

---

## ノード

nodesは同じWS serverに`role: node`で接続し、capabilityを広告する：

- `canvas.*`、`camera.*`、`screen.record`、`location.get`
- headless node hostなら`system.run`/`system.which`をそのマシン上でexpose
- browser proxyも自動広告

### device identityとpairing

Gatewayがmembershipのsource of truthで、pending request → approval → token issuanceのflowを持つ。2026.3.31以降はnode pairing承認前はdeclared node commandsが無効化され、device pairingだけではcommand surfaceが出ない。

nodesは単なるremote shellではなく、**device identityとcommand trustをGateway側で仲裁するcapability surface**である。exec approvalsもnode host側に存在し、per-agent allowlistと組み合わさる。

---

## キューイング

OpenClawのqueueは後付けではなく、**agent architectureの一部**である：

- inbound auto-reply runsはtiny in-process queueに入る
- **session lane**と**global lane**で直列化
- `runEmbeddedPiAgent`は`session:<key>`にenqueueされ、さらに`main` laneにも通る
- 同一sessionのraceを防ぎつつ、全体並列度も`agents.defaults.maxConcurrent`で抑制

### queue mode

`collect`、`followup`、`steer`、`steer-backlog`、`interrupt`をper-channel/per-sessionで切り替え可能：

- `collect`: follow-upでまとめる
- `steer`: 次のtool boundary/model boundaryでcurrent runに注入

これは単なるmessage bufferではなく、**実行中のagent runと新着messageの整合を取るorchestration policy**である。

---

## サブエージェント

既存runからspawnされるbackground agent run：

- 独自session `agent:<agentId>:subagent:<uuid>`を持つ
- 終了時にrequester chatへannounce
- 各sub-agent runはbackground taskとして追跡され、専用queue lane `subagent`を持つ

### spawn制御

- デフォルトではsub-agentはさらに子をspawnできない
- `maxSpawnDepth: 2`でmain → orchestrator sub-agent → worker sub-sub-agentsが可能
- tool policyもdepthで変化：通常sub-agentはsession/system toolsを持たず、depth-1 orchestratorだけ追加のsession toolsを持てる

設計思想はGateway-first：Claude Codeのforkのような親文脈継承中心ではなく、**background run / session tree / announce chain**として管理される。announceはbest-effortで、Gateway restartでpending announce workは失われうる。

---

## プラグインシステム

4層アーキテクチャで構成される：

1. **Manifest + discovery**
2. **Enablement + validation**
3. **Runtime loading**
4. **Surface consumption**

discoveryやconfig validationはmanifest/schemaだけで成立し、native runtime behaviorは`register(api)`に任せるboundaryが明確。

### 実行モデル

native pluginsはGatewayと**同一プロセス内**で`jiti`経由でloadされ、sandboxはされない——trust boundary的にはcore codeと同格。

### capability register API

text inference、speech、media understanding、image generationなどのcapability register APIが用意され、plugin shapeも以下のように分類される：
- plain-capability
- hybrid-capability
- hook-only
- non-capability

provider pluginについては、generic agent loop・failover・transcript handling・tool policyはcoreが持ち、provider固有差分だけhook surfaceで渡す。plugin systemは「便利add-on」ではなく、**platformのpublic extension ABI**に近い。

---

## スキル

AgentSkills-compatibleな`SKILL.md`フォルダで、bundled・managed・workspaceなど複数のsourceからロードされる。

**索引注入パターン**：system promptにはskillのinstructions本体ではなく、**name / description / locationを持つcompact list**だけがinjectedされ、必要になったらmodelが`read`で`SKILL.md`を開く想定。

これはtoken設計として優れており、skillsを常時全部promptに突っ込まず、**metadataだけ常駐、本文はdemand-load**にしている。OpenClawのdocsはskill listのdeterministic overheadまで説明しており、context pressureをかなり意識している。

---

## セキュリティ

OpenClawは**personal assistant trust model**を前提としており、hostile multi-tenant boundaryではない：

- 1 Gatewayあたり1 trusted operator boundaryを想定
- 複数のadversarial userを同じgateway/agentに載せる構成は非推奨
- hostと`~/.openclaw`を触れる者はtrusted operatorとみなされる

この前提はアーキテクチャ全体に浸透している：
- native pluginsはunsandboxed
- Gatewayはstateのsource of truth
- execはhost/nodeに出られる
- channel surfaceは実メッセージングに繋がる

OpenClawは「強いtenant isolationを提供するSaaS platform」ではなく、**自分用・自分管理のassistant OS**に近い。これは欠点というより設計目標の違いである。

---

## まとめ

OpenClawのアーキテクチャを一言で言い切るなら：

> **「長寿命Gatewayを中心に、埋め込みagent runtime、typed WS protocol、session/transcript persistence、sandbox/approvals、nodes、pluginsを束ねたassistant control plane」**

強み：
- control planeが明確で、protocolとplugin boundaryが型付けされている
- queue・session・sandbox・approvalsが運用的に整理されている

トレードオフ：
- Gateway hostが大きなtrust bottleneckになる
- native pluginsは高信頼コード扱い
- workspace/bootstrap注入はtoken pressureを増やす

アーキテクチャ理解のための推奨読書順: `Gateway protocol` → `Agent loop` → `Pi integration architecture` → `System prompt` → `Command queue` → `Plugin architecture` → `Sandboxing / Security`

### 関連ページ

- [[concepts/hermes-agent-architecture]] — Hermes Agentの対照的アーキテクチャ（agent-first設計）
- [[comparisons/hermes-vs-openclaw-architecture]] — agent-first vs gateway-firstの設計思想比較
- [[concepts/openclaw/_index]] — OpenClaw コンセプトクラスターインデックス
- [[concepts/openclaw/philosophy]] — OpenClaw 設計哲学
- [[concepts/openclaw/five-tier-precedence]] — OpenClaw 5層優先順位モデル
- [[entities/openclaw]] — OpenClawプロジェクト概要
- [[entities/peter-steinberger]] — OpenClaw作者
- [[entities/nvidia-nemoclaw]] — OpenClawをバンドルしたNVIDIAのセキュアエージェントフレームワーク
- [[entities/pi-coding-agent]] — OpenClawが埋め込むpi-agent-core
