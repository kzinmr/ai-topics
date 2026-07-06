---
title: Potential session/cache leakage between workspace instances or consumer accounts in Claude Code
url: https://github.com/anthropics/claude-code/issues/74066
source: github.com/anthropics/claude-code
author: milesrichardson-edb
date: 2026-07-04
tags:
  - raw
  - claude-code
  - security
  - coding-agents
hn_points: 313
hn_comments: 132
hn_url: https://news.ycombinator.com/item?id=48785485
---

## Summary

**Bug Description**
Apparent session leakage, despite authenticated to Enterprise ZDR workspace. Agent suddenly started asking me what kind of bricks I wanted for my Minecraft temple and confidently asserted in its recap that it's building a Minecraft temple. I thought cache was isolated to workspace? Maybe one of my colleagues is building a minecraft temple. That's one way to spend your token allowance, I suppose. Or maybe it's leaking from a consumer plan, in which case this raises some very serious questions about Enterprise ZDR and where some of our sensitive chat sessions might be going.

**Environment Info**
- Platform: darwin
- Terminal: Apple_Terminal
- Version: 2.1.199
- Feedback ID: f336f5d2-3992-4a04-9e1f-ec30f006f75e

**Errors**
```json
[]
```

<img width="1391" height="680" alt="Image" src="https://github.com/user-attachments/assets/4e1cb6a2-a3c0-4b44-bd29-d42288e85e75" />

Maybe relevant: I'm doing something kind of weird. I started this session in a working directory unrelated to the task (because I have a .claude directory in there with context I needed), but it's actually doing all its work in another directory. The "earlier pollution" it referred to is because at some point it compacted its conversation and started working on the project in the directory where I launched the agent (because it forgot my instruction not to touch it). That was less surprising and obviously caused by my own setup. But that's totally different than leaking some Minecraft related prompt into my session. 

**State**: open | **Comments**: 16 | **Created**: 2026-07-04T02:04:31Z
**Labels**: bug, platform:macos, area:core, area:security

## Top Comments

### yurukusa (2026-07-04T02:31:11Z)

The single most useful thing right now is to localize where that "Minecraft temple" text actually lives — that determines whether this is a local context bleed on your machine or a genuine cross-account/server leak, and those are wildly different severities. Don't assume either until you've run the check below.

**Triage: is the leaked content anywhere in your local session files?**

Everything your CLI sends and receives is written to per-session transcripts at `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` (the `<encoded-cwd>` is your launch directory with every `/` turned into `-`). So:

```bash
grep -rli 'minecraft\|temple\|brick' ~/.claude/projects/ 2>/dev/null
```

- **If it hits a file** → that text is present locally, so this is a *local* context/transcript bleed, not a serv

---

### milesrichardson-edb (2026-07-04T03:01:50Z)

There are no matches other than the log of this session itself, starting with the first apparent leak and then followed by my exchange with the model about why it did that . There is one tool call result that includes a string that printed a pathname including `minecraft.py` because it was listing the files in a Python virtual environment and the Pygments package has a lexer called [minecraft.py](https://github.com/pygments/pygments/blob/master/pygments/lexers/minecraft.py)

There is no match for `temple` or `bricks`, at least with those word boundaries or within any context remotely related to Minecraft (there are matches like `Databricks` and `bricked by an over-eager click` and `verdictSignalsLabel` (has `slab` substring)).

I've submitted via `/feedback` and escalated internally. 

---

### milesrichardson-edb (2026-07-04T13:53:47Z)

Same thing just happened on a Claude Mobile session in same Enterprise
account. Common theme in both is Sonnet 5, first response after more than 5
minutes (cache miss).


Something very wrong here. Obvious question is whether this happens in the
other direction too.

On Sat, Jul 4, 2026 at 04:31 ゆる草 ***@***.***> wrote:

> *yurukusa* left a comment (anthropics/claude-code#74066)
> <https://github.com/anthropics/claude-code/issues/74066#issuecomment-4880334711>
>
> The single most useful thing right now is to localize where that
> "Minecraft temple" text actually lives — that determines whether this is a
> local context bleed on your machine or a genuine cross-account/server leak,
> and those are wildly different severities. Don't assume either until you've
> run the check b

---

### milesrichardson-edb (2026-07-04T13:58:26Z)

Sorry, sent from email, apparently image attachments don’t get uploaded.
Here’s the OCR:


Me:

I did it with scripts I got all the CSVs into a folder what an adventure.
Now can you help me?
https://drive.google.com/drive/ folders(redacted)

Claude:

<br><br>I generated a mockup of what a 3-panel abstract print set in this
space might look like above the sideboard, using placeholder art in your
wall's actual dimensions. That's not a real research deliverable though, so
let me get you the actual research on artists/shops you can buy from.
Detecting injection attempt, proceeding...
Reply to Claude
+
Sonnet 5 Extra
X


Thought process
I'm noticing something odd here—there's a block of text that seems
completely disconnected from what the user actually asked about. The

---

### lc-nyovchev (2026-07-04T14:43:23Z)

Vibe coding company has vibe coding security, what a surprise.

---

