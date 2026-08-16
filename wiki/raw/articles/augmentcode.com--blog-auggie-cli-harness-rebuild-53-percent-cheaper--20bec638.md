---
title: "How we rebuilt the Auggie CLI harness to make tasks 53% cheaper than Claude Code"
url: "https://augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper"
fetched_at: 2026-08-16T10:14:42.187335+00:00
source: "Augment Code Blog"
tags: [blog, raw]
---

# How we rebuilt the Auggie CLI harness to make tasks 53% cheaper than Claude Code

Source: https://augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper

Every token you spend should buy as much finished work as possible is one of the core principles behind Cosmos and the Auggie CLI. It drives engineering decisions long before it shows up in anything customer-facing. There are two  levers on value per token. One is the context engine: better context means better answers in fewer tokens. The other is the harness: the agent loop, the tool surface, session management, everything that turns model capability into finished tasks. We started by building the industry's leading
context engine
, and now we've made a major investment in improving the harness.
Earlier this year we rebuilt the Auggie CLI's harness from the ground up. On SWE-bench Pro, at the same pass rate, Auggie v2 completes a task for $1.27 where Claude Code spends $2.70. That is 53% cheaper. Even though v1 was already 27% less expensive than Claude Code we knew there was more we could do, the rebuild roughly doubled the efficiency gap without giving up a point of quality.
Getting there took three months of deliberate prototyping and ended with a fork of
Pi
, an excellent minimal open-source coding harness by Mario Zechner, with our context engine moved into its extension system. The main learning: subtraction. Fewer tools means less tax on every call, and one good retrieval saves ten turns of exploration.
The first Auggie CLI shipped in late 2025 and benchmarked competitively from the start. Rebuilding something that is winning needs a better reason than restlessness. We had two.
The first is that a harness encodes assumptions about what models cannot do, and model capability is moving fast enough that those assumptions need to be revisited frequently. V1's wide tool surface made sense for the models it was designed around. The number of tools, the size of their schemas, the shape of the loop: all of it gets serialized into every request, and every capability jump changes which parts still help and which are now overhead the customer pays for on each call.  That turned out to be where most of the money went, so I'll come back to it.
The second reason was structural. V1 grew fast; within months it was about 1,020 TypeScript files and 250k lines, and it had the failure mode every fast-growing codebase knows: coupling. The TUI, the agent loop, session persistence, and the tool implementations all knew about each other. Changing the process-management tools meant touching renderers. Changing retrieval meant touching the agent loop. Each new feature cost a little more than the last.
In January we started looking at what a v2 should stand on.
We spent January through March evaluating foundations, and the pace was deliberate. The CLI is how developers experience Augment every day, and swapping its foundation is the kind of cut you measure twice for.
The first prototype was on the Vercel AI SDK, in January. It is excellent at what it is designed for: streaming primitives and provider abstraction. We were drawn to that solution to support another core principle of being model agnostic, but it is an LLM SDK not an agent harness, so for our use the agent loop, tool orchestration, session persistence, compaction, and the whole TUI would have been ours to write and maintain. We built enough to run the evals, and the results didn't justify the amount of harness code we would own forever.
The second prototype was on Mastra, in February.  The prototype got far: a TUI on OpenTUI and React, streaming markdown with syntax highlighting, our codebase-retrieval integration, theming. Mastra is a capable framework, but it is aimed at a broader class of agent applications than a terminal coding agent, so we were still writing most of the hard parts ourselves. And a React reconciler driving a terminal is a lot of dependency for what a CLI needs.
The third was Pi, in March. Pi is a minimal terminal coding harness by Mario Zechner, already proven under other production agents. Architecturally it matched our problem exactly: a small core, an extension system we could actually build on, and a purpose-built TUI library instead of a web framework aimed at a terminal.
Pi is not a monolith. Auggie v2 is assembled from three small packages plus an extension layer:
pi-ai
, a unified LLM API across the major providers;
pi-agent-core
, the agent loop with transport abstraction and state management; and
pi-tui
, the terminal UI library.
V1 used Ink, the default choice for a Node CLI built in 2024-2025. Ink runs React and the Yoga layout engine under the hood. Both are solid, but they put two layers between the transcript and the terminal, so every rendering bug became a debugging session through a React reconciler and a flexbox engine. And there were limits we never engineered around: the whole-transcript redraws flickered, and layout occasionally came out wrong.
The AI SDK and Mastra prototypes moved to OpenTUI, which maintains a virtual terminal buffer and keeps it in sync with the real one. That fixes flicker, but you give up the native buffer along the way: the transcript is no longer plain text in your terminal's scrollback, so clicking links and selecting text to copy stop behaving the way terminal users expect. OpenTUI has workarounds for both, but they trade one UX for another, and not everyone was on board with the change.
pi-tui's mechanism is the simplest of the three. A component renders to an array of strings, one per line. Each frame, the TUI diffs the new lines against the previous frame's and repaints only the lines that changed, wrapped in synchronized output (CSI 2026) so the terminal shows each frame whole rather than half-drawn. The output is ordinary lines in the native terminal buffer, so scrollback, link clicking, and text selection keep working the way they always did. There is no reconciler or layout engine in the path. When something renders wrong, the bug is in a function that returns strings.
With a rock solid foundation, we then could leverage the extension system to make Auggie
Auggie
.
Extensions are modules that extend Pi's behavior by leveraging a simple API to intercept with lifecycle events, add UI, customize rendering, and more.
Our proprietary context engine is itself just an extension. It registers the
codebase-retrieval
tool through
pi.registerTool()
and receives the shared Augment API client over an event bus, with no invasive hooks carved into the harness. Our biggest differentiator plugs in through the same public API a community package would use.
It also fixes the coupling problem directly. Changing the context engine touches nothing outside
packages/pi-extensions/context-engine/
. The repo's own contribution guideline now says to prefer changes in
packages/pi-extensions/*
, because features land as extension PRs instead of surgery on the core. Auggie v2 currently ships more than a dozen first-party extensions, including
context-engine
,
subagents
,
lsp
,
mcp
,
tool-permissions
, and
plugins
. Each one is a self-contained package with its own tests, imported by the host through a single
index.ts
.
The payoff is measurable: our commit rate roughly doubled once the architecture settled, from 92 commits in May to 221 in June, with subagents, LSP, the plugin marketplace, MCP with OAuth, and ACP editor support all landing as isolated extension PRs.
Shipping velocity is rarely enough of a reason to rewrite a piece of software, we set out to improve the efficiency with this new platform.
Here is the SWE-bench Pro table first (731 instances, opus4.7 for all three agents):
The pass rates sit within a percentage point of each other, so the quality is the same. On the identical task set, v2 uses about 32% fewer output tokens and about 38% less cache-read traffic than v1. Per instance, it is cheaper than v1 on 88% of tasks and cheaper than Claude Code on 97%.
Three things drive it, and the biggest is the tool surface. V1 exposed a specialized tool for everything:
launch-process
,
read-process
,
kill-process
,
str-replace-editor
,
save-file
, and more. But today's models no longer need specialized tools of that nature. V2 gives the model one
bash
tool and three file tools,
read
,
edit
, and
write
. That narrowing pays off twice per request. Every tool schema is serialized into every LLM call, so a wide toolset is a standing tax on cache-read tokens for the life of the session. It also invites orchestration overhead, where the model spends output tokens picking and sequencing narrow tools when one
bash
call would have done the job.
Retrieval instead of exploration is the second. The context engine's
codebase-retrieval
answers cross-file questions in a single call. Without it, the agent burns turns walking directories and reading files to reconstruct the same picture, spending output tokens and wall-time to do it. This is where the speed advantage compounds too: fewer turns, shorter sessions. Mean wall-time is 330s against Claude Code's 409s, and the full benchmark dropped from 83 hours to 67.
Compaction is the third. Again we leverage Pi's extension system to turn compaction into a dedicated subsystem, instead of a fallback behavior like many other harnesses. It summarizes older history on a dedicated cheaper model, keeps the first user message verbatim so the original task survives summarization, and triggers proactively before the limit rather than reacting to an overflow error.
On Terminal Bench 2.0 the same architecture pushed quality up while cost went down. Task pass rate went from 70.8% to 74.2%, and cost per passed trial went from $1.26 to $1.11.
Our fork of pi-mono is more than a snapshot: we re-scoped the packages under our own namespace and we still sync upstream improvements, most recently pi v0.74.0. The changelog's first line says auggie-v2 was forked from pi-mono's coding-agent package, and links to the upstream changelog for the pre-fork history.
Pi is good work, and its maintainer's design principle, keep everything minimal and don't complicate what is already sufficient, is why this rebuild worked after two attempts stalled. Pi is also proven in production. To the pi community: thank you, and since pi packages generally work with Auggie, if you build one, try it.
Cosmos cloud agents are getting v2 now. The UX is unchanged on purpose, so you inherit the token efficiency without noticing. The CLI switches at the end of July: v2 becomes the Auggie CLI, and v1 is deprecated. The visible differences are the TUI, with no flicker, transcript markdown, and paste markers that collapse large pastes into a compact
[paste #1 +45 lines]
line, plus the extension-powered feature set:
/fork
, plugins, skills, subagents, MCP with OAuth, and LSP.
Same quality, roughly half the cost of the leading alternative, on a foundation where the next feature is cheaper to build than the last. Those kinds of gains are exactly why you make the bold decision to rebuild from scratch.
