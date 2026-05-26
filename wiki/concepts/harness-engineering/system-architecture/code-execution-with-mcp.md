---
title: "Code Execution with MCP"
type: concept
aliases:
  - code-execution-mcp
  - code-mode
  - mcp-code-execution
  - filesystem-tool-discovery
created: 2026-04-12
updated: 2026-05-01
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - mcp
  - coding-agents
status: draft
sources:
  - "https://www.anthropic.com/engineering/code-execution-with-mcp"
---
# Code Execution with MCP

MCP (Model Context Protocol) servers exposed as a code API — a pattern where agents write code and call tools. Same core insight as Cloudflare's "Code Mode."

## Core Insight

> "The core insight is the same: LLMs are adept at writing code and developers should take advantage of this strength to build agents that interact with MCP servers more efficiently."

**LLMs are good at writing code. This strength should be leveraged to streamline interactions with MCP servers.**

## Problem: Context Overload from Direct Tool Calling

When agents scale to tens/hundreds of MCP servers:
- **Tool definition bloat**: Pre-loading all tool schemas consumes enormous context before request processing
- **Token waste on intermediate results**: Raw output (transcripts, large datasets) passes through the model context multiple times
  - Example: Processing a 2-hour sales meeting transcript twice = **~50,000 additional tokens**

## Solution: Expose MCP as a Code API

Expose MCP servers as a structured filesystem. Agents write code to orchestrate tools and load definitions on demand.

### Implementation Architecture

```
servers
├── google-drive
│   ├── getDocument.ts
│   └── index.ts
├── salesforce
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

**Tool definition example:**
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

**Agent workflow example:**
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

## Benefits

| Benefit | Mechanism | Impact |
|:---|:---|:---|
| **Progressive disclosure** | Agent navigates filesystem or loads only needed definitions via `search_tools` | Eliminates upfront context bloat |
| **Context-efficient results** | Data filtered/transformed in execution environment before returning to model | 10,000-row sheet -> return only 5 rows |
| **Powerful control flow** | Native loops, conditionals, error handling replace chained tool calls | Reduces "time to first token" latency. Clean polling/retry handling |
| **Privacy protection** | Intermediate data stays in execution environment. MCP client auto-tokenizes PII | Sensitive data flows safely without entering context |
| **State persistence and skills** | Intermediate results saved to files. Reusable code persisted as `./skills/` + `SKILL.md` | Workflow resumption and cumulative agent capability growth |

## Trade-offs

- **Infrastructure overhead**: Requires secure execution environment (sandboxing, resource limits, monitoring)
- **Complexity vs direct calling**: Higher operational burden than simple tool routing
- **Recommendation**: Compare token/latency reduction against implementation cost. Best for large datasets, complex workflows, strict privacy requirements

## Key Metrics

| Metric | Value |
|---|---|
| **Token reduction** | `150,000 -> 2,000 tokens` (**98.7% savings**) |
| **MCP adoption** | Launched November 2024. Industry de facto standard. Thousands of community servers |
| **Industry validation** | Cloudflare's "Code Mode" demonstrates identical efficiency improvements |

## Practical Recommendations

1. **Shift from direct tool calling to code execution**: When scaling beyond dozens of MCP servers
2. **Filesystem-based tool discovery**: Progressive context loading via `search_tools`
3. **Filter/aggregate data in code**: Before returning to the model
4. **MCP client tokenization pipeline**: Leverage in PII-heavy workflows
5. **Save reusable logic as skills**: `SKILL.md` + code. Cumulative agent capability over time
6. **Invest in secure sandboxes**: Safely execute agent-generated code

## Related Concepts

- [[concepts/programmatic-tool-calling]] — Higher-level concept: LLM writes code to call tools via API mechanism. Code Execution with MCP is the MCP implementation of this pattern
- [[concepts/code-execution-with-mcp]] — Higher-level (root): Architecture pattern treating MCP as a code API
- [[concepts/code-mode]] — Concrete implementations: Cloudflare Code Mode (V8 MCP), Pydantic Monty
- [[concepts/harness-engineering]] — Parent index
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — Advanced tool use (related to PTC)
- [[concepts/harness-engineering/system-architecture/writing-tools-for-agents]] — Tool design for agents
- [[concepts/harness-engineering/system-architecture/building-effective-agents]] — Fundamentals of building agents
