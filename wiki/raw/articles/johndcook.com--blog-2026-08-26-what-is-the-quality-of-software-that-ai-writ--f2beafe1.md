---
title: "What is the quality of software that AI writes?"
url: "https://www.johndcook.com/blog/2026/08/26/what-is-the-quality-of-software-that-ai-writes/"
fetched_at: 2026-08-27T10:01:12.147193+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# What is the quality of software that AI writes?

Source: https://www.johndcook.com/blog/2026/08/26/what-is-the-quality-of-software-that-ai-writes/

AI-powered coding agents increase productivity for many developers. But do these agents produce good-quality code?
Some say this doesn’t matter, we are heading toward dark software factories with source code never inspected, and
maybe
we should
eliminate
source code altogether—“source code is the new assembly code”.
Others have a different view. Humans sometimes need to debug source code. Source code may need to be audited by humans for compliance. Code should be clear enough for a human to inspect and reason about the algorithms and behavior. Also, good code quality can make the code more legible to agents and reduce unnecessary context.
Developer teams can have many different ideas of what constitutes high-quality software and good coding style. Though there are many valid ways to write code, there is also wide consensus on general
principles
of code quality. For example, avoiding very large single functions or modules, avoiding code duplication, avoiding undisciplined feature creep or patchy code and avoiding unnecessarily deep class hierarchies or function call chains. Some coding style choices are testable empirically for impact on developer productivity. Furthermore, some code complexity measures can be computed objectively and programmatically.
My experiences are with GPT 5.5 (Extra High reasoning) and 5.6 (Extra High, Max and occasionally Ultra). Much of my experience is “out of the box” usage of Codex, with simple AGENTS.md file, though I am working on
improving
the engineering of guidance files, and it is helping. My source code is mostly Python. Unfortunately it is difficult to generalize any one set of experiences universally, since developers have different code bases, languages, models, harnesses and AGENTS.md files. One-shotting a simple computer game or website would be very different from developing a complex research code in a new domain.
At first glance, the AI-written code is not incomprehensible. It does not use odd variable names like “iiii” or “a87275,” and it does not look like it came out of an
obfuscated code competition
. But, in my experience, still the generated code has deficiencies:
The agent has a tendency to write much more code than is necessary (commonly 2-3X more—see also related findings
here
). Though it is capable of deleting code, its primary impulse seems to be to write more code.
You can work with the agent to shorten the code, but it takes work. The agent it seems is not fluent in finding structural simplifications and then extracting commonalities. In one session I spent 1/2 hour having the agent write a few hundred lines of code, and 4 hours to get it to shorten and simplify the code. You can imagine the kind of technical debt this would accumulate.
It behaves as though code simplification is much more out of its reach than code generation. At times it just completely fails to do some simplification task I ask it to do.
It has no instinct for when to break a file into multiple files for conceptual clarity, even if a file becomes over 10,000 lines long.
It can reinvent a similar but different helper function in different code modules rather than designing a simple reusable function once.
It can make massive function argument lists with 10-20 arguments rather than recognizing that the parameters may form a coherent concept representable as an abstraction or parameter object.
Importantly, it can define functions based on abstractions that do not model the underlying domain well and are hard to decipher. When I called it on this, it said: “You’re right. The code is naming implementation mechanics instead of stating intent … it forces the reader to mentally execute several layers of infrastructure just to discover that it means.”
It often invents terminology that cannot instantly be understood by the reader (the source code analogy of
Don’t Make Me Think
).
It can repeat the same expression multiple times instead of defining a variable with a meaningful name to represent the quantity.
It can hardwire unexplained “magic constants” into the code instead of defining them with meaningful names.
Indeed, when pressed, the models are sometimes capable of doing better. For example, for a hard design problem, 5.6 Ultra was capable of creating a good object design that was a good match to the problem domain, when I asked it to look hard at the problem—better than the less sophisticated models.
I would certainly expect that with more engineering of the agent guidance files, many or most of these problems would get better. However, it should not require extreme measures to get coding agents to write good code.
I have not compared other coding agents, but it would not surprise me if they had similar issues. Rightly, the coding models have been optimized for their software development utility, and this has undoubtedly succeeded in a revolutionary way.
It seems there is not yet a widely accepted code-quality benchmark playing the role for frontier coding models that SWE-bench has played for software engineering capability (though there are
efforts
). It’s especially interesting because many aspects of code quality are verifiable, making the problem seemingly quite amenable to treatment in post-training. I am hoping that someone can put together a good benchmark for this problem, and that the frontier labs will embrace these kinds of evaluations in model development.
