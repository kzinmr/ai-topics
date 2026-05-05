---
title: "Publishing my first game using pico-8"
url: "https://boyter.org/posts/publishing-a-pico8-game/"
fetched_at: 2026-05-05T07:01:55.685966+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Publishing my first game using pico-8

Source: https://boyter.org/posts/publishing-a-pico8-game/

TL/DR;
Play/Download a copy from itch.io
I had always wanted to create games. In fact its one of the reasons I went down the development path. For various reasons I never invested enough time (probably too much time playing them) and went into writing code for businesses.
In hindsight that was probably the right move from a financial perspective, since it seems most game developers tend to be fairly underpaid and the drama in the game development space makes high school teen drama look tame.
I had attempted a few times to make a game and always failed for one reason or another.
I decided I would improve my chances, by limiting the scope and sticking to a very simple rock/paper/scissors premise and commit to shipping it the moment it was good enough. It sounds immodest but I have become quite good at hitting deadlines over the years, even if they are self imposed.
I picked pico-8 as the engine simply because I know I work better with constraints and the limited size and capabilities of it would ensure I would not attempt perfection since I know I do not have the skills to reach it anyway. I have been a professional developer for 10+ years so code syntax is not my biggest issue, but knowing how to architect things, deal with the art and sound.
By sticking within what pico-8 provides I thought I could achieve this, where I had previously failed with tools like Game Maker.
A few days ago I finished and published the result. You can
play/download a copy from itch.io
or if you have
pico-8 get a copy off the bbs
.
The premise is fairly simple. Pick your spell and cast it, with the enemy doing the same. Its rock/paper/scissors with each spell having strengths and weaknesses. For example lighting is powerful, but is defeated by shield, while shield protects from everything except acidball which will pass through it.
I initially wanted everything to be deterministic with the AI, and generally it is, however I quickly realized what I guess many game developers have that this isn’t ideal. As such some of the AI is random in order to produce more fun moments.
The big thing for me was discovering in lua first class functions, so you can throw around different ones at runtime which makes assigning different draw/update functions really easy. As such it was about a 2 min job to start a title screen with instructions. It also allowed my to create screen transitions which was something I had massive issues with previously.
So I can confirm basic sounds effects add a LOT to the experience. A lot more than I was expecting.
I took a crash course in learning the the basics of music theory to get any sort of music in… but then stuck to one track played on the intro. This is easily my biggest pain point, as I have never been musical, and know nothing about it. Something to improve on.
While I am not super happy with everything about about it, I am very happy I finished and shipped. So much so I am starting to toy with new ideas as there are game ideas I have had for a long time that I wanted someone to implement.
Seems some people played it too, at least according to the itch.io reports. Not a breakout success, but certainly a lot more people played it than I ever expected!
I am however very impressed with pico-8 and how easy it is to work with. I can see why people use it now, allowing you to nail down the core mechanic for distilled fun, and then build out on that. The fact I was able to go from
September 18th 2023 - I think im actually going to commit to finishing something in pico-8. I find I work best with constraints and not a blank canvas. Because it is so constrained you have to cut down to the barest thing possible.
to
September 26th 2023 - Published.
About a week. Nothing short of amazing to me. Now to tackle something a little more complex, and grind out game development for a bit. Maybe one day I can make something people really want to play.
EDIT: Someone posted this post to Hacker News
https://news.ycombinator.com/item?id=37703651
