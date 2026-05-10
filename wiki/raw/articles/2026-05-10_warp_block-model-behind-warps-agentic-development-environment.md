---
title: "The Block Model Behind Warp's Agentic Development Environment"
source: "Warp Blog"
url: "https://www.warp.dev/blog/block-model-behind-warps-agentic-development-environment"
scraped: "2026-05-10T01:27:02.156151+00:00"
lastmod: "2026-05-04T14:33:47.000Z"
type: "sitemap"
---

# The Block Model Behind Warp's Agentic Development Environment

**Source**: [https://www.warp.dev/blog/block-model-behind-warps-agentic-development-environment](https://www.warp.dev/blog/block-model-behind-warps-agentic-development-environment)

Engineering
The Block Model Behind Warp's Agentic Development Environment
David Stern
Oz
April 29, 2026
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Nearly five years ago, Aloke Desai
wrote
about Warp's foundations: a list of typed "blocks," a GPU-backed renderer, and a custom UI framework built in Rust. At the time, those choices were motivated by wanting a better terminal. Today Warp is an Agentic Development Environment — a place where developers and AI agents collaborate on real code in the same session — and the same foundation still holds it up.
We think that's worth writing about, for two reasons. First: Warp is now
open source
, which means we can point at real code rather than just describe it. Second: the block model Aloke described in 2021 turns out to be a good fit for the ADE era. In this post, we'll flesh out the details of that block model — starting with how a shell tells Warp that a block exists, then how Warp stores that block, and finally how the same model extends to hold agent conversations alongside your commands — with pointers into the source wherever you want to keep reading on your own.
What's a Block?
A traditional terminal — xterm, iTerm2, the
Terminal.app
bundled with macOS — thinks of its viewport as a single two-dimensional grid of character cells. As programs print, their output is parsed and laid out into that grid, filling rows top to bottom. When the grid fills, older rows are pushed into scrollback and new ones appear at the bottom. The grid
is
the terminal: from the application's point of view, there's no such thing as a "command," just a stream of bytes in and a stream of bytes out.
Warp's viewport is structured differently. Rather than one big grid, it's an ordered list of
blocks
: typed, self-contained units of content that stack vertically and scroll together. We call this the
BlockList
. Each block knows what kind of thing it is, and that decides how it's stored and how it's rendered.
Where a traditional terminal is a single grid of character cells, Warp’s BlockList is an ordered list of typed blocks: terminal blocks wrapping a command and its output, and rich content blocks — like the agent conversation here — that host an arbitrary UI view in the same list.
Originally, all blocks in Warp were terminal blocks: each one wrapping a single command along with its output. That structure gives you affordances you don't get from a plain grid: you can navigate between commands with a keystroke, select an entire command's output in one gesture, share a block as a link, and run follow-up actions on a whole block at a time. Today, some blocks aren't tied to a command at all — most notably, agent conversation blocks, which render an agent session's reasoning, tool calls, and diffs inline alongside your own work, while the agent's own shell commands still show up as ordinary command/output blocks in the same stream.
That's the user-facing model. The rest of this post is about what makes it work — starting with how a shell tells Warp where one block ends and the next begins.
A Brief Terminal Primer
Feel free to skip ahead if you already know what a PTY is.
A terminal emulator talks to programs through a channel called a
pseudo-terminal
, or PTY for short. At a high level, a PTY is just a bidirectional byte stream between two programs. Most of those bytes are plain characters — either typed input or text to display — but either side can also interleave
control sequences
: short runs of special bytes that mean things like "move the cursor up one row" (
0x1B 0x5B 0x41
), "clear the current line" (
0x1B 0x5B 0x32 0x4B
), or "set the foreground color to green" (
0x1B 0x5B 0x33 0x32 0x6D
). Longstanding specifications define a large, standard set of these, but they also leave room for custom additions, which Warp takes advantage of, as you'll see later in this post.
Unintuitively, the terminal doesn't decide what shows up when you type. Your keystrokes go straight into the PTY as bytes, and the program on the other end decides what to send back. Usually it echoes those keystrokes as characters for the terminal to display, maybe paired with a cursor move or a color change, but it doesn't have to. So even the text of the command you're in the middle of typing is, from the terminal's point of view, just more bytes coming back from the program.
The shell — zsh, bash, fish, PowerShell — is one such program, running on the other end of the PTY. But the terminal doesn't formally know anything about what's on the other end: it can't inherently distinguish bytes coming from the shell itself (printing a prompt, say) from bytes produced by a program the shell has run. That distinction, however, is exactly what we'll need in order to segment the output into blocks.
Marking Block Boundaries
For any of this to work, Warp needs to know when one command ends and the next begins. As we just saw, the terminal itself can't tell — prompts, typed commands, and command output all arrive as bytes on the same stream. That means we need to define a small contract between Warp and the shell — a way for the shell to tell Warp what it's doing.
The only entity that actually knows is the shell, so we ask it. Warp ships a
small set of bootstrap scripts
— one each for bash, zsh, fish, and PowerShell — that run when a shell starts up under Warp. Each one hooks into the shell's
precmd
and
preexec
extension points — short for "pre–command line" and "pre–command execution" — natively where they exist, or via
bash-preexec
for bash. The bootstrap scripts use these hooks to emit events back to Warp on stdout. Those events are wrapped in escape sequences — the same class of sequences a terminal uses for things like "set the window title" — with a JSON payload inside describing what just happened.
In zsh, that boils down to a few lines in
zsh_body.sh
:
Sh
warp_preexec () {  local warp_escaped_command="$(warp_escape_json $1)"  warp_send_json_message "{\"hook\": \"Preexec\", \"value\": {\"command\": \"$warp_escaped_command\"}}"  # ... }
warp_preexec
is registered with zsh via its built-in
preexec_functions
array, and zsh calls it right before executing each command, allowing us to separate the command from its output. There's an analogous
warp_precmd
that fires after each command finishes, carrying prompt metadata like the working directory and git state; alongside a small command-finished event carrying the exit code, that's enough for Warp to close out one block and initialize the next.
On the Warp side, our ANSI parser decodes the escape sequence, parses the JSON into a typed
DProtoHook
enum, and dispatches to typed methods on the
Handler
trait:
Golang
fn handle_decoded_hook(&mut self, hook: Result<DProtoHook, serde_json::Error>) {  match hook {  Ok(DProtoHook::CommandFinished { value }) => self.handler.command_finished(value),  Ok(DProtoHook::Precmd { value }) => self.handler.precmd(value),  Ok(DProtoHook::Preexec { value }) => self.handler.preexec(value),  // ...other variants (and error handling) elided...  } }
The same channel carries other information Warp needs from the shell — pwd and git state ride along with the
Precmd
payload. The same pattern runs the other way, too. When Warp needs to execute a command on a remote machine to power a feature — for completions, for example — it writes the command into the shell's input as usual, and instructs the shell to wrap the
response in the same kind of escape-sequence markers
so Warp can pluck it back out as out-of-band data rather than normal shell output. The application-level protocol grows as we need it, but the transport stays fixed — each new kind of event is just another variant in the
DProtoHook
enum and another handler method, wrapped in the same escape-sequence envelope we started with.
The net effect: the contract we actually need is pretty small. A
precmd
/
preexec
equivalent (native or bolted on) plus the ability to print arbitrary bytes on stdout is enough. Every shell Warp supports has both — and in principle, anything else with the same shape (a REPL, say) could implement the same API and slot in.
Storing Terminal Blocks
Now that we can structure the PTY output into blocks, we need somewhere to put them. That's the
BlockList
: an ordered sequence of blocks, where each entry is either a terminal block (one that wraps a shell command) or a rich content block (one that hosts an arbitrary UI view). Every block on screen lives in that list.
Inside a terminal block are, at a high level, two grids: a
command-side
grid, which holds the prompt and the command the user typed, and an
output grid
, which holds whatever that command printed. Each is logically a 2D matrix of cells — a row-by-column array of characters plus per-cell styling.
warp_preexec
flips the block from "writing the command" to "writing the output"; when the command finishes, the block is closed out. Once the next block starts, a terminal block is largely immutable; window resizes can reflow its grids, but otherwise nothing writes to it again.
There's a reason we specified that each is only
logically
a 2D grid of cells. In memory, Warp uses two different physical representations for them:
GridStorage
and
FlatStorage
.
The first is
GridStorage
: the naive rows-of-cells layout. It's mutable, it supports random access, and it's what we use for the portion of a grid the shell's cursor can still reach — the active region where new output is being written, plus the alt screen when a fullscreen program is running. Cheap to modify, but it pays for that with memory: every visible row is a preallocated list of cells, whether or not those cells contain anything.
GridStorage
began as an adaptation of Alacritty's
Grid
implementation; we're very grateful to the maintainers for their generous technical feedback on the approach when we were getting started in 2020.
In GridStorage, every grid position holds a full Cell struct (c, fg, bg, flags). Empty cells still occupy a slot, just at default values, so memory scales with the grid’s dimensions rather than its content.
The second is
FlatStorage
: a packed buffer of the printed content plus a small index mapping row numbers to byte offsets into that buffer. There's no per-cell slot and no preallocated grid; styling is kept in separate interval maps keyed on byte offsets. Keying styling on byte offsets rather than row/column coordinates is a key design choice: when the grid resizes, the styling data doesn't need to move — only the row index has to be rebuilt.
FlatStorage
supports indexing, scanning, push, and pop — and deliberately doesn't support insert, because a flat buffer can't insert cheaply. That limitation isn't a problem for its job: scrollback. Rows that have shifted up out of the cursor's reach can never change, and the memory savings show up block after block for the life of a session.
FlatStorage restructures the same content into a packed byte buffer plus a few sparse tables — a row index and two interval maps for styling attributes — each storing only the byte offsets where something changes. The same logical content fits in a fraction of GridStorage’s memory by eliminating duplication.
Each storage type is optimized for the access pattern it actually sees. Mutable regions stay in
GridStorage
; the rest of the content lives in
FlatStorage
. In practice, that means Warp doesn't have to pay full mutable-grid costs for a block full of lengthy server log output just because the most recent rows are still live.
Fullscreen programs — vim, less, or anything else that takes over the whole terminal via the alt screen — sit outside this setup entirely. The alt screen has no scrollback, gets replaced wholesale when the program exits, and doesn't map onto "a command and its output." Rather than shoehorn it into the block list,
AltScreen
lives alongside the list with its own
GridStorage
. Programs swap between the primary screen (our block list) and the alt screen via the standard control sequences for that mode, and Warp renders whichever one is active.
Back at the
BlockList
level: it isn't a plain
Vec
. Finding "which blocks are in the viewport right now?" naively is O(n) — you'd walk the list from one end, accumulating heights, until you hit the range you cared about. Long Warp sessions accumulate thousands of blocks, so we store heights in a
SumTree
: a balanced tree that aggregates per-block heights at every interior node. That turns "find the blocks that intersect rows A through B" into an O(log n) operation no matter how long the session is. (SumTrees show up all over Warp;
the 2021 post
covers the data structure in more depth if you want to keep reading.)
The performance payoff compounds at render time. Rendering a
BlockList
is virtualized at two levels:
BlockList
level: we only ask blocks that intersect the viewport to render themselves.
Terminal block level: within a visible block, we only render the rows that actually intersect the viewport.
This way, we only pay rendering costs for what you can actually see, no matter how much content the
BlockList
holds in total.
Extending the Model to Agents
The block model has one defining property: the
BlockList
doesn't care what's
inside
a block. It only needs each block's height. That's what the
SumTree
sums over, and that's what the virtualized renderer consults. Anything that can report a height can sit in the list next to terminal blocks, and nothing downstream has to care what it is.
That's what opens the door to
rich content blocks
: arbitrary UI views, plugged into the
BlockList
at a specific position, wrapping a handle to a view the UI layer knows how to render. Terminal blocks and rich content blocks live in the same
BlockHeightItem
enum, share the same SumTree, and pass through the same virtualized renderer — none of which need to know which kind of block they're handling.
A real agent session shows what that looks like in practice:
You type
cargo test
and hit enter. That's a terminal block, same as always.
You ask the agent to fix the failures. A rich content block appears — the agent's conversation view — showing its plan and reasoning.
The agent runs its own shell commands to reproduce the failure. Those are terminal blocks too, indistinguishable from what you'd type yourself: command grids, output grids, storage, the whole thing.
The agent renders intermediate thinking, tool-call results, and a unified diff for review. Those are all rich content.
You run
git diff
yourself to double-check. Another terminal block.
All of that lives in a single
BlockList
, scrolling as one continuous stream. None of it requires special cases in the height/indexing machinery or the virtualized renderer. Those parts don't need to know what a "conversation" is; they only need a sequence of items with heights.
Notably, the full
BlockList
in the model and the list you actually see on screen aren't the same thing. Warp's view layer filters and collapses blocks based on context — whether an agent view is active, which conversation you're looking at, and what kind of block it is. In a remote session, if Warp runs a command on your behalf to generate tab completion results,
the block for that command
is created in the model but hidden by default in the UI. Rich content associated with a specific agent conversation is
hidden when a different view is active
. Terminal blocks an agent ran on your behalf can be presented as compact summaries inside the conversation view, expandable on demand. Under the hood, the block list already separates the underlying data (the
Vec<Block>
) from the height-indexed structure that drives viewport lookups (the SumTree over
BlockHeightItem
s), so "hidden in this view" can be as cheap as a zero-height entry. The view layer reads from that same structure at render time, and since anything hidden carries zero height, it's naturally skipped over without any special-case code in the renderer.
That separation between the underlying model and the view turns out to matter. It's a big part of how the same block system could grow from "better terminal" infrastructure into the foundation for an ADE — without being reinvented from scratch.
Building in the Open
For years, "how Warp works" was something we could describe but not show, and open-sourcing Warp closes that gap. But access to the code is only half of what's new. Warp's development is also
moving into the open
: the roadmap, the issues, and the day-to-day feature work are things you can now see and shape. The model we're building around is one where Oz agents do the implementation heavy lifting, and people — our team and the community both — decide what to build, spec how it should behave, and verify that the result works. We invite you to help decide what gets built next — come join us at
github.com/warpdotdev/warp
.
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
Mar 16, 2026  ·  9 min
Building Computer use for Cloud Agents
Imagine you're on your phone and a teammate messages you: the onboarding flow is broken after the latest deploy, the signup form isn't validating inputs, the progress bar is stuck, and the confirmation screen doesn't…
