# GitHub PR as Development History Source

When the user provides a GitHub PR alongside a blog post or docs page about a technology, treat the PR as a **primary development history source**. PRs often contain structural truth that polished blog posts gloss over.

## When to Apply

This pattern fires when:
- User says "このPRの内容も開発経緯として理解して" (understand this PR as development history)
- A blog post mentions a PR number but doesn't detail it
- User provides a PR URL explicitly as context for understanding how something evolved

## What to Extract from a PR

### 1. Structural Changes (the diff tells the real story)
- **File moves/renames**: reveals when components were separated. e.g., PR #4471 moved app-server logic from `codex-rs/mcp-server/` to `codex-rs/app-server/` — this IS the birth of app-server as a distinct entity.
- **Size of change**: +1525/-414 across 49 files signals whether this was a refactor or a greenfield split.
- **New crates/modules introduced**: shared utilities, new protocol types.

### 2. Backward Compatibility Breaks
PR descriptions often note them explicitly — e.g., "non-backwards-compatible change." These are gold for understanding protocol versioning. Note what broke and why:
- New enum variants that old clients won't recognize
- Changed handshake sequences
- Deprecated methods replaced by typed alternatives

### 3. Discussion Comments Reveal Design Intent
Reviewer comments often capture the rationale that blog posts omit:
- `"Since we already have codex mcp, should this be codex mcp start-server?"` → rejected because "managing MCPs vs. running Codex as an MCP server are different concerns"
- `"LGTM"` alone is less useful than comments explaining WHY a split was necessary
- Look for comments about code duplication being intentional ("expected to diverge later")

### 4. Follow-up Plans
PRs often list mechanical renames or cleanup planned for subsequent PRs. These show what was considered but deferred:
- `"Mechanical renames (e.g., McpProcess → AppServer) in subsequent PRs"`
- `"Real pagination will come later by leveraging SQLite"`

## How to Integrate into a Wiki Page

### Add a "Development History" Section
Structure it as chronological phases with source attribution:

```markdown
## Development History

### Phase 1: Internal Harness Reuse (date)
Context from blog post...

### Phase 2: The MCP Split — PR [#NNNN](url) (date)
Structural details from the PR:
- What was split
- What broke backward compatibility
- Key reviewer comments
- Follow-up planned

### Phase 3: Platform Stabilization (date)
...
```

### Include a Before/After Table
When a PR splits or renames commands, a visual table is more scannable than prose:

| Before | After |
|--------|-------|
| `codex mcp serve` (everything) | `codex mcp-server` — pure MCP |
| | `codex app-server` — application server |

### Quote the PR Directly
PR descriptions and reviewer comments have authority. Quote them with blockquotes and attribution.

## Source Attribution

Always cite the PR in the page's frontmatter `sources:` list alongside the blog post:

```yaml
sources:
  - raw/articles/2026-02-04_openai-unlocking-the-codex-harness.md
  - https://github.com/openai/codex/pull/4471
```

## Pitfalls

- **Don't treat the PR as just a link.** The diff, discussion, and follow-up notes contain information the blog post doesn't. Extract them.
- **Don't trust the PR title alone.** "fix: separate codex mcp into..." sounds minor. The +1525/-414 diff tells the real story.
- **Copypasta is intentional, not sloppy.** When a PR duplicates files between crates (`message_processor.rs` in both `mcp-server/` and `app-server/`), this is often a deliberate "diverge later" pattern — note it, don't criticize it.
