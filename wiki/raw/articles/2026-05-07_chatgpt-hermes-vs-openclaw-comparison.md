公式ドキュメントとリポジトリを読む限り、Hermes Agent は「CLI付きのツール呼び出しボット」ではなく、**`AIAgent` を中心に、永続 state、prompt 組み立て、tool runtime、gateway、plugin/memory provider を周辺にぶら下げた“統合エージェント実行基盤”**として設計されています。以下は **2026年4月13日公開の v0.9.0 系ドキュメント/リポジトリ**をベースにした、アーキテクチャの詳細オーバービューです。 ([GitHub][1])

## 全体像

一番大きな見方をすると、Hermes は
**入力面**（CLI / messaging gateway / ACP / cron / batch）
→ **実行コア**（`run_agent.py` の `AIAgent`）
→ **支援層**（prompt builder、provider resolver、tool registry、compression、memory/session）
→ **外部接続**（terminal backends、platform adapters、MCP、plugins）
という層構造です。公式の architecture / agent-loop / gateway docs は、CLI や gateway を主役にするより、まず `AIAgent` を主コアとして置き、その周りに session・tool・provider・gateway が接続される構図で説明しています。 ([エルメスエージェント][2])

## 1) 中心コアは `AIAgent`

Hermes のアーキテクチャ上の中心は `run_agent.py` の `AIAgent` です。公式 docs では、このクラスの責務として **effective prompt の組み立て、provider/API mode の選択、interruptible な LLM call、tool 実行、session history 維持、compression / retry / fallback model 処理** が挙げられています。つまり Hermes は、プロンプト管理だけ別サービス、tool 実行だけ別ランナー、というより、**1つの大きい agent core に主要 orchestration を集める**設計です。 ([エルメスエージェント][3])

このコアは 3 つの API execution mode を持ちます。`chat_completions`、`codex_responses`、`anthropic_messages` で、provider 選択や base URL の解決に応じて切り替わります。CLI、gateway、cron、ACP、auxiliary task でも provider resolution のロジックは共有されており、Hermes 全体を貫く共通 runtime として機能しています。 ([エルメスエージェント][3])

また、UI や integration は callback surface でコアにぶら下がります。`tool_progress_callback`、`thinking_callback`、`clarify_callback`、`stream_delta_callback` などがあり、CLI、gateway、ACP がこの面から進捗表示や承認フローを実現します。つまり Hermes の表層は多様でも、**内部では 1 つの agent loop を複数の front-end が共有する**構造です。 ([エルメスエージェント][3])

## 2) 1ターンの実行フロー

1ターンのライフサイクルはかなり明快です。ユーザーメッセージを履歴へ追加し、必要なら preflight compression を行い、cached system prompt をロードまたは構築し、API 用の messages を作り、ephemeral layer を注入し、必要に応じて prompt caching を適用してから LLM を呼びます。返答が tool call なら tool を実行して履歴へ結果を戻し、最終テキストなら session を保存して返します。 ([エルメスエージェント][3])

ここで重要なのは、Hermes が **interruptible call** を標準で持っていることです。CLI でも gateway でも、実行中にユーザーから新しい入力が来たら停止・割り込みできる前提になっています。加えて、複数 tool call が返った場合は **single/interactive tool は逐次**, **non-interactive tool 群は並列** という使い分けをします。結果の再挿入順序は conversation history と整合するよう保たれます。 ([エルメスエージェント][3])

さらに、Hermes は親子 agent 間で **shared iteration budget** を持ち、残り予算が少なくなると budget pressure hints を注入します。fallback model もサポートしており、特定の失敗パスでは別 provider/model に切り替えられます。これは「1回の LLM 呼び出し」ではなく、**長めの agentic run を安全に完遂するための実行機構**として設計されている、ということです。 ([エルメスエージェント][3])

## 3) Prompt assembly はかなり戦略的

Hermes の prompt 設計で特に重要なのは、**cached system prompt** と **API 呼び出し時だけ入る ephemeral additions** を明確に分離している点です。公式 docs はこれを「最も重要な設計の1つ」と位置づけており、token usage、prompt caching、session continuity、memory correctness に効くと説明しています。 ([エルメスエージェント][4])

cached system prompt の組み立て順は、概ね

1. `SOUL.md` 由来の agent identity
2. tool-aware behavior guidance
3. Honcho static block
4. optional system message
5. frozen MEMORY snapshot
6. frozen USER snapshot
7. skills index
8. context files
9. timestamp / optional session ID
10. platform hint
    です。つまり Hermes は prompt を単なる “system string” ではなく、**人格・規律・記憶・スキル索引・プロジェクト文脈・プラットフォーム表現を合成した構造体**として扱っています。 ([エルメスエージェント][4])

この構造の要点は、**memory も context files も mid-session では基本的に固定**だということです。built-in memory は session start 時に snapshot として埋め込まれ、途中で `memory` tool が内容を書き換えても prompt 自体はその場では変えません。これは memory の整合性だけでなく、provider-side prompt cache を壊さないためでもあります。 ([エルメスエージェント][4])

prompt caching 自体もかなり明示的で、Anthropic native と Claude-via-OpenRouter 系では **system prompt + 直近3つの non-system messages** を cache 対象にし、TTL はデフォルト 5 分です。長い対話では context compression と併用し、**stable prefix をなるべく不変に保つ**方針がはっきりしています。 ([エルメスエージェント][5])

ひとつ細かい注意点として、公式 docs には context files の説明に少し揺れがあります。developer guide の Prompt Assembly は **`.hermes.md` / `AGENTS.md` / `CLAUDE.md` / `.cursorrules` を priority で first-match-wins 的に扱う**説明ですが、user guide の Context Files ページは AGENTS.md の再帰的ロードを前面に出しています。私の読みでは、**current internals を追うなら developer guide 側をより重く見る**のが安全です。これは docs 間の差分からの推論です。 ([エルメスエージェント][4])

## 4) 永続 state: session、memory、search

Hermes は every conversation を session として保存します。保存先は 2 系統で、**`~/.hermes/state.db` の SQLite + FTS5** と、**`~/.hermes/sessions/` の JSONL transcripts** です。DB には session ID、platform source、user ID、title、model、system prompt snapshot、full message history、token counts、timestamps、親 session ID などが入り、JSONL 側には raw transcript が残ります。 ([エルメスエージェント][6])

この設計が効くのは、Hermes が built-in の `session_search` tool を持つからです。FTS5 で relevant message を引き、上位 session をまとめ、対象会話を切り出して要約モデルにかけることで、過去会話を横断的に再利用できます。つまり Hermes の “記憶” は、単なる KV メモではなく、**bounded memory + searchable transcript archive** の二層です。 ([エルメスエージェント][6])

built-in memory 自体は `MEMORY.md` と `USER.md` の 2 ファイルです。前者は環境・慣習・学習内容、後者はユーザー嗜好やコミュニケーション特性を置く用途で、どちらも `~/.hermes/memories/` に保存されます。メモリは文字数上限付きの bounded store で、`memory` tool が add/replace/remove を行います。ここでも、**全知識を memory に詰めるのではなく、常時必要な durable facts だけを prompt 内常駐させる**設計です。 ([エルメスエージェント][7])

さらに Hermes には external memory provider plugin の仕組みがあり、Honcho、RetainDB、ByteRover などを追加できます。built-in memory は常に残り、その上に **外部 provider を 1 つだけアクティブ化**する形です。provider が有効だと、turn 前 prefetch、turn 後 sync、session end extract、provider-specific tools の追加などが走ります。 ([エルメスエージェント][8])

また、compression 後は session lineage が分岐します。Hermes は middle turns を要約して context を軽くする一方、親 session ID を DB に保持するので、**“軽量な現役セッション” と “検索可能な祖先履歴”** を両立させています。これは長寿命 agent にかなり向いた設計です。 ([エルメスエージェント][5])

## 5) Tool runtime は registry 中心

tool layer は `tools/registry.py` を中心にした **self-registering registry** 方式です。各 tool module が import 時に `registry.register()` を呼び、`model_tools.py` が AST で top-level の `registry.register()` を含む tool file を見つけて import します。その後に MCP tools と plugin tools も追加 discovery されます。これは、新しい built-in tool を増やしても手動の中央リスト更新をほぼ不要にする設計です。 ([エルメスエージェント][9])

tool は toolset 単位でも管理されます。`web`、`terminal`、`file`、`browser`、`vision`、`image_gen`、`skills`、`memory`、`session_search`、`cronjob`、`code_execution`、`delegation`、`clarify`、MCP などがあり、platform preset や enabled/disabled list で出し分けます。`check_fn` による availability 判定もあり、API key やバイナリの存在次第で schema からその tool 自体を落とせます。 ([エルメスエージェント][10])

実行時には、model から返った tool call が `model_tools.handle_function_call()` に入り、plugin pre-hook、registry dispatch、plugin post-hook の順で処理されます。ただし `todo`、`memory`、`session_search`、`delegate_task` は agent-level state が必要なので、registry 直行ではなく **agent loop 側で特別扱い**されます。例外は二重に JSON error wrapping され、LLM 側には未処理 exception を返さないようになっています。 ([エルメスエージェント][9])

安全面では terminal tool が `DANGEROUS_PATTERNS` による approval flow を持ちます。危険コマンド検知、CLI/gateway の承認プロンプト、session 単位の承認状態、永続 allowlist、さらに optional な smart approval まで揃っており、Hermes は shell 実行を単なる raw escape hatch にしていません。terminal backend も local、docker、ssh、singularity、modal、daytona を持ちます。 ([エルメスエージェント][9])

## 6) Subagent delegation と `execute_code` は別物

Hermes でかなり特徴的なのが、**`delegate_task` と `execute_code` を別の execution primitive として持っている**点です。`delegate_task` は child `AIAgent` を起動し、fresh conversation、separate terminal、restricted toolsets でタスクを処理させます。子は親の会話履歴を知らず、`goal` と `context` だけを見て動き、親に返るのは最終 summary だけです。最大 3 並列、再帰 delegation や memory write などはいくつか禁止されています。 ([エルメスエージェント][11])

一方の `execute_code` は、LLM が Python script を書き、その script が `hermes_tools.py` スタブ経由で tool を RPC 呼び出しする仕組みです。子プロセスは Unix domain socket 経由で親 Hermes に tool call を戻し、LLM に返るのは `print()` 出力だけです。API keys などの危険な env var は child に渡されず、temporary directory と process group で実行されます。これは reasoning-heavy delegation ではなく、**機械的な multi-step pipeline を 1 turn に圧縮するための sandboxed executor** です。 ([エルメスエージェント][12])

この 2 つを併置しているのが Hermes らしいところで、
**判断が必要な下請け**は subagent、
**ループ/分岐/フィルタ中心の処理**は execute_code、
という分担がかなり明確です。 ([エルメスエージェント][11])

## 7) Gateway は “常駐フロントエンド層”

gateway は long-running process で、14+ の messaging platform を統一アーキテクチャで扱います。`GatewayRunner` が platform adapter 群を束ね、`MessageEvent` に正規化し、session key を解決し、slash command をさばき、必要なら `AIAgent` を立てて返答します。つまり gateway は agent core の代替ではなく、**AIAgent にメッセージング世界を接続する常駐 orchestration 層**です。 ([エルメスエージェント][13])

message flow もかなり作り込まれています。adapter 側と runner 側の **two-level message guard** があり、実行中 session への新規入力は queue へ入り、interrupt event が立ちます。`/approve` や `/deny` のような実行中でも到達すべき command は inline dispatch でバイパスします。session key、authorization、running-agent guard、DM pairing まで備えた、かなり本格的な messaging control plane です。 ([エルメスエージェント][13])

gateway にはさらに cron ticking、session expiry、memory flush、cache refresh などの background maintenance があり、hooks も持ちます。gateway hooks は `~/.hermes/hooks/` 以下の `HOOK.yaml` + `handler.py` で登録され、plugin hooks は CLI と gateway の両方で動きます。どちらも non-blocking で、hook の失敗は agent を落とさない設計です。 ([エルメスエージェント][13])

## 8) Provider runtime は全体を横断する共通基盤

provider 解決は個々の feature ごとにバラバラではなく、Hermes 全体の shared runtime resolver で処理されます。優先順位は **明示指定 > `config.yaml` > environment variables > provider defaults/auto** です。これにより、CLI で選んだ model/provider を gateway や cron や ACP でも再利用しやすくなっています。 ([エルメスエージェント][14])

加えて、auxiliary task も main conversational model とは独立に provider/model/base_url を持てます。vision、web extraction summarization、compression、session search、skills hub、MCP helper、memory flush などが別 routing を取りうるので、Hermes は単一モデル一発ではなく、**補助処理を含む multi-runtime agent** に近いです。 ([エルメスエージェント][14])

fallback model の扱いも実務的で、認証失敗や一定の retry failure 後に 1 度だけ in-place で runtime を切り替えます。ただし docs 上は、subagent delegation、cron、auxiliary tasks にはこの fallback mechanism がそのままは乗りません。つまり fallback は “Hermes 全体の透過的 HA” というより、**main agent loop 用の failover 機能**です。 ([エルメスエージェント][14])

## 9) Extension model: plugins、hooks、memory/context providers

plugins は Python ベースの first-class extension です。一般 plugin は tool、hook、slash command、CLI command、skill bundling、message injection を追加でき、`~/.hermes/plugins/`、project-local の `.hermes/plugins/`、または pip entry points から発見されます。project-local plugin はデフォルト無効で、信頼した repo に限って有効化する設計です。 ([エルメスエージェント][15])

plugin hooks には `pre_tool_call`、`post_tool_call`、`pre_llm_call`、`post_llm_call`、`on_session_start`、`on_session_end` があり、guardrail、metrics、tool interception、context injection に使えます。ここから分かるのは、Hermes の plugin は UI テーマ程度ではなく、**agent loop の前後へ食い込める trusted-code extension** だということです。 ([エルメスエージェント][16])

さらに plugin には 3 種あります。general plugins、memory providers、context engines で、memory provider と context engine は single-select の provider plugin です。つまり Hermes は拡張を “便利機能の追加” だけでなく、**memory 層や compression/context engine 自体の差し替え**まで視野に入れています。 ([エルメスエージェント][15])

## 10) 何がアーキテクチャ上いちばん特徴的か

私の見立てでは、Hermes の設計を特徴づけているのは次の4点です。

* **AIAgent中心主義**
  gateway や CLI は重要ですが、設計の重心は `AIAgent` にあります。prompt、tool、session、compression、fallback をひとつのコアへ集約しているのが最大の特徴です。 ([エルメスエージェント][3])

* **prompt-cache-aware な state 設計**
  frozen memory snapshot、ephemeral layers 分離、stable prefix 重視など、Hermes は “正しさ” だけでなく “cache stability” をアーキテクチャ制約として組み込んでいます。 ([エルメスエージェント][4])

* **記憶が二層ではなく三層ある**
  built-in memory、searchable session archive、optional external memory provider の三層があり、短い durable fact と長い履歴資産を分離しています。 ([エルメスエージェント][7])

* **実行 primitive を分けている**
  normal tool loop、subagent delegation、execute_code、cron、gateway delivery と、実行様式ごとに primitive が分かれていて、それぞれ token cost や isolation の哲学が違います。 ([エルメスエージェント][3])

## 11) 設計上のトレードオフ

トレードオフもあります。まず、`AIAgent` の責務が広いので、**概念モデルは分かりやすい反面、コア実装の複雑性は高くなりやすい**です。公式 docs でも prompt assembly、provider resolution、tool execution、compression、fallback がこのコアに集中しています。これはソースを追う順番を簡単にする一方、変更点がコアに集まりやすい設計です。これは docs の構造からの推論です。 ([エルメスエージェント][3])

次に、memory や prompt の安定性を優先するため、**その場で memory を書いたのに prompt 上は次 session まで反映されない**など、即時性より整合性を優先する場面があります。これは性能と分かりやすさには効きますが、設計思想としてはかなり意図的です。 ([エルメスエージェント][7])

最後に、subagent は本当に blank-slate なので、親が `goal` と `context` をきちんと書けないと性能が落ちます。これは制約でもありますが、逆に言えば **親コンテキスト汚染を防ぎ、要約だけを戻す**ための強い isolation でもあります。 ([エルメスエージェント][11])

## コードを読む順番

実装を追うなら、私は
`run_agent.py` → `agent/prompt_builder.py` → `agent/context_compressor.py` → `model_tools.py` / `tools/registry.py` → `hermes_state.py` → `gateway/run.py` → `gateway/session.py`
の順を勧めます。公式 architecture / gateway docs の責務分担とも一致していて、Hermes の「コア → state → 外部接続」という骨格が最も見やすい順です。 ([エルメスエージェント][2])

次は `run_agent.py` を中心に、**1ターンの call graph と主要メソッド単位**まで落として解説します。

[1]: https://github.com/NousResearch/hermes-agent/releases?utm_source=chatgpt.com "Releases · NousResearch/hermes-agent · GitHub"
[2]: https://hermes-agent.nousresearch.com/docs/developer-guide/architecture/?utm_source=chatgpt.com "Architecture | Hermes Agent"
[3]: https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop/?utm_source=chatgpt.com "Agent Loop Internals | Hermes Agent"
[4]: https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly/ "Prompt Assembly | Hermes Agent"
[5]: https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching/?utm_source=chatgpt.com "Context Compression & Prompt Caching | Hermes Agent"
[6]: https://hermes-agent.nousresearch.com/docs/user-guide/sessions/?utm_source=chatgpt.com "Sessions | Hermes Agent"
[7]: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/?utm_source=chatgpt.com "Persistent Memory | Hermes Agent"
[8]: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers?utm_source=chatgpt.com "Memory Providers | Hermes Agent"
[9]: https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime/ "Tools Runtime | Hermes Agent"
[10]: https://hermes-agent.nousresearch.com/docs/user-guide/features/tools/?utm_source=chatgpt.com "Tools & Toolsets | Hermes Agent"
[11]: https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation/?utm_source=chatgpt.com "Subagent Delegation | Hermes Agent"
[12]: https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution/?utm_source=chatgpt.com "Code Execution | Hermes Agent"
[13]: https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-internals/ "Gateway Internals | Hermes Agent"
[14]: https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime/?utm_source=chatgpt.com "Provider Runtime Resolution | Hermes Agent"
[15]: https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins/ "Plugins | Hermes Agent"
[16]: https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks/?utm_source=chatgpt.com "Event Hooks | Hermes Agent"
