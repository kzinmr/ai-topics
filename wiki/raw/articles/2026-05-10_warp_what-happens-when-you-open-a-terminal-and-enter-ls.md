---
title: "What happens when you open a terminal emulator and enter “ls”"
source: "Warp Blog"
url: "https://www.warp.dev/blog/what-happens-when-you-open-a-terminal-and-enter-ls"
scraped: "2026-05-10T01:28:24.021986+00:00"
lastmod: "2026-04-24T15:03:34.000Z"
type: "sitemap"
---

# What happens when you open a terminal emulator and enter “ls”

**Source**: [https://www.warp.dev/blog/what-happens-when-you-open-a-terminal-and-enter-ls](https://www.warp.dev/blog/what-happens-when-you-open-a-terminal-and-enter-ls)

Engineering
What is a Terminal Emulator? Understanding 'ls' Command
Suraj Gupta
Andy Carlson
January 11, 2023
Introduction
History - From Teletypes to Terminal Emulators
‍
Opening the Terminal App
‍
What Needs to Be Initialized
‍
Creating a “PTY”
‍
Spawning the Shell
Shell Initialization
Login vs Non-login Shells
Running a command
Entering keystrokes
Hitting Enter
Parsing a command
Returning output
Escape Sequences
Closing the terminal
‍
‍
Introduction
“What happens when you open a web browser and enter google.com?” Many of us recall being asked this question before. I think it leaves an impression because navigating web pages is this magical process that we take for granted. We do it hundreds, if not thousands of times per day without knowing how it works. Most developers and engineers can explain
parts
of it, but the depth at which you can
discuss
this question is infinite.
Today, we’ll discuss the details of something else we take for granted: the terminal. What happens when you open a terminal emulator and enter “ls”? Like with browsers, there is too much content to fit into one blog post. We’ll give you what we think are the interesting details.
History - From Teletypes to Terminal Emulators
Much of how modern terminal apps work comes from their historical predecessors:
teletypes
(TTY for short). These machines were designed for an era when entire institutions might’ve had just one or a few mainframe computers, when data was stored on magnetic tape, and when a computer’s memory was measured in kB.
‍
‍
Figure 1
: An IBM 2741 teletype
1
and the IBM System/360 Mo. 40 mainframe computer.
2
These were released in the late 60s, and were prevalent until the 70s. The purchase of one of these mainframes (>$200k at the time) included a teletype.
3
Teletypes were basic text clients to allow users to interact with a computer. It’s short for “teletypewriter” because they descend from typewriters, and are partly mechanical devices. They communicated with the computer via a physical wire connecting the two devices. The communication worked like this:
ASCII text would be transmitted character-by-character over the wire as the user typed.
The kernel of the mainframe would receive the input and decode it.
The text gets sent to a driver called the
TTY driver
. This kernel module was responsible for sending this input to user programs and collecting the output.
Finally, the kernel sends that output back to the teletype for display to the user.
One thing to mention is the
line discipline
, which buffered the characters in kernel memory. The program wouldn’t receive the input until “Enter” was pressed. The line discipline allowed this buffer to be editable and provided some program-independent shortcuts, e.g. ctrl-w. It was also an important performance optimization at the time because asking the program to react to every individual character was highly inefficient.
4
As computing advanced, many of these individual components modernized. For example, teletypes were replaced by terminals which were fully electronic machines, including electronic displays.
‍
Figure 2
: A VT100 (VT = video terminal), released in 1978 by DEC.
5
This model implemented and popularized the ANSI escape codes which are still used today.
‍
With electronic terminals came new affordances like colors and bell sounds. Fundamentally, however, this machine did exactly the same thing that the teletype did: send a stream of input characters and display output.
Of course, computing has changed a lot since then. But curiously, much of the workings of modern terminal apps resembles this classic teletype architecture. Like with other systems with multiple interfacing parts, individual components can improve but still be subject to compatibility requirements with other components. With this convoluted history in mind, it's a bit easier to understand why the terminal ended up the way it did.
Opening the Terminal App
Finally, let’s fast-forward to today. Terminals are no longer dedicated pieces of hardware. Now everyone has a general-purpose computer that runs an operating system which oversees many user apps. The terminal is just one of these apps.
‍
‍
Like a typical GUI app, the terminal is a process under the supervision of the operating system and will listen for events and input from the user, and tell the OS what to display in a window. Note that the app doesn’t
directly
interface with these peripherals, there are things like drivers and a window manager sitting in between.
You’ll sometimes hear these apps referred to as
“terminal emulators”
instead of simply “terminals”. Since the term “terminal” used to refer to a dedicated piece of hardware, we consider these apps as emulating that device. However, most people simply say “terminal.” So what happens when you open your terminal?
What Needs to Be Initialized
Fundamentally, the terminal is an app that enables you to “use your computer,” i.e. run programs on it. You’ve probably written commands like
ls
,
rm -rf node_modules
,
mv file folder
, and the like.
ls
,
rm
and
mv
are programs (
written in C
if you’re curious). Using your computer may involve more than issuing simple commands like these. We may want to automate things with scripts which group together a sequence of many commands, use branching conditional logic, run repeated loops, or parallelize commands, etc. To service the full spectrum of use-cases, we want a full, interactive, interpreted programming environment. These are not implemented in the terminal emulator. The work of running other programs as processes and interpreting the commands you write is done by a shell. There are several choices of shell. Popular ones include
Bash
),
Zsh
, and
fish
). The terminal and the shell are separate programs with separate concerns: the shell with the content of the commands you type and the terminal with the UI-related things, e.g. fonts, colors, tabs, scrolling.
To get things started, the terminal needs to spawn a process for the shell the user wants, as well as a method for communicating with the shell and with any processes the shell starts.
Creating a “PTY”
Before the terminal spawns a child process for the shell, it establishes a way to communicate with it. Much like their teletype ancestors, terminal emulators work by streaming characters as the user types them. Streaming into
what
, though? There is no longer a wire to another computer because everything is happening on one system. Instead, the wires of the traditional TTY are replaced with pairs of file descriptors known as the
PTY
, short for pseudo-TTY. These files are like the two ends of that wire that transmits user-entered input to programs and sends back the output.
The terminal asks the kernel to create these files. There is still a TTY driver in the kernel with a line discipline responsible for mediating the data between the two ends of the PTY. One end is the
leader
6
, intended for the terminal to interface with, write user input to, and read output from for display to the user. The other end is the
follower
, which will be used by the shell and all other processes created in the session.
‍
‍
Remember that in Unix, many things are
treated as files
, i.e. they have the same read/write interface that files do. These file descriptors (fd) are not “normal files,” but virtual
character devices
. The fd for the leader just points to a buffer in memory, while the follower is a character device file with an actual path on disk. If you want to see what that path is, run the
tty
command from the terminal. You can write to this path from a different process and see the data you write appear in the other session!
‍
‍
Spawning the Shell
Before receiving the user's first command, the terminal has one remaining task: spawn the shell process. Shells are fully interactive programming language interpreters. It is here where the power of programming constructs, e.g. conditional statements, loops, parallelism, lies. The shell is also what creates the child processes for each command that the user wants to run. The shell is the first child process of the terminal session. The terminal will spawn it and set it to read and write from the PTY
follower
. It does this by setting the shell’s stdin, stderr and stdout (fd 0 through 2) to the PTY follower.
‍
‍
At this point, the shell is ready to take over! It has its own initialization process.
Shell Initialization
When the shell initializes, it runs some startup scripts to enable users to customize the experience. This may involve setting environment variables, aliases, functions, or printing any information the user may want to see when the session starts. The exact paths of these scripts depend on a couple of things: which shell you’re using and whether or not the session is a login shell.
Login shells are shell sessions wherein this shell process is the one the user is logging into the system with; the process is the first process under this user ID. For example, if you log into a server running the Linux distribution Ubuntu Server, which doesn’t have a GUI environment, you’ll be logging in with a shell and that is a login shell. On the other hand, if you are already logged in and you start a subshell in a session, it will be a non-login shell.
Note:
Many terminal emulators and multiplexers are configured by default to start your sessions as login shells even if they technically
aren't
.
Login vs Non-login Shells
Login shells have a different set of startup scripts from non-login shells, and their file paths depend on the shell. Also, most shells will have both system-wide scripts and user-specific ones. To take Zsh as an example, non-login shells run
/etc/zshrc
for all users and then
$HOME/.zshrc
for the logged-in user. Login shells will also run
/etc/zprofile
and
$HOME/.zprofile
respectively. Traditionally, there is one login shell session for a user, as any subsequent shells, for example if they use
screen
for multiplexing, will be non-login shells.
Suppose you have a Raspberry Pi at home. You want it to sync with your Dropbox files, but you only need it to stay in sync while you are logged in. Suppose you have installed a Dropbox client daemon that talks to the Dropbox API to keep your files in sync. You would put a command to spawn that daemon in
$HOME/.zprofile
, because if you put it in
$HOME/.zshrc
, you would get multiple instances of that daemon if you opened multiple shells. Another example is that you may want to put expensive things in the login shell. For example, maybe on login you want to see some resource usage statistics, like disk usage with the
du
command. The
du
command can be rather slow, so you may only want to see this once when you log in rather than on every session.
Finally, the shell prepares itself to accept user input. This usually involves printing a prompt. It might look something like:
user@ubuntu:/var/log$
. Most shells store the content of the prompt in a variable, e.g.
PS1
for Bash and Zsh. Most shells also support dynamic information in the prompt in two ways:
They have placeholders to substitute variables for each prompt, e.g.
%d
for the working directory. See
here for all Zsh
placeholders.
If the shell has no placeholder for the particular information you want to show, most shells can run some arbitrary code before printing the prompt for each command. Therein you can re-assign
PS1
with the new information. For example, Zsh recognizes a variable
precmd_functions
which is an array of functions that run before each prompt. One use for this is adding the name of the active
Conda
environment to the prompt.
Now that we know what happens when you
open
a terminal application, let’s explore what happens as you
interact
with the terminal.
Running a command
Entering keystrokes
As a terminal user, the primary mode of interaction with a terminal emulator is with your keyboard device. Traditional terminals were limited to keyboard interaction by their hardware and while hardware has evolved (e.g. the addition of a mouse device), terminals still primarily rely on keyboard interaction.
When you type in the terminal, the keystrokes are first translated to ASCII characters (e.g. the backspace key is translated to the ASCII character 0x08). These characters are then written to the PTY leader by the terminal. Recall that the PTY
leader
is the end of the PTY that interfaces with the
terminal emulator
, while the PTY
follower
interfaces with the
shell
. The TTY driver then reads the characters from the PTY leader and stores them in its line discipline, which acts as an intermediate buffer between the PTY ends. The line discipline’s job is to interpret the characters from the PTY leader its own character set and then process them. How a character is processed by the line discipline is solely dependent on the character itself.
Let’s consider two categories of line discipline characters
special characters
7
(e.g. ERASE, INTR)
everything else (e.g. characters like “l” and “s”)
Depending on the special character, the line discipline will decide whether it needs to write back to the PTY leader, write through to the PTY follower, or both. For example, when the line discipline receives a BS character (ASCII 0x08) which is entered by the
backspace
key, it interprets it as an
ERASE
character. To process it, the line discipline will edit its internal buffer by removing the last character and then writing the delete intent back to the PTY leader. The terminal emulator can then read the change from the PTY leader and reflect it in the terminal display. Notice that the PTY follower was never written to in this case.
On the other hand, when the line discipline receives an ETX character (ASCII 0x03) which is entered by the keys
CTRL-C
(and displayed as ^C), the line discipline will interpret it as an
INTR
(short for
INT
E
R
RUPT) character: it’ll send a SIGINT to the PTY follower in order to interrupt any processes running in the foreground (i.e. programs reading input from and writing output to the terminal). Note that background processes are unaffected.
8
The line discipline will also write the ETX + linefeed characters back to the PTY leader, which is why the terminal emulator then displays
^C
and moves to the next line.
For all non-special characters, like the friendly “l” and “s”, the line discipline will just write the character back to the PTY leader. Since they are written back to the leader, the terminal program reads them back out and into the display which creates the “echo” effect of characters as they’re typed. Otherwise, you wouldn’t actually be able to see characters while you type!
Gotcha: While the line discipline is a useful construct, most modern shells actually disable the line discipline’s editor and “echoing” feature. Instead, characters are buffered by the shell process itself so that the shell can implement features like tab completions and
autosuggestions
which
need
to see characters as they’re typed. That being said, parts of the line discipline are still used. For example, the handling of some special characters, like ^C, is usually still delegated to the line discipline. That way, if the shell process is too busy to handle user input (e.g. it’s in an infinite loop), the foreground process can still be sent an interrupt signal. A shell can control these terminal settings via the
termios
interface.
9
You might be wondering why we, as terminal users, would care about a line discipline. Well, since the line discipline acts as an intermediary between the PTY ends, that means we can actually configure it to change how characters are interpreted (among other things). For example, let’s say I wanted to use ASCII 0x0E (entered as
CTRL-N
and displayed as ^N) to send an interrupt. The line discipline can be configured to handle this!
‍
Notice how CTRL-C does not terminate the `sleep` once we change the stty configuration.
‍
In this case, when the line discipline receives ^N from the PTY leader, it interprets it as an INTR character and sends a SIGINT to the PTY follower.
There’s still one special character that’s important for our journey: NL (short for
N
EW
L
INE), which is the special line discipline character that’s translated from the NL (ASCII 0x0A) and CR (ASCII 0x0D) characters (usually entered by the
Enter
,
CTRL-J
or
CTRL-M
keys).
10
Gotcha: In Warp, entering keystrokes is not the same as entering keystrokes in a traditional terminal. While keystrokes are directly sent over the PTY as they are entered in a traditional terminal, Warp only sends the keystrokes over the PTY once
Enter
is entered (or a designated keystroke, e.g.
CTRL-C
). Instead, the input buffer is maintained at the app layer rather than at the TTY (as part of the line discipline) or shell layer. This allows Warp to provide an
IDE-like editing experience
.
Hitting Enter
This brings us to one of the final parts of our journey: executing a command. Like we’ve seen before, these seemingly simple actions we do everyday (like opening a terminal) are actually more complicated than expected.
Carrying where we left off: once the
Enter
key is pressed, the terminal will send the CR ASCII character to the line discipline which will interpret it the same as an NL character. To process this character, the line discipline will forward its internal buffer along with the line feed to the program listening on the PTY follower (i.e. the shell). From this point, our discussion will focus on the shell's role in executing a command.
Parsing a command
Once the shell receives the user input and linefeed, it begins to parse the command to figure out what it means.
First, the command is tokenized and syntactically/semantically analyzed. For a simple command like “ls”, that’s easy! But for a more complicated command, the shell needs to make sure it actually makes sense:
ls > foo.txt
(correct)
ls >
(incorrect syntax; token missing after
>
)
ls | foo.txt
(incorrect semantics; both sides of a pipe need to be runnable processes)
Note that each shell comes with its own programming language so syntax and semantic analysis is done differently from shell to shell (e.g. the conditional AND operator is written as
&&
in Bash while it’s written as
and
in fish)
Next, tokens that aren’t shell keywords nor paths need to be resolved for meaning. That is, the shell needs to determine what these tokens actually refer to. To do so, the shell searches through a few different primitives to find what a token references:
aliases
: a mapping between a user-defined word and other tokens, often used to abbreviate complicated commands
e.g.
alias ll="ls -lh"
functions
: a sequence of shell statements grouped together for a particular purpose (akin to “functions” in other programming languages)
e.g.
function mkcd() { mkdir -p $@ && cd ${@:$#} }
environment variables
: a set of global variables to retain data throughout a shell’s lifetime
e.g.
HOME=/Users/bob
(referenced by
$HOME
)
builtins
: predefined set of commands implemented within the shell executable itself
e.g.
echo
,
cd
,
pwd
,
exit
,
kill
PATH executables
: external commands that the shell can locate (via the $PATH variable
11
) and run
e.g.
brew
,
git
,
docker
,
k8s
It’s worth noting that aliases, functions and environment variables will expand to more tokens, so this resolution process is actually recursive!
If you’re ever unsure what a token references, you can use the
type
command to see how the shell will resolve that token:
‍
https://app.warp.dev/block/3R8oLrzGaDvl2jS8OANCYa
‍
If you’d like to persist aliases, functions and environment variables (e.g. changes to
$PATH
) across shell sessions, you can do so by writing them in your shell's resource file (see
here
for an example of how to do this in Bash and Zsh).
Out of the 5 groups mentioned above, executables are the most interesting. Unlike builtins which are handled within the shell process, executables are separate programs (files with the executable bit set) that need to be located on the filesystem and executed as a separate process (i.e. as a forked process). When the shell locates the executable, it will fork a process and run the executable in the child process, passing along any command arguments.
To visualize these different processes, you can think of the terminal emulator as the root of a process tree where one if its children is the shell itself and any programs you run are descendants thereof. In fact, you can visualize this tree with the
pstree
command! All you have to do is provide the process ID of the terminal. Here is an example of a terminal with 3 tabs (i.e. 3 sessions):
https://app.warp.dev/block/RFg1c0MUKy63DsBb8Hj7I5
In this example, the terminal emulator process (Warp) has PID 84860 and the tabs/shell processes have PIDs 84890, 85525 and 86041. In one of the tabs (PID 86041), we’re running
tmux
and hence, it’s a direct child of that shell process itself, as expected!
Gotcha: at some point, you might have wondered why some “commands” are both builtins and executables. For example,
echo
is usually both a shell builtin but also available as an executable. Shells will offer builtin alternatives to executables when they can be more efficiently run within the shell process itself rather than forking and running another process. Some commands, like
cd
, just can’t be executables because they need to mutate the shell process’s state. If
cd
were to be run as an executable, it would run in a child process and modify the
child process’s
working directory as opposed to modifying the
shell process’s
working directory.
Returning Output
Since our command
ls
is pretty simple, we don’t need to do much tokenization/resolution. Let’s assume
ls
resolves to
/bin/ls
. As mentioned before, the shell will fork a child process and have it run
/bin/ls
within. Since the child process inherits its parents’ file descriptors, the output produced by the child process will get written to the PTY follower, which is shuffled along to the line discipline. Instead of processing these bytes, the line discipline will just forward them to the PTY leader. The terminal emulator app will then read the characters from the PTY leader and display them on the screen.
Hopefully you have a better high-level understanding of how the character output produced by
ls
makes its way to your terminal screen! But we’re still missing a few things. Notice that in the following command/output pair, the output is all the same color:
https://app.warp.dev/block/YQf4xeJwtIK5vYEQrAYA39
But oftentimes, output will have text decorations like colors and bolding. For example, in the following command/output pair, the output is intentionally colored (directories are a different color from simple files, which are a different color from executables):
https://app.warp.dev/block/OjfO0sTU2UzCvPoguX2uYX
So how did
ls
emit these colors? And how did the terminal emulator know what to do with them? The answer is escape sequences!
Escape Sequences
It turns out that the shell (and other programs) can emit more than just plain-old-characters for the terminal to print. They can emit
escape sequences
to have
control
over the terminal, including text decorations, moving the cursor, scrolling, etc.
In this case, the directories are printed a different color because there is an escape sequence to first change the foreground color before the characters for the directory name are emitted. So by the time the characters for the directory name reach the terminal, the terminal will know to print these characters with a certain color. It’s the terminal's job to actually render the characters on the screen with an appropriate color (an incompatible terminal would just ignore the escape sequences). Let’s look at the escape sequences emitted by the output of
ls --color
:
https://app.warp.dev/block/a7kW0Jk6vyu6UQx4hbZmUQ
First, note that escape sequences are characterized as a sequence of bytes that start with the ASCII ESCAPE character (
\x1b
in hexadecimal and
\033
in octal). That’s why they’re called escape sequences!
All of the escape sequences in this output have the format
ESC[c1;...;ckm
. These are called
Select Graphic Rendition
(SGR) escape sequences and are used to assign attributes, like text decorations, to characters. The ci’s are the codes that control the rendering. For example, the code
1
is used to turn on bolding. The code
3x
is used to set the foreground color (where x ∈ 0, 7] is an ANSI color).
Let’s dissect the escape sequences above, one by one:
The first escape sequence is used to turn on bolding which explains why
dir
is bolded in the final output. The second escape sequence sets the foreground color, specifically to cyan. The next part is an unescaped sequence of bytes and is simply the name of the directory
dir/
. The next escape sequence combines setting the foreground and background colors back to their defaults. And the final escape sequence is used to reset all the SGR attributes.
As an exercise to the reader, try to come up with the escape sequence needed to print the name of the executable with its color (see
here
for the answer).
With so many different programs and various terminal applications, there needs to be a specification that guides CLI developers and terminal builders (that’s us!) to interact in a consistent and correct manner with one another.
12
The ANSI X3.64 was one of the first popular specificationsthat provided a guide on how to control the terminal via escape sequences.
13
It was adopted by the popular
VT100 terminal
. The spec itself, however, didn’t actually include all that many escape sequences. As terminals evolved from physical devices to software and gained access to better hardware like displays with color, the specs also kept evolvingto give CLIs even more control.
14
Back when it was first written, the X3.64 spec didn’t need to include escape sequences for colored text because the physical terminals at the time could only support monochromatic text! Nowadays, if you’re going to build a terminal emulator, you’ll likely want to implement the widely-adopted
xterm spec
which includes escape sequences to color text, for example.
Closing the terminal
Now that you know all the gnarly details about what happens when you enter “ls”, you might just want to close the terminal and forget about it (we hope you don’t feel the same way about this blog). But closing a terminal is its own can of worms! When you close your terminal, you’re also quitting any active shell sessions. And before a shell quits, it might run a logout script (if any), write the commands from the session into a history file and so on. The actual teardown will be pretty boring: killing child processes and cleaning up file descriptors. We omitted some details here, but that’s pretty much it.
Footnotes
1.
https://en.wikipedia.org/wiki/IBM_2741
2.
https://www.ibm.com/ibm/history/exhibits/mainframe/mainframe_PP2040.html
3.
https://www.ibm.com/ibm/history/exhibits/mainframe/mainframe_PP2025.html
4.
https://www.sobyte.net/post/2022-05/tty/
5.
https://en.wikipedia.org/wiki/VT100
6.
You might come across the terms “master” and “slave” instead of “leader” and “follower” (respectively) in other readings.
7.
See here
for a more complete list of special characters.
8.
To see this, try running sleep 100 & and then CTRL-C. The process for sleep 100 will still be running in the background (can be confirmed with ps).
9.
See here
for an example of how zsh does this.
10.
Technically, there’s a dedicated CR line discipline character, but it behaves just like NL in most cases.
11.
The $PATH variable is a list of directory paths that the shell will search through when it’s trying to find an executable.
12.
Terminal applications will usually set the $TERM variable
which CLIs can query to check which spec the terminal emulator app is following and take advantage of its features.
13.
ANSI escape code history
14.
Since most terminal specs are supersets of previous widely-accepted specs, they are often backwards-compatible.
See here
for an example of fish running on a VT220!
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
