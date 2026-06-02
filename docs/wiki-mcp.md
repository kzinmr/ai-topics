# Wiki MCP — querying the wiki from agents

Publish the `wiki/` knowledge base as a **read-only local MCP server** so any
agent (Claude Code, Claude Desktop, …) can browse and read it, the way
[DeepWiki](https://deepwiki.com/) or codewiki expose a corpus — but entirely on
your machine and pointed at this repo's `wiki/`.

> **Shell-capable agent (Claude Code, Codex)?** A read-only `wiki` **CLI** is often
> the better fit — it composes with the agent's Bash, does real full-text search
> via ripgrep, and supports metadata filtering, with no Docker/registration. See
> [wiki-cli.md](wiki-cli.md). MCP and CLI can coexist.

This is the **phase 1** publication: direct filesystem access via the official
[Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem).
It matches the [Karpathy LLM-Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
model the wiki is built on — agents **navigate the markdown directly** rather
than hitting a search index. Full-text search and metadata filtering are
deferred to a later MCP (see [Roadmap](#roadmap)).

## Architecture

```
wiki/ (hermes-maintained, immutable)
  │   read-only bind mount (Docker `,ro`)
  ▼
Docker: mcp/filesystem  ──stdio JSON-RPC──►  Claude Code / any MCP client / agent
  ├─ index.md     catalog — entry point, read this first
  ├─ SCHEMA.md    3-layer model, frontmatter, tag taxonomy (the "skill" knowledge)
  ├─ concepts/ entities/ events/ comparisons/ queries/   Layer 2 (curated pages)
  └─ raw/         Layer 1 (original sources — articles, papers, newsletters)
```

**Why Docker + `ro`:** the Filesystem MCP server has no native read-only mode and
exposes write/edit/move/create tools alongside read tools. Mounting `wiki/` with
the Docker `ro` flag makes writes fail at the filesystem level (`EROFS`), so a
query agent can never modify this hermes-maintained wiki. Verified: `write_file`
returns `isError: true → EROFS: read-only file system`.

## Setup

The helper script wraps every step (`scripts/wiki-mcp-filesystem.sh`):

```bash
scripts/wiki-mcp-filesystem.sh pull     # docker pull mcp/filesystem
scripts/wiki-mcp-filesystem.sh smoke     # handshake + read works + write is rejected
scripts/wiki-mcp-filesystem.sh config    # print the registration JSON
scripts/wiki-mcp-filesystem.sh           # all of the above
```

If `docker pull mcp/filesystem` is unavailable, build it from source:

```bash
git clone https://github.com/modelcontextprotocol/servers
docker build -t mcp/filesystem servers/src/filesystem
```

### Register with Claude Code

User-level (`~/.claude/settings.json`) or a project `.mcp.json`:

```json
{
  "mcpServers": {
    "ai-topics-wiki": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "--mount", "type=bind,src=${HOME}/ai-topics/wiki,dst=/wiki,ro",
        "mcp/filesystem", "/wiki"
      ]
    }
  }
}
```

Or via the CLI:

```bash
claude mcp add ai-topics-wiki -- docker run -i --rm \
  --mount type=bind,src=${HOME}/ai-topics/wiki,dst=/wiki,ro \
  mcp/filesystem /wiki
```

Verify with `claude mcp list`. The container starts on demand per session
(`--rm` cleans it up); no daemon to manage.

### Use from Codex

Codex CLI registers MCP servers via `codex mcp add` (writes `~/.codex/config.toml`):

```bash
scripts/wiki-codex-setup.sh mcp          # read-only Filesystem MCP (this doc)
scripts/wiki-codex-setup.sh mcp --qmd    # qmd full-text/semantic MCP (see wiki-mcp-qmd.md)
# equivalent manual form:
codex mcp add ai-topics-wiki -- docker run -i --rm \
  --mount type=bind,src=$HOME/ai-topics/wiki,dst=/wiki,ro mcp/filesystem /wiki
```

`codex mcp list` to verify, `scripts/wiki-codex-setup.sh remove` to undo. On Codex,
the lighter [CLI route](wiki-cli.md#use-from-codex) (shell + `AGENTS.md` priming) is
often enough; MCP is for parity with non-shell tooling. Run the setup from the
canonical `~/ai-topics` clone so the mounted path is stable.

## Exposed tools (image `mcp/filesystem`, `secure-filesystem-server` v0.2.0)

| Tool | Use |
| --- | --- |
| `read_file` | Read one file's full text (e.g. `/wiki/concepts/foo.md`). |
| `read_multiple_files` | Read several files at once — good for resolving many `[[wikilinks]]`. |
| `list_directory` | List a directory's entries (`[FILE]`/`[DIR]`). |
| `directory_tree` | Recursive JSON tree of a subtree. |
| `search_files` | **Filename / path glob only — NOT full-text content search.** |
| `get_file_info` | File metadata (size, mtime, …). |
| `list_allowed_directories` | Show the mounted root (`/wiki`). |
| `write_file` `edit_file` `move_file` `create_directory` | Present but **fail under `ro`** — do not use. |

## How an agent should navigate (SKILL-aware recipe)

The Filesystem MCP server is generic — it cannot carry per-directory meaning.
The wiki, however, **describes itself**: `SCHEMA.md` and `index.md` sit at the
mounted root. A consuming agent becomes "llm-wiki aware" simply by reading them
first. The wiki itself is never modified to support this.

Recommended access pattern:

1. `read_file /wiki/SCHEMA.md` — domain, the 3-layer model, frontmatter fields, tag taxonomy.
2. `read_file /wiki/index.md` — sectioned catalog of every existing page with one-line summaries.
3. `search_files` (filename glob, e.g. `*programmatic-tool*`) to locate candidate pages, then `read_file` them.
4. Follow `[[wikilinks]]` and `raw/...` citations inside a page with `read_file` / `read_multiple_files`.

Directory roles:

| Path | Role |
| --- | --- |
| `index.md` | Catalog / entry point. |
| `SCHEMA.md` | Conventions: layers, frontmatter, tag taxonomy. |
| `log.md`, `log-*.md` | Chronological action log. |
| `concepts/` | Concept & topic pages (Layer 2). |
| `entities/` | People, orgs, products, models (Layer 2). |
| `comparisons/` | Side-by-side analyses (Layer 2). |
| `events/`, `queries/` | Timeline events; filed query results (Layer 2). |
| `raw/` | Immutable source material cited by Layer 2 (`articles/`, `papers/`, `newsletters/`). |

**The wiki is written in English.** Issue search globs and reason about content
**in English** — page names are lowercase-hyphenated English (e.g.
`transformer-architecture.md`).

### Priming block for a consuming project

Since a stock MCP server can't inject instructions, drop this into the consuming
project's `CLAUDE.md` (or a small skill) so its agents use the wiki well:

```markdown
## ai-topics-wiki MCP
A read-only filesystem MCP over an AI/ML knowledge base at `/wiki` (English).
When answering AI/LLM/agent questions, consult it:
1. Read `/wiki/SCHEMA.md` then `/wiki/index.md` to orient.
2. Locate pages with `search_files` (filename glob, English) and `read_file` them.
3. Follow `[[wikilinks]]` and `raw/...` citations.
`search_files` matches filenames only (no full-text search yet); the wiki is read-only.
```

## Limitations

- **No full-text search.** `search_files` matches filenames/paths, not content.
  Use `index.md` as the discovery layer; descriptive filenames make globbing useful.
- **No metadata filtering.** Frontmatter (`type`, `tags`, dates) is readable but
  not queryable as structured filters.
- **English only** by assumption.

## Roadmap

- **Full-text + semantic search MCP** (additive, separate server): index `wiki/`
  with [qmd](https://github.com/tobi/qmd) (SQLite FTS5 BM25 + optional local vector
  search) — `qmd` ships its own `qmd mcp` server. **Step-by-step setup:
  [wiki-mcp-qmd.md](wiki-mcp-qmd.md).** A pure-Python alternative is
  [bm25s](https://github.com/xhluca/bm25s) + pandas (lexical search with structured
  frontmatter filtering, no Node/model download).
- **Schema-aware custom MCP:** a thin server that bakes the llm-wiki schema into
  its MCP `instructions` and curated tool descriptions (e.g. `read_page`,
  `list_by_type`, `resolve_wikilink`), and can enforce a "query in English" hint
  the generic filesystem server cannot.
