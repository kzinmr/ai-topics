---
title: "Building Agents That Build Themselves"
source: Vanishing Gradients (Substack)
author: Hugo Bowne-Anderson
co_author: Ivan Leo
date: 2026-02-28
url: https://hugobowne.substack.com/p/building-agents-that-build-themselves
type: article
tags: [agent-harness, self-improving, openclaw, coding-agents, agent-loop]
---

# Building Agents That Build Themselves

     1|Workshops
     2|
     3|Building Agents That Build Themselves
     4|
     5|Full code walkthrough: agents that iterate on their own harnesses
     6|
     7|Hugo Bowne-Anderson
     8|
     9|Feb 28, 2026
    10|
    11|16
    12|
    13|2
    14|
    15|Share
    16|
    17|Yesterday, I ran a workshop with Ivan Leo (ex-Manus) called “Building Your Own OpenClaw from Scratch” to show you how to build your own AI assistant from first principles. We covered:
    18|
    19|How coding agents are really 
    20|
    21|general-purpose computer use agents
    22|
    23| that happen to be great at writing code
    24|
    25|Building the 
    26|
    27|core agent loop
    28|
    29| with an LLM and tool calls
    30|
    31|Context management
    32|
    33|, memory compaction, and progressive disclosure
    34|
    35|How agents can 
    36|
    37|write their own tools
    38|
    39| and hot-reload them on the fly (via a factory pattern)
    40|
    41|Making the agent 
    42|
    43|trigger actions automatically
    44|
    45| (send a Telegram message, log to a database, fire off an email) using hooks
    46|
    47|Connecting the agent to 
    48|
    49|Telegram via FastAPI
    50|
    51|Sandboxing
    52|
    53| and production deployment with Modal
    54|
    55|We wrote this blog post for those who don’t have 100 minutes to watch the entire workshop right now.
    56|
    57|Thanks for reading Vanishing Gradients! Subscribe for free to receive new posts and support my work.
    58|
    59|Subscribe
    60|
    61|All the code from the workshop is available in the 
    62|
    63|build-your-own-ai-assistant
    64|
    65| repo.
    66|
    67|👉 
    68|
    69|These are also the kinds of things we cover in our 
    70|
    71|Building AI Applications course
    72|
    73|. Our final cohort starts March 9. 
    74|
    75|Here is a 25% discount code for readers
    76|
    77|.
    78|
    79| 👈
    80|
    81|Defining the Agent: From Coding Tools to General Computer Use
    82|
    83|(
    84|
    85|Timestamp: 05:16
    86|
    87|)
    88|
    89|An agent is 
    90|
    91|an LLM calling tools in a loop
    92|
    93|.
    94|
    95|The agentic loop is as follows:
    96|
    97|User Prompt:
    98|
    99| The input is sent to the LLM.
   100|
   101|Tool Decision:
   102|
   103| The model decides to call a specific tool (e.g., read_file or search).
   104|
   105|Execution:
   106|
   107| The tool runs and returns the result to the LLM.
   108|
   109|Reasoning:
   110|
   111| The LLM analyzes the output to decide the next step, either another tool call or a final response.
   112|
   113|This is the agentic loop. We gave two examples to make it concrete, a coding agent and a search agent.
   114|
   115|A Coding Agent
   116|
   117|When you ask a coding agent to edit a file, it doesn’t edit immediately. It first:
   118|
   119|Calls
   120|
   121| the read tool to ingest the file (or sometimes the entire codebase)
   122|
   123|Returns
   124|
   125| those contents to the LLM
   126|
   127|Reasons
   128|
   129| about the current state
   130|
   131|Then 
   132|
   133|calls
   134|
   135| the edit tool to make changes
   136|
   137|Each step is a turn through the loop: tool call, result, reasoning, next action.
   138|
   139|A Search Agent
   140|
   141|When you ask a search agent to compare two frameworks, for example, it can’t always answer in one shot. It:
   142|
   143|Searches
   144|
   145| for framework X, returns the results to the LLM
   146|
   147|Realizes
   148|
   149| it needs information about framework Y
   150|
   151|Searches
   152|
   153| for framework Y, returns those results
   154|
   155|Synthesizes
   156|
   157| both results into a comparison
   158|
   159|The agent decides on each next step based on what it learned in the previous one: that’s the loop in action.
   160|
   161|A note on agent harnesses:
   162|
   163| An agent harness is the scaffolding that wraps around an LLM to turn it into an agent. It handles the loop, tool execution, context management, safety guardrails, and state. Think of it this way: 
   164|
   165|the LLM is the brain, the harness is everything else that lets it actually do things.
   166|
   167| We describe this in more detail in 
   168|
   169|How To Build a General Purpose AI Agent in 131 lines of Python
   170|
   171|. This workshop is about building that harness from scratch.
   172|
   173|Coding Agents ARE General Purpose Computer Using Agents
   174|
   175|We should stop referring to them as coding agents because they really are computer use agents that happen to be good at coding or great at writing code when you give them a bash tool. 
   176|
   177|Timestamp: 08:22
   178|
   179|)
   180|
   181|What’s more: A general-purpose agent can be built in 
   182|
   183|131 lines of Python
   184|
   185| using only four fundamental tools: 
   186|
   187|read, write, edit, and bash
   188|
   189|.
   190|
   191|Hugo demonstrates this with a local script. He asks the agent to clean up a messy desktop directory. The agent:
   192|
   193|Lists
   194|
   195| the directory contents with ls
   196|
   197|Identifies
   198|
   199| the file types and a logical folder structure
   200|
   201|Executes
   202|
   203| shell commands to move files into that hierarchy
   204|
   205|Interacts
   206|
   207| with the operating system exactly as a human developer would
   208|
   209|It doesn’t write a script for the user to run: 
   210|
   211|it runs the commands itself
   212|
   213|.
   214|
   215|The Architecture: Pi and OpenClaw
   216|
   217|The goal of the workshop was to help people understand and build MVPs of two popular and useful agents:
   218|
   219|Pi
   220|
   221|:
   222|
   223| A minimal, extensible agent foundation. It uses the four core tools and operates on a philosophy of self-extension. If you want the agent to perform a task it currently cannot do, you ask the agent to write the tool for itself.
   224|
   225|OpenClaw
   226|
   227|:
   228|
   229| OpenClaw builds on Pi and adds many features to it. A few key ones are:
   230|
   231|Gateway:
   232|
   233| Manages sessions and connects to channels like Telegram.
   234|
   235|Proactive Loop:
   236|
   237| Uses heartbeats and cron jobs to check emails, calendars, or alerts without user input.
   238|
   239|Sub-agents:
   240|
   241| Delegated units for specific tasks.
   242|
   243|Core Philosophy: Context, Capabilities, and Memory
   244|
   245|In which we explore how memory and progressive disclosure make agents actually useful over time.
   246|
   247|An agent’s effectiveness depends heavily on the underlying model. Running a legacy model like GPT-3.5 yields vastly different results compared to modern frontiers like Claude Opus or Gemini Pro. Once a capable model is in place, the architecture must solve for two specific requirements: context and capabilities.
   248|
   249|When you’re building a task, you want to use the best models first. Cost is something you want to think about very far down the line, once you’ve confirmed that a frontier model can actually do the task.
   250|
   251|(
   252|
   253|Timestamp: 51:04
   254|
   255|)
   256|
   257|Context is King
   258|
   259|Context allows the agent to understand the user over time
   260|
   261|. As interactions increase, the model should reference past discussions, mistakes, and workflows. OpenClaw manages this through a specific memory architecture. It creates memory files for every day. When a conversation reaches a certain length, a compaction pattern triggers. This process summarizes the interaction and appends it to a timestamped Markdown file.
   262|
   263|The model reads these files to understand the chronological history of the user’s work. While the agent retains access to raw database traces (JSON files), the timestamped summaries serve as the primary retrieval mechanism. This allows the agent to make informed decisions based on historical patterns rather than just immediate inputs.
   264|
   265|If the model wants to figure out what we talked about during the conversation, it still has access to the raw database or the raw traces... But the real takeaway is just that it should have more context on you as you interact more and more with it... creating memory files for every day every time a compaction is reached.
   266|
   267|(
   268|
   269|Timestamp: 16:21
   270|
   271|)
   272|
   273|No vector database and no embeddings:
   274|
   275| just append to a text file!
   276|
   277|People are just so surprised that something simple like appending summaries to a markdown file timestamped. It works so well for memories and people like it so much. A lot of the love that OpenClaw has is just because the model can see the raw chats and the model can see the summaries.
   278|
   279|(
   280|
   281|Timestamp: 29:32
   282|
   283|)
   284|
   285|Capabilities
   286|
   287|Capabilities refer to the agent’s ability to extend itself. Following the Pi coding agent philosophy, the goal is “
   288|
   289|building software that builds software
   290|
   291|.” Developers can extend agents by adding skills, modifying system prompts, or integrating Model Context Protocols (MCPs). 
   292|
   293|But agents can extend themselves also
   294|
   295|!
   296|
   297|The distinction between context and capabilities defines the agent’s utility:
   298|
   299|Context:
   300|
   301| The model has access to data sources, such as a calendar or past chat logs. It knows 
   302|
   303|what
   304|
   305| has happened.
   306|
   307|Capabilities:
   308|
   309| The model has the tools to act on that data. It knows 
   310|
   311|how
   312|
   313| to execute tasks.
   314|
   315|If an agent has access to a calendar (Context), it can see a user had late-night calls for three days straight. With the right instructions (Capabilities), it can proactively suggest sleeping in.
   316|
   317|With better context, better system prompt, better prompts, better information, the models can do more for you. With capabilities, a lot of it is about extending it and making it easy for the model to either write its own tools or be able to get the information it needs.
   318|
   319|(
   320|
   321|Timestamp: 18:19
   322|
   323|)
   324|
   325|But 
   326|
   327|more tools doesn’t mean more capable
   328|
   329|. Progressive disclosure matters because models struggle when you dump everything on them at once.
   330|
   331|You got to have a bit of empathy for the model. Imagine if someone gave you like 200 tools to choose from every time you had to make a decision. You wouldn’t even be able to finish reading all of the tools before you asked to give a response.
   332|
   333|(
   334|
   335|Timestamp: 21:42
   336|
   337|)
   338|
   339|For the practical application of these principles, we used Gemini 3 Flash. While not as powerful as Opus, Flash is fast and cost-effective. Its speed makes interactions feel instant, reducing the immediate need for complex streaming architectures during the build process. The fundamental architecture remains a language model running in a loop with a managed token budget, extended via tool calling to interact with the environment.
   340|
   341|The following sections cover 
   342|
   343|building these components from scratch
   344|
   345|, starting with 
   346|
   347|the base loop
   348|
   349| and moving toward 
   350|
   351|memory compaction
   352|
   353|, 
   354|
   355|factory patterns for tool creation
   356|
   357|, and 
   358|
   359|deploying to sandboxed environments like Modal
   360|
   361|.
   362|
   363|Implementing the Loop: Gemini, Pydantic, and Thought Signatures
   364|
   365|In which we build the agentic loop from scratch, one API call at a time.
   366|
   367|Remember that building an agent is building 
   368|
   369|an LLM calling tools in a loop
   370|
   371|: you send a user prompt, the model decides to call a tool, you execute that tool, and you send the result back. This cycle continues until the model determines the task is complete or runs out of tokens.
   372|
   373|At the core of this loop is the transition from regarding LLMs as smart autocomplete engines to reasoning agents that interact with their environment. By enforcing type contracts (essentially telling the model that calling a specific function requires a specific JSON payload) you enable the system to read files, execute bash commands, or query databases.
   374|
   375|First, we declare a tool and make a single API call (
   376|
   377|workshop/1/agent.py
   378|
   379|):
   380|
   381|The model returns a 
   382|
   383|function_call
   384|
   385| in its response (it 
   386|
   387|wants
   388|
   389| to read the file) but nothing executes it yet. We just see the request.
   390|
   391|Next, we add the actual function, execute the tool call, feed the result back, and call the model again (
   392|
   393|workshop/2/agent.py
   394|
   395|):
   396|
   397|This is one manual round-trip: the model asks for a tool, we execute it, we send the result back. Notice the line 
   398|
   399|contents.append(completion.candidates[0].content)
   400|
   401|: that preserves the model’s thought signatures, which we’ll discuss next.
   402|
   403|This is still hardcoded for a single round-trip. To make a real agent, we need a loop that keeps going until the model stops requesting tools (
   404|
   405|workshop/3/agent.py
   406|
   407|):
   408|
   409|The 
   410|
   411|run()
   412|
   413| function handles one model call: if the model returns a function call, execute it and return the result. If it returns text, return None.
   414|
   415|The inner while True keeps calling 
   416|
   417|run()
   418|
   419| until the model is done. This is the agentic loop.
   420|
   421|Thought Signatures and Context Preservation
   422|
   423|When implementing this loop with Gemini, handling the model’s internal reasoning (referred to as “thought signatures”) is critical for performance. Frontier models are trained on unrestricted chains of thought. When the model generates a response, it often includes these internal reasoning traces alongside the final output or tool call.
   424|
   425|If you strip these signatures out when passing the conversation history back to the model for the next turn, 
   426|
   427|you sever its train of thought
   428|
   429|. Preserving this metadata ensures the model retains the context of 
   430|
   431|why
   432|
   433| it made a specific decision.
   434|
   435|By preserving the thought signatures you can actually ensure that your model performance increases by like 5 to 10%. That’s the case with the Gemini 3 series of models... for a lot of these frontier models when the models are trained they’re trained based off their unrestricted chain of thought.
   436|
   437|(
   438|
   439|Timestamp: 00:38:20
   440|
   441|)
   442|
   443|The Factory Pattern: Refactoring for Extensibility
   444|
   445|It’s incredible how straightforward it is to allow an agent to write its own tools.
   446|
   447|We refactored our agent so that tools are just classes. Each tool inherits from a base class, defines its parameters, and implements an execute method. The runtime uses Pydantic to automatically generate the function calling schemas from type hints. Because execution is separate from the schema, you can test each tool independently without invoking the LLM (
   448|
   449|workshop/4/agent_tools.py
   450|
   451|):
   452|
   453|The AgentRuntime dispatches by name and validates args via Pydantic: it doesn’t know about specific tools (
   454|
   455|workshop/4/agent.py
   456|
   457|):
   458|
   459|Adding a new tool means adding a class to 
   460|
   461|agent_tools.py
   462|
   463| and appending it to TOOLS. 
   464|
   465|The runtime and the agent loop don’t change at all.
   466|
   467| This is what makes self-writing tools possible: the pattern is so simple that the agent can read the tools file, see the pattern, and write new tool classes itself.
   468|
   469|All you need to do to implement a new tool is define the parameters you want. These are automatically converted into a schema. Define an execute function. And the beauty of this is that you can actually test and validate your execute function independently of your model being called.
   470|
   471|Once tools have their own execute methods, you also want to make them async from day one:
   472|
   473|It’s much more useful to start with an async runtime... when you’re interfacing with like databases, logging, etc. A lot of these are written and implemented as async functions. And so if you don’t have async functionality built in from the beginning, it’s a bit complicated down the line.
   474|
   475|(
   476|
   477|Timestamp: 1:00:08
   478|
   479|)
   480|
   481|Software Building Software: Hot Reloading and Self-Modification
   482|
   483|What’s amazing is the agent can modify its own harness!
   484|
   485|When you give the agent access to the source code of its own tools, it can read the patterns, understand how tools are defined, and write new ones for itself. This is a new paradigm of software building software, and the factory pattern we just set up is what makes it possible. Standard Python runtimes load modules once, so if an agent writes a new tool, the server normally requires a restart. Hot reloading solves this.
   486|
   487|The mechanism is straightforward: the runtime tracks the 
   488|
   489|last_modified
   490|
   491| timestamp of the 
   492|
   493|agent_tools.py
   494|
   495| file where tool classes are defined and before every inference step, specifically when get_tools or execute_tool is called, the system checks if this timestamp has changed (
   496|
   497|workshop/6/agent.py
   498|
   499|):
   500|
   501|
