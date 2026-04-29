---
title: "I ported Photoshop 1.0 to C# in 30 minutes"
url: "https://martinalderson.com/posts/ported-photoshop-1-to-csharp-in-30-minutes/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-29T07:02:04.199498+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# I ported Photoshop 1.0 to C# in 30 minutes

Source: https://martinalderson.com/posts/ported-photoshop-1-to-csharp-in-30-minutes/?utm_source=rss&utm_medium=rss&utm_campaign=feed

Over the holidays I saw a link to the original
Photoshop 1.0 source code
from 1990. Of course this gave me the idea - how well could Claude Code do at porting it to 'modern' cross platform C# code?
And, more seriously, what does this tell us about the future of software ecosystems?
Turns out agents can do less popular languages
A lot of the criticism from software developers I hear is that LLMs are only good at certain languages because they are mostly trained on that. This is in my opinion a gross simplification - the LLMs can start to understand general patterns of software development and the logic that goes along with that and don't need to have many examples to work with.
Photoshop 1.0 is ~100k lines of Pascal and ~20k lines of 68k Assembler.
I definitely think Pascal and 68k assembly is
not
topping any popularity charts these days. And I doubt there is much training data for the LLMs to work from in comparison - I could find low hundreds of repos
total
with some Google searches for 68k assembly on GitHub.
I made a folder for Claude Code to work in, grabbed the zip with
curl
and told it to unzip the original source code and explore the original 1990 codebase and make a plan to port it to C#.
It gave me a few options of frameworks to use for cross platform UIs with .NET (it's been a while since I've developer a cross platform GUI in .NET!), and I decided to go with Avalonia which allows you to build apps that target Windows, Mac and Linux. I've actually never used Avalonia before so I definitely didn't guide the approach much.
After a few subagents explored the codebase and wrote a
very
detailed  plan, we delved into implementation. I decided to suggest parallel subagents to implement it, which actually worked extremely well.
30 minutes later, a somewhat usable port
Amazingly 30 minutes later I had a running version of the app, running in C# on modern macOS. I didn't provide any feedback to the agent(s) - my lack of Pascal and 68k knowledge really wouldn't have helped it much.
There's a few bugs here and there - it's definitely not finished - but most of the functionality works and I have no doubt if I had a few more hours I could get a pretty solid port. It did "cheat" in some ways by using SkiaSharp (a drawing library), but the original Mac version used QuickDraw which is also an abstraction
¯\_(ツ)_/¯
. It did, however, port the core concepts faithfully, along with the filter algorithms.
Cool party trick. But what does this mean?
I think this has a lot of implications past toy projects like this.
Firstly, over my career I've had to "rescue" a lot of projects that started out in one language that really struggled to scale. A common issue I've came across is building a project in, for example, Python which with time ends up really struggling with very high throughput.
This has then led to a hasty port of 'hot path' API endpoints/service to a language more suited to high throughput like Go or C# to try and cope with demand spikes better.
I think coding agents would
already
make this process far easier. I suspect this will become an emerging pattern - build the MVP/1.0 of your product in your preferred language (I think Django has one of the best developer experience out there, FWIW), then use agents to quickly port it into a high(er) performance language
if
you start experiencing scale problems.
The end of cross platform apps?
Ironically, despite building this port in a cross platform UI framework, it occurred to me that one of the biggest benefits of this could be building fully native apps and UIs for each platform you target with no 'compromises'.
I spent a near decade building mobile apps in Xamarin (RIP) and React Native, and while they delivered a pretty polished experience with enough time and care, there was definitely quite a few drawbacks - especially with React Native's very single threaded approach.
I'd always really liked the vision of a cross platform app for mobile, as often with doing separate "native" apps for iOS and Android you really needed two teams, and inevitably the apps started diverging. In the end for many apps the compromises of a cross platform framework made a lot of sense for the resource and coordination efficiencies.
But now, I can easily see teams picking a 'lead' language like Swift for iOS, then having a code agent periodically port it all to Kotlin for Android (or visa versa). I think this is going to be a game changer for mobile teams - especially those struggling with limitations of cross platform apps or that don't have the experience in both ecosystems. With correct prompting I think it would be quite possible to end up with the best of both worlds - platform specific features but a rapidly iterating 'core' of the app that is kept in sync automatically by the agent.
Security
Equally I'm extremely bullish on the future of Rust and other memory safe alternatives to C/C++. There's been
far
too many security issues caused by C/C++ and I think agents can play a big part in accelerating the transition away from it.
I noted that Galen Hunt from Microsoft put a (not very well worded, and quickly edited) post on LinkedIn looking for a principal software engineer to just this.
Galen did substantially backtrack on this I should add, and said it was just a research project. Regardless, I think it's a really interesting look into the future of where things may end up. For 'legacy' codebases that
also
have excellent tests around them, I think agents can really shine working in loops transposing codebases from one language to another.
Ironically, LLMs may enable many more esoteric languages
To sum up, I think LLMs are actually going to enable a new 'golden' period of language innovation. New programming languages will be able to port huge quantities of existing libraries - which is usually the main thing holding back adoption of new development ecosystems.
The best library ecosystem used to win. Now you can just bring the libraries with you.
