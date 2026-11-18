---
title: "Open Source Project Sudden Disappearance"
created: 2026-11-18
updated: 2026-11-18
type: concept
tags:
  - open-source
  - supply-chain
  - ai-supply-chain-security
  - infrastructure
  - trust
  - microsoft
  - package-compromise
status: L2
confidence: medium
sources:
  - https://news.ycombinator.com/item?id=50539610
  - https://github.com/microsoft/onnxruntime
---

# Open Source Project Sudden Disappearance

On 2026-11-17, **Microsoft's ONNX Runtime** — the most widely used engine for serving deep-learning models in production, with ~22k GitHub stars — **vanished from GitHub without notice**. `github.com/microsoft/onnxruntime` returns 404. The story hit 350 points on Hacker News (item 50539610). As of 2026-11-18 Microsoft had published no explanation, and the episode has become a case study in how a critical open-source project can disappear overnight and strand every pipeline that depends on it.

## What happened

- Users discovered the outage operationally: "[nvader] We found out about this this morning, when evals started failing in our pipelines... Does anyone know why or how a repository with 22k stars just went dark?"
- No advance warning, no deprecation notice, no README stub — the standard GitHub ToS-violation email that hit other Microsoft repos (e.g. azure-functions-host six months earlier, per [robjam]) apparently did not fire here either.
- Mirrors became the lifeline within hours: Intel's fork (`github.com/intel/onnxruntime`, with OpenVINO modifications) and a SourceForge mirror (`sourceforge.net/projects/onnx-runtime.mirror`). Community warning attached immediately: "[genxy] Note to people downloading these archives, there is a high likelihood that they contain malware" — unverified mirrors of a disappeared repo are a classic typosquat/malware vector.

## Candidate explanations (all unconfirmed)

1. **Security-driven takedown.** The most-discussed theory ties to the **Phrack 73** "Backdoor Attacks Against Machine Learning" article (published the same day, HN 50535992): "[momojo] In March 2026, we noticed a parser flaw: an ONNX model can cause ORT to read from arbitrary file paths (or memory addresses) without validations." Taking the reference implementation dark during disclosure of an ORT model-parser exploit would be consistent — but also "amateur hour tier" ([giancarlostoro]), since hiding the repo does not hide the code from attackers and only hurts defenders who need to patch.
2. **Package/repo compromise cleanup.** "[hiddenvulkcan] Maybe related to one of their packages that was compromised?" — referencing the reported `agent-framework` PyPI compromise (opensourcemalware.com). Quarantine-by-deletion is an incident-response move, not a communication plan.
3. **ToS/DMCA-style automated action**, per the azure-functions-host precedent.

Microsoft had not confirmed any of these at report time. Treat all as hypotheses.

## Why it matters

- **Supply-chain single point of failure.** ONNX Runtime sits under an enormous share of production inference (including Hugging Face model serving "without too much scrutiny," per the Phrack excerpt). A repo-level availability failure is an availability attack surface you do not control.
- **No sunset protocol for critical OSS.** The thread converged on the missing norm: repos should be able to enter a clearly-labeled "temporarily hidden, incident in progress" state instead of a bare 404, which routes users to unvetted mirrors — the worst possible outcome during a suspected compromise.
- **[rtpg]**'s proposal captures the asks: a paid package-manager intermediary that "default[s] to not promoting things until 2 weeks have passed" and "generally just does the right things."
- Connects to the broader 2026 pattern of infrastructure trust erosion: same-week Optimizely A/B-test malware injection into top websites (see [[concepts/systemic-software-breakdown]]) and Windows coding-agent telemetry ([[concepts/windows-coding-agent-telemetry]]).

## Related

- [[concepts/ai-supply-chain-security]] — the umbrella discipline
- [[concepts/systemic-software-breakdown]] — same-week trust-collapse incidents
- [[concepts/artifact-provenance-gates]] and [[concepts/pace-provenance-aware-capability-enforcement]] — the artifact-trust side of the same problem
- [[entities/microsoft-ai-team]] — Microsoft's AI org (unrelated to ORT, same vendor)

## Sources

- HN: "Microsoft's ONNX Runtime has disappeared from GitHub" — https://news.ycombinator.com/item?id=50539610 (350 pts, 2026-11-17)
- Original repo URL (404 at report time): https://github.com/microsoft/onnxruntime
- Phrack 73, "Backdoor Attacks Against Machine Learning" — https://phrack.org/issues/73/ (context, HN 50535992)
