---
title: "Perfectionism vs. Pragmatism in Product Engineering"
source: "Warp Blog"
url: "https://www.warp.dev/blog/perfectionism-vs-pragmatism-in-product-engineering"
scraped: "2026-05-10T01:27:59.771615+00:00"
lastmod: "2026-04-24T14:39:47.000Z"
type: "sitemap"
---

# Perfectionism vs. Pragmatism in Product Engineering

**Source**: [https://www.warp.dev/blog/perfectionism-vs-pragmatism-in-product-engineering](https://www.warp.dev/blog/perfectionism-vs-pragmatism-in-product-engineering)

Product
Perfectionism vs. Pragmatism in Product Engineering
Zach Bai
June 28, 2023
For a lot of software engineers out there, it’s hard not to be a perfectionist. The endeavor of programming dictates a perfectionist mindset – the code must be written without error, else the compiler will fail. A forgotten semicolon or indent can lead to a window littered with red underlines. A PR can’t be merged until it passes CI with zero test failures.  Passing test suites and successful compilations (with no warnings!) are small achievements not too dissimilar from a 10/10 on a pop quiz.
I include myself in this bucket of perfectionists. And to be clear, I largely consider this a good thing. It’s good to consider edge cases, ensure tests are passing (and that the tests exist in the first place), and generally have a rigorous approach to technical tasks, whether it be fixing a regression or designing greenfield architecture.
That being said, when I transitioned into a Tech Lead role at Warp, I solicited some advice from the other Zach (Warp’s CEO) on how best to do my (new) job. One piece of feedback I got: “I worry you have a bit of a perfectionist bent”.  To which part of me instinctually responds, “Yeah, duh, isn’t that a good thing?” for all the reasons I listed above. However, the other part of me understands what Zach was saying. It’s not that it’s a bad thing to be a perfectionist, but it
might
be bad to consider perfection the
most important thing
. Ultimately, we’re here to build a product – not write code.
In contrast to writing code, when you’re building a product, there’s no mandate for perfection. Our end goal is to build a great product, to be sure, but it’ll certainly make stops at “not-so-good”, “ok”, and “good” before it gets there.  Like coding, the process is iterative. Unlike coding, however, iterations aren’t clearly demarcated by a passing test suite and merged PR. Instead, each loop is focused on identifying and achieving “good enough” – which itself is hard to define. My take is that “good enough” means “good enough” to solve the user’s problem at hand, to the extent that it’s solved in a meaningfully better way than before.  It’s the compromise between what you
can
and
should
achieve now and the “great” you aim to achieve eventually. Its definition changes from the prototype to the MVP to the V1 to the V2.
So when I asked other Zach for advice on how to reconcile my “perfectionist bent” with the duties of my new role, his response was “be pragmatic”. (At least that was the gist of it). In other words: there’s a time and place to be a perfectionist – designing a canonical data model or redundant serving architecture might be examples. But when it comes to building a product, eschew perfectionism for pragmatism and continually pursue “good enough” with the end goal of achieving an unqualified “great”.
Pursuing a perfect solution for Subshells in Warp
I recently led a project at Warp to build “Subshell Support.”  This is a feature that enables Warp’s core feature set in nested shell sessions, whether that be a local subshell or a nested shell session in a remote Docker VM. For readers who don’t know, Warp is our take on a terminal reimagined for the modern developer. Here are some gifs to demonstrate:
before subshell support
after subshell support
Basically, it makes “subshell”
1
sessions look like other (non-sub-)shell sessions in Warp, in all their blocks/modern input editor/completions-filled glory.
Unfortunately, the feature has some less-than desirable quirks:
Warp asks you if you want to “Warpify” the subshell, rather than just doing it automatically.
Warp only asks you to Warpify for certain commands, and doesn’t for others.
If you had the wherewithal to find your way to the Subshells settings page and “add a subshell command” (because Warp didn’t ask you to Warpify; see 1), the next time you use that command, Warp only
asks
you to spawn the subshell, rather than doing it automatically. Yes, this is the same as 1, but this time you explicitly
told
Warp it was a subshell spawning command, so why doesn’t it do it automatically? What gives???
These are all great points. And clearly I’m aware of them – I just listed them. In fact, these quirks were explicit parts of the product spec written before the implementation began in earnest. So why do they exist? Is it because the team missed my PRD in their inboxes?
Nope, the answer is that the quirks listed above are tradeoffs of a path forward for Subshell Support that we deemed “good enough”.
What’s good enough to ship?
For Subshell Support specifically, the ideal product experience was always clear. The initial PRD was basically:
The user executes a command that spawns a subshell.
Warp automatically recognizes that a subshell was spawned, triggering “Warpification”
The subshell is treated like any other shell session; blocks, completions, syntax highlighting etc. all continue to work.
My natural instinct was to pursue these requirements.  I spent the first couple weeks of the project following possible leads for automatic subshell detection: maybe subshells printed some recognizable, distinct byte sequence to stdout. Or maybe there was some archaic process signal emitted when a subshell is spawned.  I even looked into trying to watch the filesystem for new pty allocations that might correspond to a spawned subshell process.
As you might have guessed, none of these leads panned out. I concluded that the only viable approach for “automatic subshell detection” required the user to modify a shell configuration file sourced on startup .If you have an idea for another way, email me at zachbai
at] warp.dev. Seriously.  And this, too, wasn’t a perfect solution because it’s not always feasible to update an RC file. What if the subshell session is running on a remote host? Or you’re frequently connecting to a set of changing machines?
At this point I was faced with a red pill/blue pill-type decision:
Be a product perfectionist and continue trying to find a technical solution for the (seemingly) impossible
OR
Be a product pragmatist and accept the technical limitations, pivot, and move forward.
I took the red pill, accepted the technical limitations, and moved on. In other words, I revised (2) from my initial PRD:
The user executes a command that spawns a subshell.
Warp doesn’t recognize that a subshell was spawned. But the user tells us it was, triggering “Warpfication” themself.
The subshell is treated like any other shell session; blocks, completions, syntax highlighting etc. all continue to work.
Not quite “magic”, but still usable. With this approach, we quickly got to an initial prototype, iterated with Warp’s designer Rob on the UX details, and started dogfooding internally.  At this point, I considered the experience OK. Certainly not perfect, not quite “good”, and maybe still not “good enough.” But it was indeed a starting point and sparked a feedback loop to propel improvements.
Later on in the project, we determined that it might make sense to also implement the RC file-based subshell detection I mentioned earlier, so users would have the option to use it if it made sense for their use case.  When dogfooding this iteration, I found that the RC file solution, though not perfect, did address a non-trivial swath of use cases – for example, when using a local poetry subshell for python development, or in long-running docker containers for personal development. We recaptured some share of that ideal product experience we thought we’d abandoned earlier.
One of the issues with the latest iteration was discoverability – how would users know to update their .zshrc, for instance?  For most of the project timeline, I figured the most practical approach would be to include this information in our docs site.  But this isn’t a great solution – not all of us are “read the directions” kind of people.  As we got closer to the projected launch date, I became more and more confident that the “go-to-our-website-and-find-the-docs” solution definitely didn’t pass the “good enough” bar.
So about a week before we intended to launch, we spent some time iterating on not-so-great solutions (e.g. “how about we add a toast with a link to the docs?”) until we landed on the “success block”, which is easier to show than tell:
Fortunately for us, it turned out to be quick and simple to implement – a relatively rare moment when it  was indeed pragmatic to build the ideal thing.  At last, we arrived at the iteration that we later launched and is live in Warp today.
After a couple additional days of dogfooding the latest version and some positive feedback from teammates, it became clear that while the experience isn’t perfect, it’s certainly improved the experience of using subshells in Warp by a meaningful margin.  For V1 of this feature, that is good enough.
Optimizing for “good enough”
To be clear, I do mean
good enough
, not necessarily “great”.  Whether or not it’s “great” is for Warp’s users to decide. If they disagree, that’s good too, because it means (a) they’re using the feature and (b) they care enough about the feature that there’s motivation to disagree.  As the person who led the project, I wouldn’t be so bold as to assert the feature is plain “great” – yet. However, I
am
confident that we have a good starting point.  If you’ve used Subshells in Warp and have an idea for how they can be better, please file a GitHub issue! Maybe it’ll be the thing that makes the experience great.
–—
The Subshells project is one small case study of trading perfectionism for pragmatism, particularly when it comes to identifying and moving towards your product goal.  In this particular case, technical limitations were the primary adversary of ideal experience, but there are certainly other honorable mentions – time, headcount, funding.  Whatever it may be, the challenge remains the same. Be ready to embrace a pragmatist approach – for us at Warp, that means continually building and iterating on “good enough” until we get to “great”.  It won’t satisfy the same perfectionist itch as the first zero-warning/error compilation after a major refactor or a passing integration test suite (both locally
and
in CI!) but it
will
drive forward progress in building a better product.
1 I put “subshell” in quotes here because the definition of “subshell” we use for this feature is not identical to the true Unix definition of a “subshell”. There’s more detail on this in our Subshells feature docs here.
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
