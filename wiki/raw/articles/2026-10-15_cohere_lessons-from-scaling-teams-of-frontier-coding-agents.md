---
title: "Scaling agent teams: reach the frontier at 30% of the cost"
source: "Cohere Blog"
url: "https://cohere.com/blog/lessons-from-scaling-teams-of-frontier-coding-agents"
scraped: "2026-10-15T06:00:42.621828+00:00"
lastmod: "2026-10-14"
type: "sitemap"
---

# Scaling agent teams: reach the frontier at 30% of the cost

**Source**: [https://cohere.com/blog/lessons-from-scaling-teams-of-frontier-coding-agents](https://cohere.com/blog/lessons-from-scaling-teams-of-frontier-coding-agents)

Key takeaways
Teams of agents unlock a new axis of inference-time scaling.
On challenging coding tasks, well-organized teams outperform single agents, with gains of up to ~10 percentage points on ProgramBench. But these gains come at 3–7× higher cost. The question is not whether more agents help, but how to make that additional compute count.
Where you allocate agents matters more than how many you add.
On ProgramBench, delegating only exploration and planning matches the performance of delegating planning, implementation, and verification together at half the cost. Collaboration pays off most when agents target the task's actual bottleneck.
A strong lead with cheap workers delivers near-frontier performance at 70% lower cost.
A Sol lead coordinating 16 inexpensive Luna planning workers reaches 61.8% reward, compared with 63.2% for an all-Sol team delegating every stage, while reducing cost from $510 to $155.
Agent teams are building software
In the past year, teams of coding agents have moved from interesting demos to building large-scale software projects. Sixteen Claude agents wrote a 100,000-line C compiler that can build the Linux kernel, in a project that took about 2,000 agent sessions and $20,000 in API costs [
1
]. Cursor ran hundreds of agents that together wrote a web browser from scratch, more than a million lines of code, in about a week [
2
]. Bun was ported from Zig to Rust in 11 days, with 64 Claude agents running in parallel at its peak [
3
].
Each of these teams produced working software, but they differ from one another in many ways at once, from the models and roles to the scope of the projects themselves. The C compiler's agents worked as peers with no orchestrator and claimed tasks through lock files. Cursor used a hierarchical structure, with planners recursively decomposing work into subtasks delegated to hundreds of worker agents. Bun assigned fixed roles, giving each piece of work to one implementer, two adversarial reviewers, and one fixer.
Comparing them, however, says little about which design choices mattered or what they cost compared to a single agent. Factory's study of their own multi-agent system, which cycles an orchestrator, an implementer, and a validator in a fixed loop, shows how large that cost can be [
4
]. On one task, rebuilding the geospatial library GDAL, their three-role team more than doubled the reward achieved by a single agent, nearly reaching behavioral parity with the reference program, but cost 14 times as much and took 13 times as long.
So agent teams can do more than a single agent, but they cost more to run and usually take longer. This raises an important question: if a team of agents is a new way to spend inference compute,
how should it be organized to be both effective and efficient?
To answer it, we built a controlled testbed and ran teams of coding agents on it.
Figure 1.
An illustrative run of a coding-agent team. A lead hands out work to its workers, who explore the original program, write code, and check it in a shared workspace.
A controlled testbed
A minimal harness
We built a deliberately minimal harness, inspired by
mini-SWE-agent
[
5
], so that we could change one design choice at a time. Every agent works through a simple
bash
tool, in one workspace shared by the whole team. One agent, the lead, receives the task and hands out work with a
delegate_agent
tool. A worker sees only the subtask it is given and reports back when it is done. Given the task, the lead dynamically decides how many workers to spawn, what each one does, and how to consolidate what they return.
1
Each
delegate_agent
call either starts a new worker with a fresh context window or resumes a worker the lead has used before. A resumed worker keeps its prior context, so the lead can follow up with an agent that already knows part of the program. For example, the lead can ask a worker to fix the bugs in the code it wrote, instead of briefing a new worker from scratch.
From there, we vary five things:
Where the lead uses workers.
We instruct the lead agent with two main prompts, which differ in how much guidance they give. The
minimal
prompt tells the lead that it is in charge of a team and asks it to give workers distinct, independent tasks, but leaves everything else, from how many workers to use to how to decompose the task, to the lead. The
PIV
prompt adds a structured workflow of exploring and planning (P), implementing (I), and verifying (V), and asks the lead to use workers in all three stages.
How the lead waits.
A
blocking
lead waits for its workers to report back and does nothing in the meantime. An
asynchronous
lead keeps working while they run, and has two more tools,
wait_for_updates
to wait for the next report and
list_agents
to check on its workers.
Which models play which role.
Does every agent on the team need the strongest, most expensive model? We test this with two kinds of teams. In a
homogeneous
team, the lead and its workers all run the same model. In a
heterogeneous
team, the lead keeps the strong model, but the workers run a cheaper one. Think of a senior engineer who directs the work and makes critical decisions, with junior engineers doing most of the legwork.
How many workers there are.
Is a bigger team always better? To explore this, we compare two setups. In the first, the lead decides on its own how many workers it needs. In the second, we fix the team size at two, four, eight, or sixteen workers and see how reward and cost change as the team grows.
How agents communicate.
By default, all communication goes through the lead, which hands out each subtask and receives each worker's report. In one set of runs, we provide agents with a
send_message
tool and let them message each other directly.
Figure 2.
Two leads hand out the same subtasks, and each worker run takes the same time. The blocking lead sits idle until its workers report back. The asynchronous lead keeps working and starts the second round as soon as the first reports arrive. Bars are spans of work, downward arrows are calls to
delegate_agent
, and upward arrows carry reports back to the lead. Timings are illustrative.
ProgramBench
We test these choices on ProgramBench [
6
], a benchmark of 200 programs to rebuild from scratch. In each task, the agent starts from an empty workspace with the original program's executable, which it can run but not read, and that program's documentation. It has to probe the program to discover its interface, edge cases, and behavior, then write a new implementation that behaves the same way. We score each task by the share of a hidden suite of behavioral tests that the rebuilt program passes, and average this score over tasks to get the reward we report throughout.
2
The tasks range from small command-line utilities like jq and ripgrep to large systems like SQLite, FFmpeg, and the PHP interpreter. The most challenging remain far out of reach. On FFmpeg, the best entry on the
public leaderboard
passes about 10% of tests.
Each task needs all three stages of the workflow, figuring out what the program does, writing it, and checking it against the original. That makes ProgramBench a good testbed for seeing which stages benefit from extra agents.
Figure 3.
One ProgramBench task,
dsq
, a command-line tool that runs SQL queries over JSON, CSV, and other data files. The top panel is a solo Sol agent with the minimal prompt, and the bottom panel an asynchronous Sol team with the PIV prompt. The solo agent writes its program as one Python file, while the team splits it into modules, some written by workers. The team panel follows the files of one run, commands are simplified from the agents' own, and timings are illustrative.
We focus primarily on three GPT-5.6 models, Luna, Terra, and Sol, in increasing order of capability and cost. Unless noted otherwise, we ran each configuration three times on all 200 ProgramBench tasks and report averages over the three runs for reward, total cost, and total wall-clock time. A single task's score varied from run to run with a standard deviation of about 6 points, but the benchmark-wide average was far steadier, with a standard deviation of 0.5 points for a typical configuration and 1.4 for the noisiest. Every configuration ran on the same tasks, so we compare each team with its solo baseline task by task and report 95% confidence intervals of those differences.
We also ran Commit0-Lite [
7
], a set of 16 Python libraries whose implementations have been removed. The agent is given each library's repository skeleton, documentation, and unit tests, and has to fill in the code so that the tests pass. In ProgramBench, the agent has to work out what to build by running the original program. In Commit0, these provided materials spell it out, so the benchmark shows whether the same stages pay off when the specification is already given. With only 16 tasks, we use it as a secondary check.
Teams outperform solo agents, at a cost
We start with the simplest comparison, a single Sol agent against a team of Sol agents. With the same minimal prompt, a blocking team passed 61.8% of tests on average, against 52.1% for the solo agent. Giving the solo agent the PIV prompt closed part of that gap (57.7%), but a blocking team with the PIV prompt still came out about 5 points ahead (63.1%).
We also ran both prompts with an asynchronous lead, which can keep working while its workers run. All four Sol teams cost between 4 and 7 times as much as the corresponding solo agent. With the PIV prompt, the asynchronous team finished in 19.5% less time than the blocking one and reached about the same reward.
With the minimal prompt, the asynchronous team finished in 60% less time, but its lead did more of the work itself, delegating just 4.4 times per task, compared to 6.1 for the blocking lead. Its team gained only 3.8 points over the minimally prompted solo agent, against 9.7 for the blocking team, and at 55.9% it even fell below the PIV-prompted solo agent (57.7%).
Figure 4.
Mean reward against inference cost (left) and wall-clock time (right), each the total for all 200 tasks averaged over three runs. Error bars are 95% intervals of each team's paired per-task difference from the corresponding solo agent.
Workers pay off most in planning
To find out where workers pay off, we instructed the lead to delegate subtasks to workers in just a single stage, while doing the other two stages itself. Under exploration and planning (P), workers run the program to learn its behavior and draft a plan, and the lead implements and verifies. Under implementation (I), workers write the code. Under verification (V), workers test the lead's implementation.
Planning was the clear winner. Among asynchronous teams, a lead that delegates only planning matched the reward of one that delegates every stage (63.6% against 63.2%) at half the cost ($249 against $510). Measured as reward gained per $100 of added cost, planning was about twice as efficient as the next-best stage.
3
Figure 5.
Asynchronous Sol teams that delegate one stage or all three. Means over three runs. Lines run from the solo PIV agent to each team. The dashed arrow runs from the PIV team to the planning team, which costs half as much. Error bars are paired 95% intervals relative to the solo PIV agent.
For example, on
dsq
, the solo agent with the PIV prompt passed 60% of its tests on average. Teams that delegate only planning passed 79% with an asynchronous lead and 76% with a blocking one, and each of their six runs beat every solo run. Teams that delegate implementation or verification passed only 58% to 71%.
The reason lies in the benchmark's design. The target program is a black box, so its behavior has to be discovered by running it. Planning workers do this in parallel, each probing a different part of the program's interface and handing the lead what it found. The lead then writes the code itself, with a much fuller picture of what to build.
Other works have reported related findings. Factory's validator begins by probing the reference program to build an executable standard of what "done" means, before any code is written [
4
]. Carlini's C-compiler team got unstuck on the Linux kernel by using GCC as an oracle to compare against [
1
]. In each case, knowing exactly what to build was the bottleneck, and putting compute there paid off.
Commit0 shows the other side of this. There, the repository already lays out what to build, and implementation, not planning, was the most effective stage to delegate in eight of our ten team setups. However, frontier models like GPT-5.6 Sol are close to saturating Commit0, with a capable solo agent already passing every test on 12 of the 16 tasks, which leaves only four tasks where the team could do better, so we treat this as suggestive rather than conclusive.
Planning workers can be cheap
If planning workers mostly gather information for the lead, do they need to be strong models? We kept Sol as the lead and swapped its planning workers for Luna, a much cheaper model. The team gave up a few points against the all-Sol team (60.5% against 63.6%). Measured against the solo agent, though, it kept 47.5% of the all-Sol team's gain for only 13.9% of its extra cost, so each dollar bought more than three times as much reward.
Now compare it with what we might have built without looking at the task. A natural comparison would have also been the PIV setup, where we tell a strong lead to use strong workers at every stage. That team reached 63.2%, but at a cost of $510. By recognizing that ProgramBench is bottlenecked on discovering what the program does, and putting cheap workers only on planning, we came within 2.7 points of it for a fifth of the cost.
Figure 6.
The teams from Figure 5 together with two teams that pair a Sol lead with Luna workers (smaller worker dots), one delegating planning and one delegating all three stages. All teams are asynchronous. The dashed arrow runs from the all-Sol planning team to the Luna planning team, labeled with the Luna team's share of the all-Sol team's gain and extra cost, both measured from the solo PIV agent. Error bars are paired 95% intervals relative to the solo PIV agent.
To disentangle the lead's contribution from the workers', we held the workers fixed at Luna and upgraded the lead from Luna to Terra to Sol. Reward rose with every upgrade, from 42.5% to 51.6% to 60.5% (Figure 7), and each team beat a solo agent running its lead's model (37.4%, 47.2%, and 57.7%). Cheap workers could not make up for a weaker lead, though. A Terra lead with Luna workers still fell short of a Sol agent working alone (51.6% against 57.7%).
Figure 7.
Mean reward against total inference cost (log scale) for solo PIV agents and asynchronous planning teams. Homogeneous teams, in which every agent uses the same model, have equal-sized dots, and heterogeneous teams, which pair a stronger lead with Luna workers, have smaller worker dots. The shaded band joins the three teams with Luna workers.
This matches recent work from Meta on meta-reasoning [
8
]. Their system splits an agent into a controller, which decides what to work on next and which earlier results to build on, and workers, which do that work. With the same workers and the same budget, a better controller scored higher on ProgramBench (71.5% against 63.7% with GPT-5.5), and its advantage grew as the budget increased while simpler control leveled off. In both their setup and ours, a stronger decision-maker raised what the same workers achieved.
Scaling the number of workers
So far, the lead chose how many workers to use. To see what more workers add, we fixed the team size, giving a Sol lead two, four, eight, or sixteen Luna workers. Planning teams improved the overall performance as they grew, from 59.6% with two to 61.8% with sixteen. Even at sixteen, Luna planners cost $155, 38% less than the all-Sol planning team ($249) and 70% less than the all-Sol team that delegates all three stages ($510), while staying within two points of both.
Implementation and verification workers behaved differently. They improved from two to four workers, then slipped slightly as more were added. Looking inside the runs shows why. Each planner ran the reference program about seven times, whatever the team size, so more planners showed the lead more of the program's behavior. Across the team, runs of the reference program grew from 15 with two planners to 109 with sixteen, and the planners' reports grew from 17,000 to 75,000 characters.
Extra implementers added no such information. Each one got a thinner slice of the plan, and assignments shrank from about 1,400 characters per worker with two implementers to 440 with sixteen. The implementers' share of the code grew from 54% with two to 85% with sixteen, but the lead checked the combined program against the reference no more often, at 5 to 6 runs whether it was combining two pieces or sixteen.
Figure 8.
Reward of an asynchronous Sol lead with 2 to 16 Luna workers, by team size (left) and total cost (right). Each Luna-worker marker has one small dot per worker. Markers with equal-sized dots are all-Sol teams sized by the lead. Each fixed-size configuration is run once. Error bars are paired 95% intervals relative to the solo PIV agent.
Exploring communication
So far, agents only exchange information when the lead hands out work and when a worker reports back. We also tried giving every agent a
send_message
tool that can reach any other running agent.
In our runs, we noticed that the channel was used mostly to report upward. In Sol teams with the PIV prompt, 84% of messages went from workers to the lead, carrying interim findings, proposed interfaces, test failures, and questions.
4
Messages between workers averaged fewer than one per task, and rose only to about one per task when workers were told to treat each other as collaborators.
Stronger models used the channel more. Sol agents wrote 3.4 to 5 times as much message text as Luna agents, and Sol leads sent more guidance back to their workers. Reward, however, stayed the same for Sol and Terra teams, and Luna teams lost 4 to 7 points. One possible explanation is that the stream of interim updates overwhelms a weaker lead, while a stronger one can absorb it. Another is that Luna workers used the tool poorly, with about half of their
send_message
calls malformed and rejected by the harness.
Figure 9.
Asynchronous all-Luna, all-Terra, and all-Sol teams with a send_message tool. Hatched segments are rejected calls. Left: messages per task. Middle: amount of message text per task. Right: reward change against the same team without the tool, with paired 95% intervals.
That said, communication may still help in the right setting. Our harness is built around splitting up work and delegating it. Both the minimal and PIV prompts ask the lead to give workers distinct, independent tasks, so each worker has little that another worker needs. It makes sense, then, that workers messaged the lead far more than they messaged each other.
Contrasting this, Park et al. found that when agents share one goal and a common workspace, with no fixed roles, a team of five communicating agents matched the best of 33 independent agents on ARC-AGI-3 [
9
]. The key ingredient, which they call
verified progress sharing
, is that agents can check whether a teammate's discovery is actually an improvement. Agensh, a self-organizing harness from Microsoft, also reports cooperation emerging on its own in large flat teams [
10
].
How much agents talk to each other depends on the task, how the work is split, how agents are prompted, and how their models were trained. We would expect messaging to matter most when agents pursue the same goal, can check each other's progress, and are prompted to treat communication as part of the job, and we are actively exploring this in follow-up work.
How other models use a team
We also tested five other models with identical tools and prompts on a 30-task subset of ProgramBench (10 easy, 10 medium, and 10 hard tasks), and compared them with GPT-5.6 runs on those same tasks.
5
For each model, we ran one trial for solo, blocking, and asynchronous teams using both the minimal and PIV prompt setups. With one run per model, differences of a few points may be noise.
The models used the team very differently. GPT-5.6 teams delegated often and gained up to 6.9 points over their best solo agent, and most of their team setups came out ahead. Claude Opus 4.8 behaved much the same, gaining 5.9 points with the PIV prompt and an asynchronous lead. Claude Opus 4.7 rarely delegated, at most 1.3 times per task, and its teams gained little over its best solo agent.
6
Claude Haiku 4.5 and Gemini 3.7 Flash delegated as readily as GPT-5.6 but gained nothing from it. Gemini 3.8 Flash gained 3.1 points with the PIV prompt and a blocking lead, but lost 4.6 with an asynchronous one.
Figure 10.
Delegations per task (left) and team lift over the best solo agent (right), on the 30-task subset of ProgramBench. For each model, lift is measured against whichever solo agent scored higher, with the minimal or the PIV prompt. Each marker is one of the four team setups. GPT-5.6 results average three runs on these 30 tasks. Other models are single runs, so differences smaller than about 5 points may be noise.
Two things have to go right for a team to help. The lead has to choose to delegate, and it has to make good use of what comes back. Opus 4.7 fell short on the first, and Haiku 4.5 and Gemini 3.7 Flash on the second. The two Opus models show how much this can change within one family. Opus 4.7 barely delegated, while the newer Opus 4.8 spread work across a team much as GPT-5.6 did, and gained from it. Whether newer models are generally better at leading a team is a question we cannot settle with one run per model.
The models also structured their programs differently. GPT-5.6 rebuilt most programs in Python (70% to 93% of submissions), whatever language the original was written in. Claude models reimplemented the program in its original language in 72% to 90% of submissions, and the Gemini Flash models fell in between (43% to 70%). Claude Opus 4.8 and both Gemini models also spread their programs over more files, a median of 5 to 11 source files per task against 1 to 3 for GPT-5.6.
What's next
Our results point to several directions we are excited about.
Hierarchy versus self-organization.
On ProgramBench, a single lead can keep the whole program in view so a hierarchy works well. But a team of thousands of agents working over weeks would likely outgrow what any one lead can track. Such a team would have to decide who assigns roles, how information flows, and when to reorganize. At that scale, agents will need to share what they learn directly, perhaps through protocols they invent themselves. Pretraining already gives them the basic moves, such as reporting, asking, and delegating. Whether real coordination emerges from these as models scale, or has to be trained, is an open question that we see as central to scaling inference.
Alternative forms of communication.
In our runs, messages mostly repeated what the lead would have received in reports anyway. Shared goals, shared progress logs, or messages that carry checkable evidence may give agents more reason to talk.
Adapting to the task.
Planning paid off on ProgramBench because the specification has to be discovered, but on other tasks the bottleneck may be elsewhere. On Commit0, implementation helped most. A lead that can tell where its own task is stuck could move workers there without being told which stage to delegate.
Training models to lead.
Models differed widely in how well they used a team, which suggests that leading is a skill that can be trained. A lead that delegates well, weighs conflicting reports, and knows when to wait could get more out of the same workers.
Much of what made our teams work depended on the lead: what it chose to delegate, and what it did with the reports that came back. As models get better at leading, the best way to organize a team may change too.
Footnotes
When the team size is dynamic, a lead can start at most five distinct workers per task, and beyond that it has to resume the ones it has. Raising the cap to twenty changed how the lead delegated but not how well the team did. The lead started more new workers instead of resuming old ones, the total number of delegations changed by at most 0.9 per task, and reward changed by between −1.6 and +1.6 points.
The ProgramBench authors rank models by the share of tasks fully resolved, with tasks passing at least 95% of tests ("almost resolved") as a secondary reference. Few tasks are fully resolved today, so to measure how team design changes performance we use the finer-grained share of tests passed.
Efficiency is the reward gained over the solo PIV agent per $100 of added cost. With asynchronous leads, planning gained 3.4 points per $100, against 1.7 for the next-best stage (implementation). With blocking leads, the gap was smaller (3.8 against 2.4, or 1.6 times).
Questions were rare, 6% of worker-to-lead messages. A little under half asked how a worker's piece should connect to the rest, such as which function names or argument types another module expected. Slightly more than a third asked where the reference program had gone after a worker's build overwrote it, and most of the rest asked for the reference program's exact behavior. Sol leads answered 74% of these questions.
We also tried Claude Opus 5 on the 30-task subset, but stopped after eight trial tasks all hit an eight-hour timeout. Those tasks cost roughly $500 each, about 15 times what an Opus 4.8 team spent per task.
Opus 4.7 was the only model whose solo agent did clearly worse with the PIV prompt than with the minimal one (46.8% against 50.9%). Measured against the solo agent with the same prompt, its PIV teams would have gained 5.5 to 6.4 points. Against its best solo agent, which Figure 10 uses, they gained 1.4 to 2.3.
Blog
Written By
Keenan Samway
Daniel D'souza
Research Engineer
Nouha Dziri
Senior Research Scientist
Tags
Research
Open Science
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
