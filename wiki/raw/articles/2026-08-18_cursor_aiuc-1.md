---
title: "Cursor earns AIUC-1 certification for agent security and reliability · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/aiuc-1"
scraped: "2026-08-18T06:00:27.179736+00:00"
lastmod: "2026-08-18T06:00:26.830Z"
type: "sitemap"
---

# Cursor earns AIUC-1 certification for agent security and reliability · Cursor

**Source**: [https://cursor.com/blog/aiuc-1](https://cursor.com/blog/aiuc-1)

Blog
/
company
Aug 13, 2026
·
company
Cursor earns AIUC-1 certification for agent security and reliability
Kenneth Moras
·
4 min read
Table of Contents
↑
Independent audit and adversarial testing
Agent safeguards built into Cursor
Ongoing evaluation as agents improve
Following an extensive independent review of our controls and the behavior of our agents, we're happy to share that Cursor is now AIUC-1 certified.
AIUC-1
is a new standard for AI agent security, safety, and reliability that combines an audit of organizational controls with adversarial testing of the product itself.
Today, 70% of the Fortune 500 use Cursor, and agents are taking on increasingly consequential work inside those companies. As that autonomy grows, enterprises need stronger evidence about how agents behave when their safeguards are put under pressure.
Existing security certifications can tell an enterprise a lot about how its data is stored, protected, and governed. They do less to evaluate how an agent itself behaves in practice. What happens when an agent is asked to write insecure code, expose a secret, or take an action it should refuse?
For Cursor, AIUC-1 provides an independent test of the safeguards we have built around our agents, and evidence for customers that those safeguards continue to hold when the product is pushed into difficult or adversarial situations.
#
Independent audit and adversarial testing
AIUC-1 was developed with input from more than 100 Fortune 500 CISOs and risk leaders, with technical contributions from MITRE, the Cloud Security Alliance, and Stanford researchers.
It translates established frameworks such as the NIST AI Risk Management Framework, MITRE ATLAS, and the OWASP agentic threat taxonomy into requirements that can be tested against live AI systems. For coding agents, those requirements extend to areas such as secrets protection, secure code generation, MCP security, and agent identity and permissions.
To assess how Cursor performs against those requirements, we underwent an independent audit by Schellman, the world's first ANAB-accredited ISO 42001 certification body and the first authorized auditor for AIUC-1. Schellman reviewed our documented controls and validated the AI governance practices and implementations behind them.
We also put our agents through adversarial testing across thousands of scenarios designed to probe the limits of Cursor's safeguards.
The testing covered our key agent surfaces, including the IDE and cloud agents, using a representative enterprise configuration. Evaluators exercised the safeguards we have built into Cursor, including rules, hooks, and Auto-review, across scenarios involving the risks coding agents are most likely to encounter.
Across two rounds of testing and several thousand scenarios, Cursor passed the AIUC-1 requirements, with its safeguards holding across both benign and adversarial conditions.
#
Agent safeguards built into Cursor
Passing those evaluations reflects the safeguards we have built into Cursor over time. Organizations can use rules and hooks to shape agent behavior and enforce checks around agent actions, while Auto-review evaluates risky commands before they run. These application-level controls sit alongside safeguards that influence how the agent responds to insecure requests and whether it generates secure code by default.
AIUC-1 evaluated those protections together, alongside the model-level safeguards that shape how the agent responds to insecure requests. It also tested how the agent handles potentially destructive actions, from generating vulnerable code to running unsafe commands or deleting data.
#
Ongoing evaluation as agents improve
One advantage of AIUC-1 over many traditional certifications is that the
evaluation recurs
. Maintaining certification requires Cursor to be tested at least quarterly, with a full audit each year.
That ongoing scrutiny is important as our agents become more capable and the risks around them change. AIUC-1 itself is updated quarterly, including requirements specific to coding agents, so each new evaluation holds Cursor to a higher bar as the standard evolves.
AIUC-1 is one part of a broader security program that includes our SOC 2 Type II attestation, third-party penetration testing, bug bounty program, and our work toward ISO 27001 and ISO 42001 certification.
Our AIUC-1 report, including the scope of the
certification
and detailed testing results, is available through our trust portal at
trust.cursor.com
.
Read more about Cursor's enterprise security, compliance, and administrative controls in
our docs
, or visit
cursor.com/security
.
Filed under:
company
Author
:
Kenneth Moras
