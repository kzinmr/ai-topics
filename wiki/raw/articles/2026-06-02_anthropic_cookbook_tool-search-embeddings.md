---
title: "Tool Search with Embeddings: Scaling Claude to Thousands of Tools"
url: https://platform.claude.com/cookbook/tool-use-tool-search-with-embeddings
date: 2026-06-02
source: Anthropic Claude Platform Cookbook
author: Henry Keetay (@henrykeetay)
published: 2025-11-24
---

# Tool Search with Embeddings: Scaling Claude to Thousands of Tools

Building Claude applications with dozens of specialized tools quickly hits a wall: providing all tool definitions upfront consumes your context window, increases latency and costs, and makes it harder for Claude to find the right tool. Beyond ~100 tools, this approach becomes impractical.

Semantic tool search solves this by treating tools as discoverable resources. Instead of front-loading hundreds of definitions, you give Claude a single `tool_search` tool that returns relevant capabilities on demand, cutting context usage by 90%+ while enabling applications that scale to thousands of tools.

## By the end of this cookbook, you'll be able to:

- Implement client-side tool search to scale Claude applications from dozens to thousands of tools
- Use semantic embeddings to dynamically discover relevant tools based on task context
- Apply this pattern to domain-specific tool libraries (APIs, databases, internal systems)

This pattern is used in production by teams managing large tool ecosystems where context efficiency is critical. While we'll demonstrate with a small set of tools for clarity, the same approach scales seamlessly to libraries with hundreds or thousands of tools.

## Prerequisites

### Required Knowledge

- Python fundamentals - comfortable with functions, dictionaries, and basic data structures
- Basic understanding of Claude tool use - we recommend reading the Tool Use Guide first

### Required Tools

- Python 3.11 or higher
- Anthropic API key

## Setup

First, install the required dependencies:

```python
%pip install --only-binary :all: -q anthropic sentence-transformers numpy python-dotenv
```

Load your environment variables and configure the client:

```python
import json
import random
from datetime import datetime, timedelta
from typing import Any

import anthropic
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

MODEL = "claude-sonnet-4-6"

claude_client = anthropic.Anthropic()

# all-MiniLM-L6-v2 is a lightweight model with 384 dimensional embeddings
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
```

## Define Tool Library

Before we can implement semantic search, we need tools to search through. We'll create a library of 8 tools across two categories: Weather and Finance.

In production applications, you might manage hundreds or thousands of tools across your internal APIs, database operations, or third-party integrations. The semantic search approach scales to these larger libraries without modification—we're using a small set here purely for demonstration clarity.

```python
TOOL_LIBRARY = [
    # Weather Tools
    {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "The unit of temperature"},
            },
            "required": ["location"],
        },
    },
    {
        "name": "get_forecast",
        "description": "Get the weather forecast for multiple days ahead",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state"},
                "days": {"type": "number", "description": "Number of days to forecast (1-10)"},
            },
            "required": ["location", "days"],
        },
    },
    {
        "name": "get_timezone",
        "description": "Get the current timezone and time for a location",
        "input_schema": {
            "type": "object",
            "properties": {"location": {"type": "string", "description": "City name or timezone identifier"}},
            "required": ["location"],
        },
    },
    {
        "name": "get_air_quality",
        "description": "Get current air quality index and pollutant levels for a location",
        "input_schema": {
            "type": "object",
            "properties": {"location": {"type": "string", "description": "City name or coordinates"}},
            "required": ["location"],
        },
    },
    # Finance Tools
    {
        "name": "get_stock_price",
        "description": "Get the current stock price and market data for a given ticker symbol",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {"type": "string", "description": "Stock ticker symbol (e.g., AAPL, GOOGL)"},
                "include_history": {"type": "boolean", "description": "Include historical data"},
            },
            "required": ["ticker"],
        },
    },
    {
        "name": "convert_currency",
        "description": "Convert an amount from one currency to another using current exchange rates",
        "input_schema": {
            "type": "object",
            "properties": {
                "amount": {"type": "number", "description": "Amount to convert"},
                "from_currency": {"type": "string", "description": "Source currency code (e.g., USD)"},
                "to_currency": {"type": "string", "description": "Target currency code (e.g., EUR)"},
            },
            "required": ["amount", "from_currency", "to_currency"],
        },
    },
    {
        "name": "calculate_compound_interest",
        "description": "Calculate compound interest for investments over time",
        "input_schema": {
            "type": "object",
            "properties": {
                "principal": {"type": "number", "description": "Initial investment amount"},
                "rate": {"type": "number", "description": "Annual interest rate (as percentage)"},
                "years": {"type": "number", "description": "Number of years"},
                "frequency": {"type": "string", "enum": ["daily", "monthly", "quarterly", "annually"], "description": "Compounding frequency"},
            },
            "required": ["principal", "rate", "years"],
        },
    },
    {
        "name": "get_market_news",
        "description": "Get recent financial news and market updates for a specific company or sector",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Company name, ticker symbol, or sector"},
                "limit": {"type": "number", "description": "Maximum number of news articles to return"},
            },
            "required": ["query"],
        },
    },
]
```

## Create Tool Embeddings

Semantic search works by comparing the meaning of text, rather than just searching for keywords. To enable this, we need to convert each tool definition into an embedding vector that captures its semantic meaning.

Since our tool definitions are structured JSON objects with names, descriptions, and parameters, we first convert each tool into a human-readable text representation, then generate embedding vectors using SentenceTransformer's `all-MiniLM-L6-v2` model.

We picked this model because it is:
- Lightweight and fast (only 384 dimensions vs 768+ for larger models)
- Runs locally without requiring API calls
- Sufficient for tool search (you can experiment with larger models for better accuracy)

```python
def tool_to_text(tool: dict[str, Any]) -> str:
    """
    Convert a tool definition into a text representation for embedding.
    Combines the tool name, description, and parameter information.
    """
    text_parts = [
        f"Tool: {tool['name']}",
        f"Description: {tool['description']}",
    ]

    if "input_schema" in tool and "properties" in tool["input_schema"]:
        params = tool["input_schema"]["properties"]
        param_descriptions = []
        for param_name, param_info in params.items():
            param_desc = param_info.get("description", "")
            param_type = param_info.get("type", "")
            param_descriptions.append(f"{param_name} ({param_type}): {param_desc}")
        if param_descriptions:
            text_parts.append("Parameters: " + ", ".join(param_descriptions))

    return "\n".join(text_parts)


# Create embeddings for all tools
tool_texts = [tool_to_text(tool) for tool in TOOL_LIBRARY]
tool_embeddings = embedding_model.encode(tool_texts, convert_to_numpy=True)
# Shape: (8, 384) - 8 tools, 384 dimensions per embedding
```

## Implement Tool Search

With our tools embedded as vectors, we can now implement semantic search. If two pieces of text have similar meanings, their embedding vectors will be close together in vector space. We measure this "closeness" using cosine similarity.

The search process:
1. **Embed the query**: Convert Claude's natural language search request into the same vector space as our tools
2. **Calculate similarity**: Compute cosine similarity between the query vector and each tool vector
3. **Rank and return**: Sort tools by similarity score and return the top N matches

```python
def search_tools(query: str, top_k: int = 5) -> list[dict[str, Any]]:
    """
    Search for tools using semantic similarity.

    Args:
        query: Natural language description of what tool is needed
        top_k: Number of top tools to return

    Returns:
        List of tool definitions most relevant to the query
    """
    query_embedding = embedding_model.encode(query, convert_to_numpy=True)

    # SentenceTransformer returns normalized embeddings, so dot product = cosine similarity
    similarities = np.dot(tool_embeddings, query_embedding)

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    results = []
    for idx in top_indices:
        results.append({"tool": TOOL_LIBRARY[idx], "similarity_score": float(similarities[idx])})

    return results


# Test: "I need to check the weather" → get_weather (0.560), get_forecast (0.508), get_air_quality (0.401)
```

## Define the tool_search Tool

Now we'll implement the meta-tool that allows Claude to discover other tools on demand. When Claude needs a capability it doesn't have, it searches for it using this `tool_search` tool, receives the tool definitions in the result, and can use those newly discovered tools immediately.

This is the only tool we provide to Claude initially:

```python
TOOL_SEARCH_DEFINITION = {
    "name": "tool_search",
    "description": "Search for available tools that can help with a task. Returns tool definitions for matching tools. Use this when you need a tool but don't have it available yet.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Natural language description of what kind of tool you need",
            },
            "top_k": {
                "type": "number",
                "description": "Number of tools to return (default: 5)",
            },
        },
        "required": ["query"],
    },
}


def handle_tool_search(query: str, top_k: int = 5) -> list[dict[str, Any]]:
    """
    Handle a tool_search invocation and return tool references.
    Returns a list of tool_reference content blocks for discovered tools.
    """
    results = search_tools(query, top_k=top_k)

    tool_references = [
        {"type": "tool_reference", "tool_name": result["tool"]["name"]} for result in results
    ]

    return tool_references
```

## Implement Conversation Loop

Now let's put it all together! We'll create a conversation loop that handles the complete tool search workflow.

The conversation flow:
1. Claude starts with only the `tool_search` tool available
2. When Claude calls `tool_search`, we run semantic search and return matching tool definitions
3. Claude can then use the discovered tools immediately
4. When Claude calls a discovered tool, we execute it (using mock responses for this demo)
5. The loop continues until Claude has a final answer

```python
def run_tool_search_conversation(user_message: str, max_turns: int = 5) -> None:
    """Run a conversation with Claude using the tool search pattern."""
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        response = claude_client.messages.create(
            model=MODEL,
            max_tokens=1024,
            tools=TOOL_LIBRARY + [TOOL_SEARCH_DEFINITION],
            messages=messages,
            extra_headers={"anthropic-beta": "advanced-tool-use-2025-11-20"},
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            for block in response.content:
                if block.type == "text":
                    print(f"ASSISTANT: {block.text}")
            break

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "text":
                    print(f"ASSISTANT: {block.text}")
                elif block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input
                    tool_use_id = block.id

                    if tool_name == "tool_search":
                        query = tool_input["query"]
                        top_k = tool_input.get("top_k", 5)
                        tool_references = handle_tool_search(query, top_k)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": tool_use_id,
                            "content": tool_references,
                        })
                    else:
                        mock_result = mock_tool_execution(tool_name, tool_input)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": tool_use_id,
                            "content": mock_result,
                        })

            if tool_results:
                messages.append({"role": "user", "content": tool_results})
```

## Example 1: Weather Query

```
USER: What's the weather like in Tokyo?

--- Turn 1 ---
🔧 Tool invocation: get_weather
   Input: {"location": "Tokyo"}
   ✅ Mock result: {"location": "Tokyo", "temperature": 75, "unit": "fahrenheit", "conditions": "partly cloudy", ...}

--- Turn 2 ---
✓ Conversation complete

ASSISTANT: The weather in Tokyo is currently:
- Temperature: 75°F (about 24°C)
- Conditions: Partly cloudy
- Humidity: 61%
- Wind Speed: 9 mph
```

## Example 2: Finance Query

```
USER: If I invest $10,000 at 5% annual interest for 10 years with monthly compounding, how much will I have?

--- Turn 1 ---
🔧 Tool invocation: calculate_compound_interest
   Input: {"principal": 10000, "rate": 5, "years": 10, "frequency": "monthly"}
   ✅ Mock result: {"principal": 10000, "rate": 5, "years": 10, "compounding_frequency": "monthly", "final_amount": 16470.09, "interest_earned": 6470.09}

--- Turn 2 ---
✓ Conversation complete

ASSISTANT: If you invest $10,000 at 5% annual interest for 10 years with monthly compounding, you will have:
Final Amount: $16,470.09
This means you'll earn $6,470.09 in interest over the 10-year period.
```

## Conclusion

In this cookbook, we implemented a client-side tool search system that enables Claude to work with large tool libraries efficiently. We covered:

- **Semantic tool discovery**: Using embeddings to match natural language queries to relevant tools, enabling Claude to find the right capability without seeing all available tools upfront
- **Dynamic tool loading**: Returning tool definitions in tool results using Claude's tool search feature, allowing Claude to discover and immediately use new tools mid-conversation
- **Context optimization**: Reducing initial context from thousands of tokens (19+ tool definitions) to just the single `tool_search` definition, cutting context usage by 90%+

### Applying This to Your Projects

Consider tool search when:
- You have >20 specialized tools and context usage becomes a concern
- Your tool library grows over time and manual curation becomes impractical
- You need to support domain-specific APIs with hundreds of endpoints (database operations, internal microservices, third-party integrations)
- Cost and latency optimization are priorities for your application

### Next Steps

- **Persist embeddings**: Cache embeddings to disk to avoid recomputing on every session
- **Improve search quality**: Experiment with different embedding models (e.g., `all-mpnet-base-v2`) or implement hybrid search combining semantic and keyword matching (BM25)
- **Scale to larger libraries**: Test with hundreds or thousands of tools
- **Add tool metadata**: Include usage statistics, cost information, or reliability scores in your search ranking
- **Implement caching**: Cache frequently used tool definitions to reduce repeated searches

### Further Reading

- Claude Tool Use Guide - Comprehensive guide to building with tools
- SentenceTransformers Documentation - Learn more about embedding models and semantic search
- Tool Search Tool Documentation - Official documentation on the tool search pattern
