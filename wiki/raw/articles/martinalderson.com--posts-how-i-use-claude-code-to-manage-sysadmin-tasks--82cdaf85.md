---
title: "How I use Claude Code to manage sysadmin tasks"
url: "https://martinalderson.com/posts/how-i-use-claude-code-to-manage-sysadmin-tasks/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-05-01T07:02:07.164323+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# How I use Claude Code to manage sysadmin tasks

Source: https://martinalderson.com/posts/how-i-use-claude-code-to-manage-sysadmin-tasks/?utm_source=rss&utm_medium=rss&utm_campaign=feed

If like me you're heavily bought into the benefits of
blazing fast, affordable, bare metal servers
I've found Claude Code makes a superb assistant for helping managing the maintenance of them. This pattern does, however, work just as well for cloud-first deployments (see the section towards the end).
I've built this pattern organically over the past few months, and I've found it has worked great for small teams. This is obviously not designed for larger teams with a SRE function and compliance requirements.
Infrastructure as markdown
The key to getting this working well, in my experience, is organising the 'tasksets' you might want to do in individual folders with CLAUDE.md files. I commit each of these separately to Git to version them and share them with others. If you're working on a new type of process or task, you can easily branch off main and PR them back.
The folder structure I came up with looks something like this:
agentic-sysadmin/
├── projectname-app-maintenance/ (git repo)
│   └── CLAUDE.md
└── projectname-dba/ (git repo)
    ├── CLAUDE.md
    └── benchmark-queries.md
For each project I'm working on I set up a folder for groups of tasks and git repo. In this simplistic example I've got two different git repos - one for general maintenance tasks, and one for DBA style tasks.
The core of it is a CLAUDE.md file, but I also include helpful outputs - for example, for the DBA repo I include a set of common queries the application does so if we're working on improving query performance it can just grab them. The CLAUDE.md has hints to the other files and an explanation of what to use them for. This "progressive disclosure" pattern means you can be context efficient.
I'll come to more concrete examples of tasks and what's in the CLAUDE.md, but at a minimum I include:
General Information about the server(s) - how to connect, hardware specs, OS info, inventory of packages/docker containers installed
General context about what the project does
Hint of where the source code for the project lives on your filesystem
Common tasks and playbooks, known issues/workarounds
You can of course get Claude Code to start building this out for you - once you have secure access setup, you can carefully get it to start doing an inventory of the server for you.
SSH Keys and Security Setup
To improve security, it's important to setup SSH key access to your server and then tunnel all commands over that - basic security applies. This also avoids this folder having any credentials in it whatsoever. It's just documentation.
I've also setup
~/.ssh/config
with aliases so it doesn't even need to know IP addresses and usernames. You just put something similar to this in your config file, and then reference the server "Use ssh appserver1-lon-uk to connect" in your CLAUDE.md file:
Host appserver1-lon-uk
        HostName 10.10.10.10
        User appuser
        ProxyJump bastion-host
For additional security you can use a bastion and use the ProxyJump command to proxy all commands through that. This works great in my experience and Claude doesn't even need to know about it!
I can't emphasise this enough - you want
zero
sensitive information in these repos. Don't overlook security setup you'd do normally.
A concrete example
I've been working a lot with Clickhouse recently. As we were building the infrastructure out I wanted to setup a solid backup system. I started by doing the normal research I'd normally do, and it seemed like
clickhouse-backup
was the best supported approach to do this.
I first start with the plan command in Claude Code to come up with a detailed plan, pasting in all the documentation on clickhouse-backup . I then did plenty of research on each part of the plan - the idea is to do the absolute opposite of 'vibe coding' here. Meticulously research each step it is suggesting, push back on what isn't clear and make sure you don't leave anything to chance.
It should feel like you are "pairing" with the agent - asking it to check before doing anything, getting it to come up with verification steps
before
running anything and being willing to take over to do certain things yourself if you feel happier with that psychologically. You want to be reading every ssh command it issues like you wrote it yourself.
In about an hour I'd managed to get
clickhouse-backup
(something I'd not used before) setup with encryption, backing up to s3 compatible storage and done a test recovery locally with verification against the real database. I also set up a dead man's switch if a backup doesn't occur to alert me (with a webhook to https://healthchecks.io/).
CLAUDE.md as Project Memory
Where this comes into its own is it becomes self documenting. There is no doubt I could have set the backup example up myself. However, now you can ask Claude to update the CLAUDE.md with what you did, verification steps and any 'gotchas' that came up. Doing this myself would take far longer than the task itself.
Once you do this, you'll have a new section in your CLAUDE.md, with something like this (but much more detailed):
- Backups
    - Backups are handled with clickhouse-backup, and run every x hours
    - They are backed up to S3
    - To verify the backups have worked correctly, run `command` and assert `timestamp` is within the right amount of time
    - To restore backups, do...
    - Known issues: the s3-compatible storage we are using requires `x` version of the S3 protocol. Using an older version will result in `S3Version` errors.
This now makes it trivial to ask the agent in future to verify backup status, restore backups, etc. For me this has been a gamechanger with less-familiar tech that I don't have the common commands seared into my memory - and you can easily share this with teammates.
This is not a static document. Each section can be updated as you do things. For example, if you find out in a few months that backup restores take too long and you need to use a multithreaded approach, document that in CLAUDE.md. It should be a combination of a playbook and an incident log. This hugely helps the agent to not go round in circles on things you've already done - just like you'd document for a new engineer (but probably don't get round to it every time).
Cloud-first
This also works extremely well if you give it access instead of SSH but to the gcloud/azure/aws CLI, with access management setup correctly. The same approach applies - but instead of issuing SSH commands you are issuing $HYPERSCALER CLI commands.
Conclusions
I've found this scales surprisingly well for small teams. One question you may ask is why not just put this in the development repo (which is where I started)?
I've found when you start putting a lot of sysadmin info into your code repos CLAUDE.md it starts becoming the worst of both worlds - often trying to connect to production servers to debug something it doesn't need to, and equally looking far too much at code for things that are really quick infrastructure tweaks. Plus if you have multiple repos for your code, it's hard for it to have an overarching view of all the infrastructure involved.
The key is the documentation that is trivially added compounds in value. You end up with it remembering niche issues you resolved months ago that you forgot that caused strange side effects - hugely reducing time to resolution.
The psychological shift isn't always about saving time on the task itself. Instead, I find it's much more about documenting everything. If you are in a rush, it's very difficult to always take detailed notes of every command you ran and each thought you had.
Once you get into the habit of updating CLAUDE.md after every 'session' it also provides an interesting reflection of where your thought process went. I've definitely felt like I'm learning to be a better engineer seeing where I thought the issue was and what it ended up being in a summary diff.
Finally - this is also just as useful for humans. You can easily read and explore the CLAUDE.md and even get it to turn it into a nicely presented HTML file in a couple of minutes. Once it starts getting longer than a few pages, you just ask it to summarize certain areas. If you launch claude in the folder above your project folders, you can even ask it to do something like 'what version of Linux kernel are we on across every server' and get a report back in a couple of minutes.
