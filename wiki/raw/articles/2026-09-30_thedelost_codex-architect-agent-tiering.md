---
title: "Codex tip: GPT-6.1 Sol メイン時に Astra をアーキテクトとしてオンコール化する役割分担"
type: x_note_tweet
date: 2026-09-30
date_ingested: 2026-10-02
source: https://x.com/thedelost/status/2105398038026195279
author: delost (@thedelost)
platform: x
tweet_id: "2105398038026195279"
published_utc: "2026-09-30T20:43:03.000Z"
tags: [coding-agents, prompt-engineering, openai]
external_links:
  - https://developers.openai.com/codex/subagents
engagement:
  bookmarks: 2913
  likes: 1525
  impressions: 556709
---

# 原文（Note Tweet 全文）

> Codex tip: once GPT-6.1 Sol is your main model, stop running Astra on every turn
>
> put Astra on call as an architect agent
>
> GPT-6.1 Sol keeps writing the code
> Astra only gets spawned at three points:
>
> → before a plan: is this the right approach?
> → when the same error comes back: am I digging in the wrong place?
> → before "done": what did I miss?
>
> Astra reviews. Sol ships
>
> Jev engineering is the same move one layer down: the forks that need no thinker (which file, which tool, retry or stop) go to Jev in under half a second, and the big models only see the ones that split
>
> - the full tree
>
> \> GPT-6.1 Sol on high runs the main session
> \> explorer reads the code on Luna
> \> worker edits and runs tests on Sol
> \> researcher pulls the docs on Luna
> \> all three on medium
> \> Astra on call as the architect
> \> auto_review checks every approval
>
> paste the tree and this prompt into Codex ↓
>
> "Rebuild my Codex setup around this tree:
>
> 1. Check ~/.codex/agents and .codex/agents for agents that already fit explorer, worker and researcher.
>
> \> Draft new TOML files only for missing roles
> \> explorer and researcher on gpt-6-luna, worker on gpt-6.1-sol, all with model_reasoning_effort medium
> \> Add an architect agent on gpt-6-astra, model_reasoning_effort high, whose only job is reviewing plans, repeated errors and finished work
> \> Skip any that pin a different model and list them
>
> 2. In ~/.codex/config.toml set model to gpt-6.1-sol, model_reasoning_effort to high and approvals_reviewer to auto_review
>
> 3. Find anything that would override this (active profiles, flags in my shell aliases, agents.default_subagent_model). Report it, change nothing
>
> 4. Add one rule to AGENTS.md: spawn the architect before a large plan, when an error repeats, and before calling a long task done
>
> Show me every change as a diff first. No edits until I say go."

（引用URL: https://developers.openai.com/codex/subagents ）

# 要約・ポイント

- **核心**: 最強モデル（Astra）を毎ターン回すのをやめ、アーキテクト役として「呼ばれた時だけ」起動する役割分担構成。
- **3つの起動タイミング**: ①大規模計画の前（アプローチ検証）②同じエラーの再発時（_wrong direction 検証）③完了宣言の前（見落としチェック）。
- **役割原則**: Astra はレビューのみ、Sol が出荷する。「Astra reviews. Sol ships.」
- **一段下も同様に軽モデル（Jev）へ**: 考える必要のない分岐（どのファイル/ツール、リトライか停止か）は 0.5 秒未満で軽モデルにさばかせ、大モデルは「枝分かれが必要な仕事」だけ見る。
- **フルツリー**: Sol(high)=メイン、explorer/researcher=Luna(medium)、worker=Sol(medium)、Astra=オンコールアーキテクト、auto_review=全承認チェック。
- **プロンプトの防御設計**: 既存 agent TOML を先に確認 → 欠けた役割だけ新規作成 → 上書き要因（profiles/shell alias/agents.default_subagent_model）は変更せず報告のみ → 全変更を diff で提示、許可まで編集禁止。AGENTS.md にアーキテクト起動ルールを1行追加。
- 実践は Codex サブエージェント（`~/.codex/agents` / `.codex/agents` の TOML 定義）が基盤。公式リファレンス: https://developers.openai.com/codex/subagents
