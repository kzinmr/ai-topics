---
title: "How to connect a Notion MCP to Cursor (4 steps)"
url: "https://www.merge.dev/blog/notion-mcp-cursor"
fetched_at: 2026-07-08T07:00:57.088633+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# How to connect a Notion MCP to Cursor (4 steps)

Source: https://www.merge.dev/blog/notion-mcp-cursor

Connecting to Notion's API requires understanding its data models, and every question about them pulls you out of Cursor.
Each lookup means leaving the editor, hitting Notion's API explorer or a scratch script, and carrying the answer back in a browser tab.
To help your developers query Notion data without leaving Cursor, we'll show you how to connect Notion with
Merge Agent Handler's Notion MCP server
.
How it works
Merge Agent Handler connects Cursor to Notion's API through the Merge CLI.
You install the CLI, authenticate once, and run a single setup command from your project root. That command writes a
## Merge CLI
section to your project's
.cursorrules
file, which tells Cursor's agent when to call
merge search-tools
and
merge execute-tool
to reach third-party services.
Once connected, Merge manages your Notion OAuth token storage and refresh on your behalf, so no credential state lives in your local environment.
Related:
How to use the Notion MCP in Claude Code
Prerequisites
Before getting started, you'll need the following:
A
Merge Agent Handler account
Cursor installed
pipx installed (run
pipx --version
to confirm, or install via
pip install pipx
)
A Notion account with appropriate workspace permissions
If you want to connect Merge Agent Handler's Notion MCP with internal or customer-facing agentic products, you can follow the steps
in our docs
.
1. Install the Merge CLI
Add the Merge CLI to your environment with pipx:
pipx install merge-api
Confirm the installation succeeded:
merge --version
2. Log in to Merge
Connect the CLI to your Merge Agent Handler account:
merge login
This links the CLI to your account so Merge can make authorized requests against Notion on your behalf.
3. Connect the CLI to Cursor
Run the following from the root of the project where you want to use Merge tools:
This writes a
## Merge CLI
section to
.cursorrules
so Cursor knows to use the CLI for third-party services. The command is idempotent, so it's safe to re-run if you need to reset.
Related:
The steps for integrating a Notion MCP with Codex
4. Authenticate Notion
Open a Cursor chat in your project and try a query like:
Pull one of my Notion databases and show me its full property schema, including each property's type and configuration, so I can model it correctly in my integration code.
The first time you invoke a Notion tool, a Magic Link will appear to complete connector authentication.
{{this-blog-only-cta}}
Notion MCP FAQ
In case you have more questions on setting up and using the Notion MCP in Cursor, we've addressed several more commonly-asked questions below.
What can you do once the Notion MCP is connected to Cursor?
With Notion connected, Cursor can:
Inspect a real block object before writing your parser:
retrieve a page's block children to see how Notion nests block types, where rich text lives, and how child blocks are referenced, so your parser handles the real tree instead of a simplified one
Pull a database's property schema before modeling it:
fetch a database definition to see each property's exact type and configuration (select options, relations, rollups) so your type definitions match the API rather than a guess
Resolve real page, block, and database IDs:
get the actual ID formats your integration will pass to the API so you don't hardcode values that fail to resolve at runtime
Inspect the rich text object shape before rendering it:
retrieve a block or property containing rich text to see the annotation and link structure so your rendering or conversion code handles every span
Validate pagination on a real workspace:
run a query that returns many results to see how
next_cursor
and
has_more
come back before you implement your pagination loop
Why use Merge Agent Handler vs. a self-hosted Notion MCP server?
You can self-host a Notion MCP server using open-source packages that wrap the Notion API directly. For a solo developer working against their own workspace, that setup works: create a Notion integration, generate an internal integration token, stand up the server, and point Cursor at it.
The overhead compounds at the team level.
Notion auth means managing integration tokens or OAuth credentials, keeping them fresh, and making sure they survive process restarts. If several developers need Notion access through Cursor, each one manages their own token or they get shared in ways that are hard to audit and revoke cleanly. There's no built-in way to scope which pages, databases, or operations a given agent can reach.
Merge Agent Handler centralizes authentication and adds a control layer on top.
You define which Notion operations each agent is allowed to call, Merge enforces those boundaries, and every tool call is logged with a full audit trail that includes the input and output.
For teams where Notion holds product specs, customer data, or internal runbooks, that combination of access scoping and observability is what makes a production deployment defensible rather than just functional.
Why connect Notion to Cursor?
Developers writing Notion integrations have to understand the API's data model before they can write correct code against it.
Notion represents a page as a tree of typed block objects, stores database values as typed properties, and returns text as arrays of annotated rich text spans. That structure is documented, but reading the docs isn't the same as seeing a real object from the workspace your integration will run against.
With the Notion MCP connected, Cursor can pull real Notion data directly in the chat panel.
You can fetch a page while writing the parser that will process it, retrieve a database schema while writing the model it maps to, or resolve real IDs while writing the calls that use them.
The data your code operates on and the code itself live in the same session, which removes the round-trip to the API explorer or a separate test script.
Can I use Merge Agent Handler's Notion MCP with my employees?
Yes,
Agent Handler for Employees
is built to help organizations provision, secure, and govern how employees connect AI to tools like Notion.
Common patterns include:
Provisioning and access control via SCIM with identity providers like Okta and Microsoft Entra ID, so IT can manage which employees can read or edit Notion content by role or team
DLP and policy enforcement on tool calls, so admins can block retrieval of confidential pages or databases before results reach the employee's AI session
User-level audit logging so security and IT teams can review which pages were accessed or edited, by which employee identity, and when
In practice, employees can use the Notion MCP to search workspace knowledge, draft and update pages, and query databases, and more, while IT keeps centralized control over which content and operations each identity can reach.
