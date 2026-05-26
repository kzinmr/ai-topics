---
title: "Copying Remote Command Output to Your macOS Clipboard"
url: "https://it-notes.dragas.net/2026/05/26/copying-remote-command-output-to-your-macos-clipboard/"
fetched_at: 2026-05-26T07:14:42.702004+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Copying Remote Command Output to Your macOS Clipboard

Source: https://it-notes.dragas.net/2026/05/26/copying-remote-command-output-to-your-macos-clipboard/

I use Apple devices very often. Overall, I like macOS. Certainly more than Windows.
One of the things I find extremely useful is a command I discovered not too long ago:
pbcopy
.
pbcopy
can be used to copy to the clipboard whatever it receives from standard input. For example, when I am in a shell, I often use a command like this:
cat filename.md | pbcopy
At that point I know that the content of the file is in the clipboard, and I can paste it wherever I need, calmly and without any additional steps.
There is one limitation, though: this only works locally. It works when I am using my Mac and I want to copy something from the macOS shell.
When I connect to a remote (*BSD, Linux, illumos based) server via ssh,
pbcopy
is not available. Or, more precisely, even if I create a command with the same name on the server, that command cannot directly talk to the clipboard of my Mac in the usual way.
Luckily, modern terminal emulators have a few tricks available.
I use iTerm2 for most of my ssh sessions and, once I realised how useful it would be to have something similar to
pbcopy
in remote sessions too, I created a small script that works both on Linux, the BSDs and illumox based OSes.
The caveat is that the remote server cannot "magically" access the clipboard of my Mac. So the trick works because the remote command prints a special terminal escape sequence, and the local terminal emulator interprets it.
The sequence is called OSC 52. In short, it allows a program running inside the terminal to ask the terminal emulator to put some base64-encoded text into the local clipboard. This means that support depends on the terminal emulator I am using locally.
I use iTerm2, which supports OSC 52. Other terminal emulators support it too, so the idea is not tied exclusively to iTerm2. However, Apple's default Terminal.app does not appear to support OSC 52, so I would not expect this specific solution to work there.
So, in practice:
with iTerm2, it works;
with other OSC 52-compatible terminals, it should work (I haven't tested it, but should work with kitty, Ghostty, etc.);
with Apple's Terminal.app, at least at the time of writing, it should not.
Before creating the command on the remote server, a specific iTerm2 option needs to be enabled:
Settings -> General -> Selection -> Applications in terminal may access clipboard
This option allows programs running inside the terminal to access the clipboard through escape sequences.
Of course,
this has security implications
. A program running in the terminal, including a program running on a remote server through ssh, may be able to write to the local clipboard. For my use case this is acceptable, but it is worth knowing what is happening.
All I need to do is create a command, a small sh script. I log into the server where I want to create the command. In my case, I usually create a file called
/usr/local/bin/pbcopy
with the following content:
#!/bin/sh
printf '\033]52;c;%s\a' "$(base64 | tr -d '\n')"
Then I make it executable:
chmod a+rx /usr/local/bin/pbcopy
From that moment on, I can use
pbcopy
on the remote server too, piping another command into it:
cat filename.md | pbcopy
The content will not end up in the clipboard of the remote server. It will end up in the local clipboard of my Mac, because iTerm2 receives the OSC 52 sequence and updates the macOS clipboard.
