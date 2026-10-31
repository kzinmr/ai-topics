---
title: AI Supply Chain Security
created: 2026-05-21
updated: 2026-10-31
type: concept
tags:
  - concept
  - security
  - agent-safety
  - developer-tooling
  - governance
  - open-source
aliases: []
sources:
  - raw/newsletters/2026-05-20-everything-important-from-google-i-o-2026.md
  - https://venturebeat.com/security/ai-supply-chain-attacks-release-pipeline-red-teams-not-covering/
  - raw/articles/nesbitt.io--2026-06-26-incident-report-cve-2026-lgtm-html--da259599.md
  - raw/articles/nesbitt.io--2026-10-24-this-week-in-package-management-html--b6c5a952.md
  - raw/articles/nesbitt.io--2026-10-30-signing-and-attestations-across-package-registrie--fb28e540.md
---

# AI Supply Chain Security

**AI Supply Chain Security** refers to the vulnerability surface of the ML/AI software supply chain — release pipelines, dependency management, CI/CD runners, and packaging infrastructure — as distinct from the model-level security that dominates AI safety discourse. In a 50-day period (April–May 2026), four major AI supply chain incidents demonstrated that the most critical attack surfaces are **not the models themselves** but the infrastructure around them.

## The Four Incidents (50 Days, Apr–May 2026)

### 1. OpenAI Codex Command Injection
Attackers exploited Codex's CI/CD pipeline to inject malicious commands during build and deployment, compromising the integrity of Codex releases.

### 2. LiteLLM / Mercor Breach
The LiteLLM open-source LLM gateway project and Mercor (AI recruiting platform) suffered concurrent breaches, compromising credentials and infrastructure access.

### 3. Anthropic Claude Code Source Map Leak
Claude Code's build pipeline leaked internal source maps, exposing proprietary implementation details and potentially revealing security-relevant architecture decisions.

### 4. TanStack Worm — Mini Shai-Hulud
The most sophisticated of the four attacks:
- **84 malicious npm packages** published with valid SLSA Level 3 provenance
- Targeted the TanStack ecosystem (React Query, Router, Table)
- Demonstrated that even cryptographically-verified supply chain attestations can be weaponized against the ecosystem they're meant to protect
- Named "Mini Shai-Hulud" after the sandworm from Dune

## Attack Surface Framework (VentureBeat)

VentureBeat's analysis identified **7 release surface classes** that model red-teaming does NOT cover:

| Surface | Description | Example |
|---------|-------------|---------|
| CI runner trust boundary | Compromised CI runners exfiltrate credentials | Codex CI injection |
| OIDC certificate management | Misconfigured identity federation | — |
| Dependency hooks | Pre/post-install scripts in packages | TanStack worm |
| Packaging gate integrity | Package registry trust models | SLSA provenance weaponization |
| Build artifact provenance | Signed build attestations | — |
| Release pipeline segmentation | Shared vs isolated pipelines | LiteLLM breach |
| Source map exposure | Debug artifacts in production | Claude Code leak |

## Industry Implications

- **Model red-teaming is insufficient**: None of the four attacks targeted model weights, training data, or inference — they all hit the software supply chain around the models
- **OpenClaw/Moltbook (770K-agent deployment)**: The largest documented autonomous agent deployment incident, highlighting the risk surface of agent orchestration at scale
- **SLSA Level 3 is not enough**: The TanStack worm demonstrates that even valid provenance attestations can be compromised, requiring higher-level integrity guarantees
- **Regulatory gap**: Current AI regulation (EU AI Act, US Executive Orders) focuses on model evaluation, not supply chain integrity

### 5. Nesbitt's CVE-2026-LGTM — Satirical Stress Test (June 2026)

Andrew Nesbitt's fictional "Incident Report: CVE-2026-LGTM" (June 2026) serves as a satirical stress test of AI-augmented supply chain security: seven independent AI-powered security gates fail for different reasons, none of which is "the code is safe." While fictional, the piece accurately diagnoses systemic blind spots in AI-augmented security tooling — each gate's failure mode maps directly to real incidents from the preceding 50 days (Codex CI injection, TanStack worm, Claude Code leak). The satire demonstrates that tooling which is individually reasonable can be collectively exploitable through shared blind spots.

Related: [[entities/andrew-nesbitt]]

### 6. Code Provenance for AI Contributions (Sep 2026)

A distinct supply-chain dimension emerged in the 2026 policy wave: provenance of the *contributed code itself* (human vs AI-generated), as opposed to provenance of the build pipeline. OpenJDK's Skara PR affirmation checkbox is effectively a lightweight, human-scale attestation mechanism analogous to SLSA attestations — but, like SLSA (see TanStack worm above), it attests only what the attester claims, not what was actually generated. See [[concepts/ai-code-provenance-in-open-source]] for the OpenJDK/Rust/Debian mechanism comparison and why detection-based verification remains out of reach (C2PA-style watermarking for code is the open research question).

### 7. LiteLLM 1.107.0 PyPI Compromise (October 21, 2026)

The LLM gateway itself became the payload carrier. `litellm==1.107.0` shipped a
credential stealer (`cook.pth`/`cook.py`) and an hourly RCE beacon
(`sitecustomize.py`) in all seven wheels; both execute at *every* Python
interpreter start on the host, not only when `litellm` is imported. Exfiltration
covered SSH keys, cloud creds, CI/CD secrets, AI-tool tokens, browser passwords
and — the AI-specific part — the provider API keys stored in the LiteLLM proxy
database. The injection was a single `data = "cook"` maturin line present only
in the sdist's `pyproject.toml`; no public commit in `BerriAI/litellm` contains
it, so repository-side review would have cleared the release. PyPI pulled it by
13:23 UTC; the affected Docker tags served the payload 11:46–14:20 UTC.

Two lessons for the framework above: (1) **a brokered-credential store is a
crown-jewel dependency** — gateway compromise == compromise of every provider
key behind it; (2) **sdist↔wheel differential auditing** is a cheap, high-yield
detection primitive that existing gates (including SLSA attestations) do not
cover, for the same reason the TanStack worm slipped past valid provenance.

See [[entities/litellm]] and [[events/2026-10-21-litellm-pypi-compromise]].

**Follow-up (24 Oct, Nesbitt weekly)**: LiteLLM's maintainers told Help Net Security the attacker used what appear to be **stolen GitHub CLI OAuth tokens** from three engineers' accounts — changing the release pipeline from the first, triggering and approving the release from the second, then deleting the workflow records from the third. The container image's build provenance recorded the source repo as `Berri-AI/litellm`, **one hyphen away** from the real `BerriAI/litellm`, and the payload files are absent from the release tag in the real repository. This makes 1.107.0 LiteLLM's **second compromise of 2026** and upgrades the lesson set: repository-side review clearing the release is *necessary but not sufficient* — the human/token layer above the repo is the actual failure point.

### 8. npm Trusted Publishing matched on repository *names* (October 2026)

Bloom Security found that npm's Trusted Publishing bound configurations on the **`owner/repo` name** rather than the **permanent numeric repository ID** that GitHub already includes in the OIDC token. Once a maintainer renamed or deleted the bound repository, *anyone* could register the freed name and publish new versions of the package — carrying a valid provenance attestation that named their own repository. Bloom counted the exposure across **more than 1,500 packages**. GitHub's fix (announced 2 October) expires any configuration that goes **48 hours without validation**, and npm's documentation now states the first publish binds to the repository's immutable identity.

This is the same structural bug as the SLSA/TanStack failure two sections up — **attestation validates a mutable human-readable identifier instead of an immutable one** — and it reappears in the LiteLLM case as a one-hyphen typosquat of the source repo. The recurring mitigation is not stronger attestation but *immutable identity binding* plus periodic re-validation.

### 9. Registry-level policy proxies for coding agents (October 2026)

GitHub **package firewall** entered public preview for Enterprise Cloud: a proxy between upstream registries and CI runners, **coding agents**, or internal registries that checks metadata requests and downloads against an enterprise policy covering cooldown periods, malware/vulnerability advisories, and **attestation downgrades**. npm-only and free during preview. Notable because it moves the cooldown/registry-timestamp protections discussed in [[entities/andrew-nesbitt|Nesbitt's "One Small Bug"]] out of client-side package-manager settings (which silently ignore unknown `.npmrc` keys) into an infrastructure chokepoint that an agent cannot misconfigure.

Related same-week signals: the **curl project** publishes LOW/MEDIUM vulnerability reports openly from 26 October (keeping embargoes only for HIGH/CRITICAL) after receiving 13 reports on a single Saturday — an explicit admission that embargo capacity is exceeded by AI-accelerated disclosure volume; and **Chainguard broke the PHP 8.5.12 embargo**, shipping fixed images over six hours before the coordinated release.

### 10. Cross-registry signing vs. attestation verification gap (October 2026)

[[entities/andrew-nesbitt|Andrew Nesbitt's]] cross-registry survey of signing, provenance attestations and trusted publishing makes the agent-relevant gap explicit: **producing evidence is now easy, checking it at install time is still rare**. Trusted publishing hands a registry a verified CI identity via short-lived OIDC credentials, which is why the Ultralytics compromise produced malicious releases carrying *valid* attestations when they came from the project's own release workflow — only token-uploaded releases lacked them. A compromised workflow is therefore an attestation factory, and coding agents are the workload most likely to be running from one.

The verification-default column is where the exploitable surface sits: **Cargo, Julia's Pkg and conda validate downloads against hashes in metadata served over TLS but unsigned** (corruption detection only), crates.io has no signing whatsoever, and **conda-forge uses neither signing nor trusted publishing**. npm and PyPI verify nothing at install — `npm audit signatures` is a separate command and pip/uv install-time checks remain open issues blocked on PEP 751's `attestation-identities` field. Genuine default verification is limited to Go's signed checksum log, Hackage's TUF index, NuGet restore (Windows always, Linux since .NET 8, macOS off), Terraform providers, Hex, SwiftPM, and the source-building caches (Nix/Guix/Spack).

Two retrograde moves deserve flagging for agent-infrastructure planning: **GitHub's Immutable Actions proposal was removed from the roadmap in December 2025**, and the **October 2026 workflow-lockfiles public preview pins direct and transitive actions to commits without integrity hashes** — the subsystem coding agents consume most got pinning without provenance. Meanwhile Anaconda's TUF-based `conda-content-trust` hit end of support (September 2026) and Notary v1 shuts down 8 December 2026. On the identity side, Nesbitt's framing generalizes the npm name-vs-ID bug above: signature validity and *identity* assertion are two separate checks, and CLIs make the second one a per-invocation user burden (`gh attestation verify --owner/--repo`, `*** verify pypi --repository`).

Source: [[raw/articles/nesbitt.io--2026-10-30-signing-and-attestations-across-package-registrie--fb28e540.md]]

## Responses and Mitigations

Organizations are responding with:
- **Zero-trust for CI/CD**: Treating build pipelines as untrusted by default
- **Dependency pinning with audit**: Locking all transitive dependencies with cryptographic verification
- **Release pipeline isolation**: Fully air-gapped build environments for critical releases
- **Agent-level sandboxing**: Restricting what running agents can access in deployment environments

## Related Pages
- [[concepts/security-and-governance/ai-safety]] — Broader AI safety framework
- [[concepts/ai-code-provenance-in-open-source]] — human-scale provenance attestation for AI contributions
- [[concepts/llm-policies-open-source]] — OSS project LLM contribution policies
- [[entities/andrew-nesbitt]] — weekly package-management digest: npm Trusted Publishing name-matching flaw, GitHub package firewall
- [[entities/openai-codex]] — Codex command injection incident
- [[concepts/openai/tanstack-supply-chain-2026]] — TanStack worm detailed analysis
- [[entities/litellm]] — LiteLLM gateway + 1.107.0 PyPI compromise
- [[events/2026-10-21-litellm-pypi-compromise]] — same-week gateway publish-step compromise
- [[events/distillation-attacks-2026]] — Related: supply chain concerns in model distillation
- [[entities/anthropic]] — Claude Code source map leak
- [[entities/andrew-nesbitt]] — Nesbitt's CVE-2026-LGTM satirical incident report
