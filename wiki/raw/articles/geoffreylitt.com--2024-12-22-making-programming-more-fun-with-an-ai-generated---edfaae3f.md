---
title: "AI-generated tools can make programming more fun"
url: "https://geoffreylitt.com/2024/12/22/making-programming-more-fun-with-an-ai-generated-debugger.html"
fetched_at: 2026-04-29T07:02:18.715340+00:00
source: "geoffreylitt.com"
tags: [blog, raw]
---

# AI-generated tools can make programming more fun

Source: https://geoffreylitt.com/2024/12/22/making-programming-more-fun-with-an-ai-generated-debugger.html

I want to tell you about a neat experience I had with AI-assisted programming this week. What’s unusual here is:
the AI didn’t write a single line of my code.
Instead, I used AI to build a
custom debugger UI
… which made it more fun for me to do the coding myself.
* * *
I was hacking on a Prolog interpreter as a learning project.
Prolog
is a logic language where the user defines facts and rules, and then the system helps answer queries. A basic interpreter for this language turns out to be an elegant little program with surprising power—a perfect project for a fun learning experience.
The trouble is: it’s also a bit finicky to get the details right. I encountered some bugs in my implementation of a key step called
unification
—solving symbolic equations—which was leading to weird behavior downstream. I tried logging some information at each step of execution, but I was still parsing through screens of text output looking for patterns.
I needed better visibility. So, I asked
Claude Artifacts
to whip up a custom UI for viewing one of my execution traces. After a few iterations, here’s where it ended up:
I could step through an execution and see a clear visualization of my interpreter’s stack: how it has broken down goals to solve; which rule it’s currently evaluating; variable assignments active in the current context; when it’s come across a solution. The timeline shows an overview of the execution, letting me manually jump to any point to inspect the state. I could even leave a note annotating that point of the trace.
Oh yeah, and don’t forget the most important feature: the retro design 😎.
Using this interactive debug UI gave me far clearer visibility than a terminal of print statements. I caught a couple bugs immediately just by being able to see variable assignments more clearly. A repeating pattern of solutions in the timeline view led me to discover an infinite loop bug.
And, above all: I started having more fun!
When I got stuck on bugs, it felt like I was getting stuck in interesting, essential ways, not on dumb mistakes. I was able to get an intuitive grasp of my interpreter’s operation, and then hone in on problems. As a bonus, the visual aesthetic made debugging feel more like a puzzle game than a depressing slog.
* * *
Two things that stick out to me about this experience are 1) how fast it was to get started, and 2) how fast it was to iterate.
When I first had the idea, I just copy-pasted my interpreter code and a sample execution trace into Claude, and asked it to build a React web UI with the rough functionality I wanted. I also specified “a fun hacker vibe, like the matrix”, because why not? About a minute later (after a single iteration for a UI bug which Claude fixed on its own), I had a solid first version up and running:
That fast turnaround is absolutely critical, because it meant I didn’t need to break focus from the main task at hand.
I was trying to write a Prolog interpreter here, not build a debug UI. Without AI support, I would have just muddled through with my existing tools, lacking the time or focus to build a debug UI. Simon Willison says:
“AI-enhanced development makes me more ambitious with my projects”
. In this case: AI-enhanced development made me more ambitious with my
dev tools
.
By the way: I was confident Claude 3.5-Sonnet would do well at this task, because it’s great at building straightforward web UIs. That’s all this debugger is, at the end of the day: a simple view of a JSON blob; an easy task for a competent web developer. In some sense, you can think of this workflow as a technique for turning that narrow, limited programming capability—rapidly and automatically building straightforward UIs—into an accelerant for more advanced kinds of programming.
Whether you’re an AI-programming skeptic or an enthusiast, the reality is that many programming tasks are beyond the reach of today’s models. But many decent
dev tools
are actually quite easy for AI to build, and can help the rest of the programming go smoother. In general, these days any time I’m spending more than a minute staring at a JSON blob, I consider whether it’s worth building a custom UI for it.
* * *
As I used the tool in my debugging, I would notice small things I wanted to visualize differently: improving the syntax display for the program, allocating screen real estate better, adding the timeline view to get a sense of the full history.
Each time, I would just switch windows, spend a few seconds asking Claude to make the change, and then switch back to my code editor and resume working. When I came back at my next breaking point, I’d have a new debugger waiting for me. Usually things would just work the first time. Sometimes a minor bug fix was necessary, but I let Claude handle it every time. I still haven’t looked at the UI code.
Eventually we landed on a fairly nice design, where each feature had been motivated by an immediate need that I had felt during use:
Claude wasn’t perfect—it did get stuck one time when I asked it to add a
flamegraph
view of the stack trace changing over time. Perhaps I could have prodded it into building this better, or even resorted to building it myself. But instead I just decided to abandon that idea and carry on.
AI development works well when your requirements are flexible
and you’re OK changing course to work within the current limits of the model.
Overall,
it felt incredible that it only took seconds to go from noticing something I wanted in my debugger to having it there in the UI.
The AI support let me stay in flow the whole time; I was free to think about interpreter code and not debug tool code. I had a yak-shaving intern at my disposal.
This is the dream of
malleable software
: editing software at the speed of thought. Starting with just the minimal thing we need for our particular use case, adding things immediately as we come across new requirements. Ending up with a tool that’s molded to our needs like a leather shoe, not some complicated generic thing designed for a million users.
