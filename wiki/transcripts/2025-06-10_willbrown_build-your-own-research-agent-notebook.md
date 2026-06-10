---
title: "Build Your Own AI Research Agent — Lightning Lesson (Notebook Walkthrough)"
author: Will Brown
date: 2025-06-10
date_ingested: 2026-06-10
source: https://github.com/willccbb/research-agent-lesson
type: transcript
tags:
  - ai-agents
  - research-agent
  - tool-calling
  - context-engineering
  - deep-research
  - education
  - transcript
related_article: articles/2025-06-10_willbrown_build-your-own-research-agent-lightning.md
participants:
  - Will Brown (instructor)
---

# Build Your Own AI Research Agent — Lightning Lesson (Notebook Walkthrough)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** June 10, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**GitHub:** [research-agent-lesson](https://github.com/willccbb/research-agent-lesson)
**Related summary:** [[raw/articles/2025-06-10_willbrown_build-your-own-research-agent-lightning|Lightning Lesson Summary]]

---

## Overview

This notebook walkthrough accompanies the "Build Your Own AI Research Agent" lightning lesson — a pre-course warm-up for [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering]]. It demonstrates how to build a research agent from scratch using the OpenAI chat completions API, progressing from basic tool calling to a multi-step research loop with web search and synthesis.

---

## Section 1: Setup & Imports

The lesson begins with environment setup using [[concepts/context-engineering|UV]] as the package manager and standard dependencies for agent construction.

```python
# Environment setup
# uv venv && source .venv/bin/activate
# uv pip install openai pydantic tavily-python

import os
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Literal

client = OpenAI()  # Uses OPENAI_API_KEY from environment
```

**Key point:** Every project should have its own virtual environment. UV makes this fast and painless — it's essentially a better pip with ~100x faster installs and better dependency resolution.

---

## Section 2: Defining a Research Query Schema with Pydantic

The first building block is a structured schema for decomposing research queries. Pydantic provides typed, validated outputs that guarantee downstream compatibility.

```python
class ResearchSubQuestion(BaseModel):
    """A decomposed sub-question from a research query."""
    question: str = Field(description="The specific sub-question to investigate")
    search_query: str = Field(description="Optimized search query for this sub-question")
    priority: Literal["high", "medium", "low"] = Field(
        description="Priority level for answering this question"
    )

class ResearchPlan(BaseModel):
    """A structured plan for researching a topic."""
    topic: str = Field(description="The original research topic")
    sub_questions: list[ResearchSubQuestion] = Field(
        description="Decomposed sub-questions, ordered by priority"
    )
    approach: str = Field(description="Brief description of the research approach")
```

**Key insight:** `Literal` types are a very useful primitive for agent applications. They provide guaranteed field validation — you know the output will be one of a fixed set of values, which makes the pipeline robust. Ordering matters: chain-of-thought fields must precede action fields in the schema, because transformers are autoregressive and planning must happen before execution.

---

## Section 3: Research Planning — Decomposing a Query

The planning step breaks a high-level research question into actionable sub-questions with optimized search queries.

```python
def plan_research(topic: str) -> ResearchPlan:
    """Decompose a research topic into a structured plan."""
    response = client.beta.chat.completions.parse(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": (
                "You are a research planning assistant. "
                "Given a research topic, break it into specific sub-questions "
                "that would need to be answered to thoroughly research the topic. "
                "For each sub-question, create an optimized search query."
            )},
            {"role": "user", "content": f"Research topic: {topic}"},
        ],
        response_format=ResearchPlan,
    )
    return response.choices[0].message.parsed

# Example usage
plan = plan_research("What are the latest developments in AI agent frameworks?")
print(f"Research plan for: {plan.topic}")
print(f"Approach: {plan.approach}")
for sq in plan.sub_questions:
    print(f"  [{sq.priority}] {sq.question}")
    print(f"    → search: {sq.search_query}")
```

**Key point:** This uses OpenAI's built-in Pydantic parser (`beta.chat.completions.parse`) to get structured outputs directly. The model doesn't generate free-form text first — its first token is the start of the structured output, constrained to the schema.

---

## Section 4: Tool Calling with Web Search

The research agent needs to actually search the web. This section demonstrates how to define tools in the OpenAI schema format and handle tool call responses.

```python
from tavily import TavilyClient

tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def search_web(query: str, max_results: int = 3) -> list[dict]:
    """Search the web using Tavily API."""
    results = tavily.search(query, max_results=max_results)
    return [
        {"title": r["title"], "url": r["url"], "snippet": r["content"]}
        for r in results["results"]
    ]

# Define the tool schema for the LLM
search_tool = {
    "type": "function",
    "function": {
        "name": "search_web",
        "description": "Search the web for information on a topic. Returns title, URL, and snippet.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to execute"
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of results to return (default: 3)"
                }
            },
            "required": ["query"]
        }
    }
}
```

**Key insight:** Having an OpenAI-compatible API set up — whether or not it's actually OpenAI, or something that just speaks the same protocol — is totally fine. Chat completions is the most portable option: DeepSeek, Gemini, Claude, and most open model providers all support it.

---

## Section 5: The Research Agent Loop

The core of the lesson — a multi-turn agentic loop that thinks, searches, and iterates until it has enough information to synthesize a report.

```python
def run_research_agent(topic: str, max_iterations: int = 5) -> str:
    """Run a research agent that searches and synthesizes findings."""
    plan = plan_research(topic)

    messages = [
        {"role": "system", "content": (
            "You are a research agent. You have access to a web search tool. "
            "Your goal is to thoroughly research the given topic by searching "
            "for information, evaluating what you find, and deciding when you "
            "have enough to write a comprehensive report.\n\n"
            "Always think step by step before calling a tool. "
            "After each search, assess what you've learned and what's still missing. "
            "When you have sufficient information, write a final report with citations."
        )},
        {"role": "user", "content": (
            f"Research the following topic thoroughly:\n\n"
            f"**{plan.topic}**\n\n"
            f"Research plan:\n{plan.approach}\n\n"
            f"Sub-questions to investigate:\n" +
            "\n".join(f"- {sq.question} (search: {sq.search_query})" for sq in plan.sub_questions)
        )},
    ]

    all_sources = []

    for i in range(max_iterations):
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=messages,
            tools=[search_tool],
        )

        message = response.choices[0].message

        # If the model wants to call a tool
        if message.tool_calls:
            messages.append(message)

            for tool_call in message.tool_calls:
                query = tool_call.function.arguments
                # Parse the JSON arguments
                import json
                args = json.loads(query)
                results = search_web(args["query"], args.get("max_results", 3))
                all_sources.extend(results)

                # Return tool results to the model
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(results),
                })
        else:
            # Model has produced a final response (no more tool calls)
            return message.content, all_sources

    # If max iterations reached, ask for final synthesis
    messages.append({
        "role": "user",
        "content": "You've reached the iteration limit. Please synthesize your findings into a final report now."
    })
    final = client.chat.completions.create(model="gpt-4.1", messages=messages)
    return final.choices[0].message.content, all_sources

# Example usage
report, sources = run_research_agent(
    "What are the latest developments in AI agent frameworks?"
)
print(report)
print(f"\n--- Sources ({len(sources)}) ---")
for s in sources:
    print(f"  - {s['title']}: {s['url']}")
```

**Key points:**
- **Think then act pattern:** The system prompt instructs the model to "always think step by step before calling a tool." This is the [[concepts/agentic-rl|ReAct]] pattern — interleaving reasoning and action.
- **State management:** The `messages` list accumulates the full conversation state. Without this, the model is just a language model in a vacuum with no memory of what it already searched.
- **Iteration limit:** A safety valve to prevent infinite loops. After `max_iterations`, the agent is forced to synthesize.
- **Tool results as context:** Each search result is appended as a tool message, giving the model fresh context for its next decision.

---

## Section 6: Structured Output for Intermediate Findings

For more structured research, findings can be captured in typed objects rather than free-form text.

```python
class Finding(BaseModel):
    """A single research finding."""
    claim: str = Field(description="The key claim or finding")
    evidence: str = Field(description="Supporting evidence or data")
    source_url: str = Field(description="URL of the source")
    confidence: Literal["high", "medium", "low"] = Field(
        description="Confidence in this finding"
    )

class ResearchReport(BaseModel):
    """A structured research report."""
    topic: str
    summary: str = Field(description="Executive summary of findings")
    findings: list[Finding] = Field(description="Individual findings with evidence")
    gaps: list[str] = Field(description="Identified knowledge gaps or areas needing further research")
    conclusion: str
```

**Key insight:** Using Pydantic models for intermediate and final outputs ensures that the research agent's results can be consumed programmatically — for example, to feed into an evaluation pipeline or another agent.

---

## Section 7: Helper Models for Bulk Processing

An important pattern for research agents is offloading bulk reading to a cheaper helper model.

```python
def summarize_source(url: str, snippet: str, model: str = "gpt-4.1-mini") -> str:
    """Use a cheap helper model to summarize a source."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Summarize the key points from this source in 2-3 sentences."},
            {"role": "user", "content": f"Source: {url}\nSnippet: {snippet}"},
        ],
    )
    return response.choices[0].message.content
```

**Key point:** It's good to have a go-to smaller, cheaper helper model — a model where you're less worried about burning through tokens. When you want to have a model read 10 websites at a time, it's often best to offload this to a helper model like GPT 4.1 Mini, Gemini Flash, or Haiku. The primary agent model makes the strategic decisions; the helper does the bulk reading.

---

## Key Takeaways

1. **Research agents = planning + tool use + iteration + synthesis** — decompose queries into sub-questions, search iteratively, assess what's missing, and synthesize with citations
2. **Pydantic for structured outputs** — typed schemas guarantee downstream compatibility; `Literal` types for categorical fields
3. **Thinking-first ordering** — chain-of-thought fields must precede action fields (transformers are autoregressive)
4. **Chat completions over Responses API** — portable across providers (OpenAI, DeepSeek, Gemini, Claude)
5. **Multi-turn state is what makes an agent** — without a message list accumulating context, you just have a chatbot
6. **Helper models for bulk processing** — offload reading/summarization to cheaper models; reserve the primary model for strategic decisions
7. **Start with non-reasoner models** — GPT 4.1, DeepSeek V3, Claude Sonnet for primary agents; reasoners add latency and cost that compound in multi-tool loops

---

## Related

- [[raw/articles/2025-06-10_willbrown_build-your-own-research-agent-lightning|Lightning Lesson Summary]]
- [[transcripts/2025-06-17_willbrown_agents-mcp-rl-agent-patterns-lecture|Lesson 1: Agent Patterns & Principles (Lecture)]]
- [[raw/articles/2025-06-17_willbrown_agents-mcp-rl-lesson1|Lesson 1: Agent Patterns & Principles (Summary)]]
- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[entities/will-brown]]
- [[concepts/research-agent-fundamentals|Research Agent Fundamentals]]
- [[concepts/deep-research]]
- [[concepts/context-engineering]]
- [[concepts/agentic-rl]]
