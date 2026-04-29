---
title: "Could Excel agents unlock $1T in economic value?"
url: "https://martinalderson.com/posts/excel-agents-could-unlock-1T-in-economic-value/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-29T07:02:04.346386+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Could Excel agents unlock $1T in economic value?

Source: https://martinalderson.com/posts/excel-agents-could-unlock-1T-in-economic-value/?utm_source=rss&utm_medium=rss&utm_campaign=feed

It seems the new space that is going to get transformed by agents is Excel. We've had
Shortcut
, then
Agent Mode
from Microsoft, and now
Claude for Excel
. This trend really piqued my attention and got me thinking of the economic impact of these agents. I think it's going to be absolutely enormous.
NB. When I refer to Excel here, I also include Google Sheets or other spreadsheets.
(Most?) software engineers underestimate the scale of Excel
Reading the Hacker News comments on the Claude for Excel launch puzzled me as most commentors did not seem to understand the scale of Excel usage out there. There are
billion
dollar processes in finance that are ran through a shared Excel file on a mounted network drive.
To me, Excel is where the majority of actual "software" exists. Virtually every company - of any size - will have
so many
critical business processes being ran and managed in Excel. For every "properly" designed and developed web app or other customer software, there will be dozens of Excel sheets hidden away.
The quality of these Excel "systems" vary, but is generally somewhere between appalling and mediocre. There is no source control management like Git, instead you've got FINAL v2 FIXED FINAL.xlsx. No unit/integration testing, and you're doing well if you have good quality input data validation.
As such, agents can have in my opinion an outsized impact on this market. Hopefully most of us now agree agents for software dev are useful, and a few months I posted a blog about how even Claude Code could have
amazing results for non-code tasks
. Seeing these new agents work within Excel is really interesting as it gets rid of the requirement for non technical people to understand terminal based apps.
Why this is such a big deal
While you've been able to input Excel files into ChatGPT/Claude/Gemini for some time, the workflow ends up being very similar to my pre-agent workflow for software engineering - a lot of copying and pasting and while helpful, slow and error prone.
The agent workflow make this far, far better. Instead of having to read the entire xlsx file, it can instead just read the parts it needs - which makes it far faster and stops you running out of context window in a few turns.
Most importantly, it's working against a real Excel instance, not naively editing the Excel file and hoping for the best. This means it can iteratively work and debug itself, allowing it to work on far more complex sheets.
If there is the equivalent of AGENTS.md, users can explain what a certain Excel file (or folder of files) do and how they relate to each other. This means it doesn't need to spend the first few minutes of the session getting up to speed. I think this will be even more powerful than in pure software development, as most code is actually quite readable even without comments to LLMs. Excel files are not the same.
Finally, they can also use scripting and bash commands to work things out "out of band" and verify results - and (very soon) transform that back to VBA or similar to Excel sheets. This will enable far more concise Excel sheets, as most users don't get into VBA and it is far more efficient for many tasks. Combine this with subagents that can go and do research on live data APIs and it is going to get extremely powerful for non-technical users.
$1T? Really?
I was in two minds to include this somewhat clickbaity number, but to be honest it could be
conservative
.
While the data is a bit messy, some research I found shows that
38% of knowledge workers time
is spent in Excel.
According to the
Bureau of Labor Statistics
, there are approximately 70.9 million workers in management, professional, and related occupations in the United States. Applying the 38% number to this workforce gives  the equivalent of 27 million full-time employees doing nothing but Excel work.
In the same report, the BLS also reports that professional and business services workers earn an average of $44.57 per hour, which translates to approximately $92,700 annually for full-time work. Using a conservative estimate of $90,000 average salary for knowledge workers, we're looking at roughly $2.4 trillion in annual labour costs devoted to spreadsheet work across the US economy.
To give a concrete example - imagine a small manufacturer transposing data from a customs website to their own Excel sheet. This may involve downloading a CSV of customs data, and then painstakingly copying and pasting each row into a 'master' Excel sheet for cost tracking. This can take
days
of hard work (and is error prone). Agents could read the CSV file, use a python script to transpose and insert it into the Excel sheet, and run a bunch of verifications in the time it takes to make a coffee.
Importantly, the user doesn't need to know about Python (or even what Python is) - much like how Claude Code impresses with complex chained bash commands that I'd never think to write myself.
Therefore, even a 50% improvement in productivity unlocked by Excel agents has enormous impact - across the whole economy I suspect there is at least $1T of labour time 'wasted' in Excel - fixing formulae, copying and pasting data, getting insights out of the data, etc. These tasks are all very doable with the
current
state of LLMs, and will only get better from here.
What this means
As these general agents start working in a way less technical users can really leverage the power of them, I think it's fair to say there is enormous potential for huge productivity increases that will really transform the economy.
This is also going to mean big changes in employment too. Quite how that works out is difficult to know, but there are definitely going to be winners and losers as this technology sweeps through industry.
If you found this interesting, you might also enjoy:
