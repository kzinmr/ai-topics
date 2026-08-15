---
title: "Training a Reinforcement Learning Model to Play Bonk.io"
url: "https://blog.pixelmelt.dev/training-a-reinforcement-learning-model-to-play-bonk-io/"
fetched_at: 2026-08-15T10:14:59.359520+00:00
source: "blog.pixelmelt.dev"
tags: [blog, raw]
---

# Training a Reinforcement Learning Model to Play Bonk.io

Source: https://blog.pixelmelt.dev/training-a-reinforcement-learning-model-to-play-bonk-io/

This is
Bonk.io
, a simple browser game where you, a circle, try to knock other circles off of a map sumo style.
I've been playing this game for a few years at this point and recently had the idea of trying to train a neural network to play the game. It should be interesting since despite looking simple, there is quite a high skill ceiling.
It should be easy,
right
?
A player sitting on a platform in game.
Lets look at the state we will need to teach the bot to output as well as read on other players.
A list of the different inputs a player can preform.
Pretty simple, but now we need to create the environment where the network will fight against itself in a loop to learn to play the game.
Building the Training Harness
This is where the hard part begins, since Bonk.io was originally a flash game, it is using
Box2DWeb
, a JavaScript port of the same Box2D engine used in the flash era.
Also, the game client is obfuscated with
JScrambler
and completely incomprehensible.
Creating this environment is not going to be easy, we have a few options at this point.
Browser Manipulation
We could use an instrumented browser where we send key presses to the DOM and read positions out of the games memory.
This is probably the most time efficient way to pull this off, and some other people have done this! But if you end up doing this you are stuck running the game in real time. One browser tab gives you one game environment running at 30 fps, and reading state back out means hooking the frame drawing APIs of an obfuscated program.
Reinforcement learning needs a lot of data, my current training run just passed 10 billion frames. At 30 fps that's over ten years of continuous play for a single tab, so this approach would need a server full of browsers running for months, a server that I don't have.
Reimplement the Physics?
Option two, I reimplement the physics myself from how the game looks and feels. The problem is that "close enough" is not close enough. If I train on an approximation, the bot learns my approximation. Every mistake in my engine becomes a misconception in the final model, and it makes no sense to begin with since I would need to hook the browser anyway just to run the finished model against the real game.
Here is the thing, bonk.io uses deterministic lockstep networking. Every client in a match simulates the entire game locally, and the only thing that crosses the wire is each player's keypresses. For that to work, the physics has to be a pure function: same state plus same inputs gives the same floats, bit for bit, on every machine.
Which means that
the game ships its own engine to every browser that opens the page
. I just had to find and use it.
Bonk.io's JScrambler protected source code
Stealing the Physics
The first thing I had to do was make the client readable at all. Most of that work was not mine, my friend
Ciaran
did the heavy lifting on
deobfuscating the JScrambler build
, I only had to reverse some non JScrambler bonk specific code obfuscation. Ciaran has
his own technical blog
along with
some articles on this one
if you want to see more from him.
After a lot of staring at the 31,339 lines that came out the other end, I figured out that the physics the game runs is is a modified build of
Box2DWeb
. And even better, the game rebuilds the entire physics world from scratch every frame. There is no persistent world. Each frame, every body, fixture and joint is recreated from a plain JSON game state, the world is stepped once, and the results are read back into a brand new state. This means that the engine is a pure function over data, exactly what I needed.
Also small Easter egg, the player's friction constant is
0.001337
!
Speed
Initially I started out by using the JavaScript ripped from the client. But the siren song of making an LLM rewrite the library in rust was too strong.
That's about how it went
This is actually a great use of LLMs, since the goals for the project are extremely verifiable in their correctness, in this case we have two things to optimize for,
execution speed and parity to the JavaScript implementation
.
Getting the rust port "close" to the JavaScript version fails for the same reason that rewriting based on how it looks fails. So the port mirrors every float expression in the original in shape and evaluation order.
All math goes through wrappers that round to 7 decimals, exactly like the game's SafeTrig utility functions. Even the JSON parser had to be correctly rounded, because the default one isn't, and parity breaks at the first division.
Then the test harness. I used a corpus of 1,961 real maps from the game. Forcing the LLM to do a full frame-by-frame comparison against the original implementation was successful and came out to 1961/1961 bit-identical in the end.
Training a brain
With real physics in hand, the actual machine learning could start. The trainer is TypeScript running on Bun, with the Rust engine loaded over FFI.
I initially started out with TensorFlow.js on the GPU, but doing that made training slower than the equivalent TF.js CPU build (4k fps vs 41k), because the network is tiny, it spends most of its time on overhead. So its time to call up our friend again.
I'm seeing a pattern here
Just like with before, we can validate the accuracy of the output against the existing tensorflow implementation, this assertion is a little more shaky and potentially prone to edge cases, but in the end it did work so who am I to complain. Now that we have PPO written from scratch, cuBLAS for the matmuls and 31 custom CUDA kernels for everything else.
The bot makes a decision every 2 physics frames (15 Hz). Eight rollout workers run 512 game instances against each other, a central inference server batches every worker's policy evaluations into big GPU waves so they don't fight over the card, and PPO updates happen on the same GPU between waves.
The bot sees 14 numbers about its own disc and 19 about the opponent, positions, velocities, ability charge, who's touching what, stacked over 7 frames at offsets 0, 1, 3, 7, 15, 30 and 60, so it gets a couple of seconds of history to inform its next decision. Plus decaying traces of its own recent buttons, 16 raycasts into the map geometry reporting wall proximity and death-zone proximity, stacked 4 deep. 385 floats total.
Its output options are left, right or neither, up, down or neither, heavy on or off.
The reward while playing is +1 for a win, −1 for a loss, −0.3 for draws.
And for the opponents I used a league. About a third of games against the models current self, a third against a reservoir of past versions, and a third against "exploiters", which are policies trained specifically to beat the current main agent, so it can't settle into strategies with holes in them. Every sample is also mirrored horizontally, doubling the data and forcing the policy to be symmetric.
Where it's at now
The bot beats plenty of casual players and still loses to strong ones.
On a live Elo table my best deployed policy sits 5th out of 522 tracked players, behind four very good humans, and ahead of every other regular who has joined the room.
The robot wins in the end
Big thank you to legendboss123 for guiding me on this project and providing in game replays for pretraining.
LEGENDBOSS123 - Overview
100% totally a professional coder frfr. LEGENDBOSS123 has 50 repositories available. Follow their code on GitHub.
