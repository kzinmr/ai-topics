---
title: "Surprisingly Turing-Complete"
source: https://gwern.net/turing-complete
author: Gwern Branwen
publication: gwern.net
date: 2012-12-09
modified: 2022-12-17
type: essay
tags: [turing-completeness, emergence, complexity, security, weird-machines]
---

# Surprisingly Turing-Complete

## Core Philosophical Argument

Turing-completeness (TC) is (avoiding pedantically rigorous formal definitions) the property of a system being able to, under some simple representation of input & output, compute any program of interest, including another computer in some form.

TC, besides being foundational to computer science and understanding many key issues like "why a perfect antivirus program is impossible", is also weirdly *common*: one might think that such universality as a system being smart enough to be able to run any program might be difficult or hard to achieve, but it turns out to be the opposite -- it is difficult to write a useful system which does *not* immediately tip over into TC. "Surprising" examples of this behavior remind us that TC lurks everywhere, and security is extremely difficult.

I like demonstrations of TC lurking in surprising places because they are often a display of considerable ingenuity, and feel like they are making a profound philosophical point about the nature of computation: computation is not something esoteric which can exist only in programming languages or computers carefully set up, but is something so universal to any reasonably complex system that TC will almost inevitably pop up unless actively prevented.

> Any sufficiently complicated C or Fortran program contains an ad hoc, informally-specified, bug-ridden, slow implementation of half of Common Lisp.
> -- Greenspun's Tenth Law

## "On Seeing Through and Unseeing" (Appendix)

Defining the security/hacker mindset as extreme reductionism: ignoring the surface abstractions and limitations to treat a system as a source of parts to manipulate into a different system, with different (and usually unintended) capabilities.

To draw some parallels, unexpected Turing-complete systems and weird machines have something in common with heist movies or cons or stage magic: they all share a specific paradigm we might call the security mindset or hacker mindset. What they (and hacking, speedrunning, social-engineering etc.) all have in common is that they show through a system's surface-level presentation to the underlying reality.

The key cognitive operation is "unseeing" -- stripping away the intended purpose and seeing the raw parts that can be recombined into something entirely different.

## Catalog (Selection)

Examples of accidentally Turing-complete systems:
- CSS (Cascading Style Sheets)
- Magic: The Gathering (card game)
- Minecraft (redstone circuits)
- x86 MOV instruction (data transfer only)
- C++ template system
- Sendmail configuration files
- PostScript, TeX
- Apache mod_rewrite
- PowerPoint (Turing-complete animation system)
- Conway's Game of Life (borderline -- chosen for its complexity, later proven TC)
- Many more...

## Security Implications

The security implications of accidental TC are severe: any Turing-complete component can be used to run attacks on the rest of the system. "Weird machines" -- unintended virtual machines constructed from a system's own parts -- can execute arbitrary computation, bypassing security boundaries. The impossibility of perfect antivirus follows directly from Rice's theorem.

The only way to guarantee absence of TC is to keep a system simple. Once complexity crosses a threshold, TC becomes practically inevitable.
