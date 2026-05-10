---
title: "Codex Models Now Available in Warp"
source: "Warp Blog"
url: "https://www.warp.dev/blog/codex-models-in-warp-apply-patch-and-prompting-changes"
scraped: "2026-05-10T01:27:13.262973+00:00"
lastmod: "2026-04-07T02:42:24.000Z"
type: "sitemap"
---

# Codex Models Now Available in Warp

**Source**: [https://www.warp.dev/blog/codex-models-in-warp-apply-patch-and-prompting-changes](https://www.warp.dev/blog/codex-models-in-warp-apply-patch-and-prompting-changes)

Engineering
Codex Models Now Available in Warp
Suraj Gupta
December 22, 2025
We’re excited to announce that Warp now supports the latest OpenAI Codex models, unlocking the coding performance improvements that these models deliver over the core GPT models.
Why now?
Support for Codex has been a frequently requested feature since the Codex models were first released (see
Warp issue #7490
). Until recently, however, integrating Codex into Warp resulted in a meaningfully degraded experience.
Early Codex models were heavily optimized for the Codex CLI harness. When used inside Warp’s agent harness, core behaviors suffered: planning quality regressed, the models failed to reliably invoke Warp’s optimized file-search tools, and overall task completion was less consistent than with the mainline GPT models.
However, the latest generation of Codex models is significantly more robust across heterogeneous agent environments. With targeted changes to our harness (see below), Codex now works well with Warp’s agent while preserving the core model strength that users expect.
Just as importantly, Codex models are now reaching SOTA performance for coding workloads. In our internal evaluations, we’ve observed a 3–5% performance improvement over their standard GPT equivalents across a range of agentic coding tasks. We’re also excited about future iterations of codex models and believe the work to integrate will pay dividends for future model releases.
The apply_patch tool
High-quality file editing is foundational to any effective coding agent. While many LLMs are trained on string-replacement-based editing tools (i.e., given an unstructured search block S, replace it with R), GPT-family models have been trained with a more structured diff format, called the V4A patch format. Codex models are heavily trained on the
apply_patch
tool’s V4A patch format, which can be described using a context-free grammar (
reference
):
YAML
start: begin_patch hunk+ end_patch
begin_patch: "*** Begin Patch" LF
end_patch: "*** End Patch" LF?

hunk: add_hunk | delete_hunk | update_hunk
add_hunk: "*** Add File: " filename LF add_line+
delete_hunk: "*** Delete File: " filename LF
update_hunk: "*** Update File: " filename LF change_move? change?

filename: /(.+)/
add_line: "+" /(.*)/ LF -> line

change_move: "*** Move to: " filename LF
change: (change_context | change_line)+ eof_line?
change_context: ("@@" | "@@ " /(.+)/) LF
change_line: ("+" | "-" | " ") /(.*)/ LF
eof_line: "*** End of File" LF
Unlike string-replacement-based diffs, the V4A format relies on contextual anchors to identify edit regions. It also supports file deletions and renames, which our agent previously only supported via the
run_shell_command
tool by invoking
rm
and
mv
.
Supporting
apply_patch
therefore required changes across our entire stack, including both the agent harness and the Warp client. The extra work paid off: we’ve observed more reliable and higher-fidelity file edits, particularly when making larger refactors that span multiple files.
While implementing this tool, we also uncovered an edge case in Codex CLI’s implementation: its V4A patch parser does not correctly handle more than one
change_context
operation in a single patch. We reported this to the Codex team, but it underscored the importance of implementing and validating the format rigorously to support high-precision edits.
Finally, since Warp automatically falls back to alternative models when a selected model is unavailable or errors, we also needed to ensure full interoperability between V4A-based diffs and traditional string-replacement-based editing tools.
Prompting lessons
In addition to tooling changes, supporting Codex required several prompt-level refinements to our agent harness:
Tool renaming for in-distribution alignment: We renamed tools to match names Codex was trained on (e.g.,
grep
→
ripgrep
), improving tool selection accuracy.
Removal of tool preamble prompting: Certain instructional preambles caused Codex models to stall or loop. Removing these prompts led to more stable tool invocation and execution flow.
These changes materially improved reliability and reduced failure rates during long, multi-step coding sessions.
Try it now
GPT-5.1 Codex and GPT-5.1 Codex Max, across all available reasoning levels, are now available in Warp. See the difference in your next coding task.
We’re excited to hear your feedback—what’s working well, what isn’t, and where Codex can push Warp’s agentic workflows even further.
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
