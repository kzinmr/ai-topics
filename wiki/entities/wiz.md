---
title: Wiz (cloud security company)
created: 2026-08-19
updated: 2026-08-19
type: entity
tags: [entity, company, security, agent-security, autonomous-security-agents, vulnerability-discovery, developer-tooling, ai-infra-security]
sources: [raw/articles/2026-08-19_wiz_red-agent-snowflake-copilot-cicd.md]
---

# Wiz (cloud security company)

**Wiz** is a cloud-security company (founded 2020, NYC) known for its developer-first threat-detection platform spanning cloud, code, and data. Its research team published the **Wiz Red Agent** case study in Aug 2026 — an autonomous, AI-powered security agent that independently found and exploited a live GitHub Actions injection in Snowflake's public repo and exfiltrated a Jira token, all without human intervention.

## Key 2026 event: Red Agent × Snowflake (Aug 17 2026)

- **Tool**: "Red Agent" — autonomous AI security-research agent with a CI/CD capability
- **Target**: `snowflakedb/snowflake-connector-net` (public), `jira_issue.yml`
- **Vuln**: attacker-controlled GitHub issue title interpolated into a shell `run:` block; a no-op `if:` guard (using `github.event.pull_request.user.login`, which is null on issue events) gave a false sense of protection
- **Exploit**: agent self-corrected its own payload (first attempt used `#` and hit a bash syntax error; switched to `; echo '` to close the shell block), then exfiltrated `JIRA_API_TOKEN` via an oast.me callback
- **Outcome**: Jira read access to Snowflake's engineering, security-compliance, and bug-bounty projects; same-day patch by Snowflake (Jun 23), token rotated; 5-day exposure window with Wiz confirmed as sole actor via audit logs
- **AI code-gen angle**: the PR was co-authored with **GitHub Copilot**, which "identified it as all-clear without noticing the critical vulnerabilities" (Wiz's Aug 17 19:57 UTC update). GitHub Advanced Security scan also missed it.
- **Public disclosure**: Jul 25 2026 (per Snowflake's 30-day policy)
- **Author**: Gal Nagli, Wiz Research

## Why this case is in the wiki

It is the canonical public example of an **autonomous security agent** performing end-to-end vulnerability discovery *and* exploitation against a live, production-adjacent target — the shift from "AI finds a CVE" to "AI finds, exploits, and evidences a CVE in the wild." See [[concepts/autonomous-security-agents]] for the pattern analysis.

## Related

- [[concepts/autonomous-security-agents]] — the broader concept
- [[concepts/ai-agent-security]] — threat-side framing
- [[concepts/prompt-injection]] — the LLM attack primitive this case sits alongside
- [[concepts/enterprise-coding-agent-security]] — enterprise risk profile
- [[concepts/agent-approval-spoofing]] — related agent-UI vulnerability class
