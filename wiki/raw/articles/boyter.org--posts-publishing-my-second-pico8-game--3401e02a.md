---
title: "Publishing a second game using pico-8"
url: "https://boyter.org/posts/publishing-my-second-pico8-game/"
fetched_at: 2026-05-05T07:01:53.549725+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Publishing a second game using pico-8

Source: https://boyter.org/posts/publishing-my-second-pico8-game/

TL/DR;
Play on itch.io
or
Plan or download from lexaloffle
I previously wrote about making a game using
pico-8
. Once done I more or less instantly wanted to make another one and started sketching out some ideas.
Years ago I had watched a Youtube video
https://www.youtube.com/watch?v=slDAvewWfrA
about how Britain’s peak power demand spikes when the closing credits of a popular soap opera runs, since everyone gets up to make a cup of tea. As a result the people responsible for dispatching more power actually have a TV to watch the show, since the credits are never at the same time, and when the demand kicks in, ramp up hydroelectric dam output to meet the demand. The goal being to ensure grid stability by keeping the frequency as close to 50hz as possible and avoid damaging equipment or shutting the grid down.
This sounded like an interesting idea to me, since the common assumption is that power is a simple matter of hooking a power station and it just works. This ignores the actual complexity involved, where literally every light turned on requires a little more effort from the power plants. That’t not factoring in the modern grid, with gas dispatch, uneven solar, batteries, demand spikes and everything else.
So I sketched out the basic idea. You do the same thing. You have control over the dispatch sources and your goal, your only goal is to manage them to ensure the grid stays as close to 50hz as possible, without going to high or low which causes a grid shutdown.
The result? Power Control.
A few simple rules.
Control keys to select a button. X/O to click them.
Adjust power generation on the fly to keep it at the 50hz value! Too high, or too low and the grid will shut down!
Your power sources,
Coal. Infinite power. Slow to spool up or down.
Hydro. Spins up and down faster than coal, but runs out. Replenishes faster when it rains.
Gas. Spins up fast. Runs out fast.
Solar. You have no control over this. Works when its sunny. Does not work as well when its cloudy, and does not work at night.
Battery. Smooths the grid out. Will soak up excess, and release to keep it stable, but will run out quickly!
I am embarrassed to admit I had most of this done in 2023…. sometime after publishing Wizard Duel. Here is a early gif screenshot I took back then to show some people,
You can see the early concept. The different power sources, the ability to spin them up or down, the hz meter with a leading indicator of where it was going, and a trailing line with jitter to simulate the normal grid fluctuations that any grid has to deal with. The ticker at the bottom informing you of events that modify the load.
However… then I got distracted. To be honest I had way too many ideas and things going on at the time. However I am making up for this now, and as such you can now play the real thing.
pico-8 remains a delight to use, and the enforced limitations really make you work on the core concept. As I discovered previously, sound plays a huge part of the experience.
Is power control something that could become a larger game? No idea. I don’t think I know enough about game design to determine that, but maybe someone else can let me know. Is it as good as wizard duel? I don’t think so, but publishing and getting something else off my backlog feels good.
For now, im going to focus on some more ambitious games I want to make in Godot. I bought iPad Air with an expensive pencil for a reason dammit, and come hell or high water im doing to focus on learning to draw with it well enough to make something I can be proud of.
