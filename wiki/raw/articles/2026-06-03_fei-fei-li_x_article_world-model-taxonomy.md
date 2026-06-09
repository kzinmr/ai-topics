---
title: "A Functional Taxonomy of World Models"
author: Fei-Fei Li
source: x.com/drfeifei/status/2062247238143996275
url: https://x.com/drfeifei/status/2062247238143996275
article_url: https://x.com/i/article/2062244283940544512
date: 2026-06-03
type: x_article
tags:
  - world-models
  - spatial-intelligence
  - robotics
  - taxonomy
  - fei-fei-li
  - world-labs
metrics:
  impressions: 890080
  likes: 4402
  retweets: 911
  bookmarks: 5774
  replies: 154
  quotes: 197
---

"The world is everything that is the case."
— Ludwig Wittgenstein, Tractatus Logico-Philosophicus, 1921

The world is not made of words.

In an earlier essay, we argued that spatial intelligence is AI's next frontier and that world models are the path to it. Here, the World Labs team and I want to go one level deeper: of the many things now being built and called 'world models,' which functional pieces actually compose that capacity — and what is each one for?

Language models have given machines an extraordinary command of concepts, vocabulary, and reasoning, but the physical world, virtual or real, runs on a different substrate. Where language models learn the statistical structure of text, world models learn the statistical structure of space and time: how light falls on a surface, how a garden looks from an angle no camera has captured, how objects respond to force and follow the laws of physics.

That makes "world model" one of the most important and most overloaded terms in AI today. Computer vision, robotics, reinforcement learning, and generative AI each claim to be building world models, and each means something quite different. A video model that produces gorgeous but physically impossible flames, a language model improvising a playable game, and a physics engine that faithfully simulates combustion all go by the same name.

The ancient Greeks could never agree on what the world was made of, whether fire, water, or indivisible atoms, because "world" was never a single thing. It was always a stand-in for whatever totality a given thinker needed to reason about. AI has inherited the same problem, at exactly the moment when the field needs precision.

## The loop beneath the taxonomy

Cutting through that confusion starts with a diagram older than any of the technology in question. Reinforcement learning textbooks, including the canonical Sutton and Barto, have used a version of the same picture for decades to describe how an agent interacts with a world. The formal name for this picture is the partially observable Markov decision process, or POMDP, and the original definition of the term "world model" belongs to that tradition.

An agent, which can be a person, a robot, or a software system, takes actions. Those actions affect the state of the world. The agent never sees the state directly. What reaches the agent are observations: the photons that fall on a retina, the readings from a sensor, and the pixels in a video frame. New observations inform new actions, and the loop continues.

The word "state" needs unpacking, because the meaning shifts from field to field. This is not the chemist's state, the difference between solid, liquid, and gas. This is the physicist's and roboticist's state: a complete description of what is happening in the world at a given moment, including every object, every position, every velocity, every property. State is the underlying reality of the world; complete in principle, but never directly visible to any agent inside it. Observations are an agent's partial view of that reality. Actions are what the agent does in response.

This loop — agent to action to state to observation and back — is the structure that gave the modern term "world model" its technical meaning. The phrase itself is older, traced to Kenneth Craik's 1943 proposal that minds reason by running "small-scale models" of reality, and carried into neural networks by the late 1980s and early 1990s. And the loop also explains what people mean by the term today. The different things now being called world models are in fact different projections of this same loop. Each one outputs a different piece of it.

## Three functions of a world model

The first kind of world model is a renderer. A renderer outputs observations in the form of pixels meant for human eyes, and the quality that matters most is visual fidelity. A video model that turns a text prompt into a cinematic drone shot is a renderer. So is an interactive system like Google's Genie 3, or World Labs' own RTFM, where the model generates frames in real time conditioned on user input. The model carries no explicit understanding of three-dimensional structure. It produces what a viewer would see, not what is. The buildings in the drone shot may look flawless from above, but try to drive through the city below and they fall apart.

The second kind is a simulator. A simulator outputs state: a geometrically, physically or dynamically faithful representation of the world that humans and computer programs can both compute on and interact with. Where the renderer's contract is purely visual, the simulator's contract is structural, demanding geometry that holds up under inspection, physics that respects Newton's laws, and dynamics that behave the way the world needs to behave given the laws of physics. A simulator serves two consumers at once. Human professionals such as architects, designers, filmmakers, and game developers need accuracy beyond visual plausibility. Computer programs such as reinforcement learning agents, robot controllers, and autonomous vehicles use simulators as training grounds where they can interact with the world at scale, testing scenarios that would be dangerous, expensive, or impossible to run in reality.

The third kind is a planner. A planner outputs actions. Given an observation and a goal, a planner answers the question of what the agent should do next. This is, in many ways, the inverse of the renderer. Where a renderer takes actions as input and produces observations, a planner takes observations as input and produces actions, closing the perception-action loop. Vision-Language-Action models, model-based systems, and the new wave of World Action Models are all attempts at planners: systems that can decide what a robot should do in an unstructured world.

These three categories describe most of what is actually shipping today, and the distinction between them is useful in practice. The categories are not, however, fundamentally separate. The same underlying knowledge of how the world works—geometry, physics, dynamics—sits beneath all of them. A model that can render a cup from any angle ought, in principle, to be able to simulate what happens when the cup is pushed and plan a hand to pick the cup up. Increasingly, the most interesting research deliberately blurs the boundaries between the three.

## Why simulation is the linchpin

Of the three categories, the simulator gets the least public attention, and is the most consequential of the three. This essay addresses this asymmetry.

The renderer is by far the most commercially mature. A number of image- or text-to-video products are expanding in the consumer or enterprise markets rapidly. Google's Nano Banana model has put renderer-quality image generation in the hands of potentially hundreds of millions of users. The technology is real, and the markets are real. Yet renderers optimize for visual plausibility rather than physical accuracy, and that ceiling matters. Their outputs are beautiful, but they cannot be trusted to design a building or train a robot.

The planner is the most intriguing and the most nascent, closely connected to the rapidly evolving field of robotic learning. The field has produced robotic demos in the last two years that look impressive in videos, but candor is required about what those demos actually show. Almost all have been confined to heavily constrained laboratory setups, with narrow object sets and short task horizons. None have been validated at the complexity, variability, or duration that real-world deployment demands. The gap between a compelling demo reel and a robot that reliably works in a kitchen, a warehouse, or an operating room remains vast. The commercial bets are nonetheless substantial. A wave of well-funded entrants is racing to ship general-purpose planning systems, while the largest infrastructure players are positioning planning atop broader simulation stacks. A robot that can plan is a robot that can work, and the entire industry is racing to be the one that gets there first.

Simulation is the bridge between the two. If language is an abstraction of the world and pixels are a projection of it, then geometry, physics, and dynamics are the world itself. A simulator must work at that level: the structural backbone from which both visual appearance (for renderers) and action consequences (for planners) can be derived.

A model that masters simulation can project its understanding into pixels for human consumption, and into action predictions for embodied agents. A model that masters only rendering, or only planning, cannot do either. The commercial surface area is enormous. NVIDIA's Omniverse alone targets what the company estimates as more than a trillion dollars of addressable market in factories, warehouses, supply chains, and digital twins. Robotics training, autonomous vehicle testing, architectural visualization, engineering, and drug discovery all depend on something simulation-shaped.

The hardest open problems in the field live there too. Three-dimensional data with explicit geometry, material properties, and physical annotations is orders of magnitude scarcer than the internet video that renderers train on. The sim-to-real gap, which is the difference between how things behave in simulation and how they behave in reality, persists. Generative simulators introduce a new risk on top of that: AI-generated geometry can look correct while containing self-intersections or wrong scale that produce nonsensical physics. Multi-physics simulation at scale, where rigid bodies, deformable objects, fluids, and cloth all interact, remains orders of magnitude more expensive than single-domain simulation.

At World Labs, Marble is our first move into this territory. It takes multimodal prompts (text, image, video, or spatial sketch) and generates explorable 3D environments, outputting Gaussian splats for visual exploration alongside collision meshes a physics engine can operate on. But Marble is only the first chapter of a much longer arc being written across the field as the lines between rendering, simulation, and planning begin to collapse.

## Where the boundaries are collapsing and what comes next

But more is to come. The most important pattern in the field right now is that the three categories are starting to blend into one another. The shared insight is that the knowledge required to render a world, simulate it, and act in it is largely the same. Continuing the earlier example, a model that truly understands how a cup sits on a table (its geometry, material properties, response to force, etc.) should be able to render that cup from any angle, simulate what happens when the cup is pushed, and plan for a hand to pick the cup up. The three categories are three projections of a single underlying understanding.

For example: a small but growing number of recent work from various robotics labs have demonstrated that—at least conceptually—a pretrained video renderer can be used as the backbone for joint world-and-action prediction, suggesting a bridge between the renderer and the planner by letting one model imagine what will happen and what to do. World Labs' Marble already outputs Gaussian splats and collision meshes from a single model, dissolving the boundary between the renderer and the simulator. Every level is moving from passive output to interactive system, with renderers becoming action-conditioned, simulators generating worlds that are more controllable and editable, and planners deliberating rather than just reacting.

The logical endpoint is a unified world model: one foundation model that can render photorealistic views, produce physically accurate structure, and plan action sequences, switching between output modalities depending on what the downstream consumer needs. We will still face a number of daunting challenges. The data picture is uneven, with renderers awash in internet video while simulators and planners face acute shortages of 3D assets and robot demonstrations. Optimizing for visual beauty can sacrifice the precision a robot or a high-fidelity simulation needs. Reconciling these tensions inside a single architecture is the defining open problem in world model research today, and this is what World Labs sets out to do as we continue to evolve Marble.

The direction, however, is clear. The same bet the field has been making since the late 1980s — that a sufficiently rich model of the world is all that any agent needs to see worlds, build them, and act in them — is the bet now driving an entire generation of research. What gives that "big bet" weight is the convergence already underway: three threads, each already driving and shaping multi-billion-dollar industries on its own, that began as separate research programs are starting to behave like one. Taken together, as the boundaries between them collapse, they will reshape something larger: the relationship between machine intelligence and the physical world it inhabits - the long arc of spatial intelligence.

Language gave machines a way to talk about that world. World models are how machines will finally come to understand, imagine, reason and interact with it.
