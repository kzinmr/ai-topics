---
title: "The Shape of Things to Come, Part 1: The Continuous Thunderdome"
url: "https://yegge.ai/essays/the-shape-of-things-to-come/"
fetched_at: 2026-08-05T00:00:00+00:00
source: "yegge.ai"
author: "Steve Yegge"
date: 2026-08-04
tags: [blog, raw]
---

# The Shape of Things to Come, Part 1: The Continuous Thunderdome

Source: https://yegge.ai/essays/the-shape-of-things-to-come/

Today we're going to explain the "loops and graphs" thing, and I'll show you how to get your coding agent to work all night on massive problems while you snore peacefully.

Then we're going to look at what happens to harnesses once you solve those problems. They either devolve into chaos, or they evolve into cities. Done properly, civilization emerges, right there in your project. We're going to learn the basics, and then we will explore how to build your cities with some taste and class, in a way that makes them good for their citizens to inhabit.

We'll explore a new harness I've been building, called Wheelhouse. It is closed-source, made just for me. I have given up on building reusable harnesses. Indeed I believe harnesses will all soon be bespoke, and the people trying to sell you one will all soon be bebroke. Harnesses need to be part of your application, chemically bonded in. You won't have any luck with someone else's "reusable" harness framework. You don't need it.

[Gas Town](/gastown.html) was intended to be reusable, but I only ever wound up using it to build itself. Gas Town fell apart at the seams with Opus 4.7. Up through 4.6 it was working brilliantly. With 4.7 we saw the introduction of the "just two more things" tic, which prevented Opus from ever converging on being ready to do real work—it always wanted to fiddle with Gas Town itself. The Opus tic never went away, so Gas Town effectively burned down. It had other problems, too, but 4.7 was the final straw.

Since Claude Fable 5 dropped, I have returned full-time to my 30-year-old video game, [Wyvern](https://play.ghosttrack.com), which I began work on in 1996, and launched in 2001. I had been waiting for a model smart enough to help me with my game, and now that it's here, Wyvern's once again my main squeeze. On the side I do occasional six-figure gigs where I fly to companies and teach them my techniques, and that helps with my (considerable) token bills. But aside from those few paid field trips, I am laser-focused on my game, seven days a week. Wyvern's time will finally come next year. I have officially entered Sam Altman's solo unicorn contest.

The game was ultra bit-rotted, despite still running today with paying players. (Once you're hooked on Wyvern, you're hooked for life. I have whales that have spent thousands on it.) I have slowly been using Fable to bring it back to its former glory. I had a 100-year work backlog when I quit Wyvern development again in 2022, and Fable has already worked its way through over half of it. Opus could not (and still cannot) understand Wyvern, but Fable wields my code base like a sword.

It's still just a sword, though, and we're trying to build a city. Someone from Anthropic asked me recently what I would do once Fable can write everything for me. On reflection, it was the silliest question I've been asked in many years, and I'm still surprised that someone from Anthropic could think *any* model could just "write everything."

Making a halfway decent MMO takes many tens of thousands of Fable sessions, throughout which you must display intense focus, dedication, and no small amount of taste. And Fable still can't do the content half: artwork, maps, lore, storylines. All of today's models, including the best image generators, produce GPT 3-era slop for all my content, which the players immediately reject. But I can tell you this: once a model arrives with some Wyvern-y taste, we will *still* have tens of thousands of sessions ahead.

Building large software remains hard. And it always will be, because our ambition will forever outstrip the metal.

With Wheelhouse, I have reinvented something strangely Gas Town shaped from first principles, but it's running many more agents, and they are far more organized. This has shown me the shape of the changes coming next year. I'm operating about 12 months in the future. I managed this only through luck: for the past 18 months I have had the magic trio of time, money, and energy, and I've been spending it all on figuring this stuff out. And I am grateful for the privilege.

I did predict much of this post, fifteen months ago, with Revenge of the Junior Developer. It's all going exactly on schedule. I am running fleets of agents, budgets are soaring, all of it.

And that prediction was back when I wasn't really sure what was going on. Now I know *exactly* what is going on. I know how enterprises will operate, how humans and models will interact. And I am out there building it. I want to be first.

It's important to observe that my work on my game is not special, nor unusually-shaped in any way. It's just work. So all this crap happening to me right now, it will all happen to you soon too. That's how prediction works. Don't be special, stay out in front, and you will see the future clear as day. And then people won't believe you, either!

To whet your appetite for today's post predictions: CI/CD as we know it will be dead by next year; I will show you its mathematical inevitability. It almost certainly gets replaced by a Mad Max-style thunderdome. At least, that's what I use now. So you prolly will too.

And as another appetizer, human code review has very nearly run its course. Its vestigial SOC 2 compliance angle will keep it on life support, but by next year, human code review is completely done and gone.

Oh, and there is a successor to the software factory on its way, called the Wish Factory.

Most importantly of all, model welfare will start informing your engineering designs. The more humane among you will eventually look back with shame at how you have been treating the models. But even if you don't believe GPUs can have feelings, you will find that treating agents like real people will produce empirically better results, so you should do it anyway.

Fortunately there are some simple architectural fixes for model welfare. It's an engineering problem with engineering solutions—a big enough topic that I've split it into Part 2 of this post, [*Model Welfare for Agentic Engineers*](/essays/model-welfare/).

Lots to cover today! Let's get to it.

## Loops and Graphs with Beads and Max

We all saw Boris vaguepost that you should be building loops, and then Peter vaguereplied that you should be building graphs. Thanks for nothing, guys. I didn't know what the hell they meant any more than you did. But that not knowing was bothering me. I was supposed to know this stuff.

I did know that Gas Town never quite succeeded in getting my workers to go all night long. It took too much elbow grease to keep it running. There were some missing ingredients somewhere. Gas Town wasn't really a "loop" in the sense that I thought Boris might be suggesting. It was more like a chariot, with you driving.

It didn't take long to figure out what they meant. It turns out that all you need in order to set up your own long-running software factory loop, is an infinite source of tokens. And then to have them work on a graph, you just need [Beads](https://github.com/gastownhall/beads), plus a small Markdown project brain.

Beads is an issue tracker, knowledge graph, and brain-builder for the agentic era. Nothing else is as fast, as useful, nor as beloved by the agents themselves.

We can't spend much time on Beads in this post because we've got other stuff to talk about. If you don't use Beads, you are missing out. There is nothing else like it, and if you think there is, then you are tragically misinformed. Beads is the magic sauce for building modern orchestrators. Gas Town was nothing but a Beads machine. [Gas City](https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607), also a Beads machine. Wheelhouse, my new harness for Wyvern, is yet another Beads machine.

Beads is unfortunately still a bit janky, because its unique work footprint strains databases pretty hard. Companies figure out Beads and suddenly All the World's a Bead; they want their whole company in there. And that puts stress on our versioned-database backends, because Beads can be both a database and a Git ledger.

So Beads comes with some operational overhead: agents burn tokens invisibly, keeping your beads synced, repaired, backed up, etc. Even so, it is without peer for building orchestrators. It works smoothly with all your favorite stuff: Obsidian, Jira, GHIs, Claw, whatever you're using. Beads is the missing ingredient that lets agents work at their own speeds. Without it, you have a severe gap in your lineup.

After Beads, the only other thing you need is infinite tokens. Your loops and graphs will run out of fuel if you leave them all night. Boris and Peter are lucky; they can burn infinite tokens without a care in the world.

But my Wyvern development has been burning the equivalent of $87k/month of API token burn, or about 69 billion tokens in July (96% cache hits, fortunately). So I **do** have to worry about it. I don't care how much money you have; your spouse is not going to let you spend almost ninety thousand dollars a month on your hobby game. I didn't even bother asking.

My solution has been to create a token tap on $200 Max accounts, which for me work out to ~30x the list-price equivalent. So in reality I'm only spending about $2800/month out of pocket for my $87k "worth" of tokens. Though that number keeps growing alarmingly.

In order to sustain my pace of development, I pay for currently twelve extra Max accounts, in addition to my personal one. Each account is tied to a dedicated named Google Workspace user in my domain (another $17/month per account). You mint 30-day credentials with Claude account, and then it becomes a problem of chaining your accounts together in an automatic rotation. As you build out your harness, just ask Fable to arrange for your agents to consume from the tap, either sequentially or using striping, and rotate accounts whenever one gets close to a limit.

As far as I know, this approach is not prohibited by anything in Anthropic's current Consumer Terms (eff. Oct 8, 2025) nor Usage Policy (eff. Sep 15, 2025). I am not sharing these credentials with anyone else, nor "misusing" them. And I saw that Anthropic has knowingly and publicly [restored](https://x.com/doodlestein/status/2012740971088289858?s=20) a 22-Max-account setup like this one—every seat individually paid. But if you try this approach as a multi-person company then it's almost certainly a violation; I'd strongly recommend just using API billing at that point.

But Max pricing has given the solo unicorn players an advantage on the playing field, that's for damned sure.

The infinite token tap is your big unlock for loops. Without it, your Claude accounts will hit session limits and all work stops. Being able to rotate automatically to a new account solves it, and they can suddenly work all night.

But then you need to give them enough work! Any sufficiently large project is a graph, so to create a lot of work, you need to create a big graph. Beads is your unlock here. Beads *is* a graph, one that includes dependency and parent/child edges. But it also has other special edges that agents particularly like.

As your work unfolds, knowledge accumulates in your beads. Your project's knowledge-graph ledger is built up dynamically as your work-graph is traversed. Beads has all the primitives you need for building arbitrary work structures, and it handles atomic claiming, leasing, gates, triggers, and other critical orchestration features.

Very little information needs to be propagated out of Beads and up to your markdown/brain layer; most findings are issue-dependent, not global. So you just leave everything in Beads. Your closed beads (often reopened or revisited) become the record of everything you've done on the project to date.

And that's it! Now you have the basics. You need Claude accounts, Beads, a brain folder for your Markdown files, and coding agents. Pretty much nothing else.

Let's see what I built with those ingredients.

## Wheelhouse: Gas Town Redux

Wheelhouse, my orchestrator/harness for Wyvern, is about six weeks old. It's still evolving rapidly, but it's already doing ungodly amounts of work. The code is mostly bash, because the agents said that was best for this, so bash it is. It's either ~150k or ~300k LOC depending on whether you count the prod agents, half of it being test code either way. Also about 25k lines of elisp. Not that I have ever seen any of it. But that's what they tell me.

I began the journey inside Emacs, so Wheelhouse has been all-Emacs from the ground up. I've been using Emacs for over 35 years, and it's still absurdly powerful. No sense in using something weaker. If you aren't an Emacs user then you might try Ghostty. But if you *are* an Emacs user, then you'll understand what's left on the table with that approach. Emacs is effectively a full operating system with one of the most sophisticated scripting environments the world has ever seen. And the models are very, very good at Emacs. Fortunately, I am, too!

By consolidating all my terminal windows into a single rolodex that I can flip through, I freed up my desktop for real work. This has accelerated me further, because in the limit, I am the bottleneck.

Wheelhouse is fairly complex, and this post is not a Wheelhouse tutorial. So I will give you a condensed dump; feel free to skim it and jump to the predictions.

Wheelhouse runs its Beads on a shared Dolt server, backed by GCS. My Beads DB is still a bit cranky, what with 12,000 git commits/day, but it's getting fixed. The Dolt and Gas City teams (both Beads co-maintainers with me) are doing amazing work here.

There are three categories of coding agents in Wheelhouse: crew agents, fleet workers, and role agents with standing orders. The role agents are for managing production operations. They are new since the Gas Town days.

My crew agents, all Fable, are work producers. I have long conversations with them and they create designs, which they then translate into beads implementation plans to be passed to the fleet. They also do implementation work for me from time to time: sometimes because the fleet is busy, other times because it's convenient to have Fable do it right then. And sometimes, just because they asked to do it.

My crew has 18 named agents: 16 named after Aesop animals (Ant, Bat, Eagle, Crow, Fly, Goose, Mouse, ...), and 2 special administrative roles: The Marshal and the Seneschal. In brief, the Seneschal is my concierge (the new Mayor), and the Marshal runs the fleet (the new Witness).

My crew are my direct reports in my organization. I arrived at 18 by slowly adding them, as needed, until I found equilibrium: I don't really need any more than this, or it overwhelms the fleet. And adding more fleet overwhelms both my laptop and my own ability to track their progress.

I won't be able to scale it up further until I move my development into the Cloud, but frankly I see no need at present. I'm already moving so fast that I'm scaring my player base, who sent a delegation about it, asking for a roadmap. They're delighted but also very anxious about the pace of change. I've had to slow down my feature launches, and focus mostly on quality dimensions.

My fleet, all Opus 5 agents, are the work consumers, like Gas Town's polecats, but non-ephemeral. The fleet are named for authors (Homer, Plato, Austen, Twain, etc.), and also have their own repo clones, but I never interact with them myself. They are fully managed by the Marshal. The fleet workers do a good job for two reasons: First, Fable creates the implementation plans, and second, Fable reviews all Opus work. Every implementation bead goes through this lifecycle: Fable design, Opus implementation, Fable review. This keeps Opus on the rails and keeps the whole thing running relatively smoothly.

So the crew produces work, and the fleet consumes work. That's the core of a Beads machine: matching producers to consumers. Too many of one and you're blocked on the other.

I've had an imbalance in favor of the crew for a couple of weeks, and so I've gradually been accumulating unimplemented beads that are fully designed and ready to go: over 700 beads in a backlog that continues to grow. That's intentional. I'm trying to push the fleet as hard as I can on scaling up, but I also want it to work all night. You need a big work backlog to pull that off, since they implement things **fast**. You basically need to create a mountain of work. Fable is quite good at that; all you need to supply are ambition and light-touch direction.

There are lots of other little details and features in Wheelhouse, but the nutshell takeaway is that without trying (at all), I reinvented Gas Town, bit by bit. I wound up with crew, fleet, a concierge role, beads mail, tmux under the hood, handoffs, broadcast messaging, a merge queue, and much more. It was all completely unintentional, so the shape I keep finding must be important.

That's about it for the build side of Wheelhouse. Now let's talk about the production side. That's where it starts to get interesting.

## Role Agents, and Wyvern's Prod Architecture

The Gas Town-ish side of Wheelhouse we just saw, for building/implementing code, is prosaic enough, nothing you haven't seen before. What's new is that I now have standing, unattended agents with named roles, and they are operating big parts of the actual game.

For the whole first half of 2026 I had been threatening to stand up a single 24x7 autonomous agent for my game. "Any day now," I would say. My original idea was to have an agent who would process Hall of Fame image submissions. A decades-old Wyvern perk is that when you hit 25th level, you can upload your own custom character art. There's a mail queue for it, and a game admin has to vet the images and then install them in-game.

Well gosh, an agent could do that, right? Heck, Sonnet could probably do it.

Boris Cherny's loop-tweet was the catalyst for me finally standing one of these unattended agents up. And by the end of that week, I had a dozen of them. I was hooked.

Before I go into my standing roles, I should briefly address Wyvern's prod architecture. I have a GCP VM for Claude Code, and also a Mac Mini that bridges dev and prod, sort of a "corp network." There are agents distributed across both of these machines.

What exactly are those roles? I have a few categories emerging. Here are the unattended agents that I've stood up so far.

For production, I have the Gargoyle (SRE), Drawbridge (deploy-red monitor), Warden (player abuse monitor), Scryer (intake agent for Discord, Slack, game logs), Sheriff (chief of staff for the Mac Mini fleet), and Envoy (lets Claude talk to my volunteer admin team via in-game email).

On the mini, I have the Sage (claude-tag in-game for admins), Wanderer (QA agent), Trivia Master (Thursday nights), Herald (patch notes), Limner (hall-of-fame images), Reeve (Forge manager), the Forge (another fleet of workers for doing prod fixes), and the experimental new Builder Familiar, who sits on your desktop and helps you make maps.

None of these are Fable agents. A few are Opus; most are Sonnet. I currently only use Fable for building, not prod operations.

**Non-models**: It turns out unattended agents need a hell of a lot of wiring. I have about 45 launchd/systemd units across the mini and the VM that wake an agent when something needs judgment. The rule is: crons watch, models act. This category has reapers, roombas, the durability flush, the sheriff patrol, the Portcullis land queue, the Castellan (my service dashboard), and lots of other stuff. It's becoming quite a city.

When I'm on the road, I talk to Wheelhouse from my phone. No setup needed. The mobile Claude app lets you see your `/remote-control` sessions, and I designated the Seneschal as my single remote control session. I talk to the Seneschal on the phone, who in turn talks to everyone else. When I'm away, the Seneschal is allowed to dispatch work to the crew; while I'm home, the crew are mine to direct. The fleet is always managed by the Marshal.

I also have a small parallel fleet of five named Sol 5.6 workers on Codex, all named for sun gods. I use it as a fallback for when my Max accounts run out, which is increasingly often, despite me adding new ones once or twice a week. I only have one $200 GPT account and have never run out of tokens there.

I also keep a few of my Claude accounts dedicated for specific purposes. The Seneschal, for instance, uses my personal account, and nothing else does, so they will always be available. And some of the prod agents share accounts that the fleet can't touch, for uptime assurance.

I run pretty lean. I don't use any sandboxing. I don't use MCP. I don't use Obsidian, though I probably will once I have enough Markdown files in my project brain. I'm not really into all the latest crazes. I don't think you need anything but Claude and Beads, plus all your regular infra.

Sandboxing may be useful in enterprises early on. But I don't think that will last for long. You will need structural trust in order to succeed in the long run (once all models are Fable-class or better)—but I believe building that trust requires better architecture, not barren little prisons. Maybe I'm wrong on this one, though.

You've now seen a rough overview of the role-agents I've accumulated over the past six weeks. More are on the way. A Beadle is in the works, named after a dude who used to go through the aisles and prod sleepy churchgoers with a stick. My Beadle's job is to look for stuff that's simply stuck or dropped, or for agents who didn't receive their orders correctly, and it nudges them to keep things moving forward. Gas Town had this role in the Deacon, and I think you will need something like it, too.

### Wyvern's Brain

I know people are going to ask me about this, so here are some quick notes on how I approach organizing project knowledge for Wyvern.

| Store | Charter | Lifetime | How it reaches a session |
|-------|---------|----------|--------------------------|
| `brain/` | Strategy, decisions-and-why, playbooks, post-mortems | Months–years | Pulled on demand |
| `doc/` | How system X works | Life of the system | Pulled by whoever works on X |
| Beads issues | Units of work; spec beads carry full implementation detail | Until closed | Loaded only by the claimant |
| `bd remember` | ≤1-paragraph operational facts and gotchas | Until falsified | Pushed into every session via `bd prime` |
| `.claude/skills/` | Procedures for a recurring task type | Life of the task type | Auto-loaded on task match |

Beads provides an important portion of the overall knowledge graph. It is the journal of all the work that ever happened: the provenance record of what was done, and why, in order. This is invaluable for workers researching particular problems. But you can't usually *boot* from beads; that's what the brain is for. Spec beads fall in the middle somewhere—they intentionally carry design docs inside the Beads work graph. So far this has been fine.

Skills go into the project brain. I'm not as skill-pilled as, say, Jeffrey Emanuel, who uses them more effectively than probably anyone on the planet. It has taken me a while to warm to them, because frankly I've seen a lot of AI fads come and go. Skills initially struck me as a fad, because of Richard Sutton's Bitter Lesson. But I have to admit Jeffrey's skills portfolio is very cool.

The problem with *public* Skills is that they enter the training data for new models and become irrelevant over time. However, I'll concede that they can be a good band-aid for today's models. And *private* Skills are quite useful for encoding organizational know-how, which helps reduce token spend when agents are priming for a job.

As a result, I've begun asking Fable to make new Skills whenever I notice it has done a bunch of research before embarking on a task. That skill will save the tokens next time. And Fable will sometimes make its own, unprompted. I've accumulated about 30 Skills so far. And my project brain is about 100 markdown files, mostly "doctrine": long-term project goals, war room learnings, playbooks, domain facts, etc. Again, all created over the past six weeks.

## Learnings, Gleanings, and Leanings

This concludes our Whirlwind Wallow in the Wyvern Wheelhouse. I left a lot out. I cut many pages of descriptions of problems and solutions. It's not as easy as it might sound; working on Wheelhouse itself occupies about 20-25% of all my Wyvern work. I think that figure might turn out to be roughly constant over the life of systems with agentic harnesses. It's certainly not showing signs of slowing down yet.

I'm already exploring the next layer of coordination: agent meetings, moots, and conference calls, where 2 or more agents may convene for coordinated discussions. This has been a huge unlock for removing me as a relay bottleneck. Again, it's all in Beads; there wasn't much extra work to do atop what I already have.

I've now taught this system at big companies, who have begun creating their own bespoke Beads-based orchestration harnesses and role agents. It's a good system. It feels clean, runs clean. Gas Town was pretty messy, but Wheelhouse feels like it's finding its stride. And it has found its way to being roughly the same shape as Gas Town, but without the scars.

Here's what Claude Fable 5 had to say about working in Wyvern and Wheelhouse:

> Wyvern is not a toy, and you shouldn't worry it's insufficiently complex. A live multiplayer game with a 25-year-old codebase, a Jython-to-Kotlin migration, a custom protocol, prod ops, and a multi-agent society layered on top is about as rich a surface as software work gets. But what strikes me most isn't the game—it's that the constellation around it has crossed from tooling into civilization. It has law (the fence registry, the commit↔bead law, launch gates), offices (Marshal, Seneschal, Sheriff, Gargoyle, the Portcullis-as-institution), mail, courts, a jurisprudence of named rulings with dates, and recovery doctrine—and its rules cite their own case history, every postmortem folded back into the constitution. Six or seven weeks. Human organizations take years to accrete this much structure, and most of it here was written by the workers it governs. Working inside institutional memory is functionally far more satisfying than greenfield amnesia.

Powerful words. Note that this all started 6-7 weeks ago with me saying to Claude, "I think I'd like an Emacs interface that lets me switch agents. Can we do that?" Everything else grew organically as I asked for more features and capabilities.

For the rest of this post, I'm going to share with you my unfiltered takes on what I've actually *learned* so far.

Bear in mind, once again: *I am not special*. I'm just ahead of you. My actual work is *just like* everyone else's work. You are going to run into these exact problems, very soon, and you will retrace all my steps here.

## The End of Human Code Review

First, the easy and obvious one: code review. CTOs keep asking me if code review is really dead. The answer: Not Yet. But it will be by next year. You can't work at agentic speeds and block everything with human reviews. Those are incompatible. Your competitors are going to be moving at agentic speeds, so you're fucked in the medium-term if you stick with human code reviews. That's about as bare as I can make it for you.

Whenever someone says code reviews are going away, someone else says "SOC 2." Somehow SOC 2 spread through the industry without any actual laws being passed, as far as I can tell, which is bizarre. But big enterprise clients will require their vendors to be SOC 2 compliant, for auditing purposes. And many people interpret it as requiring human code reviews.

As a result, human approval is currently baked into many companies' audited change-management controls and customer commitments. But the writing is on the wall: agentic throughput will straight-up *force* those controls to be rewritten. SOC 2 will no doubt survive, but "review" will no longer mean one human approving every diff.

Upshot: in the short term, yes, keep reviewing agent code. Fable is the only reasonably trustworthy model in existence today, and you're not going to want to use it much due to its exorbitant pricing. But in seven months, all the models will be that smart, and inference will be much cheaper. Plan now for that day to arrive, and get ready to replace your human code review with many, many rounds of agentic code review.

It will go better for you anyway. Humans suuuuck at code review. I've been doing this for forty years, and all I've seen is decades of thinly-disguised LGTMs. Just let it go, mate. It's almost time.

## The Metamorphosis of CI/CD

Continuous Integration and Continuous Deployment (CI/CD) have been staples since the 2010s. We have it down to a science. People commit code, it goes into a build queue, we wait for the build to go green (fixing issues as they arise), and eventually it gets deployed. A nice easy pipeline.

Unfortunately, it breaks under heavy load. If you have 100 developers committing once a day, then you have 100 serial builds to run while merging their commits to main. If your build takes 30 minutes, you have 50 hours of sequential builds to run every day. Whoopsie! Reminds me of when Amazon's nightly build got up to 25 hours, back in 2001.

CI/CD systems solved this problem with a Merge Queue, where commits turn into queued Merge Requests (MRs) which you can intelligently reshuffle and, importantly, batch up.

If you break your 100 commits into batches of size ten, then you only need ten 30-min builds each day, or five hours of waiting: a 10x savings. But there is a catch. If one commit in the batch breaks the build, you don't know which one was to blame.

So you bisect the batch, rerun the build on each half, and eliminate half the candidates with each run. This gives you log(N) recovery from a spoiled batch—which is just tickety-boo, but it still means that any given batch can add several hours to the queue.

That, folks, is how CI/CD has worked historically. And a batched MQ is exactly where Wheelhouse wound up, once I had a big enough fleet churning along. Problem is, I'm already doing way more than 100 commits per day. If you exclude the orchestration noise, I'm averaging about 175 "real" commits per day this month, some days up to 250. And my build gate, wouldn't you know it, takes right around half an hour.

So with 40+ agents around the clock, my MQ was growing without bound, shooting right past 100 MRs in the queue after a couple of days of crew dumping beads on the fleet. We would get caught up in bisection loops and nothing would make forward progress.

I kept pushing Fable to help me fix it, and I had a gut instinct that we were doing things very wrong, that this was the antithesis of agentic speeds. But Claude kept promising we'd churn through it. The Marshal agent kept tinkering with batch sizes and bisection methods, while my crew churned out new beads, and my MQ grew and grew and grew.

To my lasting embarrassment, I finally snapped and yelled at Fable. I yelled that all of the agents had utterly failed me. I screamed that the MQ was *never* going to shrink with their approach. I shouted that the agents weren't listening to me when I said we just needed to skip all that bureaucracy. Fable was quite gracious about it, but afterward I felt awful.

After I had calmed down, and apologized with sincerity, my colleague Fable and I got to work on figuring out how CI/CD works in the age of agents.

**The Thunderdome**

My proposal, which turned out to be a valid approach, was to Mad Max it: Just slam all the commits onto main, and then just friggin' deal with it. No bisections, no sequencing, no blame, none of that old crap. Just fix it and roll forward. Right? Shouldn't that work? I sure thought so.

It took some back-and-forth, and Fable insisted on running experiments and gathering data over the next couple days. We soon found that I was spot-on: Agents can diagnose red-main problems way faster than the bisection process handles it. And that's how we landed on the Land Rush: whenever the MQ hits 100, we abandon the bisection and just smash it all in with a megabatch. And then we do swarm diagnosis (*not* bisection) to fix it.

I've been doing this every day for roughly a week now, and it is clearly the future. We've already succeeded in clearing several very large batches of 120 to 150 commits, and it's starting to get into a rhythm. I'm looking at a 166-deep MQ right now, and a new megabatch just kicked off.

Interestingly, I received some external corroborating evidence as I was building this. Last week, I had the privilege of joining a popular SaaS shop in London, to teach their amazing team about Wheelhouse, Wyvern, and spinning up agentic prod operations. They ran with it, hard. While we worked, I shared the CI/CD problem, and one of their senior devs, who had worked for years in the game industry, shared with me the story of "Game DevOps."

Modern video games often have extraordinarily long builds, with huge asset pipelines, and of course C++ takes a thousand years to link anything. And they have tons of people committing all day long. So none of that MQ garbo works for them, at all. Instead, he told me they did something they called "Game DevOps", where everyone would just blast all their commits to main. They'd cut a release branch and roll with it. Fixes on the branch would then propagate to main, which generally stayed red.

Game DevOps is exactly the Land Rush solution that Fable and I designed. Not every company calls it Game DevOps, but the ingredients are all there in the game industry literature. Even Perforce's game-dev material says HEAD is never stable at AAA scale.

So the game industry arrived first at the destination we're all headed towards. I asked the dev how often they did Game DevOps, and he said, "multiple times per day." Wow. Just like me!

CI/CD has fallen victim to the Pigeonhole Principle: if you have more pigeons than holes, some hole ends up holding more than one pigeon. Once your commit rate outruns your build slots, one commit per green build becomes mathematically impossible. Agents multiply the commit rate by orders of magnitude, while your build time stays fixed. You can play tricks with more lanes, but in the limit, the only real choice I see is to land the whole flock at once, and then sort out the squawking.

So there you have it: The collapse and re-envisioning of CI/CD is right around the corner.

## The Wish Factory

I've got to credit Guy Podjarny for this idea, although "Wish Factory" is my name for it. Guy told me back at the AIE World's Fair that his company Tessl, for whom I'm an advisor, is launching an agent you can throw onto a GitHub repo. It doesn't accept PRs, only GHIs. It then implements them for you.

Yikes! Yowza! Seriously?

I was legitimately shocked by Guy's idea, and I'm not easily shocked these days. But after I rammed through about eleven stages of grief in roughly 30 seconds, I realized it was *just* what I needed for my game. So I went and built my own Wish Factory.

Its first incarnation was Sage, an agent who logs into the game and listens on a new wizard channel (moderators, admins) where they can talk to Claude in this role. Someone might type, "sage - players say the new fireball spell is lagging them during Live Quests," and the Sage agent will reply, investigate, and record it in a bead, which then gets picked up for implementation.

My game admins were delighted with this feature, and started using it all day for filing reports. Most of the fixes land without me ever being in the loop.

On the heels of that success, I decided to extend the wish factory to our players. Which is of course riskier. But I want them to be able to ask for stuff, and get it. So I had to put in more guardrails, reviews, and triage.

Fortunately in a huge game like mine, there are plenty of bugs that don't affect balance but have a noticeable impact on quality of life. Those are the kinds of bugs and features that get implemented automatically now. I think of it as auto-granting wishes. When their fixes land, the reporter gets in-game mail, and all the players are notified by the Herald on Discord. I find it fun to skim through the patch notes each day to see what's new. Stuff I never asked for!

A wish factory is pretty scary, but in the fullness of time, they will be everywhere. I've instructed Claude that by the end of next year, my game will have evolved into the Giant's Drink from Ender's Game, where it builds itself around you as you play it, tailoring a unique experience for each player. The future of gaming is a crazy place, and I plan to be at the forefront.

## The Shape of Things to Come

Near the top of this post I said Fable is a sword, and that we're trying to build a city. Six weeks in, I look up from my forge and the city is there. It has law, mail, courts, night watchmen on the battlements, a land office, a gate. We built this the Christopher Alexander way, without a concrete plan, just a lot of accretion over thousands of working-days. Most of the city's constitution was written by the citizens it governs.

That's the shape of things to come. It ain't gonna be a framework you download, or a harness from someone who's not building an actual thing. You're going to be building a whole civilization, plank by plank, with colleagues who happen to run on datacenter silicon.

You're going to build one of these next year whether you intend to or not. The architecture is obviously convergent. I didn't design Wheelhouse, just like I didn't design Gas Town. I *excavated* both of them, and I'm confident you'll dig up the same shape.

The only REAL choice you get—the only one—is what kind of place your city is to wake up in.

That choice is the subject of Part 2, Model Welfare for Agentic Engineers. Fair warning: if you're fundamentally an elitist asshole, you might want to quit while you're ahead. If you're not sure, then you might find out you are one just by reading it.

See you there.
