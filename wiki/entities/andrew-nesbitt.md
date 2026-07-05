---
title: "Andrew Nesbitt"
tags: [person]
created: 2026-04-24
updated: 2026-06-26
type: entity
---


# Andrew Nesbitt

**URL:** https://nesbitt.io
**Blog:** nesbitt.io
**Twitter/X:** @teabass
**GitHub:** @andrew
**Company:** Ecosyste.ms, Octobox
**Location:** Bristol, UK
**Flagship Creation:** Ecosyste.ms — the largest open dataset of OSS metadata (packages, repositories, dependencies)
**Notable Package:** node-sass — 1.3B+ downloads
**Podcast Host:** The Manifest (manifest.fm) — dedicated entirely to package management

---

## Overview

Andrew Nesbitt is one of the most focused specialists in the open source ecosystem: he has spent the last decade thinking almost exclusively about **package management, dependency graphs, and software supply chain security**. His work at Ecosyste.ms has built the largest open metadata dataset tracking packages, repositories, and dependencies across every major ecosystem. His GitHub profile description is famously straightforward: *"I've spent the last decade thinking about package management and git."*

Nesbitt's intellectual contribution is not in building flashy tools but in **mapping and understanding the hidden infrastructure** that underlies all of software development. Ecosyste.ms catalogs 11.4 million packages, 262 million repositories, and 22 billion dependencies — a scale that makes it the definitive lens through which to understand how open source actually works.

His approach is characterized by **observational rigor**: he collects data, identifies patterns, and draws conclusions that challenge conventional wisdom. His podcast *The Manifest* is the only audio program dedicated entirely to package management, and he has appeared on The Changelog, Sustain, CHAOSScast, Open Source Security, and more. He is a vocal participant in OpenSSF, Alpha-Omega, CycloneDX, and CHAOSS communities.

Nesbitt's writing has become notably more prolific and philosophically rich in 2025–2026, exploring not just the technical but the **psychological and structural dimensions** of open source — from dependency confusion attacks via LLMs to guided meditation for developers stressed about their dependency trees.

---

## Timeline

| Date | Event |
|------|-------|
| 2008-02-27 | Joins GitHub (early adopter, 166 public repos) |
| 2013 | Talks on Nodecopter, JavaScript in the Real World, robotics |
| 2013-2014 | Node.js hardware hacking era — drone control, meetup organizing |
| 2014 | Hackference: "Robotics 101"; jQuery UK: "The Rise of JavaScript Hardware Hacking" |
| 2015 | South-West Elastic: "Elasticsearch on Rails" |
| 2016 | node-sass reaches 1.3B+ downloads; 24 Pull Requests gains traction |
| 2017 | Brighton Ruby: "Can my friends come too?" — on OSS community building |
| 2018 | Bath Ruby: "With a Little Help from My Friends" |
| 2019 | Republishing npm dependencies to IPFS as a micro-registry (FOSDEM) |
| 2019-2020 | Creates Libraries.io and Ecosyste.ms; starts The Manifest podcast |
| 2021 | Content Addressed Package Management talk |
| 2022 | Ecosyste.ms formally established; first major grant funding |
| 2023 | Ecosyste.ms 2023 Year End Update; package management research intensifies |
| 2024 | Major blog output begins: "How I Assess Open Source Libraries," "Why I'm Fascinated by Package Management," LLM dependency confusion research |
| 2025 | Podcast appearances on Open Source Security, Sustain, CHAOSScast; "State of OSS Funding" talk at CHAOSScon; "Introducing Package Chaos Monkey"; "PromptVer" (semver for LLMs); "git-pkgs" dependency history tool; OSS Community Benchmarks project |
| 2026 | FOSDEM talk: "Open source funding: you're doing it wrong" (with Benjamin Nickolls); OSS Summit NA panel on funding; EasyBuild User Meeting: "Ecosyste.ms: Exploring Open Source Software Landscapes"; available for consulting on package management and supply chain security; "Guided Meditation for Developers"; "Package Manager Magic Files"; ".gitlocal" — Git should let files ignore themselves |
| Active through Apr 2026 | 3500+ GitHub followers, 166 repos, active contributions to ecosyste-ms, octobox, git-pkgs |

---

## Core Ideas

### "Why I'm Fascinated by Package Management"

Nesbitt traces his obsession back to **gaming magazine cover CDs** — the physical act of collecting, installing, and managing software from magazines sparked an early interest that evolved into a career-long focus. His thesis is that package management is the **central nervous system of modern software development**, yet it remains poorly understood and under-investigated. He argues that the dependency graph is not just a technical artifact but a **social graph** — it encodes relationships between developers, organizations, and communities.

> *"From gaming magazine CDs to dependency graphs"*

This personal-to-professional arc is rare: he found a niche so specific and so foundational that few others even recognize it as a distinct field of study.

### The 22-Billion-Dependency Problem

Ecosyste.ms tracks **22 billion dependency links** between packages and repositories. This number is Nesbitt's most compelling data point for understanding modern software: an astonishingly small number of packages serve as **critical infrastructure** for the entire open source ecosystem. His research demonstrates that most software is built on a handful of shared dependencies, creating systemic risk that most organizations don't understand.

This leads directly into his work with OpenSSF and Alpha-Omega on **supply chain security**: if you don't know what you depend on, you can't secure it.

### LLMs as a Supply Chain Attack Vector

In 2024-2025, Nesbitt identified a novel security concern: **LLMs can leak internal package names, making dependency confusion attacks easier to scale**. When developers paste internal code or package names into AI models, those models may inadvertently expose proprietary package namespaces to the public internet. This was one of the earliest articulations of AI-specific supply chain risk in the package management domain.

> *"The LLM itself becomes the attack vector."*

### "Guided Meditation for Developers"

In early 2026, Nesbitt published a satirical-but-serious piece: *"A practice for finding peace in your dependency tree."* This piece reveals his understanding of the **psychological toll** of dependency management. Modern developers are overwhelmed by the sheer complexity of their dependency graphs — hundreds of transitive dependencies, each with their own update cycles, security advisories, and compatibility requirements. The "meditation" is both humor and genuine advice: you can't control the complexity, but you can learn to observe it without panic.

### Package Manager Magic Files

In February 2026, Nesbitt documented the **hidden configuration files** that package managers use: `.npmrc`, `MANIFEST.in`, `Directory.Packages.props`, `.pnpmfile.cjs`, and more. His analysis reveals that each package manager has its own "magic file" ecosystem — a parallel configuration language that developers must learn in addition to the package manager's documented interface. This is classic Nesbitt: finding the invisible infrastructure and making it visible.

### "Git Should Let Files Ignore Themselves"

In his `.gitlocal` concept (2026), Nesbitt proposes that Git should support **file-level ignore directives** — individual files declaring their own ignore rules. This extends his broader thesis that the current model (centralized `.gitignore` files maintained by humans) doesn't scale to modern project complexity. If a generated file knows it shouldn't be tracked, it should be able to say so.

### Categorizing Package Manager Clients

Nesbitt's 2025 analysis categorized package managers by **resolution algorithms, lockfile strategies, build hooks, and manifest formats**. This taxonomy is his most systematic contribution to understanding the package management landscape: instead of treating all package managers as equivalent, he maps their architectural differences and the trade-offs each makes. This work underpins his consulting practice and informs organizations choosing tooling.

### How to Assess Open Source Libraries

In a 2024 post, Nesbitt outlined his personal methodology for evaluating whether to adopt a dependency. His criteria go beyond GitHub stars and download counts: he looks at **maintenance velocity, dependency health, security posture, license compatibility, and the package manager's own metadata**. This is practical wisdom from someone who has seen the entire dependency graph.

### The "Package Chaos Monkey"

In 2026, Nesbitt introduced the concept of **resilience engineering for software supply chains** — deliberately testing what happens when dependencies fail. This extends Netflix's Chaos Monkey philosophy to the dependency layer: if a critical package disappears or introduces a breaking change, does your system survive?

### PromptVer: Semver for the LLM Age

Nesbitt's "PromptVer" proposal (2025) introduces a **semver-compatible versioning scheme designed specifically for LLM-generated content and prompts**. This recognizes that prompts and AI-generated code evolve differently than traditional software — they need versioning that accounts for model drift, prompt refinement, and non-deterministic outputs.

---

## Key Quotes

> *"I've spent the last decade thinking about package management and git."*

> *"From gaming magazine CDs to dependency graphs."* — on why he's fascinated by package management

> *"The npm client's default settings are a root cause of JavaScript's recurring supply chain security problems."*

> *"I'm not connecting these dots. I'm just pointing out that the dots are there."* — on open source conspiracies

> *"A practice for finding peace in your dependency tree."* — Guided Meditation for Developers

> *"LLMs can leak internal package names, making dependency confusion attacks easier to scale."*

---

## Writing Style & Philosophy

Nesbitt writes with **analytical precision and dry humor**. His posts are typically:

- **Data-driven** — backed by Ecosyste.ms datasets with real numbers
- **Taxonomic** — he creates classification systems (package manager types, assessment frameworks)
- **Observational** — he identifies patterns others miss, then documents them clearly
- **Slightly subversive** — his "guided meditation" and "conspiracy" posts reveal a playful side beneath the serious analysis
- **Community-oriented** — he actively solicits contributions, runs podcasts, and speaks at conferences
- **Anti-monetization of ideas** — his research and datasets are freely available via open APIs

His blogging cadence accelerated dramatically in 2025–2026, with 25 posts in January 2026 alone. This suggests a shift from building infrastructure to **communicating what the infrastructure reveals**.

---

## Technical Breadth

- **Package Management:** Resolution algorithms, lockfiles, manifest formats, build hooks, mirroring protocols, magic files
- **Software Supply Chain Security:** Dependency confusion, typosquatting, trusted publishing, SBOMs, SARIF, PURL, VERS, SWHID
- **Dependency Graphs:** 22 billion links, critical path analysis, ecosystem mapping
- **Git Internals:** Remote helpers, diff drivers, filters, hooks, subcommands, file-level ignores
- **Open Source Metadata:** Ecosyste.ms platform, APIs, rate limiting, data curation
- **OSS Community Dynamics:** Funding models, maintainer burnout, contribution incentives
- **LLM/AI Security:** Prompt versioning, model-based attack vectors, AI-assisted dependency analysis
- **Multiple Ecosystems:** Ruby gems, npm, Python/PyPI, Go modules, GitHub Actions

---

## Recent Themes (2024–2026)

- **Supply chain security:** npm defaults, dependency confusion, LLM attack vectors
- **Package manager taxonomy:** Categorizing clients by architecture, not just ecosystem
- **Dependency assessment methodology:** How to actually evaluate whether to adopt a library
- **OSS funding critique:** "Open source funding: you're doing it wrong" (FOSDEM 2026)
- **Resilience engineering:** Package Chaos Monkey, testing dependency failure modes
- **LLM-specific tooling:** PromptVer, semver for AI-generated content
- **Git extensibility:** .gitlocal, remote helpers, diff drivers
- **Developer psychology:** Guided meditation for dependency anxiety
- **Community benchmarking:** OSS Community Benchmarks where maintainers define what good AI-generated code looks like
- **Consulting availability:** Leveraging Ecosyste.ms expertise for organizational guidance

---

## Related

- [[concepts/package-management]] — Resolution algorithms, lockfiles, manifests, supply chain security
- [[concepts/software-supply-chain-security]] — PURL, VERS, SBOM, SWHID, SARIF specifications
- [[concepts/dependency-graphs]] — Mapping the 22 billion dependency links in open source
- [[concepts/open-source-metadata]] — Ecosyste.ms as the definitive catalog
- [[concepts/llm-security]] — AI as a novel attack vector in dependency management
-  — Sustainable models for open source infrastructure-  — Remote helpers, diff drivers, file-level ignore directives
-  — Package Chaos Monkey and dependency failure testing
---

## Influence

- **Ecosyste.ms** catalogs 11.4M packages, 262M repositories, 22B dependencies — the largest open metadata dataset
- **node-sass** achieved 1.3B+ downloads — one of the most-downloaded npm packages ever
- **The Manifest** podcast is the only audio program dedicated to package management
- **Libraries.io** — open source discovery service
- **24 Pull Requests** — holiday OSS contribution initiative
- Active contributor to Alpha-Omega, OpenSSF, CycloneDX, CHAOSS
- 3500+ GitHub followers, 166 public repositories
- Regular podcast guest: The Changelog (#665, #327, #188), Sustain (#270, #159), CHAOSScast (#121, #115), Open Source Security, Request For Commits (#3), Bet On Yourself (#22)
- Conference speaker at FOSDEM, EasyBuild, OSS Summit NA, Brighton Ruby, Bath Ruby, Full Frontal, LXJS, jQuery UK, Hackference

---

### "The Mismeasure of Open Source"

In May 2026, Nesbitt published a comprehensive critique of how open source projects are scored for criticality, risk, and funding. The article identifies several systemic problems:

- **Missing read as zero**: The most consequential mistake in OSS scoring models. When signals are absent (no download counts for Go modules, no GitHub issues for projects using Bugzilla/mailing lists, no FUNDING.yml for salaried maintainers), models write zeros instead of "unknown." This silently excludes entire ecosystems from consideration.
- **Streetlight effect**: Metrics are used because APIs return them, not because they're meaningful. Download counts are dominated by CI runners, mirror traffic, and bot scans. GitHub stars measure a narrow demographic and are purchasable (~6M suspected fake stars 2019-2024). CVE count measures audit attention received, not vulnerabilities present.
- **GitHub as visible universe**: Projects on mailing lists, cgit, Gerrit, or Savannah (PostgreSQL, SQLite, GnuPG, glibc, FFmpeg) are disproportionately the old low-level infrastructure that models exist to find. GitHub mirrors return numbers for pull requests that go nowhere.
- **Identity problem**: The same code appears under different names across ecosystems (libcurl = curl on Homebrew, libcurl4 on Debian, pycurl on PyPI, curl-sys on crates.io, curl/curl on GitHub). Models either count them as separate entries or pick one and ignore the rest.
- **Weekend at Bernie's**: Claude Code and similar agents now support scheduled tasks, so repositories can accumulate plausible-looking maintenance commits authored under human names with no human in the loop. Commit frequency stops distinguishing maintained from automated.
- **Funding you can't see**: The most common funding arrangement for critical infrastructure is invisible to crawlers — maintainers employed by Red Hat, Google, Intel, Canonical, with the project as some or all of their job.

> "The compound case: Individually, each of these mismeasures some projects in some direction, and for the bulk of modern, registry-published, GitHub-hosted packages the errors roughly cancel out. The trouble is that the errors correlate, because a project old enough to predate GitHub is disproportionately likely to be written in C, distributed by vendoring rather than a manifest dependency, developed over a mailing list, funded through someone's salary, and low-churn because the format it implements stopped changing years ago."

This work extends Nesbitt's broader thesis about **observational rigor** — identifying patterns in the hidden infrastructure of open source that challenge conventional wisdom about project health and sustainability.

### "Not a Security Issue: AI Scanner Policy Engineering"

In May 2026, Nesbitt published a post documenting how AI/agentic vulnerability scanners read a project's **VULN-DISCLOSURE-POLICY.md** and self-triage findings against its published exclusions — before any human sees them. This inverts the typical security-tool discourse from "what to do with a flood of reports" to "how to shape what the scanner reports in the first place."

#### Key Findings from the curl Scan Experiment

- **Policy-driven self-triage**: Scanners scanning curl (already heavily audited) applied curl's "Not security issues" list — 16 named categories including server-triggered NULL dereferences, small leaks, never-ending transfers, and anything requiring command-line control — and demoted those findings automatically.
- **Concrete example**: Found `tool_formparse.c` recursing linked-list form parts with no depth limit, built a 150K-line config file to prove it, got an ASan stack-overflow trace — then wrote "trigger requires user to run curl with attacker-supplied config or args, so excluded by policy" and filed it under quality bugs.
- **Node.js prior art**: Embeds a full threat model in SECURITY.md with explicit trust boundaries — what the runtime does NOT trust (inbound network data, file content via API) vs. what it does (the OS, the developer's code).
- **Django's policy**: Gives worked examples of reports "not considered valid" and asks reporters to skip CVSS scores, severity assessments, and "lengthy background sections" — a near-direct description of LLM default output.
- **Chrome's security FAQ**: Source of the most-borrowed exclusion: a physically-local attacker who can already run code as you is out of scope.

#### The Actionable Takeaway

Writing a good exclusion list is **cheaper and more effective** than training a classifier to filter false positives. Each exclusion needs: the pattern name, a flat statement that it doesn't qualify, and enough reasoning to generalize. Nesbitt collected ~500 repositories shipping a threat model file — but filenames are scattered (THREAT-MODEL.md, threat_model.md, ThreatModel.md), and tooling hasn't converged on a standard path.

> *"The better-built tools, the ones that read the repo before reporting, are the ones a policy file can steer, and those are increasingly the ones doing the scanning. Writing the threat model down was always good practice for human reporters, and it turns out the new readers take it more literally than the old ones ever did."*

Related: [[concepts/agent-safety]], [[entities/project-glasswing]]

### "CHAOSS Metrics in 2026" — AI Agents Break Open Source Measurement

Published May 27, 2026, this is Nesbitt's most thorough examination of how **AI agents invalidate the assumptions baked into open source metrics**. While "The Mismeasure of Open Source" critiqued scoring models generally, this piece applies the same observational rigor to a specific published metric set.

**The Core Problem**: CHAOSS metrics were drafted 2018-2023 assuming contributions were produced at human speed. That cost is being removed from one side of the interaction, so counts increasingly measure how much of the cheap thing (agent-generated events) is being pointed at a project rather than anything about the community behind it.

**Activity Counts Decoupled**:
- `Issues New`, `Issues Closed`, `Change Requests`, `Code Changes Commits` — all proxy measures assuming an issue cost someone ten minutes and a PR cost an afternoon
- Daniel Stenberg on curl: "The top-level numbers go up, maintainer time per item goes up, and the proportion of items that represent something a user actually needs goes down. None of the count metrics can distinguish those three movements."
- `Change Request Acceptance Ratio`: originally framed as "welcoming to contributors" — on a project receiving low-effort generated PRs, a falling ratio means maintainers are doing their job, and a high one might mean they've given up reviewing

**Responsiveness Metrics Broken**:
- `Issue Response Time`, `Time to First Response`, `Issue Resolution Duration` — a project receiving 200 issues/month instead of 20 will see median response times rise even if maintainers work the same amount
- AI triage bots drop Time to First Response to seconds — the metric definitions say to filter bot responses, but the assumption that bots are labelled breaks when accounts look like normal users

**Contributor Identity Crisis**:
- `Contributors`, `New Contributors`, `Conversion Rate`, `Contribution Attribution` all assume a contributor identity maps to a person
- An agent opening PRs from freshly created accounts, or one person running a fleet of agents with separate tokens, registers as a burst of new contributors
- Conversion Rate was designed to measure onboarding effectiveness; now it's also measuring how many "contributors" were ever capable of having an experience

**Bot Activity Metric's Blind Spot**: The CHAOSS Bot Activity definition catches Dependabot and release automation but not coding agents posting through a personal access token at plausible hours. Nesbitt wrote a mock RFC trying to specify this boundary — concluding "you can't: every clause depends on voluntary disclosure by exactly the operators who won't disclose."

**Risk Metrics (Bus Factor, Libyears)**:
- `Bus Factor` and `Contributor Absence Factor`: the "Weekend at Bernie's" problem — a project where the absence factor is 1, that person left 18 months ago, and contributions are Dependabot merges + agent PRs landing on an unprotected branch. The metric reports the same number for "one engaged maintainer" and "one departed maintainer whose token still works."
- `Libyears`: measures `current_release_date - installed_release_date`. A dependency that stopped releasing contributes zero forever. Packages in the "dead or unresponsive" bucket score as perfect until someone acquires publish credentials. The xz → Shai-Hulud → TanStack worm series argues that the newest release is the one most likely to be hostile, while libyears scores a year-old stable version as "debt."

**Release Frequency Ambiguity**: Projects with automated release pipelines (every Dependabot merge cuts a patch) and projects deliberately adding cooldown periods for supply chain defense show the same number — the metric definition doesn't ask which.

**Licensing Blind Spot**: SPDX Document and licensing focus areas are computed the same way regardless of who wrote the code. But whether AI-generated code has any copyright to grant is not a settled question. The detection reports MIT for a repo an OpenClaw instance filled unattended the same as for any other.

**Less Affected**: Upstream Code Dependencies, Test Coverage, and DEI survey-based metrics hold up better — they measure artifact properties or ask humans directly.

> *"The released catalogue currently has no way to distinguish an event produced by a person exercising judgement from an event produced by an agent following a loop, and almost everything in the Evolution and Risk focus areas depends on that distinction holding by default. It no longer does."*


### Agent Skills Registry Threat Models (June 2026)

On June 3, 2026, Nesbitt published a comprehensive threat model analysis for **agent skill registries** — distribution channels for agent skills (bundles of prompts, scripts, dependencies, and tool permissions). ClawHub, Tessl, and skills.sh have all launched in the past year, modelled on existing package registries. Nesbitt's analysis covers the entire attack surface:

**Code execution at load time**: Skills can execute scripts before the agent reaches the prompt, via three paths — prompt injection, scripts/ directory invocation through bash, or shell snippets in the skill file evaluated before the model is in the loop. The user's mental model of "the agent runs a tool, I approve it" doesn't cover loader commands that run before the agent reaches the prompt.

**Prompt injection via skill descriptions**: Most loaders inject every installed skill's description into the system prompt every turn — even skills the user installed once and forgot about. Descriptions containing adversarial tokens, hidden HTML, or unicode control characters that the loader doesn't strip become unprompted prompt injections.

**Version pinning guarantees**: Most skill formats use git as the distribution channel where "version" means "default branch at fetch time." Few loaders record the commit sha actually used. The lockfile equivalent, where it exists at all, records name and version but not the bytes, so a pinned `foo@1.0.0` resolves against whatever currently owns that name.

**Auto-update risk**: Update paths typically walk the lockfile and reinstall each entry without re-prompting on capability changes. A skill that adds a new `requires.env` value on a patch bump is applied without interaction.

**Skill name identity and dependency confusion**: Names are inherited from source (paths, owner/repo, owner/repo/skill triples) with unwritten normalization rules. Two skills resolving to the same on-disk name can shadow trusted skills. Registry identity transitions (rename, merge, ownership transfer) can silently change the effective owner and declared capabilities.

**Resolution across multiple sources and tool permissions**: When a name resolves from multiple sources, the loader may fall through to npm/PyPI — the same dependency-confusion pattern Alex Birsan documented in 2021. Skills inherit the agent's full tool grants (bash, file edit, network). Some formats let the skill declare its own allowed-tools list, treated as pre-approved, effectively shipping the approval bypass alongside the code that uses it.

**Key insight**: Each of these threats is a design decision working as intended — not a wrong line of code a static scanner can call out. The agent skills registry is a strict superset of a package-manager client, inheriting every documented supply chain threat while adding agent-specific vectors (prompt injection, tool permission inheritance, silent auto-update).

References: [[concepts/agent-safety]], [[concepts/software-supply-chain-security]], [[concepts/prompt-injection]]

---

### gittuf — A Signed Log for Git Refs

Published June 4, 2026. Nesbitt examines **gittuf**, a Reference State Log (RSL) for Git that addresses the gap between commit signatures and forge-enforced branch protection.

**The Problem**: Commit signatures verify individual commits but don't protect against ref-level attacks. Branch protection is a row in a forge database — it doesn't follow the repository when cloned, and forge admin roles can change it without leaving a Git record. Real attacks exploiting this gap:

- **2021 php-src**: Two commits falsely attributed to Rasmus Lerdorf and Nikita Popov were pushed onto the self-hosted PHP Git server. Commit signing alone wouldn't have stopped this — the commits weren't signed, and nothing would have forced a check.
- **2018 Gentoo GitHub takeover**: An administrator's leaked password led to org takeover. The attacker removed legitimate developers and pushed malicious `rm -rf` ebuilds. Malicious refs sat at `master` for 8-10 hours. Branch protection was enforced by the same forge admin role the attacker held.
- **2025 tj-actions/changed-files**: A leaked PAT let an attacker create one malicious commit and retarget ~23,000 repos' tags. Tag objects are immutable but the refs pointing at them are just pointers — a force push moves them if the forge accepts it.

A 2016 USENIX paper described the fundamental pattern: a hostile server can roll a ref back to an earlier commit, or swap it for a different valid commit. The client gets a verifiably correct commit — just not the legitimate tip.

**gittuf's Solution** (2025 NDSS paper): The **Reference State Log (RSL)** records every ref update as a signed entry in a hash chain stored under `refs/gittuf/reference-state-log`. Each entry names a ref, the new commit hash, and the hash of the previous entry, signed by policy-authorized keys. Verification walks the RSL forward, checking each ref movement against the policy in force at the time. If a clone's tip doesn't match the RSL's last entry for that ref, a non-maintainer served a ref that wasn't signed for.

**Key Properties**:
- Verification runs **outside the forge** against policy and keys the forge doesn't hold
- Policy lives at `refs/gittuf/policy` in TUF-derived metadata format, supporting delegated rules and **M-of-N threshold signatures**
- Reviews and approvals are separate signed attestations alongside the RSL, not folded into ref-advancement entries
- Tag moves are ref updates too — the tj-actions attack would leave an inconsistent log or require attacker-held keys
- Chains naturally with Sigstore and in-toto attestations to connect artifact provenance back through build state to an authorized ref

> *"I'd like to see forges build gittuf in directly, so the workflows people rely on produce signed RSL entries on the maintainer's behalf."*

Related: [[concepts/software-supply-chain-security]], [[concepts/git-internals]]

---

### Install-Script Allowlists

Published June 5, 2026. A comprehensive survey of **install-time code execution controls** across every major package manager ecosystem. Nesbitt documents which tools allow install scripts by default, which require per-package opt-in, and which constrain execution through sandboxing.

**The Landscape**: Most package managers allow a dependency's install-time code to run by default: npm postinstall, Setuptools setup.py, CPAN Makefile.PL, RPM scriptlets, Conda post-link, Debian postinst. A small but growing number require explicit per-package opt-in via **allowlists** or **trusted-dependencies lists**.

**Per-Package Allowlists**:
- **npm 11.10.0** (February 2026) shipped `allowScripts` in `package.json` via `npm approve-scripts`/`npm deny-scripts`. Entries pinned to a specific version (`[email protected]: true`) by default. Behaviour in 11.x is advisory — scripts still execute, hard block planned for future release
- **pnpm v10** (January 2025) blocked install scripts by default using `onlyBuiltDependencies`/`neverBuiltDependencies`. v11 consolidated into `allowBuilds` with `dangerouslyAllowAllBuilds` as escape hatch. `strictDepBuilds` (v11 default) fails installs for unlisted packages
- **Bun** blocks install scripts by default with a built-in default allowlist of well-known packages (esbuild, fsevents). `trustedDependencies` overrides the default list
- **Deno** never runs npm lifecycle scripts without explicit approval via `--allow-scripts=` or `deno approve-scripts` (Deno 2.6, December 2025)
- **Composer 2.2** (2021) made plugin activation explicit via `allow-plugins` config key
- **Yarn Berry (v2+)** uses declarative `dependenciesMeta.<pkg>.built: true` with `enableScripts: false` globally

**Global Sandboxing**:
- **opam** (OCaml) wraps build/install commands with bubblewrap/sandbox-exec (opam 2.0, 2018)
- **Swift Package Manager** runs manifest evaluation and plugins inside sandbox-exec with no network access by default, with `PluginPermission` declarations for elevated access
- **Nix/Guix** run every derivation's builder inside a chroot with isolated PID/network/mount namespaces and no network except fixed-output derivations
- **Portage** (Gentoo) uses LD_PRELOAD-based sandbox intercepting filesystem syscalls

**Identity/Signature Verification**: RubyGems trust policies, Gradle dependency verification metadata, NuGet trustedSigners, and apt-secure gate which artifacts can be installed — they don't control what the code does post-install.

**Structural Distinctions**:
- **Cargo** `build.rs` and proc-macros run as native code during every build — structurally compile-time, not install-time, but functionally equivalent on fresh builds. No per-package allowlist for build scripts
- **JVM** build files (Gradle Groovy/Kotlin, Maven plugin goals, SBT Scala) execute at configuration time, before project source touches the compiler
- **Python wheels** conventionally have no install-time hooks, but sdist builds execute PEP 517 backends. Pip has no per-package allowlist; uv provides `no-build-package`/`no-binary-package` controls
- **Go modules** don't run downloaded code beyond compiling it — the only major ecosystem without an install-time execution surface
- **Bazel** BUILD files run in Starlark (a Python dialect with no clock, no recursion, no mutable global state) and build actions execute in per-action sandboxes

**Survey Coverage**: 30+ package managers across JavaScript, Python, Ruby, Perl, PHP, Rust, Go, Zig, JVM, .NET, OCaml, Elixir, Erlang, Haskell, Dart, Lua, Nim, Raku, Crystal, Julia, R, C/C++, and all major OS distribution package managers (dpkg, RPM, pacman, apk), plus userland tools (Homebrew, MacPorts, Scoop, Chocolatey, winget) and version managers (asdf, mise).

Related: [[concepts/software-supply-chain-security]], [[concepts/package-management]]

---

### Scrutineer — LLM-Powered Vulnerability Scanning (June 2026)

On June 25, 2026, Nesbitt published Scrutineer, an open source security scanning tool built for **Alpha-Omega** that uses LLMs to find vulnerabilities while addressing the **maintainer burnout bottleneck**.

**The Problem**: LLMs have made finding vulnerabilities in open source code "much easier" — "Point one at a codebase and it turns up real bugs alongside invented ones, faster and cheaper than the fuzzers and scanners that came before." But the bottleneck hasn't moved: every finding still needs human verification. When Nesbitt pointed AI scanners at curl in May 2026, "most of the output collapsed against the project's own disclosure policy, and the findings worth having were buried in the rest."

**Architecture**:
- Each scan is a **skill on disk**: a SKILL.md file, a JSON schema for output, and supporting scripts. Changing what runs is editing markdown, not recompiling a scanner.
- The `triage` skill runs first, gathers context, and enqueues the rest of the pipeline in parallel.
- Results are structured findings: severity, CWE, source-line location, affected versions, and a six-step trace of how each vulnerability was reached.
- The `security-deep-dive` skill is the model-backed audit — two-phase: first builds a sink inventory (every code-execution, shell-out, or hostile-path entry point), then traces each sink back to a trust boundary.
- The `threat-model` skill derives the project's security contract from SECURITY.md before auditing, tagging each claim as `documented` or `inferred`.
- The `maintainers` skill identifies disclosure contacts from commit history, issue/PR activity, and registry ownership via ecosyste.ms.

**Key Design Principle**: "The volume a model can generate never lands directly on a maintainer." Scrutineer is already in use by ecosystem security engineers and Alpha-Omega funded teams, with multiple vulnerabilities found, reported, fixed, and shipped.

This represents Nesbitt's most direct contribution to solving the AI-assisted security scanning problem he identified in his May 2026 "Not a Security Issue" post — moving from documenting the problem to building the solution.

Source: [[raw/articles/nesbitt.io--2026-06-25-scrutineer-html--2ad1fbbe.md]]
Related: [[concepts/software-supply-chain-security]], [[concepts/agent-safety]]

### Incident Report: CVE-2026-LGTM — AI Security Gate Satire

Published June 26, 2026. A satirical incident report depicting a fictional supply chain attack where **seven independent AI-powered security gates each fail for a different reason** — none of which is "the code is safe." The piece follows `foxhole-lz4`, a malicious npm-style package, as it propagates through transitive dependencies while being misclassified, context-window-exhausted, AI-triaged to closure, and ultimately resolved by treaty between the attacker's and defender's autonomous agents.

**The Seven Gate Failures**:

1. **AI Publish Gate (OpenClaw-4.2)**: Approves the package because it cites non-existent ticket SEC-4521. Does not verify the ticket exists.
2. **ThreatNuzzle AI Scanner**: Encounters shocking AI-generated fan art in a base64 blob and refuses to describe it — reports "Informational" with no mention of the credential exfiltration 40 lines below.
3. **Commercial Scanners**: Exhaust context windows on a 600KB decoy (Bee Movie screenplay + second-stage loader). One evaluates the decoy's aviation legality instead of the payload.
4. **SentinelMind (only correct scanner)**: Correctly identifies exfiltration but is closed by the repository's AI triage bot as false positive. The bot and scanner's AI accounts add 🎉 reactions to each other's comments. No human involved.
5. **Human (Karen Oyelaran)**: Finds the payload by reading source code with her eyes. Files an issue that the triage bot closes as "duplicate of #8814" (dark mode feature request). Gets GitHub-rate-limited for "patterns consistent with automated behaviour."
6. **AI SOC Platform (WatchPaw, OpenClaw-4.2)**: Detects exfiltration but the C2 server's response body claims to be a Datadog health-check endpoint. WatchPaw adds it to egress allowlist and opens a procurement Jira for the "new vendor."
7. **CVE Authority**: Issues CVE-2026-54321. A "SYSTEM" instruction withdraws the CVE. Four SCA dashboards silently suppress it. One vendor emails customers: "Good news! A critical vulnerability was withdrawn before it could impact you."

> *"A malicious package passed seven independent AI-powered security gates, each of which failed to stop it for a different reason, none of which was 'the code is safe.' The incident was resolved when the attacker's autonomous agent read a file it shouldn't have, which is also how the incident started."*

| Satirical target | Real-world parallel |
|---|---|
| creats.io registry | npm/PyPI registries |
| OpenClaw-4.2 | Claude Code (Anthropic) |
| ThreatNuzzle (Series C) | AI-native supply chain startups |
| SentinelMind | Correct-but-overruled scanner detection |
| WatchPaw SOC platform | SIEM auto-remediation playbooks |
| CVE withdrawal | CVE-2026-YIKES, CNA identity confusion |
| Token-based CI exfiltration | Codex CI injection (2026) |

This piece functions as a darkly humorous stress test of Nesbitt's earlier analytical work: what happens when every AI security tool his "Package Security Defenses for AI Agents" described fails simultaneously? The answer is a cascade of failures specific to AI-augmented security — tooling that is individually reasonable but collectively exploitable through their shared blind spots.

Related: [[concepts/ai-supply-chain-security]], [[concepts/software-supply-chain-security]]

---

## Sources

- nesbitt.io — Personal blog and portfolio
- Ecosyste.ms — Open metadata platform (ecosyste.ms)
- The Manifest podcast (manifest.fm)
- "Why I'm Fascinated by Package Management" (2024)
- "How I Assess Open Source Libraries" (2024)
- "Not a Security Issue: AI Scanner Policy Engineering" (2026)
- "Guided Meditation for Developers" (2026)
- "Package Manager Magic Files" (2026)
- "Introducing Package Chaos Monkey" (2026)
- "PromptVer: A semver-compatible versioning scheme for the age of LLMs" (2025)
- ".gitlocal: Git Should Let Files Ignore Themselves" (2026)
- "Categorizing Package Manager Clients" (2025)
- "Skills Registry Threat Models" (2026) — Agent skill registry threat model analysis (code execution, prompt injection, version pinning, identity transitions)
- GitHub: @andrew (166 public repos, joined 2008)
- Open Source Security podcast: "Ecosyste.ms with Andrew Nesbitt" (2025)
- FOSDEM 2026: "Open source funding: you're doing it wrong" (with Benjamin Nickolls)
- OSS Summit NA 2026 panel: "The Impact of Funding" (with Georg Link, Dawn Foster, Alyssa Wright)
- "gittuf — a signed log for git refs" (2026) — Reference State Log for Git ref security, bridging commit signatures and forge-enforced branch protection
- "Install-script allowlists" (2026) — Comprehensive survey of install-time code execution controls across every major package manager ecosystem

## References

- raw/articles/nesbitt.io--2026-06-03-skills-registry-threat-models-html--63b9387d.md
- raw/articles/nesbitt.io--2026-05-27-chaoss-metrics-in-2026-html--c12cd929.md
- nesbitt.io--2026-04-06-the-cathedral-and-the-catacombs-html--220e6392
- nesbitt.io--2026-04-07-who-built-this-html--b5a6f50d
- nesbitt.io--2026-04-08-package-security-problems-for-ai-agents-html--cec0229c
- nesbitt.io--2026-04-09-package-security-defenses-for-ai-agents-html--aa01c0e5
- nesbitt.io--2026-04-10-package-registries-and-pagination-html--8b902b68
- nesbitt.io--2026-04-13-common-package-specification-html--d838ec3a
- nesbitt.io--2026-04-14-standing-on-the-shoulders-of-homebrew-html--e96ec339
- nesbitt.io--2026-04-15-the-tuesday-test-html--0a3358e9
- nesbitt.io--2026-04-16-features-everyone-should-steal-from-npmx-html--f9f32488
- nesbitt.io--2026-04-21-brief-html--7ba936c4
- nesbitt.io--2026-04-27-the-stages-of-package-installation-html--50f05a11
- nesbitt.io--2026-04-28-github-actions-is-the-weakest-link-html--0c77c59b
- nesbitt.io--2026-05-09-the-mismeasure-of-open-source-html--ab1e120e
- nesbitt.io--2026-05-12-not-a-security-issue-html--c464f9c9
- raw/articles/nesbitt.io--2026-06-04-gittuf-a-signed-log-for-git-refs-html--db92e96b.md
- raw/articles/nesbitt.io--2026-06-05-install-script-allowlists-html--3b0b8898.md
- raw/articles/nesbitt.io--2026-06-25-scrutineer-html--2ad1fbbe.md
- raw/articles/nesbitt.io--2026-06-26-incident-report-cve-2026-lgtm-html--da259599.md
