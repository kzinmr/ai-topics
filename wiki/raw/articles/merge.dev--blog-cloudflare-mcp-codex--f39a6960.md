---
title: "How to connect a Cloudflare MCP with Codex (4 steps)"
url: "https://www.merge.dev/blog/cloudflare-mcp-codex"
fetched_at: 2026-06-25T07:01:41.119744+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# How to connect a Cloudflare MCP with Codex (4 steps)

Source: https://www.merge.dev/blog/cloudflare-mcp-codex

When you hand Codex a task to scaffold a Worker or write a DNS migration, you usually describe your Cloudflare setup in the prompt.
That description rarely matches the real account. The actual zone config, the existing DNS records, the KV namespaces, and the route bindings are details a summary skips.
So Codex generates a deploy script that assumes the wrong routes, a migration that misses records, or KV code that doesn't match the real namespace. The source of truth lives in your Cloudflare account, not in the few lines you wrote into the task.
To give Codex direct access to Cloudflare as it works through your coding tasks, we'll show you how to connect Cloudflare with
Merge Agent Handler's Cloudflare MCP server
.
How it works
Merge Agent Handler connects Codex to the Cloudflare API through the Merge CLI.
You install the CLI, authenticate once, and run a single setup command from your project root.
That command writes a Merge CLI section to your project's
AGENTS.md
file, which tells Codex when to call
merge search-tools
and
merge execute-tool
to reach Cloudflare.
Once connected, Merge handles API token storage and rotation on your behalf, so you never embed Cloudflare credentials in your repo or manage them per developer.
Related:
How to use the Cloudflare MCP in Claude Code
Prerequisites
Before getting started, you'll need the following:
A
Merge Agent Handler account
Codex access (available via the OpenAI platform)
pipx installed (run
pipx --version
to confirm, or install via
pip install pipx
)
A Cloudflare account with access to the zones and resources your tasks need
If you want to connect Merge Agent Handler's Cloudflare MCP with internal or customer-facing agentic products, you can follow the steps
in our docs
.
1. Install the Merge CLI
Install the Merge CLI with pipx:
pipx install merge-api
Verify the install:
merge --version
2. Log in to Merge
Run the following to authenticate the CLI with your Merge Agent Handler account:
merge login
This links the CLI to your Merge account and stores your session credentials locally.
3. Add Agent Handler to Codex
From the root of the project where you want Codex to reach Cloudflare, run:
This writes a Merge CLI section to your project's
AGENTS.md
file so Codex knows to use the CLI when a task needs Cloudflare data. The command is idempotent, safe to re-run if you need to reset the configuration.
Commit the updated
AGENTS.md
so the configuration travels with the repo.
Related:
A guide to integrating the Cloudflare MCP with Cursor
4. Authenticate Cloudflare
Create a Codex task that needs live Cloudflare data, for example: "Read the DNS records and route bindings for my primary zone, then scaffold a migration script that recreates them in a new zone and flags any proxied records."
The first time Codex invokes a Cloudflare tool, a Magic Link will appear to complete connector authentication.
‍
Once authenticated, Codex can reach your Cloudflare account through Merge for every later task in this project.
{{this-blog-only-cta}}
Cloudflare MCP FAQ
In case you have more questions on setting up and using the Cloudflare MCP with Codex, we've addressed several more commonly-asked questions below.
What can you do once the Cloudflare MCP is connected to Codex?
With Cloudflare connected, Codex can:
Read the real zone config before scaffolding a Worker:
pull the existing routes and bindings so the deploy code it generates targets the actual zone rather than an assumed setup
Pull existing DNS records before generating a migration:
fetch the real record set, including which records are proxied, so the migration it writes recreates them accurately instead of dropping or mishandling some
Read a KV namespace before generating code that populates it:
fetch the real keys and value structure so the code it writes matches what the namespace actually holds
Pull zone analytics before generating a monitoring or alerting module:
fetch real traffic and error data so the thresholds and queries it scaffolds reflect actual baselines
Read existing firewall rules before scaffolding security automation:
fetch the current rules so the automation it generates extends them correctly rather than conflicting with what's live
Why use Merge Agent Handler vs. a self-hosted Cloudflare MCP server?
You can build your own MCP server on top of the Cloudflare API. For one developer on one account, it's workable: create an API token, write the server, and wire it into Codex.
It gets harder once more than one person uses it or tasks run in CI. Each connected developer needs their own Cloudflare token, scoped correctly, with rotation handled, and there's no central record of what agents touched.
A self-hosted server doesn't solve that, since you still own the token management, the server, and the access scoping yourself. With no central audit log, a Codex task can read or change production infrastructure with no record of what happened.
Merge Agent Handler handles credential storage and rotation across every connected user. You can scope exactly which Cloudflare operations a Codex task can call, and every call is logged with identity, timestamp, and inputs.
For an agent that can modify DNS, Workers, and firewall rules on production traffic, scoped access plus full audit logging is the foundation you want in place first.
Why connect Cloudflare to Codex?
Cloudflare holds the zone config, DNS records, and KV state that edge-infrastructure code has to match exactly.
Codex tasks that scaffold Workers, write migrations, or generate monitoring need that ground truth to produce code that works against the real account.
The alternative is describing your setup in the prompt, and those descriptions are always incomplete. A missed proxied record, an assumed route, or a wrong namespace is enough to make Codex generate code that breaks against live infrastructure.
Connecting Cloudflare lets Codex read the actual resources when a task needs them.
Can I use Merge Agent Handler's Cloudflare MCP with my employees?
Yes,
Agent Handler for Employees
is built to help engineering organizations provision, secure, and govern how employees connect AI tools like Codex to operational tools like Cloudflare.
Common patterns include:
Provisioning and access control via SCIM with identity providers like Okta and Microsoft Entra ID, so IT can manage which zones and resources an employee's agent can reach by role or team
DLP and policy enforcement on tool calls, so admins can restrict which operations an employee's AI can run against production infrastructure before the call is made
User-level audit logging so security and IT teams can review which Cloudflare resources were accessed or changed, by which employee identity, and when
Taken together, employees can use the Cloudflare MCP to scaffold Workers against real zone config, generate migrations grounded in actual DNS records, build monitoring tied to real analytics, and more, while IT keeps centralized control over which zones each agent can reach.
