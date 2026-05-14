---
title: "The complete claude code tutorial "
created: 2026-01-10
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2010076957938188661"
x_article_author: "Eyad"
x_article_author_handle: "@eyad_khrais"
source: "https://x.com/eyad_khrais/status/2010076957938188661"
tags: [x-article]
---

I’ve been a SWE for 7 years, between Amazon, Disney, and Capital One. The code I’ve shipped touches millions of users, and I built systems that couldn’t afford to break. Now I’m the CTO of a startup that builds agents for enterprise, and Claude Code is my daily driver.
Here’s a beginners playbook you might find useful, containing everything I’ve learned about Claude after using it to build robust systems that handle complex workloads from large companies. Let me know if it helps below.
Think First
Most people assume that with Claude Code and other AI tools, the first thing you need to do is type (or start talking). But that's probably one of the biggest mistakes that you can make straight off the bat. The first thing that you actually need to do is think.
10 out of 10 times, the output I've gotten with plan mode did significantly better than when I just started talking and spewing everything into Claude Code. It's not even close.
Now for some of you, this is easier said than done. You might not have years of software engineering experience that would allow you to think about this on your own. To this extent I have two pieces of advice:
1. Start learning. You are handicapping yourself if you never pick up on this, even if just a little bit at a time.
2. Have a deep back and forth with ChatGPT/Gemini/Claude, where you describe exactly what you want to build, you ask the LLM for the various options you can take in terms of system design, and ultimately the two of you settle on a solution. You and the LLM should be asking each other questions, not just a one way street. .
This applies to everything. This also includes very small tasks like summarizing emails. Before you ask Claude to build a feature, think about the architecture. Before you ask it to refactor something, think about what the end state should look like. Before you ask it to debug, think about what you actually know about the problem. The more information that you have in plan mode, the better your output is actually going to be because the better the input is going to be.
The pattern is consistent: thinking first, then typing, produces dramatically better results than typing first and hoping Claude figures it out.
This brings me onto my next point of architecture. Architecture, especially in software engineering, is a little bit like giving a person the output and nothing more. This leaves for A LOT of wiggle room in how to get to the output, which is essentially what the problem with AI generated code is. If you say something super broad like “build me an auth system” as opposed to “Build email/password authentication using the existing User model, store sessions in Redis with 24-hour expiry, and add middleware that protects all routes under /api/protected.”, you can see the difference.
You click shift + tab twice, and you’re in plan mode. Trust me when I say this, this is going to take 5 minutes of your time, but will save you hours upon hours of debugging later on.
CLAUDE.md
CLAUDE.md is a markdown file. Markdown is a text format that AI models process extremely well, and Claude in particular handles it better than most other models I've tested.
When you start a Claude Code session, the first thing Claude does is read your CLAUDE.md file. Every instruction in that file shapes how Claude approaches your project. It's essentially onboarding material that Claude reads before every single conversation.
Most people either ignore it completely or stuff it with garbage that makes Claude worse instead of better. There is a threshold where too much or too little information means worse model output.
Here's what actually matters:
Keep it short. Claude can only reliably follow around 150 to 200 instructions at a time, and Claude Code's system prompt already uses about 50 of those. Every instruction you add competes for attention. If your CLAUDE.md is a novel, Claude will start ignoring things randomly and you won't know which things.
Make it specific to your project. Don't explain what a components folder is. Claude knows what components are. Tell it the weird stuff, like the bash commands that actually matter. Everything that is part of your flow should go into it.
Tell it why, not just what. Claude is a little bit like a human in this way. When you give it the reason behind an instruction, Claude implements it better than if you just tell it what to do. "Use TypeScript strict mode" is okay. "Use TypeScript strict mode because we've had production bugs from implicit any types" is better. The why gives Claude context for making judgment calls you didn't anticipate. You'll be surprised how effective this actually is.
Update it constantly. Press the # key while you're working and Claude will add instructions to your CLAUDE.md automatically. Every time you find yourself correcting Claude on the same thing twice, that's a signal it should be in the file. Over time your CLAUDE.md becomes a living document of how your codebase actually works.
Bad CLAUDE.md looks like documentation written for a new hire. Good CLAUDE.md looks like notes you'd leave yourself if you knew you'd have amnesia tomorrow.
The Limitations of Context Windows
For example, Opus 4.5 has a 200,000 token context window. But here's what most people don't realize: the model starts to deteriorate way before you hit 100%. (this is varying dependent on whether you use through API vs desktop app)
At around 20-40% context usage is where the quality of the output starts to chip away, even if not significantly.  If you've ever experienced Claude Code compacting and then still giving you terrible output afterwards, that's why. The model was already degraded before the compaction happened, and compaction doesn't magically restore quality. (hit /compact for compacting)
Every message you send, every file Claude reads, every piece of code it generates, every tool result - all of it accumulates. And once quality starts dropping, more context makes it worse, not better. So here are some things that actually help with not having terrible context
Scope your conversations. One conversation per feature or task. Don't use the same conversation to build your auth system and then also refactor your database layer. The contexts will bleed together and Claude will get confused. I know at least one of you reading this is guilty of that.
Use external memory. If you're working on something complex, have Claude write plans and progress to actual files (I use SCRATCHPAD.md or plan.md). These persist across sessions. When you come back tomorrow, Claude can read the file and pick up where you left off instead of starting from zero. Sidenote: if you have a hierarchy system of files, keeping these at thievery top is how you can get these to work for every task / feature that you decide to build out.
The copy-paste reset. This is a trick I use constantly. When context gets bloated, I copy everything important from the terminal, run /compact to get a summary, then /clear the context entirely, and paste back in only what matters. Fresh context with the critical information preserved. Way better than letting Claude struggle through degraded context.
Know when to clear. If a conversation has gone off the rails or accumulated a bunch of irrelevant context, just /clear and start fresh. It's better than trying to work through confusion. Claude will still have your CLAUDE.md, so you're not losing your project context. Nine times out of ten, using clear is actually better than not using it, as counterintuitive as that sounds.
The mental model that works: Claude is stateless. Every conversation starts from nothing except what you explicitly give it. Plan accordingly.
Prompts Are Everything
People spend weeks learning frameworks and tools. They spend zero time learning how to communicate with the thing that's actually generating their code.
Prompting isn't some mystical art. It’s probably the most fundamental form of communication there is. And like any communication, being clear gets you better results than being vague. Every. Single. Time.
What actually helps:
Be specific about what you want. "Build an auth system" gives Claude creative freedom it will use poorly. "Build email/password authentication using this existing User model, store sessions in Redis, and add middleware that protects routes under /api/protected" gives Claude a clear target. Even this is still not perfect.
Tell it what NOT to do. Claude has tendencies. Claude 4.5 in particular likes to overengineer - extra files, unnecessary abstractions, flexibility you didn't ask for. If you want something minimal, say "Keep this simple. Don't add abstractions I didn't ask for. One file if possible." Also, always cross-reference what Claude produces because you don't want to end up having technical debt, especially if you're building something super simple and it ends up building 12 different files for a task that realistically could have been fixed with a couple of lines of code.
Something that you have to remember is that AI is designed to speed us up and not completely replace us, especially in the era of very professional software engineering. Claude still makes mistakes. I'm sure that it will keep making mistakes, even if it's going to get better over time. So being able to recognize these mistakes will actually solve a lot of your problems.
Give it context about why. "We need this to be fast because it runs on every request" changes how Claude approaches the problem. "This is a prototype we'll throw away" changes what tradeoffs make sense. Claude can't read your mind about constraints you haven't mentioned.
Remember: output is everything, but it only comes from input. If your output sucks, your input sucked. There's no way around this.
Bad Input == Bad Output
People blame the model when they get bad results. "Claude isn't smart enough" or "I need a better model."
Reality check: you suck. If you're getting bad output with a good model like Opus 4.5, that means your input and your prompting sucks. Full stop.
The model matters. A lot, actually. But model quality is table stakes at this point. The bottleneck is almost always on the human side: how you structure your prompts, how you provide context, how clearly you communicate what you actually want.
If you're consistently getting bad results, the fix isn't switching models. The fix is getting better at:
How you write prompts. Specific > vague. Constraints > open-ended. Examples > descriptions.
How you structure requests. Break complex tasks into steps. Get agreement on architecture before implementation. Review outputs and iterate.
How you provide context. What does Claude need to know to do this well? What assumptions are you making that Claude can't see?
That said, there are real differences between models:
Sonnet is faster and cheaper. It's excellent for execution tasks where the path is clear - writing boilerplate, refactoring based on a specific plan, implementing features where you've already made the architectural decisions.
Opus is slower and more expensive. It's better for complex reasoning, planning, and tasks where you need Claude to think deeply about tradeoffs.
A workflow that works: use Opus to plan and make architectural decisions, then switch to Sonnet (Shift+Tab in Claude Code) for implementation. This will depend on your task, sometimes you can use opus 4.5 for implementation as well. Think about selling your kidney if you’re doing this through the API usage tab though. Your CLAUDE.md ensures both models operate under the same constraints, so the handoff is clean.
MCP, Tools, and Configurations
Claude has a ridiculous amount of features. MCP servers. Hooks. Custom slash commands. Settings.json configurations. Skills. Plugins.
You don't need all of them. But you should actually try them and experiment, because if you're not experimenting, you're probably leaving time or money on the table. I promise you there's at least one new feature coming out in Claude that you don't know about, that you can actually learn about if you follow Boris, the founder of Claude Code.
MCP (Model Context Protocol) lets Claude connect to external services. Slack, GitHub, databases, APIs. If you find yourself constantly copying information from one place into Claude, there's probably an MCP server that can do it automatically. There's a ton of MCP marketplaces, and if there is not an MCP, it's just a way of getting structured data, so you can just create your own MCP server for whatever tool that you need added that doesn't exist at the moment. I will be very surprised if you find one that doesn't exist though.
Hooks let you run code automatically before or after Claude makes changes. Want Prettier to run on every file Claude touches? Hook. Want type checking after every edit? Hook. This catches problems immediately instead of letting them pile up. This is actually what helps remove technical debt as well. If you set a specific hook after every thousand lines, you have the security feature potentially cleaning up your code. Should be very helpful when Claude reviews your PRs.
Custom slash commands are just prompts you use repeatedly, packaged as commands. Create a .claude/commands folder, add markdown files with your prompts, and now you can run them with /commandname. If you're running the same kind of task often - debugging, reviewing, deploying - make it a command.
If you have the Pro Max plan (I pay the $200/month), why not try everything Claude has to offer? See what works and what doesn't. You're paying for it anyway.
And here's the thing: don't get shut off if something doesn't work on the first try. These models are improving basically every week. Something that didn't work a month ago might work now. Being an early adopter means staying curious and re-testing things.
When Claude Gets Stuck
Sometimes Claude just loops. It tries the same thing, fails, tries again, fails, and keeps going. Or it confidently implements something that's completely wrong and you spend twenty minutes trying to explain why.
When this happens, the instinct is to keep pushing. More instructions. More corrections. More context. But the reality is that the better move is just to change the approach entirely.
Start off simple - clear the conversation. The accumulated context might be confusing it. /clear gives you a fresh start.
Simplify the task. If Claude is struggling with a complex task, break it into smaller pieces. Get each piece working before combining them. But in reality, if Claude is struggling with a complex task, that means that your plan mode is insufficient.
Show instead of tell. If Claude keeps misunderstanding what you want, write a minimal example yourself. "Here's what the output should look like. Now apply this pattern to the rest." Claude is extremely good at understanding what success metrics look like and actually being able to follow them, of what a good example is.
Be creative. Try a different angle. Sometimes the way you framed the problem doesn't map well to how Claude thinks. Reframing - "implement this as a state machine" vs "handle these transitions" - can unlock progress.
The meta-skill here is recognizing when you're in a loop early. If you've explained the same thing three times and Claude still isn't getting it, more explaining won't help. Change something.
Build Systems
The people who get the most value from Claude aren't using it for one-off tasks. They're building systems where Claude is a component. But claude code is way better than that. It has a -p flag for headless mode. It runs your prompt and outputs the result without entering the interactive interface. This means you can script it. Pipe output to other tools. Chain it with bash commands. Integrate it into automated workflows.
Enterprises are using this for automatic PR reviews, automatic support ticket responses, automatic logging and documentation updates. All of it logged, auditable, and improving over time based on what works and what doesn't.
The flywheel: Claude makes a mistake, you review the logs, you improve the CLAUDE.md or tooling, Claude gets better next time. This compounds. Right now I'm in the process of being able to have Claude already improve its own Claude.md files though. After months of iteration, systems built this way are meaningfully better than they were at launch - same models, just better configured.
If you're only using Claude interactively, you're leaving value on the table. Think about where in your workflow Claude could run without you watching.
TLDR
Think before you type. Planning produces dramatically better results than just starting to talk.
CLAUDE.md is your leverage point. Keep it short, specific, tell it why, and update constantly. This single file affects every interaction.
Context degrades at 30%, not 100%. Use external memory, scope conversations, and don't be afraid to clear and restart with the copy-paste reset trick.
Architecture matters more than anything. You cannot skip planning. If you don't think through structure first, output will be bad.
Output comes from input. If you're getting bad results with a good model, your prompting needs work. Get better at communicating.
Experiment with tools and configuration. MCP, hooks, slash commands. If you're paying for Pro Max, try everything. Stay curious even when things don't work the first time.
When stuck, change the approach. Don't loop. Clear, simplify, show, reframe.
Build systems, not one-shots. Headless mode, automation, logged improvements over time.
If you're building with Claude - whether it's your own projects or production systems - these are the things that determine whether you're fighting the tool or flowing with it.
Modern day technology is absurdly capable. If you want more tips on how to get the most out of AI for yourself or your business, subscribe to my free weekly AI newsletter: https://varickagents.com/newsletter
