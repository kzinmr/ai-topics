---
title: "Using My Fucking Brain"
url: "https://terriblesoftware.org/2026/05/27/using-my-fucking-brain/"
fetched_at: 2026-05-28T07:00:49.722725+00:00
source: "terriblesoftware.org"
tags: [blog, raw]
---

# Using My Fucking Brain

Source: https://terriblesoftware.org/2026/05/27/using-my-fucking-brain/

I’m angry right now. Not at Dario. Not at Sam. Definitely not at you, reader. I’m angry at myself.
A few days ago, there was a new Sentry issue. I copied the link, pasted it into a Claude Skill I built, and asked Claude to investigate it. Then I asked Claude to create a PR. The PR got reviewed. It got approved. I merged it.
Here is the part that feels gross to write down: I never opened the Sentry issue myself. I never looked at the code Claude wrote. I never checked whether the fix made sense. I did the software engineering equivalent of forwarding an email with
“thoughts?”
and then going to lunch.
After I realized what I had done, I went back and did the investigation myself. I opened Sentry. I read the stack trace. I looked at the relevant code. I traced the bug from symptom to cause to fix.
Same answer as Claude’s. Great, I guess?
If Claude had been wrong, this post would be easier to write. I could talk about hallucinations, tell everyone to be careful, say something serious about production software, and we could all nod along together.
But Claude
was
right. The scary part is that the workflow would have looked exactly the same if it had been wrong.
I mean, I love these tools. I use Claude Code all the time. I write Skills for repetitive work. I ask models to explain code, find bugs, suggest fixes, summarize long threads, draft tedious things. I’m not writing this from outside the AI cave with a torch and a warning sign. I’m very much inside the cave, laptop open, asking a model to do things for me right this very second while I write this.
I wrote before that
AI can write your code, but it can’t do your job
. I still believe that, probably more than before. The job was never about
typing
code. The job is noticing when the reported bug is only a symptom. The job is reading the weird line in the stack trace twice. The job is knowing when a fix is technically correct and still too narrow.
The job is the part where your fucking brain has to be in the room.
There is a way of using AI that feels like getting a second brain. You open the issue, read the error, form a rough theory, and then ask the model to challenge it. You have it search the codebase. You ask what else could explain the symptom. You ask it to write the boring first draft of the fix.
Then
you read the patch, poke at the edges, and decide.
That’s great and might be the dream, honestly. The model makes you sharper, and it helps you keep more of the problem in view. It catches things you missed. It turns a slow loop into a fast one.
Then… there’s the thing I did.
You paste the issue into the machine before reading it. You accept the explanation before forming your own. You create a PR before even understanding what the problem you’re fixing is (!). You request a PR review before reading the diff. You merge because the checks passed and the reviewer approved it and the whole thing smells like progress.
And then, if you’re lucky, a few minutes later your stomach drops. Because wait. What did I just ship again?
And I don’t think I’m special here. I think a lot of us are quietly building workflows where the model sees the issue, the model reads the code, the model writes the patch, and we show up at the end to approve the shape of the answer.
But if we’re not careful, we’re
training ourselves out of the reps
that made us useful in the first place.
And to be clear, I don’t care whether you typed the code yourself. I care whether you understood it before you shipped it. I care whether you can explain why the bug happened, why this fix is the right fix, what the model might have missed, and what would make you roll it back.
So, with all that said, here’s the new hard rule I’m following after this “incident”:
if I still can’t explain the change, I can’t ship it
. No exceptions.
This post is mostly for me. I wish it wasn’t. I wish I could write it from a place of earned superiority, looking down at all the careless engineers vibe-merging AI patches into production while I, a Responsible Adult, carefully inspect every token.
Nope.
I’m still doing this. I still catch myself pasting context into a model before I’ve really looked at it. I still feel the tiny dopamine hit of skipping straight from problem to answer. I still like how clean it feels when ambiguity becomes a PR.
But I don’t want to become a person who ships software by clicking merge on work I don’t understand.
AI should make me think better. It should help me hold more context, see more possibilities, and get unstuck when my brain is tired.
It should never become a comfortable place to hide from the work.
