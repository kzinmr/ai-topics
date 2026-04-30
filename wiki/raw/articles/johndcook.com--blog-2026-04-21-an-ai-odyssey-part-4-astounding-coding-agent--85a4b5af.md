---
title: "An AI Odyssey, Part 4: Astounding Coding Agents"
url: "https://www.johndcook.com/blog/2026/04/21/an-ai-odyssey-part-4-astounding-coding-agents/"
fetched_at: 2026-04-30T07:01:59.871158+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# An AI Odyssey, Part 4: Astounding Coding Agents

Source: https://www.johndcook.com/blog/2026/04/21/an-ai-odyssey-part-4-astounding-coding-agents/

AI coding agents improved greatly last summer, and again last December-January. Here are my experiences since my
last post
on the subject.
The models feel subjectively much smarter. They can accomplish a much broader range of tasks. They seem to have a larger, more comprehensive in-depth view of the code base and what you are trying to accomplish. They can locate more details in obscure parts of the code related to the specific task at hand. By rough personal estimate, I would say that they helped me with 20% of my coding effort last August and about 60% now. Both of these figures may be below what is possible, I may not be using them to fullest capability.
This being said, they are not a panacea. Sometimes they need help and direction to where to look for a problem. Sometimes they myopically look at the trees and don’t see the forest, don’t step back to see the big picture to understand something is wrong at a high level. Also they can overoptimize to the test harness. They can also generate code that is not conceptually consistent with existing code.
They can also generate much larger amounts of code than necessary. Some warn that that this will lead to explosion of coding debt. On the other hand, you can also guide the coding agent to refactor and improve its own code—quickly. In one case I’ve gotten it to reduce the size of one piece of code to less than half its original size with no change in behavior.
I use OpenAI Codex rather than Claude Code.  I’m glad to hear
some technically credible people
think this a good choice. Though maybe I should try both.
My work is a research project for which the code itself is the research product, so I can’t give specifications of everything in advance; writing the code itself is a process of discovery. Also, I want a code base that remains human-readable. So I am deeply involved in discussion with the coding agent that will sometimes go off to do a task for some period of time. It is not my desire to treat the agent as what some have called a
dark software factory
.
Some say they fear that using a coding agent will result in forgetting how to write code without one. I have felt this, but from having exercised this muscle for such a very long time I don’t think it is a skill I would easily forget. The flip side of this argument is, you might even learn new coding idioms from observing what the coding agent writes, that is a good thing.
Some say they haven’t written a line of code in weeks because the coding agent does it for them. I don’t think I’ll ever stop writing code, any more than I will stop scribbling random ideas on the back of an envelope, or typing out some number of lines of code by which I discover some new idea in real time while I am typing. Learning is multisensory.
My hat’s off to the developers who are able to keep many different agents in flight at the same time. Personally I have difficulty handling the cognitive load of thinking deeply about each one and doing a mental context switch across many agents. Though I am experimenting with running more than one agent so I can be doing something while another agent is working.
I continue to be astounded by productivity gains in some situations. I recently added a new capability, which normally I think would’ve taken me two months to learn a whole new algorithmic method and library to use. With the coding agent, it took me four days to get this done, on the order of 10X productivity increase. Though admittedly things are not always that rosy.
In short, the tools are getting better and better. I’m looking forward to what they will be like a few months or a year from now.
