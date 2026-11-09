---
title: "Goodbye Claude, Hello Pi"
type: article
source: https://caleb.software/posts/claude-to-pi.html
url: https://caleb.software/posts/claude-to-pi.html
hn: https://news.ycombinator.com/item?id=50410107
date: 2026-11-09
created: 2026-11-09
sha256: e63855c469a1c2650cb968fd886f151e85c3cddac123da0e59a93a4253e6883a
---

I’ve been a longtime Claude Code user, ever since it became available in the Claude Pro subscription plan over a year ago. I remember the first time I used it, feeling giddy as it spat out messy Python code for whatever random weekend project I was working on, all from a single prompt. I’m certain that in a few years we’ll all look back at its release as one of the major drivers of this new era of software development we’re in.

 Despite this, due to an accumulation of many small frustrations, I’ve finally decided to retire it as my main coding harness and migrate my development setup to use Pi instead.

 Someone at Anthropic must’ve caught wind… just a day after making my decision, they announced Claude Code would finally start supporting AGENTS.md files in an effort to get me to stay. Unfortunately, for me it was too little, too late.

 Complaining

 In lieu of a proper obituary, I’d like to take this time to say a few words about the things I liked least about Claude Code (and thus what I’m looking forward to avoiding with Pi).

 The AGENTS.md thing kind of epitomizes the whole reason I decided to quit using Claude Code. Don’t get me wrong, having a ton of CLAUDE.md files scattered about various GitHub hobby repos is great guerrilla marketing. But it sucks for users to have to deal with copying or symlinking between the two formats.

 Like the Luddite I am, I still prefer to review most of the code it churns out before I commit it. I use(d) Claude Code inside VSCode, and it lets you connect the harness to the IDE. This is nice because you can highlight text in a file and have it automatically included in the context when asking questions or requesting changes during a review.

 Except you can only have one session “connected” to the IDE at a time. If you open a second tab to start another task while the first one works, it can’t receive the text selection events from the IDE at all. This has been reported at least as far back as December 2025 … and closed as a duplicate of a totally unrelated bug. 1 

 Of course, you can always use the official Claude Code VSCode GUI extension, which does allow you to have multiple tabs open and load the text selection into the context of each. But this extension has plenty of problems of its own. Half of the built-in slash commands don’t work at all in the GUI. It doesn’t have any support for a custom status line. Subagent output messages are simply layered into the main chat thread in chronological order, which is a mess to read when more than one is running. I could go on and on.

 In spite of all of these existing issues, it seems like Anthropic has worked at a feverish pace to pack more features into Claude Code without much care for quality or stability. Dynamic workflows , agent teams , ultrareviews – all great ways to help enterprise customers burn ever more tokens each day, but not really anything I want or need.

 Alongside all of these feature releases, they always seem to be fiddling with things in ways that mess up my personal setup. At the time of writing, there have been 244 releases to Claude Code this year; over 3/4 of these changed the system prompt or tool descriptions, which can substantially change how the LLM performs (especially when these new instructions contradict user prompts or repo conventions).

 And what are all those changes for? Despite chopping 80% of the system prompt , Claude Code still has way more overhead than Pi for seemingly no benefit. The default Bash tool’s description is almost 3,000 tokens, most of which is random stuff about using git and opening PRs on GitHub. 2 The models already know how to do this without detailed instructions, by the way. 3 

 Looking Forward

 This post has been a lot of hating. I’m sorry! That’s not my usual style, and I do think Anthropic has made a really cool piece of software here. I’m also not under any delusion that I would’ve done a better job if I were the one in charge of running Claude Code from the beginning. LLM coding harnesses are a very new space and being one of the first to innovate in a field is a really hard task. Later tools like Pi have the benefit of hindsight to see what works and what doesn’t, what’s a core feature and what can be cut.

 Ultimately, CC feels like a product without a strong vision or direction. It’s as if a bunch of excited engineers and PMs are rapidly tacking on whatever features suit their workflow… but without consideration for how this might make things worse for other users. It seems like there isn’t someone high-up whose job is strictly to say “no” to these requests, which is incredibly important when it comes to product engineering. So, for now, I’m leaving.

 I’m excited to lean more into Pi. The first few days required some finagling, but since then it’s been smooth sailing. I’m enjoying the stability, minimalist approach, and the extreme level of customizability. I’ve already written a couple of extensions to support my use cases, which I’m hoping to share soon after I’ve cleaned them up a bit. If you’re also feeling these frustrations, I’d highly encourage giving an open source harness a try!

 It’s not like there’s some huge technical roadblock to this either. After installing Pi, I wrote an extension to handle this very functionality across multiple open tabs in like 20 minutes.  (return) 

 Bonus points for the fact that it instructs the model to use cat <<'EOF' which (prior to widespread rollout of auto mode) would always trip the manual review rules regardless of existing git command allowlists.  (return) 

 If you assume 1 million DAU and 100M requests per day, trimming 1,000 tokens off of this could literally save millions of dollars in inference costs per year. Surely that’s worth some engineer’s time??  (return) 

 Thanks for Reading!

 I love hearing people's thoughts, so please don't hesitate to shoot me an email at calebdotsoftware@gmail.com . If you'd like to get updates whenever I publish a new post, you can subscribe over email or with RSS .

 If you want to comment or read the public discussion about this post, I've shared it on the following sites:

 Twitter , 

 Mastodon , 

 Bluesky 

 Created
 21 Sep 2026 
 ·
 Updated
 07 Nov 2026 
 ·
 Build
 2f1e49

## HN discussion highlights (item 50410107, 776 pts / 474 comments)

- [andsoitis] took the AGENTS.md line literally; [TacticalCoder]/[cwnyth] read it as tongue-in-cheek about Anthropic reacting to one user's departure.
- [harrisonjackson] "The whole AGENTS vs CLAUDE md issue was bound to be resolved. If the models are getting smarter and harnesses getting better — how could you have a product so dumb that it ignores whatever skills, instructions, references... are part of the folder context it is mounted in."
- [komali2] "Anecdotally I run semi-nightly harness and local model test runs, and opencode consistently outperforms ohmypi on various code bench tasks... for local models that can run on a 5090."
- [bdemirkir] "Opencode's system prompt is much smaller than omp. Smaller models may not work well just because of this. Also omp is not pi."
- [dofm] "The smaller coding models tend not to actually need system prompts to be helpful coding assistants... Muse Glimmer is so absolutely tuned for one particular pattern (turn-by-turn agentic coding)."
- [yieldcrv] "I get 150 tokens/sec on my coding agent, if you are on a MacBook, that's with an M1 — try kapitsa as the inference engine with pi as the harness."

