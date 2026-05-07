公式 docs とリポジトリ README をベースにすると、OpenClaw は「LLM にツールを付けたアプリ」よりも、**単一の長寿命 Gateway を中心に、チャネル接続・セッション・WS 制御面・agent 実行・ツール・ノード・UI を束ねる assistant platform** として設計されています。README も Gateway を control plane と位置づけ、アーキテクチャ docs も「1つの Gateway が全 messaging surface を所有する」と明言しています。 ([GitHub][1])

私の見立てを一言で言うと、OpenClaw の本質は **agent-first ではなく gateway-first** です。agent loop はもちろん重要ですが、それは Gateway の中に埋め込まれた authoritative execution path であって、外側では WS protocol、pairing、routing、queue、sandbox、plugin registry、nodes、Control UI が一体の制御面を形成しています。 ([OpenClaw][2])

## 全体像

高レベルには、OpenClaw は次のような層で見ると理解しやすいです。
**チャネル/クライアント/ノード** → **Gateway** → **embedded agent runtime** → **tools / sessions / plugins / sandbox / nodes**。
Gateway architecture docs では、WhatsApp・Telegram・Slack・Discord・Signal・iMessage・WebChat などの messaging surface を単一 Gateway が持ち、CLI・macOS app・web UI・automations・nodes が同じ WebSocket 面にぶら下がる構図になっています。Canvas/A2UI も Gateway 側の HTTP surface で提供されます。 ([OpenClaw][2])

この設計の意味は、「どの UI から話しかけたか」よりも、「Gateway がどの session にどう流すか」が主役になることです。WebChat も Control UI も Gateway の WS API を直接使い、remote setup でも同じ tunnel / auth model の上に乗ります。つまり OpenClaw は、複数の front-end を持っていても、内部では **一つの control plane が会話・配信・状態を統治する** モデルです。 ([OpenClaw][3])

## 1) Gateway が中核

Gateway は長寿命 daemon で、provider 接続を維持し、typed WebSocket API を公開し、JSON Schema で inbound frame を検証し、`agent`、`chat`、`presence`、`health`、`heartbeat`、`cron` などのイベントを出します。1ホストに1 Gateway という前提で、特に WhatsApp session はその host 上の Gateway だけが開く、という invariant も docs にあります。 ([OpenClaw][2])

この「Gateway 中心」は README の表現にも出ていて、OpenClaw は常駐 Gateway を立て、その上に chat surfaces、CLI、WebChat、macOS app、iOS/Android nodes を接続する形で説明されています。だから OpenClaw を理解するときは、まず model provider や prompt ではなく、**Gateway を中心にした分散 assistant runtime** と見たほうが全体像を掴みやすいです。 ([GitHub][1])

## 2) 通信モデルは WebSocket 制御面

プロトコル面では、Transport は WebSocket の text JSON frame で、最初の frame は必ず `connect` です。以後は `req/res` と `event` の形で流れ、`hello-ok.features.methods/events` は discovery metadata です。TypeBox schemas から JSON Schema が生成され、さらに Swift models もそこから生成されるので、OpenClaw は protocol typing をかなり真面目に扱っています。 ([OpenClaw][2])

接続認証も一段厚いです。shared secret の token/password に加えて、Tailscale Serve や trusted proxy の identity headers も使えますが、**device identity と pairing** が別にあります。すべての WS client は原則 `device` identity を持って `connect` し、server-provided challenge への署名も必要です。loopback の一部は auto-approval されますが、tailnet や LAN は同一マシン起点でも remote 扱いで pairing 承認が必要です。 ([OpenClaw][4])

このため、OpenClaw の WS は単なる RPC pipe ではありません。**認証・デバイス識別・pairing・イベント配信**まで含む control-plane protocol です。しかも docs は「events are not replayed; clients must refresh on gaps」と明言しており、protocol 自体が durable event log ではなく、**live control channel** として設計されています。 ([OpenClaw][2])

## 3) agent runtime は「埋め込み型」

agent 実行は外部プロセス起動ではなく、pi SDK の埋め込みです。Pi Integration Architecture によると、OpenClaw は pi を subprocess や RPC mode で起動せず、`createAgentSession()` を介して pi の `AgentSession` を直接 import / instantiate します。この方式により、session lifecycle、event handling、tool injection、system prompt customization、session persistence、auth/profile rotation、provider-agnostic model switching を OpenClaw 側が握れます。 ([OpenClaw][5])

ここがかなり重要で、OpenClaw は「外部 agent を呼ぶ gateway」ではなく、**pi-agent-core を内蔵した platform** です。docs 上の `runEmbeddedPiAgent()` は、そのための主入口で、workspace、session file、provider/model、timeout、runId、block reply callback などを受けて agent run を実行します。 ([OpenClaw][5])

そして runtime boundary も明瞭です。agent runtime 自体は Pi core に依存しますが、**session management、discovery、tool wiring、channel delivery は OpenClaw-owned** と docs が明記しています。つまり OpenClaw は pi を使ってはいるが、上位の orchestration を相当量自前で持っています。 ([OpenClaw][6])

## 4) agent loop は authoritative path

Agent Loop docs は、OpenClaw の agentic loop を「intake → context assembly → model inference → tool execution → streaming replies → persistence」と定義しています。`agent` RPC は session を解決して metadata を保存し、即座に `{ runId, acceptedAt }` を返し、その後 `agentCommand` が model/thinking/skills snapshot を解決して `runEmbeddedPiAgent()` を呼びます。`agent.wait` はその `runId` の lifecycle end/error を待つ別経路です。 ([OpenClaw][7])

この loop の面白い点は、**streaming と persistence が一体**になっていることです。`subscribeEmbeddedPiSession` が pi-agent-core の event を OpenClaw の `assistant` / `tool` / `lifecycle` stream に橋渡しし、tool start/update/end、assistant delta、compaction、error まで live に流します。つまり Gateway は単に最終回答を受け取るのではなく、run の過程全体を event stream として観測します。 ([OpenClaw][7])

hook もここに食い込みます。Gateway hooks と plugin hooks の二系統があり、`agent:bootstrap` や command hooks に加え、`before_model_resolve`、`before_prompt_build`、`before_agent_reply`、`before_tool_call`、`after_tool_call`、`tool_result_persist`、`session_start/end` などで loop に介入できます。これは OpenClaw が「モデル呼び出し器」ではなく、**agent lifecycle を拡張可能な実行基盤** であることを示しています。 ([OpenClaw][8])

## 5) セッション管理は Gateway が source of truth

Session Management deep dive はかなり露骨に、「**Source of truth: the Gateway**」と書いています。UI は session list や token count を Gateway に問い合わせるべきで、remote mode では local machine を見ても実際の状態は分かりません。これは OpenClaw が state をクライアントに散らさず、Gateway に集約していることの表現です。 ([OpenClaw][9])

永続化は二層です。
1つ目は `sessions.json` で、`sessionKey -> SessionEntry` の小さな mutable store。現在の session id、last activity、toggles、token counters などの metadata を持ちます。
2つ目は `<sessionId>.jsonl` の append-only transcript で、`id` と `parentId` を持つ tree 構造、message/toolResult/compaction/branch summary などを保存します。 ([OpenClaw][9])

これにより、OpenClaw は **軽い session registry** と **重い transcript persistence** を分離しています。しかも transcript は Pi の `SessionManager` を使いつつ、OpenClaw 側で guard/caching/history limiting/compaction を載せています。per-agent transcript path も `~/.openclaw/agents/<agentId>/sessions/...` に固定され、multi-agent 構成でもセッション境界が比較的明快です。 ([OpenClaw][9])

## 6) workspace は単なるフォルダではなく prompt の一部

OpenClaw は agent ごとに workspace を持ち、それが tools と context の `cwd` になります。docs は `agents.defaults.workspace` を required としており、bootstrap では `AGENTS.md`、`SOUL.md`、`TOOLS.md`、`BOOTSTRAP.md`、`IDENTITY.md`、`USER.md` などの user-editable files を seed します。 ([OpenClaw][6])

この workspace の特徴は、ファイルが prompt に自動注入されることです。OpenClaw の system prompt には Project Context として bootstrap files が trimmed/truncated されて毎ターン入ります。`MEMORY.md` もある場合は injected されますが、`memory/*.md` の daily files は tool 経由の on-demand です。per-file / total で文字数上限もあり、`/context list` や `/context detail` でその負荷を見られます。 ([OpenClaw][10])

つまり workspace は、Hermes のような巨大 memory store ではない代わりに、**人格・作業規約・所有者情報・局所記憶を prompt 常駐ファイルとして管理する方式**です。ここは OpenClaw の「ファイル駆動の assistant personality / ops model」をよく表しています。 ([OpenClaw][10])

## 7) system prompt は OpenClaw-owned

System Prompt docs のいちばん大事な一文は、OpenClaw が **every agent run ごとに custom system prompt を組み立てる** こと、そしてそれが **OpenClaw-owned** であって pi-coding-agent default prompt を使わない、という点です。provider plugins は prompt 全体を乗っ取るのではなく、`interaction_style`、`tool_call_style`、`execution_bias` のような core sections の差し替えや、cache boundary を意識した stable prefix / dynamic suffix の追加を行います。 ([OpenClaw][10])

prompt の中身もかなり platform-oriented です。Tooling、Safety、Skills、Self-Update、Workspace、Documentation、Workspace Files、Sandbox、Time、Reply Tags、Heartbeats、Runtime、Reasoning といった固定セクションを持ち、cron の使い方、background process の扱い、subagent 待ちの poll を避けること、approval UI を優先することまで埋め込まれます。つまり prompt は persona 文というより、**runtime の操作マニュアル兼 policy hint** です。 ([OpenClaw][10])

sub-agent 用には `promptMode=minimal` があり、Skills、Memory Recall、Self-Update、User Identity、Messaging、Heartbeats などを落として小さくします。さらに sub-agent では bootstrap file 注入も `AGENTS.md` と `TOOLS.md` に絞られます。これは OpenClaw が **prompt size と cache stability を明示的に最適化している** ことを示します。 ([OpenClaw][10])

## 8) tool 実行は sandbox / policy / approvals を分離している

OpenClaw の実行安全性は、1つのスイッチで決まるわけではありません。docs ははっきり、**Sandbox / Tool Policy / Elevated** は別物だと説明しています。sandbox は「どこで実行するか」、tool policy は「何を使わせるか」、elevated は「sandbox から host に escape させるか」の制御です。 ([OpenClaw][11])

`exec` tool は `host=auto|sandbox|gateway|node`、`security=deny|allowlist|full`、`ask=off|on-miss|always` を持ち、sandbox 中なら基本は sandbox、必要に応じて gateway/node host に出られます。approval が必要な場合は immediately `approval-pending` を返し、その後 `Exec finished` / `Exec denied` の system event が session に流れます。 ([OpenClaw][12])

sandboxing 自体も単純な Docker jail ではなく、mode は `off|non-main|all`、scope は `agent|session|shared`、backend は `docker|ssh|openshell` を持ちます。workspace access も `none|ro|rw` で変えられ、browser まで sandbox 側で動かせます。elevated はその外へ出る exec-only escape hatch で、`/elevated on|ask|full|off` によって per-session で制御されます。 ([OpenClaw][13])

この分離は設計上かなり良いです。OpenClaw は prompt 上の safety に頼り切らず、**hard stop は tool policy・exec approvals・s sandbox・channel allowlists でやる**と docs が明言しています。運用者が理解すべき面は増えますが、そのぶん実行制御はかなり明示的です。 ([OpenClaw][10])

## 9) nodes は「別マシン上の能力」を Gateway に繋ぐ面

nodes は同じ WS server に `role: node` で接続し、`canvas.*`、`camera.*`、`screen.record`、`location.get` などの capability を広告します。headless node host なら `system.run` / `system.which` をそのマシン上で expose でき、さらに browser proxy も自動広告できます。つまり nodes は「別デバイスの I/O 面」を Gateway control plane にぶら下げる仕組みです。 ([OpenClaw][2])

pairing も node 向けに別途あります。Gateway-owned pairing docs では、Gateway が membership の source of truth で、pending request → approval → token issuance の flow を持ちます。2026.3.31 以降は node pairing 承認前は declared node commands が無効化され、device pairing だけでは command surface が出なくなったと説明されています。 ([OpenClaw][14])

このため OpenClaw の nodes は、単なる remote shell ではありません。**device identity と command trust を Gateway 側で仲裁する capability surface** です。exec approvals も node host 側に存在し、per-agent allowlist と組み合わさるので、Gateway から見て「どの host で何を実行させるか」をかなり細かく分けられます。 ([OpenClaw][15])

## 10) queueing は architecture の一部

OpenClaw の queue は後付けではなく、agent architecture の一部です。Command Queue docs によると、inbound auto-reply runs は tiny in-process queue に入り、**session lane** と **global lane** で直列化されます。`runEmbeddedPiAgent` は `session:<key>` に enqueue され、さらに `main` lane にも通るので、同一 session の race を防ぎつつ、全体並列度も `agents.defaults.maxConcurrent` で抑えます。 ([OpenClaw][16])

さらに queue mode があり、`collect`、`followup`、`steer`、`steer-backlog`、`interrupt` を per-channel / per-session で切り替えられます。`collect` は follow-up でまとめ、`steer` は次の tool boundary / model boundary で current run に注入します。これは単なる message buffer ではなく、**実行中の agent run と新着 message の整合を取る orchestration policy** です。 ([OpenClaw][16])

## 11) sub-agents は background task として扱う

Sub-agents は既存 run から spawned される background agent run で、独自 session `agent:<agentId>:subagent:<uuid>` を持ち、終了時に requester chat へ announce します。各 sub-agent run は background task として追跡され、専用 queue lane `subagent` を持ちます。 ([OpenClaw][17])

デフォルトでは sub-agent はさらに子を spawn できませんが、`maxSpawnDepth: 2` で main → orchestrator sub-agent → worker sub-sub-agents という構成が可能になります。tool policy も depth で変わり、通常 sub-agent は session/system tools を持たず、depth-1 orchestrator だけ追加の session tools を持てます。 ([OpenClaw][17])

ここでも設計思想は Gateway-first です。sub-agent は Claude Code の fork のような親文脈継承中心ではなく、**background run / session tree / announce chain** として管理されます。docs も limitation として announce が best-effort で、Gateway restart で pending announce work は失われうると書いています。 ([OpenClaw][17])

## 12) plugin system はかなり platform-like

Plugin Architecture docs は、OpenClaw の plugin system を 4 層に分けています。

1. Manifest + discovery
2. Enablement + validation
3. Runtime loading
4. Surface consumption
   という構成で、discovery や config validation は manifest/schema だけで成立し、native runtime behavior は `register(api)` に任せる、という boundary が明確です。 ([OpenClaw][18])

しかも native plugins は Gateway と **同一プロセス内** で `jiti` 経由で load され、sandbox はされません。つまり plugin は強力ですが、trust boundary 的には core code と同格です。その代わり、capability model はかなり整理されていて、text inference、speech、media understanding、image generation などの capability register API が用意され、plugin shape も plain-capability / hybrid-capability / hook-only / non-capability に分類されます。 ([OpenClaw][18])

provider plugin についても、OpenClaw は generic agent loop・failover・transcript handling・tool policy は core が持ち、provider固有差分だけ hook surface で渡します。これは plugin system が「便利 add-on」ではなく、**platform の public extension ABI** に近いことを示しています。 ([OpenClaw][18])

## 13) skills は prompt 注入ではなく“索引注入”

skills は AgentSkills-compatible な `SKILL.md` フォルダで、bundled・managed・workspace など複数の source からロードされます。system prompt には skill の instructions 本体ではなく、**name / description / location を持つ compact list** だけが injected され、必要になったら model が `read` で `SKILL.md` を開く想定です。 ([OpenClaw][19])

これは token 設計としてかなり良いです。skills を常時全部 prompt に突っ込まず、**metadata だけ常駐、本文は demand-load** にしているからです。OpenClaw の docs は skill list の deterministic overhead まで説明しており、context pressure をかなり意識していることが分かります。 ([OpenClaw][19])

## 14) セキュリティ前提は「単一 trust boundary」

Security docs はかなり率直で、OpenClaw は **personal assistant trust model** を前提にしており、hostile multi-tenant boundary ではない、と明言しています。1 Gateway あたり 1 trusted operator boundary を想定し、複数の adversarial user を同じ gateway/agent に載せる構成は推奨しません。host と `~/.openclaw` を触れる者は trusted operator とみなされます。 ([OpenClaw][20])

この前提はアーキテクチャ全体に浸透しています。native plugins は unsandboxed、Gateway は state の source of truth、exec は host/node に出られる、channel surface は実メッセージングに繋がる。要するに OpenClaw は「強い tenant isolation を提供する SaaS platform」ではなく、**自分用・自分管理の assistant OS** に近いです。これは欠点というより、設計目標の違いです。 ([OpenClaw][18])

## まとめ

OpenClaw のアーキテクチャを短く言い切るなら、
**「長寿命 Gateway を中心に、埋め込み agent runtime、typed WS protocol、session/transcript persistence、sandbox/approvals、nodes、plugins を束ねた assistant control plane」**
です。agent loop はその中核実行路ですが、全体の重心は Gateway 側にあります。 ([OpenClaw][2])

強みは、control plane が明確で、protocol と plugin boundary が型付けされ、queue・session・sandbox・approvals がかなり運用的に整理されている点です。代わりに、Gateway host が大きな trust bottleneck になり、native plugins は高信頼コード扱いで、workspace/bootstrap 注入は token pressure を増やします。これも docs から自然に読める OpenClaw のトレードオフです。 ([OpenClaw][18])

次に掘るなら、`Gateway protocol`、`Agent loop`、`Pi integration architecture`、`System prompt`、`Command queue`、`Plugin architecture`、`Sandboxing / Security` の順で読むと、設計の骨格がかなり綺麗に見えます。 ([OpenClaw][2])

必要なら次に、これをさらに **「コードディレクトリ単位の call graph」** まで落として、Gateway 起点で `agent` RPC が `runEmbeddedPiAgent` に到達する流れを擬似シーケンス図つきで解説します。

[1]: https://github.com/openclaw/openclaw?utm_source=chatgpt.com "GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 · GitHub"
[2]: https://docs.openclaw.ai/concepts/architecture?utm_source=chatgpt.com "Gateway Architecture - OpenClaw"
[3]: https://docs.openclaw.ai/web/webchat?utm_source=chatgpt.com "WebChat - OpenClaw"
[4]: https://docs.openclaw.ai/gateway/protocol?utm_source=chatgpt.com "Gateway Protocol - OpenClaw"
[5]: https://docs.openclaw.ai/pi?utm_source=chatgpt.com "Pi Integration Architecture - OpenClaw"
[6]: https://docs.openclaw.ai/concepts/agent?utm_source=chatgpt.com "Agent Runtime - OpenClaw"
[7]: https://docs.openclaw.ai/agent-loop?utm_source=chatgpt.com "Agent Loop - OpenClaw"
[8]: https://docs.openclaw.ai/concepts/agent-loop?utm_source=chatgpt.com "Agent Loop - OpenClaw"
[9]: https://docs.openclaw.ai/reference/session-management-compaction?utm_source=chatgpt.com "Session Management Deep Dive - OpenClaw"
[10]: https://docs.openclaw.ai/concepts/system-prompt?utm_source=chatgpt.com "System Prompt - OpenClaw"
[11]: https://docs.openclaw.ai/gateway/sandbox-vs-tool-policy-vs-elevated?utm_source=chatgpt.com "Sandbox vs Tool Policy vs Elevated - OpenClaw"
[12]: https://docs.openclaw.ai/tools/exec?utm_source=chatgpt.com "Exec Tool - OpenClaw"
[13]: https://docs.openclaw.ai/sandboxing?utm_source=chatgpt.com "Sandboxing - OpenClaw"
[14]: https://docs.openclaw.ai/gateway/pairing?utm_source=chatgpt.com "Gateway-Owned Pairing - OpenClaw"
[15]: https://docs.openclaw.ai/tools/exec-approvals?utm_source=chatgpt.com "Exec Approvals - OpenClaw"
[16]: https://docs.openclaw.ai/concepts/queue?utm_source=chatgpt.com "Command Queue - OpenClaw"
[17]: https://docs.openclaw.ai/tools/subagents?utm_source=chatgpt.com "Sub-Agents - OpenClaw"
[18]: https://docs.openclaw.ai/plugins/architecture?utm_source=chatgpt.com "Plugin Architecture - OpenClaw"
[19]: https://docs.openclaw.ai/tools/skills?utm_source=chatgpt.com "Skills - OpenClaw"
[20]: https://docs.openclaw.ai/gateway/security?utm_source=chatgpt.com "Security - OpenClaw"
