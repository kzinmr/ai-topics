---
title: "Agent Platforms for Inventing Agents"
url: "https://hyperbo.la/w/agent-platform/"
fetched_at: 2026-09-06T10:01:20.931593+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Agent Platforms for Inventing Agents

Source: https://hyperbo.la/w/agent-platform/

An agent is a parameterized program over a set of capabilities.
By late 2026, the industry has started to coalesce on identifying the standard
set of capabilities that make up an agent:
A model and its configuration
An inference-and-tool-calling loop
A computer
A disk
“Context”
Skills (a named
special case of context
, due to their privilege in
post-training)
“Tools”
Connectors (a named subset of tools that are first-party provided)
Programming runtimes
Network policy
Agent identity
IAM bundle
“Guardrails”
I/O channels for steering and response
System prompt
Across the agents I’ve built and worked on, these capabilities keep showing up. Each system makes different choices about how to provide them.
Agent
Model and configuration
Inference-and-tool-calling loop
Computer and disk
Tools and context
Credentials
ChatGPT with external data connectors
gpt-4o
Harmony
Python tool
Connectors exposed as opaque file-search backends
Injected via plugin registry
Agentic data scientist
gpt-5 and gpt-5-codex snapshots; model slug changed in TypeScript and redeployed
Codex
Local computer, with the host user’s binaries
Arbitrary code against upstream providers using their native SDKs
Inherited the host user’s credentials; a credential-injecting proxy supplied upstream authentication
FDE team in a box
A combination of gpt-5, codex-mini, and gpt-5-mini; models could not be configured independently
Agents SDK v1 spawning 12 collaborating subagents
Remote server binding compute and an ephemeral disk
Hosted tool calling + TypeScript-backed local tools
None
Agentic TPM
gpt-5.4 with several gpt-5-mini subagents
Codex CLI for the main agent and subagents; small helpers also paired LLM output with fixed code
Headless execution on a cloud VM with an EBS-like block device
Tools delivered through a centralized plugin service
The plugin service injected handles to credential bundles
Agentic software engineering manager in
Symphony
A variety of GPT models
Elixir actor system delegating individual tickets to remote Codex CLI workers
Server with remote execution workers
Individual tickets supplied to coding agents
Manually provisioned
Agentic SRE in Google Cloud
Selected dynamically from Vertex based on customer config
Antigravity
microVMs or BYO compute
Offline indexing, dreaming, and distillation loops
Agent Gateway
Building a general knowledge worker agent on
Agents SDK v1
required 400,000 lines of code on top of the SDK. To let the agent execute its
tasks through code, we had to provide (and invent in the first place!) skills
for the agent, provision sandboxes and Python environments, install
dependencies, manage worktrees, and stand up credential-injecting proxies. All
undifferentiated work, but the platform had no reusable primitives for it. Some
eventually landed in Agents SDK v2 through the container and bundled skills
APIs.
Across these agents, I’ve used product development to discover concrete
implementations of that standard set of agent capabilities. We don’t know yet
which implementations will work, so the platform has to let us invent them, try
them in real products, and make the useful ones reusable.
We do not know how to build agents generally
We have figured out how to build individual agents. We have not figured out how
to generalize what it means to mint an arbitrary agent. The capabilities are
recognizable, but their implementations remain bound together inside particular
systems.
We
also
do not know the best concrete implementations, or
providers
, for
these agent capabilities. There are an infinity of ways to both curate and
provide context, no one knows which tools are good or correct, system prompts
will want online variation and task- and customer-specific overrides, etc. The
implementations that work for one agent are choices we need to be able to
revisit for the next.
Freezing those choices inside a harness puts everyone building on it at the
mercy of its authors. Every dependency hidden inside the harness is a parameter
the builder cannot bind.
1
The next experiment depends on
whether someone else anticipated it, exposed the right config knob, or is
willing to put it on their roadmap.
That limits how good an agent can become. For example, an organization cannot
make a hosted agent, like
ChatGPT Workspace Agents
or
Claude Tag
, an expert in its internal network topology if it
has no way to supply that context. The organization may have the information and
know how to prepare it, but the agent cannot use it. The missing interface
prevents the people who understand the task from making the agent good enough to
do it.
2
It also limits where agents can be used. An organization may know the controls
and policies it requires and have the engineering capacity to implement them. If
the harness cannot accept those controls, adoption is blocked on the harness
owner’s priorities.
These are consequences of the same architectural choice. The capability is
present, but the builder cannot supply the implementation. An agent platform has
to give builders that freedom across the entire agent. An agent platform has to
standardize and open up the seams.
Define capabilities and leave their implementations open
An agent platform, then, must do several things:
Define the capabilities.
Provide the most smooth-brained, low-level, flexible RPC contract that can be
used to fulfill the capability.
Provide zero privilege to concrete implementations of the capabilities the
platform provides.
Provide composition primitives for concrete implementations of capabilities,
such as merge and overlay.
Act as a microkernel: invoke and compose the capability providers just in
time to mint a trajectory with governance guarantees.
Notably, in this model, the agent platform is not itself an agent. It is the
system for minting agents from compositions of capabilities.
First-party providers use the same contracts as everyone else. This keeps the
platform loosely coupled: it depends on the capability interfaces, and each
provider owns its implementation. Shipping a provider does not make its
implementation choices part of the platform’s contract.
These interfaces are incredibly low level and composable. A computer could be
local execution on the same machine, an LXC on some random desktop, a
Firecracker VM, gVisor, a remote Cloud Run instance, or a node pool in your own
Kubernetes cluster. Disk does not even specify a filesystem. The contracts leave
those implementation decisions to the providers.
Context could be an in-memory filesystem, a static list of files, a GCS bucket
that you should splat to disk, a tarball, or a slice of cross-agent
LLM
wikis
hydrated just in time by intersecting an agent’s learned blast
radius with a world model. Each requires different work to make the context
available. If the platform makes a particular file loader the context interface,
every other source has to fit through that loader’s assumptions. A provider
contract lets the builder supply that work and compose its output with the
selected computer and disk.
The harness that does inference and tool calls in a loop is itself one of the
capabilities! It could be
ADK
,
OpenAI Agents SDK
, a coding
agent harness like
Antigravity
,
Codex
,
Claude
Code
,
Pi
, or a system that separates the loop from the
microVM executing tool calls. A model and its configuration are another
capability. Choosing the loop should not also choose the model, the computer,
and the policies under which it operates.
This means neither Codex nor Claude Code nor Pi is an agent platform in this
model. They freeze at least one of these capabilities as part of the harness,
putting builders at their mercy to provide the config knobs they need. They can
be useful implementations to compose into an agent. Their integration limits
should determine where that implementation can be used, rather than define the
limits of the whole platform.
Mint the agent from a composition
To define an agent is to define which provider RPCs to hit and how they compose
together. To spawn it is to supply the parameters passed to those RPCs to enable
just-in-time resolution. The wiring is a program for constructing the agent.
Providers can themselves be composed from other providers. End products should
own their system prompts. Skills can be fetched from multiple places or
just-in-type synthesized by agents. A tool provider can obtain a manifest from
another provider, fetch the binaries, verify their checksums, and splat them
into the bin directory. These choices can be expressed in the wiring, before any
particular execution is requested.
In Starlark-style pseudocode, provider constructors configure that composition:
agent
=
wiring(
model
=
VertexProvider(),
loop
=
CodexProvider(),
computer
=
KubernetesProvider(
cluster
=
"..."
,
node_pool
=
"..."
),
disk
=
SnapshotDiskProvider(
snapshot
=
"..."
),
context
=
merge(
InMemoryFilesystemProvider(
files
=
{
...
}),
GCSTarballProvider(
bucket
=
"..."
,
object
=
"..."
),
),
skills
=
overlay(
merge(
SFTPProvider(
host
=
"..."
,
path
=
"..."
),
GitProvider(
repo
=
"..."
,
ref
=
"..."
),
),
CustomerSkillsProvider(),
),
system_prompt
=
AiStudioPromptProvider(),
tools
=
merge(
MCPRegistryProvider(
registry
=
"..."
,
selector
=
{
...
}),
BinaryManifestProvider(
manifest
=
GCSProvider(
bucket
=
"..."
,
object
=
"..."
),
require_checksums
=
True
,
install_dir
=
"/usr/local/bin"
,
),
OpenAPIProvider(
spec
=
"..."
,
credentials
=
CredentialProxyProvider(),
),
),
guardrails
=
compose(
ParameterClampProvider(
limits
=
{
...
}),
JudgeProvider(
model
=
BedrockProvider(
model
=
"gpt-oss-safeguard"
),
rubric
=
"..."
,
),
TwoPartySignoffProvider(),
ToolCallBudgetProvider(
calls
=
20
,
on_exhaustion
=
HumanElicitationProvider(),
),
),
)
agent.spawn(
customer
=
"Yezzir"
,
user
=
"lopopolo"
,
task
=
"Assess the quality of this system as bbno$ would."
)
Constructing the provider objects defines how to resolve the capabilities.
Calling
spawn
supplies the customer, user, and task, and triggers that
resolution. The platform invokes the provider RPCs with the relevant inputs and
composes their results to instantiate the agent. A binding can resolve to a
value, an allocated resource, or a service used during execution.
The prompt provider could just be an API served by the product implementing the
agent. A product like AI Studio could use it to inject learned memory from the
last ten conversations into the system prompt. It could also run Mendel
experiments or apply customer overrides. The agent platform has no knowledge of
memory or experiments; it invokes the provider with the parameters supplied at
spawn and gets back a system prompt. The product team owns how that prompt is
produced and can improve it without needing anything from the platform team.
Composition makes new behavior possible
The value of this decomposition is that builders can produce behavior the
platform authors have not implemented.
Compaction is one example. You might consider
compaction
and other
long-horizon task-enabling behaviors to be capabilities. However, the proper way
to think about this is that compaction is just a tool you are giving to your
agent. We will want post-training and model hill climbing to include its ability
to learn when to compact so that it can perform well over long-horizon
trajectories.
The compaction tool can be (but does not have to be!) backed by another agent,
composed from the same pieces. The working agent decides when to call it. The
compaction agent uses its own model, prompt, context, and tools to produce the
context needed to continue. The loop supports using that result for subsequent
inference.
This gives builders control over both when compaction happens and how it works.
They can improve those choices against performance on long-horizon tasks.
Compaction does not have to remain bound to a first-party model family and
harness, and the platform does not have to ship a privileged compaction
implementation before anyone can experiment.
A tool backed by an agent is another parameterized program over capabilities.
The same construction works recursively. We can discover useful behaviors by
composing the pieces we already have.
Customers control the conditions of autonomy
Working on an
agentic SRE
, I learned that customers enable autonomy against a
set of controls they trust. They want to lock in, or have attestations around,
the guardrails and bright lines under which the agent can act. A model or
harness upgrade should not silently change the conditions they approved.
Auto mode
is a useful example. An LLM judge can approve or deny tool calls
against a rubric. Antigravity does not expose an auto mode; Codex and Claude Code
do not let the builder inject an arbitrary rubric or judge into theirs. The
harness author therefore gets to define the policy boundary of autonomous
execution. An agent platform should let the builder bind that policy
independently of the loop.
Those controls belong in the customer’s context and can be served through an API
the customer controls. The organization can supply its
rubric, judge, and
approval mechanisms
, then evolve that composition through its own processes.
The platform needs to let those controls govern execution without requiring the
agent builder to implement each customer’s policy.
This lets the agent builder continue to improve the capability and quality of
the agent while the customer remains in control of its safety and compliance
posture. The customer decides when and how its operating boundaries change,
through its own processes.
Structure the platform itself this way
No one knows how to build agents generally. If concrete implementations remain
privileged inside the platform, everyone building on it has to wait for its
authors to decide what to support. Structuring the platform itself around
composable providers distributes that work across teams and companies. Teams
focused on agent quality can throw a ton of things at the wall, evaluate them,
and hill climb rapidly without turning every experiment into a platform feature
request. What works becomes available for other builders to compose and improve.
This is as much a way of operating as a systems architecture: the platform makes
experimentation possible without requiring its authors to anticipate the
results.
Every interface the platform defines, every implementation it ships, and every
provider a builder supplies is in service of minting a trajectory so the agent
can do a thing.
