---
title: "Shopify went back to native. I think the bigger shift is formal verification"
url: "https://martinalderson.com/posts/shopify-native-formal-verification/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-10-08T10:01:34.386060+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Shopify went back to native. I think the bigger shift is formal verification

Source: https://martinalderson.com/posts/shopify-native-formal-verification/?utm_source=rss&utm_medium=rss&utm_campaign=feed

The social media discourse is ablaze with people porting apps from slower dynamic languages to faster statically compiled languages. And we've seen both
Shopify
and
Coinbase
start switching away from React Native back to native mobile apps. What's changed, and what's next for programming ecosystems? I think the answer is less about performance than it first looks.
Why did people use cross platform frameworks?
When modern smartphones first came out, there was an explosion in native app development. Cross platform web apps on smartphones were (and to be honest, still are in many respects) limited in terms of the features and quality of UX you could deliver to users.
This involved most companies having to build totally separate app codebases, one per platform. Typically you'd have a Swift (previously Objective-C) iOS app and a Java/Kotlin Android app.
For many teams, this is a huge headache. Not only do you require ~twice the resources, building everything twice, but coordinating feature releases and maintenance gets really tricky. For example, if you do a big backend migration, you need to coordinate it across two teams, in a totally different language ecosystem. Typically one app - usually iOS - would get more attention than the other, too, with wildly diverging feature sets.
As such, there was an explosion of cross platform mobile app frameworks, with React Native becoming the most popular, though it's important to mention other ones like Flutter and Xamarin (which was rebuilt as .NET MAUI, and lost nearly all the traction it had during the post acquisition migration).
These allowed you to (mostly) write your app once, and the framework would do the job of translating it to the platform below. In general, they worked quite well, but did have performance issues (especially React Native) and a huge swath of framework bugs which were often painful to work around.
As such, many companies migrated to these frameworks. But now we see the migration being undone with the advent of coding agents.
Agents translate between platforms
As coding agents have got better and better, it's become obvious that
writing
code is nowhere near as time consuming as it used to be. So the main objection to writing native apps - resourcing requirements - has collapsed. You can even just have one 'primary' platform and have the agent autonomously port each change to the 'secondary' platform, which works surprisingly well on more capable models.
I'd argue it isn't completely solved, given you still want to test and ensure your features are well designed for both platforms. But cross platform frameworks didn't really solve that before, and arguably agents can do a far better job of translating your requirements to each platform than a cross platform framework like React Native can.
And obviously this gives big improvements in performance of the app, plus often better access to underlying platform features (which can lag support in React Native et al).
But maybe it's not just about performance
I thought at first that really it was going to be quite clear that all software gets written in the most performant language, as advocated by DHH's
autonomous porting experiments
, and this switch to native apps is just a very visible example of it.
But the Shopify move made me think about it differently. What it really shows is that
writing
code has stopped being the expensive part - Shopify can afford two native codebases now because agents are writing them. The expensive part is knowing the code is actually correct: reviewing it, testing it, trusting it. And "use a faster language" doesn't help with that at all.
So my slightly wildcard guess is that we will end up with formal verification systems being the primary way we (and by we, I mean agents) write software going forward.
Formal verification systems (Lean being the most well known example, though it's mostly used for mathematical proofs - Dafny is much closer to 'normal' programming) are fairly obscure outside of certain fields. Typically they'd be used for the most critical parts of software - think aeronautical control systems, or critical security systems at AWS (they
built their Cedar authorisation language
this way). They allow you to
prove
the software does what it says. While traditional software testing approaches like unit testing help you (and agents!) catch bugs, they require writing the problems ahead of time to test for.
Formal verification systems on the other hand use a solver to
prove
the code does what you said. Instead of just writing a test that checks you don't have a bug in your order handling code, you can formally prove that an order can't move into an invalid state, or a user can't see data they shouldn't be able to see.
The enormous drawback to them previously was they are torturously hard (and slow) for humans to write the proofs. Worth it for ensuring critical infrastructure works well, but very much
not
worth it for most software.
But the calculus for this switches hugely with agents. They could write all your code in something like
Dafny
, which then outputs the
actual
code into a fast language like C# or Go, getting great performance
and
a step change in reliability and quality of software. It's the same economics as native apps: something that was too expensive for humans to do twice becomes cheap when an agent does the grunt work.
This isn't quite the slam dunk currently, though. Dafny relies on an SMT solver to do the proving, and it's notoriously
brittle
- a proof that worked yesterday can time out today because you renamed a variable or upgraded Dafny. If you thought Rust compile times were frustrating, an unpredictable verifier is a whole new world of hurt, especially when an agent can't tell the difference between "my proof is wrong" and "the solver gave up".
But I'd expect this to get a lot better. Verification tooling has had a tiny fraction of the attention and investment that mainstream compilers and languages get, simply because it was so niche and esoteric. If agents make it mainstream, I suspect we'll see the same kind of rapid improvement we saw when JavaScript engines suddenly mattered.
So I'd recommend you spend some time playing around with formal verification systems. The
Dafny guide
is a good start, or just ask your agent of choice to formally verify one critical function in your codebase and see what it finds. I strongly suspect you'll be hearing a lot more about them.
I did
write previously
that we'd actually see a resurgence in 'esoteric' programming languages, not the monoculture many expect. But I actually think we're going to speedrun every programming language innovation that has come out of (primarily) academia
very fast
with agents.
