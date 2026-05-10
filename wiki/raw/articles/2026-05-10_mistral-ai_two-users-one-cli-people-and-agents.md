---
title: "Two users, one CLI: people and agents"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/two-users-one-cli-people-and-agents"
scraped: "2026-05-10T01:20:21.854501+00:00"
lastmod: "2026-04-21T20:32:48.402Z"
type: "sitemap"
---

# Two users, one CLI: people and agents

**Source**: [https://mistral.ai/news/two-users-one-cli-people-and-agents](https://mistral.ai/news/two-users-one-cli-people-and-agents)

Two users, one CLI: people and agents
Engineering
Designing for agents forced us to build better tools, starting with our internal ones.
Mar 31, 2026
Mistral AI
Most developer tools start the same way. You need to do a thing repeatedly, so you write a script. The script grows flags. The flags grow subcommands. Before you know it, you've got a CLI.
We had this exact experience when building an internal platform tool to help our solutions team ship faster. It scaffolds projects, spins up dev environments, generates configs, and deploys to staging.
As our CLI grew in scope, so did the number of our internal users. But then, something interesting happened: suddenly, we were no longer building just for human developers, but for coding agents too.
What Good DX Looks Like
Before we talk about agents, let's talk about what makes a CLI actually pleasant for human developers.
Spaces is opinionated about the boring stuff. It picks sane directory structures so you don't have to. It generates the config files you'd otherwise copy from the last project. It wires services together so your API and your frontend can talk on day one, not after an hour of YAML editing or “vibing”.
Here's what a typical session looks like:
$
spaces init my-project
$
cd
my-project
$
spaces dev
Three commands. You go from nothing to a running multi-service project with hot reload, a database, and generated Dockerfiles. That's the bar.
The commands that matter tend to fall into three buckets:
Scaffolding
-- These create structure, ask questions, show options, let you explore.
Development
-- These are your inner loop. They just “run”.
Operations
-- These touch production. Careful, double-check before acting
This is all table stakes. But then our second user showed up and we discovered we needed something a little different, and a lot more interesting.
The Second User: The Agent
We built a TUI module picker for
init
. Fancy changes, commands, it looked super.
Then an agent tried to use it.
The agent saw raw ANSI escape codes.
\\\\x1b[36m?\\\\x1b[0m Select components
. It couldn't send arrow keys or toggle selections. It was locked out of the command entirely.
The fix seems obvious in retrospect: add a
--components
flag. But the real insight was bigger than one flag.
Every prompt is a flag in disguise
Every time your CLI asks an interactive question, there's an implicit contract: "I need this piece of information to proceed." To fulfill that contract, you can use an interactive prompt. Or you can use a flag or config file.
The trick is to think about the
information
first and the
input method
second.
def
init_command
(
components:
str
|
None
= Option(
None
),
yes:
bool
= Option(
False
,
"-y"
),
):
if
components:
selected = components.split(
","
)
elif
yes:
selected = get_defaults()
else
:
selected = show_picker()
# Same logic from here
create_project(selected)
Three input paths, one execution path. The business logic doesn't know how the inputs arrived. This means you test it once, not three times.
The
-y
flag deserves special attention. It's not just "skip confirmations." It's a contract that says:
I'm providing everything you need programmatically, don't block on stdin.
When you run with
-y
, every prompt resolves to either a flag value or a smart default. If it can't, it fails loudly instead of hanging.
Example in practice: the interactive elements in this post.
The elements were built in a fresh repository. An agent was retroactively asked to wire the project into [spaces cli] for deployment. It started by running
--help
across the relevant commands to understand the interface. From that, it figured out which configuration files were needed, generated a
config.yaml
, and connected the Dockerfile and registry settings - no hand-holding required.
In the same pass, it set up the GitHub Actions CI pipeline. From a single prompt to a live deployment took under 10 minutes (a cycle time we're actively working to bring down). After that, the repository was fully configured and the embeds were
deployed
with
Koyeb
— as a Space, scaffolded and deployed through Spaces itself. Yes, the interactive demos embedded in this blog post about Spaces are running as a Space.
Spaception
.
Because every interactive input had a flag equivalent, the agent could operate autonomously end-to-end.
Structured Data as Interface
The CLI our team was building helped our applied AI engineers ship apps. But not every app looks the same. Some need a backend and a vector database. Others just need a relational database, a frontend, and some APIs. A few are worker-only services with no UI at all.
We were not about to hardcode the module types. So we built a plugin system where each component is a plugin that declares its own properties:
class
ModulePlugin
(
BaseModel
):
type_id:
str
category:
str
default_port:
int
def
get_env_vars
(
self
) ->
list
[EnvVarDef]:
...
def
get_dev_command
(
self, port:
int
) ->
str
:
...
Plugins are introspectable. You can list them, serialize them, diff them. A human browses a TUI picker. An agent queries the registry and gets JSON back. Same data, different rendering.
This accidentally solved a problem we didn't know we had. Before, adding a new module type meant updating the picker, the Dockerfile generator, the env file writer, and the compose template. Now it means writing one plugin class. The registry is the single source of truth and everything reads from it.
Teaching Agents About Your Project
There's an old saying that content is king. With agents, context is.
The most impactful thing we did for agent usability was generating two files on every
init
:
context.json
-- a structured snapshot of the project: what modules exist, ports they use, commands to run, env vars they need.
AGENTS.md
-- a set of rules written for LLMs and more imperative than your regular one. Not "this project uses PostgreSQL" but "run
mycli dev --migrate
before testing database changes."
An agent that reads these files before acting makes dramatically fewer mistakes. Basically, it won’t guess at port numbers, run the wrong test command, try to install dependencies that are already managed by the toolchain.
The context file also acts as a cache-buster for stale agent assumptions. When you add a module or change a deploy target, the context file updates automatically on the next
dev
or
init
. The agent reads fresh state every time.
Implicit State is the Enemy
The subtlest problem we hit was implicit state. Our
add
command read
config.yaml
from the current working directory. A human
cd
s to the right folder without thinking. An agent running commands from a workspace root has no idea it needs to be in a subdirectory.
The fix:
# Before: CWD dependency
config = load_config(Path.cwd() /
"config.yaml"
)
# After: explicit with fallback
config = load_config(
path
or
find_config_in_parents(Path.cwd())
)
Every hidden assumption -- CWD, environment variables, dotfiles in
$HOME
-- is a place where an agent will trip. Explicit parameters with sensible fallbacks solve it for agents and make scripting easier for humans too.
The Checklist
Looking back, the changes were small individually. Just a set of principles applied consistently:
Every interactive input has a flag equivalent
Every flag has a smart default for headless mode
State is explicit. CWD, env vars, and config paths are inputs, not assumptions
Plugins are data models, not just code. Introspectable by default
Context files give agents (and CI, and scripts) a structured description of the project
Building a Better Tool for Everyone
The funny part is that none of this made the CLI worse for humans. The TUI picker still works and looks fancy, progress spinners still spin, confirmation dialogs still confirm. We just added a second door.
And that second door turned out to be the more important one. Not because agents matter more than humans, but because the constraints they impose are the same constraints that make a CLI composable, scriptable, and testable. Designing for agents forced us to build a better tool for everyone.
If you're building developer tools right now, you don't need a separate agent API. You need to look at every
input()
call, every CWD assumption, every pretty-printed-only output, and ask: what if the user on the other end is a process, not a person?
The answer to that question will improve your tool either way.
Spaces CLI is built by Lorenzo Signoretti, Riwa Hoteit & Sam Fenwick at Mistral AI. Special thanks to our Applied AI team, the earliest and most demanding users of the CLI, whose real-world usage shaped every pattern described here. We're excited to see the applications it will help them build with our Customers to solve painful use cases.
The tooling layer between humans and agents is still being figured out. If building developer tools at the intersection of AI and infrastructure sounds like your thing,
we’re hiring
.
Share this article
More from Mistral AI
News
Models
AI Services
