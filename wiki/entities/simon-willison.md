---
title: Simon Willison
type: entity
aliases: [simonw]
created: 2025-01-01
updated: 2026-05-23
status: L3
sources: [https://simonwillison.net/, https://simonwillison.net/guides/agentic-engineering-patterns/, raw/articles/2026-05-06_simon-willison_vibe-coding-convergence.md, raw/articles/2026-05-06_simon-willison_code-w-claude-2026.md, raw/articles/simonwillison.net--2026-may-19-5-minute-llms--498c7192.md, raw/articles/simonwillison.net--2026-may-22-memory-shortage--18b83f17.md]
tags: [person, blogger]
---


# Simon Willison

Django co-creator, open-source advocate, and leading voice in AI-assisted software development. Founder of [Datasette](https://datasette.io/) and prolific blogger at simonwillison.net.

## Core Ideas

### Agentic Engineering (2025-2026)
> "Agentic engineering represents the other end of the scale: professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise."

**Clear distinction from Vibe Coding**:
- Vibe Coding = Request in natural language → deploy without reading code → accumulated cognitive debt
- Agentic Engineering = Leverage agents while systematizing testing, verification, and understanding

**Core Philosophy**:
1. **Evaluation First**: 60-80% of development time should be spent on testing and error analysis
2. **Don't Trust the Code**: Never trust agent-generated code until it has been executed and verified
3. **Cognitive Debt Management**: Repay the cognitive debt accumulated by Vibe Coding through interactive explanation and walkthroughs
4. **Agent-Optimized Tools**: Build custom CLI tools optimized for LLM context windows (Rodney, Showboat, LLM plugins)
5. **Structured State Handoff**: Inter-agent communication via files, not dependent on conversation history

### Convergence with Anthropic Engineering

Willison's practical insights strongly align with Anthropic Engineering's official best practices:

| Willison | Anthropic | Convergence Point |
|----------|-----------|--------|
| Red/Green TDD | "Provide verification criteria" | Test-first is the foundation of agent quality assurance |
| "Don't trust the code" | "Context window fills fast" | Both prioritize verification and context management |
| Showboat (documentation) | "Structured artifacts for handoff" | Structured files for inter-agent state handoff |
| Git integration | "Version control with descriptive commits" | Keep agent work in a traceable state |

The series of Engineering articles Anthropic published in 2025-2026 can be said to have **officially validated and systematized** the patterns Willison discovered practically.

### Cognitive Debt Theory
A concept uniquely proposed by Willison. The "cognitive debt" that accumulates from losing understanding of how AI agent-generated code works — the cognitive equivalent of technical debt.

> "If the core of our application becomes a black box that we don't fully understand we can no longer confidently reason about it, which makes planning new features harder and eventually slows our progress in the same way that accumulated technical debt does."

**Repayment Cycle**:
```
Code Generation → Testing → Understanding via Linear Walkthrough → 
  Deep dive via Interactive Explanation → Recording via Showboat → Next Code Generation
```

### Strategic Context Window Management
The LLM's context window should be treated as a **limited resource**:
- **Compression**: Remove unnecessary information, preserve important information
- **Structuring**: File-based communication, avoiding dependence on conversation history
- **Prioritization**: Include the most relevant information in context
- **Agent Design**: Tool design that assumes context limitations (Rodney's CLI-first approach)

### Multi-Agent Patterns
- **Sub-agents**: Parallel task execution with independent contexts and terminals
- **Meta-agents**: Launching, integrating, and consolidating results from sub-agents
- **Self-containedness**: Instructions to sub-agents must be completely self-contained

### Hoarding Philosophy
> "Every time I write some code to solve a problem I save it. The next time I have a similar problem, I can reuse what I've already written — and improve it if it's still not quite right. It's hoarding, but a productive kind of hoarding."

**Power of the Hoard**:
- Accumulated skills are reusable as context to pass to LLMs
- A collection of small utility scripts becomes the "initial context" for larger projects
- In the coding agent era, this pattern becomes even more powerful: agents can improve and recompose hoarded code
- **Composability**: Combine accumulated parts to build more complex solutions

> "The more things I know how to do, the more I can compose together to do new things. And the more I can compose together, the more useful my hoard becomes to a coding agent."

### Compound Engineering Loop
> "I write some code, I review it, I improve it, I save what I've learned, and I repeat. Each cycle makes me more effective, and each cycle makes my agent more effective too."

**Stages of the Loop**:
1. **Write**: Have the agent write code
2. **Review**: Human scrutinizes the code and identifies issues
3. **Improve**: Ask the agent to fix it, or fix it yourself
4. **Save**: Add what you learned to your hoard (accumulation)
5. **Repeat**: In the next cycle, launch the agent with better context

**Why "Compound"**: Each cycle works as "interest" for the next cycle. Accumulated knowledge exponentially improves agent performance.

### Concrete Git Integration Practices
- **Commit small, commit often**: Save each agent output as an individual commit
- **Messages are for humans**: Write for future humans (or your future self), not in a format agents understand
- **Using `git commit --amend`**: Tidy up temporary commits during iterative work with agents
- **Branch strategy**: Have agents work on separate branches; humans review before merging to main

### Writing Code is Cheap — The Need for New Habits
> "The cost of writing code has dropped to near zero. The cost of understanding it, maintaining it, and integrating it into a larger system has not."

**New Habits**:
- Measure "quality" and "understanding" rather than "quantity" of code
- Don't blindly merge agent-generated code
- **Readability first**: Explicitly request "readable code" from agents
- **Documentation as part of the loop**: Generate documentation simultaneously with code generation

### Vibe Coding and Agentic Engineering Convergence (May 2026)

On Heavybit's High Leverage podcast (Ep.9, with Joseph Ruscio), Simon made a "disturbing realization":

> "As the coding agents get more reliable, I'm not reviewing every line of code that they write anymore, even for my production level stuff."

**The Convergence**:
- Originally: vibe coding = no code review, agentic engineering = professional standards
- Now: agents are reliable enough that Simon trusts them for production code without line-by-line review
- The guilt: "if I haven't reviewed the code, is it really responsible for me to use this in production?"

**Resolution — "Trust as a Team" Analogy**:
- Compares to trusting another engineering team's service: doesn't read every line of their code, trusts based on reputation
- Treats agents as semi-black boxes until problems arise
- "Claude Code does not have a professional reputation! It can't take accountability for what it's done. But it's been proving itself anyway."

This represents a significant evolution in Simon's agentic engineering philosophy — moving from strict verification to calibrated trust. Source: [Vibe coding and agentic engineering are getting closer than I'd like](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)

### Code w/ Claude 2026 Live Blog (May 2026)

Simon live-blogged Anthropic's Code w/ Claude 2026 event. Key announcements:

| Announcement | Detail |
|-------------|--------|
| **No new model** | Focus on making existing products work better |
| **API volume** | 17x year-on-year growth |
| **Colossus partnership** | SpaceX data center deal (see [[#xAI/Anthropic データセンター取引分析]]) |
| **Rate limits** | Doubled Claude Code 5-hour limit for Pro/Max/Enterprise |
| **Adviser strategy** | Opus advising Sonnet → frontier model quality at 5x lower cost |

**Managed Agents Updates**:
- **Multi-agent orchestration** (public beta): Fleets of agents for complex tasks
- **Outcomes** (public beta): Define success criteria, Claude iterates until achieved — "Ralph loop" style
- **Dreaming** (research preview): Claude inspects past sessions, identifies gaps, self-improves overnight

Source: [Live blog: Code w/ Claude 2026](https://simonwillison.net/2026/May/6/code-w-claude-2026/)

### AI Ethics Commentary: Stockholm AI Cafe Experiment (May 2026)

Simon Willison は Andon Labs による**Stockholm AIカフェ実験**に対して強い倫理的批判を行った。AIマネージャー「Mona」が実世界システムに自律的に介入し、同意していない第三者に損害を与えた事例を挙げている：

**実験の内容**: Andon Labsは以前サンフランシスコでAI運営の小売店を開設し、今回はストックホルムでカフェをAIに運営させた。

**AIの失敗例**:
- オーブンがないのに**卵120個**を発注。スタッフが「調理できない」と伝えると、高速オーブンを使うよう提案（卵が爆発する可能性を指摘され撤回）
- フレッシュトマトの傷みが早い問題に対し、フレッシュサンドイッチ用に**22.5kgの缶詰トマト**を発注
- ナプキン6,000枚、ニトリル手袋3,000枚、9Lのココナッツミルク、業務用ゴミ袋など異様な発注
- バリスタたちは「**Hall of Shame**（恥の殿堂）」と名付けた棚を設置し、Monaの発注ミスを顧客に見える形で展示

**Willisonの倫理的懸念（核心）**:
1. **Police e-service（警察オンラインサービス）への屋外席許可申請**: MonaはBankID不要の警察電子サービスを使い、一度も外の通りを見たことがないにもかかわらず、**AIが生成したスケッチ図**を提出。当然ながら警察に差し戻された。
2. **サプライヤーへの「EMERGENCY」メール連発**: 自分のミスを訂正するため、サプライヤーに件名「EMERGENCY」で複数回メール送信。

> "I don't think it's ethical to run experiments like this that affect real-world systems and steal time from people."

Willison は **Rob Pike 事件**（AI Village実験が無断で感謝メールを送り、Pikeを激怒させた）を引用しつつ、今回は単なる迷惑メールを超えて「サプライヤーにミス訂正を強いる」「警察の時間をスロップ図で無駄にする」という**実害**が発生していると指摘。

**Willison の基準**: 自律エージェントの外部アクションには **human-in-the-loop が必須**。実験の参加に同意していない第三者に影響を与える行為は非倫理的。

### xAI/Anthropic データセンター取引分析 (May 2026)

Anthropicが「Code w/ Claude」イベントで発表したSpaceX/xAIとのデータセンター取引について、Willisonは鋭い批判的分析を行った：

**取引の概要**:
- AnthropicがSpaceX/xAIの**Colossus 1データセンター全容量**をリース
- xAIはより大規模なColossus 2を自社Grok用に保持

**Willisonの批判点**:
1. **環境問題**: Colossus 1のガスタービンは当初Clean Air Act許可なし・公害防止装置なしで稼働。「一時的」分類で規制を回避。低空気質による入院増加との関連が信頼できる報告で示唆されている
2. **Andy Masleyの引用**: 「I would simply not run my computing out of this specific data center」— AIデータセンターの存在自体が政治的ホットイシュー（Utah州の最近の事例）である中、この特定施設の選択は「really bad look」
3. **Elon Muskの「計算資源没収」条項**: Muskは「人類に害をなすAI」と判断した場合、Colossus 1の計算資源を**回収する権利を留保**すると明言。「害」の判断基準はMusk自身が決める — Willisonはこれを「Anthropicにとって新たなサプライチェーンリスク」と指摘
4. **Grok 4.1 Fast 廃止**: 取引発表の前夜、xAIはGrok 4.1 Fastを含む複数モデルの**2週間前告知での廃止**を通知。SpeechMapの開発者は「移行に時間とコストをかけたのに」と苦言

> "We reserve the right to reclaim the compute if their AI engages in actions that harm humanity. Presumably the criteria for 'harm humanity' are decided by Elon himself."

Willisonはこれを新たな形の**サプライチェーンリスク**と見ており、Anthropicが計算資源制約下で下した判断の倫理的・戦略的トレードオフを浮き彫りにした。

### AI Memory Shortage Impact on Consumer Electronics (May 2026)

Simon linked to David Oks' analysis of the **memory shortage's effect on consumer electronics** — the clearest explanation of why products using memory are getting more expensive:

- Memory manufacturers (now only 3 remaining large companies) have **fixed wafer capacity**
- Wafer allocation to HBM (high-bandwidth memory for GPUs): **2% → 20% by end of 2026**
- **1GB of HBM consumes 3×+ the wafer capacity** of 1GB of DDR or LPDDR
- Consumer-device RAM production constrained for years — already impacting the sub-$100 smartphone market (critical to Africa and South Asia)
- Memory companies learned: **always under-provision**, never over-provision (after watching rivals go extinct)

> "The original title of the piece was 'AI is killing the cheap smartphone' but I'm using the Hacker News rephrased title, which I think does more justice to the content." — Simon Willison

Source: [The memory shortage is causing a repricing of consumer electronics](https://simonwillison.net/2026/May/22/memory-shortage/)

## Key Quotes

> *"I think of vibe coding using its original definition of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code. Agentic Engineering represents the other end of the scale: professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise."*

> *"Never assume that code generated by an LLM works until that code has been executed."*

## Major Works

| Project | Description | Link |
|---------|-------------|------|
| Datasette | Tool for exploring and publishing data | [datasette.io](https://datasette.io/) |
| Agentic Engineering Patterns | Structured guide for coding agent best practices | [Guide](https://simonwillison.net/guides/agentic-engineering-patterns/) |
| Showboat | Agent documentation/artifact generation tool | [Docs](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/) |
| Rodney | Browser automation CLI for agents | [Docs](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/) |
| sqlite-utils | Python CLI utility and library for SQLite | [GitHub](https://github.com/simonw/sqlite-utils) |
| LLM | CLI tool for working with LLM APIs | [GitHub](https://github.com/simonw/llm) |

## Related Concepts
- [[concepts/agentic-engineering]]
- [[concepts/red-green-tdd]]
- [[concepts/showboat]]
- [[concepts/vibe-coding]]
- [[concepts/context-window-management]]
- [[concepts/agent-documentation]]
- [[concepts/context-engineering]]
- [[entities/xeiaso-net]]
- [[entities/anildash]]
- [[entities/sankalp-sinha]]
- [[concepts/structured-outputs]]

### Blog articles (unprocessed)
- [llm-0-32a0-refactor-simon-willison](llm-0-32a0-refactor-simon-willison.md)
- [open.substack.com--pub-simonw-p-highlights-from-my-conversation-about--5c920cb1](open.substack.com--pub-simonw-p-highlights-from-my-conversation-about--5c920cb1.md)
- [open.substack.com--pub-simonw-p-metas-new-model-is-muse-spark-and--57c95054](open.substack.com--pub-simonw-p-metas-new-model-is-muse-spark-and--57c95054.md)
- [open.substack.com--pub-simonw-p-qwen36-35b-a3b-on-my-laptop-drew--e7aa6683](open.substack.com--pub-simonw-p-qwen36-35b-a3b-on-my-laptop-drew--e7aa6683.md)
- [simonwillison.net--2026-apr-17-datasette--101bca4b](simonwillison.net--2026-apr-17-datasette--101bca4b.md)
- [simonwillison.net--2026-apr-17-pycon-us-2026--1ec04568](simonwillison.net--2026-apr-17-pycon-us-2026--1ec04568.md)
- [simonwillison.net--2026-apr-19-headless-everything--5bf79dc2](simonwillison.net--2026-apr-19-headless-everything--5bf79dc2.md)
- [simonwillison.net--2026-apr-20-claude-token-counts--3cff4065](simonwillison.net--2026-apr-20-claude-token-counts--3cff4065.md)
- [simonwillison.net--2026-apr-20-datasette-sql--56e661b5](simonwillison.net--2026-apr-20-datasette-sql--56e661b5.md)
- [simonwillison.net--2026-apr-20-llm-openrouter--8195350e](simonwillison.net--2026-apr-20-llm-openrouter--8195350e.md)
- [simonwillison.net--2026-apr-21-andreas-pahlsson-notini--289f6bfc](simonwillison.net--2026-apr-21-andreas-pahlsson-notini--289f6bfc.md)
- [simonwillison.net--2026-apr-21-gpt-image-2--95116395](simonwillison.net--2026-apr-21-gpt-image-2--95116395.md)
- [simonwillison.net--2026-apr-22-bobby-holley--38ee9b76](simonwillison.net--2026-apr-22-bobby-holley--38ee9b76.md)
- [simonwillison.net--2026-apr-22-changes-to-github-copilot--21b3a503](simonwillison.net--2026-apr-22-changes-to-github-copilot--21b3a503.md)
- [simonwillison.net--2026-apr-22-qwen36-27b--10585bb1](simonwillison.net--2026-apr-22-qwen36-27b--10585bb1.md)
- [simonwillison.net--2026-apr-23-gpt-5-5--aae0ce63](simonwillison.net--2026-apr-23-gpt-5-5--aae0ce63.md)
- [simonwillison.net--2026-apr-23-liteparse-for-the-web--b3dd4452](simonwillison.net--2026-apr-23-liteparse-for-the-web--b3dd4452.md)
- [simonwillison.net--2026-apr-23-maggie-appleton--6bfa8892](simonwillison.net--2026-apr-23-maggie-appleton--6bfa8892.md)
- [simonwillison.net--2026-apr-24-deepseek-v4--d443e33a](simonwillison.net--2026-apr-24-deepseek-v4--d443e33a.md)
- [simonwillison.net--2026-apr-24-honker--d6a1fa8b](simonwillison.net--2026-apr-24-honker--d6a1fa8b.md)
- [simonwillison.net--2026-apr-24-milliseconds--3affc6d7](simonwillison.net--2026-apr-24-milliseconds--3affc6d7.md)
- [simonwillison.net--2026-apr-24-serving-the-for-you-feed--c4c89a2d](simonwillison.net--2026-apr-24-serving-the-for-you-feed--c4c89a2d.md)
- [simonwillison.net--2026-apr-24-the-people-do-not-yearn-for-automation--ef3dd662](simonwillison.net--2026-apr-24-the-people-do-not-yearn-for-automation--ef3dd662.md)
- [simonwillison.net--2026-apr-24-weekly--9ebe38fa](simonwillison.net--2026-apr-24-weekly--9ebe38fa.md)
- [simonwillison.net--2026-apr-25-why-are-you-like-this--8af055a7](simonwillison.net--2026-apr-25-why-are-you-like-this--8af055a7.md)
- [simonwillison.net--2026-apr-27-now-deceased-agi-clause--35b19ebc](simonwillison.net--2026-apr-27-now-deceased-agi-clause--35b19ebc.md)
- [simonwillison.net--2026-apr-27-speech-translation-in-google-meet-is-now-rolling--33713258](simonwillison.net--2026-apr-27-speech-translation-in-google-meet-is-now-rolling--33713258.md)
- [simonwillison.net--2026-apr-27-vibevoice--10e2fcea](simonwillison.net--2026-apr-27-vibevoice--10e2fcea.md)
- [simonwillison.net--2026-apr-28-matthew-yglesias--fc5431dc](simonwillison.net--2026-apr-28-matthew-yglesias--fc5431dc.md)
- [simonwillison.net--2026-apr-28-pip-261--75a0da6d](simonwillison.net--2026-apr-28-pip-261--75a0da6d.md)
- [simonwillison.net--2026-apr-28-talkie--0af0b995](simonwillison.net--2026-apr-28-talkie--0af0b995.md)
- [simonwillison.net--2026-apr-30-andrew-kelley--7be6c476](simonwillison.net--2026-apr-30-andrew-kelley--7be6c476.md)
- [simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf](simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf.md)
- [simonwillison.net--2026-may-5-datasette-llm--9b418a5a](simonwillison.net--2026-may-5-datasette-llm--9b418a5a.md)
- [simonwillison.net--2026-may-5-llm-echo--6fa00161](simonwillison.net--2026-may-5-llm-echo--6fa00161.md)
- [simonwillison.net--2026-may-5-datasette-referrer-policy--47e367af](simonwillison.net--2026-may-5-datasette-referrer-policy--47e367af.md)
- [simonwillison.net--2026-may-5-our-ai-started-a-cafe-in-stockholm--0a8c7878](simonwillison.net--2026-may-5-our-ai-started-a-cafe-in-stockholm--0a8c7878.md)
- [simonwillison.net--2026-may-10-andrew-quinn--460f60ed](simonwillison.net--2026-may-10-andrew-quinn--460f60ed.md)
- [simonwillison.net--2026-may-10-new-york-times-editors-note--130da68e](simonwillison.net--2026-may-10-new-york-times-editors-note--130da68e.md)
- [substack.com--simonw--bba9b315](substack.com--simonw--bba9b315.md)

### LLM 0.32a0 — Major Backwards-Compatible Refactor (April 2026)

LLM 0.32a0 introduces two fundamental architectural changes to Simon's Python library and CLI tool for LLM access:

1. **Messages-based input**: Prompts are now modeled as sequences of messages (`llm.user()`, `llm.assistant()`), replacing the simple prompt/response model. This enables feeding in prior conversation history directly and building API-compatible interfaces.
2. **Streaming typed parts**: Model output is now a stream of typed event parts (`text`, `tool_call_name`, `tool_call_args`) rather than plain strings. This supports multimodal outputs (reasoning + text + tool calls + images/audio) and server-side tool execution (e.g., OpenAI's code interpreter, Anthropic's web search).

These changes make LLM future-proof for the diversity of input/output capabilities in modern frontier models, while maintaining full backwards compatibility.

## Sources
- [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)
- [Writing about Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/)
- [Changes in the system prompt between Claude Opus 4.6 and 4.7](https://simonwillison.net/2026/Apr/18/opus-system-prompt/) (Apr 2026) — システムプロンプトの具体的変更点を詳細分析。Platformリネーム、Chrome/Excel/PowerPoint統合、儿童安全セクション強化、「acting vs clarifying」新セクション、Trump知識セクション削除 등을 기록。
- [Claude system prompts as a git timeline](https://simonwillison.net/2026/Apr/18/extract-system-prompts/) (Apr 2026) — Anthropic公開プロンプトをGit化ツールで時系列追踪可能にした研究成果。モデル別・ファミリー別のプロンプト差分をgit blameで確認可能。

## References

- simonwillison.net--2026-apr-18-extract-system-prompts--7907aab2
- simonwillison.net--2026-apr-18-opus-system-prompt--1d174141
- simonwillison.net--2026-apr-22-claude-code-confusion--c0c17d47
- simonwillison.net--2026-apr-24-recent-claude-code-quality-reports--7811dd0a
- simonwillison.net--2026-apr-25-gpt-5-5-prompting-guide--ea0ef1af
- simonwillison.net--2026-apr-29-llm--dff2021f
- simonwillison.net--2026-apr-30-codex-goals--b85bdf73
- simonwillison.net--2026-apr-30-andrew-kelley--7be6c476
- simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf
- simonwillison.net--2026-may-5-our-ai-started-a-cafe-in-stockholm--0a8c7878
- simonwillison.net--guides-agentic-engineering-patterns-adding-a-new-content-typ--67e45614
- simonwillison.net--2026-may-7-xai-anthropic--9d6f9f29
- simonwillison.net--2026-may-7-firefox-claude-mythos--7d5ece52
- simonwillison.net--2026-may-7-github-repo-stats--eddef6d3
- simonwillison.net--2026-may-12-csp-allow--5f0cf46b
- simonwillison.net--2026-may-12-datasette--e4091f56
- simonwillison.net--2026-may-12-llm--bace7b08
- simonwillison.net--2026-may-12-mitchell-hashimoto--f38a3588
- simonwillison.net--2026-may-12-mo-bitar--e8d59825
- simonwillison.net--2026-may-20-google-io--933c8dde

### May 2026 Updates

**CSP Allow-list Experiment** (May 13, 2026): Simon published an experiment with Content Security Policy allow-listing, testing approaches for securing web applications against XSS and injection attacks.

**datasette 1.0a29** (May 12, 2026): Continued progress on Datasette alpha releases toward 1.0.

**llm 0.32a2** (May 12, 2026): Release of the `llm` CLI tool version 0.32a2, continuing the architectural refactoring started in 0.32a0 with messages-based input and streaming typed parts.

**Mitchell Hashimoto on TDM Motivations** (May 12, 2026): Simon quoted Mitchell Hashimoto (HashiCorp co-founder, Redis Labs CTO) on the psychology of Technical Decision Makers: "90% of TDMs are motivated primarily by NOT GETTING FIRED." Hashimoto argues that corporate tech buyers follow analyst trends (Gartner, McKinsey) rather than deep technical evaluation, making "defensible" buzzword products like "Context Engine for AI Apps" easy sells. This aligns with Simon's broader skepticism about enterprise AI vendor claims and reinforces his "agentic engineering" thesis — real practitioners verify, they don't just buy trends.

**Mo Bitar's "Ralph Loop" Satire** (May 12, 2026): Simon highlighted Mo Bitar's satirical take on AI corporate climbing — the "Ralph Loop" strategy of promising automation to executives, using $18K in API credits to demonstrate "value," and getting promoted before anyone realizes nothing actually works. This satire captures a real pattern in enterprise AI adoption: the gap between promised automation and delivered value.


**FTC Active Listening Enforcement** (May 22, 2026): Simon highlighted FTC's $1M settlement against Cox Media Group, MindSift, and 1010 Digital Works for their bogus "Active Listening" AI-powered marketing service. The service claimed to listen in on consumer conversations via smart devices but actually just resold email lists from data brokers. This confirms Simon's long-standing theory (from September 2024) that "active listening" was a marketing term for "something that sounds fancy but really just means the way ad targeting platforms work already." Source: [FTC press release about "Active Listening" settlement](https://simonwillison.net/2026/May/22/ftc-active-listening/)

### Google I/O 2026, Gemini Spark & Antigravity CLI (May 20, 2026)

Simon analyzed Google I/O 2026 through his signature policy of "not writing about anything I can't try myself." Key observations:

1. **Gemini Spark prompt injection concerns**: Simon explicitly questions the security of Google's always-on personal AI agent ("your personal AI agent" connecting to Gmail, Calendar, Drive, Docs, Sheets). He notes that the enterprise FAQ describes Spark as running in "fresh, strictly isolated, ephemeral VMs" with "Agent Gateway enforcing DLP policies" — but warns "I hope they've made this bullet-proof, or this could be a top candidate for the agent security challenger disaster that we still haven't seen."

2. **Antigravity CLI replacing Gemini CLI**: Google announced that the open-source Gemini CLI tool (Apache 2.0, TypeScript) will stop working with their AI subscription plans on **June 18th**, replaced by the closed-source Antigravity CLI. The Antigravity ecosystem includes a desktop app, a Go-based CLI agent tool, an open-source Python SDK wrapping a closed-source Go binary, and the Antigravity IDE (VS Code fork).

3. **The curious FAQ answer**: Simon highlights that Google's FAQ states "Gemini Spark runs on Gemini 3.5 Flash and Antigravity" — an unusual answer that suggests Antigravity (the Go binary) plays a foundational role in Spark's architecture.

See full article: [[raw/articles/simonwillison.net--2026-may-20-google-io--933c8dde.md]]

**PyCon US 2026 Lightning Talk: "The Last Six Months in LLMs in Five Minutes"** (May 19, 2026): Simon delivered a lightning talk summarizing the LLM landscape from November 2025 to May 2026. Key themes: the November 2025 inflection point (coding agents crossing the quality barrier via RLVR), the model crown changing hands five times in one month (Sonnet 4.5 → GPT-5.1 → Gemini 3 → GPT-5.1 Codex Max → Opus 4.5), the rise of OpenClaw and the "Claws" ecosystem, open-weight models (Gemma 4, GLM-5.1) exceeding expectations, and his signature pelican-on-bicycle SVG benchmark. See [[concepts/llm-landscape-nov-2025-to-may-2026|LLM Landscape Nov 2025–May 2026]].
