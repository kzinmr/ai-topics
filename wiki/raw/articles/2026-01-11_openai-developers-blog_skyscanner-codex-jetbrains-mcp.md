---
title: "Supercharging Codex with JetBrains MCP at Skyscanner"
url: "https://developers.openai.com/blog/skyscanner-codex-jetbrains-mcp/"
date: "2026-01-11"
source: "OpenAI Developers Blog"
tags: ["openai", "developer-blog", "codex", "agents", "mcp", "skills", "skyscanner", "jetbrains"]
---

# Supercharging Codex with JetBrains MCP at Skyscanner

Learn how Skyscanner turbocharged OpenAI’s Codex CLI by integrating it with JetBrains IDEs, giving their AI assistant the same debugging and testing tools that human developers use.

At Skyscanner, we’re always looking for ways to accelerate development without compromising quality. Over the past few months, I’ve been experimenting with OpenAI’s Codex as a pair programmer in my daily workflow.

The twist? I hooked the Codex CLI into JetBrains’ IDEs using their Model Context Protocol (MCP) server: essentially letting the AI see and use the IDE’s capabilities. This integration has been a game-changer. In this post, I’ll share how giving Codex access to JetBrains tools has improved its problem-solving skills and sped up our development.

## Giving Codex an IDE’s Context

Working with Codex using the JetBrains MCP server means the AI can now tap into the rich context of my development environment—things it normally wouldn’t “see”.

With the JetBrains MCP, Codex can ask the IDE for extra context, for example:

Find file problems: analyse a file for errors and warnings using IntelliJ inspections and return the exact issues (with error messages and locations).
Execute run configurations: run predefined run configurations (like unit tests, linters, or formatters) and retrieve exit codes and output.

- Find file problems: analyse a file for errors and warnings using IntelliJ inspections and return the exact issues (with error messages and locations).

- Execute run configurations: run predefined run configurations (like unit tests, linters, or formatters) and retrieve exit codes and output.

This has proved to be extremely powerful—by tapping into the same feedback loops human developers rely on when writing, compiling, and testing code, Codex can use the IDE’s context to check and verify its output more effectively, reducing iteration time.

### Catching Errors Faster: A Real-World Example

As I was writing unit tests for error handling in our code that uses Databricks’ Java SDK, I prompted Codex to help me stub out an exception scenario. It confidently produced a line of Java code which looked something like this:

```
var stubError = new NotFound("dummy error");
```

var stubError = new NotFound("dummy error");

At first glance, that looks reasonable—we want to simulate a NotFound error. But moments later, IntelliJ highlighted that line with a big red underline.

NotFound

The problem: the NotFound exception class in the Databricks SDK doesn’t have a constructor that takes a single string argument (you can see this in the Databricks SDK source: NotFound.java). In other words, Codex’s suggested code was never going to compile.

NotFound

By default, Codex wouldn’t know about this mistake. It might only realise something’s wrong later when trying to run tests. However, because of the JetBrains MCP integration, Codex immediately noticed the error. Behind the scenes, Codex called the IDE’s get_file_problems tool to inspect the file, which returned the compilation issue (no matching constructor) right away.

get_file_problems

Without the MCP, the likely flow would have been:

Generate code
Determine how to run unit tests
Run the unit tests (potentially needing to escalate commands to the user)
Read and parse the failure message
Attempt to fix the error

- Generate code

- Determine how to run unit tests

- Run the unit tests (potentially needing to escalate commands to the user)

- Read and parse the failure message

- Attempt to fix the error

With the JetBrains MCP, that loop is much tighter:

Generate code
Ask JetBrains for file problems
Fix the exact error that IntelliJ reports

- Generate code

- Ask JetBrains for file problems

- Fix the exact error that IntelliJ reports

This saved time and context, and it felt very much like pair programming with an engineer who immediately says, “Ah, that class doesn’t have a constructor like that—it actually requires something different. Let me quickly fix that”.

### Predefined testing and formatting

Another advantage I’ve enjoyed is letting Codex drive our existing build and test tooling directly from the IDE. For most of our projects, I have already defined local run configurations in my IDE, such as running tests, formatting and linting. With the JetBrains MCP, Codex can discover and run these configurations on demand.

In practice, this reduces the time and context required for Codex to figure out how to run this functionality, helping it maintain focus on the original problem. With this change, I’ve observed that Codex no longer stumbles when running tests, formatting or linting.

In my custom agent instructions, I therefore instruct Codex to run tests, linting and formatting after every change.

```
## Code edit instructions

After you've finished editing

- Use the jetbrains mcp (if available) to find any problems
- Run format command if available
- Run lint command if available
```

## Code edit instructions

After you've finished editing

- Use the jetbrains mcp (if available) to find any problems
- Run format command if available
- Run lint command if available

I’ve noticed Codex now often solves issues itself without me having to intervene. As a developer, that feels like a huge win:

I don’t have to manually run tests, linting and formatting every time Codex changes something.
I don’t have to copy-paste error messages back into the chat.
Codex gets rapid, precise feedback on whether its changes actually work, reducing the number of feedback cycles.

- I don’t have to manually run tests, linting and formatting every time Codex changes something.

- I don’t have to copy-paste error messages back into the chat.

- Codex gets rapid, precise feedback on whether its changes actually work, reducing the number of feedback cycles.

This gives me more time to focus on the task at hand: delivering high-quality working software.

## What This Means for How We Build

Integrating Codex with JetBrains MCP has made our AI assistant markedly more capable and reliable in our development process. Some of the practical benefits we’ve seen are:

Faster feedback loops: Codex gets immediate feedback from the IDE about compile errors and failing tests.
Fewer back-and-forth prompts: Codex doesn’t always have to wait for me to run something and paste an error message—it can query the IDE directly.
Higher-quality suggestions: Because Codex can see what the IDE sees, its fixes are more likely to compile and pass tests on the first try.
Better alignment with existing workflows: Codex plugs into our existing tooling, instead of inventing its own.

- Faster feedback loops: Codex gets immediate feedback from the IDE about compile errors and failing tests.

- Fewer back-and-forth prompts: Codex doesn’t always have to wait for me to run something and paste an error message—it can query the IDE directly.

- Higher-quality suggestions: Because Codex can see what the IDE sees, its fixes are more likely to compile and pass tests on the first try.

- Better alignment with existing workflows: Codex plugs into our existing tooling, instead of inventing its own.

Overall, it has turned Codex from a standalone tool into a more integrated part of our development ecosystem.

## Summary

For us at Skyscanner, the key insight has been simple: context is everything. Codex on its own is powerful, but Codex with IDE awareness is far more effective. This context gives Codex even more insight, enabling it to produce accurate fixes faster and further increasing my trust in its output.

We hope our story inspires others to experiment with these integrations. It truly feels much less like using a tool and much more like collaborating with an AI pair programmer that can see what we see.
