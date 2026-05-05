---
title: "Writing safe Verilog"
url: "https://danluu.com/pl-troll/"
fetched_at: 2026-05-05T07:01:35.663359+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Writing safe Verilog

Source: https://danluu.com/pl-troll/

Troll? That's how people write Verilog. At my old company, we had a team of formal methods PhD's who wrote a linter that typechecked our code, based on our naming convention. For our chip (which was small for a CPU), building a model (compiling) took about five minutes, running a single short test took ten to fifteen minutes, and long tests took CPU months. The value of a linter that can run in seconds should be obvious, not even considering the fact that it can take hours of tracing through waveforms to find out why a test failed.
Lets look at some of the most commonly used naming conventions.
Pipeline stage
When you
pipeline
hardware, you end up with many versions of the same signal, one for each stage of the pipeline the signal traverses. Even without static checks, you'll want some simple way to differentiate between these, so you might name them
foo_s1
,
foo_s2
, and
foo_s3
, indicating that they originate in the first, second, and third stages, respectively. In any particular stage, a signal is most likely to interact with other signals in the same stage; it's often a mistake when logic from other stages is accessed. There are reasons to access signals from other stages, like bypass paths and control logic that looks at multiple stages, but logic that stays contained within a stage is common enough that it's not too tedious to either “cast” or add a comment that disables the check, when looking at signals from other stages.
Clock domain
Accessing a signal in a different clock domain without synchronization is like accessing a data structure from multiple threads without synchronization. Sort of. But worse. Much worse. Driving combinational logic from a metastable state (where the signal is sitting between a 0 and 1) can burn a massive amount of power. Here, I'm not just talking about being inefficient. If you took a high-power chip from the late 90s and removed the heat sink, it would melt itself into the socket, even under normal operation. Modern chips have such a high maximum power possible power consumption that the chips would self destruct if you disabled the thermal regulation, even with the heat sink. Logic that's floating at an intermediate value not only uses a lot of power, it bypasses a chip's usual ability to reduce power by slowing down the clock. Using cross clock domain signals without synchronization is a bad idea, unless you like random errors, high power dissipation, and the occasional literal meltdown.
Module / Region
In high speed designs, it's an error to use a signal that's sourced from another module without registering it first. This will insidiously sneak through simulation; you'll only notice when you look at the timing report. On the last chip I worked on, it took about two days to generate a timing report
0
. If you accidentally reference a signal from a distant module, not only will you not meet your timing budget for that path, the synthesis tool will allocate resources to try to make that path faster, which will slow down everything else, making the entire timing report worthless.
PL Trolling
I'd been feeling naked at my new gig, coding Verilog without any sort of static checking. I put off writing my own checker, because static analysis is one of those scary things you need a PhD to do, right? And writing a parser for SystemVerilog is a ridiculously large task. But, it turns out that don't need much of a parser, and all the things I've talked about are simple enough that half an hour after starting, I had a tool that found seven bugs, with only two false positives. I expect we'll have 4x as much code by the time we're done, so that's 28 bugs from half an hour of work, not even considering the fact that two of the bugs were in heavily used macros.
I think I'm done for the day, but there are plenty of other easy things to check that will certainly find bugs (e.g, checking for regs/logic that are declared or assigned, but not used). Whenever I feel like tackling a self-contained challenge, there are plenty of not-so-easy things, too (e.g., checking if things aren't clock gated or power gated when they should be, which isn't hard to do statistically, but is non-trivial statically).
Huh. That wasn't so bad. I've now graduated to junior PL troll.
