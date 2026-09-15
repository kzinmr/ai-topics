---
title: "AI is breaking our proxies for expertise"
url: "https://seangoedecke.com/ai-is-breaking-our-proxies-for-expertise/"
fetched_at: 2026-09-13T10:01:14.139982+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# AI is breaking our proxies for expertise

Source: https://seangoedecke.com/ai-is-breaking-our-proxies-for-expertise/

Mathematicians are broadly not anti-AI. They’re more culturally open to using AI as a tool than, say, artists or writers
. However, now that more and more
genuinely
prestigious
problems have fallen to AI, that might be changing. Almost five thousand mathematicians (including twenty-five Fields medalists) have signed a declaration called
A Severe Misaligment of AI in Mathematics
. The core argument goes something like this:
In recent months, the success of AI in solving major mathematical problems has made headlines even outside mathematical circles. But solving problems is only a tool and proxy for achieving the primary goal of conceptual understanding and insight. Forgetting this in the world of AI may turn the tool against the primary goal. Indeed, the mass production at faster and faster pace of “true/false” statements could destroy fertile ground instead of breathing life into new ideas.
A lot of people online have interpreted this as the expected complaint from any field that gets automated: translators did it, artists and programmers have been doing it, and now it’s the turn of the mathematicians. I think this is too dismissive. Understanding the concrete problem mathematicians are upset about can help us better understand the impact of AI on our own fields, and what we’ll have to do about it.
Puzzle-solving and idea-generating
There are two types of mathematics. Most people are familiar with the first, which we might call “puzzle-solving”: you take a problem and try to find a solution to it. When you’re a student, these problems are typically easy, like simplifying some algebraic expression. When you’re a researcher, these problems can be nearly impossible, like proving
Fermat’s Last Theorem
. Puzzle-solving is easy to understand but hard to do, which makes it impressive to non-mathematicians, which makes it highly prestigious. In other words, puzzle-solving is
legible
.
The second type of mathematics is “idea-generating”: coming up with new ways of thinking about mathematics, and thus new terms or concepts. For examples of these, just glance down the list of
arXiv mathematics papers
. “Hardy spaces”, “Schatten exponent”, “Banach lattices” and so on are all concepts someone thought was interesting. This work is largely unimpressive to non-mathematicians, because nobody really knows if the concepts you come up with are particularly difficult or insightful. For instance, I have just generated the concept of a “Goedecke set”, which is the set of all natural numbers whose digits add up to a prime number. Who cares? The categories we want are the
“natural kinds”
of mathematics — the concepts that “carve nature at its joints” — and it’s almost impossible to tell what those are without years or decades of hard work.
How are the two types of mathematics related? We might say
that generating ideas is the real intellectual work of mathematics. Puzzle-solving is important instrumentally: to identify which ideas can be used to answer longstanding questions, and thus which ideas are worthwhile. Over time, those worthwhile ideas become better understood and easier to use, until they reach the point where they can be used to advance science in general. Eventually the ideas become so well-understood that they can be taught to children: “zero”, “negative numbers”, “imaginary numbers” and “calculus” were all once rarefied mathematical ideas, but are now concepts we’d expect any precocious twelve-year-old to grasp.
There’s another, more prosaic purpose of puzzle-solving: to make mathematical skill and progress legible to outsiders. I can’t appreciate Terence Tao’s mathematical work, but I know what a Fields Medal is. I don’t have a good intuitive sense of what a Galois representation is, but I know about the proof of
Fermat’s Last Theorem
. We might say that puzzles like this have served as a way to indirectly reward skilled mathematicians for their more important idea-generating work (or for conclusively demonstrating
that the ideas used in the proof are useful).
Do AI proofs undercut idea generation?
AI proofs undercut both of these purposes. I can now lay out precisely why I think mathematicians are so unhappy:
Puzzles serve as a high-legibility, high-reward target for mathematicians
To solve these puzzles, new ideas must typically be generated; the puzzle’s solution serves as evidence that the ideas are useful
But now AI can solve many of these targets “the hard way”, without generating intuitive new ideas
This undercuts both ways puzzle-solving supports idea-generation: AI companies claim the prestige while not meaningfully advancing mathematical progress
This is bad for mathematics as a whole, because puzzle-solving is ancillary to the real goal of mathematics
This is kind of like
Goodhart’s Law
. Puzzles were a useful, impossible-to-game measure for mathematical progress. But now that AI companies can game that measure (by solving them in a way that’s inaccessible
to humans), the whole point of those puzzles disappears.
Are the mathematicians right? I think it’s broadly unclear whether (3) is true: i.e. whether frontier AI models aren’t generating or can’t generate new mathematical ideas. We’re still in the very early days of AIs solving our hardest mathematical problems. Who knows what they’re going to be capable of? I give basically zero credence to the idea that AIs are incapable of this because of some intrinsic feature of how LLMs work. For the last three years, we’ve seen people claim that LLMs are intrinsically incapable of X, only to have LLMs excel at X a few months later.
Even granted that (3) is true, there’s still work to be done for human mathematicians in building the conceptual machinery that can make AI-generated proofs accessible to humans: i.e. in generating a “human proof” to go alongside the existing “AI proof”. In fact, I’d expect the existence of an AI proof to help with this. If you know proposition X is true, it’s easier to figure out why, because you’re not constantly worried you’re wasting your time. For more on this, I recommend Gwern’s blog
On Really Trying
, where he quotes a series of instances where simply being told that a solution exists is enough of a clue to help people find it.
Mathematics, chess, and speedrunning
Of course, there’s a prestige and motivation problem. “I’m the first person to solve Navier-Stokes” is a much more compelling target than “I figured out a better way to explain the AI solution to Navier-Stokes”, and it’s much easier to award prizes for. Will mathematicians bother to work on problems that have already been solved? I think so.
To see why, we can look at other domains where AI has come in and outcompeted the best humans, such as chess or video game speedrunning. I can run a chess program on my phone that will beat Magnus Carlsen 100-0. Computer programs — called “tool-assisted speedruns” or “TAS” — can finish any video game much faster than even the fastest human. But in both of these areas, humans still compete in human-only leagues, and there’s still prestige attached to the most capable humans. It’s possible that mathematics ends up in this kind of state, where “human mathematics” and “AI mathematics” exist in largely separate spheres, and the first “human” solution to a mathematical problem can still earn acclaim.
In fact, in both of those areas, the presence of inhumanly strong computer players has improved the human game. Despite many computer chess moves being basically incomprehensible to humans, top chess players have
learned from
the computer “style”. In speedrunning, many moves once considered “TAS-only” are now performed by humans. AI mathematics might likewise improve human mathematics.
Software engineering
I am not a mathematician. I did major in mathematics during undergrad, and I have fond memories of proofs from
real
and
complex
analysis, but it’s not even close to my field. However, I am watching the effects of powerful AI on mathematics very closely, since my own field — software engineering — is being colonized by AI agents in the same way.
The field of software engineering does not have the same structure as mathematics. We write code to make money, not to earn prestige or advance the frontier of human knowledge. But AI is undercutting the traditional avenues for prestige in software engineering as well. It used to be that you could put a meaty project on your GitHub — say, an emulator, or a toy OS — and people would know you were a skilled engineer. But now projects like that are worthless, because everyone just assumes they’re vibe-coded. We used to tell stories about engineers who would disappear and rewrite a system over the weekend, or produce thousands of lines of code a day. Now anyone can do that with an OpenAI subscription.
Like mathematics, software engineers are going to have to rebuild our cultural sense of the kind of work we value. We are either going to have to silo “AI work” off from “human work” like chess, or to find some legible human skills to recognize that can’t be easily counterfeited by AI. In the meantime, a lot of people who were successful in the old world are going to be very unhappy.
Here's a preview of a related post that shares tags with this one.
