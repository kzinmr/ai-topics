---
title: "PHP2Shell — AI-discovered core PHP RCE (CVE-2026-109618/109619)"
created: 2026-10-21
updated: 2026-10-26
type: event
tags: [security, vulnerability, vulnerability-discovery, autonomous-security-agents, ai-infra-security, ai-safety, wiz, announcement, event]
sources:
  - raw/newsletters/2026-10-25-the-signal-old-holes-new-helpers-and-ai-in-a-box.md
  - raw/articles/wiz.io--blog-php2shell-php-rce--2026-10-21.md
  - raw/articles/lwn.net--articles-1101687--84a881d4.md
  - https://www.wiz.io/blog/php2shell-php-rce
  - https://jackalsyn.com/posts/php-up-2026.html
---

# PHP2Shell — AI-discovered core PHP RCE (2026)

## Overview

On **October 21, 2026**, Wiz Research disclosed **PHP2Shell**, a set of critical
memory-safety vulnerabilities in the **core PHP engine** — the scripting language
that powers ~70% of the web (WordPress, Drupal, Joomla, MediaWiki/Wikipedia). The
flaws allow **unauthenticated remote code execution** and **Heartbleed-style
process-memory disclosure** (leaking passwords, tokens, API keys) in PHP itself,
independent of any application running on top of it.

The event is significant less for the CVEs themselves than for **how they were
found**: the vulnerable code had sat in the PHP codebase for over a decade, but
its exploitability required a chain of steps "at the edge of what human
researchers could practically achieve." **Frontier AI models collapsed that
barrier.** Wiz frames PHP2Shell as the AI-era analogue of Heartbleed (2014) and
Log4Shell (2021) — a turning point that changes how "vulnerable in practice" is
defined.

## Key facts

| Detail | Value |
|--------|-------|
| **Disclosed by** | Wiz Research (Sagi Tzadik, Shir Tamari, Nir Ohfeld, Tomer Schwartz) — independently found by **Calif** and **OpenAI** (see below) |
| **CVEs** | CVE-2026-109618, CVE-2026-109619 |
| **Severity** | Up to CVSS 9.2 (Wiz framing) |
| **Affected** | Nearly every PHP version since 5.4 (~10+ years) |
| **Impact** | Unauthenticated pre-auth RCE on WordPress/Drupal/Joomla; application-agnostic remote memory disclosure |
| **AI tooling used** | Wiz Atlas, **Gemini 4 Argon**, **GPT-5.6 Sol** |
| **Patch date** | 2026-10-21 (coordinated) |
| **Disclosure start** | 2026-08-19 (first vuln found); reported to PHP team 2026-08-24 |

**Three independent discoveries.** The page above follows Wiz's own account, but two
other parties found the same flaws (The Signal, Oct 25): **Calif** spotted it on
**Aug 1** with AI assistance and reported a working attack on **Aug 11**; **OpenAI
and Wiz** found it independently on their own, and OpenAI says it **led the group
that prepared the fixes** before publication. The NSA advised organisations that
could not update to **take systems offline**, and **Amazon reportedly saw attack
attempts before the news broke**. See [[concepts/ai-vulnerability-discovery]],
[[concepts/autonomous-security-agents]] and the OpenAI *Patch the Planet* program
([[entities/openai]], [[entities/wiz]]).

## The root cause

All flaws stem from how PHP handles **fatal errors — especially out-of-memory
errors — while processing requests**. A fatal error mid-request can leave a
corrupted internal PHP state (dangling pointers in `BG(unserialize)`, `PS(id)`,
`EG(last_fatal_error_backtrace)`, OPcache shared maps). A later request or worker
reuses that stale cross-request state → use-after-free / type-confusion
primitives. Four exploitable instances were reported (grouped under two CVEs);
more tracked and untracked variants exist.

Demonstrated targets: WordPress, Drupal, Joomla latest container images — but the
primitives live at the engine level, so even a "Hello World" app on a vulnerable
PHP can be exploited. The memory-disclosure bug works even when the app never
calls `session_start()`.

## Why it is an "AI inflection point"

The durable claim for this wiki: **AI changed the economics of exploit
development.** The flaw was old; what changed was the ability to understand the
weakness and turn it into a working exploit. Wiz's thesis:

> With frontier AI models and the right tools, a single researcher completed in a
> week what previously would have taken a world-class team months of work.
> Vulnerabilities that once seemed impractical to exploit become viable targets.

This makes it a canonical case in [[concepts/autonomous-security-agents]] and
[[concepts/vulnerability-discovery]] alongside the Wiz/Snowflake CI/CD case.

## Contested: the independent (jackalsyn) account

There is a **contested account** of the exploit chain. An independent researcher
(jackalsyn.com "PHP-UP-2026", corrected 2026-10-21) argues the headline cached-
pointer RCE chain is "DEAD at the addref" (no free, no RCE), and the real,
ASAN-confirmed bug is a serialize-state cross-request use-after-free that is
prefork-only, memory-safety-only, **CVSS 5.3 Medium** — not the CVSS 9.2 pre-auth
RCE Wiz emphasizes. The independent write-up also notes someone ran AI tools
against PHP and publicly disclosed a PoC ahead of the embargo.

Both accounts are retained per wiki policy (do not erase contradictions):
the AI-discovery-of-longstanding-flaws narrative is not disputed; the severity and
reliability of the RCE chain is. LWN's "Critical PHP security update coming"
captured the pre-disclosure advisory context.

## The "Defender's Window" (OpenAI framing) and the timeline gap

OpenAI labelled the interval between discovery and mass exploitation the
**"Defender's Window"** — the period after a flaw becomes findable but before it is
weaponised at scale. The Signal (Alex Banks, Oct 25) reconstructs the calendar and
is sceptical of the framing: *"I'd call it a lucky head start that only counts if
you use it."*

| Milestone | Date / duration |
|-----------|-----------------|
| Root cause introduced | PHP 5.4 era, **2012** (~14 years) |
| Calif's team spots the flaw (AI-assisted) | **Aug 1, 2026** |
| Calif reports a working attack | **Aug 11, 2026** (10 days to weaponise) |
| Patch ships (PHP Foundation, one day early after bug IDs leaked) | **Oct 21, 2026** (71 days after report) |

Two numbers carry the argument: **10 days** from spotting to a working exploit,
versus **71 days** to ship the fix. AI collapsed the discovery/exploit side of the
equation; the remediation side did not speed up, and the same models are equally
available to attackers. Banks also notes the patch was pulled forward a day because
the CVE IDs leaked, and that **a third of PHP sites still run PHP 5 or 7**, which
received no official fixed release at all (source patches only for some versions) —
so the "window" is not evenly distributed.

Independent corroboration of the non-event: Calif published a follow-up titled
**"PHP hasn't caused a disaster yet"**, and Nathan Lambert reports that despite the
Mythos/open-model panic that followed the disclosure, **mass exploitation has not
materialised** — no wave of scanning and damage appeared after the patch went
public. A circulating (unverified) claim that a "DeepSeek swarm" was performing
mass automated fixing of vulnerable installs was described by someone at a large
cloud provider; Lambert's own verdict: *"Coin flip on if it's real."* Brand's
counter-observation on the defence side is a human one: SMEs simply do not patch —
friends at small/medium businesses had not updated PHP versions in years and were
already exposed to other, still-unexploited bugs.

Related same-week incidents that fed the "everything is insecure" impression (see
[[entities/litellm]] for the LiteLLM 1.107.0 PyPI compromise): security practitioners
dubbed October 2026 **"Black October"**, with one circulating list counting ~27 major
incidents in about a day.

## Detection signals (pre-patch)
- Unusual multipart requests followed by memory-limit errors or repeated HTTP 500s
- Unexpectedly large/malformed `PHPSESSID` response cookies
- Unexplained PHP worker churn

## X reactions

- **@hynek** (Hynek Schlawack, LAMP shared webhoster): "looks like some PHP RCE
  (CVE-2026-109618 / CVE-2026-109619 / PHP-UP-2026) deets started to drop. as a
  LAMP shared webhoster we're obviously Very Excited™" (2026-10-21)
- **@steipete** (Peter Steinberger): link-dropped the Wiz post (2026-10-21)

## Related

- [[entities/wiz]] — the discovering security research team
- [[concepts/autonomous-security-agents]] — the broader pattern
- [[concepts/vulnerability-discovery]] — AI-driven discovery
- [[entities/hynek-schlawack]] — reacted as a LAMP webhoster
- [[entities/peter-steinberger]] — amplified the disclosure

## Sources

- [[raw/articles/wiz.io--blog-php2shell-php-rce--2026-10-21.md]] — full Wiz writeup
- [[raw/articles/lwn.net--articles-1101687--84a881d4.md]] — LWN advisory coverage
- [Wiz blog](https://www.wiz.io/blog/php2shell-php-rce)
- [Independent write-up (jackalsyn)](https://jackalsyn.com/posts/php-up-2026.html)
