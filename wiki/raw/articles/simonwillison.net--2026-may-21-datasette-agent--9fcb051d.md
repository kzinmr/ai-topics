---
title: "Datasette Agent"
url: "https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything"
fetched_at: 2026-05-22T07:01:11.067503+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Datasette Agent

Source: https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything

Datasette Agent
21st May 2026
We just
announced the first release of Datasette Agent
, a new extensible AI assistant for Datasette. I’ve been working on my
LLM
Python library for just over three years now, and Datasette Agent represents the moment that LLM and
Datasette
finally come together. I’m really excited about it!
Datasette Agent provides a conversational interface for asking questions of the data you have stored in Datasette. Add the
datasette-agent-charts
plugin and it can generate charts of your data as well.
The demo
The
announcement post
(on the new Datasette project blog) includes this
demo video
:
I recorded the video against the new
agent.datasette.io
live demo instance, which runs Datasette Agent against example databases including the classic
global-power-plants
by
WRI
, and a copy of the
Datasette backup
of my blog.
The live demo runs on
Gemini 3.1 Flash-Lite
—it’s cheap, fast and has no trouble writing SQLite queries.
A question I asked in the demo was:
when did Simon most recently see a pelican?
Which ran
this SQL query
:
SELECT
title, commentary, created
FROM
blog_beat
WHERE
beat_type
=
'
sighting
'
AND
(title
LIKE
'
%pelican%
'
OR
commentary
LIKE
'
%pelican%
'
)
ORDER BY
created
DESC
LIMIT
5
And replied:
The most recent sighting of a pelican by Simon was recorded on
May 20, 2026
.
The observation included a California Brown Pelican, along with a Common Loon, Canada Goose, Striped Shore Crab, and a California Sea Lion.
Here’s
that sighting on my blog
, and the
Markdown export
of the full conversation transcript.
The plugins
My favorite feature of Datasette Agent is that, like the rest of Datasette, it’s extensible using plugins.
We’ve shipped three plugins so far:
Building plugins is
really fun
. I have a bunch more prototypes that aren’t quite alpha-quality yet.
Claude Code and OpenAI Codex are both proving excellent at writing plugins—just point them at a checkout of the
datasette-agent repo
for reference and tell them what you want to build!
Running it against local models
I’ve also been having fun running the new plugin against local models. Here’s a
uv
one-liner to run the plugin against
gemma-4-26b-a4b
in
LM Studio
on a Mac:
uvx --prerelease=allow \
  --with datasette-agent --with llm-lmstudio \
  datasette --internal internal.db --root \
  -s plugins.datasette-llm.default_model lmstudio/google/gemma-4-26b-a4b \
  data.db
Datasette Agent needs reliable tool calls and the ability for a model to produce SQL queries that run against SQLite. The open weight models released in the past six months are increasingly able to handle that.
What’s next
Datasette Agent opens up
so many
opportunities for the LLM and Datasette ecosystem in general.
It’s already informed
the major LLM 0.32a0 refactor
which I’m nearly ready to roll into a stable release, maybe with some additional “LLM agent” abstractions extracte from Datasette Agent itself.
I’ve been exploring my own take on the Claude Artifacts, which is shaping up nicely as a plugin.
I’m excited to use Datasette Agent to build my own
Claw
—a personal AI assistant built around data imported from different parts of my digital life, which is a neat excuse to revisit my older
Dogsheep
family of tools.
We’ll also be rolling out Datasette Agent for users of
Datasette Cloud
.
Join our
#datasette-agent Discord channel
if you’d like to talk about the project.
