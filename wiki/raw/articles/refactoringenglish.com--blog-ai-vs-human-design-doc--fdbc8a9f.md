---
title: "Which Design Doc Did a Human Write?"
url: "https://refactoringenglish.com/blog/ai-vs-human-design-doc/"
fetched_at: 2026-04-29T07:01:22.248859+00:00
source: "refactoringenglish.com"
tags: [blog, raw]
---

# Which Design Doc Did a Human Write?

Source: https://refactoringenglish.com/blog/ai-vs-human-design-doc/

The answer
🔗
How’d you do?
Which version did readers think was AI?
🔗
Before writing this post, I surveyed my readers to see if they could spot the human version from among the three options.
Just under 50% thought my version was the human-written one, beating the other versions by a 2:1 margin. Still, I was surprised that 1 in 4 readers judged my hand-written doc as “Definitely AI.”
What made me obviously human
🔗
When readers guessed about which docs were AI-generated, I invited them to submit comments about what informed their guesses.
The biggest giveaway of me being a human was that I expressed more personal opinions and shared details based on experience:
It contained anecdotal experience (eg. in the Architecture section) and is a lot more personal than the other variants.
Versions A and C almost never portray any autonomy ie; “I think” or “We’ll”.
There aren’t really too many links in the other entries whereas there are a couple tangents in B like the John McAfee VICE link for example
Other readers pointed out that the way I presented architecture and interface choices felt distinctly human:
The User Interface ToC headings (and the ToC headings generally) feel human oriented (as far as how you’d think about actions) instead of just saying “View” which is technically correct but I personally would be less inclined to talk like that for non-business software (ie; for “home baked” software)
Architecture’s headings are a sort of ordered chaos where they make sense as far as useful groupings to build up a mental model in someone else’s head but purely in terms of “categories”, it doesn’t make any sense because they’re all different “shapes” so it feels more human.
My version also made unusual technology and licensing choices like NixCI and the PolyForm-Noncommercial license, whereas AI tends to stick with whatever’s most popular:
there are a few technological decisions that imply a certain tech stack. For example choosing NixCI implies that the author is confident in writing Nix
Once or twice, a timezone is specified whereas the other articles always keep things generic deferring to “the user’s timezone”
What made the AI obviously AI?
🔗
The most common way readers spotted AI writing was “bloat.” Even though the human version was longer by word count, the AI versions were more verbose and fluffy:
The main indicator I’d say is the bloat, where every sentence is stuffed with irrelevant blahblah.
AI is fluffy and regresses to the mean.
Focusing on unimportant details when it comes to the design.
A few readers detected awkwardness in how the AI versions wrote about meeting the project’s goals, suggesting a divergence between the author of the goal (me) and the author of the rest of the doc:
“That choice matches the self-hosted goal”
“…is the right tradeoff…”
Readers also commented on overuse of bold text in ways that felt meaningless:
bullet list with bolded key point and then non-bolded follow up text, very visible
in A
One reader correctly identified Claude Opus as the author from its
overly precise time estimates
:
Implementation timeline with # of hours per milestone is a common delusional thing I see Claude generating for me all the time. As an engineer, I wouldn’t estimate a set of tasks as “10 hours”.
What made readers guess incorrectly?
🔗
Even though verbosity was an AI giveaway, it was also the reason most readers incorrectly flagged my version as AI-generated:
longer and more in depth about things that didn’t seem as useful to someone trying to understand the why of the project
Useless details, complicated formatting in useless details, focus on technical details
Readers also perceived shorter documents as more likely to be human:
It was shorter and kept implementation/code details to the end.
Shorter content, more focussed on the what than the non functional requirements
had only the essential info
One reader inferred that the Codex version must have been a human developer based on the laziness of its
implementation timeline
:
Compared to the others, version C’s milestones aren’t as flushed out (lazy and good enough for a passion project).
Images were a dead giveaway
🔗
My actual design doc
has diagrams
, so I told the AI agents to include diagrams as well. Here’s the architecture diagram Codex came up with:
Claude created better diagrams, but it had similar layout problems where elements collided with each other in ways that a human would instantly recognize as wrong.
I could have coached the agents into generating better diagrams, but that felt like introducing too much human influence into the AI-generated versions, so I stripped the diagrams from all three versions.
My reviews of the other docs
🔗
I was pleasantly surprised by Claude’s doc.
Claude’s technology choices were so similar to mine that I wonder if I tainted it. I’m deeply in the minority on
avoiding frontend frameworks
, so I’m surprised that Claude recommended my standard tech stack of Go + vanilla JavaScript.
Before I spun up the Claude session to write the doc, I deleted the repo’s git history, but I had asked Claude to review my version in a previous session. Maybe the information seeped into Claude’s cross-session memory.
I was surprised at how poor the Codex version was.
I find that Opus and GPT-5.4 write code of similar quality, but GPT-5.4 does better at planning and investigation, so I expected it to come out on top here.
In some sections, GPT completely missed the point. Opus understood that “Alternatives considered” is supposed to talk through alternate design options, whereas GPT-5.4’s
“Alternatives considered”
was a more bloated rewrite of the
“Non-goals”
section.
They miss the hard problems
🔗
The biggest thing missing from both AI-generated design docs is a sense of what the hard problems were. What were the competing interests that the design had to balance?
Design docs force you to think through issues at design time that would be expensive to fix at implementation or release time. When you read a human-written design doc, you can intuit the tough decisions based on how much real estate they occupy in the doc.
For me, the biggest challenge of this app is balancing security and usability. How can it feel easy and fun to use while still protecting the privacy of all the users? My
Privacy
and
Security
sections are so long because I was trying to think through as many threats as possible. In the AI-generated docs, the Security and Privacy sections are generic lists of web app best practices without anything specific to this app.
Implementation now in progress
🔗
Now that the design doc is done, I’m implementing this app and distributing it under a FOSS-ish license. Little Moments is a self-hosted web app for sharing photos with family and friends, similar to TinyBeans or PhotoCircle.
It’s still in the early stages, but here’s the repo if you’d like to follow along:
Thanks to the readers who volunteered to give me notes on my design doc while it was still in draft stage, especially Cliff Brake and Jerry Orr. And thanks to everyone who guessed which docs seemed AI-generated.
