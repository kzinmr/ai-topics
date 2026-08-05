---
title: "New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging"
url: "https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything"
fetched_at: 2026-08-05T10:12:32.261733+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging

Source: https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything

New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging
4th August 2026
I released
LLM 0.32
this morning, the most significant new version of LLM since the initial launch of the project. The new version includes support for visible reasoning traces, server-side provider tools, redesigned content-addressable SQLite logs, new models, and new features enabled by the OpenAI Responses API. I also released a new version of the
llm-anthropic plugin
with substantial updates of its own.
Headline features for LLM CLI users
Running LLM against reasoning models now
displays their reasoning traces
to standard error, so you can see what they are “thinking” without that information being included in the standard output that you might pipe to another tool. Add
-R/--hide-reasoning
to turn this off.
LLM includes support out-of-the-box for the
GPT-5.6 model family
, and the new default model used with
llm "prompt"
is now the inexpensive but capable
GPT-5.6 Luna
.
LLM calls can now use
server-side tools
from various providers. OpenAI provide
a code execution environment
as a server-side tool; LLM can now run prompts that benefit from that like so:
llm --tool CodeInterpreter
'
Show current python and SQLite versions
'
OpenAI also gets a
WebSearch
tool.
The
llm-anthropic
plugin adds
WebSearch
,
WebFetch
,
CodeExecution
, and
AnthropicMCP
, which looks like this:
llm -m claude-sonnet-5 -T
'
AnthropicMCP("https://datasette.simonwillison.net/-/mcp")
'
\
'
how many rows in the blog_blogmark table?
'
That causes Anthropic to execute MCP calls against my new
datasette-mcp
plugin as part of a single request/response interaction with their API.
The new
llm openai endpoint
command provides a tool for
executing prompts against
any
OpenAI compatible endpoint
as a one-liner. These aren’t logged, which makes this a handy tool for running one-off prompts against anything that speaks the lingua franca of the LLM API world.
Here’s how I use that to run prompts against Gemma 4 12B running in my localhost
LM Studio
API, via
uvx
(no LLM installation required) and mixing in the
llm-tools-quickjs
tool plugin for good measure:
uvx --with llm-tools-quickjs \
  llm openai endpoint http://localhost:1234/v1 -m google/gemma-4-12b \
  -T QuickJS
'
Use QuickJS to multiply 3434 * 2434
'
--td
New features in the Python API
LLM’s Python API previously required you to create a conversation and then send messages to it one at a time. This was an abstraction over the true nature of LLMs, where each request carries a complete history of the messages that came before it. That abstraction started to get in the way for some more advanced cases, so the new release introduces a
model.prompt(messages=[])
parameter that can be used like this:
import
llm
from
llm
import
user
,
assistant
,
system
model
=
llm
.
get_model
(
"gpt-5.6-luna"
)
response
=
model
.
prompt
(
messages
=
[
system
(
"You are a helpful pirate."
),
user
(
"What is the capital of France?"
),
assistant
(
"Paris, matey."
),
user
(
"And Germany?"
),
])
print
(
response
.
text
())
LLM previously returned an iterable sequence of strings from each prompt. This worked great when models returned a string response, but failed to predict the weird shape that models would evolve towards. Today many models return a mix of reasoning text, output strings, tool calls, and even image attachments. With LLM 0.32 you can
do this instead
:
for
event
in
model
.
prompt
(
"Explain cats"
).
stream_events
():
if
event
.
type
==
"reasoning"
:
print
(
f"[thinking]
{
event
.
chunk
}
"
,
end
=
""
,
flush
=
True
)
elif
event
.
type
==
"text"
:
print
(
event
.
chunk
,
end
=
""
,
flush
=
True
)
else
:
print
(
f"Other event:
{
event
}
"
)
Combine these features and we can
finally
provide a robust implementation of the semi-standard OpenAI chat completions API, which I’ve now released as the
llm-chat-completions-server
plugin:
llm install llm-chat-completions-server
llm chat-completions-server --port 9000
#
Server is now running on http://127.0.0.1:9000/v1
Now you can run prompts against LLM via that server, using the new
llm openai endpoint
command!
llm openai endpoint http://127.0.0.1:9000/v1
'
hello
'
-m gpt-5.4-mini
The bigger challenge with that kind of API concerns logging. If we’re going to support the pattern where the message sequence is appended to on every request, ideally we can avoid logging all of that duplicate JSON for every turn.
The solution is the new
content-addressable message store
, modeled after Git. You can see the new schema for that
in the documentation
, but the
llm logs
and
llm logs --json
commands have both been upgraded to convert that format back into something that’s easy to consume.
And the rest
There is a whole lot more in this release. The
0.32 release notes
are pretty comprehensive, and the notes for
0.32rc2
,
0.32rc
,
0.32a3
,
0.32a2
, and
0.32a0
should fill in any gaps.
Existing LLM plugins should all continue to work, but plugins that provide extra models will need to be upgraded to 0.32 in order to participate fully in the new streaming events system. There’s a guide to implementing plugins with
Structured messages and streaming events
in the documentation.
I’ve updated some of my own plugins:
I guess LLM is an agent framework now
Quite a few of the lower-level tools changes in this release were driven by the needs of
Datasette Agent
. When I started work on LLM, the term “agent” had such a vague definition that I refused to use it. In
September 2025
I came around to the idea that "
An LLM agent runs tools in a loop to achieve a goal
" is well established enough now that I could stop avoiding the term entirely.
Tool chains can now
pause for human approval
and
resume from a stored message history
—both needed by Datasette Agent.
Looking at LLM today it’s beginning to look very agent-shaped to me. There’s something neat about having a CLI utility that can mix and match different tools from different sources with different models all as a one-liner, and that includes a Python library powerful enough to build systems like
Datasette Agent
and
llm-coding-agent
.
Maybe the next version of LLM will bake the concept of an “agent” into the core library. I’m still trying to figure out what that would look like.
