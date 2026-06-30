---
title: "How to connect a Freshdesk MCP with Codex (4 steps)"
url: "https://www.merge.dev/blog/freshdesk-mcp-codex"
fetched_at: 2026-06-30T07:01:00.880299+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# How to connect a Freshdesk MCP with Codex (4 steps)

Source: https://www.merge.dev/blog/freshdesk-mcp-codex

Developers turn Freshdesk tickets into Codex task descriptions, and that translation drops the details that matter.
The original ticket has the exact error string, the customer's environment, the SLA policy that applies, the conversation thread where support already narrowed down the cause.
What survives into the task prompt is a developer's paraphrase of all that. Codex then writes code against the paraphrase, not against what the ticket actually documents.
The result is automation and fixes that handle a general version of the problem instead of the specific conditions the customer reported. The source of truth stays in Freshdesk while Codex works from a lossy copy of it.
To give Codex direct access to Freshdesk as it works through your coding tasks, we'll show you how to connect Freshdesk with
Merge Agent Handler's Freshdesk MCP server
.
How it works
Merge Agent Handler connects Codex to the Freshdesk API through the Merge CLI. You install the CLI, authenticate once, and run a single setup command from your project root.
That command writes a Merge CLI section to your project's
AGENTS.md
file, which tells Codex when to call
merge search-tools
and
merge execute-tool
to reach Freshdesk.
Once connected, Merge handles API key storage and rotation on your behalf, so you never commit a Freshdesk key to your repo or manage rotation across environments yourself.
Related:
How to use the Freshdesk MCP in Claude Code
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
A Freshdesk account with admin access to authenticate the connector
If you want to connect Merge Agent Handler's Freshdesk MCP with internal or customer-facing agentic products, you can follow the steps
in our docs
.
1. Install the Merge CLI
Install the CLI with pipx:
pipx install merge-api
Verify it installed correctly:
merge --version
2. Log in to Merge
Authenticate the CLI with your Merge Agent Handler account:
merge login
This links the CLI to your Merge account and stores your session credentials locally.
3. Add Agent Handler to Codex
From the root of the project where you want Codex to have access to Freshdesk, run:
This writes a Merge CLI section to your project's
AGENTS.md
file so Codex knows to use the CLI when a task requires Freshdesk data. The command is idempotent, safe to re-run if you need to reset the configuration.
Commit the updated
AGENTS.md
so the configuration travels with the repo and every developer and CI environment running Codex gets the same tool setup.
Related:
Steps for integrating a Freshdesk MCP with Cursor
4. Authenticate Freshdesk
Create a Codex task that requires live Freshdesk data, something like: "Read the open tickets tagged 'api-timeout', then scaffold a retry wrapper for our Freshdesk client that handles the specific failure cases those tickets describe."
The first time Codex invokes a Freshdesk tool, a Magic Link will appear to complete connector authentication.
Once authenticated, Codex has access to your Freshdesk account through Merge for all subsequent tasks in this project.
{{this-blog-only-cta}}
Freshdesk MCP FAQ
In case you have more questions on setting up and using the Freshdesk MCP with Codex, we've addressed several more commonly-asked questions below.
What can you do once the Freshdesk MCP is connected to Codex?
With Freshdesk connected, Codex can:
Read a requirements ticket before scaffolding a feature:
pull the full ticket and its conversation thread so the feature Codex generates matches the exact behavior the customer and support team specified, not a summarized version of it
Pull SLA policy definitions before generating escalation logic:
fetch the actual response and resolution targets configured in Freshdesk so any escalation or alerting code Codex writes uses the real thresholds rather than guessed constants
Read a ticket's custom field structure before generating type definitions:
retrieve the custom fields and their value sets on your tickets so generated models, validators, and parsers match your account's real schema instead of a generic ticket shape
Pull contact and company records to generate accurate account-tier routing code:
read the customer and company attributes Freshdesk stores so routing or prioritization logic Codex generates keys off the fields that actually exist on those records
Read group and agent configurations to generate assignment logic:
fetch the groups and agents defined in your Freshdesk instance so auto-assignment code Codex writes references real group IDs and routing rules, not placeholders
Why use Merge Agent Handler vs. a self-hosted Freshdesk MCP server?
You can build a self-hosted Freshdesk MCP server that calls the Freshdesk REST API directly.
For a single developer, that's workable: generate an API key, write tool schemas for the endpoints you need, and point Codex at it.
The self-hosted path breaks down at team scale.
Freshdesk API keys are per-user and tied to a subdomain, so every developer manages their own key and endpoint config. There's no central place to scope which ticket data or operations a Codex task can reach, no audit trail of what the agent read or wrote, and no clean revocation path when someone leaves.
Merge Agent Handler adds a managed layer: API key storage and rotation handled by Merge, per-user access scoping so each developer authenticates with their own identity, and full audit logging on every tool call.
For teams running Codex on production codebases where Freshdesk tickets carry customer PII, that observability isn't optional.
Why connect Freshdesk to Codex?
Autonomous coding agents are only as accurate as the context they're given, and stale documentation is where they go wrong.
A Codex task working from a hand-written summary of a Freshdesk ticket inherits every gap in that summary: wrong field names, guessed SLA values, an incomplete list of the error conditions to handle.
Those gaps produce code that looks right and fails against the live API. The custom field doesn't exist under the name Codex assumed, the enum value isn't valid, the pagination behavior differs from what the prompt described.
Connecting Freshdesk lets Codex read the source directly when a task needs it. The requirements ticket, the SLA policy, the real custom field structure, the agent and group configuration: Codex pulls the actual definitions instead of a developer's recollection of them.
The generated code then matches your live Freshdesk setup. That's the difference between a task that ships and one that comes back as a follow-up bug.
Can I use Merge Agent Handler's Freshdesk MCP with my employees?
Yes,
Agent Handler for Employees
is built to help engineering organizations provision, secure, and govern how employees connect AI tools like Codex to customer support systems like Freshdesk.
Common patterns include:
Provisioning and access control via SCIM with identity providers like Okta and Microsoft Entra ID, so IT can manage which employees can reach which ticket queues, groups, and Freshdesk data by role or team
DLP and policy enforcement on tool calls, so admins can block Codex tasks from reading tickets outside their designated scope or prevent retrieval of customer PII before it reaches the agent's context
User-level audit logging so security and IT teams can review which tickets were read, which records were retrieved, and which Freshdesk data was accessed, by which employee identity, and when
Taken together, employees can use the Freshdesk MCP to scaffold features against real requirements tickets, generate escalation logic from live SLA policies, and write integration code that matches your actual field schema, and more, while IT keeps centralized control over which queues and data each developer's agent can reach.
