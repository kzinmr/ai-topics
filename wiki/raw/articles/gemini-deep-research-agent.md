# Gemini Deep Research Agent

- **Source:** https://ai.google.dev/gemini-api/docs/deep-research
- **Author:** Google
- **Date:** 2026-04 (preview update)
- **Domain:** ai-agents, research-agents, google-ai
- **Tags:** agent, research, preview, google, mcp

## Summary

Google released **Gemini Deep Research Agent** in preview — an autonomous research agent that plans, executes, and synthesizes multi-step research tasks. Powered by Gemini, it navigates complex information landscapes to produce detailed, cited reports. The latest preview adds collaborative planning, visualization support, MCP integration, and document input.

## Capabilities

- **Autonomous multi-step research:** Plans, executes search/reading loops, synthesizes cited reports
- **Collaborative Planning:** Review and refine research plan before execution (multi-turn interactions)
- **MCP Support:** Connect to external tools via MCP servers
- **Visualizations:** Include charts and graphs in output
- **Document Input:** Provide documents directly as input
- **Two Versions:**
  - **Deep Research** (`deep-research-preview-04-2026`): Speed and efficiency, streamable to client UI
  - **Deep Research Max** (`deep-research-max-preview-04-2026`): Maximum comprehensiveness

## API Design

- Exclusively available via **Interactions API** (not `generate_content`)
- Must use background execution (`background=true`) — tasks take several minutes
- Async pattern: create interaction → poll for status → retrieve outputs

### Example (Python)
```python
import time
from google import genai
client = genai.Client()
interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True
)
# Poll until status == "completed"
```

### Collaborative Planning
Set `collaborative_planning=True` — agent returns a research plan instead of executing immediately. User can review, modify, or approve through multi-turn interactions.

## Why This Matters

Gemini Deep Research represents Google's entry into the autonomous research agent space, competing with tools like Perplexity and OpenAI's research capabilities. The MCP integration is particularly interesting — it means Deep Research can be extended with custom tools and data sources. The collaborative planning feature adds a human-in-the-loop control layer that addresses the "black box research" problem.
