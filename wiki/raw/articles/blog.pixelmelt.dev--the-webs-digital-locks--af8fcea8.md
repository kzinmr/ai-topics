---
title: "The Webs Digital Locks have Never had a Stronger Opponent"
url: "https://blog.pixelmelt.dev/the-webs-digital-locks/"
fetched_at: 2026-07-04T07:01:40.265480+00:00
source: "blog.pixelmelt.dev"
tags: [blog, raw]
---

# The Webs Digital Locks have Never had a Stronger Opponent

Source: https://blog.pixelmelt.dev/the-webs-digital-locks/

Recently I've been benchmarking my JavaScript code protection against the strongest Claude model set to max thinking and I'm up to 22 minutes (and 170k tokens) before it can crack a small protected sample open starting from 0 knowledge. (
More about the protection scheme here
)
Its kind of disappointing for how much time I've put into my work but man is it good at helping point out flaws in the system and showing what I'm doing well based on where it get tripped up in the process.
This made me think about reverse engineering and the potential of LLM's in it in general. To me the appeal of LLM's is in taking on massive amounts of tedious mental work quickly. I could hire someone to do the same thing, but the LLM gets to the same output quicker.
The whole point of code protection is to make reversal (which is mathematically impossible to stop) take as long as possible.
The basic idea
Information Wants To Be Free
Based on my own observations I wouldn't be hesitant to claim that we are already in a renaissance era of reverse engineering, everything can be taken apart, the defenders are going to be on the back foot until we figure out some way to cope with LLM's. Keep in mind this is currently strictly in the JavaScript ecosystem. I am not a binary reverse engineer, but I would expect it'll happen to the binary side of things eventually too, once the training data side of things gets there.
Evidence?
Just the other week I had Claude rip a friends college textbook out of a proprietary online reader with very little input from me, it took 30 minutes when before that would have taken hours potentially days. ( expect some cool blog posts soon :> )
The floor for reverse engineering the web has been raised immensely. When an uninformed user can say "deobfuscate this code" and a frontier LLM will rip through even a commercial antibot or an ebook platforms code protection, it raises questions on whether these schemes are even doing what they were originally designed for anymore.
The difference you get from paying 50k is the difference between any Joe schmoe defeating your protection and a hobbyist doing it.
The experts have always been able to reverse protections but now that they can command the tedious task solver machine they can reverse much faster than before.
Before it was 'make it take longer before it inevitably falls' and then update it to hit back at the attackers, now I would be hard pressed to see the attackers being kicked down for more then a few hours while they identify what changed and how to break that too.
My point is LLMs annihilate the upfront cost of reverse engineering a code sample. It can reverse my protection and it can reverse commercial protections, exposing data to the user over the web is less safe then it has ever been before.
You Can Just Generate Source Maps Now
You can just take a bundled app and regenerate the source files. I've seen this done to three separate websites. Remember when
Apple's app store source map was posted accidentally
? You can do this to any website you want!
One was minified and bundled with webpack.
One was written in a JavaScript derivative language (Coffeescript).
One was protected with Jscrambler obfuscation.
No difference in the outcome.
You want to get minified variables back? No problem, want to port the whole codebase to typescript too? Might need a little bit more instructing, maybe write a harness but sure why not?
Part of the code from a game reversed with an LLM
The defenders have LLMs too, just pit them against each other?
There's no anti LLM obfuscations yet and it's Interesting to think about what that would look like, but also, the traditional use case of obfuscation can't mesh with that idea in the first place, Once I crack your game or program with IP in it, Its over you don't get another chance, Its only antibots who have the luxury of being able to evolve their protection in real time.
Whats next?
Is there a world where the defense side gets equivalent agentic tooling? Automated protection that evolves faster than an agent can characterize it? Or is that a fundamentally asymmetric problem where offense wins by default because reversing is easier to automate than protecting?
It very well could happen, I've seen no evidence of it though, perhaps because defense requires generating novel complexity, its harder to automate then offense, which only requires classifying existing complexity.
