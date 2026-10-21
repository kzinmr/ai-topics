---
source: https://www.anthropic.com/research/attack-surface-reduction
author: Chris Rohlf (Team Frontier Red Team, Anthropic)
date: 2026-10-20
fetched: 2026-10-21
type: article
title: "Using Claude to reduce the attack surface of code"
sha256: 67390206a651e75a7ea2d818221b0e59e1a4c8edcae288bf40a1288e06d0b42b
---

# Using Claude to reduce the attack surface of code

Anthropic Research — Team Frontier Red Team, Chris Rohlf. Published Oct 20, 2026.

## Summary

Automated attack surface analysis and reduction can meaningfully improve the security of
deployed software in the near term. Over the past year Anthropic published data showing
frontier AI models are more than capable of discovering and exploiting security
vulnerabilities. Showing how previously unknown vulnerabilities might be exploited is only
the start of what frontier models can do for cyber *defense*. This post summarizes initial
research into automated attack surface analysis and reduction: using AI models to map the
code that is reachable, then removing or restricting access to anything a given deployment
doesn't need to expose.

## Key idea: reduce reachability, don't just patch bugs

- Securing software by finding and fixing individual vulnerabilities alone scales poorly:
  fixing even a critical vulnerability tells you nothing about the vulnerabilities that
  remain.
- By contrast, **reducing code reachability** can reduce the severity of *unknown*
  vulnerabilities, including ones under active exploitation.
- These techniques don't remove the unknown vulnerabilities in the code, but they make them
  harder to reach, and thereby reduce their severity.
- Minimizing a codebase's attack surface yields better security *without ever having to find
  or fix an individual vulnerability*.

## Method & results

- Claude was run over **25 open-source projects** (a variety of languages).
- It discovered **493 issues** — reachable code that the deployment didn't need to expose.
- The aim is to show Claude can meaningfully, and economically, improve software security
  through attack-surface reduction, and that developers can apply similar techniques to their
  own code.

## Framing

- Software tends to become more complicated over time, with new layers of abstraction —
  growing the reachable attack surface.
- Attack surface reduction is a defensive complement to AI-driven vulnerability discovery:
  rather than enumerating and patching each bug, shrink what an attacker can reach at all.
