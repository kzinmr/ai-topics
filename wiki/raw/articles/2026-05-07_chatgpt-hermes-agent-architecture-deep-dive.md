かなり良い分析だと思います。
ただし、これは厳密には「アーキテクチャ比較」そのものというより、**skills を中心に見た product/UX/運用哲学の比較**として読むのがいちばんしっくりきます。一次情報で見ると、Hermes は `AIAgent` を中心に memory・session search・compression・skill 管理を束ねる **agent-core-first** な設計で、OpenClaw は単一の長寿命 Gateway を control plane にして sessions・prompt・skills・sandbox を統治する **gateway-first** な設計です。そこが土台の違いです。 ([Hermes Agent][1])

Hermes 側についての観察は、かなり当たっています。公開 docs でも、Hermes は built-in learning loop を掲げ、agent-managed skills を持ち、複雑なタスクの成功後やエラーを踏んで正解ルートを見つけたとき、あるいはユーザーに修正されたときに skill を create/patch/edit/delete できると説明されています。しかも bundled/optional の skills catalog はかなり広く、最初から多くの領域をカバーする前提です。なので elvissun のいう「blank framework ではなく、最初からかなり完成した agent」という見方にはかなり賛成です。 ([Hermes Agent][2])

一方で、引用文の中の **「every N tool calls で nudge」「background review がこう走る」** みたいな細かい cadence は、私が確認した公開 docs からはそこまで厳密には言えません。一次情報で確認できるのは、Hermes が skill 自己生成・skill patch/update・pre-compression の memory flush を持つことまでです。なので、挙動の方向性は正しいけれど、ヒューリスティクスの細部までは少し体感ベースが混じっている、と見ます。 ([Hermes Agent][2])

Hermes の **skill explosion 問題** の指摘は、私はかなり鋭いと思います。Hermes では bundled、hub-installed、agent-created の skills が基本的に `~/.hermes/skills/` という単一の主ディレクトリに集まり、agent 自身がそれを modify/delete できます。その意味で procedural memory としては非常に強い反面、長期運用では taxonomy・dedupe・メトリクスが必要になりやすい構造です。もっとも、Hermes は progressive disclosure を採用していて、フル skill 本文は必要時だけ読み込み、さらに `fallback_for_*` / `requires_*` で自動的に隠せる skills もあります。だからこの問題は、まず **discoverability と corpus governance の問題** であって、即座に prompt token が破綻する話ではありません。これは docs からの推論です。 ([Hermes Agent][2])

OpenClaw 側の観察も、方向としてかなり正しいです。ただし現行 docs では「5 sources」ではなく、skills の可視ソースは **workspace / project-agent / personal-agent / managed-local / bundled / extraDirs の 6 層**で、さらに location/precedence と visibility は別概念として、**per-agent allowlist** でも絞れます。加えて eligible skills は session 開始時に snapshot 化され、prompt に入るのは SKILL 本文ではなく name/description/location のコンパクトな一覧で、その token cost も deterministic に説明されています。ここは確かに Hermes より **可観測性・スコープ制御・コスト予測性** が強いです。 ([OpenClaw][3])

ただ、**「OpenClaw にはその問題がない」** は少し強すぎます。OpenClaw は local な load order と scope control は Hermes より追いやすいですが、docs 自体が third-party skills を **untrusted code として扱え** と明言していますし、ClawHub も公的レジストリとして公開アップロード、報告、モデレーションの仕組みを持つ設計です。つまり OpenClaw は entropy をなくしているというより、Hermes のような **“自己増殖するローカル corpus” の問題** を、**supply-chain review / operator policy / sandbox / approvals** 側へ寄せている、と理解するのが正確です。 ([OpenClaw][3])

`TOOLS.md` と `AGENTS.md` を使った routing 最適化の話も納得感がありますが、これは skill architecture というより **prompt architecture の勝ち筋** です。OpenClaw は `AGENTS.md`、`SOUL.md`、`TOOLS.md` などの bootstrap files を毎ターン prompt に注入しつつ、skills はコンパクトな index として持たせて必要時にだけ `read` で開かせます。Hermes も `SOUL.md`、bounded な `MEMORY.md` / `USER.md`、project context files を prompt に入れますが、そこに self-authored skills と memory loop が重なります。つまり「explicit > implicit」が OpenClaw で効きやすいのは本当ですが、それは OpenClaw の推論器が特別というより、**runtime がその明示ルールを見えやすく保っている**からです。 ([OpenClaw][4])

なので私の最終的な見立てはこうです。
elvissun の整理は **daily-driver の感触** と **product positioning** ではかなり当たっています。でもアーキテクチャの言葉に直すなら、Hermes は **capability accumulation system**、OpenClaw は **scope-controlled assistant control plane** です。前者は learned procedures が増えるほど強くなり、後者は visible scope が明示的で狭く管理されるほど強くなります。だから「Hermes = Rails、OpenClaw = Linux」という比喩にはかなり賛成ですが、核心は minimal vs maximal というより **agent-core-first vs gateway/governance-first** だと思います。 ([GitHub][5])

いちばん面白いのは、両者が相互に学べることです。Hermes は OpenClaw から **skill allowlist / precedence / observability / corpus hygiene** をもっと取り込むと強いし、OpenClaw は Hermes から **post-task の procedural capture と patch-in-place の学習ループ** を取り込むと、かなり強くなると思います。

[1]: https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop?utm_source=chatgpt.com "Agent Loop Internals | Hermes Agent"
[2]: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills?utm_source=chatgpt.com "Skills System | Hermes Agent"
[3]: https://docs.openclaw.ai/tools/skills?utm_source=chatgpt.com "Skills - OpenClaw"
[4]: https://docs.openclaw.ai/concepts/system-prompt?utm_source=chatgpt.com "System Prompt - OpenClaw"
[5]: https://github.com/nousresearch/hermes-agent?utm_source=chatgpt.com "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"
