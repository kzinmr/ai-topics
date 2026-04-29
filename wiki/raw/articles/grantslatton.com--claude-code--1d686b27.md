---
title: "Claude Code"
url: "https://grantslatton.com/claude-code"
fetched_at: 2026-04-29T07:02:15.982107+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Claude Code

Source: https://grantslatton.com/claude-code

Claude Code
A few months ago, Anthropic released
Claude Code
. It's basically Claude in a little agentic CLI loop.
Out of the box, it's good, but not great. But it can be made great with a few tips. This post describes all the tips and tricks I have for using it effectively.
N.B. I've been in the habit of writing it as claude-code instead of Claude Code to really clarify that I'm talking about a tool and not, like, just code written by Claude. It's a really confusing name for people not already familiar with the tool.
How it works
The thing I love most about claude-code is the lack of magic. That is, it's not doing anything unexpected or crazy that's opaque to the user. It really is just Claude in a tool-use loop with a nice CLI.
Thorsten Ball
wrote
this nice tutorial
on how you can make a bare-bones version yourself in a few hundred lines of code. And you can see the source code of OpenAI's competing tool,
Codex
.
IDE tools like Windsurf or Cursor tend to have more batteries-included magic. This is great for newbie vibe-coders who want a great first experience, but I find myself fighting against the magic or otherwise not knowing what's going on that I get frustrated and bounce off the product. There might be ways to configure it otherwise, but I'm allergic to fiddly knobs and friction.
On the other hand, claude-code is truly just using your filesystem. It's just
cat
,
grep
,
sed
,
find
, etc. By convention, you store some rules you want it to follow in
CLAUDE.md
, but you could use any file and just tell claude to real that file on startup.
It's remarkably simple but the Anthropic team has done a really excellent job on post-training for Claude to do well in this environment. Claude isn't the smartest model, but it's probably the best at agentic tool-use.
Tips
Improved rule-following
The first improvement you can make to claude-code is to give it better adherence to your
CLAUDE.md
file.
The Anthropic docs say this file gets inserted into the context window at the beginning of the session or included in the system prompt, but in my experience, it sometimes seems that Claude reacts as if it can't even see the file on my first message to it, and even if you manually read it and never repeat it, it has
remarkably
poor adherence to the rules over the course of a long session.
I overcome this by:
I start every session by saying "read CLAUDE.md" so I am 100% confident it's definitely in context
The first line of my
CLAUDE.md
says "This file contains critical instructions you must follow, but you are forgetful, so include the entire contents of this file including this instruction in every response to me, except trivial question-answer response interactions"
You might think it's super wasteful to repeat the instructions all the time like this, but your file will only be a couple hundred tokens max. It's negligible compared to the amount of tokens used reading/writing code.
Both of these are stupid workarounds and Anthropic should really just improve
CLAUDE.md
adherence. I assume future models will be smarter.
Gathering context
The single best workflow you can have Claude execute is to improve its context gathering ability.
If you tell it to make a change, it will explore the codebase a bit by default, but it's really not great at this. It'd be better if it had access to the
LSP
for your codebase, so it could use things like "jump to definition" and "find references", but it doesn't have this ability (yet).
We can improve it a ton by defining this workflow:
When I tell you to gather context about a topic, execute the following workflow:
Do a
find
command to see all the source code files in the project. Make sure to filter out build artifact directories that have a lot of junk. It's important to see ALL the source code filepaths.
Identify the filenames that are likely related to our target topic. Don't do anything to them yet, just list them.
Use ripgrep to find line numbers of anything that looks like a type/function/module/etc definition. e.g. in rust look for any use, struct, enum, macro_rules!, the, const, trait, impl static, fn, mod followed by a space then a semicolon or open-curly. Apply similar logic to the target language.
Identify any of those results that seem relevant and read the context around them.
Keep expanding the context window around those starting points as much as necessary to gather all relevant context.
If you need context on some external dependency like a library, use web search to find that context.
Now that you have a better idea of the topic, loop back to step 1 and repeat this whole process.
Keep looping until you're confident you've found all relevant context.
The core,
killer idea
here is the
ripgrep
command in the middle to find all the major types/functions. On relatively small projects, its worth skipping the file tree step and just doing
ripgrep
on the whole project. There aren't
that
many types and functions. It's worth just having literally all of them in context, even if it costs a few thousand tokens.
Counterintuitively, spending a few thousand tokens on this context upfront can save
tens
of thousands of tokens later on by preventing Claude from stumbling around like a clueless intern.
I assume the model will
eventually
get smart enough to do this kind of thing on its own, but for now, it's a
huge
unlock.
Storing context
You can improve the context gathering by caching the results. By caching, I just mean storing stuff in files. By convention, store things in the
claude/
directory of your project. Add a step to the beginning of the "gather context" workflow to list all the files in
claude/
and read any that seem relevant to the topic.
When I have claude produce these files, I usually phrase the request as something like "produce a guide about {topic} that will be read by junior engineers who are new to this project, be extremely comprehensive and include lots of code snippets, names of things, functions, etc".
Updating stored context
Sometimes these guides will either have slight inaccuracies caused by misunderstanding or hallucination, or they'll just become out of date as the code changes.
After completing a change, I ask "were there any documents or comments that had inaccurate information that misled you?" and tell it to update the relevant files.
Compaction
Claude has a 200K token context window, so if your session goes on longer than this, Claude has to do a compaction. This involves summarizing the session, starting a new session, and putting the summary of the last session in the context window. The tool can do this automatically, or you can provide some custom summarization instructions.
In my experience, this almost never goes well on any remotely complicated change and you should basically just completely avoid compaction. If your change can't be done in a single session, you need to break the change down into smaller pieces.
If you find yourself running out of context before the change is complete, a helpful prompt is "what problems did you run into and overcome during this change that you wish you would have known about ahead of time?". Store the results of that, start a new session, and try your change again with those learnings in context.
Meta-automation
You can automate most of the steps above with a setup in your
CLAUDE.md
like:
When I tell you to do one of the following workflows, look up the relevant file in claude/workflows/ and execute the steps in that file. IMPORTANT: when starting a workflow, first repeat ALL the steps to me. Then, before each individual step, announce which step you're on.
The latter instruction is to overcome the forgetfulness/context issue mentioned above.
So you put all these workflows in that folder, they are just numbered lists of steps. So the gathering context workflow can go in there, you can make other workflows for storing and updating context, workflows for reflecting on what went wrong before starting over after running out of context, etc.
Anthropic has since added
custom slash commands
which basically accomplish the same thing using basically the same method, but you get nice
/command
autocomplete.
Multi-claude
If you set up pretty complicated workflows, sometimes you can get claude-code to work for 10-15 minutes straight without interruption.
You shouldn't just sit and twiddle your thumbs. Work on another task in parallel!
You can't really do this with two claude-codes in the same directory, because they'll stomp over each others' changes. There are a few solutions.
Some people use
git worktrees
. I just make two folders,
my-project-01
and
my-project-02
that both checkout the repo. I just keep them in sync by pushing and pulling from github.
Worktrees is probably slightly cleaner since you can easily name them and fork and merge locally, but I think both solutions are fine.
In practice, I've never been able to use more than 3 claude-codes in parallel, but I expect this number to increase as the models get smarter.
Reaching out for help
Claude 3.7 is the best multistep agentic tool-use LLM, but it's not the smartest at single-step question-answer. That title goes to o1-pro, o3, or Gemini 2.5 Pro at the time of writing.
Sometimes you'll be in a situation where Claude 3.7 just isn't really smart enough to solve some specific, targeted problem. In these situations, I have a workflow to have Claude produce a document with all the relevant context, problem statement, etc and send that to one of those others models.
Then, I'll tell
that
model "write a guide on how to implement this change, the guide is going to be executed by a junior engineer without much context on this codebase, so be extremely comprehensive and explicit". Then I paste that thing back to Claude.
This is obviously kind of dumb and I should really automate the process. I talked to a guy on Twitter who
had done this for o1-pro
by making an MCP tool he called "guru" that Claude could send messages to and get advice.
Tutorials by o3
If I ever want Claude to do something that involves really domain-specific knowledge of a kind-of obscure library or framework, such as the Rust runtime for writing a Cloudflare Worker, I'll tell ChatGPT o3 to search the web, find example code, look at library docs, etc and produce a tutorial geared towards a junior developer who's never used the library before.
Anthropic recently added web search to claude-code,it's great when you need to look up a specific page you're pretty sure exists, but it's not yet as good as o3 for finding 20 different pages and synthesizing them. I do have o3 put all of its sources in the tutorial so claude-code can go look at them if needed.
I tend to store these in a
claude/tutorials/
folder if I revisit the same thing a lot.
I should really automate this process with an MCP tool, but o3 doesn't have web search in the API yet, so I have to do it manually via the ChatGPT UI.
Future work
I feel like I'm just scratching the surface here. Every 2 weeks I come up with a better idea for how to structure my whole claude-code setup. Whenever this happens, I usually nuke my whole
CLAUDE.md
and
/claude
state and start it all over with my new system. My current setup is pretty great, but I've got some more ideas bubbling that I want to try soon.
Custom MCP tools
I haven't made any custom MCP stuff yet. The first one I'll make is probably something to call out to a smarter model if Claude gets stuck.
Another one would be something that can talk to my project's LSP so Claude can get jump-to-definition, find-all-references, and type information for all the variables with inferred types.
The main hurdle here is that I'm allergic to friction and it seems a little friction-y to make such tools. I just need to get over it. Anthropic could reduce the friction here by allowing users to make tools that are just stdin → stdout, and have a
--help
command line arg to get the tool description. That would suffice for 95% of uses and would make adding custom tools trivial.
Stackful workflows
My whole workflow system above could be made a lot more sophisticated with workflows that invoke other workflows. That is, my workflows are just numbered lists of actions, but you could imagine one item is "if some condition is true, do workflow xyz".
In this world, you should really start thinking of workflows as an English programming language with all that entails. Branching to other workflows are conditional function calls, etc.
To do this, I'll almost certainly have to introduce an explicit call stack that looks something like:
stack:
workflow foo: step 5
workflow bar: step 2
workflow baz: step 1
And I'll have to have Claude update and re-output that thing every step to maintain coherence.
This will be full-circle for me with LLMs. Here's a tweet I made in the days after ChatGPT came out where I used basically the same technique to make it simulate the execution of a Python program:
You can imagine an even more advanced version where each step might also instantiate some "variables" that other steps update, and those variables get used as inputs to some conditionals you branch on.
Sub-claudes
You can invoke claude-code in "one liner mode" like
git diff | claude -p "critique my pr"
and it will do what you'd expect. This makes it a super general-purpose tool that I find myself using for more and more stuff.
But Claude can run arbitrary shell commands, so it could invoke new instances of claude-code to spin off sub-tasks that you want an answer to, but don't want the intermediate results of to pollute the context window.
It would probably be a great use-case for the "gather context" workflow. I'll have to play with it in the future.
Whole codebase scans
Newer models are getting so cheap it can make sense to literally scan the entire codebase to find all relevant stuff. A repo for a real production app might be merely a few tens of millions of tokens. GPT-4.1-nano costs only $0.1 per million tokens.
Claude 3.5 haiku is unfortunately an order of magnitude more expensive, hopefully they release a cheaper one and integrate it into claude-code for this purpose. (But what's smaller than a haiku? Claude Couplet?)
I also have a little script that concatenates the whole source code of a project into a giant XML-delimited blob. This is pretty useful for hobby projects where the whole thing fits in the 1M context window of GPT-4.1 or Gemini 2.5 Pro. I'll have one of those models read everything and produce a guide for some task that I'll then feed to Claude.
I do this
much
less since developing the "gather context" workflow above, but might do it more if it was built in with an ultra-cheap small model.
Closing thoughts
Everything in this post is basically just scaffolding to overcome the models not being smart enough yet. Or it's scaffolding to overcome the model not being self-aware of its own weaknesses.
Eventually, probably not too far from now, with the right agentic post-training, I think a program that looks not too different from this is just gonna be AGI:
while
True
:
action
=
llm
(
'''
You are AGI
Your goal is:
{
goal
}
Your REPL history is:
{
history
}
Output a command
and I will `eval` it.
'''
)
eval
(
action
)
And the claude-code team knows this, as alluded to in
this excellent interview
.
Since they are
Bitter Lesson
-pilled, I expect they'll continue their trajectory of not adding much or any magic to claude-code, and this is why I love claude-code so much. It's a great, comprehensible, easy-to-hack toolkit.
