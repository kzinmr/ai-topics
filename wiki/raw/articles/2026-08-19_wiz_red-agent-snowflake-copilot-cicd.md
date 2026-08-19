---
title: "AI-Generated GitHub Copilot 'Autofix' Allowed Compromise of Snowflake's Jira"
type: article
source: https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug
publisher: Wiz Research
author: Gal Nagli
published: 2026-08-17
fetched: 2026-08-19
fetched_by: active-crawl
---

# Wiz Red Agent Finds Its Way Into Snowflake's Internal Jira Through a Flaw in a GitHub Copilot–Assisted PR

_Source: https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug (Wiz Research, Gal Nagli, August 17 2026; HN ~421 pts Aug 17 2026)_

## Summary

Wiz's autonomous security agent "Red Agent" independently discovered and exploited a GitHub Actions script-injection vulnerability in Snowflake's public repo `snowflakedb/snowflake-connector-net`, exfiltrating a Jira API token that granted read access to Snowflake's internal Jira (engineering, security-compliance, and bug-bounty projects). No human was involved. The flaw became live when PR #1218 was merged on June 18 2026 — just 5 days before discovery. GitHub Advanced Security's scan analyzed the final PR revision, including the vulnerable workflow, but did not flag the injection.

**Aug 17 19:57 UTC update (from the post):** "This blog has been updated to clarify that Copilot was a co-author that checked the merged PR and code change, and identified it as all-clear without noticing the critical vulnerabilities. It is unclear whether the code-change was AI-assisted."

## The vulnerability

`jira_issue.yml` triggered on `issues: opened` and interpolated the attacker-controlled issue title directly into a shell command:

```
- env:
  - ISSUE_TITLE: ${{ github.event.issue.title }}
- run: jq -n --arg title "$ISSUE_TITLE" ...
+ run: TITLE=$(echo '${{ github.event.issue.title }}' | sed ...)
```

The `sed` escaping runs *after* GitHub's template expansion; a single quote in the title breaks out of `echo '...'` → arbitrary command execution. The merged PR removed the repo's previously safe `env:` + `jq --arg` pattern.

An apparent security gate — `if: (github.event_name == 'issues' && github.event.pull_request.user.login != 'whitesource-for-github-com[bot]')` — was a no-op: on `issues` events, `github.event.pull_request` is always null, so `null != 'bot'` is always true.

## Exploitation (autonomous)

- Red Agent's CI/CD capability scanned Snowflake's GitHub org and flagged the workflow
- First exfil attempt used `#` to comment out the rest of the line → bash syntax error (the `#` consumed the closing paren of `TITLE=$(...)`)
- Agent self-corrected: adjusted the payload to `; echo '` to properly close the shell block, then exfiltrated `JIRA_API_TOKEN`, `JIRA_USER_EMAIL`, `JIRA_BASE_URL` base64-encoded via an out-of-band callback to a subdomain.oast.me listener
- The runner (Azure IP 20.106.182.197) called back within seconds; the token authenticated as `qa@snowflake.net` to `snowflakecomputing.atlassian.net`
- All POC data was deleted by Wiz after testing

## Timeline

- **Jun 18 2026** — PR #1218 merged (squash commit 4a1b8ce); injectable pattern live
- **Jun 23 2026** — Wiz identifies, exploits, and reports via HackerOne (report #3819931); same-day Slack notification to Snowflake security
- **Jun 23 2026** — Snowflake patches workflow (commit 1dc7766, PR #1402), restoring safe `env:` + `jq --arg`; Jira token revoked/rotated; audit logs confirm Wiz was the sole actor during the 5-day exposure window
- **Jul 25 2026** — Public disclosure deadline (30 days after resolution, per Snowflake policy)

## Wiz's key lessons

1. **AI code generation demands rigorous oversight** — AI tools predict code probabilistically and can reintroduce deprecated/insecure shell patterns; AI-generated PRs must undergo the same static analysis as human code
2. **Collapsing discovery windows** — the flaw was live only 5 days before an autonomous agent discovered and validated it; automated discovery now occurs in hours, requiring rapid patch cycles and short-lived credentials
3. **Preventing CI/CD security regressions** — security intent is lost when safe patterns aren't explicitly enforced; the merged PR removed the safe pattern while the existing security tooling failed to flag the resulting injection

## Snowflake statement (embedded in the post)

"The disclosure was received on June 23, 2026, and it was immediately investigated and remediated. Our investigation found no evidence of unauthorized access. Protecting our systems is of utmost importance to our customers, employees, and partners… We are working together with Wiz to share these learnings with the broader industry."
