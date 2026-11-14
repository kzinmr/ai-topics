---
title: "After 600 experiments, here's what I discovered about JEPA world models"
url: "https://haddyalchaer.com/jepa"
source: "haddyalchaer.com (Haddy Alchaer)"
date: 2026-11
fetched_at: 2026-11-14T11:12:00+00:00
tags: [blog, raw, primary-source]
note: "HN item 50487185 (264 pts, 2026-11-13). Author handle @haddyalchaer."
---

After 600 experiments, here's what I discovered about JEPA world models — Haddy Alchaer 
 Haddy Alchaer 
 World models · JEPA · Planning After 600 experiments, here's what I discovered about JEPA world models By Haddy Alchaer · November 2026 
 Solving long-horizon tasks without any extra training 
 0 / 24 on target · step 0 Vanilla LeWM can be augmented to solve long-horizon physics tasks on out-of-distribution goals. This method uses transformations on a memory graph to generate on-the-fly subgoals without any additional training. Shown here are some of the hardest tasks it solved. 
 There's a big debate in AI right now about what a world model should be. Most of the attention goes to generative world models, which predict the future by generating it, usually in pixels. Many scientists, including Yann LeCun, argue that this is wasted effort. Most of the pixels don't matter for deciding what to do, and many of them can't be predicted at all. [1] 
 The proposed alternative is JEPA, the joint-embedding predictive architecture. It has three parts: an encoder, a predictor and a planner. The encoder turns each frame of observation into a learned embedding, a compact vector that describes the scene. The predictor takes that embedding plus an action and predicts the embedding of the next frame. The planner then tries hundreds of action sequences inside the predictor and picks the one whose predicted end state lands closest to the embedding of the goal. The whole loop runs in embedding space, so the model only has to learn the parts of the scene that are important for deciding actions. 
 The three parts of a JEPA world model. 
 This year a team including LeCun released LeWM [2] , a JEPA world model whose main benchmark is Push-T [3] , a simulation where a robot pushes a gray T-shaped block across a table until the T sits in the green target position shown in a goal image. I've spent the last few months running 600 experiments on it. 
 A goal image from Push-T The planner is given an image like this one and has to make the scene match it. The gray T is the block, the blue disc is the robot's pusher, and the green T is the goal position painted on the table. One detail in this image turned out to affect the success rate more than replacing the predictor with simulated physics. 
 The first thing I wanted to know was how much LeWM is held back by its predictions, so I started by swapping out the predictor for the simulator's perfect physics, while keeping everything else the same. I then gave both versions long-horizon tasks, with the goal 75 steps away, along with the same subgoals: frames from an expert demonstration, one every 25 steps. Vanilla LeWM succeeded 78% of the time. The version with true physics succeeded 77%. Along the kinds of paths it was trained on, LeWM's predictions are already as good as perfect physics for planning. 
 Success on 250 long-horizon tasks 78 % 
 Vanilla LeWM learned predictor ≈ 77 % 
 LeWM real physics the simulator itself 
 That means the next gains for a JEPA world model come from how the trained architecture is used, and that's where most of my 600 experiments went. 
 Without retraining the model once, I found four new planning methods. The first two together took LeWM's success rate on long-horizon tasks from 22% to 85%, about the same as a planner that is handed the ideal subgoals from an expert demonstration. The other two methods extend LeWM to harder goals, and one of them, a single change to how the goal is scored, raised the success rate by 60 points, three times as much as swapping in perfect physics did. 
 1. Plan through subgoals 25 steps apart 
 Used exactly as published, LeWM succeeds on 22% of long-horizon tasks, where the goal is 75 steps away. [2] When the goal is 25 steps away, it reaches it 89.7% of the time, within a point of the exact-physics version at 90.5%. 
 So the model is accurate over 25 steps and struggles over 75. The usual explanation is that small prediction errors compound over a long plan, which would call for a better model. I tested that against the alternative on the same 250 long-horizon tasks. 
 250 long-horizon tasks, goal 75 steps away LeWM, all 75 steps at once as published 
 22% Exact physics, all 75 steps at once the simulator itself 
 42% +20 LeWM given a new subgoal every 25 steps same model, shorter hops 
 80% +58 0 25 50 75 100% 
 Exact physics added 20 points. Splitting the task into 25-step segments, each the length LeWM already handles almost perfectly, added nearly 60. LeWM's useful planning horizon is about 25 steps, so it was clear that the way to go further is to chain segments of that length together. 
 LeWM's planning horizon is about 25 steps Plan all 75 steps at once ... one search, far goal 22% A subgoal every 25 steps ... three short searches 80% Chaining 25-step searches through subgoals keeps every search inside the range where LeWM is accurate. 
 This is hierarchical planning: a high level picks subgoals and a low level reaches them. It's widely considered one of the main open problems for world models, and on Push-T it's worth three times as much as swapping in perfect physics. 
 Extra search doesn't substitute for it. Running the planner four times and keeping the lowest-cost plan took four times the compute and added less than one point, because the four runs almost always succeeded or failed together. 
 The subgoals in this experiment came from an expert demonstration, which a deployed robot won't have. The second method removes that dependence. 
 2. A latent memory graph with a cost on every jump 
 LeWM was trained on expert demonstrations of the task, and its encoder can embed every frame of them, giving about 460,000 embedded states that I connected into a graph. Each state links to the states that follow it in its own demonstration, and to states in other demonstrations that are close in embedding space. To solve a long-horizon task, the planner searches this graph for a path from the current state to the goal and uses the states along that path as subgoals. 
 This only works if distance in embedding space means something physical, and it does. Take one subgoal the robot can reach within 25 steps and one it can't, and LeWM's embedding distance ranks the reachable one as closer 87% of the time. So the embedding space doubles as a map of what the robot can reach. 
 The first version had a flaw. A jump between nearby states in two different demonstrations cost the same as a real step, so the search strung jumps together into paths the block could never follow (318 of 1,015 plans tried to use six or more jumps). The fix was adding a cost on every jump between demonstrations in the graph. Using nothing but LeWM's own embeddings of past demonstrations, success on the same 250 long-horizon tasks (goal 75 steps away) went from 62% to 85%, which is the same score received by the planner using expert subgoals. Can't get much better than that, right? 
 Planning through a memory of demonstrations start goal 
 Jumps are free · 8 jumps · 62% 
 Each jump has a cost · 1 jump · 85% Each thin path is one demonstration. With free jumps, the shortest route hops between demonstrations into a path the block can't physically follow. With a cost per jump, it stays on them. 
 The standard Push-T test is easier than it looks 
 The caveat is that the standard test takes a demonstration, starts the robot partway through it, and sets the goal a fixed number of steps further along the same demonstration. That's a reasonable design, but in Push-T every demonstration ends with the block in the same place. So every test goal sits on a path that demonstrations already travel, heading for the spot they all end at. For 84% of the standard test's goals, the memory graph already held a nearly identical state from another demonstration. 
 demonstrations, all ending in about the same place 
 goals in the standard test 
 goals from other demonstrations The standard test picks its goals along these streams. The harder test asks for goals like the orange ones, which no single demonstration leads to. 
 The usual sample is also small. On the official 50 episodes, LeWM succeeded 68% of the time with the goal 50 steps away. On 250 fresh episodes drawn the same way, it succeeded only 44%. Changing nothing but the planner's random seed flipped 38 of 250 episodes between success and failure. 
 That's where I decided to build a harder test, where each task takes its start from one demonstration and its goal from another, so the robot has to travel between states that no single demonstration connects. It only counts as a success if the block stays on target for the last 10 steps. Under these rules the memory-graph planner succeeds 75% of the time on standard tasks and 45% on the new ones. The third and fourth methods I found work on that gap. 
 3. Fill gaps in memory with transformed memories 
 A memory graph is only as good as its coverage. When I deleted every stored state near the goal, success fell from 93% to 32%. 
 Push-T has a useful symmetry here. The physics of pushing a block doesn't change if you shift, rotate or mirror the whole table. So when the graph has no states near a goal, it can take demonstration segments from elsewhere, transform them to fit the gap, and plan through those. With these transformed segments, success came back to 85%. They also stretch a small memory a long way (a graph built from 1% of the demonstrations plus transformed copies did about as well as one built from 10%). 
 Filling a gap in memory with transformed demonstrations a demonstration segment from elsewhere the same segment, shifted, rotated or mirrored Block reached its target, 250 long-horizon tasks (goal 75 steps away) 93% full memory 
 32% states near the goal deleted 
 85% gap filled with rotated and mirrored copies 
 On the harder test, transformed segments raise success from 45% to 56%, and they help most where demonstrations are thinnest. When the goal lies in the direction the demonstrations flow, the memory-graph planner already succeeds 69% of the time. When it lies the opposite way, plain memory gets 27% and transformed memory gets 46%. 
 Harder test, by where the goal lies about 83 tasks per row Goal lies with the flow of the demonstrations 
 69% Goal lies across it 
 39% 54% Goal lies against it 
 27% 46% 0 25 50 75 100% success rate plain memory with transformed segments 
 4. The cost was “wrong” 
 I also built an interactive demo where I could place the block anywhere and pick any goal. A goal has to be an image, and an image of the scene has to show the pusher somewhere, so I placed the pusher just behind the goal. In one run, the robot pushed the block to within 14 pixels of the target, close enough to count as solved. Then it pushed the block away from the goal, and kept moving the pusher toward where the pusher was in the goal image. 
 The goals in the harder test are frames from expert demonstrations, so each one also shows where the expert’s pusher happened to be at that moment. A planner that compares its prediction with the whole goal image is trying to put the pusher there too. 
 To measure how much this matters, I took the model out of the question. I ran the exact-physics planner twice on the same 50 tasks from the harder test, and the only difference was whether its cost included the pusher’s position as well as the block’s. 
 Block held on target, same 50 tasks exact-physics planner Block and pusher 9 / 50 
 Block only 39 / 50 
 success with either cost 30  succeed only without the pusher 0  succeed only with the pusher included 
 Thirty tasks went from failure to success when the pusher was left out, and none went the other way. A split like that happens by chance about twice in a billion. The physics here is from the actual simulator, not predicted, so the 4x in success comes from how the goal was created . 
 The planner that scored the pusher did exactly what it was asked. On the 30 tasks that flipped, it got the pusher to within half a pixel of where the goal image put it, and lost the block on the way. Placing both the T and the pusher in the exact goal position is a much harder problem to solve. 
 Pusher included vs. not 
 Cost compares the block and the pusher 
 Cost compares the block only 
 target for the block where the goal image put the pusher 
 Replay 
 But LeWM can’t simply be told to ignore the pusher. It scores a plan by the distance between two embeddings, and its embedding of a goal image holds the block and the pusher together, with no part labeled “pusher”. So, as a test, I measured how far a planner gets by searching over the pusher instead. It compares each prediction against 16 versions of the goal image, all with the block in the same place and the pusher moved to positions taken from stored demonstrations, and keeps the closest match. That doubled LeWM’s success on the harder test, from 11% to 23%, without retraining. 
 Sixteen versions of one goal A predicted end state 
 16 copies of the goal with the pusher moved, and the closest one sets the cost 
 This applies to any robot because a goal should just be a set of end states, not a copy of an image. “Put the cup on the shelf” is solved wherever the robot’s arm ends up, but a goal image picks one arm position and makes the planner match it. A good goal accepts every end state that solves the task, and still includes what the task needs from the robot, like coming to rest at the end. 
 The good news is that large sets of demonstrations already contain many real frames of the same object in the same place, each with the robot somewhere different. Scoring a plan against the closest of those goals allows for a larger set of valid end states to plan for. 
 What comes next 
 None of these four discoveries change the model's weights. They apply to LeWM as published, and they should carry over to larger JEPA world models that plan the same way, at no extra training cost. 
 The biggest open problem remaining is generalizing to tasks that don't have perfect demonstrations. On the harder Push-T test, the best planner holds the block on target 56% of the time, and most of the remaining failures are goals that run against the direction of the data. Closing that gap needs a higher level that can propose its own subgoals beyond the demonstrations, and do it better than today's learned hierarchies like H-JEPA [4] , which so far match or slightly beat flat LeWM on Push-T. 
 Hierarchical subgoal planner on top of LeWM 
 demonstrations in memory subgoals taken from memory a goal beyond the data 
 Going in, I assumed LeWM's predictions would be the bottleneck, but a JEPA small enough to train in a few hours already predicts about as well as the simulator itself, and there are several gains that can be achieved simply by changing the way it plans. What it can't do yet is choose its own subgoals where no demonstration has been. That's what I'm currently working on, and if you want to see more, I'll post about it first on X, @haddyalchaer . 
 References 
 [1] Y. LeCun, A Path Towards Autonomous Machine Intelligence . OpenReview, 2022. 
 [2] L. Maes, Q. Le Lidec, D. Scieur, Y. LeCun, and R. Balestriero, LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels . arXiv:2603.19312, 2026. 
 [3] C. Chi et al., Diffusion Policy: Visuomotor Policy Learning via Action Diffusion . RSS, 2023. 
 [4] W. Zhang, B. Terver, M. Rabbat, Y. LeCun, and R. Balestriero, H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning . arXiv:2610.06805, 2026. 
 © 2026 Haddy Alchaer
