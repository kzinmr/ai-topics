# Wiki CLI — querying the wiki from shell-capable agents

`scripts/wiki` is a **read-only CLI** over the `wiki/` knowledge base — a
shell-native alternative to the [Filesystem / qmd MCP servers](wiki-mcp.md),
aimed at agents that already have a shell (**Claude Code**, Codex) and at humans.

**Why a CLI for Claude Code (vs. an MCP server):**

- **Composes with the agent's existing Bash** — no MCP registration, no Docker,
  no model downloads, no separate process to keep alive.
- **Real full-text search out of the box** via `ripgrep` (the Filesystem MCP only
  globs filenames), plus **metadata filtering** on frontmatter `type` / `tags`.
- **Read-only by construction** — the script only reads; it never writes to `wiki/`.
- **Token-efficient** — returns just the snippets/paths asked for, and emits
  `path:line` locations that are clickable in Claude Code.

Trade-off: a CLI only helps agents that can run shell commands. For MCP-only
clients (e.g. Claude Desktop), use the [MCP servers](wiki-mcp.md) instead. The
CLI and the MCP servers can coexist.

> The wiki is written in **English** — search in English. Page names are
> lowercase-hyphenated English (e.g. `transformer-architecture`).

## Install

The script is stdlib-only Python 3 and uses `ripgrep` (`rg`) if present.

```bash
# Option A: put it on PATH (~/.local/bin is already on PATH here)
ln -s "$PWD/scripts/wiki" ~/.local/bin/wiki
wiki search "context engineering"

# Option B: call it directly
scripts/wiki search "context engineering"
```

Wiki location resolves to the `wiki/` next to the repo, or `$WIKI_PATH` if set.

## Commands

```text
wiki search <query>   Full-text content search (ripgrep) with snippets
wiki find <glob>      Filename search, e.g. 'transformer*'
wiki show <page>      Print a page (resolve by path or fuzzy name)
wiki meta <page>      Print a page's frontmatter only
wiki links <page>     Outbound [[wikilinks]] + inbound backlinks
wiki list             List pages matching metadata filters
wiki index | schema   Print wiki/index.md | wiki/SCHEMA.md
```

**Shared filters / flags:**

- `--type T` (repeatable) — frontmatter `type`: `concept`, `entity`, `comparison`, `event`, `query`.
- `--tag T` (repeatable, AND) — require a frontmatter tag (handles both `tags: [a, b]` and block-list styles).
- `--area concepts|entities|comparisons|events|queries|raw` — restrict to one area (`search`, `list`).
- `--curated` — curated layer only, exclude `raw/` (`search`, `list`).
- `-n N` — max files (`search`, default 15); `--snippets K` — snippet lines per file.
- `--json` — machine-readable output (all query commands) for piping/agents.

## Examples

```bash
# Full-text, curated layer only, top 5 pages
wiki search "programmatic tool calling" --curated -n 5

# Full-text within concept pages tagged both 'tool-use' and 'mcp'
wiki search "code execution" --type concept --tag tool-use --tag mcp

# Find pages by name; list all comparison pages
wiki find "agent-*" --type concept
wiki list --type comparison

# Read a page, inspect its frontmatter, walk its link graph
wiki show programmatic-tool-calling
wiki meta programmatic-tool-calling --json
wiki links programmatic-tool-calling      # outbound [[links]] + backlinks → raw/ citations

# Orient like the llm-wiki SKILL: schema → index → pages
wiki schema | head -60
wiki index
```

## SKILL-aware usage recipe

Same navigation model as the [MCP doc](wiki-mcp.md), expressed in CLI verbs:

1. `wiki schema` — domain, 3-layer model, frontmatter fields, tag taxonomy.
2. `wiki index` — catalog of existing pages.
3. `wiki search <english query> [--type/--tag/--curated]` — find relevant pages.
4. `wiki show <page>` to read, `wiki links <page>` to follow `[[wikilinks]]` and
   `raw/...` citations.

### Priming block for a consuming project

Drop into the consuming project's `CLAUDE.md` so its agents discover the tool:

```markdown
## ai-topics wiki (CLI)
A read-only AI/ML knowledge base is queryable via the `wiki` command (English).
For AI/LLM/agent questions, prefer it over web search:
- `wiki search "<english query>" [--type concept] [--tag <tag>] [--curated]` — full-text search
- `wiki show <page>` / `wiki meta <page>` / `wiki links <page>` — read & navigate
- `wiki schema` then `wiki index` to orient first.
```

Optionally allowlist it so it runs without prompts, e.g. in `.claude/settings.json`:
`"permissions": { "allow": ["Bash(wiki:*)", "Bash(scripts/wiki:*)"] }`.

## Use from Codex

Codex has shell access, so the `wiki` CLI works there too. Codex has no "skills"
mechanism; its always-on instructions live in `AGENTS.md`. The helper sets both up:

```bash
scripts/wiki-codex-setup.sh cli      # add the same priming to ~/.codex/AGENTS.md (idempotent)
scripts/wiki-codex-setup.sh status   # wiki on PATH? AGENTS.md primed? mcp registered?
scripts/wiki-codex-setup.sh remove   # strip the AGENTS.md block (+ any codex mcp entry)
```

`cli` only edits `~/.codex/AGENTS.md` (between managed markers) and checks that
`wiki` is on PATH — the `~/.local/bin/wiki` symlink itself is owned by
`wiki-skill-install.sh`, so run that once first (or `ln -s scripts/wiki ~/.local/bin/wiki`).
A project-local `AGENTS.md` works the same way if you only want it in one repo.

Prefer the MCP route on Codex? See [wiki-mcp.md → Use from Codex](wiki-mcp.md#use-from-codex).

## Access-method comparison

| | Wiki CLI (`scripts/wiki`) | Filesystem MCP | qmd MCP |
| --- | --- | --- | --- |
| Best for | Claude Code / Codex (shell) | any MCP client | any MCP client |
| Full-text search | ✅ ripgrep | ❌ filename glob only | ✅ BM25 + semantic |
| Metadata filter (type/tag) | ✅ | ❌ | ❌ |
| Setup | symlink | Docker `ro` mount | npm + ~1.8 GB models |
| Read-only | ✅ by design | ✅ via `ro` mount | ✅ (separate index) |
| Docs | this file | [wiki-mcp.md](wiki-mcp.md) | [wiki-mcp-qmd.md](wiki-mcp-qmd.md) |
