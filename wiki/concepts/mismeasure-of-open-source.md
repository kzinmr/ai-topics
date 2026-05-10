---
title: "The Mismeasure of Open Source"
type: concept
created: 2026-05-10
updated: 2026-05-09
tags:
  - open-source
  - evaluation
  - economics
  - security
  - benchmark
sources:
  - https://nesbitt.io/2026/05/09/the-mismeasure-of-open-source.html
  - raw/articles/nesbitt.io--2026-05-09-the-mismeasure-of-open-source-html--ab1e120e.md
---

# The Mismeasure of Open Source

> "The quiet system library with one tired maintainer and no dashboard footprint is exactly what we built all of this tooling to find, and it remains the thing the tooling is structurally worst at seeing."
>
> — Andrew Nesbitt, May 2026

## Overview

Andrew Nesbitt delivers a comprehensive critique of open source criticality scoring models, arguing that despite a decade of effort and far more data, all major scoring systems inherit the same fundamental blind spots. The article identifies **six systemic failures** in how we measure open source health, risk, and funding needs.

## The Six Blind Spots

### 1. Missing Read as Zero

The most consequential mistake: treating **absence of a signal as a low value** of that signal.

- **Download counts**: Go modules, C libraries (apt, dnf, apk, vendoring, static linking) publish no per-module download counts. If a model's entry filter is "top N by downloads," these ecosystems are excluded before scoring begins.
- **GitHub issues**: Zero might mean no users, or it might mean bugs tracked in Bugzilla, mailing lists, Launchpad, or Debian BTS.
- **FUNDING.yml**: Absence could mean nobody is paying, or that maintainers are on Red Hat's payroll.
- **OpenSSF Scorecard**: Missing result tells you nothing about security if the project is hosted on cgit.

**The Entry Filter Problem**: The scoring formula gets debated, but the candidate set makes the bigger decision silently. The 2015 CII census scored Debian packages above a popcon threshold — sudo and polkit weren't misranked, they were never in the input. Modern equivalents start from "top N% of registry downloads" or "packages with resolvable GitHub URL," and excluded projects disappear without a trace.

### 2. Easy to Collect, So It Must Mean Something (Streetlight Effect)

Availability mistaken for relevance. The GitHub and registry APIs are the lamp post; most actual risk lies in the dark.

| Metric | What It Actually Measures | What People Assume |
|--------|--------------------------|-------------------|
| **Download counts** | CI cache misses, mirror traffic, bot scans | Users or installations |
| **GitHub stars** | People with GitHub accounts who clicked a button | Popularity, quality |
| **CVE count** | Audit attention received, not vulnerabilities present | Risk level |
| **Code complexity** | Branches and operators visible to static analyzers | How hard to replace |
| **Commit cadence** | Git log activity | Maintenance health |

**Key examples:**
- ICU (linked into every browser, Android, JDK, Node): ~3,500 stars
- c-ares (async DNS for curl, Node, gRPC): ~2,100 stars
- libxml2's GitHub mirror: 735 stars
- ~6 million suspected fake stars on GitHub (2019–2024), rate climbing sharply

**CVE count as inverse signal**: OpenSSL and the Linux kernel have hundreds of CVEs because researchers look at them constantly. An unfuzzed C parser unexamined since 2014 has none — and is more dangerous for it. CVE count tracks audit attention, not vulnerability presence.

**The coding agent problem**: Claude Code and similar agents now support scheduled/repeating tasks, so repositories accumulate "Weekend at Bernie's" commits — plausible-looking maintenance authored under a human's name with no human in the loop. Bot-only category is large enough that activity metrics ignoring authorship are measuring the bots.

### 3. One Number, Many Units

Comparing absolute values across ecosystems produces nonsense because the **units are different even when the column header is the same**:

- **npm downloads**: Mostly CI cache misses
- **Homebrew analytics**: Pings from macOS developer laptops
- **Debian popcon**: Opt-in reports from shrinking population, never representative of servers/containers

**Dependent counts**: npm's culture of tiny single-purpose packages means a string-padding helper has tens of thousands of declared dependents. A C compression library statically linked into every browser, database, and game has a few dozen — because C dependencies are `#include`, vendored files, git submodules, or CMake lines, none of which produce manifest edges a registry crawler can follow.

**Package granularity**: A Rust workspace might publish 40 crates from one repo where a Python project of the same size publishes one package. The Rust project shows up as 40× nodes in the graph, internal edges inflate PageRank, and the same maintainers get counted 40× in any bus-factor sum.

### 4. GitHub as the Visible Universe

Most models lean on GitHub API for everything not a registry field. By package count, most open source is on GitHub — but **projects hosted elsewhere are disproportionately the old low-level infrastructure these models exist to find**.

**PostgreSQL, SQLite, GnuPG, glibc, FFmpeg, and most GNU projects** run primary development on mailing lists, self-hosted cgit, Gerrit, or Savannah. Some have read-only GitHub mirrors — which the API scores as if they were the real project.

**curl's contributor fallacy**: THANKS file lists 3,600+ contributors, but GitHub API returns a few hundred (only those linkable to accounts). Bus-factor formulas then report curl as 1, because Daniel Stenberg authored over half the commits.

**Lifetime totals mislead**: A project with 80 contributors in 2012 and one exhausted person today shows reassuring headcount. No field exists anywhere in the API for whether that one person is close to walking away.

**OpenSSF Scorecard's GitHub bias**: Checks like Branch-Protection, Token-Permissions, Dependency-Update-Tool, CI-Tests detect GitHub features, not security properties. A project with self-hosted Buildbot CI, mailing-list patch review, and 20 years of careful security process scores **worse** than a weekend template repo with default Actions enabled. And once scores drive funding decisions, **Goodhart's Law** kicks in: projects enable checkboxes rather than doing the work.

### 5. Identity Resolution Failures

The same code appears under different names across ecosystems:
- libcurl = `curl` (Homebrew), `libcurl4` (Debian), `pycurl` (PyPI), `curl-sys` (crates.io), `curl/curl` (GitHub)
- Models that don't unify these hold five separate low-scoring entries for one risk surface

Conversely, one repo ships dozens of artifacts:
- LLVM, GCC, coreutils, util-linux, BusyBox each ship dozens of separately-named packages
- Models that assume one package = one repo either pick one artifact or count maintainers dozens of times
- Several models exclude these projects entirely because complexity metrics timeout on repos that size — **the criticality scoring has a hole exactly where the most critical projects sit**

### 6. Funding You Can't See

Public tip-jar layer (GitHub Sponsors, FUNDING.yml, Open Collective) is a **thin film** over a much larger, almost entirely opaque body of:
- Corporate salary (maintainers employed by Red Hat, Google, Intel, Canonical, hardware vendors)
- Foundation grants disbursed without public reporting
- Support revenue

A model reading only the public layer marks a project with a salaried team as **unfunded** while treating an enabled but barely-used Sponsors button as evidence of sustainability.

## The Compound Case

Individually, each blind spot mismeasures some projects in some direction. For the bulk of modern, registry-published, GitHub-hosted packages, **errors roughly cancel out**.

**But errors correlate**, because a project old enough to predate GitHub is disproportionately likely to be:
- Written in C
- Distributed by vendoring rather than manifest dependency
- Developed over mailing list
- Funded through someone's salary
- Low-churn because the format it implements stopped changing

So the same project gets: undercounted on downloads, dropped from dependency graph, nulled on contributor metrics, scored low on Scorecard, marked unfunded, and flagged as inactive — **all at once, for six different expressions of the same underlying fact: it doesn't look like an npm package.**

## Implications for AI Agent Infrastructure

This analysis has direct relevance to the AI agent ecosystem:

1. **Agent tool selection**: If agents use GitHub stars/downloads to pick dependencies, they inherit the same blind spots as criticality scoring models
2. **Supply chain risk**: The most critical infrastructure (C libraries, system packages) is least visible to automated scanning
3. **Funding allocation**: Agent-driven funding recommendations would systematically miss salaried maintainers
4. **Measurement integrity**: Any agent evaluating "project health" via API signals alone will produce the same compound errors Nesbitt identifies

## Key Quotes

> "The scoring formula in a criticality model is the part that gets discussed, but the candidate set it runs over has usually made the bigger decision already."

> "A model reading only the public layer will mark a project with a salaried team as unfunded while treating an enabled but barely-used Sponsors button as evidence of sustainability."

> "The quiet system library with one tired maintainer and no dashboard footprint is exactly what we built all of this tooling to find, and it remains the thing the tooling is structurally worst at seeing."

## Related

- [[entities/andrew-nesbitt]] — Author; ecosyste.ms maintainer, open source metadata researcher
- [[concepts/criticality-scoring]] — Open source project criticality measurement
- [[concepts/supply-chain-security]] — Software supply chain risks
- [[entities/daniel-stenberg]] — curl maintainer, subject of several examples in this article

## References

- [The Mismeasure of Open Source](https://nesbitt.io/2026/05/09/the-mismeasure-of-open-source.html) — nesbitt.io, May 9, 2026
- [FOSDEM 2025 talk](https://fosdem.org/2025/) — Ben Nickolls & Andrew Nesbitt on open source funding
- [xz-utils backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) — Criticality scoring failure case (xz-utils scored 6/13 in 2015 CII census, row 254)
