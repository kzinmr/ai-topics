---
title: "PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet"
url: "https://www.wiz.io/blog/php2shell-php-rce"
fetched_at: 2026-10-21T22:35:00+00:00
source: "wiz.io"
tags: [blog, raw]
---

# PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet

Source: https://www.wiz.io/blog/php2shell-php-rce
Authors: Sagi Tzadik, Shir Tamari, Nir Ohfeld, Tomer Schwartz (Wiz Research)
Published: 2026-10-21

## Executive Summary

Wiz Research uncovered multiple critical vulnerabilities in core PHP, a popular
general-purpose scripting language that powers 70% of all websites in the world.
Successful exploitation could allow attackers to take control of affected servers,
steal sensitive data, and deface the websites running on them.

PHP is a backbone of the web: it powers WordPress, Joomla, Drupal, Wikipedia's
MediaWiki, and many others. These vulnerabilities include memory disclosure and
unauthenticated remote code execution in PHP itself, independent of the
application running on top of it, putting every affected website in immediate
risk. Every PHP version released in the last decade is affected by at least one
of these vulnerabilities, going back to version 5.4.

On October 21, 2026, PHP released the patch fixing multiple memory-safety
vulnerabilities in the core engine. These findings rank among the most severe
vulnerabilities discovered in PHP, and arguably in software history. The
underlying flaws had been present for decades, but demonstrating their
exploitability required an exceptionally complex chain of steps, at the edge of
what human researchers could practically achieve. Frontier AI models
substantially reduced that barrier, turning a longstanding flaw into an exploit.

## Overview

The issues stem from key architecture decisions, some made over a decade ago,
and are grouped under two CVEs, with severity reaching CVSS 9.2. The work grew
into a cross-industry effort to protect customers, find variants, deploy
detections and mitigations, and verify a patch in time for coordinated
disclosure. Nearly every PHP version is affected, including releases dating back
to PHP 5.4.

Wiz positions PHP2Shell alongside Heartbleed (2014) and Log4Shell (2021) as a
potential turning point for the AI era, illustrating how AI can change the
practical exploitability of longstanding vulnerabilities. Building the exploit
required chaining multiple flaws and adapting to each target's memory layout
through repeated testing and debugging. Frontier models were critical to making
this process practical, enabling the team to develop and adapt working exploits
across multiple applications in hours.

Wiz used **Wiz Atlas, Gemini 4 Argon, and GPT-5.6 Sol** throughout this
research, with Gemini 4 Argon making an invaluable contribution to finding the
vulnerability, exploit development, attack detection, and validation of the
patch. OpenAI and Calif also published blogs on the vulnerability. Collaboration
partners for customer guidance: Google Cloud, Cloudflare, AWS, Microsoft,
Automattic, Fastly, Akamai, Imperva, Vercel, and many others.

## The Vulnerabilities

All of the disclosed vulnerabilities are memory-safety issues that stem from bugs
in how PHP handles fatal errors while processing requests, particularly
out-of-memory errors. These bugs can leave a corrupted internal PHP state behind
after a request ends unexpectedly. A later request or worker can reuse that stale
state, leading to memory disclosure or corruption.

| Tracking ID | Bug | What an attacker can achieve |
|---|---|---|
| CVE-2026-109618 | Upload-progress unserializer use-after-free | Unauthenticated disclosure of PHP worker memory; pre-auth RCE on WordPress, Drupal, Joomla; application-agnostic remote memory disclosure |
| CVE-2026-109619 | Fatal-error backtrace use-after-free / OPcache type confusion | Corrupt process memory and execute code; corrupt shared PHP state and execute code; pre-auth RCE on Drupal and WordPress |

While this post covers four instances of exploitable bugs (grouped under two
CVEs), there are other tracked — and likely untracked — variants in the PHP
codebase with different exploitation requirements and impacts. The patch fixes
the issue at its core and eliminates all variants in the patched release.

## Impact

Wiz combined the vulnerabilities into a single exploit script, **php2shell**, and
demonstrated unauthenticated remote code execution on deployments of WordPress
(`wordpress:latest`), Drupal (`drupal:latest`), and Joomla (`joomla:latest`)
using their latest container images. The vulnerabilities are in PHP itself — even
a simple "Hello World" application running on an affected PHP version can be
vulnerable.

Separately, attackers could read sensitive data from the PHP process's memory —
passwords, tokens, API keys — without needing to achieve RCE.

## The AI inflection point

The vulnerable code had been present for more than a decade. Turning these flaws
into working exploits required chaining multiple bugs and accounting for how PHP
allocates and reuses memory across requests. Pre-AI, this manual work would be
difficult to implement and even harder to scale. With AI this is no longer a
barrier. LLMs help adapt an exploit to different PHP versions, configurations and
memory layouts; with testing and debugging tools, models can analyze failures and
iterate on adjustments, reducing the specialist effort required for each target.

> "With frontier AI models and the right tools, a single researcher completed in
> a week what previously would have taken a world-class team months of work. This
> changes the economics of both discovery and exploitation. Vulnerabilities that
> once seemed impractical to exploit become viable targets."

Raluca Ada Popa (Head of Gemini Security, Google DeepMind): "For over a decade,
these critical vulnerabilities remained unaddressed because vulnerability
discovery and exploitation were incredibly complex. We're pleased to see Gemini
4 Argon help defenders bridge that gap, finding vulnerabilities and helping patch
them."

## Technical deep dive (summary)

- **Upload-progress unserializer use-after-free**: PHP's Session module can decode
  session data during upload-progress handling in the pre-initialization window.
  The decoder stores request-owned bookkeeping in `BG(unserialize)`. A fatal
  allocation failure can interrupt this path, destroy the request heap and leave
  the unserializer's global state published. A later request on the same worker
  consumes attacker-reclaimed memory as live unserializer bookkeeping.
- **Remote process-memory disclosure**: PHP parses RFC1867 multipart requests
  during request startup, before normal module initialization. An out-of-memory
  error can abort the request before cleanup, leaving `PS(id)` pointing to a freed
  allocation. A later request URL-encodes reclaimed heap contents into a
  PHPSESSID response cookie. Works even when the application never calls
  `session_start()`, making it application-agnostic.
- **Fatal-error backtrace use-after-free**: PHP retains the backtrace of the most
  recent fatal error in `EG(last_fatal_error_backtrace)`. A fatal OOM error can
  destroy the request heap without undefining that executor-global value, leaving
  a dangling pointer across requests.
- **OPcache type confusion**: OPcache persists compiled structures in shared
  memory; an allocation failure during `zend_accel_script_persist()` leaves the
  process-local frontier advanced while shared state still considers slots
  available, creating a cross-worker type confusion.

Defender signals until patched: unusual multipart requests followed by
memory-limit errors or repeated HTTP 500 responses, unexpectedly large or
malformed PHPSESSID response cookies, and unexplained PHP worker churn.

## Responsible disclosure timeline

- August 19, 2026: Wiz Research discovers the first PHP vulnerability using Wiz
  Atlas, Gemini 4 Argon, and GPT-5.6 Sol.
- August 20, 2026: Unauthenticated RCE confirmed against Drupal.
- August 21, 2026: Unauthenticated RCE confirmed against WordPress.
- August 24, 2026: Reported to the PHP security team.
- September 21, 2026: PHP acknowledges and begins developing a coordinated fix.
- October 21, 2026: Patched PHP releases become available; public disclosure.

## Related independent write-up (jackalsyn.com)

Hynek Schlawack shared an independent researcher write-up at
https://jackalsyn.com/posts/php-up-2026.html ("PHP-UP-2026"). That write-up
(CORRECTED 2026-10-21) reports a more skeptical view of the specific exploit
chain: the cached-pointer chain is "DEAD at the addref" (no free, no RCE) and the
real bug is a serialize-state cross-request use-after-free, ASAN-confirmed at
`var.c:756`, prefork-only, memory-safety only, CVSS 5.3 Medium. It also notes
someone reportedly ran AI tools against PHP and publicly disclosed a PoC before a
patch existed. This is a contested account relative to Wiz's CVSS 9.2 pre-auth
RCE framing. See LWN "Critical PHP security update coming"
(https://lwn.net/Articles/1101687/) for the PHP team's advisory context.

## X reactions noted in the scan

- @hynek (Hynek Schlawack): "looks like some PHP RCE (CVE-2026-109618 /
  CVE-2026-109619 / PHP-UP-2026) deets started to drop. as a LAMP shared webhoster
  we're obviously Very Excited™" (2026-10-21)
- @steipete (Peter Steinberger): link-drop of the Wiz post (2026-10-21)
