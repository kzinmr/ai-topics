# Why Datasette needs an AI assistant
**Source**: https://simonw.substack.com/p/datasette-agent-an-ai-assistant-for
**Author**: Simon Willison
**Date**: 2025-07-08
**Saved**: 2026-06-16

---

I've been thinking a lot about how AI assistants can interact with data tools. I've built a new plugin for Datasette that gives it an AI assistant—an agent that can explore a Datasette instance, write SQL queries against it, and help users answer questions about their data.

## The idea

The core idea is straightforward: Datasette already has a rich introspection API. You can list tables, fetch schemas, and run arbitrary SQL queries through the JSON API. If you give an AI model access to those endpoints, it can autonomously explore a database and answer natural-language questions.

I've been calling this "Datasette Agent"—it's a plugin that hooks into the Datasette interface and gives you a chat-like experience where you can ask questions about your data.

## How it works

Datasette Agent uses tool use (also known as function calling) to interact with Datasette. The agent has access to a set of tools:

- **list_tables**: Lists all tables in the database
- **get_schema**: Returns the schema for a given table
- **execute_sql**: Runs a SQL query and returns the results
- **sample_data**: Returns a few sample rows from a table

When you ask a question, the agent figures out which tools to call, inspects the schema, writes appropriate SQL, and iterates until it has a good answer.

## The model I'm using

I'm currently using Claude (via the Anthropic API) as the backbone for the agent. Claude is excellent at SQL and at reasoning about data, and the tool use API works well for this kind of interactive exploration.

That said, the architecture is model-agnostic. You could swap in GPT-4, Gemini, or a local model. The important thing is that the model supports structured tool use.

## Why this is exciting

There are a few reasons I'm excited about this:

- It lowers the barrier to exploring data. You don't need to know SQL to ask questions of a database.
- It makes Datasette more useful for non-technical users.
- It demonstrates the power of tool use. The agent doesn't need to guess or hallucinate answers—it goes and actually queries the data.
- It builds on existing infrastructure. Datasette's API was already designed to be introspectable.

## The plugin

The plugin itself is called **datasette-llm-agent**. It's open source and available on GitHub. It installs as a standard Datasette plugin and adds a chat interface to the Datasette web UI.

The chat interface lets you type questions, and the agent responds with answers. You can see the SQL it generated, the queries it ran, and the results it got. This transparency is important—I want people to trust the answers and be able to verify them.

## Challenges

- **Token costs.** Every query involves multiple round-trips to the API, which can get expensive.
- **Query safety.** You don't want the agent running destructive queries. It only runs SELECT queries by default.
- **Accuracy.** While Claude is good at SQL, it still makes mistakes. The agent includes error-handling logic that lets it retry.
- **Schema understanding.** Some databases have complex schemas with many tables and relationships.

## What's next

- Support for more database types beyond SQLite
- Better visualization of results (charts, graphs)
- The ability to save and share conversations
- Integration with Datasette's permission system

## Labels
datasette, ai, llm, agents
