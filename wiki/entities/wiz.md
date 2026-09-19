---
title: Wiz (cloud security company)
created: 2026-08-19
updated: 2026-09-19
type: entity
tags: [entity, company, security, cybersecurity, ci-cd-security, agent-security, autonomous-security-agents, vulnerability-discovery, developer-tooling, ai-infra-security, snowflake]
sources:
  - raw/articles/2026-08-19_wiz_red-agent-snowflake-copilot-cicd.md
  - raw/articles/2026-06-26_cohere_cohere-security-ai-agent-north-wiz.md
  - https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug
---

# Wiz (cloud security company)

**Wiz** is a cloud-security company (founded 2020, NYC) known for its developer-first threat-detection platform spanning cloud, code, and data. Its research team published the **Wiz Red Agent** case study in Aug 2026 — an autonomous, AI-powered security agent that independently found and exploited a live GitHub Actions injection in Snowflake's public repo and exfiltrated a Jira token, all without human intervention.

## Company Profile

- **Founded**: 2020, New York City; deep roots in the Israeli cybersecurity community.
- **Product**: A cloud security posture management (CSPM) + threat-detection platform that graph-indexes cloud, code, and data layers to surface toxic combinations of misconfigurations, vulnerabilities, and sensitive data exposure. Developer-first positioning: security findings surfaced inline in CI/PRs rather than a separate console.
- **Wiz Research**: The company's security-research arm, responsible for high-impact disclosures in cloud and CI/CD ecosystems. Known for publishing full exploit writeups including timeline, root cause, and remediation guidance.
- **Positioning in AI security (2026)**: Wiz is the most prominent vendor pushing **autonomous security agents** as both a research tool (Red Agent) and a defensive product line, and is one of the companies most frequently cited when AI-agent-driven offensive security moves from theory to production incident.
- **Google acquisition**: Google announced a ~$32B acquisition of Wiz in 2025, completed by early 2026 — the largest cybersecurity M&A on record. Multiple wiki sources corroborate the deal (e.g. a Harvey LAB case study explicitly modeled on it, and Ed Zitron noting it as completed earlier in 2026). It integrates Wiz's cloud-security graph with Google Cloud and Google Threat Intelligence. See `[[entities/google]]` for the acquirer.

## Key 2026 event: Red Agent × Snowflake (Aug 17 2026)

- **Tool**: "Red Agent" — autonomous AI security-research agent with a CI/CD capability
- **Target**: `snowflakedb/snowflake-connector-net` (public), `jira_issue.yml`
- **Vuln**: attacker-controlled GitHub issue title interpolated into a shell `run:` block; a no-op `if:` guard (using `github.event.pull_request.user.login`, which is null on issue events) gave a false sense of protection
- **Exploit**: agent self-corrected its own payload (first attempt used `#` and hit a bash syntax error; switched to `; echo '` to close the shell block), then exfiltrated `JIRA_API_TOKEN` via an oast.me callback
- **Outcome**: Jira read access to Snowflake's engineering, security-compliance, and bug-bounty projects; same-day patch by Snowflake (Jun 23), token rotated; 5-day exposure window with Wiz confirmed as sole actor via audit logs
- **AI code-gen angle**: the PR was co-authored with **GitHub Copilot**, which "identified it as all-clear without noticing the critical vulnerabilities" (Wiz's Aug 17 19:57 UTC update). GitHub Advanced Security scan also missed it.
- **Public disclosure**: Jul 25 2026 (per Snowflake's 30-day policy)
- **Author**: Gal Nagli, Wiz Research

### Detailed Timeline

| Date | Event |
|---|---|
| **Jun 18 2026** | PR #1218 merged (squash commit `4a1b8ce`); injectable shell-interpolation pattern live in `jira_issue.yml` |
| **Jun 23 2026** | Red Agent autonomously identifies and exploits the vuln via an oast.me out-of-band callback; HackerOne report #3819931 filed; Slack alert to Snowflake security within minutes |
| **Jun 23 2026** | Snowflake patches workflow (commit `1dc7766`, PR #1402), restoring safe `env:` + `jq --arg` pattern; Jira token revoked/rotated; audit logs confirm Wiz was the sole actor during the 5-day window |
| **Jul 25 2026** | Public disclosure deadline (30 days after resolution, per Snowflake policy) |
| **Aug 17 2026** | Wiz Research publishes full writeup; HN ~421 pts; Aug 17 19:57 UTC update adds GitHub Copilot co-authorship detail |

### Wiz's Published Lessons

1. **AI code generation demands rigorous oversight** — LLMs predict code probabilistically and can silently reintroduce deprecated/insecure shell patterns (here: replacing safe `env:` + `jq --arg` with unsafe `echo '${{ github.event.issue.title }}'`). AI-generated PRs must undergo the same static analysis as human code — and existing tools (GitHub Advanced Security) evidently missed it.
2. **Collapsing discovery windows** — the flaw was live only **5 days** before an autonomous agent found and exploited it. Automated discovery now happens in hours, so patch cycles and credential lifetimes must compress accordingly.
3. **Preventing CI/CD security regressions** — security intent is lost when safe patterns aren't explicitly enforced as policy. The PR removed the safe pattern; the "security gate" `if:` was itself a no-op.

### Snowflake Statement

> "The disclosure was received on June 23, 2026, and it was immediately investigated and remediated. Our investigation found no evidence of unauthorized access. Protecting our systems is of utmost importance to our customers, employees, and partners… We are working together with Wiz to share these learnings with the broader industry."

## Other Notable 2026 Engagements

- **Cohere North security agent (June 2026)** — Wiz collaborated with [[entities/cohere]] on the Cohere North security-agent launch, an applied example of LLM-driven enterprise security workflows with Wiz telemetry as source-of-truth context. See `[[raw/articles/2026-06-26_cohere_cohere-security-ai-agent-north-wiz]]`.

## Why this case is in the wiki

It is the canonical public example of an **autonomous security agent** performing end-to-end vulnerability discovery *and* exploitation against a live, production-adjacent target — the shift from "AI finds a CVE" to "AI finds, exploits, and evidences a CVE in the wild." See [[concepts/autonomous-security-agents]] for the pattern analysis.

## Related

- [[concepts/autonomous-security-agents]] — the broader concept
- [[concepts/ai-agent-security]] — threat-side framing
- [[concepts/prompt-injection]] — the LLM attack primitive this case sits alongside
- [[concepts/enterprise-coding-agent-security]] — enterprise risk profile
- [[concepts/agent-approval-spoofing]] — related agent-UI vulnerability class
