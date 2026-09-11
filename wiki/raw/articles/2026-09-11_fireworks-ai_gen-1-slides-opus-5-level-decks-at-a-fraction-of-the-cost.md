---
title: "Gen-1 Slides: Opus 5-level decks at a fraction of the cost"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/gen-1-slides-opus-5-level-decks-at-a-fraction-of-the-cost"
scraped: "2026-09-11T06:00:17.308120+00:00"
lastmod: "2026-09-10T16:13:16.000Z"
type: "sitemap"
---

# Gen-1 Slides: Opus 5-level decks at a fraction of the cost

**Source**: [https://fireworks.ai/blog/gen-1-slides-opus-5-level-decks-at-a-fraction-of-the-cost](https://fireworks.ai/blog/gen-1-slides-opus-5-level-decks-at-a-fraction-of-the-cost)

Join us for our inaugural conference, Forge 2026
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Gen 1 Slides Opus 5 Level Decks At A Fraction Of The Cost
Gen-1 Slides: Opus 5-level decks at a fraction of the cost
PUBLISHED
9/10/2026
Table of Contents
TL;DR
Building specialized intelligence for agentic work
Why this is a reinforcement learning problem
The training partnership
Encoding Genspark's standard
A curriculum, not a single run
Keeping the run stable
Matching Opus 5 at a fraction of the cost
Considerations for teams running long-horizon RL
Table of Contents
Talk to the Fireworks training team
Get in touch
Table of Contents
TL;DR
Building specialized intelligence for agentic work
Why this is a reinforcement learning problem
The training partnership
Encoding Genspark's standard
A curriculum, not a single run
Keeping the run stable
Matching Opus 5 at a fraction of the cost
Considerations for teams running long-horizon RL
Table of Contents
Talk to the Fireworks training team
Get in touch
TL;DR
•
Genspark partnered with Fireworks Lab to post-train MiniMax M3 into Gen-1 Slides, a model that plans, writes, and checks its own slide decks end-to-end.
•
Gen-1 Slides matches Opus 5 on deck quality on Genspark’s evaluation, at about 1/17 of Opus 5's input-token list price.
Per finished deck, Gen-1 Slides costs about 90% less than Opus 5.
In production it is on par with Opus 5 on every metric, and it
cut low-rated decks from 18% to 3.6%
over its base.
•
Genspark's research team defined what a good deck is, encoded it as an evaluation standard, led the design of the algorithms to train that standard into the model, and validated it on live traffic. Fireworks Lab managed the full training to get the model there: the reward engineering, the 100-plus experiments, and the systems work that keeps a 100,000-token trajectory numerically stable.
Aggregate internal-grader score, 200 real tasks. Comparison is primarily against Opus 5, the frontier model served at scale on this task; Claude Fable 5 / 5.1 shown for reference only.
Building specialized intelligence for agentic work
Slides are one of Genspark's highest-volume agentic workloads. Users generate them for quarterly reviews, client pitches, and board updates, and they need output that holds up in front of an audience, not a draft they still have to fix by hand.
Off-the-shelf models, including the best proprietary ones, produce decks that look right at a glance but fail on inspection: text overflowing its box, blank renders, invented content. On a closed model, Genspark couldn't tune for the quality the workload needed, and at over a trillion tokens a month, couldn't control the cost either. Owning the model meant owning both.
Why this is a reinforcement learning problem
A deck isn't a single output you can hand a model to imitate. Producing a good one means working in a live workspace across dozens of turns: planning the arc, writing the HTML, rendering it, reviewing the render, catching a layout defect, and fixing it, over hundreds of thousands of tokens in one session.
A finished deck records none of that work, only its result. Examples can show the model what a good deck looks like, but not the sequence of judgments that produced it, so imitation alone can't teach the behavior. That is what made this a reinforcement learning (RL) problem, and a hard one on three counts:
Long horizons.
Episodes run dozens of turns. Small per-token errors compound into broken layouts, truncated files, and abandoned decks.
Judgment, not just correctness.
A deck can be syntactically perfect and visually incoherent. The reward has to capture design quality, not just task completion.
Credit assignment across turns.
A layout decision on an early turn can look fine and only produce a broken render dozens of turns later. The signal has to reach back from the failure to the decision that caused it.
The training partnership
Clearing all three at once is what stood between Genspark and a model they could own.
That is exactly what Fireworks Lab is built for: it brings the training and inference infrastructure, compute, and research talent of a frontier lab to a customer's hardest training problems, so they can compete on quality, cost, and performance.
Its researchers embedded with Genspark's team to post-train MiniMax M3, an open-weight multimodal model, into Gen-1 Slides.
Genspark shaped the objectives and algorithms. They brought their real production environment directly into training and defined the standard behind it: the judgment of what makes a deck good, the design principles behind it, and the process for sharpening that standard. They also led the design of the algorithms to train that standard into the model.
Fireworks Lab codeveloped the algorithm and managed the training process. Beyond the infrastructure, their researchers were deeply involved in optimizing the process for efficiency and for alignment with Genspark's goals. They drove more than 100 experiments and read trajectories to catch the model gaming the score. In one case, the model raised its visual-design score while task completion slipped, so the total went up but the deck wasn't better. Keeping a run whose episodes run past 100,000 tokens stable enough to converge is as much a systems problem as a research one.
Encoding Genspark's standard
RL optimizes toward the evaluation, so what it measures is what the model becomes. Genspark's methodology scores each deck across the quality dimensions that matter and penalizes the defects that ruin one in practice: a blank render, text past its margins, invented content. The scores came from live production behavior. As training progressed, quality scores rose while penalties fell.
Reward across training. Gen-1 Slides climbs from the MiniMax M3 base to Opus 5's level over the run.
A curriculum, not a single run
Fireworks Lab structured the training as a sequence of stages, each raising the context length and fixing the failure the previous stage exposed.
Learn what good design looks like.
Fireworks Lab began with an SFT pass on curated decks, giving the model the visual vocabulary of good slides before any RL.
Start RL at short context.
Long contexts early on produce long, error-filled rollouts and a noisy gradient, so they started RL on short episodes to keep the signal clean, and lengthened the episodes as the policy steadied. The first solid checkpoint generated better slides but still laid them out unreliably.
Extend the context window.
Once the reward carried a clean signal, they widened the window to let longer, richer trajectories into training, and layouts became reliable.
As trajectories lengthened, the binding constraint stopped being the reward and became the numerics of a very long episode.
Keeping the run stable
An RL update is only correct if the two engines in the loop agree. The inference stack samples a rollout and the trainer scores it, and the update is unbiased only when both assign the same probability to the same token. They run on different code paths, so that agreement is never automatic. On a short episode the difference is negligible; on a trajectory past 100,000 tokens it compounds into a biased gradient.
Fireworks measures that agreement at every step, and the measurement caught the run's worst failure, one that raised no error and left nothing else looking wrong. The trainer and sampler were pulling apart on long trajectories, and Fireworks Lab traced it to the token stream.
Tokenization does not round-trip cleanly, so the sequence the trainer scored differed slightly from the one the model had sampled, and the importance ratio was computed against the wrong tokens. That biased the gradient on every step. Aligning the two token streams fixed it, and token- and batch-level filtering cleared the rare extreme divergences that remained.
A failure like this raises no error and biases every update. Catching it takes a training stack where inference and training are one aligned system, not a trainer bolted onto a separate inference engine.
Matching Opus 5 at a fraction of the cost
Gen-1 Slides is live today as the default in Genspark AI Slides' Standard mode. On Genspark's evaluation, it matches Opus 5: it leads on visual design and on aggregate score, and
ranks first in eight of the nine grader columns spanning three independent graders, and in the top two in all nine graders
, at about 1/17 of Opus 5's input-token list price
.
Measured per finished deck, Gen-1 Slides runs about one-tenth of the cost of Opus 5.
For a team producing 1,000 decks per month, that means a reduction in spend of roughly 90% (from about $4,200 to $400). The budget that used to serve one user at frontier quality can now serve roughly ten.
In production, Gen-1 Slides is on par with Opus 5 on every metric, and cut low-rated decks from 18% to 3.6% against the base model. Because it was trained on full agent sessions rather than a benchmark, the planning, self-checking, and error recovery it learned are what show up in front of users.
Considerations for teams running long-horizon RL
Designing the reward is a research problem. Keeping the run stable enough to optimize against it is a systems problem, and as trajectories grow long, that is where the hardest and least visible failures live. Three of them are worth planning for.
•
The hardest bugs were numerical.
The tokenization mismatch above was the most damaging, and fixing it raised a further puzzle: a more exact alignment method produced near-perfect agreement metrics but unstable training.
•
Sequence-level objectives beat token-level ones at long context.
Averaging the importance ratio across a trajectory dampens the effect of individual outlier tokens, whose per-token ratios can otherwise dominate the update once a trajectory runs to hundreds of thousands of tokens.
•
Visual quality scaled with output length, up to a point.
Longer responses meant richer layouts and more HTML elements, and design quality rose with them, until late in training, when added length stopped improving quality and started driving instability.
Gen-1 Slides is specialized intelligence Genspark owns: a model tuned to their domain that matches the frontier on one of their highest-volume workloads. What makes it durable is the standard behind it. Genspark's definition of a good deck lives in the reward and the eval, so it carries to every base model they train and produces the next when a stronger base arrives.
Slides are one of several capabilities Genspark has
brought in-house with Fireworks
. With the evaluation in hand, the quality ceiling for each capability is theirs to raise, instead of being dictated by someone else. If you want to push a workflow past what off-the-shelf models can give you,
talk to Fireworks Lab
.
Related Posts
Partner Announcements
8/26/2026
Post-training Kimi K3 with Harvey for long-horizon legal work
Partner Announcements
12/15/2025
NVIDIA Nemotron 3 Nano on Fireworks: The Engine for Next-Generation AI Agents
Partner Announcements
11/24/2025
Fireworks Expands AWS Alliance: Strategic Collaboration Agreement + GenAI Competency
Next
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
