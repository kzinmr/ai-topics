---
title: "The Production Function Changed"
url: "https://hyperbo.la/w/production-function-changed/"
fetched_at: 2026-04-29T07:02:15.111578+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# The Production Function Changed

Source: https://hyperbo.la/w/production-function-changed/

Turn on
no-await-in-loop
in a human-written codebase and you just bought
yourself a migration project. In an agentic codebase, it is one PR: enable the
rule, fix 600 violations, land exhaustive positive and negative tests, and move
on.
That is what I mean when I say the production function changed.
For decades, software output scaled roughly with human engineering time. The
scarce resource has always been human time and attention. More engineers meant
more throughput, with coordination costs eating the margins. That mental model
is deeply ingrained: planning, staffing, prioritization, and risk management all
assume it.
That was always the trade. Everyone knew what the better version looked like;
the better version just cost more. So the cheap version shipped. The missing
step was never knowing the rule. The missing step was turning the rule into code
and paying the migration cost across the repo. Agents make that cheap: the lint
or CLI check, the exhaustive positive and negative fixtures, the migration PR,
and the ratchet that keeps the regression from coming back.
Once the migration cost collapses, you stop settling for the cheap version.
Every engineer has been paged by some network call that needed a timeout and a
retry but had neither. We know what good looks like here. We still get paged
because almost nobody bothered to write the static rule, migrate the callers,
and lock the door behind the fix. Coding agents change that math.
The same move works everywhere else. Turn on
zizmor --pedantic
for GitHub
Actions. Ban raw fs and force the safe wrapper. Brand durations and IDs so raw
numbers and strings stop leaking across boundaries. None of that is novel. The
change is that it is finally cheaper to encode the rule than to keep relearning
it in production.
None of that work is glamorous. All of it used to be expensive. Now it is free
enough that I can enforce uniformity across a whole codebase instead of picking
my spots and living with the mess.
The same thing is true at a higher level of abstraction. I want a user
preference stack with
on | off | unset
, plus a service-level default for
unset
that can change over time. I want delegated registration so
“preferences” or “feature flags” stay centrally managed while each business
domain registers its own knobs. That used to sound like the kind of idea you
water down because the fiddlyness would eat the team alive. Now I can just do it
correctly. That is the change in the production function: you can do things at
the right level of abstraction for the same price as doing them shittily.
That is also why the bottleneck moved. I am not sitting next to teammates
shoulder surfing them in Vim, and I do not want to shoulder surf agents either.
So I care much less about watching code appear on screen and much more about
proof. Record a video. Give me screenshots. Show me the logs. Attach the PR
media. If the task touched a running app, prove to me that you launched it and
observed the behavior you claim you changed.
I haven’t written code by hand in months. My laptop hums with its lid half
closed at night, running
caffeinate -sdi
so a PR or three can get authored,
pushed, reviewed, and merged while I’m asleep.
That workflow already exists in my day-to-day work. When I want an end-to-end
run, I prompt Codex with
$task $launch-app $local-obs $commit $push $land $github-pr-media
and let it
rip. That is the explicit harness: do the work, gather the proof, and carry it
through landing.
There is a lighter workflow too. Sometimes the task is just replying to a Slack
thread with
@Codex do it
. Codex web picks up the thread as context, handles a
docs fixup or small ticket asynchronously, and opens a PR. At that point I am
making a yes or no merge decision with very little sunk cost fallacy, because I
am not attached to the code as written and I did not spend the day typing it.
The production function changed because implementation effort stopped being the
expensive part. The expensive part is deciding what invariants matter,
expressing them so the agent can act, and insisting on proof that the job was
actually done.
