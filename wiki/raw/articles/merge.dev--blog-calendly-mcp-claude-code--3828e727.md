---
title: "How to connect a Calendly MCP with Claude Code (4 steps)"
url: "https://www.merge.dev/blog/calendly-mcp-claude-code"
fetched_at: 2026-05-10T07:00:44.319211+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# How to connect a Calendly MCP with Claude Code (4 steps)

Source: https://www.merge.dev/blog/calendly-mcp-claude-code

Developers building agents that need to react to new bookings, pull invitee details for downstream workflows, or surface availability data have to navigate Calendly's OAuth model, handle webhook registration, and manage token storage before writing a single tool call.
To help your developers query scheduled events, access invitee records, and trigger workflows from booking data more easily from the terminal, we'll show you how to connect Calendly with
Merge Agent Handler's Calendly MCP server
.
How it works
Merge Agent Handler connects Claude Code to the Calendly API through a single CLI setup.
You install the Merge CLI, authenticate once with your Merge Agent Handler account, and register the connection with one command.
Merge handles Calendly's OAuth credentials and token lifecycle on your behalf, so you never store access tokens locally or manage refresh logic across environments.
Here's the command that registers the connection:
claude mcp add 
--transport http agent-handler https://ah-api.merge.dev/mcp
Prerequisites
Before getting started, you'll need the following:
A
Merge Agent Handler account
Claude Code installed (run
claude --version
to confirm)
pipx installed (run
pipx --version
to confirm, or install via
pip install pipx
)
A Calendly account with access to the event types and scheduling data you want to connect
If you want to connect Merge Agent Handler's Calendly MCP with internal or customer-facing agentic products, you can follow the steps
in our docs
.
1. Install the Merge CLI
Run the following to install the Merge CLI:
pipx install merge-api
Then verify the installation:
merge --version
Related:
How to use a Gmail MCP in Claude Code
2. Configure the CLI and log in
Run the interactive setup:
merge configure
This prompts you for your Merge API key and sets your default workspace preferences, linking the CLI to your Merge Agent Handler account.
Then authenticate your session:
merge login
Once login completes, the CLI can make authorized API requests on your behalf going forward.
3. Add Agent Handler to Claude Code
Register the Agent Handler MCP server with Claude Code:
claude mcp add 
--transport http agent-handler https://ah-api.merge.dev/mcp
Open Claude Code and run:
/mcp
agent-handler
should appear under Local MCPs with a
connected
status.
4. Authenticate Calendly
Select
agent-handler
from the MCP list. This opens a browser window where you select which integrations to authenticate. Choose Calendly and complete the OAuth flow. Merge stores and manages the credentials going forward.
The first time you use a Calendly tool in a Claude Code session, a Magic Link may appear to complete connector authentication, as shown below.
Once authenticated, you won't need to re-authenticate unless you revoke access.
To confirm the connector is accessible, open a Claude Code session and run a command like "List all scheduled events from the past 7 days, including the invitee name, event type, and scheduled time."
You should see an output like the following:
{{this-blog-only-cta}}
Calendly MCP FAQ
In case you have more questions on setting up and using the Calendly MCP in Claude Code, we've addressed several more commonly-asked questions below.
What can you do once the Calendly MCP is connected to Claude Code?
With Calendly connected, Claude Code can:
List scheduled events:
retrieve upcoming and past bookings filtered by date range, event type, or invitee, without opening the Calendly dashboard
Access invitee records:
pull name, email, and any custom question responses from a booking, useful for agents that need to prep materials or create records in a downstream system
Query event types:
list the event types configured on an account, including duration, availability windows, and scheduling links
Check user availability:
retrieve scheduling availability for connected Calendly users, useful for agents that need to surface open slots before suggesting a meeting time
List organization members:
pull users and their event type configurations across a Calendly organization, enabling agents to route bookings or build team-level scheduling summaries
Cancel scheduled events:
programmatically cancel a booking when triggered by an external condition, such as a CRM deal moving to a closed-lost stage
Why use Merge Agent Handler vs. a self-hosted Calendly MCP server?
You can build a self-hosted MCP server directly on Calendly's REST API. For a single user with one Calendly account and a narrow query use case, the setup is manageable: generate a personal access token, define tool schemas for the endpoints you need, and point your MCP server at the Calendly API.
The problem is multi-user and multi-organization scale.
Calendly personal access tokens are tied to individual accounts. If your agent needs to read bookings across multiple Calendly users or organizations, each requires its own token, its own storage, and its own rotation schedule. A self-hosted MCP server gives you no mechanism to enforce which event types or invitee fields an agent can access, and no audit trail of what it read or acted on.
Merge Agent Handler handles OAuth credential management across users and adds tool-level access control on top.
So, for example, an agent that sends booking confirmation emails can use tools like
scheduled_events_list
and
invitees_get
, but it may not have access to tools like
event_types_delete
or
scheduled_events_cancel
. Every tool call is also logged with the timestamp, tool name, and inputs.
Why connect Calendly to Claude Code?
Calendly holds the scheduling data that revenue and ops teams act on constantly: who booked a demo, when the onboarding call is scheduled, and which event types are driving the most volume. Developers building on that data currently have to export it manually or wire up a Calendly integration each time a new workflow needs a different slice of it.
With the Calendly MCP connected, Claude Code can query bookings, pull invitee details, and surface availability without leaving the terminal.
This is most valuable when a Calendly event needs to kick off a downstream action: creating a contact in the CRM when a demo is booked, sending prep materials to a new invitee, generating a weekly summary of scheduled calls by event type for a sales manager, and more.
