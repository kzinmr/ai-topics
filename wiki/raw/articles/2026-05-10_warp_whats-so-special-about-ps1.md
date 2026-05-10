---
title: "What’s so special about PS1? Fun with customizing Bash command prompts"
source: "Warp Blog"
url: "https://www.warp.dev/blog/whats-so-special-about-ps1"
scraped: "2026-05-10T01:28:24.485431+00:00"
lastmod: "2026-04-24T14:59:35.000Z"
type: "sitemap"
---

# What’s so special about PS1? Fun with customizing Bash command prompts

**Source**: [https://www.warp.dev/blog/whats-so-special-about-ps1](https://www.warp.dev/blog/whats-so-special-about-ps1)

Engineering
What’s so special about PS1? Fun with customizing Bash command prompts
Agata Cieplik
February 23, 2022
Long ago, when I was still a console newbie, I copied my friend’s bash configuration file. It had all the necessary stuff already included - aliases, colors, and most importantly: a nice prompt setup. I used it on all machines I had access to due to all the extra context it provided. For example, it would turn red when I was on a production machine, show me a current git branch from the repository I was working on, and indicate whether I had any changes to commit by showing a star.2
Today there are a seemingly endless set of tools for configuring the command prompt to your liking, but back then things like
Starship
were completely non-existent. Most developers I know have customized their prompts in one way or another. This fact, combined with the feedback we’ve received from the Warp community, was good motivation to dig deeper into prompt customization in Warp.
In this post I’m going to tell you how we implemented support for PS1 in Warp, and why adding it was technically challenging. Along the way, we’ll also tackle the DCS (device control string) and some fun shell tricks!
Hey, Cieplik, what actually
is
PS1?
Glad you asked! PS1 is one of the few variables used by the shell to generate the prompt. As explained in the
bash manual
, PS1 represents the
primary prompt string
(hence the “PS”) - which is what you see most of the time before typing a new command in your terminal. On top of that there are actually few more - from PS0 to PS4, each of them executed and printed in different contexts of command execution. For example, you’ll see PS2 whenever the command has multiple lines as a
secondary prompt string
. And then zsh also provides RPS1, which displays the Prompt String on the right-hand side… there's a lot to work with.
Each of the Prompt String variables can easily be customized with the
backslash-escaped special characters
, but they can also contain shell function calls or even emojis, since most modern terminals support unicode.
With Warp in the works we made a decision to provide useful defaults for users to help them hit the ground running when using a new app. This included the prompt. We explicitly decided to
not
support PS1 in Warp, as it could clash with the
bootstrapping script and PRECMD/PREEXEC hooks
we use to create blocks of inputs and outputs. By implementing our own default prompt we had much more control over the user experience, and that was critical at the early stages. Eventually, however, it became obvious that our users really need their custom setups and lack of certain information on the prompt may actually slow them down. It came time for us to honor the user’s PS1 settings. Keep in mind that this is not our last word on this topic!
What’s under the Prompt String’s hood?
In Warp, because we buffer the user’s input, we can’t allow the shell to directly render the prompt. Instead we use the metadata from the shell to do our own rendering. Our app receives it from the shell via the PRECMD hook, to do things like retrieve the current git branch, which is used in Warp’s default prompt. We use a special escape sequence and a JSON string packed with data to pass all the necessary information.
This is why we decided that the best way to support PS1 in Warp is to pass it as part of our PRECMD hook. The first challenge, however, comes from
printing
the variable into this JSON string.
Your PS1 is usually a set of variables, like information about the colors you want to see, but sometimes it can be a function call too. We have to translate it into a
rendered
Prompt String - a set of escape sequences and characters that tells the terminal the exact string to print and how to print it.
Here’s the example of an oh-my-zsh PS1 setting
Embed:
https://gist.github.com/gagata/2c5321590dc1be54be4524e3183289c3
In zsh rendering a prompt is actually quite simple. You just
print
it. (and the shell expands all parameters for you via
prompt parameter expansion
.) We insert the output into our JSON and display it on our terminal.
‍
Note that the middle prompt is the output of the print command, prepended with "rendered prompt" for clarity.
‍
Bash does have a similar way of
expanding prompt parameters
as zsh does, so we could easily run echo ${PS1@P}in our script to get the rendered prompt and call it a day! Except…
That functionality has only been introduced in bash 4.4+. But Macs do not ship with that by default (this is related to a licensing change: since version 4.0, bash switched to a GPL license, which is not supported by Apple). The question, then, is how do we render the PS1 in older versions of bash without using any special tools or libraries?
The way we ended up solving this issue is by invoking a subshell, executing a very simple command in it, capturing the entire subshell output (including the prompt), and then manipulating it to only capture the prompt itself.
This is the final code we’re currently using in Warp to get the value of the rendered bash prompt:
Embed:
https://gist.github.com/gagata/c5d57eeb2019c8216354a451e9c63a38
Let me break that down, pipe by pipe:
echo -e "\n"  prints an empty line in our subshell;
PS1="WARP\_PS1" bash --norc -i 2>&1 we pass a previously captured $WARP\_PS1 value as the PS1 in the subshell, and specify that no configuration files should be loaded (norc argument) to improve the performance of this operation; the -i flag denotes an interactive shell, while 2>&1 redirects the stderr to stdout, which allows us to capture the rendered prompt;
Head & tail operations simply help us manipulate the output to extract the prompt only.
That’s it. We've got our rendered prompt, we can start showing it in Warp!
‍
‍
Escaping the Prompt
Some things and places are really hard to escape, like
the Russian city of Omsk, where even stray dogs cannot leave
. Escaping in the terminal realm is really close to that experience, and Prompt String seems to make it even harder.
When juggling shell data and passing it to Warp via our PRECMD hook, we escape
escape sequences
that may break our JSON string with our magic sed invocation:
Embed:
https://gist.github.com/gagata/ef7cb5a8cfb2ecf5cf124f375faadb04
This is actually a series of replacements:
All double-quotes and backslashes are replaced with their escaped versions (\” and \);
\b (backspace), \t (tab), \f (form feed), \r (carriage return) are all replaced with their escaped versions;
We add an escaped \n (new line) on every line explicitly, since sed analyzes the input line-by-line and thus is not aware of the actual new lines.
This worked great, yet with the Prompt String you actually get many more things to escape: it’s not uncommon for the rendered prompt to include some extra bells and whistles (I mean the actual bell character - \a) and lots of other non-printable characters and escape sequences (most significant being \x1b aka \e or \033, which is literally
ESC
). Note that those sequences also had to be
double escaped
, to not only create a valid JSON string, but also not break our Rust implementation when
unescaped
! At least we were able to use the same tool for both supported shells this time!
In the first iteration, the final sed call looked a lot like:
Embed:
https://gist.github.com/gagata/8f6bb570c67cdc115d3aa80ad072a108
Back to the whiteboard
At this point, we started testing internally. It was then that we found a mysterious behavior.
A common tool used to customize the prompt in zsh -
oh-my-zsh
- is used by many team members. The prompt rendering worked for every theme...except the
default
oh-my-zsh theme. When the theme was used, the entire bootstrapping script would fail, leaving Warp in an unusable state.
Robby Russell’s oh-my-zsh prompt theme
It turned out the little arrow (➜) to the left was the root cause!
With shells and terminal emulators it always makes sense to analyze the actual bytes that are being processed. Let's check what’s under the hood of this little arrow:
This particular emoji consists of 4 bytes: e2, 9e, 9c and 0a. A careful reader may notice that both 9e and 9c bytes come from the extended ASCII table, but do they carry any special meaning? When in doubt, it’s always good to go back to the source - in this case, check the
shell parser documentation
. For completeness, let's quickly unpack what VT100 (and other VTs) is, and what this mysterious DCS is that are both mentioned in the linked docs:
VT100 was a Video Terminal introduced in the 70s. It was one of the first machines that allowed for cursor control with ANSI-escape codes, and added a bunch of other control options. Later on its spec became a de facto standard, and modern terminal emulator programs try to follow it (including Warp).
Control characters and control sequences in the terminal world are special ANSI-escape characters that control the terminal’s behavior. It can be anything from the cursor position, mouse control, even colors. DCS (device control string) is a special control sequence that is followed by a data string. You can find out more
here
.
unhook
When a device control string is terminated by ST, CAN, SUB or ESC, this action calls the previously selected handler function with an “end of data” parameter. This allows the handler to finish neatly.
As it turned out - the 9c byte carried a special meaning in a terminal world - it’s an
ST (string terminator) escape sequence
, which also happens to denote the
unhook
operation. As a result, the emoji in our JSON string would prematurely end the PRECMD hook, making it impossible for Warp to fully start.
From there the solution was simple - rather than trying to escape emojis and unicode characters that may have similar issues in the future, we simply encoded the entire Prompt String as a hexadecimal string. This completely eliminated the need for using sed and simplified our shell script.
Below you'll find a snippet with our current precmd function (example in bash):
Embed:
https://gist.github.com/gagata/d9b48d8c3037e8a57abbd87f3b534155
Future of the prompt
Warp now has the option to honor the user's PS1 setting. It works with most configurations, though you’ll find the full compatibility table in our
docs
.
It is not, however, the last time you'll hear from us about working on the prompt. Our
key product principles
include fixing the UI and providing a great out-of-the box experience. One of the ideas we're currently exploring is Context Chips - our low-calorie approach to snacking on bite-size information.
We’re working on plenty of interesting problems just like this one at Warp; and we’re hiring! If you want to be a part of
our team
and work together on improving the day-to-day life of developers from around the world - check out our
careers
page.
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
