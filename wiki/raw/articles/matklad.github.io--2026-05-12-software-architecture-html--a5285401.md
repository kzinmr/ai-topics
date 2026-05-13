---
title: "Learning Software Architecture"
url: "https://matklad.github.io/2026/05/12/software-architecture.html"
fetched_at: 2026-05-13T07:01:24.400223+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# Learning Software Architecture

Source: https://matklad.github.io/2026/05/12/software-architecture.html

Learning Software Architecture
May 12, 2026
In reply to an email asking about learning software design skills as a
          researcher physicist:
I was attached to
a bioinformatics lab
early in my career, so I think I understand
          what you are talking about, the phenomenon of “scientific code”! My
          thoughts:
First
meta observation is that “software design” is
          something best learned by doing. While I had some formal “design”
          courses at the University, and I was even “an architect” for our
          course project, that stuff was mostly make-believe, kindergarteners
          playing fire-fighters. What really taught me how to do stuff was an
          accident of my career, where my second real project (
IntelliJ Rust
) propelled me to a position of software leadership,
          and made design my problem. I did make a few mistakes in IJ Rust, but
          nothing too horrible, and I learned a lot. So that’s good news —
          software engineering is simple enough that an inquisitive mind can
          figure it out from first principles (and reading random blog posts).
Second
meta observation, the bad news:
Conway’s law
is important. Softwaregenesis repeats the social architecture of the
          organization producing software. Or, as put eloquently by
neugierig
,
If I were to summarize what I learned in a single sentence, it
              would be this: we talk about programming like it is about writing
              code, but the code ends up being less important than the
              architecture, and the architecture ends up being less important
              than social issues.
I suspect that the difference you perceive between industrial and
          scientific software is not so much about software-building knowledge,
          but rather about the field of incentives that compels people to
          produce the software. Something like “my PhD needs to publish a paper
          in three months” is perhaps a significant explainer?
Two things you can do here.
One
, at times you get a chance to
          design or nudge an incentive structure for a project. This happens
          once in a blue moon, but is very impactful.
This
is the
          secret sauce behind
TIGER_STYLE
, not the set of rules per se, but the social context
          that makes this set of rules a good idea.
Two
, you can speedrun the four stages of grief to acceptance.
          Incentive structure is almost never what you want it to be, but, if
          you can’t change it, you can adapt to it. This is also true about most
          industrial software projects — there’s never a time to do a thing
          properly, you must do the best you can, given constraints.
Let me use
rust-analyzer
as an example. The physical reality of the project
          is that it’s simultaneously very deep (it’s a compiler! Yay!) and very
          wide (opposite to an LLM, a classical IDE is
a lot
of
          purpose-built special features). The social reality is that “deep
          compiler” can attract a few brilliant dedicated contributors, and that
          the “breadth features” can be a good fit for an army of weekend
          warriors, people who learn Rust, who don’t have sustained capacity to
          participate in the project, but who can sink an hour or two to scratch
          their own itch.
My insistence that
rust-analyzer
doesn’t require building
rustc
, that it builds on stable, that it doesn’t have any
          C dependencies, and that the entire test suite takes seconds, was in
          the service of the goal of attracting high-impact contributors. I was
          wrangling the build system to make sure people can work on the borrow
          checker without thinking about anything else.
To attract weekend warriors, the internals of rust-analyzer are split
          into multiple independent features, where each feature is guarded by
catch_unwind
at runtime. The thinking was that I
explicitly
don’t want to care too much about quality there,
          that the bar for getting a feature PR in is “happy path works &
          tested”. It’s fine if the code crashes, it will only attract further
          contributors, provided that:
the quality is isolated to a feature, and doesn’t spill over,
at runtime, the crash is invisible to the user (it’s crucial that
            rust-analyzer features work with an immutable snapshot, and can’t
            poison the data).
In contrast, when working on the core
spine
which provided
          support for features, I was very relatively more pedantic about
          quality.
A word of caution about adapting to, rather than fixing incentive
          structure — the future is uncertain, and tends to happen in the least
          convenient manner. The original motivation behind rust-analyzer
experiment
was to avoid the need to write a parallel compiler
          (the one in IntelliJ Rust), and to
prototype
a better
          architecture for LSP, so that the learnings could be backported to
rustc
. So, even in core (especially in core), the code
          was
very
experimental. Oh well. Stuck with one more compiler
          now, I guess?
I might hazard a guess that something similar happened to uutils
          project, which started as the primary destination for people learning
          Rust, and ended up as Ubuntu coreutils implementation.
Third
, now to some concrete recommendations. Sadly, I
          don’t know of a single book I can recommend which contains the truths.
          I suspect one can only find such a book in an apocryphal short story
          by Borges: practice seems to be an essential element here. But here
          are some things worth paying attention to:
Boundaries
talk by Gary Bernhardt is all-time favorite. It
          contains solid object-level advice, and, for me, it triggered the meta
          inquiry.
How to Test
is something I wish I had. I immediately understood
          the importance of testing, but it took me a long time to grow arrogant
          enough to admit that most widely-cited testing advice is shamanistic
          snake-oil, and to conceptualize what actually works.
∅MQ guide
and,
          more generally,
writings by Pieter Hintjens
introduced me to Conway’s Law thinking. That “feature development”
          architecture of rust-analyzer? –
optimistic merging
,
          applied.
Reflections on a decade of coding
by Jamii is excellent, goes very meta. It is intentionally the first
          of
my links
.
Ted Kaminski
blog is
          the closest there is to a coherent theory of software development,
          appropriately framed as a set of notes to a non-existing book!
As for the actual books,
Software Engineering at Google
and Ousterhout’s
The Philosophy of Software Design
are often
          recommended. They are good. SWE, in particular, helped me with
a couple of important names
. But they weren’t ground breaking for
          me.
