# How Cognition Uses Devin to Build Devin

**Source:** https://cognition.ai/blog/how-cognition-uses-devin-to-build-devin
**Published:** Early 2026
**Tags:** cognition, devin, dana, data-analyst, bug-triage, playbooks, mcp

---

## Summary

Cognition's comprehensive overview of using Devin internally — covering specialized agents (DANA for data analysis, bug triage/end-to-end fixes, design system maintenance), automated code review (Devin Review), knowledge management (DeepWiki, Playbooks), and extensibility (MCP Marketplace, REST API). In early 2026, the team merged **659 Devin PRs** in a single week.

## DANA (Data Analyst Agent)

A specialized version of Devin for data tasks:
- Queries data warehouses (Redshift, Snowflake, BigQuery)
- Creates visualizations (Seaborn)
- Builds dashboards
- Access via `/dana` or `@Devin !dana` in Slack
- Allows non-engineers to answer ad-hoc questions without pulling engineers away

## Bug Triage & End-to-End Debugging

- **Triage Playbook:** Triggered by Bug label in Linear. Devin searches code, checks git history, summarizes root cause
- **Connected to Datadog (logs) + read-only DB replicas**
- **End-to-End Fixes:** Traces breaking commits, writes fix with regression test, opens PR
- Treats data analysis as an engineering debugging workflow

## Key Components

- **Devin Review:** Autofix, Smart Diffing, Bug Catcher
- **DeepWiki:** Auto-generated docs with architecture diagrams
- **Playbooks:** Custom system prompts for repeatable complex tasks
- **MCP Marketplace:** One-click integrations (Sentry, Vercel, Notion, Airtable)
- **Session Insights:** Completed tasks → "Improved prompt suggestions"
