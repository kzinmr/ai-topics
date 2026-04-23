---
title: "Tangle: An open-source ML experimentation platform built for scale (2025)"
url: "https://substack.com/redirect/2afd5c29-762b-4e90-9bee-75351d8890a3?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-23T05:08:29.535438+00:00
source_date: 2026-04-22
tags: [newsletter, auto-ingested]
---

# Tangle: An open-source ML experimentation platform built for scale (2025)

Source: https://substack.com/redirect/2afd5c29-762b-4e90-9bee-75351d8890a3?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

By Alexey Volkov, Staff Engineer, Search Product & Tooling
Jump to getting started
Your experiment finally finished. Six hours later, your teammate asks you to reproduce it. You can't remember which notebook version you used, whether you pulled fresh data, or what parameters you changed at 2 a.m. Now you're looking at another eight-hour run, just to
maybe
reproduce what you already did.
Machine learning development shouldn't work this way, but it does.
80% of development time is spent on data engineering
, not algorithms.
Teams all across Shopify felt this pain, especially
Search & Discovery
which ranks millions of products across billions of queries. We couldn't afford this friction.
So we built
Tangle
: an ML experimentation platform we’ve battle-tested at commerce scale. Since using it, we’ve racked up more than a year of compute time savings.
Today, we open-sourced the platform.
Why we're open-sourcing Tangle
Shopify's Search & Discovery team built Tangle (originally Cloud Pipeline Studio, a tool I built before joining Shopify) to accelerate ML experimentation without sacrificing reliability.
Tangle is proving to be useful for teams all across Shopify. It works at our scale. Data scientists iterate faster. Engineers maintain less custom pipeline code. Team members share pipelines and runs. Infrastructure costs decrease through global caching.
Shopify is committed to making the web as good as it can be through open-source contributions. We know the broader ML community faces identical challenges to us, so open-sourcing Tangle was a no-brainer. This way, we can extend Tangle’s impact and invite collaboration from researchers and practitioners worldwide.
The problem: Six ML development failure modes
Engineers must remember each custom query they write
for each experiment, keeping a log to track which query was used at which stage, causing mistakes and slowdowns.
Notebooks accumulate
without structure.
Hours-long data preparation
for experiments is frequently repeated.
Can't recreate
old results.
Deployment takes longer
than training.
There’s no sharing.
A team member can’t help or try their own variants.
Most platforms solve for some of these failures and not others. We decided to try and tackle them all with Tangle.
Our solution: Visual pipelines + any code
Tangle is an open-source, platform-agnostic experimentation platform that enables teams to build ML and data pipelines through a visual interface, and execute them in cloud environments without requiring local development setup.
Some existing tools can only do specialized data-processing, or can only do ML training, but Tangle can do all of that in a single pipeline in any combination—along with any other unconventional processing you need. It even handles non-processing tasks like deploying models, using human judges to acquire result labels, and calculating human-based metrics.
Think of Tangle as the glue that connects everything in your workflow, no matter how mismatched, whether you're bridging components written in different languages or integrating tools that weren't designed to work together.
The platform is architected around these foundational principles:
Platform agnostic
Tangle integrates with existing codebases across any programming language and executes on any cloud provider or local infrastructure without requiring code modifications.
Robust caching
The system tracks task executions and their artifacts, enabling automatic reuse of duplicate computations across all pipeline runs from team members. Results that took hours to produce are automatically reused from cache in seconds. And unlike other systems, Tangle can reuse not only fully succeeded task executions, but also still-running ones.
Visual pipeline editing
Developers construct pipelines through an interactive drag-and-drop interface that renders the complete data flow as a directed acyclic graph (DAG), providing immediate visibility into pipeline structure without parsing notebook code.
Language-neutral architecture
Tangle components wrap arbitrary existing command-line programs that read and write files (rather than requiring the user to rewrite their code with some framework-specific constructs). It supports components written in Python, Shell, Javascript, C#, C++, Rust, Java, Go, R, or any language capable of CLI execution.
Architecture: How Tangle works
Tangle's architecture follows a simple hierarchy:
Component:
Conceptually similar to a function definition—reusable specification that describes component metadata (name, description, annotations), interface (inputs/outputs), and implementation (a templated command-line of a containerized CLI program, or a graph of tasks)
Task:
Conceptually similar to a function call line in code—configured instance of component with specified input arguments
Execution:
Conceptually similar to a function invocation—when you submit a pipeline, each task executes and produces output artifacts
Graph:
A graph of connected tasks where outputs from one task are passed to another task as inputs
Pipeline:
A root graph component; its implementation is a graph of tasks
This declarative model provides advantages over code-centric approaches. Components are plain-text YAML files that can be organized into libraries, indexed, searched, and safely loaded from any source (GitHub, web, or cloud storage). Unlike Python packages installed globally, components can be versioned independently—users can reference exact versions by content hash, mix different component versions in the same pipeline for comparison, and share specific component versions without dependency hell.
Components: Reusable building blocks
A component is a self-contained unit of functionality defined by a YAML specification. Components follow a clear contract: they accept inputs, perform a specific task, produce outputs, and run in complete isolation.
Here’s an example component specification:
Components are designed as pure functions: deterministic (identical inputs produce identical outputs) and free from side effects. This enables effective caching and artifact reuse.
Language-agnostic design
Tangle components describe arbitrary containerized CLI programs that do not need to be aware of Tangle at all. This provides three advantages:
Language neutrality:
Write components in any language that supports CLI execution.
Distributed orchestration:
Components execute on different machines at different times without shared runtime requirements.
Clear isolation:
Containers allow hermetic execution without state pollution.
Since a container component describes an arbitrary CLI program command line, users can create components based on small inline scripts without the need to put user code inside a container.
Here’s an example of an inline Python script component (Note that for Python developers, there's a feature called Lightweight Python Component Generator which generates such components automatically. So, here we’re just demonstrating the concept.):
Here’s an example of an inline JavaScript script component:
Content-based caching
Most ML platforms use lineage-based caching. When upstream components change, all downstream components must re-execute. Tangle uses content-based caching instead: downstream components check output content hashes and reuse cached results when outputs remain identical. This leads to some major performance improvements:
Real-world impact:
A 10-hour pipeline completes in 20 minutes when only one component changes. The outputs are identical.
Global artifact reuse:
Tangle's cache operates globally across all users. When three data scientists submit experiments sharing a preprocessing step, Tangle executes preprocessing once and all three pipelines share the artifact—even for still-running executions.
Data flow architecture
Tangle components communicate through file paths, not in-memory objects:
Producer writes
to local path
System uploads
to storage (GCS, S3, etc.)
Consumer reads
from local path
System retrieves
transparently
The system replaces placeholders with actual file locations at runtime. Components implement standard file input/output while storage remains abstracted.
Execution flow
When you submit a pipeline, Tangle's orchestrator manages execution automatically:
Queue tasks:
Each task starts in a queued state.
Check dependencies:
Wait for upstream tasks to complete and verify input artifacts are available.
Check cache:
Calculate execution cache key and search for reusable executions (succeeded or still running).
Execute or reuse:
If cache hit, reuse existing results. Otherwise, launch container in cloud cluster.
Monitor:
Track container status, capture logs, and update execution state.
Finalize:
Store output artifact metadata (size, hash, small values) and signal downstream tasks.
This happens automatically. You submit, the system orchestrates, you monitor results.
Optional type system
Tangle uses optional typing—types provide metadata for tooling but aren't enforced. That means:
Components specify their I/O types
(String, Float, JsonObject, ApacheParquet, TensorflowModel). Type names can be arbitrary, but should be used consistently.
System treats all artifact data as opaque blobs/strings
(or directories).
There is no centralized data validation
—the consuming components validate their own inputs.
Here’s our design rationale:
Openness:
Any user/team can declare their own specialized types
Performance:
No runtime validation overhead
Security:
No parsing vulnerabilities from centralized validation
Flexibility:
Version compatibility without rigid schemas
Visual editor: Pipeline development
Tangle renders pipelines as interactive directed acyclic graphs (DACs), eliminating the need to parse notebook code.
Build visually
Add
components from library
Connect
outputs to inputs
Configure
parameters inline
Submit
with one click
Monitor in real-time
Track
task execution status
View
artifacts and logs
Identify
cached steps
Spot
performance bottlenecks
Iterate rapidly
Every run is preserved with complete lineage. This allows fast iteration without losing experiment history.
Getting started
Tangle’s architecture allows it to run anywhere. We’re expanding the list of installation recipes.
At this moment, Tangle can be used locally (using Docker/Podman launcher) or at HuggingFace (using HuggingFace Job launcher).
Start with HuggingFace
The easiest way to try Tangle is via HuggingFace.
Go
here
and start building. Creating a pipeline does not require any registration, but to run your pipeline, you’ll need a HuggingFace account with
Pro
subscription ($9/month).
Build a pipeline
Start with the sample XGBoost training pipeline or build a new one from scratch:
Drag
components onto canvas
Connect
components (outputs to inputs)
Configure
task arguments
Submit
pipeline for execution (requires login)
Monitor
the pipeline run in real-time
Edit a pipeline:
Monitor a pipeline run:
See the list of all your pipeline runs:
HuggingFace x Tangle integration
We've deployed Tangle to HuggingFace Spaces as a multi-tenant service, which uses HF infrastructure for storage, compute, and authentication.
The shared multi-tenant instance is live
here
.
Tangle’s multi-tenant architecture maintains a central tenant database (storing user IDs, access tokens, and orchestrator configs) plus individual per-tenant SQLite databases in the main TangleML/tangle HuggingFace Space persistent storage. Each user’s pipelines run via that user’s HuggingFace Jobs, and the execution logs and output artifacts are stored in the user's own private HuggingFace Dataset repo (user/tangle_data), with clickable links in the UI to both artifacts and HuggingFace Jobs.
You can also deploy your own single-tenant instance. You do this by duplicating the Tangle space to your HF account and providing an
HF token
. These single-tenant Tangle deployments store their database in your own HF Space persistent storage, giving you complete control and data isolation.
If you clone Tangle to an organization, you’ll get a single-tenant multi-user Tangle deployment for your team, where multiple team members can see eachother’s pipeline runs and enjoy org-wide cache.
Start locally
Follow the installation instructions on
GitHub
.
Install
Docker
and
uv
.
Download the app code
(needs to be done once):
Start the app:
Linux and Mac OS:
cd tangle && backend/start_local.sh
Windows:
cd tangle && backend\start_local.cmd
Open the
http://localhost:8000
URL
in a web browser o
nce the "
start_local: Starting the orchestrator
" message appears in the terminal, and start using the app.
Click the "New Pipeline" button
at the top to start building a new pipeline.
Why choose Tangle
Tangle was built to make machine learning better for teams and individuals.
For organizations
Automatic tracking and reproducibility:
Every pipeline run is recorded with complete lineage: graph structure, execution logs, artifact metadata, and metrics. Intermediate data is immutable and never overwritten, de-risking experimentation and enabling safe sharing across teams. Team members can clone any colleague's pipeline run, investigate issues, modify parameters, and resubmit—all tracked automatically.
Time and compute savings:
Previously executed tasks are reused automatically through content-based caching, saving both execution time and cloud costs.
Component libraries:
Teams build shared libraries of reusable components, establishing consistent patterns and accelerating development velocity.
Accessible to non-engineers:
Product managers and analysts can create and run pipelines without writing code or setting up development environments, enabling them to run experiments and track metrics independently.
For individual engineers
Zero-friction tracking:
Automatic versioning and execution history without manual bookkeeping.
No manual caching:
Data passes between transformations automatically with intelligent reuse—no custom caching logic required.
Non-intrusive integration:
Components wrap existing code without modification, using any CLI program, language, or container.
Composable knowledge:
Components are self-contained bits of reusable knowledge: each behaves like a simple function, not a complex framework. Forgot how to write a TensorFlow training loop? Reference a 50-line component instead of parsing a 1,000-line tutorial. Components are independent, which means no dependency conflicts, and can be shared across multiple pipelines even while using different versions simultaneously for comparison.
Language interoperability:
Connect Python, Java, Shell, Ruby, C++, and JavaScript components in the same pipeline without compatibility issues.
Battle-tested at Shopify scale
Tangle powers production ML infrastructure for Shopify's Search & Discovery team and many others, processing millions of search queries and billions of products. We use it for:
Product ranking models
across millions of SKUs
Semantic search experimentation
at query scale
Recommendation system training
Real-time feature engineering pipelines
Measured benefits
Iteration velocity:
Data scientists deploy new ranking models daily without infrastructure dependencies
Complete reproducibility:
Any experiment from six months ago can be recreated in two clicks with full artifact provenance
Cost optimization:
Global caching eliminates thousands of redundant compute hours monthly
Team collaboration:
The shared component library accelerates development and establishes consistent patterns
What's next
Tangle runs at production scale at Shopify. We're prioritizing future features based on community feedback.
Planned features
Direct support for major clouds
(GCP is already supported, but needs deployment documentation)
Expanded and enhanced component library
Artifact visualization
Get involved
⭐
Star us
on
GitHub
📖
Read
the
docs
💬
Join discussions
on
GitHub
🐛
Contribute:
Issues
and
PRs
welcome
This is just the beginning. We're excited to see how the ML community shapes Tangle’s future. Try it on your workflows, share your feedback, and help us build the best experimentation platform together.
If you’re interested in joining us on our mission to make commerce better for everyone, check out our
careers page
.
Alexey Volkov is a Staff Engineer on the Search Product & Tooling team.
