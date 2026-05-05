---
title: "Always Go To First Principles"
url: "https://boyter.org/2010/08/principles/"
fetched_at: 2026-05-05T07:02:07.695010+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Always Go To First Principles

Source: https://boyter.org/2010/08/principles/

Recently I was having an issue with some code I was working on for my pet project (A website search solution). Essentially my problem was that Smarty PHP wouldn’t loop through an array I had passed in. After much swearing and complaining I decided to take a step back and run through all of the newbie mistakes. In other words I looked at the problem from first principles.
Turns out the issue was a missing $ before the variable I was trying to loop over. DOH!!!!!
This made me think back to
TechZingLive where Justin and Jason were discussing “Tell it to the bear”
. You know what? They are 100% on the money in
this case
.
I think one of the traps that I had fallen into, (and if I have other developers probably have) is that we think we know whats going with the code we write. If something breaks its the compiler/interpreters fault, or the 3rd party software, or something to do with the alignment of your computer towards Mecca. We loose sight of the fact that the computer only does what we tell it to do. That is, whatever is playing up is most likely our own fault. I think this might be what causes NIH (not invented here) syndrome, since I can recall thinking “I should write my own template language!” while looking for the issue.
By taking that step backwards I was not only able to approach the problem correctly, I also fixed it within 30 seconds. For me its certainly something to keep in mind when trying to fix something that should just work.
