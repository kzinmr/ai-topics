---
title: "tools"
url: "https://jyn.dev/tools/"
fetched_at: 2026-04-28T07:02:50.968637+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# tools

Source: https://jyn.dev/tools/

i care a lot about my tools. i have very high standards for tools along some axes, and low standards along others—but that's the topic of a different blog post. this post is about the tools i
do
use, and about tools i have my eye on and may use in the future. hopefully it will be useful to other people, such as programmers, sysadmins, etc.
this is also not a description of
how
i use these tools, which also deserves its own blog post (i pride myself on integrating tools that were not designed to integrate with each other). this is just a list of the tools themselves.
i have a version of
tools i have my eye on
for myself that i keep regularly updated. i will probably not keep this public copy updated, unless i find a tool that's sufficiently good i want to tell people about it.
i'm always on the lookout for more useful tools. if you have a tool you use regularly that's not on this list (and not specific to a single language ecosystem), please
let me know
. the one exception is containerization software. i am interested in tools to
interact
with containers, but at this time i am not looking for more container hosts (podman, kubernetes, vagrant, lxc, systemd-nspawn, firejail, chroot, etc).
basics
you have probably seen someone else recommend these tools. it's not just hype. they are useful.
ripgrep
: file contents searching
fd
: file name searching
jq
: json processing. note that most data formats can be converted to json, which i recommend over
yq
or other format-specific filtering tools; the exception is XML and things isomorphic to it, which
cannot be represented in json with fidelity
. i tried a rewrite,
jaq
, that promised to be faster, but it had fewer features and it turns out that i rarely care about the speed of jq.
killall
: kill matching processes
pkill
: kill specific matching process
shell
zsh
. i cannot in good conscience recommend this to anyone else; most people will be better served by
fish
. i just have sunk cost from learning entirely too much bash syntax in my misspent youth.
i tried
xonsh
and was annoyed by how poorly python variables interact with regular shell variables.
i was very pleasantly surprised by
powershell
, which it turns out runs on linux these days. it has actual data types instead of just strings, which means you aren't constantly doing string munging in a language not designed for it. i would probably use it interactively if i were willing to give up my sunk cost on bash syntax.
i tried
nushell
, which is like powershell but not made by microsoft and without the .NET integration. i found it extremely verbose - it's a good scripting language but not a good interactive shell. also it breaks a bunch of bash syntax for no reason, even when the syntax is unambiguous. (much of bash's syntax
is
ambiguous and i can forgive breaking that.)
editor
i use
neovim
with a
truly absurd amount of custom configuration
. i cannot in good conscience recommend this to anyone else; most people will be better served by vscode and a few plugins.
i tried various other editors and was disappointed by all of them.
kakoune
required more configuration than i was willing to put in to just to get a "basic" experience.
helix
was extraordinarily resistant to being configured past very basic key remapping (for a while i forked it, but this didn't scale very well for the amount of configuration i wanted). VSCode dropped keystrokes and was generally laggy, both of which got worse when i installed a vim plugin.
zed
had various issues with the integrated terminal and window management (although this may have changed since i tried it in mid-2024). i have not tried
emacs
and dread the day i do because it will probably suck up weeks of my time.
terminal multiplexing
i use
a fork
of tmux with
more absurd amounts of configuration
. again, i cannot in good conscience recommend this to anyone else. most people will be better served by the integrated terminal in vscode (i spent a couple weeks on trying to get back ctrl-click for filepaths alone). vscode also works on windows MSVC, unlike terminal multiplexers.
various people have recommended
zellij
to me. i think zellij is good if you like the default keybinds, or if you use a terminal multiplexer infrequently enough that having the basic commands on-screen is helpful for you. i found that the default keybinds interfered with a bunch of programs and didn't look further into it.
wezterm and kitty are not really in the running because they don't have session save/resume.
debugging
for cmake projects:
cmake -G Ninja
. uses
ninja
instead of
make
, improving compile times and with a much nicer progress bar.
for cmake projects:
cmake -D CMAKE_EXPORT_COMPILE_COMMANDS=On
. Generates a
compile_commands.json
file that most LSPs know how to read.
for everything else:
bear
. like above, but works for arbitrary build systems.
"everything else"
watchexec
: bacon but generalized to arbitrary files and commands. i find this quite useful for a variety of tasks, including minimizing bugs.
btop
: like top but easier to use and easier to understand the output
tailscale
: software-defined networking. i mainly use it for easy NAT punching and DDNS, but it's much more flexible than that.
obsidian
: flexible and pretty markdown editor. i use it for journaling and drafting blog posts.
obsidian sync
is not required but "just works" and makes it much more convenient; it's nice to have access to the same files everywhere.
#:~:text=xyz
: link to specifically the text "xyz" on a web page. works in firefox since around the end of 2024, and in chrome since a lot earlier.
i either use these occasionally enough i need a reference, or haven't used them yet but want to.
debugging
operating systems
popos launcher config
, since i couldn't find docs for it (local copy in
/usr/lib/pop-launcher/plugins/web/config.ron
). this is what runs custom searches when you hit Super-R on PopOS 22.04.
yaft
: linux framebuffer terminal
jc
: structured parsing for unix tools
CUPS debugging
yggrasil-network
: "ipv6 for everyone"
containers
bubblewrap
: flexible adhoc sandboxing
cntr
: overlayfs that works with a running container
development
editing and diffing
ast-grep
. language-aware structured search and replace.
diffoscope
: recursive diffing
fix tabs and spaces:
unexpand -t 4 foo.c | sponge foo.c
graphics
benchmarking
