---
title: "Code Execution with MCP — Treating MCP Servers as Code APIs"
tags:
  - concept
  - coding-agents
  - mcp
  - anthropic
  - tool
  - progressive-disclosure
  - harness-engineering
  - sandbox
created: 2026-04-25
updated: 2026-05-01
type: concept
aliases:
  - code-execution-with-mcp
  - mcp-as-code-api
  - filesystem-mcp
sources:
  - https://www.anthropic.com/engineering/code-execution-with-mcp
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
  - raw/articles/2026-04-30_cloudflare-code-mode-mcp.md
status: complete
---

# Code Execution with MCP — Treating MCP Servers as Code APIs

## Definition

Code Execution with MCP is the **architectural pattern** where MCP servers are treated as code APIs rather than raw tool collections. Instead of loading all tool definitions into the context (traditional approach), agents navigate a **filesystem of TypeScript/Python wrappers**, load only what they need (progressive disclosure), and write code that calls MCP tools as async functions within a sandboxed execution environment.

**Coined by:** Anthropic Engineering (Nov 2025)
**Also known as:** MCP as Code API, Filesystem-MCP, Code Execution Pattern

## Positioning in the Hierarchy

```
Programmatic Tool Calling (API mechanism — allowed_callers, code_execution_20260120)
    └── Code Execution with MCP (Architectural pattern — MCP as code API) ★ このページ
            └── CodeMode (Specific implementations — Cloudflare MCP, Pydantic Monty)
```

| Layer | Scope | What It Provides |
|-------|-------|-----------------|
| [[concepts/programmatic-tool-calling]] | API mechanism | `allowed_callers`, `code_execution_20260120` tool, sandboxed container |
| **Code Execution with MCP** | **Architectural pattern** | **Filesystem tool discovery, progressive disclosure, PII tokenization, skills** |
| [[concepts/code-mode]] | Concrete implementations | Cloudflare V8 (JS, server-side), Pydantic Monty (Python, in-process) |

## The Problem: Token Overload

As agents scale to hundreds of MCP tools, two patterns drive cost:

### 1. Tool Definition Overload
Loading all tool schemas upfront means the model processes thousands of tokens before even reading the user request.

### 2. Intermediate Result Bloat
Every intermediate result passes through the model's context window:

> Google Drive → transcript (50K tokens) → model reads it → Salesforce → model sends it again (50K tokens) = **100K tokens wasted**

## The Solution: MCP as a Filesystem

Instead of a flat list of tools, MCP tools are organized as a **directory of TypeScript/Python files**:

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput { documentId: string; }
interface GetDocumentResponse { content: string; }

/* Read a document from Google Drive */
export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
}
```

The agent navigates this filesystem (using standard tools like `ls`, `cat`), loading only the `.ts` files relevant to the task.

### Example Workflow

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

## Key Benefits

| Benefit | Mechanism | Impact |
|---------|-----------|--------|
| **Progressive Disclosure** | Agent navigates filesystem; loads only needed definitions | Eliminates upfront context bloat |
| **Context-Efficient Results** | Data filtered/aggregated in sandbox before returning to model | 10K rows → 5 rows |
| **Native Control Flow** | Loops, conditionals replace chained tool calls | Fewer round trips |
| **Privacy-Preserving** | MCP client tokenizes PII before it reaches the model | `[EMAIL_1]` instead of raw data |
| **State & Skills** | `./workspace/` for state, `./skills/` for reusable code | Agent accumulates capabilities |

### Progressive Disclosure in Detail

The agent can request different detail levels:
- **Name only**: List available tool files
- **Summary**: Read docstrings (first lines)
- **Full schema**: Read complete TypeScript definitions

A `search_tools` utility allows semantic search: the agent sends a query string, gets back relevant tool names and file paths.

### Privacy-Preserving Operations

The MCP client automatically tokenizes PII mid-flight:

1. `gdrive.getDocument()` returns data containing emails
2. MCP client intercepts, replaces `user@example.com` → `[EMAIL_1]`, stores mapping
3. Model sees `[EMAIL_1]` in context
4. `salesforce.updateRecord()` uses stored mapping to resolve `[EMAIL_1]` back to actual data
5. **PII never enters model context**

### Skills Persistence

Agents can save reusable code as "Skills" for later use:

```typescript
// Saved to ./skills/saveSheetAsCsv.ts
export async function saveSheetAsCsv(sheetId: string) {
  const data = await gdrive.getSheet({ sheetId });
  const csv = data.map(row => row.join(',')).join('\n');
  await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
  return `./workspace/sheet-${sheetId}.csv`;
}
```

## Comparison with Alternative Approaches

| Dimension | Direct Tool Calling | Code Execution with MCP | CodeMode (Cloudflare) |
|-----------|-------------------|------------------------|----------------------|
| **Tool discovery** | All schemas upfront | Filesystem navigation (progressive) | `search()` on OpenAPI spec |
| **Data handling** | Full results go through model | Filtered in sandbox | Filtered in V8 |
| **Token cost (example)** | 150K tokens | 2K tokens (98.7% saving) | 1K tokens (99.9% saving) |
| **Sandbox** | None (results go to model) | Any (Deno, Python, V8) | Dynamic Worker V8 |
| **Security** | Per-tool permissions | PII tokenization + sandbox | V8 isolate + OAuth 2.1 |

## Relationship to Advanced-Tool-Use

This pattern is part of Anthropic's larger [[concepts/harness-engineering/system-architecture/advanced-tool-use]] framework, which includes:

- Large Tool Use (parallel tool calls)
- Programmatic Tool Calling (this page)
- Tool result caching

## See Also

- [[concepts/programmatic-tool-calling]] — API mechanism enabling this pattern
- [[concepts/code-mode]] — Concrete CodeMode implementations (Cloudflare, Pydantic)
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Deep dive (Japanese, under harness-engineering)
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — Related Anthropic tool patterns
- [[concepts/agentic-search]] — Externalized processing paradigm
