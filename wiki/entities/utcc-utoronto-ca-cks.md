---
title: Chris Siebenmann
created: 2026-04-09
updated: 2026-04-10
tags:
- person
- blogger
- hn-popular
- sysadmin
- unix
- linux
- free-software
aliases:
- utcc.utoronto.ca/~cks
- Chris Siebenmann Wandering Thoughts
- cks
---

# Chris Siebenmann

| | |
|---|---|
| **Blog** | [Wandering Thoughts](https://utcc.utoronto.ca/~cks/space/blog/) |
| **RSS** | https://utcc.utoronto.ca/~cks/space/blog/?atom |
| **Mastodon** | [@cks](https://mastodon.social/@cks) |
| **Twitter** | [@thatcks](https://twitter.com/thatcks) |
| **Role** | Unix sysadmin, blogger |
| **Known for** | Long-running Unix/Linux/sysadmin blog, deep dives into systemd, Solaris, package management, and infrastructure operations |
| **Bio** | System administrator at the University of Toronto Computer Centre. Has been writing about Unix, Linux, and systems administration since the early 2000s. Runs "Wandering Thoughts" — a blog characterized by its empirical, experience-driven analysis of systems software and operational practices. |

## Core Ideas

Chris Siebenmann is an **empirical systems thinker** — a career sysadmin who writes about technology from the trenches rather than from theory. His blog is characterized by a distinctive voice: skeptical of hype, grounded in actual operational experience, and willing to change his mind when the evidence demands it.

### Log Messages Are Not Promises

In one of his most influential essays, ["Programs shouldn't commit to fixed and predictable log messages"](https://utcc.utoronto.ca/~cks/space/blog/programming/LogMessagesNoPromises), Siebenmann argues that log messages should remain flexible and unpromised:

> *"The simple problem with making promises about what your program's logs will contain is that promises create official APIs. Everything you promise about your logs becomes part of your program's functional API."*

His thesis: every commitment about log format becomes an API that constrains future development. When programs need to change behavior, they're forced to either break log consumers or produce inaccurate messages to maintain compatibility. Instead, **important observability data should be surfaced through metrics, not logs** — metrics force deliberate design, while logs remain free to evolve.

He explicitly distinguishes this from opposing structured logging: *"I'm not against structured logging; I think it's a fine idea. I'm against making promises about exactly what specific messages and other contents your structured log messages will contain."*

### Shell Script Clarity Over Cleverness

In ["Shell scripts should be written to be clear first"](https://utcc.utoronto.ca/~cks/space/blog/programming/ShellScriptsBeClearFirst), Siebenmann pushes back against shell script minimalism and "code golfing":

> *"Shell scripts more often lack clarity than they lack performance, so I'm strongly of the feeling that you should be biased toward clarity in your shell scripting."*

He notably reversed his long-held position on "useless use of cat":

> *"I used to be on the 'anti-cat' side, but more and more I am coming to feel that 'cat file | cmd' is often clearer than 'cmd < file'."*

His clarity budget principle: every clever idiom you use costs clarity. Since shell is already an indirect, opaque language compared to proper programming languages, you can't afford to spend your clarity budget on efficiency tricks that no longer matter on modern hardware.

### The Temptation of Shell Scripts

Siebenmann's ["Shell Script Temptation"](https://utcc.utoronto.ca/~cks/space/blog/2022/04/23/) essay is a candid self-reflection:

> *"It's an article of faith in many quarters that you shouldn't write anything much as a shell script and should instead use a proper programming language. I generally agree with this in theory, but recently I went through a great experience of why this doesn't work in practice."*

He describes how what starts as a "simple thing" in shell scripting grows incrementally — each step seems easy enough — until you end up with a complex, unmaintainable script. The lesson: **the danger of shell scripts isn't that they're hard to write; it's that they're too easy to keep adding to.**

### Three Types of Service Stop

In ["Three Types of Service Stop"](https://utcc.utoronto.ca/~cks/space/blog/2017/09/12/), Siebenmann identifies that Unix init systems conflate three distinct shutdown contexts that require different behavior:

1. **Service restart** — You want the service to come back up quickly; graceful cleanup may not be necessary
2. **Administrative stop** — You want a controlled, clean shutdown with proper cleanup
3. **System shutdown** — Everything must stop; speed and order matter more than graceful cleanup

His insight: *"The first and the third context can easily conflict. The only time when they're all the same is when you have a simple daemon."* This analysis explains many of the frustrations sysadmins have with systemd's one-size-fits-all service management.

### Dependency Cooldowns for Supply Chain Security

Most recently (March 2026), Siebenmann has been advocating for **dependency cooldowns** in Go's module system — waiting a period before adopting new dependency versions to let the community inspect them:

> *"While one of Go's famous features is 'minimum version selection', you might think this already protects you. Unfortunately, this is not the actual observed reality. People update to new versions very quickly, often through automated tooling."*

He argues that cooldowns should be configurable in `go.mod` rather than as environment variables, because **defaults and avoiding mistakes are more important than opt-in configurations**.

### Empirical Decision-Making

A recurring theme across Siebenmann's writing is **empiricism over dogma**. Whether it's HTTP User-Agent behavior ("On today's web, HTTP results depend on the HTTP User-Agent you use"), system retention ("Here in 2026, we're retaining old systems instead of discarding them"), or package management ("Using 'pkg' for everything on FreeBSD 15 has been nice"), he grounds his analysis in actual data and observed behavior rather than theoretical ideals.

## Key Quotes

> *"I think that this unpredictability [of log messages] is a good thing and programs should make at most very limited promises otherwise."*

> *"Shell scripts more often lack clarity than they lack performance."*

> *"I used to be on the 'anti-cat' side, but more and more I am coming to feel that 'cat file | cmd' is often clearer than 'cmd < file'."*

> *"It's an article of faith in many quarters that you shouldn't write anything much as a shell script and should instead use a proper programming language. I generally agree with this in theory, but recently I went through a great experience of why this doesn't work in practice."*

> *"The larger a system's API (or set of APIs), the more complicated it is to maintain and evolve it. The fewer APIs you give a system, the better."*

## Related

- [[unix-philosophy]] — Siebenmann's work is grounded in Unix operational principles
- [[systemd]] — Frequent topic of analysis and critique
- [[supply-chain-security]] — Dependency cooldowns discussion
- [[simon-tatham]] — Another Unix-oriented blogger with similar pragmatism
- [[concepts/ai-observability.md]] — Logs vs metrics debate

## Sources

- [Programs shouldn't commit to fixed and predictable log messages](https://utcc.utoronto.ca/~cks/space/blog/programming/LogMessagesNoPromises) (Aug 2023)
- [Shell scripts should be written to be clear first](https://utcc.utoronto.ca/~cks/space/blog/programming/ShellScriptsBeClearFirst) (May 2022)
- [The temptation of writing shell scripts](https://utcc.utoronto.ca/~cks/space/blog/2022/04/23/) (Apr 2022)
- [Three types of service stop](https://utcc.utoronto.ca/~cks/space/blog/2017/09/12/) (Sep 2017)
- [I think dependency cooldowns would be a good idea for Go](https://utcc.utoronto.ca/~cks/space/blog/programming/GoDependencyCooldownsGood) (Mar 2026)
- [On today's web, HTTP results depend on the HTTP User-Agent you use](https://utcc.utoronto.ca/~cks/space/blog/web/UserAgentMatters) (Mar 2026)
- [Here in 2026, we're retaining old systems instead of discarding them](https://utcc.utoronto.ca/~cks/space/blog/tech/OldSystemsIn2026) (2026)
