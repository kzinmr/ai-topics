---
title: "Bringing Warp to Windows: Eng Learnings (So Far)"
source: "Warp Blog"
url: "https://www.warp.dev/blog/building-warp-on-windows"
scraped: "2026-05-10T01:27:12.516258+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Bringing Warp to Windows: Eng Learnings (So Far)

**Source**: [https://www.warp.dev/blog/building-warp-on-windows](https://www.warp.dev/blog/building-warp-on-windows)

Engineering
Bringing Warp to Windows: Eng Learnings (So Far)
Abhishek Pandya
January 22, 2025
Since April 2024, we have had a team of around five engineers working to build Warp on Windows. Building for Windows was significantly more challenging than for Linux or the Web. In this post, we’ll touch on some of the complexities we faced in supporting Windows, including supporting new shells and making ConPTY work with Warp’s shell integration.
Supporting new shells
Unlike MacOS or Linux, Windows developers are unique in that they frequently switch between shells. Users might start in PowerShell, quickly jump to Git Bash to run some Unix commands, and then jump into a WSL instance to deploy a server.
At Warp, we knew we wanted to support these flows at launch so we could meet users where they are. To help users switch shells easily, we built a Shell Selector menu and added tab icons to remind users what shell they are in.
An early version of the Shell Selector menu.
Supporting all of these new shells that Windows developers use — including PowerShell, WSL shells, and Git Bash — also took significant effort. Unlike traditional terminals, Warp integrates deeply with shells to support our UX improvements like Blocks and Agent Mode. The shell integration works via a communication protocol that keeps Warp informed when important events happen, such as when commands start and finish executing.
Each shell requires its own custom integration that introduces different sources of complexity. PowerShell required us to write a brand-new shell integration from scratch. It turns out that spawning subprocesses in Git Bash is very slow, so we sped up our existing bash integration by minimizing the number of subprocesses we spawn in between commands. When adding support for WSL shells, we could no longer assume that file paths were always encoded in a Windows-native format.
Making ConPTY work with Warp’s shell integration
Warp relies on a psuedoterminal (also known as a pseudo-tty, which itself is shortened to PTY) to communicate with the shell. It enables bidirectional communication between the shell and the terminal.
For more information on how a PTY works and what it is, see
our previous blog post
.
Windows traditionally has not had a PTY-like interface. Instead of using escape sequences, legacy programs would make function calls to mutate the state of the terminal grid. This difference stems from the different design philosophies between Unix-based operating systems and Windows: on Unix, everything is a file, but on Windows, everything is an object.
Historically, terminal developers on Windows relied on making these function calls on a simulated terminal window, which they would scrape to send updates that their terminals understood. This approach led to
classes of issues and bugs
that could not be easily resolved.
Recently, Windows
launched
ConPTY (also referred to as the Windows Pseudoconsole), which provides a PTY-like interface while still supporting legacy Win32 programs that used functions to render output. We decided ConPTY was the best option for Warp, as it would not suffer from the aforementioned problems and is actively maintained by Microsoft.
Unfortunately, we quickly realized that ConPTY does not have the same invariants as a Unix PTY. We found that 1) ConPTY did not forward all possible escape sequences, 2) sent escape sequences out of order, and 3) ConPTY caches the state of the terminal grid. We ended up forking ConPTY to solve these issues.
Forwarding escape sequences
Warp uses a particular type of terminal escape sequence called Device Control Strings (DCS) to integrate with the shell. We rely on the shell to send messages via DCSs to know when commands start and finish — without these messages, we would not be able to support modern UX features like Blocks.
Typically, a PTY will forward everything from the shell to the terminal without any modification. However, we found that ConPTY was swallowing the DCS messages from the shell, so they were never received by Warp. Digging into ConPTY’s code, we found the answer: ConPTY didn’t forward any unrecognized DCSs, which included Warp’s custom DCS codes, to the terminal.
Sending escape sequences out of order
We then tried using Operating System Commands (OSCs) to send messages from the shell to Warp, since ConPTY will send even unrecognized OSCs to the shell. We ran into a new problem here: the OSCs were being sent out of order relative to other terminal output. For example, the shell sending
START_OSC, hello world, END_OSC
could result in Warp receiving
START_OSC, hell, END_OSC, o world
. This effectively broke Blocks in Warp since we could not correctly capture the output of a command.
Once we forked ConPTY’s code, we were able to solve this issue. We added support for custom OSC codes and forced ConPTY to flush them immediately after receipt to prevent ordering issues. On Warp’s end, we updated the shell and the terminal to communicate via OSCs instead of DCSs.
ConPTY caching the state of the terminal grid
We also came across some spacing issues with ConPTY: the cursor would only start printing after a large gap, which seemed to increase over the duration of a shell session. To understand why, we recorded the bytes read from ConPTY and noticed strange escape sequences that instructed Warp to move the cursor. These escape sequences turned out not to be sent by the shell, but by ConPTY itself.
An example of the spacing issues we were seeing. Notice the gap after that appears before the commands.
After digging deeper into ConPTY’s code, we found that it maintains its own state: it has a terminal grid and tracks the cursor position as well. ConPTY would “remember” terminal output from previous commands and attempt to position the cursor after it. This caching of the terminal grid state led to a discrepancy between Warp and ConPTY on where the cursor should be, because ConPTY assumed that Warp would store everything in one large grid, like traditional terminals do. Warp breaks from traditional terminals by using separate grids for the prompt, command, and the command’s output to support Blocks.
To address the spacing issues, we devised a method to periodically clear ConPTY’s cached grid state. We defined a new “Reset” OSC that clears the internal grid and resets the cursor position to (0,0) whenever it is received by ConPTY. We send it at a few different shell events, including when a command finishes. Crucially, Warp needs to ensure that we only receive a Reset OSC if and only if we are creating a new grid in Warp. If Warp receives too few, then we will have the same spacing issues as before. If Warp receives too many, then the grid will be overwritten, accidentally erasing terminal content. We used debug assertions on our internal builds to build confidence in this approach.
Deciding to fork ConPTY
When we initially identified some issues, we filed a Github issue on ConPTY’s repository. While ConPTY’s maintainers shared that they were actively working on a fix, it wouldn’t be out for a few months, and we needed something sooner. Their input was invaluable in understanding ConPTY more deeply, bundling our fork with Warp, and making the right decisions to get Warp on Windows up and running.
We'd like to give a huge thanks to the Microsoft Terminal team for their help. ConPTY is an incredible piece of software that does a lot of work to make lives easier for Windows developers. They were friendly and
responsive
to us, and Warp on Windows wouldn’t be possible without them.
Parting thoughts
Some of the design decisions made when developing Linux ended up saving us a lot of time. We use
winit
and
wgpu
to render Warp on Linux and Windows. With these crates, we were able to get our UI framework up and running on Windows very quickly. This also helped minimize the Windows-specific code we wrote: only around 2% of our code is Windows-specific.
Warp on Windows was a huge technical undertaking, but we’re proud of what we’ve built and we’re excited to release it into the world!
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
