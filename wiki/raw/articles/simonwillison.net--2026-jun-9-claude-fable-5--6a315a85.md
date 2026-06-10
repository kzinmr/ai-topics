---
title: "Initial impressions of Claude Fable 5"
url: "https://simonwillison.net/2026/Jun/9/claude-fable-5/#atom-everything"
fetched_at: 2026-06-10T07:01:28.160078+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Initial impressions of Claude Fable 5

Source: https://simonwillison.net/2026/Jun/9/claude-fable-5/#atom-everything

Initial impressions of Claude Fable 5
9th June 2026
I didn’t have early access to today’s
Claude Fable 5
release, but I’ve spent the past ~5.5 hours putting it through its paces. My initial impressions are that this is something of a
beast
. It’s slow, expensive and has been quite happily churning through everything I’ve thrown at it so far. As is frequently the case with current frontier models the challenge is finding tasks that it can’t do.
First, let’s review the key characteristics.
Anthropic claim that
Claude Fable 5
offers the same performance as Claude Mythos 5, except with much more strict guardrails in place to prevent it being used for harmful things. Those guardrails trigger often enough that the Claude API has new mechanisms for letting you know when you hit them, and even has a
new option
to request it falls back to another model automatically if something gets rejected.
Claude Mythos 5 is out today as well,
Anthropic say it
“Shares Claude Fable 5’s capabilities without the safety classifiers”.
The models have a 1 million token context window, 128,000 maximum output tokens and a knowledge cut-off date of January 2026.
They are priced at twice the price of Claude Opus 4.5/4.6/4.7/4.8: $10/million input tokens and $50/million output tokens. There’s no increase in price for longer context usage.
Other than that the
upgrade guide
is substantially thinner than
the similar guide for Opus 4.8
.
The big model smell
The best way to describe Fable is that it feels
big
. Not just in terms of speed and cost, but also in how much it knows.
Here’s an example prompt, which I used to compare Fable’s knowledge with Opus 4.8 (typo included):
List all of Simon Willion's open source projects, most recent first, each with a rough date of when they were first released
Opus 4.8’s reply
started like this
:
I don’t have a reliable, comprehensive, and date-verified list of all of Simon Willison’s open source projects, and I want to be honest about that rather than risk giving you inaccurate dates or fabricated entries.
Here’s what I can tell you with reasonable confidence:
Well-known projects by Simon Willison:
LLM
(~2023) – A command-line tool and Python library for interacting with large language models.
Datasette
(~2017) – A tool for exploring and publishing data, probably his most prominent recent project.
sqlite-utils
(~2018-2019) – A Python library and CLI tool for manipulating SQLite databases, often used alongside Datasette.
Django
(2005) – He is one of the co-creators of the Django web framework, along with Adrian Holovaty, originally developed at the Lawrence Journal-World newspaper.
He also maintains a large ecosystem of
Datasette plugins
and many smaller utilities (often with names like
shot-scraper
, various
*-to-sqlite
tools for importing data, etc.).
That’s not bad. Here’s
the start of the response
for the exact same prompt from Fable 5—both models were running without access to search:
I think you mean
Simon Willison
— the prolific open source developer, co-creator of Django, and creator of Datasette.
An important caveat upfront: a truly complete list isn’t feasible. Simon Willison is famously prolific — he has published
hundreds
of repositories (Datasette alone has 100+ plugins, many written by him), and my knowledge has a cutoff date, so I’ll be missing his most recent work. Below are his
notable
projects with approximate initial release dates, most recent first:
Notable projects (approximate dates)
files-to-prompt
(April 2024) – concatenates files into a single prompt for LLMs
datasette-extract
(2024) – plugin for extracting structured data using LLMs
LLM
(May–June 2023) – CLI tool and Python library for interacting with large language models, plus a large ecosystem of plugins (llm-gpt4all, llm-mistral, llm-claude, etc., 2023 onward)
symbex
(June 2023) – search Python code for symbols
ttok
and
strip-tags
(May 2023) – CLI tools for token counting and HTML cleanup for LLM pipelines
datasette-lite
(May 2022) – Datasette running entirely in the browser via WebAssembly/Pyodide
shot-scraper
(March 2022) – automated website screenshots via Playwright
s3-credentials
(November 2021) – CLI for creating scoped AWS S3 credentials
django-sql-dashboard
(2021) – SQL reporting dashboards for Django
Dogsheep suite
(2019) – personal analytics tools: twitter-to-sqlite, github-to-sqlite, healthkit-to-sqlite, dogsheep-beta, etc.
sqlite-utils
(2018) – CLI and Python library for manipulating SQLite databases
Datasette
(November 2017) – his flagship project; tool for exploring and publishing data
csvs-to-sqlite
(2017) – convert CSV files to SQLite
Various early tools
(~2007–2010) – soupselect, json-head, geocoders, and others
Django
(developed 2003–2005, open-sourced July 2005) – co-created with Adrian Holovaty at the Lawrence Journal-World
(Here’s
GPT-5.5 for good measure
. It listed even more projects than Fable did!)
In the past I’ve stated that I don’t care about how much models
know
—I want them to be able to manipulate text and code in useful ways and actively look up the information they need via search tools, not bake it into their weights.
But knowledge like this is a reasonably good proxy for model size—you can cram a whole lot more details about the world into a larger number of parameters.
Does
knowing more stuff
mean the model is better at the tasks we pose to it? I can certainly imagine how a coding model with deeper knowledge of modern libraries and patterns could crunch through coding tasks more effectively.
Is Fable really bigger than Opus? Anthropic haven’t said anything about model size, so all we have are tea-leaves, but the speed, pricing and my own poking at its knowledge make me think that it’s a large model. Maybe the largest yet from any vendor.
Using Fable in Claude.ai
Anthropic made Fable 5 available across all of their surfaces—the
Claude.ai
chat interface, Claude Code for web, Claude Code CLI and Claude Cowork as well. The model is available “until June 22nd” on the subscription plans (I’m on $100/month Max at the moment), after which it will be billed extra.
Claude.ai is often under-estimated. Since
September 2025
every chat has had access to a full container environment to run code, including the ability to install additional packages and even clone repositories directly from GitHub.
Last week
I released micropython-wasm
, a Python library that uses
wasmtime
to run a custom build of MicroPython in WebAssembly to act as a sandbox for untrusted Python code.
I decided to see if Fable could upgrade that to running full Python instead. I started with this prompt:
Clone simonw/micropython-wasm from GitHub and research how this could use a full Python as opposed to MicroPython
Fable identified that it could use Brett Cannon’s
cpython-wasi-build
builds for this, but was unable to download them itself due to environment restrictions.
So I grabbed the two zip files from that page and uploaded them to Claude:
Here's the Brett Cannon builds
(
python-3.zip
,
_build-python-3.zip
as attachments)
And that was that. It churned away for a few minutes and got the entire thing working.
Part of the response included:
I tried the cleaner single-zip-stdlib approach to shrink the filesystem surface, but CPython’s
getpath
bootstrap fails to find
encodings
from inside a zip without more prefix finessing — the directory-preopen approach works reliably, so that’s what the PoC uses. The zip path is solvable but needs
_PYTHONHOME
/frozen-getpath work.
So I said:
Try a bit more at the single-zip-stdlib problem
Then a little later:
I want a wheel that has the whole system in it, the Python wrappers and the WASM files and the stdlibrary, so I can do uv run --with path-to-whl python -c "demo code"
... and it gave me
this 13.9MB cpython_wasm-0.1.0-py3-none-any.whl
file. You can try running Python code in a sandbox using that wheel URL and
uv
like this:
uv run --with https://static.simonwillison.net/static/cors-allow/2026/cpython_wasm-0.1.0-py3-none-any.whl \
  cpython-wasm -c
'
print(45 ** 56)
'
Here’s
the full chat transcript
.
This was a
very
strong start.
Adding features to Datasette Agent and LLM using Claude Code
Before I’d realized it was Fable day, my stretch goal for today was to add a new feature to
Datasette Agent
: I wanted tool calls within that agent software to gain the ability to pause mid-execution and request approval directly from the user.
This felt like a suitably meaty task to throw at the new model.
Over the course of the day Fable not only
solved that problem
, it also identified and then implemented four issues in my underlying LLM library that would help support this kind of advanced pause-resume mechanism in tool calls.
It got everything working first using somewhat gnarly hacks, but the moment I told it that changes to LLM itself were in scope it set to work unraveling the hacks and turning them into supported features of LLM instead.
My stretch goal turned into
LLM 0.32a3
, almost entirely written by Fable. Here are the release notes:
Driven by the needs of
Datasette Agent
’s human-in-the-loop
ask_user()
feature, made the following improvements to how tool calls work:
Tool implementations can declare a parameter named
llm_tool_call
in order to be passed the
llm.ToolCall
object for the current invocation. This allows them to access the current
llm_tool_call.tool_call_id
. See
Accessing the tool call from inside a tool
.
#1480
Every tool call is now guaranteed a unique
tool_call_id
—providers that do not supply one get a synthesized
tc_
-prefixed ULID.
#1481
Tools can raise a
llm.PauseChain
exception to cleanly pause the tool chain, useful for things like waiting for human approval. The exception propagates to the caller with
.tool_call
and
.tool_results
(completed sibling results) attached, and no model call is made with a placeholder result. See
Pausing a chain from inside a tool
.
#1482
Failure semantics for concurrent tool execution: async sibling tool calls always run to completion before a pause or hook exception propagates.
#1482
Chains can now resume from a
messages=
history ending in unresolved tool calls: the calls are executed through the normal
before_call
/
after_call
machinery before the first model call, skipping any that already have results. The
execute_tool_calls()
method also accepts a new optional
tool_calls_list=
argument for executing an explicit list of
ToolCall
objects in place of the calls requested by the response. See
Resuming a chain with pending tool calls
.
#1482
Fixed a bug where the async tool executor silently dropped calls to tools not present in
tools=
—these now return
Error: tool "..." does not exist
results, matching the sync executor.
#1483
I’m really impressed with the quality of API design, tests, code and documentation that Fable put together for this. I spent several hours on it today, but it feels like several days’ worth of work.
How much I’ve spent
I recently started using
AgentsView
to help track my local LLM usage across all of the different coding agents. I published a
TIL today
about adding custom Fable pricing to that tool, which I expect will not be necessary in the very near future.
After setting the price, I ran this command to start a localhost web server to explore my usage:
uvx agentsview serve
Here’s the treemap showing the breakdown of my Fable usage across various projects today:
I used $110.42 worth of tokens today, all as part of my $100/month subscription.
And some pelicans
I ran “Generate an SVG of a pelican riding a bicycle” against all five thinking effort levels with Fable.
Here are
the results
, including the token cost for each one:
low:
1,929 out, 9.67c
medium:
2,290 out, 11.475c
high:
2,057 out, 10.31c
xhigh:
5,992 out, 29.985c
max:
14,430 out, 72.175c
It’s interesting that high ended up using fewer tokens than medium for this particular run.
Here are the
Opus 4.8 pelicans
for comparison.
