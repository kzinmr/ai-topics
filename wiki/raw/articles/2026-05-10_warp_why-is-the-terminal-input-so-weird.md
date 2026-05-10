---
title: "Why is the terminal input so weird?"
source: "Warp Blog"
url: "https://www.warp.dev/blog/why-is-the-terminal-input-so-weird"
scraped: "2026-05-10T01:28:28.170336+00:00"
lastmod: "2026-04-21T21:34:29.000Z"
type: "sitemap"
---

# Why is the terminal input so weird?

**Source**: [https://www.warp.dev/blog/why-is-the-terminal-input-so-weird](https://www.warp.dev/blog/why-is-the-terminal-input-so-weird)

Product
Why is the terminal input so weird?
Zach Lloyd
November 16, 2022
This post is about why terminal-based input seems stuck in the 80s.  If you’ve ever banged your head against the wall trying to edit a command, read on…
Problems with input editing in the terminal
Why doesn’t the terminal have IDE-style text editing?
How terminal input works
The limits of TUIs
Is this actually a problem?
Building a terminal-based IDE-style editor
Challenges
Wrap up
We’ve all had this experience: you write a complex multi-line terminal command and realize you have a typo towards the start of it.  Maybe it’s a long curl command and the url is misspelled. Shit. You try pressing the up-arrow to move the cursor up a line so you can fix it.  Nothing happens (or even worse, maybe history entries start showing up :)). You know there’s some way of using the keyboard to get the cursor to the right place, but you can’t remember it.
Next you try using the mouse – a reasonable thought, since clicking to position the cursor works in pretty much every other text editing tool.  But of course it doesn’t work.  You click and nothing happens.  You double click instead, and try to select the text to delete it and re-enter it.  The selection highlighting shows up which makes you think it’s editable, so you start typing.  But instead of inserting characters at the selection, they are inserted at the end of the line.  WTF!!!  Finally you hit ctrl-c and start over, copy-pasting the old command line by line…
*long sigh*
Problems with input editing in the terminal
There are numerous problems with input editing in today’s command-lines.  Mouse accessibility is broken, as described above.  So is multi-line editing.  In fact, the terminal input is in a lot of ways less powerful and user friendly than your typical <textarea> element on a web page, which is mouse-accessible, supports multi-line editing and has features like spell check built in.
Compared to IDEs, the terminal is even further behind. For instance, my IDE
has syntax highlighting to help me understand where I am in a long block of code and whether that code is well formed.
parses my code in real-time, providing inline documentation and the ability to quickly navigate to symbol definitions.
points out where parentheses, quotes, and the like start and end.
reformats code to a predefined standard (prettifies it).
helps me write code, using AI assistive features like in Github Copilot.
and much more…you get the point
‍
Why doesn't the terminal have IDE-style text editing?
Why is the terminal input so archaic? One theory could be that assistive features aren’t useful for command-entry.  But if you take Github stars as a gauge of usefulness, that’s clearly wrong, because some of the most starred Github projects of all time make terminal input better – e.g. completions through
OhMyZsh
(>150k stars) and command correction through
thefuck
(>75k stars).
Instead, the main issue is that the technical architecture of the terminal makes it very hard to implement rich – or even “normal” – editing features like you’d find in an IDE.
How terminal input works
Some basics on terminal architecture: the mac/unix terminal is a native app that emulates an old-school physical terminal, like the
vt100
.  These old terminals were very simple character input/output devices, and like them current terminals work one character at a time. Your terminal app accepts a character as input from the keyboard and writes it to a
pty
.  Going the other direction, the terminal reads characters from the pty and renders them on the screen.
On the other end of the pty is a shell (usually bash, zsh or fish) that interprets these characters and provides a
REPL
interface.  Part of this REPL interface is a command editor, which contains a text buffer that the shell manages (this is a simplification, but it’s basically accurate).
At a high-level, the shell REPL works as follows:
Read
:
During the read step, the user populates the shell's command buffer by typing characters, which are sent one at a time from the terminal to the shell.
If the character is printable, the shell adds it to its internal buffer and echoes it back to the terminal, which displays it.
If the character is a “control character” the shell interprets it to do things like moving the cursor, deleting text, and so on.  The shell adjusts its buffer in light of these changes, and also asks the terminal to adjust its rendering state by sending back its own control characters (e.g. it might ask the terminal to show the cursor at a different position).
At the end of the read process, the command buffer is ready to be executed.
Eval
:
When the user sends a newline character to the shell, the shell interprets the command and (usually) launches a binary (I say “usually” because some commands are so common like ls and cd that they are often “built-in” directly to the shell).  This is the evaluation step.
This binary in turn also communicates with the terminal through the pty on a character by character basis.
Print
:
Whatever program the shell runs will usually write its own responses a character a time back to the pty, and the terminal will print them.  This is the print step.
Note that programs aren’t required to print anything, and some, like “cd” don’t.  They just do their thing and return.
‍
The shell can actually do more than just echo back characters during the read state.  It can also send back things like autosuggestions (the ghosted text that fish sends back to suggest a completion) or colored text as syntax highlighting.  It can react to control characters like “tab” to show completion lists below the current command.  But fundamentally, this UX is limited to characters and doesn’t support the mouse.
The limit of TUIs
So to reiterate: the shell manages all changes to the input buffer through a completely character oriented interface.  However, only in the terminal app layer is there the ability to do mouse handling and pixel-oriented graphics – things that are needed for features like IDE-style documentation and symbol lookup, as well as for “normal” things like clicking to put the cursor someplace.
In turn this means that anyone who has wanted to improve the terminal editing experience needs to do it at the shell level – and this is what some shells like fish try to do (as well how shell plugins like OhMyZsh work).  They can only do so much though, and, crucially, they can’t make terminal input work overall in a less “weird” way.
Is this actually a problem?
Some developers will likely be strongly opposed to any graphical elements or mouse interactions in the terminal on principle.  But when I think of all the time wasted and hair-pulled when trying to work around the input weirdness in the terminal, I have to respectfully disagree.
There’s good reason that IDE’s have become the preferred code editors, and those reasons apply equally well to editing terminal commands.  E.g.
IDEs support the mouse because for a lot of users and actions it can be more intuitive.
IDEs support graphical renderings (think of an overlay showing function documentation) because sometimes that’s a more efficient way of surfacing information.
IDEs are similar to most of the other text editors developers use like GDocs and Word – and are thus easier for new developers to learn.
I do however fully agree that the terminal needs to be
fast, unbloated, and keyboard-first
– I just don’t think that means it needs to be unintuitive, purely-character based, and keyboard-only.
Building a terminal-based IDE-style editor
In
Warp
, a Rust-based terminal, we have made a terminal input that works much more like an IDE.  This is technically challenging and is still a work in progress.
From a technical perspective, it required a major change from how terminals usually work: we built the command-editor into the terminal itself, rather than rely on the shell’s editor.
Moving the editor into the terminal allows for fixing the problems mentioned above: the editor can work more or less like it does in an IDE because it no longer has a character-only pty sitting between user interactions and the data model.  Instead, the input buffer lives in the terminal and is managed by a “normal” text editing UI in which we can implement any IDE-style feature.
So instead of the traditional REPL model referenced above, in Warp the REPL works like:
Read
:
The user populates the input buffer entirely at the terminal layer.
As the user types characters, enters key navigation commands, uses the mouse, the Warp text editor updates its own internal buffer with the state of the next command to send to the shell.
Warp can implement any type of UI or event handling it wants in the course of the user entering the command - e.g. we can do auto-formatting, syntax highlighting, inline documentation, etc.
Eval
:
The user enters the newline character and Warp sends the entire command buffer to the shell for execution.
Print
:
Print basically works the same as in the normal REPL, although with one major difference – in Warp we understand which command is associated with which output and use that to render a “block” – you can read more on this in
How Warp Works
.
By moving text editing into the terminal, we have been able to implement:
A “normal” text editor
- mouse accessible with all of the normal interactivity of something like VSCode, which is especially nice for editing long and multiline commands and also has some fancier features like autosuggestions, multi-cursor and selection support.
IDE-style completions
- built-in completions for hundreds of commands with a native, fuzzy-searchable completion menu.
“
Command Inspector
”
- a feature that allows users to surface a documentation popup for any command or flag in our completion engine.
Workflows
- templatized, searchable, shareable command-snippets that take advantage of our native text editor for entering parameters and seeing their documentation.
Error underline
-
highlighting of errors in commands as you type them so you can fix them before running
Syntax highlighting and auto-parens
-
colorized text for different parts of a command and shell syntax
Command corrections
-
a native implementation in Rust of using autosuggestions to fix fat-fingered commands (done in collaboration with
thefuck
)
Soft wrapping
-
long commands automatically wrap to multiple lines without having to manually escape newlines
You can check out a quick video of these features in action
here
.
And as a knock- on benefit of our approach, all of this works out of the box with zero configuration.  It also by default works over SSH – this is a big improvement because the shell editor configuration on remote machines is often quite different from your local setup, which causes a lot of user frustration and fat-fingering.
Challenges
There are a few main sorts of challenges though with this architecture.
First, we had to build an entire text editor from scratch in Rust.  Here we were helped early on by a collaboration with Nathan Sobo, the creator of Atom, who briefly worked at Warp.  The structure of the text editor is worth an entire technical post beyond this one.
Second, in taking over text entry from the shell, we had to reimplement a lot of functionality that many shells provide out of the box.  Specifically, completions, history search, and soft-wrapping are all Warp custom implementations.  In addition to creating work for us, this can also create friction for our users, since their own custom shell configuration sometimes doesn’t work properly with Warp (for example, folks who have custom completions for bash or zsh can’t access them in Warp right now, although we are working to support this).
Third, it’s actually tricky to hook into the shell’s state machine to properly run Warp’s REPL.  In order to make that work, we configure users’ shells to tell us more about what state they are in.  We also go into detail on how this works in
How Warp Works.
Wrap up
In summary, terminal input is weird.  It’s weird largely because there’s a character-only pipe sitting between the terminal and shell.  And going one step back, the weirdness comes from the whole historical division of terminal vs. shell, which is based on emulating a physical hardware setup that hasn’t been built since the 80s.
The weirdness is also fixable, but it takes a pretty big technical re-architecting that comes with a number of challenges.  We have started down this path at Warp, and so far the reaction has been super -positive, but there’s a long way to go.  We are also looking to expose APIs into our text editor so that the community can extend the initial functionality.
Thanks for reading this, and we’d welcome any feedback on how you’d like terminal input to work!!
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
