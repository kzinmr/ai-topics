---
title: "Claude Code "Don't Ask Again" exposes secrets in 1,122 public GitHub files (Apiiro)"
type: article
created: 2026-11-08
updated: 2026-11-08
source: https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again
published: 2026-11-07
tags: [claude-code, secrets-exfiltration, coding-agents, security]
sha256: 3762ebf557655496de3b1a4c196045d6b8945427023a4dbcd851fbfd7bc9828d
---



## HN discussion highlights (item 50407882, 434pts)

[qezz] > Is it public? > > Search your GitHub organization for .claude/settings.local.json and .claude/settings.json. Each hit is a file anyone can read right now. So, it's not necessarily "public", it's simply in the repository, and whether it's actually public or not depends on the repository settings. Or am I missing something

[shmulc] Thanks, fair point. Our 1,122 files are all in public repos. In a private repo, only people with access can read it, but "don't ask again" still writes the password into a project file that gets committed, so it spreads with every clone and fork, and goes public if the repo does.

[mschuster91] > So, it's not necessarily "public", it's simply in the repository, and whether it's actually public or not depends on the repository settings. Even then, you might not want every developer in your company to have the password to the production SQL database...

[Aurornis] Confusing headline. They scanned for repos where people had committed their .claude/ folder and local settings and then scanned those files for commands which contained keys or passwords. So pressing “Don’t Ask Again” by itself doesn’t expose passwords by itself. If you commit your local Claude settings and in those settings you have manually approved commands containing secrets directly in the command and then you publish the repo, that’s exposed.

[shmulc] That's the chain, yes. The part people don't expect: the file is created inside the project, and Claude Code only adds it to your global git ignore, not the repo's .gitignore. So a fresh clone or a second machine commits it like any other file. In 539 of the 1,105 repos we traced, a commit co-authored by Claude itself changed the file.

[lacoolj] This page is like 80% repeating itself If you post output from AI, please remember to edit before publishing

[nicce] If the thing is not worth writing by yourself, then it is probably not worth of reading by any humans.

[rvz] Vibe coders in open source proudly don't read the (slop)code and place all their agents in autonomous loops without them knowing that Claude leaked their passwords and environment variables on GitHub. This incident would have been caught in an open source harness. This one is closed source malware, and you don't know what Claude Code does internally to behave like this. Yet another reason why you cannot trust a closed harness.

[happyopossum] That’s ridiculously overblown rhetoric. Claude Code didn’t publish these secrets, the users did by committing their Claude Code settings to public repos. Same thing could/would happen with an open source harness.

[skeledrew] Devs have been leaking secrets in public repos a long time before now. Nothing new here, except there are now more with dev power, which statistically means more leakage.

[jedisct1] If you really need to commit private files to GitHub, use Turbocrypt https://github.com/jedisct1/turbocrypt/blob/main/docs/git.md

[bcherny] Boris from the Claude Code team here. Historically Claude Code has not done secret scrubbing (there are many good tools for that), but we are looking into what we can do to prevent this. That said, a few thoughts: 1. .claude/settings.local.json is meant to stay local. This is not a file you should check into source control. We automatically gitignore it when Claude creates the file, so in this case the files were manually created and checked in (docs: https://code.claude.com/docs/en/settings ) 2

[agentdev001] I appreciate you getting communication out in front of this fast. > "but we are looking into what we can do to prevent this" I would presume that CC's auto-review of tool-call turns would already solve this >99% of the time, no? From my read, any harness-side deterministic solution here would be saving the user from themselves, which seems like a bad pattern. Somewhat dulling the scalpel in my mind.

[markasoftware] Auto mode cannot be considered safer than anything because it does not even attempt to guarantee any sort of security. The threat model is not even defined. It cannot be quantified or compared with any other approach other than "full access"
