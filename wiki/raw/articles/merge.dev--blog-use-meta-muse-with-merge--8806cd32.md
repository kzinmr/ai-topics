---
title: "Bring Meta Muse to work with Merge for Workforce"
url: "https://www.merge.dev/blog/use-meta-muse-with-merge"
fetched_at: 2026-10-13T10:01:09.060822+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# Bring Meta Muse to work with Merge for Workforce

Source: https://www.merge.dev/blog/use-meta-muse-with-merge

Meta Muse can now access approved company tools through Merge for Workforce.
‍
Muse
is Meta's personal AI agent. It browses the web, works across connected apps, and keeps running after someone closes the app. Give it a goal and it can handle a sequence of tasks on an employee's behalf, such as managing a calendar or sending an email.
That ability to act makes Muse incredibly useful at work, but it also raises the stakes of connecting it to company systems. When an agent can send emails or update records, IT needs to control what it can reach and see what it does.
Merge for Workforce provides that control through one governed MCP endpoint. Employees can use Muse with company tools, while IT decides which tools are available, applies security rules to each action, and keeps a record of every call.
Connect Muse to approved company tools
Muse supports remote MCP servers for tools beyond its built-in connectors. With Merge for Workforce, that connection leads to the tools your company has approved, and gives Muse more than a gateway to public MCP servers. Merge ships hundreds of ready-to-use connectors, including a large catalog we build, test, and maintain ourselves.
Each connector gives Muse clear tool definitions and deep action coverage, rather than inheriting whatever a public MCP server happens to expose. That breadth and depth lets Muse carry out more of the work an employee delegates across the systems they use every day.
An employee connects Muse to Merge once, then signs in through your identity provider. The tools that appear in Muse depend on the employee's Groups. A salesperson might get approved actions in Salesforce, Gong, and Slack, while someone in Finance gets a different set in NetSuite and Google Drive.
Merge checks whether the employee can use that tool, then runs the action with their credentials and permissions. If Muse asks for something outside that set, the user is notified and can request review by an admin.
Apply company security rules to every Muse action
A personal agent can touch several systems during one assignment and keep working after the employee steps away. One bad instruction can therefore travel much farther than it would in a typical assistant session.
Before a Muse tool call leaves Merge, it is checked against the company's security rules. IT and security teams can:
Detect sensitive data.
Identify personal, financial, health, or other regulated information in a tool call.
Enforce company-specific rules.
Catch internal account numbers, project names, or other identifiers using custom rules.
Evaluate requests in context.
Use plain-language guardrails to stop actions involving a confidential project or another topic that should not cross a system boundary.
Depending on the rule, Merge can log the match, redact the sensitive value, or block the action before the third party is contacted. AI Guardrails can also inspect a tool's response before it returns to Muse.
The rules live in Merge and apply whenever Muse uses the governed connection. Security does not need to rebuild the same controls inside another AI product.
See what Muse is doing across the organization
Muse's work does not disappear into a chat transcript. Merge records each tool call with the employee, tool, status, and request context. IT can see which systems Muse reached, which actions succeeded or failed, and which security rules fired. Security and compliance teams can use the same record for investigations and reviews instead of piecing together activity from separate application logs.
For Muse usage outside Merge, shadow AI discovery shows who is using Muse and what each person is doing with it across the organization. IT can see where adoption is already happening and bring those employees onto governed connections to systems instead of starting with a company-wide block.
Let employees bring their Muse to work
Companies shouldn't have to predict which agent every employee will prefer, then rebuild identity, access, security, and audit controls each time that preference changes. Those controls should stay with the company instead of being tied to one agent.
Merge for Workforce gives Muse a governed path to company tools today, and gives IT one place to manage that path as employees adopt new agents.
Contact us
to get access to Meta Muse support in Merge for Workforce.
‍
