---
title: "Bring dots to work with Merge for Workforce"
url: "https://www.merge.dev/blog/bring-dots-to-work-with-merge-for-workforce"
fetched_at: 2026-10-16T10:00:37.250119+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# Bring dots to work with Merge for Workforce

Source: https://www.merge.dev/blog/bring-dots-to-work-with-merge-for-workforce

OpenAI’s dots can now use company tools approved by IT through Merge for Workforce.
A dot
is a personal agent in ChatGPT that runs on its own cloud computer. It can use connected plugins, manage ongoing responsibilities, and keep working in the background. An employee might ask a dot to track a project, check what changed, and follow up when something needs attention, without restarting the task or rebuilding the instructions each time.
That persistence is useful at work, where access must stay tied to employees. A dot's access should reflect the employee's existing permissions, update when they change teams, and end when they leave.
Merge for Workforce provides that control through one governed MCP endpoint. IT chooses which company tools employees can use, applies security rules to each action, and records every call routed through Merge.
Connect dots to approved company tools
ChatGPT can turn remote MCP servers into plugins, and since dots can use plugins connected to a user's ChatGPT account, the
Merge for Workforce MCP endpoint
can be added as a custom plugin and made available to an employee's dot. After your employee connects once and signs in through your identity provider, Merge uses the employee's Groups to decide which tools the dot can access. A salesperson might get approved actions in Salesforce, Gong, and Slack, while someone in Finance might get a different set in NetSuite and Google Drive.
With a single plugin, the dot now has access to hundreds of third-party systems via connectors that have been built and maintained by Merge.
On each tool call, Merge checks whether the employee's Group allows the requested action. If it does, Merge runs the action with that employee's credentials and permissions. If the tool isn’t approved for use, the call fails and the employee can submit an access request for an admin to review. Changes made in your identity provider update access without requiring the employee to reconfigure the dot.
Apply company security rules to every action dots take
OpenAI gives dots built-in safeguards, action review, plugin permissions, and optional custom rules. Merge enforces company policy when a dot accesses company systems through Workforce. Before a tool call reaches a third-party application, IT and security teams can:
Detect personal, financial, health, or other regulated information in a tool call.
Use custom rules to catch internal account numbers, project names, or other company-specific identifiers.
Apply plain-language guardrails to stop actions involving a confidential project or another topic that should not cross a system boundary.
When a policy rule triggers, Merge can log the match, redact the sensitive value, or block the action before contacting the third party. AI Guardrails in Merge for Workforce can also inspect a tool's response before it returns to the dot.
Keep track of what dots do through Merge
Merge creates a record for every tool call, and lets IT see the employee, tool, status, request context, and any security rules that fired. Security and compliance teams can investigate actions across company systems in one place rather than piecing together separate application logs.
Workforce's shadow AI discovery also helps IT understand how employees are adopting AI. Teams can identify where personal agents are appearing, then give employees a governed connection to company tools instead of blocking them across the company.
That visibility also has a clear limit: Merge records what the dot does through Workforce, not every action the dot takes elsewhere.
Let employees work with their dots
Companies should not have to rebuild their identity, access, security, and audit controls for every agent employees adopt. Those controls should follow your company instead of staying inside a single tool.
Merge for Workforce gives OpenAI dots a governed path to company tools. The same infrastructure can support other compatible agents, with the employee's access and company policy already in place.
Contact us
to get access to OpenAI dots support in Merge for Workforce.
