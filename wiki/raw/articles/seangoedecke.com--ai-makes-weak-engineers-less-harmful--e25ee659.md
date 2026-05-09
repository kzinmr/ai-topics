---
title: "AI makes weak engineers less harmful"
url: "https://seangoedecke.com/ai-makes-weak-engineers-less-harmful/"
fetched_at: 2026-05-09T07:01:08.674708+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# AI makes weak engineers less harmful

Source: https://seangoedecke.com/ai-makes-weak-engineers-less-harmful/

Like other kinds of puzzle-solving, software engineering ability is strongly heavy-tailed. The strongest engineers produce way more useful output than the average, and the weakest engineers often are actively net-negative: instead of moving projects along, they create problems that their colleagues have to spend time solving. That’s why many tech companies try to
build
a small, ludicrously well-paid team instead of a large team of more average engineers, and why so far this seems to be a winning strategy.
Being effective in a large tech company is often about managing this phenomenon: trying to arrange things so that the most competent people land on projects you want to succeed, and the least competent are shunted out of the way
. For instance, if you’re technical lead on a project, you more or less have to ensure
that the most critical pieces are in the hands of people who won’t screw them up (whether by directly assigning the work, or by making sure someone can “sit on the shoulder” of the engineer who you’re worried about).
Claude Code changed this. Frontier LLMs don’t have the taste or the system familiarity of a strong engineer, but they have absolutely raised the floor for weak engineers. Instead of getting a pull request that could never possibly work or would cause immediate problems, the worst you’ll now see is a standard LLM pull request: wrong in some ways, baffling in others, but at least functional on the line-by-line level and not so obviously incorrect that someone with no knowledge of the codebase could point it out. That is a huge improvement!
You can try this out yourself. If you attempt to deliberately make mistakes while working with a coding agent, you’ll find that the agent pushes back hard against many obvious errors (i.e. caching user data with a non-user-specific key, writing an infinite loop that might never terminate, or leaking open files). Of course, the agent will still miss subtle errors, particularly ones that require understanding other parts of the codebase.
Working with the least effective engineers is now sometimes like working with a Claude Opus or Codex instance that you communicate with over Slack. Occasionally it’s
literally
that: your colleague is simply pasting your messages into Claude Code and pasting you the response. This is annoying, but it’s a much better experience than working with this kind of engineer directly. After all, you probably already work with a bunch of LLM instances. The Slack interface is not ideal - unlike using Claude Code directly, you sometimes wait hours or days for a response, and you don’t get visibility into the agent’s thought processes - but it’s still helpful on the margin. More compute being thrown at your problem is better than less.
Of course, this isn’t a great state of affairs for the engineer in question, who is almost certainly learning less than if they were making their own (bad) decisions. It’s also a bad state of affairs for the company, who is paying a human salary and getting a Copilot subscription (which they’re likely also paying for)
. After the current push to figure out what value AI is adding to engineers, I suspect there will be a push to figure out what value
engineers are adding to AI
, and the engineers who aren’t adding much may find themselves out of a job.
You can’t talk to Claude-over-Slack like you’d talk to normal Claude. If you tend to handle LLMs roughly (insulting them, or just being very curt), you’ll have to change your communication style. A human is going to read your messages, after all, even if you’re really interacting with a LLM. There’s no point being rude. But if, like me, you say please-and-thank-you to the models
, you can treat your LLM-using coworker as just another Copilot window or Codex tab. It’s far better than having to treat them as an unwitting saboteur.
Not all net-negative engineers use AI tools like this. Many are strongly convinced in their own wrong opinions about how to build good software, or mistrust AI in general, or believe that relying heavily on LLMs is not a good way to improve
. But
no
strong engineers use AI tools like this. Even when they’re being lazy or sloppy, a capable engineer will have enough baseline taste to catch obvious AI-generated errors. So the phenomenon of engineers
becoming thin wrappers around Claude Code is limited to the kind of engineers for whom this is an improvement in their work product.
Here's a preview of a related post that shares tags with this one.
