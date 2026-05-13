---
title: "Context Engineering for Agents"
author: Lance Martin
source_url: https://rlancemartin.github.io/2025/06/23/context_engineering/
date: 2025-06-23
date_published: 2025-06-23
type: blog_post
tags: [context-engineering, agents, prompt-engineering, memory, context-window]
---

# Context Engineering for Agents

Jun 23, 2025

[Lance Martin](https://x.com/RLanceMartin)

### TL;DR

Agents need context to perform tasks. Context engineering is the art and science of filling the context window with just the right information at each step of an agent's trajectory. In this post, I group context engineering into a few common strategies seen across many popular agents today.

### Context Engineering

As Andrej Karpathy puts it, LLMs are like a [new kind of operating system](https://www.youtube.com/watch?si=-aKY-x57ILAmWTdw&t=620&v=LCEmiRjPEtQ&feature=youtu.be). The LLM is like the CPU and its [context window](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) is like the RAM, serving as the model's working memory. Just like RAM, the LLM context window has limited [capacity](https://lilianweng.github.io/posts/2023-06-23-agent/) to handle various sources of context. And just as an operating system curates what fits into a CPU's RAM, "context engineering" plays a similar role. [Karpathy summarizes this well](https://x.com/karpathy/status/1937902205765607626):

> [Context engineering is the] "…delicate art and science of filling the context window with just the right information for the next step."

What are the types of context that we need to manage when building LLM applications? Context engineering is an [umbrella](https://x.com/dexhorthy/status/1933283008863482067) that applies across a few different context types:

- **Instructions** – prompts, memories, few‑shot examples, tool descriptions, etc
- **Knowledge** – facts, memories, etc
- **Tools** – feedback from tool calls

### Context Engineering for Agents

This year, interest in [agents](https://www.anthropic.com/engineering/building-effective-agents) has grown tremendously as LLMs get better at [reasoning](https://platform.openai.com/docs/guides/reasoning?api-mode=responses) and [tool calling](https://www.anthropic.com/engineering/building-effective-agents). [Agents](https://www.anthropic.com/engineering/building-effective-agents) interleave [LLM invocations and tool calls](https://www.anthropic.com/engineering/building-effective-agents), often for [long-running tasks](https://blog.langchain.com/introducing-ambient-agents/).

However, long-running tasks and accumulating feedback from tool calls mean that agents often utilize a large number of tokens. This can cause numerous problems: it can [exceed the size of the context window](https://cognition.ai/blog/kevin-32b), balloon cost / latency, or degrade agent performance. Drew Breunig [nicely outlined](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html) a number of specific ways that longer context can cause perform problems, including:

- [Context Poisoning: When a hallucination makes it into the context](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html#context-poisoning)
- [Context Distraction: When the context overwhelms the training](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html#context-distraction)
- [Context Confusion: When superfluous context influences the response](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html#context-confusion)
- [Context Clash: When parts of the context disagree](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html#context-clash)

With this in mind, [Cognition](https://cognition.ai/blog/dont-build-multi-agents) called out the importance of context engineering:

> *"Context engineering" … is effectively the #1 job of engineers building AI agents.*

[Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system) also laid it out clearly:

> *Agents often engage in conversations spanning hundreds of turns, requiring careful context management strategies.*

So, how are people tackling this challenge today? I group approaches into 4 buckets — **write, select, compress, and isolate —** and give some examples of each one below.

### Write Context

*Writing context means saving it outside the context window to help an agent perform a task.*

**Scratchpads**

When humans solve tasks, we take notes and remember things for future, related tasks. Agents are also gaining these capabilities! Note-taking via a "[scratchpad](https://www.anthropic.com/engineering/claude-think-tool)" is one approach to persist information while an agent is performing a task. The central idea is to save information outside of the context window so that it's available to the agent. [Anthropic's multi-agent researcher](https://www.anthropic.com/engineering/built-multi-agent-research-system) illustrates a clear example of this:

> *The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated and it is important to retain the plan.*

Scratchpads can be implemented in a few different ways. They can be a [tool call](https://www.anthropic.com/engineering/claude-think-tool) that simply [writes to a file](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem). It could also just be a field in a runtime [state object](https://langchain-ai.github.io/langgraph/concepts/low_level/#state) that persists during the session. In either case, scratchpads let agents save useful information to help them accomplish a task.

**Memories**

Scratchpads help agents solve a task within a given session, but sometimes agents benefit from remembering things across *many* sessions. [Reflexion](https://arxiv.org/abs/2303.11366) introduced the idea of reflection following each agent turn and re-using these self-generated memories. [Generative Agents](https://ar5iv.labs.arxiv.org/html/2304.03442) created memories synthesized periodically from collections of past agent feedback.

These concepts made their way into popular products like [ChatGPT](https://help.openai.com/en/articles/8590148-memory-faq), [Cursor](https://forum.cursor.com/t/0-51-memories-feature/98509), and [Windsurf](https://docs.windsurf.com/windsurf/cascade/memories), which all have mechanisms to auto-generate long-term memories based on user-agent interactions.

### Select Context

*Selecting context means pulling it into the context window to help an agent perform a task.*

**Scratchpad**

The mechanism for selecting context from a scratchpad depends upon how the scratchpad is implemented. If it's a [tool](https://www.anthropic.com/engineering/claude-think-tool), then an agent can simply read it by making a tool call. If it's part of the agent's runtime state, then the developer can choose what parts of state to expose to an agent each step. This provides a fine-grained level of control for exposing scratchpad context to the LLM at later turns.

**Memories**

If agents have the ability to save memories, they also need the ability to select memories relevant to the task they are performing. This can be useful for a few reasons. Agents might select few-shot examples ([episodic memories](https://langchain-ai.github.io/langgraph/concepts/memory/#memory-types)) for examples of desired behavior, instructions ([procedural memories](https://langchain-ai.github.io/langgraph/concepts/memory/#memory-types)) to steer behavior, or facts ([semantic memories](https://langchain-ai.github.io/langgraph/concepts/memory/#memory-types)) give the agent task-relevant context.

One challenge is ensuring that relevant memories are selected. Some popular agents simply use a narrow set of files that are *always* pulled into context. For example, many code agent use files to save instructions ("procedural" memories) or, in some cases, examples ("episodic" memories). Claude Code uses [`CLAUDE.md`](http://CLAUDE.md). [Cursor](https://docs.cursor.com/context/rules) and [Windsurf](https://windsurf.com/editor/directory) use rules files.

But, if an agent is storing a larger [collection](https://langchain-ai.github.io/langgraph/concepts/memory/#collection) of facts and / or relationships (e.g., [semantic](https://langchain-ai.github.io/langgraph/concepts/memory/#memory-types) memories), selection is harder. [ChatGPT](https://help.openai.com/en/articles/8590148-memory-faq) is a good example of a popular product that stores and selects from a large collection of user-specific memories.

Embeddings and / or [knowledge graphs](https://arxiv.org/html/2501.13956v1#:~:text=In%20Zep%2C%20memory%20is%20powered,subgraph%2C%20and%20a%20community%20subgraph) for memory indexing are commonly used to assist with selection. Still, memory selection is challenging. At the AIEngineer World's Fair, [Simon Willison shared](https://simonwillison.net/2025/Jun/6/six-months-in-llms/) an example of memory selection gone wrong: ChatGPT fetched his location from memories and unexpectedly injected it into a requested image. This type of unexpected or undesired memory retrieval can make some users feel like the context window "no longer belongs to them"!

**Tools**

Agents use tools, but can become overloaded if they are provided with too many. This is often because the tool descriptions can overlap, causing model confusion about which tool to use. One approach is [to apply RAG (retrieval augmented generation) to tool descriptions](https://arxiv.org/abs/2410.14594) in order to fetch the most relevant tools for a task based upon semantic similarity. Some [recent papers](https://arxiv.org/abs/2505.03275) have shown that this improves tool selection accuracy by 3-fold.

**Knowledge**

[RAG](https://github.com/langchain-ai/rag-from-scratch) is a rich topic and [can be a central context engineering challenge](https://x.com/_mohansolo/status/1899630246862966837). Code agents are some of the best examples of RAG in large-scale production. Varun from Windsurf captures some of these challenges well:

> *Indexing code ≠ context retrieval … [We are doing indexing & embedding search … [with] AST parsing code and chunking along semantically meaningful boundaries … embedding search becomes unreliable as a retrieval heuristic as the size of the codebase grows … we must rely on a combination of techniques like grep/file search, knowledge graph based retrieval, and … a re-ranking step where [context] is ranked in order of relevance.*

### Compressing Context

*Compressing context involves retaining only the tokens required to perform a task.*

**Context Summarization**

Agent interactions can span [hundreds of turns](https://www.anthropic.com/engineering/built-multi-agent-research-system) and use token-heavy tool calls. Summarization is one common way to manage these challenges. If you've used Claude Code, you've seen this in action. Claude Code runs "[auto-compact](https://docs.anthropic.com/en/docs/claude-code/costs)" after you exceed 95% of the context window and it will summarize the full trajectory of user-agent interactions. This type of compression across an [agent trajectory](https://langchain-ai.github.io/langgraph/concepts/memory/#manage-short-term-memory) can use various strategies such as [recursive](https://arxiv.org/pdf/2308.15022#:~:text=the%20retrieved%20utterances%20capture%20the,based%203) or [hierarchical](https://alignment.anthropic.com/2025/summarization-for-monitoring/#:~:text=We%20addressed%20these%20issues%20by,of%20our%20computer%20use%20capability) summarization.

It can also be useful to [add summarization](https://github.com/langchain-ai/open_deep_research/blob/e5a5160a398a3699857d00d8569cb7fd0ac48a4f/src/open_deep_research/utils.py#L1407) at points in an agent's design. For example, it can be used to post-process certain tool calls (e.g., token-heavy search tools). As a second example, [Cognition](https://cognition.ai/blog/dont-build-multi-agents#a-theory-of-building-long-running-agents) mentioned summarization at agent-agent boundaries to reduce tokens during knowledge hand-off. Summarization can be a challenge if specific events or decisions need to be captured. Cognition uses a fine-tuned model for this, which underscores how much work can go into this step.

**Context Trimming**

Whereas summarization typically uses an LLM to distill the most relevant pieces of context, trimming can often filter or, as Drew Breunig points out, "[prune](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html)" context. This can use hard-coded heuristics like removing [older messages](https://python.langchain.com/docs/how_to/trim_messages/) from a message list. Drew also mentions [Provence](https://arxiv.org/abs/2501.16214), a trained context pruner for Question-Answering.

### Isolating Context

*Isolating context involves splitting it up to help an agent perform a task.*

**Multi-agent**

One of the most popular ways to isolate context is to split it across sub-agents. A motivation for the OpenAI [Swarm](https://github.com/openai/swarm) library was "[separation of concerns](https://openai.github.io/openai-agents-python/ref/agent/)", where a team of agents can handle sub-tasks. Each agent has a specific set of tools, instructions, and its own context window.

Anthropic's [multi-agent researcher](https://www.anthropic.com/engineering/built-multi-agent-research-system) makes a case for this: many agents with isolated contexts outperformed single-agent, largely because each subagent context window can be allocated to a more narrow sub-task. As the blog said:

> *[Subagents operate] in parallel with their own context windows, exploring different aspects of the question simultaneously.*

Of course, the challenges with multi-agent include token use (e.g., up to [15× more tokens](https://www.anthropic.com/engineering/built-multi-agent-research-system) than chat as reported by Anthropic), the need for careful [prompt engineering](https://www.anthropic.com/engineering/built-multi-agent-research-system) to plan sub-agent work, and coordination of sub-agents.

**Context Isolation with Environments**

HuggingFace's [deep researcher](https://huggingface.co/blog/open-deep-research#:~:text=From%20building%20,it%20can%20still%20use%20it) shows another interesting example of context isolation. Most agents use [tool calling APIs](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview), which return JSON objects (tool arguments) that can be passed to tools (e.g., a search API) to get tool feedback (e.g., search results). HuggingFace uses a [CodeAgent](https://huggingface.co/papers/2402.01030), which outputs code that contains the desired tool calls. The code then runs in a [sandbox](https://e2b.dev/). Selected context (e.g., return values) from the tool calls is then passed back to the LLM.

This allows context to be isolated from the LLM in the environment. Hugging Face noted that this is a great way to isolate token-heavy objects in particular:

> *[Code Agents allow for] a better handling of state … Need to store this image / audio / other for later use? No problem, just assign it as a variable [in your state and you [use it later]](https://deepwiki.com/search/i-am-wondering-if-state-that-i_0e153539-282a-437c-b2b0-d2d68e51b873).*

**State**

It's worth calling out that an agent's runtime [state object](https://langchain-ai.github.io/langgraph/concepts/low_level/#state) can also be a great way to isolate context. This can serve the same purpose as sandboxing. A state object can be designed with a [schema](https://langchain-ai.github.io/langgraph/concepts/low_level/#schema) (e.g., a [Pydantic](https://docs.pydantic.dev/latest/concepts/models/) model) that has fields that context can be written to. One field of the schema (e.g., `messages`) can be exposed to the LLM at each turn of the agent, but the schema can isolate information in other fields for more selective use.

### Conclusion

Patterns for agent context engineering are still evolving, but we can group common approaches into 4 buckets — **write, select, compress, and isolate —**:

- *Writing context means saving it outside the context window to help an agent perform a task.*
- *Selecting context means pulling it into the context window to help an agent perform a task.*
- *Compressing context involves retaining only the tokens required to perform a task.*
- *Isolating context involves splitting it up to help an agent perform a task.*

Understanding and utilizing these patterns is a central part of building effective agents today.
