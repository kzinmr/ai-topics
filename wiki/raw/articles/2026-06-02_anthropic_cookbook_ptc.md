---
title: "Programmatic Tool Calling (PTC) with the Claude API"
url: https://platform.claude.com/cookbook/tool-use-programmatic-tool-calling-ptc
date: 2026-06-02
source: Anthropic Claude Platform Cookbook
author: Pedram Navid (@PedramNavid)
published: 2025-11-24
---

# Programmatic Tool Calling (PTC) with the Claude API

Programmatic Tool Calling (PTC) allows Claude to write code that calls tools programmatically within the Code Execution environment, rather than requiring round-trips through the model for each tool invocation. This substantially reduces end-to-end latency for multiple tool calls, and can dramatically reduce token consumption by allowing the model to write code that removes irrelevant context before it hits the model's context window (for example, by grepping for key information within large and noisy files).

When faced with third-party APIs and tools that you may not be able to modify directly, PTC can help reduce usage of context by allowing Claude to write code that can be invoked in the Code Execution environment.

In this cookbook, we will work with a mock API for team expense management. The API is designed to require multiple invocations and will return large results which help illustrate the benefits of Programmatic Tool Calling.

## By the end of this cookbook, you'll be able to:

- Understand the difference between regular tool calling and programmatic tool calling (PTC)
- Write agents that leverage PTC

## Prerequisites

### Required Knowledge

- Python fundamentals - comfortable with async/await, functions, and basic data structures
- Basic understanding of agentic patterns and tool calling

### Required Tools

- Python 3.11 or higher
- Anthropic API key
- Anthropic Python SDK >= 0.72

## Setup

First, install the required dependencies:

```python
# %pip install -r requirements.txt
```

Note: Ensure your .env file contains:

```
ANTHROPIC_API_KEY=***
```

Load your environment variables and configure the client. We also load a helper utility to visualize Claude message responses.

```python
from dotenv import load_dotenv
from utils.visualize import visualize

load_dotenv()

MODEL = "claude-sonnet-4-6"

viz = visualize(auto_show=True)
```

## Understanding the Third-Party API

In `utils/team_expense_api.py`, there are three functions defined: `get_team_members`, `get_expenses`, and `get_custom_budget`. The `get_team_members` function allows us to retrieve all employees in a given department with their role, level, and contact information. The `get_expenses` function returns all expense line items for an employee in a specific quarter—this can be several hundred records per employee, with each record containing extensive metadata including receipt URLs, approval chains, merchant details, and more. The `get_custom_budget` function checks if a specific employee has a custom travel budget exception (otherwise they use the standard $5,000 quarterly limit).

In this scenario, we need to analyze team expenses and identify which employees have exceeded their budgets. Traditionally, we might manually pull expense reports for each person, sum up their expenses by category, compare against budget limits (checking for custom budget exceptions), and compile a report. Instead, we will ask Claude to perform this analysis for us, using the available tools to retrieve team data, fetch potentially hundreds of expense line items with rich metadata, and determine who has gone over budget.

The key challenge here is that each employee may have 100+ expense line items that need to be fetched, parsed, and aggregated—and the `get_custom_budget` tool can only be called after analyzing expenses to see if someone exceeded the standard budget. This creates a sequential dependency chain that makes this an ideal use case for demonstrating the benefits of Programmatic Tool Calling.

We'll pass our tool definitions to the messages API and ask Claude to perform the analysis. Read the docs on implementing tool use if you are not familiar with how tool use works with Claude's API.

```python
import json

import anthropic
from utils.team_expense_api import get_custom_budget, get_expenses, get_team_members

client = anthropic.Anthropic()

# Tool definitions for the team expense API
tools = [
    {
        "name": "get_team_members",
        "description": 'Returns a list of team members for a given department...',
        "input_schema": {
            "type": "object",
            "properties": {
                "department": {
                    "type": "string",
                    "description": "The department name. Case-insensitive.",
                }
            },
            "required": ["department"],
        },
    },
    {
        "name": "get_expenses",
        "description": "Returns all expense line items for a given employee in a specific quarter...",
        "input_schema": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "The unique employee identifier",
                },
                "quarter": {
                    "type": "string",
                    "description": "Quarter identifier: 'Q1', 'Q2', 'Q3', or 'Q4'",
                },
            },
            "required": ["employee_id", "quarter"],
        },
    },
    {
        "name": "get_custom_budget",
        "description": "Get the custom quarterly travel budget for a specific employee...",
        "input_schema": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The unique employee identifier",
                }
            },
            "required": ["user_id"],
        },
    },
]

tool_functions = {
    "get_team_members": get_team_members,
    "get_expenses": get_expenses,
    "get_custom_budget": get_custom_budget,
}
```

## Traditional Tool Calling (Baseline)

In this first example, we'll use traditional tool calling to establish our baseline.

We'll call the `messages.create` API with our initial query. When the model stops with a `tool_use` reason, we will execute the tool as requested, and then add the output from the tool to the messages and call the model again.

```python
import time

from anthropic.types import TextBlock, ToolUseBlock
from anthropic.types.beta import BetaMessageParam as MessageParam, BetaTextBlock, BetaToolUseBlock

messages: list[MessageParam] = []


def run_agent_without_ptc(user_message):
    """Run agent using traditional tool calling"""
    messages.append({"role": "user", "content": user_message})
    total_tokens = 0
    start_time = time.time()
    api_counter = 0

    while True:
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=4000,
            tools=tools,
            messages=messages,
            betas=["advanced-tool-use-2025-11-20"],
        )
        api_counter += 1
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        viz.capture(response)

        if response.stop_reason == "end_turn":
            final_response = next(
                (block.text for block in response.content if isinstance(block, (BetaTextBlock, TextBlock))),
                None,
            )
            elapsed_time = time.time() - start_time
            return final_response, messages, total_tokens, elapsed_time, api_counter

        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if isinstance(block, (BetaToolUseBlock, ToolUseBlock)):
                    tool_name = block.name
                    tool_input = block.input
                    tool_use_id = block.id
                    result = tool_functions[tool_name](**tool_input)
                    content = str(result)
                    tool_result = {
                        "type": "tool_result",
                        "tool_use_id": tool_use_id,
                        "content": content,
                    }
                    tool_results.append(tool_result)
            messages.append({"role": "user", "content": tool_results})
        else:
            elapsed_time = time.time() - start_time
            final_response = next(
                (block.text for block in response.content if isinstance(block, (BetaTextBlock, TextBlock))),
                f"Stopped with reason: {response.stop_reason}",
            )
            return final_response, messages, total_tokens, elapsed_time, api_counter
```

Our initial query:

```python
query = "Which engineering team members exceeded their Q3 travel budget? Standard quarterly travel budget is $5,000. However, some employees have custom budget limits. For anyone who exceeded the $5,000 standard budget, check if they have a custom budget exception. If they do, use that custom limit instead to determine if they truly exceeded their budget."
```

Running the traditional agent results in multiple API round-trips:
- **API calls: 4**
- **Total tokens: 110,473**
- **Elapsed time: 35.38s**

## PTC Agent

With PTC, Claude writes code that calls tools programmatically within the Code Execution environment.

```python
def run_agent_with_ptc(user_message):
    """Run agent using programmatic tool calling"""
    messages_ptc: list[MessageParam] = [{"role": "user", "content": user_message}]
    total_tokens = 0
    start_time = time.time()

    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=4000,
        tools=tools,
        messages=messages_ptc,
        betas=["code-execution-2025-05-14", "advanced-tool-use-2025-11-20"],
    )

    total_tokens += response.usage.input_tokens + response.usage.output_tokens
    messages_ptc.append({"role": "assistant", "content": response.content})

    # PTC loop - Claude writes code that calls tools in the code execution environment
    while response.stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if isinstance(block, BetaToolUseBlock):
                if block.name == "server_tool_use":
                    # Code execution tool call
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": execute_code(block.input),
                    })
                else:
                    result = tool_functions[block.name](**block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result),
                    })

        messages_ptc.append({"role": "user", "content": tool_results})
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=4000,
            tools=tools,
            messages=messages_ptc,
            betas=["code-execution-2025-05-14", "advanced-tool-use-2025-11-20"],
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        messages_ptc.append({"role": "assistant", "content": response.content})

    elapsed_time = time.time() - start_time
    final_response = next(
        (block.text for block in response.content if isinstance(block, BetaTextBlock)),
        None,
    )
    return final_response, messages_ptc, total_tokens, elapsed_time
```

PTC results:
- **API calls: 3**
- **Total tokens: 15,919**
- **Elapsed time: 34.88s**

## Performance Comparison

| Metric | Traditional | PTC |
|---|---|---|
| API Calls | 4 | 4 |
| Total Tokens | 110,473 | 15,919 |
| Elapsed Time (s) | 35.38 | 34.88 |
| Token Reduction | - | 85.6% |
| Time Reduction | - | 1.4% |

Note on API Call Count: You may notice that PTC requires more API calls in this example. This is because PTC writes more structured, sequential code that follows best practices—for instance, separating the expense fetching step from the budget checking step. Traditional tool calling can sometimes batch operations together in a single turn, but at the cost of sending all raw data through the model's context. The token efficiency gains from PTC far outweigh the minimal increase in round trips, especially when working with large, metadata-rich datasets.

## Key Takeaways

### 1. Context Preservation Through Large Data Parsing

This was the primary benefit demonstrated in our workflow. Claude wrote code to fetch and process hundreds of expense line items within the code execution environment. By processing this data programmatically, Claude parsed JSON, filtered by status, summed amounts by category, and compared against budget limits—all without sending the raw expense data and metadata through the model's context window. This resulted in a significant reduction in token usage.

### 2. Sequential Dependency Optimization

The API has a sequential dependency: `get_custom_budget(user_id)` which can only be called after analyzing expenses to identify who exceeded the standard $5,000 budget. In traditional tool calling, this requires multiple round trips—fetch team members, fetch expenses for each person, identify those over budget, then check their custom budgets one by one. With PTC, Claude writes code that orchestrates this entire workflow in the code execution environment, making programmatic tool calls in a loop and maintaining state across calls.

### 3. Computational Logic in Code Execution

Rather than requiring the model to mentally track and sum dozens of expenses with complex metadata, Claude delegated the arithmetic and aggregation logic to Python code. This reduced cognitive load on the model, ensured precise calculations, and kept irrelevant metadata (like receipt URLs and merchant locations) out of the model's context entirely.

## When to Use PTC

PTC is most beneficial when:

- Working with large, metadata-rich datasets that need filtering, parsing, or aggregation (like our expense analysis with receipt URLs, approval chains, merchant details, etc.)
- Sequential dependencies exist where one tool call depends on the results of previous calls (like checking custom budgets only for employees who exceeded standard limits)
- Multiple tool calls are needed in sequence or in loops across similar entities (checking expenses and budgets for each team member)
- Computational logic can reduce what needs to flow through the model's context
- Tools are safe for programmatic/repeated execution without human oversight

## Conclusion

Our team expense analysis demonstrated PTC's strengths: dramatically reducing context consumption when working with large, metadata-rich datasets and optimizing workflows with sequential dependencies. By allowing Claude to write code that orchestrates tool calls and processes results programmatically, we achieved substantial token savings while maintaining accuracy and insight quality.

PTC is particularly valuable for workflows involving bulk data processing with rich metadata, repeated tool invocations with dependencies, or scenarios where raw tool outputs would otherwise pollute the model's context.

## Next Steps

Try adapting this pattern to your own use cases:

- Financial data analysis and reporting with sequential lookups
- Multi-entity health checks that depend on initial scan results
- Large file processing with metadata (CSV, JSON, XML parsing)
- Database query result aggregation with follow-up queries
- Batch API operations with conditional logic based on initial results
