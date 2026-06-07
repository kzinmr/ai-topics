# Using LLMs to Secure Source Code & Defending Code Reference Harness

**Source:** Anthropic Blog + GitHub Repository  
**URL (blog):** https://claude.com/blog/using-llms-to-secure-source-code  
**URL (repo):** https://github.com/anthropics/defending-code-reference-harness  
**Authors:** Eugene Yan, Henna Dattani, with contributions from Michael Molash, Abel Ribbink, Justin Young, Ben Morris, David Dworken, Hasnain Lakhani  
**Published:** May 27, 2026  
**Scraped:** 2026-06-07  
**Context:** Eugene Yan (@eugeneyan) X post about the harness. Original post: "Stronger models have made finding vulnerabilities easier, and the bottleneck has shifted to verification, triage, patching. Here are some lessons from working with security teams to address the new bottlenecks." + "To get started, we open-sourced a harness with a skill for each step: /threat-model, /vuln-scan, /triage, /patch. Plus an autonomous find → verify → patch pipeline and isolation sandbox you can /customize"

---

## Blog Post: Using LLMs to Secure Source Code

Model capabilities are advancing quickly, and unevenly. We've been working with security teams to find and fix vulnerabilities in their own code and open source software, and the work has given us a better understanding of how to use models to secure source code. **Our primary takeaway: discovery is now straightforward to parallelize, and the bottleneck has shifted to verification, triage, and patching.**

To give some indication of this discrepancy, as part of our own scanning of open source software, as of May 22, 2026, we had disclosed 1,596 vulnerabilities. To our knowledge, 97 of these have been patched.

This guide walks through how you can work with Claude Opus to build a threat model, discover vulnerabilities in your codebase, then verify, triage, and patch them.

### The Find-and-Fix Loop

Teams finding and fixing the most vulnerabilities converged on a variation of existing best practices. We've distilled them into a sequence of six steps:

1. **Threat model:** Decide what counts as a vulnerability before you start scanning.
2. **Sandbox:** Build a sandbox environment to isolate agents and prove exploits.
3. **Discovery:** Have models look for vulnerabilities in your source code.
4. **Verification:** Independently confirm which findings are actually exploitable.
5. **Triage:** Deduplicate findings, assign severity, and prioritize what needs fixing.
6. **Patching:** Apply the fix, confirm the vulnerability is nullified, and search for variants.

The first two steps—building a threat model and a sandbox—are the setup for the rest of the loop. These are typically done once per codebase and revisited when the underlying system changes. The next four steps are the loop you'll run against the source: discover, verify, triage, and patch.

### 1. Threat Model: Define What Counts as a Vulnerability

The most common cause of false positives is that the model lacks a good understanding of your trust boundaries. You can work with Claude to build a threat model in two steps:

**First, bootstrap from the code, docs, and vulnerability history.** Feed the model what you would hand a new security engineer on day one: architecture docs, wikis, entry points, git history, and past vulnerabilities.

**Second, have the model interview someone who knows the system well.** Consider Shostack's four questions: What are we building? What can go wrong? What are we doing about it? Did we do a good job?

Key practices:
- Consider your dependencies' security policies (e.g., vLLM's security.md, SQLite's "Defense Against the Dark Arts", ImageMagick's security policy)
- Name what IS trusted — if you trust config files or authenticated clients, document it
- Include a THREAT_MODEL.md with the code

### 2. Sandbox: Run Agents Safely and Verify Exploitability

**One purpose of the sandbox is to protect your systems.** Match the isolation to your threat model. Containers are fine for the discovery agent reading code, but run the target and its PoCs in a microVM (like Firecracker) or a full VM with egress locked down.

**Another purpose of the sandbox is to prove exploitability.** When teams built a sandbox where the agent could compile code, run tests, and detonate a proof of concept, non-exploitable findings dropped significantly.

Key insight: "the biggest efficacy lever has been giving the model test beds, live systems, and running the PoCs."

### 3. Discovery: Provide Rich Context, Shorter Prompts, and Useful Tools

Give the discovery agent access to context: threat model, architecture docs, results of past scans. Frontier models benefit from increasingly simple prompts during discovery—long checklists reduce the model's creativity and generate fewer novel bugs.

Key prompting tips:
- Provide the goal and context; leave "how to scan" to the model
- Try asking for a specific vulnerability class
- Define the output with structured fields (rationale, finding, impact, severity, etc.)
- Give the model tools: grep, glob, SAST scanners, fuzzers
- Have the model partition the search space, then feed partitions to parallel discovery agents

### 4. Verification: Filter Out Non-Exploitable Findings

Discovery optimizes for recall; verification optimizes for precision. The verifier agent should be independent from the discovery agent—run it in a fresh container without a shared filesystem or conversation history.

Across the teams, adding an adversarial verifier roughly halved the rate of non-exploitable findings. Requiring that verifier to also build a proof of concept confirming the exploit brought the false positive rate to near zero.

### 5. Triage: Deduplicate by Root Cause, Rank by Preconditions and Impact

Proper triage helps prevent alert fatigue. Multiple teams shared the same lesson: if we send product engineers a pile of findings where a majority are non-exploitable, they will lose trust in the reports.

To deduplicate findings, consider the root cause. First, use a cheap deterministic pass (same file, same category, vulnerability line numbers within ten lines). Then, have a model apply qualitative rules:
- Treat as duplicate: same root cause worded differently; same vulnerability at multiple call sites; missing global protection reported per endpoint
- Treat as distinct: different vulnerability classes in the same file; different variables reaching different sinks

Severity rating based on: reachability, attacker control, preconditions, authentication, read vs. write, blast radius.

### 6. Patching: Close the Loop and Improve Context for the Next Cycle

Before patching, write a new test that fails with the existing code. Then, implement the fix and confirm the same test now passes without breaking anything else.

Validate each patch against a ladder of checks:
1. **Build.** The patch compiles and the new tests pass.
2. **Try to reproduce.** The original PoC should stop working.
3. **Check for regressions.** The original test suite still passes.
4. **Re-attack.** A fresh discovery agent runs an adversarial check.

### Acknowledgments

Written by Eugene Yan and Henna Dattani, with contributions from Michael Molash, Abel Ribbink, Justin Young, Ben Morris, David Dworken, and Hasnain Lakhani.

---

## GitHub Repository: Defending Code Reference Harness

A reference implementation for autonomous vulnerability discovery and remediation with Claude, based on learnings from partnering with security teams at several organizations since launching Claude Mythos Preview.

**This repo is not maintained and is not accepting contributions.**

Anthropic offers Claude Security, a hosted product that finds and fixes vulnerabilities in your source code across multiple projects.

### Contents

- **Claude Code skills**: `/quickstart`, `/threat-model`, `/vuln-scan`, `/triage`, `/patch`, `/customize`
- **harness/**: the autonomous reference pipeline (recon → find → verify → report → patch), configured for finding C/C++ memory vulnerabilities using Docker and ASAN

### Getting Started

```bash
git clone https://github.com/anthropics/defending-code-reference-harness
cd defending-code-reference-harness
claude
> /quickstart
```

### Ramp-Up Plan

| Step | When | Description |
|------|------|-------------|
| Step 1 | Day 1 | Build a threat model and run your first static scan + triage |
| Step 2 | Day 2 | Run the reference pipeline on a C/C++ library |
| Step 3 | Days 3-5 | Customize the pipeline for your target |
| Step 4 | Week 2 | Start autonomous scanning, triage, and patching |

### Pipeline Stages (7 stages)

1. **Build**: Compiles the target into a Docker image with ASAN
2. **Recon**: A lightweight agent reads the source and proposes a partition
3. **Find**: N agents run in parallel, each crafting malformed inputs
4. **Verify**: A separate grader agent reproduces each crash in a fresh container
5. **Dedupe**: A judge agent compares verified crashes against already-reported bugs
6. **Report**: A report agent writes a structured exploitability analysis
7. **Patch**: A patch agent writes a proposed fix, with grader agent confirmation

### Key Metrics
- **Stars**: 5.1k+
- **Forks**: 330+
- **Language**: Python (92.7%), Shell (3.5%), C (2.5%), Dockerfile (1.3%)
- **License**: View license (MIT)

### Looking Forward (from README)

After the initial ramp up, teams have tended to invest in:
1. Reviewing all internal repos and key open-source dependencies, ranking by priority
2. Setting up bespoke infrastructure for scanning
3. Incorporating scans into their SDLC (daily, weekly, CI pipelines)
4. Testing and experimenting with models to find what works best
