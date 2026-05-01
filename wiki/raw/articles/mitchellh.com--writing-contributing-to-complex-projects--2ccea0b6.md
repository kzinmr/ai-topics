---
title: "Contributing to Complex Projects"
url: "https://mitchellh.com/writing/contributing-to-complex-projects"
fetched_at: 2026-05-01T07:02:03.642691+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Contributing to Complex Projects

Source: https://mitchellh.com/writing/contributing-to-complex-projects

Table of Contents
As a frequent open source maintainer and contributor, I’m often asked: where do you
start
? How do you approach a new project with the goal of making meaningful changes? How can you possibly understand the internals of a complex project?
These questions apply to any software project regardless of whether they are open source or proprietary, hobbyist or professional. The approach I take is the same in any case. However, a critical difference with professional work is that you have direct access to other engineers who are willing — if not obligated — to help you, whereas open source projects you’re mostly on your own.
I’ve established a repeated pattern for approaching complex projects and document it in this post. I don’t expect that this pattern will work for everyone, but I hope it’ll help others have the confidence to attempt to learn and contribute to complex projects.
I’m using the term
complex project
to describe any software project where the implementation isn’t trivially understood. This definition is subjective; some people may view a project as a complex that others do not, and vice versa.
Step 1: Become a User
The first step to understanding the internals of any project is to become a user of the project. You do not have to become an expert user, but my personal graduation criteria for this step is to try to
build something real using the project
, even if it is small or simple. For example, prior to contributing to the
Zig programming language
, I created a
handful
of
real
libraries
.
As a user, you’ll gain a broad understanding of the capabilities of the project. There is a stark difference between reading the reference documentation and using a project in practice, and creating toy projects is an important step to bridge the gap from theoretical to practical understanding.
Additionally, you’ll begin to learn the idioms of the project which form the cultural undertone and help guide an understanding of why a project works the way it does, has the features it does, etc. This is important because it helps to form empathy for the other humans working on the project and it also serves as a guide of what changes may or may not make sense for the project.
I also highly recommend
joining the community
at this point. Join IRC or Discord, attend a local meetup, watch talks, and more. Spend more time listening than talking for a period of time. The goal here is to gain empathy and learn how the project works. I’m always surprised how much I learn by simply watching others learn.
Step 2: Build the Project
Learn how to build the project and get a working binary (or equivalent). Don’t bother with
understanding
the build system, the dependencies, etc. Just cargo cult guides, websites, whatever you need to reliably and repeatedly go from source code to runnable binary on your system.
Don’t read the code before learning to build the project.
Too often, I see people get bogged down trying to understand the source code of a project before they’ve learned how to build it. For me, part of that learning process is experimenting and breaking things, and its hard to experiment and break a software project without being able to build it.
Don’t worry about feature complete builds.
Complex projects often have features that are only available if you have the right dependencies, right systems, right configuration, etc. If this is the case, don’t worry about any of that. The goal is to get a binary that works
well enough
on your system. As you go through later steps, you’ll gain experience and confidence to start chasing down more feature complete builds.
During this step I also recommend learning how to run the test suite and getting that to pass. This makes it easier to experiment and break things in later steps. Complex projects often also have complex test suites, so sometimes this means getting only a subset of the test suite running — whatever is enough to experiment.
Step 3: Learn the Hot-Path Internals
To learn the internals, I like to use an approach I call “trace down, learn up.”
Trace Down
I start with a feature or use case, and start from the outside in to trace the codepath that the feature follows. During this process, I take notes about the files, lines, and functions I’m going through, but I
do not yet attempt to understand how anything works.
This is the “trace down” phase.
For example, when studying the Zig compiler, I started by tracing the
zig build-exe
command to build an executable from Zig source code. This tracing process led me to find the source for the
zig
CLI, the
build-exe
subcommand, into a “Compilation” subsystem, which then calls the lexer, parser, etc. I didn’t read the implementation details beyond what was necessary to trace the path.
From the tracing notes, you can usually get a “big picture” of how something works. Based on filenames, functions, etc. you can usually start to discern major subsystems of a project. This helps later compartmentalize the learning process into more reasonably sized chunks.
Don’t try to learn everything
. A common mistake I see people make is getting lost for weeks or months and ultimately getting discouraged because they attempt to just read an entire project line by line. Stay focused and learn feature by feature.
Tip:
When picking a feature, choose one that you're familiar with as a user. Also, if possible, try to pick a feature that seems simple on the surface. For example, the first Zig program I tried to trace to learn the compiler was one that added two numbers and had zero output.
Learn Up
After tracing a feature, it is time to actually learn how the various mapped subsystems work. Whereas with the tracing phase, I start at the outermost point such as the CLI or API call, with the learning phase, I tend to start at the innermost point.
I choose the innermost point to start because it is usually the most fundamental and least abstracted. As you climb layers, it tends to correlate with growing levels of abstraction making it harder to learn if you don’t understand the component pieces.
To start learning a specific subsystem, I recursively “trace down, learn up.” I’ll start by examining the public, exported API surface and then learn how each API call works. This is how higher level layers will be using this subsystem, so it both gives me guidance for how to learn but also will make it clearer as I move up the stack.
Experiment and Break Things
During the “trace down, learn up” process, I find it very helpful to experiment and break things to learn how something works. This is why it is critical to learn how to build a project before attempting to read the internals.
Add new log statements, implement tiny chunks of new functionality, change existing functionality, etc. then rebuild the project and see what happens. This is also a good way to really test your understanding of how something works.
For example, while learning the Zig tokenizer, I added new tokens and saw that they tokenized but then saw that the parser failed. When I got to the next system (the parser), I made my new tokens
do something
. And so on.
Throughout this phase, supplement in-the-weeds code spelunking with any available media sources: books, videos, blog posts, etc. If there is existing literature that covers internals, read it!
However, you should not expect these materials alone to get you to an expert state. Similar to step 1 and “becoming a user”, there is no supplement for getting your hands dirty and playing with the actual source code when trying to “become a maintainer.” This is another example of theoretical vs. practical application.
Tip:
If resources to learn the internals do not exist,
try writing them yourself! I did this with Zig and wrote about
Zig compiler internals
since I
couldn't find a similar up to date resource. Writing about something
is a good way to reinforce your learning and also helps future
contributors.
Step 4: Read and Reimplement Recent Commits
As a final step to learning internals, I read recent commits relevant to the subsystems I’ve studied and test that I fully understand why the change was made. This is my “doing the problem set in the back of the textbook” portion of learning.
I either view the commit history of the project or the commit history of a specific file or folder relevant to a subsystem I’ve studied. I then either study the solution first (the changes in the commit)
or
I see the bug it fixed and attempt to fix it myself and see if I arrive to a similar solution.
To “work the problem”, I’ll checkout the repository at the commit just previous to the commit I’m studying. I’ll reproduce the bug it fixes (if it is a bug fix), and then attempt to implement the solution myself. Finally, I’ll compare my work to the commit done by the maintainer or contributor.
The only hint I'll give myself is the change size necessary (the
+/-
lines on the VCS diff). I recommend avoiding changes that require more than 50 to 100 changed lines to start.
Step 5: Make a Bite-sized Change
I like to start small and incrementally take on larger and larger tasks. At this phase, you understand the
technical
components of the project, and its time to learn about the
human
components. The goal here is to make a small change and learn the contribution and review process.
The hardest part is usually finding a small change to make. There is no silver bullet here. I browse the issues looking for something that looks contributor friendly. I usually make a few false starts or abandon an issue entirely and try others. Finally, I’ll find one. The time it takes to find the issue or even fix the issue may be frustratingly long, but its the price of admission. Projects often have "contributor friendly" labels to help guide new contributors.
Most projects nowadays are good about documenting their contribution process, so once the change is implemented, follow the process exactly. If you’ve joined the community in earlier steps, this is a good opportunity to ping someone and ask for help or for someone to double-check your process.
As an example, my first contribution to Zig was a
three line change
that took me around four or five hours to complete over two evenings (not including the time commitment of prior steps). If this bug were to surface today I’d be able to fix it in minutes, but it takes time to get to that level of proficiency.
Success
At this point, you’ve learned a complex project and successfully contributed!
Don’t be afraid of complexity. I think too many engineers look at stereotypically complex projects such as programming languages, browsers, databases, etc. as magic or as destined for higher-beings. I like to remember that all projects were started by other humans. If they could do it, I can do it too. And so can you.
I hope that by sharing my process, others can find complex projects more approachable.
