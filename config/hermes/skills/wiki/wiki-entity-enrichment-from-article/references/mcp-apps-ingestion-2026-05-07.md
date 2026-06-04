# MCP Apps Ingestion — Session Reference (2026-05-07)

## Context
Article: "Interactive Connectors and MCP Apps in Claude" (claude.com/blog/interactive-tools-in-claude)
Published: 2026-01-26
Type: Product announcement / extension of existing concept (MCP)

## Decision: Section in Existing Page > New Standalone Page

**Why add to `concepts/mcp.md` instead of creating `concepts/mcp-apps.md`**:
- MCP Apps is an extension of MCP, not a standalone concept — it would be confusing without MCP context
- The MCP page already had the right audience and related-links structure
- Avoids fragmentation: one page to maintain for the entire MCP ecosystem
- The article is relatively thin (list of launch partners + basic technical description) — not enough depth for a standalone concept page

**When to create standalone instead**:
- The sub-topic has its own architecture, design decisions, and tradeoffs independent of the parent
- Multiple independent sources discuss the sub-topic (not just one announcement blog post)
- The parent page would become too long (rule of thumb: if parent page exceeds ~200 lines, consider splitting)

## Workflow Used
1. `search_files` to check if article URL or slug already referenced in wiki (found 0 matches)
2. `search_files` for related concept mentions (MCP Apps, interactive connectors) — found MCP Apps mentioned in `agentic-web.md`, `microsoft-copilot-wave-3.md`, `agentcraft.md`
3. `web_extract` to scrape the article
4. `write_file` raw article to `wiki/raw/articles/2026-01-26_anthropic-interactive-tools-claude.md`
5. `patch` to add "### MCP Apps (Interactive UI Extension)" section to `concepts/mcp.md`:
   - Key Concept description
   - Launch partner table (10 services)
   - Ecosystem adoption (Microsoft Copilot, VS Code)
   - Competition with other UI-over-MCP standards (MCP-UI, OpenAI Apps SDK, Google A2UI)
   - Getting Started instructions
   - Source section with raw article wiki-link
6. Updated frontmatter: tags (+mcp-apps), sources, updated date
7. Added Related Concepts links: agentic-web, mcp-ui entity
8. `patch` log.md with entry, `patch` index.md with `[[concepts/mcp]]` entry
9. `git add/commit/push`

## Competing Standards Identified
- **MCP-UI** by Ido Salomon — independent open-source standard for UI over MCP
- **OpenAI Apps SDK & AgentKit** — OpenAI's approach
- **Google A2UI** — Google's agent-to-user interface standard
