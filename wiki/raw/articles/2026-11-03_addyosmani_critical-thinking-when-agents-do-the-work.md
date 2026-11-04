---
title: "Critical thinking when agents do the work"
source: "X Article (Addy Osmani)"
author: "Addy Osmani"
date: 2026-11-03
scraped: 2026-11-04
url: "https://x.com/addyosmani/status/2117512471930167377"
type: x-article
tags: [cognitive-surrender, ai-assistance, coding-agents, software-engineering, comprehension-debt, verification]
engagement: "16,984 bookmarks / 1.1M impressions / 7,546 likes (as of 2026-11-04)"
---

# Critical thinking when agents do the work

*By Addy Osmani (@addyosmani), Claude Code @anthropicai. Published 2026-11-03 as an X Article.*

> Note: Retrieved via X API `tweet.fields=article` (plain_text). Invisible unicode stripped.

Back in the day, critical thinking was taught as approaching new info with humble curiosity and a healthy dose of skepticism - take in different views, form your own opinion. Still true, but increasingly, nothing in my day-to-day forces critical thinking on me now that so much of my work runs through agents. For the engineers and product people who have fully bought into agentic workflows (running multiple sessions in parallel and expecting the models to improve), I'm here to say: I'm a big fan of these tools. I'm not writing this to advocate for less agentic workflows.

My goal is to help you maintain critical thinking in a world where it's easy to offload anything to an agent.

In the past, most of our cognitive and aesthetic processing happened in the space between question and answer. That space is now measured in seconds. The more you use agentic workflows, the more difficult it becomes (though not in the way I think people expected): as the models improve, the percentage of obvious errors is lower. Many (most?) outputs will be well-written and mostly correct, but they won't demand a second look.

Even if you are running many agents at a time, you still only have one pair of eyes on the outputs.

You have to build critical thinking into your day, because by default nothing will do it for you.

Part of the reason it's hard to self-correct for this is that agentic workflows are pleasant. Getting fast, pleasant, often-correct answers is refreshing in a busy day, but that's also why it's easy to relax your vigilance.

## Offloading, deferral and surrender

When discussing this with people, I describe it as a spectrum:

At the top: cognitive offloading, the act of delegating tasks to the AI, but maintaining ownership of the result. I do this all day. You should, too. In the middle: deferral, where the output of the tool becomes your new input; the result has ceased to be a hypothesis. At the bottom: cognitive surrender - the AI's output quietly becomes your own, you feel no need to check it.

Cognitive surrender is a term coined by Steven Shaw and Gideon Nave at Wharton. It fits neatly what I've been seeing: as trust (or laziness) increases, people drift down the spectrum. The transition is rarely observed, because the steps are each gradual and seem reasonable. You read the last answer well, so you skim the next one. You just scan the skeleton of the one after that. Then you get asked about a line and can't explain it, even with your agent's help.

That's cognitive surrender. It's how cognitive debt accumulates. It's usually discovered when you try to apply a mental model of the system and it doesn't exist. Margaret-Anne Storey has written about how this shows up in teams as an eroding understanding of a shared system theory. I've written about the code equivalent, comprehension debt (a term coined by Jeremy Twei). In the moment, it's completely invisible. The codebase looks pristine and the tests pass. It doesn't become obvious until you have to make a change to the system and realize that nobody understands it anymore. The same applies when you've read the table of contents of a strategy doc or spec and signed off on it.

To be clear, I'm not advocating for the impossible. It's impossible to maintain the full mental model of a large modern codebase. The Claude Code team has said publicly that they rebuild understanding on demand: when they need to understand a part, they ask Claude to explain that slice, rather than holding the full model in their heads. As I've written about before, this sort of debt is more recoverable than most engineers expect. You don't need to maintain the full model as long as you can rebuild it locally as needed. You just need to know what you don't have.

Where the stakes are low, feel free to delegate entirely. When you can't explain the answer to a question, even by way of your agent, you've ceded ownership.

This isn't always a problem, either. Just recently, I was recording a course and had to select one out of three similarly-rated hotels to use as a recording location. I didn't have time to manually review all the reviews, so I delegated the decision to an AI. It worked, and I'd do the same thing again. However, I wouldn't do that when deciding how to invest our money, how to advise our kids on their careers, or at work: what we should build, what changes affect what users, whether it's safe to ship. Take the handoff where being wrong is cheap, keep the reasoning where others will have to deal with the consequences.

## The questions I ask myself

When I didn't know what I thought, I'd usually go back to a basic list of questions like these: How do I know that I'm working on the right problem? How do I know that I'm solving it the right way? Is there evidence that supports my conclusion? How do I know that I'm finished? Most times, this is just who, what, where, why, when and how. When written out, it looks absurdly child-like, but it forces you to think in terms of categories that you'd otherwise ignore. These days, it's too easy to simply skip all of this and ask your agent what it thinks you should do. These are the new versions of these questions that I ask myself now.

Did I formulate a hypothesis before asking? Before I run an agent on any non-trivial task, I write down, even just in my head, what I think the answer might be. It's OK if it's a bad guess. You're always welcome to change your mind in light of new information. Once you've read a well-written response, though, it's hard to imagine any other possibility. If you have no guidance whatsoever, ask for what Thariq Shihipar calls a blind spot pass: give the model what you know and have it find your unknown unknowns.

Am I asking it to help me think or to offload thinking from me? Both are OK, as long as you know which one you're doing.

What would have to be true for this to be wrong? Then go find out. A model's self-assessment of confidence is much less valuable than an actual test you can perform, so give it one.

Have I heard the counter argument from a different angle? When I've taken a hard stance on something that's somewhat open-ended, I'll ask more than one model to argue the opposite side, then review the output and form my own opinion. This takes longer, but I end up knowing much more about the subject.

Would I bet on this in front of the person who has to maintain it? This applies to code and to anything else that you're delivering. I believe that this is the bar for answerability.

What am I no longer practicing? Maybe it's some of the routine debugging. I'm OK with letting some of that go, but I want it to be intentional.

## Verification as a habit

I've been writing a lot about verification lately because I believe that the bottleneck has shifted from coding to being sure you're right. When you give an agent the means to verify what it's doing, whether that be by way of end-to-end tests, property tests, or by way of actual app interactions, it can make a change, run the verification test, read the output, and attempt again all before you've looked at anything. This is what Boris Cherny calls "give Claude a way to verify its work" and I believe that this is one of the most critical components of achieving great results. Rather than reading every line, you'll be building these loops and reviewing the evidence.

You can also surrender verification. "Is there evidence that supports my conclusion?" becomes "Did the check turn green?" Agents make it so cheap to create tests that you'll see a lot of green, and you could have a passing test that doesn't catch a broken feature. If the test is written with the same mistake as the feature, it'll pass. And a green check only conveys one property. It's too easy to imagine it covers everything.

When a check goes green, ask what it proved. Then ask what it didn't.

Define "verified" upfront, because post-facto, you'll rationalize any outcome.

The finish line for agent work should be something tangible: a test passing, a screenshot, a log or trace. This ensures that the criteria for finishing the work is factual, and not up for interpretation (and surrender) based on something like "it looks like it's done." When you receive a finish notification from an agent, before you look at the summary, first review the code snippet of the command executed and its output.

Claude Code can also self-critique (via a subagent in a fresh context) its own work as a sanity check, and it's worth baking that into the loop so it runs every time, not just when you remember. I still ask at the end "Did I miss anything?" That sounds silly, but so often, when I finish some complex feature work using a frontier model, look at it, review it, and then ask, "Did I miss anything?" It will then come back with two or three more things. That's why I always ask.

None of this needs to be the norm, of course; knowing when to go deep is a skill. My favorite rule of thumb from our write-up on how the Claude Code team does code review is: "If you can't say what the checks would miss, ask for a real review rather than a quick approval."

This applies beyond code as well. If an agent has synthesized fifty customer calls for you, or a competitive analysis, check a couple of the source documents to make sure the summary is accurate. Check a number that your recommendation depends on to make sure it's being calculated correctly.

Agents have made verification cheap to set up. What's difficult for you is knowing what good verification looks like.

## Actually paying attention to what's generated

Say an agent gives you a 600-line PR. You roughly look at the structure. You don't read every line. The variable names look reasonable and the tests pass, so you approve it. But somewhere in the middle there's a subtle ordering change in a transaction boundary, or a flipped default on an edge case you never thought about. You did review it, I guess, but only for what you already knew you'd find.

Writing code and reviewing it are different skills, and there's a point where reviewing turns into rubber stamping. So read the diff as if the AI didn't write it, and then look past the diff at what the agent decided. Over a long session it makes a lot of small decisions for you: the defaults, what's out of scope, which requirement it reinterprets when two of them clash.

You won't see any of that in a summary that says everything went well, so ask it to list the decisions and assumptions it made. Then quiz yourself. Pick a few lines at random and ask, what about this line? What about that one? For a document, close it and try to write out the main argument from memory. Some have a habit I like for long sessions: have Claude write a report on the change, and then give you a quiz at the bottom, where the rule is "I only merge after I pass the quiz perfectly."

Understand what you're shipping well enough to defend it. Because at some point, someone could ask.

Agents can also guard your attention. For example, I have an open source project that receives a lot of pull requests. I'll use agents to help determine what's incoming, what's contrary to our guidelines, and where my attention is likely required. I rarely let the agents self-determine this, but they can narrow it down to where I should focus my attention, and then I can actually think about whether these changes are solving the right problem in the right way.

Then there's volume, and you have to be honest with yourself about it. I've called this the orchestration tax. It's the gap between what your agents generate and what you'd feel comfortable putting your name on. If finished work is piling up faster than you can get through it, another session won't help until you've fixed that: tighten the checks so less of it needs you, or slow down.

When you're producing more than you can stand behind, you're no longer reviewing. You're hoping.

## Quality in, quality out

The human mental model is still involved, but instead of in the middle, it's at the front and end. You're putting your energy into the front-end of the task description and context, as well as the back-end of reviewing the output. This is why good input is so important to the quality of output, and I view good prompting as a critical thinking skill.

Historically, if you made a non-specific request, someone would challenge it, and you might realize, "Oh wait, I actually didn't figure this out." An agent often won't stop you there. It fills in what you left out and hands back something that looks done, even though the idea behind it is still fuzzy. I've written about this as intent debt, the implicit goals, constraints and rationale that may exist in artifacts you didn't write. Unlike other kinds of debt, nobody else can fix this one for you. The intent has to come from you.

Your prompt is a reflection of your understanding of the problem, and if you can't express it clearly, it may not be clear in your own mind.

Write your own request brief in your own words before you ask for help. Describe the audience, out-of-scope items, and the definition of done. When your second round of corrections hasn't got you there, stop tweaking and rewrite your prompt.

You can have the agent help you with this too. I like the distinction Andy Clark makes between delegating to an AI system and collaborating with it. In the latter case, you're in a virtuous cycle of mutual amplification: your prompts sharpen your output, sharpen your next prompt and sharpen your mental model of the problem. If it's not clear, ask the agent to interview you about what it doesn't understand. If it's not clear, ask the agent to interview you about what it doesn't understand. If you close the session having refined your own mental model, that's a sign of success.

Also be careful about the input. It's easy for each agent to just pass the previous agent's summary into its context, and before long the third agent hasn't read the original document.

You also need your own standards for output. I've played around with AI in lots of different creative mediums, and most of it never gets shown because it doesn't meet my standards. Things are all coming out nicely formatted and confident, so polish is no longer a useful signal.

AI may have made it faster to produce, but if I wouldn't feel comfortable attributing the output to myself, I won't output it.

When something doesn't meet your standards, note why in shared config, a hook or a test so that it doesn't happen again. That's how taste compounds, and noting why something didn't make the cut is good practice on its own.

## "But the models will be better at this than me"

If you're as bullish on the future of this space as many people around me are, you've probably had this thought for a couple of sections. In a year or two, the model will be able to detect what I'd be able to detect, so why bother maintaining the skill?

You may be right on a lot of that detection, and I've been arguing for increasingly pushing detection to agents myself. But here's why I think it still matters: at the end of the day, someone is responsible for what ships. Regardless of how much AI helped, a human has to take responsibility.

The question of how much to trust an agent for any given task is itself a judgment call. Part of staying calibrated is reviewing the work, because what the models get wrong keeps changing. Anthropic's own research on its engineers and researchers calls out the trap as the paradox of supervision: "supervising Claude requires the very coding skills that may atrophy from AI overuse."

These are some of the things that matter most to me and that a better model won't solve: what are you building, why is it worth it, who does it impact and what are you willing to sacrifice? Those are all questions you need to answer. An agent can be helpful in working them through, and I would like it to be, but ultimately they're still yours.

You may offload the work and much of the auditing, but not the accountability.

## Practices for the everyday

You don't need to do all this rigorously. Just plug in what works for your workflow.

Once a week, write a bit of code without an agent, or do one real thing that would suck if you forgot how to do it. (I've called this a calibration exercise, but I don't mean it as a moral one.) Once a month, write down what you've stopped doing and decide which of those you're okay not doing. One question from an old blog post of mine remains as valid as ever: How lost would you be if AI didn't exist?

If something is above your comprehension, go learn it. If I'm writing and I run into a phrase I haven't seen before, I could Google a one-line explanation and include it. I prefer to do a little research to properly understand it, so I can see where it fits.

Checking the machine properly is real work, and pretending otherwise is how teams end up not doing it. It isn't free, so schedule it as a line item and you'll actually get it done.

Skills that you stop exercising are going to go away, and probably faster than you might guess. Keep doing the ones you're not willing to let go.

## What to bring with you

Be intentional. An agent can quiz you, interview you and show you its evidence, but only if you set that up. So set that up.

Be honest about your place on the spectrum. If you can't explain the answer, even with an agent's help, you've surrendered it.

Have a hypothesis. Formulate one before asking, even if it's bad.

A green check means one thing. What did it check? What did it not check?

Look for evidence. Read what it ran and what it returned before reading the summary.

Read to know what decisions it made. What did it decide for you?

Craft your prompt. How you write what you prompt shows how much you understood the problem.

Set a bar, and stick to it. If you wouldn't put your name on it, it doesn't go out.

Keep yourself in the game by manually applying the skills that matter. One thing you could do: Before you ask, write down what you think will happen, and after the agent is done, write down one thing it didn't check. Let me know if that changes the way you read the output. Think independently. Ask better questions. Take responsibility for the outcome.
