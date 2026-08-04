---
title: "SQLite Critical CVEs or LLM Slop?"
source: https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/
date: 2026-07-30
date_fetched: 2026-08-04
author: Afek Berger, JFrog Security Research
type: research_report
status: fetched
tags: [ai-slop, security, cve, llm, sqlite, vulnerability]
---

# SQLite Critical CVEs or LLM Slop? - JFrog Security Research

JFrog security researchers investigated a batch of SQLite vulnerability advisories that were flagged as critical by NVD and CISA's ADP. Their findings:

1. **All 50+ CVEs from a single GitHub repo (programmervuln/cveadvisory-) appear to be LLM-generated ("AI slop")**.

2. **The claims fell apart under scrutiny**:
   - The cited vulnerable code didn't exist in the referenced SQLite versions
   - PoC payloads didn't work (no crash triggered)
   - None of the CVEs appear on SQLite's official advisory page
   - All advisories test positive for AI-generated content (GPTZero)

3. **The workflow appears automated**: a script uses an LLM to generate vulnerability reports from code snippets, submits them as CVEs, and creates GitHub advisories — all without human verification.

4. **Impact**: NVD and CISA flagged these as critical, wasting security teams' time on false positives. This represents a new attack vector: flooding vulnerability databases with AI-generated noise to hide real vulnerabilities or waste defender resources.

5. **Broader concern**: This is one of the first documented cases of LLM-generated "slop" polluting critical security infrastructure. As LLMs become better at mimicking vulnerability report formats, distinguishing real CVEs from AI-generated ones becomes harder.
