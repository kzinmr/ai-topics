---
title: "Fantastic terminal programs and how to quit them"
source: "Warp Blog"
url: "https://www.warp.dev/blog/fantastic-terminal-programs-and-how-to-quit-them"
scraped: "2026-05-10T01:27:24.479950+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Fantastic terminal programs and how to quit them

**Source**: [https://www.warp.dev/blog/fantastic-terminal-programs-and-how-to-quit-them](https://www.warp.dev/blog/fantastic-terminal-programs-and-how-to-quit-them)

Engineering
Fantastic terminal programs and how to quit them
Zheng Tao
September 23, 2021
It's hard to exit vim, emacs, nano, and tmux on terminals. This article explains why these apps were built this way, and provides a guide on how to exit them.
There’s a popular meme about exiting vim.
More earnestly, there’s even a
LinkedIn learning course
on how to use vim. The first module is dedicated to how to exit.
Why is it so hard? This seems like an odd problem to have. When’s the last time you’ve thought about exiting your web browser, MSWord, or any other application on your computer?
It’s not just Vim, but the user experience on the terminal as a whole.
The terminal predates human computer interaction. It existed before Xerox PARC lab & Apple Computer worked on personal computing and GUIs. Apple introduced some human interface guidelines in 1977, which have been copied pretty much everywhere else -- but the terminal has stayed the same.
Even though we’ve gone from mainframes to hobbyist computers to modern laptops, programmers still interact with the terminal in the same way.
It’s true that some popular terminal programs were created after this all happened, but there’s a big difference in their philosophy of the user.
Today, it’s not revolutionary to say, as Apple did in their human interface guidelines, that “people are not trying to use computers—they’re trying to get their jobs done.” In the terminal, it’s just the opposite: for example, people are trying to use tmux to experience
the tao of tmux
.
The terminal is hard to use. Interactive terminal programs are particularly difficult and they behave unlike anything else on your computer.
As intimidating it is to get started, it can be extremely valuable to know how to use these programs. They are cross-platform, available on even the most limited environments, keyboard-accessible, and if you’re on a remote host it’s often the best option to accomplish some task.
Here’s the basic ins-and-(literally!)outs for a bunch of programs, why they can be non intuitive, and why other modern apps aren’t difficult in the same way.
‍
Vim
Vim has a number of different modes. By default, it’s in “normal” mode. Hitting ‘i’ will get you into “insertion” mode which edits the text content directly. You’ll need to get out of insertion mode (esc) to communicate a quit command to vim.
We’re used to modeless text editors today. They’re the default editors everywhere: on computers, phones and tablets – natively and on the web.
License plate of Larry Tesler, “Primary inventor of modeless editing and cut, copy, paste.”
‍
When you are in any mode aside from normal mode, it’s communicated in the bottom left. Many tools use a similar status bar UI. This can be easy to miss if you don’t already know to look here.
Status bar in Vim
When they do use modes, other apps today clearly indicate the mode. If you go from an editing mode to viewing mode in GDocs, you can’t miss it. Any design app will also change the cursor to indicate what you’re doing.
‍
Changing modes in Figma
From normal mode in Vim, we can type
:
to get into Cmd-line mode. This makes the cursor jump from the content to the bottom-left, and vim commands can be typed.
Finally, we can type
q
<enter>
to quit.
If you have some unsaved content, vim won’t let you quit, to ensure you don’t lose anything.
One option is to go nuclear and force quit :q!.
Otherwise, you can save the file. If there’s already a filename,
:wq
or
:x
will let you save and quit. If you did come from the empty state, there’s no file here yet so you will have to explicitly save to a file (:w filename) before quitting.
Emacs
The keybinding to quit emacs is Ctrl-X + Ctrl-C.
This key sequence is more complicated - and I’ve definitely messed it up before when doing this the first couple times.
Emacs does give some visual feedback in the bottom-left corner after typing the first Ctrl-X.
‍
It’ll also tell you if you messed up in the same place. But you can also inadvertently type a bunch of stuff that edits the file, and you won’t necessarily get this feedback.
Relative to vim, it’s a little easier to deal with editing a file and saving it, because emacs will ask you how to deal with an unsaved file.
Emacs doesn’t have modality, but its shortcuts are more complicated in general. A lot of functionality in emacs uses the Meta key. For example Meta-f and Meta-b move forward and back one word respectively.
‍
While it used to be a thing, modern keyboards don’t include the Meta key. Most terminal emulator apps will let users map some other key to imitate Meta instead.  It’s not typically on by default, and sometimes one has to dig quite a lot to do this.
Mapping Option to Meta in iTerm2
We generally won’t see key sequences this complicated in other places on the computer outside of the terminal. At the very least, other apps are not going to use a key that no longer exists and put the burden on the user to figure out how to make it available.
Nano
Quitting nano is not hard relative to other things. There’s a status bar that hints Ctrl-X will exit.
Many people have found themselves in nano because git or arc put them there, even when they have not chosen it as an editor.
This is some pretty unforgiving UX. It’s rare outside of the terminal to end up in an application where you may not know how to exit.
Tmux
Tmux is a terminal multiplexer. It provides a lot of functionality, and one basic way to think of it is a way to manage multiple running shells arranged in a number of “windows” + panes.
For tmux, any attempt to communicate directly to tmux involves typing Ctrl-b (we call this the prefix key). There are two main options for getting out: Ctrl-b + d will detach the screen session. Ctrl-b + :kill-session kills the current session.
When typing command sequences after the prefix key, no feedback is given and you’ll have to internalize these commands to use tmux.
Remembering the one prefix key is not as hard as remembering all the commands to work regularly in a terminal multiplexer. In my experience, pros mess up basic tmux commands
again
and
again
.
These programs epitomize
remember-and-type
over
see-and-point
. As Apple’s human interface guidelines puts it:
“Command-line interfaces require the user to remember a command and type it onto the computer. This kind of interface makes considerable demands on the user’s memory -- especially when the commands are complex or cryptic. Such an interface is especially galling to the new or infrequent user, but it distracts all users from their task and focuses attention instead on the computer’s needs.”
Furthermore, “users rely on recognition, not recall; they shouldn’t have to remember anything the computer already knows.”
Developers know this principle very well when it comes to their code. Djikstra famously said “the competent programmer is fully aware of the limited size of his own skull. He therefore approaches his task with full humility, and avoids clever tricks like the plague.” The mantra DRY (Don’t Repeat Yourself) is programmer dogma and is present in many programming books and classes. This principle has not made it into the terminal’s user interactions.
Summary
Every program here consistently quits in a different way from all the other ones.
A final point here is, even though we are used to discussing these commands as “keyboard shortcuts”, these are not alternatives but the only way to run the command. Popular guides will also encourage usage of these programs by saying they are “keyboard accessible." The idea that keystrokes can provide a productivity boost but shouldn’t be the only interface is ingrained in the English language.
Program
How to exit
vim
* Get out of insertion mode by hitting esc * Type :q
emacs
Ctrl-x Ctrl-c
nano
Ctrl-x
tmux
Ctrl-b + d (detaches session)  Ctrl-b + :kill-session to kill session
screen
Ctrl-a + d (detaches session)  Ctrl-a + k (kill session)
Normal terminal session
Ctrl-d (End-of-Transmission / EOT)
At Warp, we believe the terminal also can be a delightful
product
, in addition to a powerful utility. We are building a terminal from the ground-up with the user in mind.
Request early access to our beta. We look forward to your input!
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
