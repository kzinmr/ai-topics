---
title: "Warped Expectations: The Iceberg of UX Ambiguity Behind Synced Inputs"
source: "Warp Blog"
url: "https://www.warp.dev/blog/warped-expectations-the-iceberg-of-ux-ambiguity-behind-synced-inputs"
scraped: "2026-05-10T01:28:23.645893+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Warped Expectations: The Iceberg of UX Ambiguity Behind Synced Inputs

**Source**: [https://www.warp.dev/blog/warped-expectations-the-iceberg-of-ux-ambiguity-behind-synced-inputs](https://www.warp.dev/blog/warped-expectations-the-iceberg-of-ux-ambiguity-behind-synced-inputs)

Engineering
Warped Expectations: The Iceberg of UX Ambiguity Behind Synced Inputs
David Melvin
August 10, 2023
Here’s a sneak peek into what the first few months of my time as a software engineer at Warp have been like. At Warp, all engineers are given three “small” starter tasks and one larger starter project. My first two starter tasks went fine. The third starter task was surprisingly complex, but it had nothing on my starter project.
It all started with this GitHub issue feature
request
. Users coming from other terminals like iTerm2 wanted the same broadcast input functionality. Broadcast input is a mode that lets you type input in one terminal session and have that input sent to other terminal sessions at the same time. An example use case is running the same setup scripts on multiple servers you’ve SSHed into. Sounds pretty simple, right? We’ll see.
The first question is also the most fundamental: what are we broadcasting?
This is simple in most terminal emulators because they center around receiving keyboard input as bytes, sending those bytes to programs, and displaying the program’s output bytes to the user. Warp’s input is more complex because there is an IDE-style input box where you can use the mouse and perform actions like performing an AI search from that box. In other words, there are inputs and outputs that are only for the terminal application, and they don’t get sent to or from the programs on the computer.
There are actually a ton of small-ish questions like this that add up to a lot of ambiguity. Much in the same way that the bulk of an iceberg lies below the water’s surface. But let’s focus on “what are we broadcasting?” first.
What “input” should we “broadcast”?
The question of what input to broadcast is straightforward in most terminal emulators. For the most part, everything boils down to “the user sends these bytes to the PTY” and “the PTY sends the response bytes back”. That’s an oversimplification–you could reduce all of computing to inputs and outputs–but the point is that most terminal emulators are pretty low-level. Most terminals don’t add a ton of abstractions or steps to this input-output process.
Even a user input like pressing the left arrow key must be represented in bytes and sent to the PTY, in a similar way to sending the ASCII character “a”. This is why the feature “broadcast input” works so naturally in other terminal emulators like iTerm2. All user input for a given terminal session is just a sequence of bytes sent to the PTY. So you can send the same input bytes to multiple PTYs across multiple sessions?
This is quite powerful because it makes no assumptions about the state of the terminal sessions you’re broadcasting to. Is their input the same as that of the session you’re broadcasting from? Is one session running vim and another session typing the flags of an
rm
command? Broadcast Input doesn’t care. It’s powerful, but it could be dangerous if not fully understood.
Warp is different. We have a full-fledged input editor akin to the code editor of an IDE. The relevant features here are that we support mouse input and dozens of actions you can in the terminal input that shouldn’t directly change what we send to the session’s PTY.
That begs the question: what “input” should we “broadcast” in “broadcast input”?
Difficult examples:
Do we sync text selection/highlights?
Do we sync cursor moves with the mouse?
Do we sync Warp-specific actions like creating a workflow?
Most of these questions boil down to the bigger question of “how do we broadcast inputs and still be useful when the terminal inputs don’t have the same starting state?”. The same problem exists in other terminals, but our terminal input allows more states and more ways of mutating that state, so the problem is bigger for us.
Navigating Deeper Down the Iceberg of Ambiguity
Step 0 (before syncing): everything works as normal
Step 1: Start syncing and select “hello” on terminal 1. How should that be reflected in terminal 2 if they are “synced”
Step 2a: Select all of "pwd". This feels reasonable, but what algorithm would we use to consistently make the most “reasonable” and intuitive selection? For example, what if terminal 2 read "pwd -P" instead of just "pwd"?
Step 2b: Select just the "w" in "pwd". This makes some sense, if our algorithm to choose how to sync selections is to identify the selected indices relative to the total length of the input, and we map that same relative selection to the other sessions. Nonetheless, this isn’t perfect.
Step 2c: Select the exact same indices in both terminals where possible. When not perfectly possible, do the next best thing. In this example, we’ve selected characters 5-10 in terminal 1. Terminal 2 only has three characters in its input, so we just move the cursor to index 3.
You might argue that syncing text selection isn’t all that important. But a further point is what happens when we start typing brave new to replace hello in that terminal 1? Generally speaking, non-intuitive behavior in the terminal can make it easier for users to accidentally run dangerous commands so we must be careful.
Trusting the (Product Development) Process
I’m glad I didn’t have to navigate this process alone. I was supported by Suraj as my engineering onboarding mentor, my engineering manager Chuck, our designer Rob for UX considerations, and the rest of the team for any questions.
Our CEO Zach Lloyd provided his thoughts about these ambiguities in some conversations near the beginning of the project. He helped in a broader way a long time ago when he wrote
How We Solve User Problems at Warp
. It was a helpful guide as I tried to wrangle this ambiguity.
Fun note: Our
How We Work
recently made some rounds on
Twitter
. I like this way of thinking and it was helpful.
Here’s how I followed our product development process effectively throughout this starter project and what I learned for next time.
Clarify the Need
Steps one and two of our Product process at Warp is to clearly identify what problem we’re solving and why we’re solving it.
This can be tricky for any project that you’ve been assigned, but it’s even more tricky when it’s one of your first projects on a new project, team, or company because you don’t have as much intuition as to the answers to these questions. That can be a blessing in disguise though because that lack of intuition can make you more open-minded to creative product and technical solutions.
Broadcast input was an interesting project because most team members at Warp either didn’t know this feature existed in other terminals or had only used it once in the past. I was one of those that didn’t know it existed. Focusing one step one of the process, I had to ask what do our users really need here?
To answer this question, I had to do some research. I combed through the main GitHub issue for
broadcast input
and all related issues in our Warp repository. Then I searched for “broadcast input” in other terminals. My goal was to understand what users were actually trying to accomplish when using this feature.
I’m reminded of the Henry Ford quote, “If I had asked people what they wanted, they would have said faster horses.” That quote is extreme and probably not actually said by Henry Ford, but the idea is that we want to think deeply about how users use the terminal and how we can improve that experience. We don’t want to simply slap together cool terminal features.
The upshot of my research was that, while users were asking us for a feature that lets them send keystrokes to multiple terminals at the same time, the underlying problem appeared to be “I need to run the same command in multiple terminal sessions at the same time”. There were some other edge cases but this covered the vast majority of user stories.
Reframing the question from “how can I broadcast input? to “how can I run the same command in multiple sessions?” leads to many different potential solutions. One we thought of was something like a “super” terminal input floating separate from all the terminal history. When in this “broadcast” mode, you’d type in this super input and when you press Enter the command would get sent to each of the sessions you specified. This would be a difficult feature to build from every angle: design, product, and technical design. It would solve the users’ main issues but didn’t appear to provide commensurate value for the effort it required. So we continued exploring.
Explore Solutions
We discussed all of this in a project kick-off/design jam meeting. We played around with the broadcast input feature in other terminals to decide what we liked and didn’t like. We found it was mostly great. The main problem we faced was how we could port this feature into Warp, as mentioned above.
Our solution was to simplify the feature. We call it “synchronized inputs” instead of “broadcast input” to drive this point home.
Revisiting the text selection example from above, here is how synced inputs look in Warp.
The solution is to simplify the problem by changing what level of abstraction we use. We’re not broadcasting the actual keyboard inputs or other actions a user takes in one terminal to another terminal. We’re only syncing the input buffer text across all synced terminals. When the terminal is in a long-running command mode we fall back to the “broadcast input” methodology because we don’t have our fancy Warp text input editor when interacting with an interaction command, for example.
Essential to this solution is that we force the input buffers of all synced inputs to become the same as soon as you begin syncing those inputs. This is to avoid the problem where you have different initial terminal input states.
This does make synced inputs less “powerful” than broadcast input because you can’t send arbitrary keystrokes to all terminal sessions regardless of their state. We chose to optimize for the main use case and ease more one-off needs with a generally feature-rich terminal and keyboard shortcuts to facilitate quick actions. Thankfully, it looks like users like it so far!
Chart the Course
Even after the simplification of only syncing the input buffers instead of keystrokes there are some remaining questions on the iceberg, including:
How do we handle autosuggestions and completions in each session?
What about ctrl-r history search or “up” previous commands?
What about Warp-specific features like Warp Drive and Warp AI?
How do you choose which session to sync?
These questions can be grouped in two:
How should synced terminal inputs act regarding additional UI elements that can appear as you interact with them?
How do you check and modify which terminals you’re syncing?
The questions in group one are about not cluttering our user interface. Another simplification came in handy: only show the cursor and additional UI elements on the focused terminal input. Additionally, the focused terminal is the only one that is actually performing checks for autosuggestions, completions, or running any other more advanced functionality. The sync “destination” terminal sessions are only receiving and applying updates to their input buffer strings. This also keeps the feature performant, which is another one of our
product principles
(build for speed).
This is where I wish I adhered more precisely to our product development process. I wish I had built and experimented with a simple prototype of this feature for a while and listed all of the questions that came up. Then I could have answered as many of them as possible in the Product Requirements Doc (PRD).
Instead, I wrote a short PRD and discovered a lot of these questions during the development process. For me this was a tough case of “How do you know what you don’t know?” I thought I detailed the UX considerations pretty thoroughly but in hindsight I should have taken it a level deeper. It was my first major project here at Warp, though, so it taught me a valuable lesson about uncovering and clearing up ambiguity.
Most of these questions are about tradeoffs. I struggle with tradeoffs because I often want to make everything “perfect”. Our How We Solve User Problems describes the value of Identifying if a project is something that we should build “fast” or “right”. This thinking encouraged me to focus less on making everything perfect, which is either impossible or would take way too long. Finding the balance between fast and right is a journey I’m still on, but it’s been a great learning experience for my professional and personal life!
Conclusion
Depending on how I present the feature of “synced inputs” it could seem like a trivial problem or a bit hairy. While it wasn’t super complex technically, I think it was a great starter project because:
It touches a critical part of the Warp app, the terminal input, which is impactful.
Many users found this feature crucial, so it felt valuable. But it also isn’t the most essential deal-breaking feature in the world so it wasn’t too stressful either.
It required exploring the structure of the Warp app to understand how we model the Warp window, tabs, panes, and terminal sessions, which made it easier to work on future projects.
Most importantly, It taught me to Trust the (Product Development) Process going forward.
Try out synced inputs in Warp and let us know what you think about it on GitHub or Twitter!
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
