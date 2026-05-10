---
title: "How technical support at Cursor uses Cursor · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/cursor-support"
scraped: "2026-05-10T01:19:39.304817+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# How technical support at Cursor uses Cursor · Cursor

**Source**: [https://cursor.com/blog/cursor-support](https://cursor.com/blog/cursor-support)

Blog
/
company
Mar 3, 2026
·
company
How technical support at Cursor uses Cursor
Kody Fisher & Zach Hudson
·
5 min read
Table of Contents
↑
Starting from the codebase
Integrating support sources with MCP
Identifying where the failure occurred
Tracking down similar cases
Determining whether it was a bug
Filing a bug report
Documentation updates
Automating the process
Commands for common steps
Rules and Skills for repeated patterns
Subagents to run steps in parallel
AI-native technical support
Support investigations are fundamentally research problems, which is why the slowest part of responding to customer challenges has always been gathering the right context. By collapsing code, logs, team knowledge, and past conversations into a single Cursor session, we've removed that bottleneck for most of our work.
Today, over 75% of Cursor's support interactions run through Cursor itself, increasing support engineer throughput 5–10x. This has led to a step-change in what is possible for support engineers from just a year ago.
#
Starting from the codebase
When we investigate, we typically begin in Ask Mode. We point it at the symptom and let it trace backward through the relevant product behavior. Because our full codebase is available locally, Cursor can index and use semantic search across product code, docs, and internal tooling in the same session.
This is where multi-root workspaces become powerful. Product context almost always spans multiple repositories. Answering the user question, "Why is this button disabled?" might involve frontend logic, backend policy checks, and docs describing the expected behavior. We keep related repositories together in one workspace so that kind of question is answerable in a single thread.
#
Integrating support sources with MCP
We use MCP servers to retrieve context and bring it into our investigations. Our support engineers no longer need to search across several tools to retrieve pertinent context because it is available in Cursor.
MCP servers allow us to integrate:
Databases with customer information, such as subscription tier, team settings, and privacy settings
Streamed event logs containing details on services used, telemetry errors, and network issues
Communication platforms like Slack, filled with threads and conversations that fill out our understanding of how customers interact with the product.
Engineering ticket platforms containing potentially dozens of unique teams that each operate differently
An internal documentation service that contains run books and troubleshooting guides
An account management service containing crucial customer information that may change the tone of how you approach a customer
With Cursor and MCP servers, our support engineers can quickly pull necessary information directly into their codebase investigations.
#
Identifying where the failure occurred
When a customer reports an error, we need to understand: Is the problem they're experiencing reproducible or transient, and where exactly did Cursor fail (client-side, API edge, downstream dependency, auth). Datadog MCP lets us pull the relevant logs and traces directly into the investigation thread, allowing us to start narrowing down the possibilities.
#
Tracking down similar cases
When a new support ticket comes in, the issue has likely been seen by another customer or someone on our team. An MCP that integrates with your support platform, as well as Slack, allows us to search that context directly and bring the most relevant threads back into the investigation. We search for hard identifiers first (error strings, request IDs), broaden if needed, and look for the newest thread that includes a current status, a workaround, and an owner.
#
Determining whether it was a bug
A lot of investigations come down to "bug or expected behavior?" Notion MCP lets us pull the relevant runbook into the thread, cross-reference it against what we're seeing, and either confirm the behavior or escalate with a much clearer bug report.
#
Filing a bug report
By the time we finish an investigation in Cursor, we've gathered all the material we need to file a ticket with engineering if something needs to be fixed. The Linear MCP lets us take all of that context and turn it into a formatted escalation directly from the same thread.
#
Documentation updates
When multiple customers run into the same questions, it's often a sign that we need to improve our documentation. Technical support is well-positioned to implement these kinds of fixes directly. We just mention @Cursor in Slack with what needs updating, and a cloud agent will open a PR against our docs repo.
#
Automating the process
#
Commands for common steps
We use slash commands for the most frequently repeated steps in the process:
Create Support Ticket
↓
↑
# Create Support Ticket
Create a Linear ticket for the reported bug or user issue.

## Format
- **Reporter Information:** Email, account ID, platform, app version
- **Summary:** Brief 1-2 sentence description
- **Expected vs Actual:** What should happen vs what happens
- **Steps to Reproduce:** Numbered list

## Notes
- Gather user info from logs before creating the ticket
- Include request IDs or trace IDs if available
- Link to related log queries or dashboards
- Default to Medium priority unless specified otherwise
Draft Customer Reply
↓
↑
# Draft Customer Reply
Draft a reply to the customer about their issue.

## Guidelines
- Use the public product name only
- Avoid internal service names, codenames, or infrastructure details
- Don't share internal error codes, file paths, or environment variables
- Stick to publicly documented features and standard troubleshooting steps

## When in doubt
Ask: "Could a customer discover this through normal product usage?"
If not, rephrase using general debugging approaches.
Search for Known Issues
↓
↑
# Search for Known Issues
Search Slack to determine if an issue is already known.

## Workflow
1. Search with identifiers (ticket ID, error code, exact error message)
2. Narrow by channel and time range
3. Find threads with status, workaround, or owner info

## Output
- **Verdict:** Known / Possibly known / Not found
- **Best thread:** Permalink + summary
- **Next search:** Query to try if results are weak
Search Logs
↓
↑
# Search Logs
Query Datadog logs for the specified request, user, or error.

## Common Patterns
- @requestId:{id} — find a specific request
- @userId:{id} or @email:{email} — find user activity
- status:error — filter to errors only
- service:{name} — filter by service

## Notes
- Always specify a time range (default: last 7 days)
- Field names vary by source—try multiple patterns
- Start broad, then narrow based on findings
#
Rules and Skills for repeated patterns
We use Rules and Skills to automate common processes in support investigations.
Customer reply (safe + actionable)
↓
↑
# Skill: Customer reply (safe + actionable)

## Inputs I need
- Customer symptom (what they see)
- What we found (grounded summary)
- Next step/workaround (if any)
- 0–2 missing data points to request

## Output format
- Short acknowledgment
- What we found (no internal details)
- What to try next (numbered steps)
- If needed: two questions max (to unblock investigation)
- Close with what we'll do next on our side

## Guardrails
- Avoid internal implementation details and internal jargon
- Prefer concrete steps over speculation
- Keep it concise; optimize for "first useful reply"
Draft a high-quality bug ticket
↓
↑
# Skill: Draft a high-quality bug ticket

## Inputs I need
- Symptom (customer-visible)
- Time window
- Any IDs (request id, user/team id)
- Evidence snippets (sanitized)

## Output format
## Summary
## Expected vs Actual
## Steps to Reproduce
## Evidence
## Scope/Severity
## Suggested next debugging step

## Quality bar
- No vague language ("sometimes", "doesn't work") without a concrete condition
- No internal-only jargon in the title
- Redact customer-specific info unless explicitly approved
Known-issue researcher (Slack + Notion)
↓
↑
# Skill: Known-issue researcher (Slack + Notion)

## Inputs I need
- Exact error text (or best approximation)
- Feature area keywords
- Time window (default: last 30 days)

## Workflow
- Search Slack first for exact phrases and identifiers.
- If results are weak, broaden with feature keywords and time filters.
- Search Notion for runbooks/FAQs for the same feature area.

## Output format
- Verdict: Known / Possibly known / Not found
- Best thread(s): 1–3 links with a one-line "why relevant"
- Workaround / mitigation (if present)
- Next search refinement: exact query to run next
#
Subagents to run steps in parallel
Subagents let us run common steps in the support process in parallel rather than sequentially.
LogInvestigator
searches Datadog for the failure point and supporting evidence.
KnownIssueMiner
scans Slack and Notion for prior threads and workarounds.
TicketWriter
formats the evidence into a complete escalation.
CustomerReplyDrafter
writes the customer response, stripping out internal details.
The results merge into a single output that we review and send.
Here is a subagent config you can adapt. The key is that each agent has a narrow scope, a clear output, and explicit constraints.
↓
↑
supportInvestigationPack
:
goal
:
>
Produce a grounded investigation summary, a draft bug ticket,
and a customer reply by running specialized agents in parallel.
inputs
:
-
customer_symptom
-
time_window
-
identifiers
:
request_id
:
""
user_or_team_id
:
""
error_text
:
""
-
investigation_notes
agents
:
-
name
:
LogInvestigator
focus
:
"Datadog: identify the most likely failure point and supporting evidence."
output
:
-
suspected_root_cause
-
strongest_evidence
-
disconfirming_checks
-
open_questions
-
name
:
KnownIssueMiner
focus
:
"Slack/Notion: find prior art, current status, and workaround."
output
:
-
verdict
-
best_links
-
workaround
-
next_search_query
-
name
:
TicketWriter
focus
:
"Write an engineering-facing bug ticket from evidence + notes."
output
:
-
title
-
summary
-
expected_vs_actual
-
steps_to_repro
-
evidence
-
suggested_next_debug_step
-
name
:
CustomerReplyDrafter
focus
:
"Draft a customer reply: clear, safe, and actionable."
constraints
:
-
"Do not include internal implementation details."
-
"Ask for at most two missing data points."
output
:
-
reply_text
-
questions_for_customer
final_assembler
:
merges
:
-
LogInvestigator
-
KnownIssueMiner
-
TicketWriter
-
CustomerReplyDrafter
produces
:
-
investigation_summary
-
ticket_draft
-
customer_reply
#
AI-native technical support
By combining these tools, we bring code research directly into the technical support process. We estimate this allows our team to be as much as an order of magnitude more productive compared to traditional approaches, which require more jumping between tools and across teams. This productivity gain enables our small (but growing) team of support engineers to effectively support our rapidly scaling user base.
If you're interested in learning more about how to bring Cursor into your CX workflow,
get in touch
.
Filed under:
company
Author
s
:
Kody Fisher & Zach Hudson
