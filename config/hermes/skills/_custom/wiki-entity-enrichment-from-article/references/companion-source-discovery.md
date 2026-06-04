# Companion-Source Discovery for Protocol/Standard Announcements

Use this workflow when the trigger article announces a **protocol, standard, extension, or tool release** — especially from the Anthropic/MCP ecosystem.

## Source Discovery Checklist

| Source Type | What to Look For | How to Find It |
|-------------|-----------------|----------------|
| **Spec/Proposal** | SEP/DEP/design docs | Links in article body, GitHub PRs |
| **Official Release Blog** | "Now available" launch post | Check project's own blog (e.g., blog.modelcontextprotocol.io) |
| **Original Project** | Independent OSS that the standard subsumed | Check article acknowledgments, "inspired by" sections |
| **GitHub Repo** | SDK code, examples, README, license | Search [GitHub](https://github.com) for project name |
| **Competing Standards** | Other approaches to same problem | Check footnotes, related work sections |
| **Client Adoption List** | Which products/IDEs support it | Check release blog post, product docs |

## Example: MCP Apps (from this session)

Trigger article: `https://claude.com/blog/interactive-tools-in-claude` (Jan 26, 2026)

Companion sources discovered:
- **Spec proposal**: [SEP-1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865) (Nov 21, 2025)
- **Official release**: [MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) (Jan 26, 2026)
- **Original project**: [mcpui.dev](https://mcpui.dev) — MCP-UI by Ido Salomon
- **GitHub**: [github.com/idosal/mcp-ui](https://github.com/idosal/mcp-ui)
- **Competing standards**: OpenAI Apps SDK, Google A2UI

## Workflow Steps

1. Read the trigger article and extract all embedded links
2. Check for links to: `github.com/*/pull/*` (spec PRs), `blog.*.io` (companion blogs)
3. Search for the project's official documentation portal
4. Check if the article credits any predecessor projects
5. Build a source inventory (at least 3-5 sources for a protocol/standard topic)
6. Scrape and save ALL sources as raw articles BEFORE building the concept page
7. Write the concept page drawing from the full inventory
