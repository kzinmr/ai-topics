---
title: "Peeking inside the bash rabbit hole"
url: "https://www.johndcook.com/blog/2026/11/14/bash-rabbit-hole/"
fetched_at: 2026-11-15T10:00:55.844966+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Peeking inside the bash rabbit hole

Source: https://www.johndcook.com/blog/2026/11/14/bash-rabbit-hole/

I have much bigger issues to be concerned with than saving a few seconds of typing with obscure bash features. But precisely because I have bigger issues on my plate, it’s fun to take a moment and solve some little tangible problem.
The shell
!$
saves the last part of the latest command. (Mnemonic: bang often refers to commands, such as
!!
to redo the previous command, and cash often refers to the last of something, such as the end of a line in a regular expression.)
This comes in handy, for example, when you copy a file to a directory and then want to cd into that directory.
cp myfile /big/long/path
cd !$
The
!$
variable is fragile, however. The sequence of commands
cp myfile /big/long/path
ls
cd !$
won’t work because after running
ls
the variable
!$
now contains “ls” rather than “/big/long/path”.
There are two ways to fix this. In the previous example you could change the last command to
cd !-2:$
This says go back two commands (
!-2
) and extract (
:
) the last argument (
$
).
Another possibility is
cd !cp:$
This says to pull up the most recent command that started with “cp” (
!cp
) and extract the last argument.
This only scratches the surface of conveniences bash offers. To learn about similar features, search on “history expansion” or “event designators.”
Because bash offers so many shortcuts, it’s hard to learn any of them from reading the manual: nothing will stick. It reminds me of when I was in Paris and had one hour to see the Louvre. I should have meandered around a room or two and been content with that. Instead, I blitzed through the museum. I wanted to “see the Louvre” but I didn’t really
see
anything.
