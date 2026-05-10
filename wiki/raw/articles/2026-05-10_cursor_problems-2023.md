---
title: "Our problems · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/problems-2023"
scraped: "2026-05-10T01:19:52.729805+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Our problems · Cursor

**Source**: [https://cursor.com/blog/problems-2023](https://cursor.com/blog/problems-2023)

Blog
/
research
Oct 12, 2023
·
research
Our problems
Sualeh Asif
·
5 min read
Update: We wrote about
some more problems
.
An unordered list of short, concrete problems:
Better context:
There are a lot of sources of information in a code editor: open files, semantically similar code chunks, symbolically connected classes, lint outputs, execution traces, git history, typing history, external documentation, and more. We want the model to instantly understand what is most relevant to the user’s question, and are currently training a custom and fast reranker model to solve this problem. For each request, we will gather 500k tokens from all different sources, and use our reranker to filter them down to the most relevant 8k tokens. This is both a model problem and, increasingly so, an infrastructure problem.
A “copilot for edits”:
While GitHub Copilot is tremendously helpful for eliminating low-entropy keystrokes while writing new code, it does not help you save low-entropy keystrokes when you need to make small, simple changes to existing code blocks. Think the navigation, deletion and input keystrokes you need to do for a rename that’s just slightly more complicated than a symbolic F2-rename can do. We will need innovation in both UX (unobtrusive diffs that are shown to you while you’re coding) and on the model-side (prompting doesn’t cut it, because of cost, latency, and intelligence problems).
Constrained, in-flow agents:
Think OpenAI’s code interpreter, but for engineering in large codebases. You are telling a constrained, few-step agent what to do, and it searches, writes and runs code for you, all the while every so often consulting you for feedback. The first step to achieve this, which we are working on right now, is to make an agent like this that works on folders of a few hundred thousand tokens. If that is successful, we will scale it up to work for entire codebases.
Bug-finding:
There are two modes here: (1) in the background, Cursor will always be passively scanning your files to find potential bugs for you, and (2) when you are deep in a debugging session, Cursor will actively look for the bug with your help. There’s a lot of interesting data collection to be done here.
Larger edits:
Cursor should be able to modify entire files, and even entire directories, for you. This is a challenge of both capabilities and UX. For speed, the model needs to be smart enough to pick out the parts to modify without rewriting everything. For making the experience good, the changes need to be shown in a parsable, real-time form.
Scale:
We have 1.4 billion vectors and 150 thousand codebases indexed, as of October 12, 2023. This will probably grow by 10x by the end of the year. We have already built a really fast Merkle-tree-based codebase syncing engine in Rust, and will probably need to build a custom indexing system soon.
Future ideas
:
Time warp
: Predict and display the cross-file code changes you’ll make in the next 15 minutes. One key command to accept all insertions/deletions.
Understanding
: Our models should deeply understand all the concepts in any codebase, in the weights.
Reader mode
: Make code understanding effortless with docs at any level of specificity and a bot that guides you through the relevant code paths, explaining as-needed.
Pseudo-code mode
: Edit an “outline” representation of your code and have the changes automatically applied at the source level.
Never worry about stack traces again
: The IDE should just get it, and auto-fix the code for you.
We tried to collect all problems we are thinking about right now, but — and this is one of the wonderful things about building a product that you use yourself for 12 hours per day — we constantly have new ideas and reprioritize, so this should not be seen as a be-all-end-all roadmap. That said, we hope it gives a sense of what we spend our brain cycles on every day.
Also, you read pretty far, so it seems likely that you may have some interest in the problems we are interested in :). If that is so, you should consider joining us! Here are a few other reasons why we think you would love to work with us:
People like using Cursor.
We’ve been quite happy with our initial growth.
You will work with really smart people here.
We deeply believe in talent density. Everyone you work with here will be really really good.
AI coding is a huge market.
And we can win it.
It’s fun.
This matters a lot to us! It’s fun to work with people you like, it’s fun to build a product where you hit Cmd-Shift-R and get instant user feedback because you yourself, while coding, is the target user, and it’s fun to make a little bit of progress every day towards automating away all boring parts of programming.
We work hard.
We feel lucky to work on these problems, and we enjoy pouring our all into solving them.
Filed under:
research
Author
:
Sualeh Asif
