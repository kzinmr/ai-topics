# How to Build a Code-Editing Agent: The "Emperor Has No Clothes" Guide

**Source:** https://ampcode.com/notes/how-to-build-an-agent
**Author:** Thorsten Ball
**Date:** April 15, 2025
**Scraped:** 2026-05-03

## Summary

Thorsten Ball demonstrates that building a functional code-editing agent is surprisingly simple — an LLM, a loop, three tools (read_file, list_files, edit_file), and ~400 lines of Go. The core thesis: the "agent" part is trivial; sophistication comes from UI, system prompts, and error handling.

## Key Points

- **Agent definition**: "An LLM with access to tools, giving it the ability to modify something outside the context window."
- **Tool use mechanics**: Prompt defines tools → model "winks" by emitting JSON → developer executes locally → results fed back into conversation history
- **Three essential tools**: read_file, list_files, edit_file (string replacement)
- **Emergent behavior**: No explicit tool selection logic needed — the model deduces tool usage from descriptions
- **Tool chaining**: Model automatically chains: list_files → read_file → edit_file to fix bugs
- **"Elbow Grease"**: Professional agents differentiate through UI/UX, system prompts, error handling, editor integration
- **Claude 3.7 Sonnet** used as the underlying model

## Full Article Text

# How to Build a Code-Editing Agent: The "Emperor Has No Clothes" Guide

**Author:** Thorsten Ball  
**Date:** April 15, 2025  
**Core Thesis:** Building a functional code-editing agent is not a "secret science." It is simply an LLM, a loop, and enough tokens. A highly impressive agent can be built in under 400 lines of Go code.

---

## 1. The Definition of an Agent
According to the author, an agent is:
> "An LLM with access to tools, giving it the ability to modify something outside the context window."

### How Tool Use Works
1. **Instruction:** You tell the model what tools are available via a prompt or API.
2. **The "Wink":** The model replies in a specific format (e.g., a JSON block) when it wants to use a tool.
3. **Execution:** You (the developer) execute the tool locally and send the result back to the model.
4. **Statelessness:** The model doesn't "remember" actions; you must maintain the `conversation` slice and send the entire history back with each turn.

---

## 2. Prerequisites & Setup
To follow the implementation, you need:
* **Go** installed.
* **Anthropic API Key** set as `ANTHROPIC_API_KEY`.

**Project Initialization:**
```bash
mkdir code-editing-agent
cd code-editing-agent
go mod init agent
touch main.go
```

---

## 3. Core Implementation: The "Heartbeat" Loop
The agent operates on a continuous loop: get user input → run inference → check for tool use → execute tool → repeat.

### The Inference Function
This snippet shows how tool definitions are passed to Claude 3.7 Sonnet:
```go
func (a *Agent) runInference(ctx context.Context, conversation []anthropic.MessageParam) (*anthropic.Message, error) {
	anthropicTools := []anthropic.ToolUnionParam{}
	for _, tool := range a.tools {
		anthropicTools = append(anthropicTools, anthropic.ToolUnionParam{
			OfTool: &anthropic.ToolParam{
				Name:        tool.Name,
				Description: anthropic.String(tool.Description),
				InputSchema: tool.InputSchema,
			},
		})
	}

	message, err := a.client.Messages.New(ctx, anthropic.MessageNewParams{
		Model:     anthropic.ModelClaude3_7SonnetLatest,
		MaxTokens: int64(1024),
		Messages:  conversation,
		Tools:     anthropicTools,
	})
	return message, err
}
```

---

## 4. The Three Essential Tools
The author implements three tools to transform a chatbot into a developer agent.

### Tool 1: `read_file`
Allows the agent to see the contents of a specific file.
* **Insight:** You must provide a clear description so the model knows *when* to use it (e.g., "Use this when you want to see what's inside a file").

### Tool 2: `list_files`
Allows the agent to explore the directory structure.
* **Implementation Detail:** The author uses a trailing slash (e.g., `dir/`) to denote directories, helping the model distinguish between files and folders.

### Tool 3: `edit_file` (The "Rabbit in the Hat")
Surprisingly, the most effective way to edit files with Claude 3.7 is simple **string replacement**.
* **Mechanism:** The tool takes `Path`, `OldStr` (text to find), and `NewStr` (replacement).
* **Logic:**
```go
newContent := strings.Replace(oldContent, editFileInput.OldStr, editFileInput.NewStr, -1)
```

---

## 5. Key Takeaways & Observations

* **Emergent Reasoning:** You don't need to tell the agent "if the user asks about a file, use `read_file`." If you provide the tool and a description, the model will deduce the necessity of using it to solve the user's request.
* **Tool Chaining:** The agent can automatically chain tools. For example, if asked to "fix a bug," it will:
    1. `list_files` to find the source.
    2. `read_file` to understand the code.
    3. `edit_file` to apply the fix.
* **Boilerplate vs. Logic:** Most of the 400 lines are "type shenanigans" and JSON schema generation. The actual logic of "acting" is minimal.
* **The "Elbow Grease" Factor:** While the core loop is simple, professional agents (like Amp) differentiate themselves through:
    * Better UI/UX.
    * Advanced system prompts.
    * Robust error handling and feedback loops.
    * Integration with editors.

> "300 lines of code and three tools and now you're to be able to talk to an alien intelligence that edits your code... That's why we think everything's changing."
