---
title: "Opus 5.5 and Fable 5.2 made my overoptimized Rust code even more overoptimized"
url: "https://minimaxir.com/2026/11/opus-fable/"
fetched_at: 2026-11-28T10:00:44.598166+00:00
source: "minimaxir.com"
tags: [blog, raw]
---

# Opus 5.5 and Fable 5.2 made my overoptimized Rust code even more overoptimized

Source: https://minimaxir.com/2026/11/opus-fable/

I like fast software. I like
very
fast software. A couple months ago, I published a blog post titled
Writing Rust code that’s faster than state-of-the-art libraries by asking agents to make the code faster
in which I listed techniques for using agentic LLMs to speed up the runtime execution of Rust software—of course, with extensive checks and balances to ensure good code quality, avoid regressions, and mitigate cheating by the LLMs. After enough iterations, the resulting Rust libraries are faster than existing state-of-the-art implementations with the same or better capabilities, even against those already written in Rust. The main bottlenecks for me open-sourcing the resulting Rust crates are a) doing comprehensive real-world testing to ensure the code works as advertised and b) I don’t want to release the code and then have another model release immediately find another 2x-or-more speed boost because that would be embarrassing.
I’m not satisfied with my code merely being faster than state-of-the-art: I want my code to push against hardware limits even for “fun” software that may not require maximum throughput. I don’t want my benchmarks to be measured in milliseconds, I want them measured in
microseconds
, dammit. Who knows if some application in the future will require submillisecond word clouds or submillisecond ASCII art generations?
In that blog post, I mostly used OpenAI’s GPT models for this agentic iteration pipeline. The day after publication, Anthropic announced
Claude Opus 5.5
, which was met with skepticism as Opus 5 was underwhelming…and then it quickly turned out that Opus 5.5 was a step-change increase in the capability of agents with the ability to complete difficult technical tasks that neither OpenAI’s nor Anthropic’s other models could complete. I spent the $20/mo to try out Opus 5.5 on my agentic iteration pipeline after observing the hype…and after only two days, the results were impressive enough that I paid the $100/mo to get more usage quota. Through more testing over the past couple months, I can confidently say Opus 5.5 and its subsequent Fable 5.2 sibling did in fact result in significant performance breakthroughs that indeed push my Rust software to its limits.
Switching from Codex to Claude Code
#
Lest people think that this post is an undisclosed #ad for Anthropic, I had grievances with
Claude Code
prior to Opus 5.5 which were the primary reasons I switched to OpenAI’s
Codex
. One such example is Claude ignoring
AGENTS.md
in favor of
CLAUDE.md
(
until very recently
), which was honestly petty enough to tip the scales.
The main grievance with using Claude Code is deciding which harness to use—or, rather, the lack of decision. Although I was fine with using Claude Code in the terminal back in the halcyon days of Opus 4.5, Codex’s ability to use any harness, such as
Zed Agent
which allows using the Codex subscription natively, made it more convenient to keep everything in one place. In contrast, Claude Code
infamously
blocks third-party harnesses and has closed workarounds used to access it regardless.
Therefore, I had to consider workarounds for using Opus 5.5 in a way that doesn’t require significant changes to my agentic iteration pipeline. Zed Agent has a
workaround to use Claude Code
by following the
Agent Client Protocol
, but there was a problem due to how Claude operates: Opus 5.5
loves
spinning up background tasks and working asynchronously, and Zed Agent had poor support for background tasks so I had little idea what the agent was actually doing. This was made worse by Opus 5.5 never
editing
code files using Edit tools; instead, Opus 5.5 likes to write Python files which surgically find/replace the code. I tried using the Claude Code terminal application again but that made the ergonomic issues above even more difficult to manage.
Claude editing a Rust file by writing a Python script.
That said, the async nature can save time when spinning up subagents (in this case Haiku 5.5) to review the changes made, as the main Opus 5.5 agent can write code or run long benchmarks while the subagents simultaneously do their nonblocking review work.
Therefore, my main harness for my Opus 5.5 work was the standard
desktop Claude app
—which will likely eliminate all my AI engineering street cred, but it is what it is. In addition to clearly listing background tasks in progress, the native app also lists current session and weekly usage which was a pain to constantly check when using Zed Agent or CLIs.
Background task sidebar in the Claude Code desktop app.
There are also two more usability perks of using Claude Code within the desktop app: images always appear inline when the agent reads them so I can tell specifically what the agent is reading, and
Remote Control
is unexpectedly useful for letting hours-long prompts run while I’m doing other things such as job hunting and touching grass (but failing because I really wanted to know how well the code is running).
Leveraging Opus 5.5
#
At first, I fed Opus 5.5
my updated Ur-Prompt
for agentic iteration—typically a prompt with an explicit directive to improve the speed at which the benchmarks run by at least a specified amount without either causing regressions or cheating the benchmark results. With this new model (and a few tweaks to
my AGENTS.md
to address some peculiarities with Claude), that approach indeed worked, and in a single pass, Opus 5.5 achieved 1.2x - 1.5x speedups on multiple distinct projects which had already been optimized with GPT 6.1 Astra.
That said, there are a few quirks with how Opus 5.5 works such as prompt queueing: with Codex/Zed Agent, I could queue a prompt such as
c'mon, do a breakthrough
such that it would only be sent to the agent after it was done with the current prompt (important as it is deliberately asymmetric information as telling someone to do a breakthrough while they are still working is counterproductive), but with Claude Code it will send any queued message when idle, e.g. while it’s waiting on background tasks such as benchmarks and subagents. My silly workaround to this behavior was to put
c'mon, do a breakthrough
in a Markdown file in another folder outside of the current environment (so Claude can’t accidentally find it when it examines the environment), then add to the prompt:
After completing this task,
**and ONLY after completing this task**
, then read
`/Users/maxwoolf/Desktop/agent_instructions/alpha.md`
and follow the instructions within.
This works, and Opus 5.5 indeed does not cheat by reading ahead of time, and the breakthrough commands do result in actual breakthroughs.
One issue I have with Opus 5.5 is that it definitely writes more lines of code than the GPT models: in the case of Rust that’s not necessarily bad performance-wise since it’s a compiled language but it adds more technical debt than I would like. For example, many of my Rust projects rely on PNG image encoding and decoding through Rust’s
png
crate. However, when Opus 5.5 was instructed to make improvements on benchmarks where PNG processing is on the hot path, it consistently creates its own bespoke PNG module from scratch (with parallelism/streaming better-aligned to how the base code processes the data) that does achieve the desired 1.2x - 1.5x speedups without causing any regressions, so I’ll begrudgingly accept it. I very frequently run
cut the amount of code by 20% without causing regressions
maintenance passes and even then it struggles to do so.
Another issue with agentic iteration work specifically is that Claude Code obfuscates how it runs benchmarks. When running benchmarks with
criterion
, instead of displaying the benchmark results as they come in, they’re piped to a temporary file so I can’t view intermediate progress. It also doesn’t return results from the benchmarks until after they’ve concluded, despite my prompting explicitly asking it to, so I have to twiddle my thumbs a bit (again, good for attempting to touch grass).
Agentic LLMs have mostly become homogenized in terms of how they work through their turns, with the difference between certain LLMs coming down to benchmarks which may be gamed, or worse—
vibes
. Overall, I have to give more trust to Opus 5.5, which I have mixed feelings about. That said, the trust has been rewarded, particularly with new approaches I found where Opus 5.5 excels where GPT models did not.
Profiling
#
In my prompts, I always added a suggestion about leveraging
process profiling
that the GPT models mostly ignored:
You may consider using profiling areas of the codebase to find specific areas and hot paths which scale poorly (e.g. O(n^2)) at large amounts of data.
Opus 5.5, in contrast, is extremely eager about profiling with
samply
to find the areas where code spends most of its time executing and will often do so as its first task, including reprofiling after each change to find changed hot paths for further improvements.
Opus 5.5 profiling a Rust crate with a somewhat inscrutable command.
Opus 5.5 also spends more time running experiments whereas GPT models edit the code first then ask questions later; both approaches have their merit but I think Opus 5.5 is more productive at it.
Reducing Peak Process Memory
#
While working on making my Rust software super-fast, I never put much thought into how much system memory it utilized. I figured it was unnecessary since a) Rust is already extremely memory efficient and b) writing to RAM beyond what is needed causes wasted system overhead which would inevitably be caught by the existing prompts to make the software faster.
I was wrong. Very wrong.
If I could get a ~20% reduction in peak memory without much code complexity change, then maybe it’s worth pursuing. Therefore I gave Opus 5.5 a simpler-than-usual prompt because I was too apathetic to prompt engineer it:
Do a pass to reduce peak memory consumption without causing significant regressions
The results on a couple projects:
Memory decreases on my Rust
HDBSCAN
/clustering crate after the prompt.
Memory decreases on my Rust text search project (in-memory, not CLI).
I
immediately
used the same prompt on all my projects and achieved similar significant peak memory reductions (doing a second pass with
c'mon, try doing a breakthrough
resulted in even stronger reductions). In general, it achieved this through the traditional tricks used to explicitly manage memory such as streaming data and smarter specification of
Vec
sizes. That said, I had hoped that this approach would result in speed improvements (i.e. the agent discovers an algorithm has no viable memory improvements and therefore it implements a better algorithm) but significant speed improvements were rare.
Visual Design and Knowledge
#
Another hyped aspect of Opus 5.5 is its ability to better handle visual design and avoid the typical “AI Slop” aesthetic when designing web applications. This capability may not intuitively translate toward maximizing the speed of my Rust software, but it’s crucially important to balancing both speed and quality for my applications that rely on visual design, as visual design isn’t always subjective and “it looks ugly” can be a legitimate software regression.
In my initial post about agentic iteration, I described implementing a
UMAP
algorithm with this approach, as UMAP is a useful-for-me dimensionality reduction algorithm (among many) that when used to project to 2D, it can automatically create intuitive visual clusters.
Images of
Digits
clustered via umap-learn.
via umap-learn docs
In my original post, I noted that the Python bindings of my Rust UMAP algorithm beat
umap-learn
by 4x - 15x after several agentic iterations. Although it excelled at all the typical quantitative benchmark metrics, my UMAP algorithm apparently failed the most important benchmark: vibes. The visual clusters in cases such as the famous
MNIST dataset
of digit images were not semantically distinct compared to existing implementations such as umap-learn,
PaCMAP
, and
TriMap
:
The Python bindings of my UMAP crate (top-left) are indeed ~12x faster than
umap-learn
but that doesn’t matter if it produces indistinct clusters.
So I asked Opus 5.5 iterate specifically to improve cluster distinctiveness compared against for the known good implementations while minimizing the speed tradeoff, along with making more apples-to-apples fairness tweaks:
Your browser does not support embedded video.
Download the video
.
Download the video
.
Opus 5.5 also made the head-to-head video, which is unexpectedly hypnotic.
The speedup relative to
umap-learn
fell to about 4x, but cluster quality is very comparable now and 4x is still a good speedup.
Another visual-oriented project I’ve been working on since Opus 4.5 is the fast and accurate automatic conversion of images from raster files to vector (SVG) files that can scale to any size. This isn’t a new concept: tools such as
Inkscape
that convert images to vectors/SVGs have been around for awhile. Rust itself has
vtracer
and
img2svg
, but I wanted to see if I could beat them not only in speed, but also a) visual fidelity between the vector and raster and b) output SVG file size, which requires deriving fewer and more efficient SVG
Paths
and
Bézier curves
.
Take for example, this image of a pelican riding a bicycle.
That is what everyone talks about
with AI, right?
A 393KB vector-art-style image generated with ChatGPT Images 2.5. Don’t think too hard about its left leg.
This test case is deliberately tricky for raster-to-vector algorithms as pelicans are very curvy.
Running the image through
vtracer
with default settings results in a 153KB SVG that’s unusably blocky.
Prior to Opus 5.5, running the image through my Rust crate that went through the GPT agentic iterative optimization pipeline resulted in much better output than
vtracer
/
img2svg
for my crate, but still had enough errors such as color blotches and jagged “staircases” that were easily identifiable and would make the output vector SVG unusable, so I shelved the project entirely. Opus 5.5 in contrast is eager to zoom into the image, find staircases, construct comparison grids and image diffs, fix the underlying algorithms, and repeat until it’s fixed.
Opus 5.5 iteratively examining output SVGs by creating comparison matrices of test outputs.
With the guardrails and repeated Opus 5.5 iterations, my approach to raster-to-vector finally beats the existing options by considerable margins.
For this pelican example, my crate beats both
vtracer
and
img2svg
in all of speed, size, and error.
Here’s the pelican SVG output from the crate, reduced from the stated 25KB to 14KB after passing it through a separate SVG compression/refinement tool I also created and optimized with Opus 5.5 using similar techniques:
It’s not 100% perfect but you
really
need to zoom in to see the defects.
This pipeline has worked well with my other test images, but it still needs more real-world tests before I will release it.
Disassembling the Compiled Binary
#
Yes, we’re going there.
The release of Opus 5.5 specifically led to a new age of reverse engineering software using LLMs, from
Reverse Engineering Anything
allowing reverse engineering anything (duh), to drastically speeding up
decompiling games
. For my work making software as fast as possible, I didn’t read too much into it until I randomly saw one of my reasoning traces run
objdump
to try and figure out why a change did not result in an expected speed increase. So as an experiment, I gave this as a part of a
dedicated variant Ur-Prompt
in its own pass (since Opus 5.5 may avoid disassembly unless you specifically constrain it):
For this particular round of optimization, focus on investigating the compiled binaries—including minimizing the number of CPU instructions emitted and reducing unnecessary branching—in order to hit the specified benchmark metric improvements.
**ALL library code changes this session MUST FIRST be discovered and justified by disassembling the binary**
. Do not chase marginal speed gains through disassembling: if performance converges and no more major changes are feasible, wrap it up.
The effectiveness of this approach legitimately surprised me…but don’t ask me to explain what’s happening.
Speedup after a disassembly optimization for a Rust graph network crate.
Speedup after a disassembly optimization for the Rust UMAP crate (w/ the visual constraints persisting).
Somehow, Opus 5.5 is smart enough to make Rust code changes that propagate through
LLVM
to the resulting binary with fewer instructions without causing regressions—I would have called that impossible a year ago.
One potential weakness of this approach is that it may overfit to specific hardware (my M3 MacBook Pro / ARM architecture) but the diffs appear to be more architecture agnostic. At the very least, it intentionally doesn’t write custom CPU instructions in Rust itself because doing so requires
unsafe
.
What About Fable 5.2?
#
You may have noticed I haven’t talked about Fable 5.2 yet despite giving it equal billing with Opus 5.5 in the headline. Fable 5.2
was released
a couple weeks ago and its benchmarks were…ok. Not much better than Opus 5.5 on paper especially below
max
effort, but
much
more expensive.
I had spare quota, so why not put Fable 5.2 (on
high
effort) through the same paces I did for Opus 5.5? I fed it the Ur-Prompt (and bumped the research subagents to Opus 5.5), and Fable 5.2 did not achieve the 1.2x - 1.5x speedup consistent with each successive model release.
Fable 5.2 instead achieved a 1.5x -
2.0x
speedup on many of my projects.
Massive speedups for my word cloud project in both text parsing and generation.
Given the benchmark results, I don’t get it but I am very much not complaining.
One tool I’ve been experimenting with (particularly in this very post) but never talked about due to potential accusations of heresy is a next-generation
grep
replacement that is faster than the beloved
ripgrep
, but with additional features; this new Rust crate named
byteseek
. ripgrep, itself written in Rust and optimized for over a decade, is tough to beat speedwise without shenanigans, however Fable 5.2 was able to find massive speedups on synthetic benchmarks in-memory.
Also massive speedups for byteseek; this is after I told Fable 5.2 to
do a breakthrough
.
ripgrep itself uses
real-world datasets to benchmark
(Linux source tree and English+Russian OpenSubtitles; Russian tests UTF-8) and does the benchmarks via the CLI which has significant overhead from opening files for scanning not present with in-memory benchmarks, so I ran an apples-to-apples CLI benchmarks comparing the two on both synthetic and real data:
byteseek particularly excels at alternation/multiple query terms and case-insensitive searches. BTW I am also developing a new scientific data visualization library in Rust and wanted an excuse to dogfood it.
Given the likely skepticism about its performance, I am officially
open-sourcing byteseek on GitHub
early as a research preview to demonstrate just what this type of overoptimized Rust code looks like. Since I have the speed headroom to do so, I also added more features such as pretty-printing output for humans,
jq
-like JSON searching (plus YAML/TOML), fuzzy and predicate matching, and Python bindings which unexpectedly
beat
the optimized
pyahocorasick
and
orjson
.
A ripgrep-like output with
byteseek
but with more information and more
pretty
.
What Now?
#
In all, this is my new agentic iteration pipeline:
The Opus 5.5 pass
Typically done using
my updated Ur-Prompt
, with various constraints tweaked depending on the problem. (e.g. the target metrics for optimization and regression mitigation)
The Opus 5.5 peak memory reduction pass
Simple prompt,
do a breakthrough
if there is a significant speed increase that implies performance has not converged.
The Opus 5.5 disassembly pass
Done with a
dedicated variant Ur-Prompt
,
do a breakthrough
if there is a significant memory reduction.
The Fable 5.2 pass
Same as the Opus 5.5 pass, although I bump the subagents to Opus 5.5 to better match the model’s power.
The (optional) Fable 5.2 disassembly pass
…if I have Claude Code quota to spare: Fable only being able to be used for half of the Claude Code weekly quota is a bummer.
My Rust software that I had already optimized with GPT-6.1 Astra now achieves a cumulative
4x speedup
on average with much lower memory utilization, and this was reproducible across multiple projects. My word cloud generator—where I was overly excited about hitting 1 millisecond generation—now generates in 374 microseconds. This also generalizes to projects where speed is more meaningful, such as my Rust statistical modeling library and my Rust data visualization library.
Per Opus 5.5, the performance for most of my Rust projects have now have hit theoretical hardware limits. Therefore I have little reason to continue procrastinating as new models likely won’t make the code meaningfully faster, so I should hopefully be shipping more quickly. That said, marketing the Rust projects has become increasingly difficult since my original post for a number of reasons, but that’s a discussion for another blog post.
In the meantime, I should learn how compiler optimization in Rust actually works as there are likely more significant code speedup opportunities there…
