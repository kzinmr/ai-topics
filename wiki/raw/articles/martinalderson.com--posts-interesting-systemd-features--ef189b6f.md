---
title: "Interesting systemd features you may not know about"
url: "https://martinalderson.com/posts/interesting-systemd-features/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-10-25T10:01:22.490234+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Interesting systemd features you may not know about

Source: https://martinalderson.com/posts/interesting-systemd-features/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I've always thought of systemd as a fairly boring piece of plumbing, that boots your system and runs background services. I also knew there was enormous controversy when it first came out, but I hadn't really dived much into it past this.
Systemd actually has tonnes of interesting features, that I think are
even
more useful for running throwaway agent-written code.
Note this is all Linux only - sorry Mac users, there's no real equivalent of systemd on macOS (launchd covers some of the cron-style stuff, but not the resource limits).
Easy memory/CPU caps per process
You may have experienced this before. You have an agent write a script, perhaps to do some data analysis. It has a terrible memory leak, and suddenly your machine freezes and (hopefully) the kernel resumes after a bit with an OOM error.
I've had this a few times, and it's very annoying. Turns out systemd has an easy way to limit processes and any subprocesses, with
MemoryMax
and
CPUQuota
.   These actually use the same underlying cgroup limits as Docker would.
If you want to for example run Claude Code with 4GB of memory max and only 2 CPU cores to avoid it burning through all your RAM, it's as simple as running this:
systemd-run --user --scope -p MemoryMax=4G -p CPUQuota=200% claude
You can obviously run any command this way. Bonus point, if you use
systemd-cgtop
instead of
top
(or
btop
), you can see memory use and CPU use per cgroup.
PS: systemd does also have sandboxing features (
ProtectHome
,
ReadWritePaths
and friends), which you'd think would be perfect for agents. But there are so many footguns with it that it's too long to explain in this article - I'll maybe do a follow up one day.
Limiting how long a process can run for
Similarly to the above, if you want to limit e.g. an autonomous agent to only run for 30min max, you can just use the
RuntimeMaxSec
argument. For example, if you want to run OpenCode to investigate something but don't want it spending more than 30 minutes, you can simply run:
systemd-run --user --same-dir --unit=opencode-agent \
  -p RuntimeMaxSec=30m \
  ~/.opencode/bin/opencode run --standalone --auto \
  "Fix the failing tests in this repo and summarise what you changed"

# follow it:   journalctl --user -u opencode-agent -f
NB: the
--standalone
arg is required, because OpenCode by default will run its work on a background server which you may already have running, which will bypass the time limit.
Inhibiting sleep
This one is likely more useful for laptops, but if you want to run a process and close your laptop,
systemd-inhibit
is a good way to do that. You can combine with the former one to make sure it expires after a while to avoid draining your battery entirely:
systemd-run --user --same-dir --unit=claude-agent \
  -p RuntimeMaxSec=30m \
  systemd-inhibit --what=sleep:idle:handle-lid-switch --why="claude agent run" \
  ~/.local/bin/claude -p \
  "Fix the failing tests in this repo and summarise what you changed"
Better cron
More obvious, but systemd has a lot of features that a simple cron doesn't. I'd recommend reading the
full man page
for full details, but there are some cool features there. For example, one I use all the time is
Persistent
, so if your computer is off/sleeping, it will run the task when it comes back online. This is really useful if like me you want an agent to summarise something and notify you every week.
Equally, the
OnSuccess
and
OnFailure
arguments are helpful. If you define a slack or email unit, you can easily pipe results of runs. It's also a good place to put 'dead man's handle' calls to the likes of Healthchecks.io.
Another nice one is adding a random delay to your cron jobs, if you have a bunch of machines hitting a service at say 1am. You can have it randomly delay the start a bit with
RandomizedDelaySec
to avoid a huge spike in load.
Path units
This is a really cool one I did not know about until I researched this article. Effectively it fires when something in a folder changes.
# ~/.config/systemd/user/agent-inbox.path
[Path]
DirectoryNotEmpty=%h/agent-inbox

[Install]
WantedBy=default.target
# ~/.config/systemd/user/agent-inbox.service
[Unit]
OnSuccess=slack-notify.service

[Service]
Type=exec
RuntimeMaxSec=30m
MemoryMax=4G
ExecStart=/bin/sh -c YOUR_COMMAND_HERE
So you could use this for watching a folder, and every time it changes, triggering something. If you have a folder of e.g. expenses or invoices, you can just drop files in there and have the agent categorise them for you as new files get added.
Overall, if like me you thought systemd was only really useful for running daemons and not much more, it's definitely worth diving into. Often it provides a lot of the plumbing you need without having to roll your own, especially for the huge amount of almost "disposable" software you tend to end up with these days.
