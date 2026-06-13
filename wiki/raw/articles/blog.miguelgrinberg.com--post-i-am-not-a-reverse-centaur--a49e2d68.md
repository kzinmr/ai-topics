---
title: "I Am Not a Reverse Centaur"
url: "https://blog.miguelgrinberg.com/post/i-am-not-a-reverse-centaur"
fetched_at: 2026-06-13T07:00:50.560281+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# I Am Not a Reverse Centaur

Source: https://blog.miguelgrinberg.com/post/i-am-not-a-reverse-centaur

About a year ago I wrote on this blog about how
coding with LLMs would not work for me
, even if there were no ethical or environmental concerns preventing me to use them. I'm not going to repeat the arguments I made that time because my views on the subject haven' t changed. What has changed, however, is that the number of contributions I receive on my open source projects has gone up, and nearly all are now made with LLMs.
The other day I had a very depressing thought regarding this. All these people who submit drive-by pull requests to my projects are pushing me to spend more and more of my time reviewing and merging code that was extruded by machines. Cory Doctorow refers to people that perform this function as
reverse centaurs
. He calls these "frail and vulnerable people being puppeteered by uncaring, relentless machines." Ouch!
Am I a reverse centaur now? Is my new purpose as a seasoned software engineer and open source developer to spend my days reviewing LLM code, in spite of having decided that I do not need nor want this technology myself? As you can guess from the title, I'm never going to become a reverse centaur. Let me tell you how I resist the forces that want me to be one.
No more unsolicited pull requests
Back in pre-LLM days, receiving an unexpected pull request (PR) from a fellow coder was a source of excitement and pride. It meant that some random person decided it was worthwhile to invest their time and effort to improve a project of mine and share the result, not just with me but with all of its users.
Today, an unsolicited PR is a red flag. Too many people lazily prompt an LLM code generation tool and ask it to alter the behavior of one of my open source projects to meet their specific needs, without any care or consideration for what is being changed or how it might affect other users. Sometimes these changes make sense and improve the project, but often enough they do not. The submitters rarely care though, they just slap a long LLM generated description and send the PR over, leaving me with the task of figuring out if the change makes any sense at all or is pure slop.
I have decided that I have more important things to do with my life than to spend my days reviewing code produced by LLMs. If you want to contribute to one of my projects, I expect you to be the direct contributor, and to have a genuine interest in improving my project.
The contribution guidelines I include in all my open source projects have these instructions for contributors.
If you are interested in contributing a change to this project, please first introduce the change you wish to make to the maintainer in an issue. Pull requests that are submitted without a previous discussion in an issue may be closed at the maintainer's discretion.
Once the maintainer accepts your proposed change and allows you to work on it, feel free to submit a pull request.
With this process I get to know the contributor and their proposal before there is a big time investment on either side, so it is a win-win for everyone.
In spite of this I still get unsolicited PRs, so clearly some users (or more likely their LLMs) do not read contribution guidelines. My initial task when a new unexpected PR arrives is to determine if there is a person behind it or not, and luckily this is easy to figure out in just a few seconds. If I don't see proof of human involvement, then I'm not interested, so the PR gets immediately closed with no questions asked.
You may argue that with this attitude I'm likely to miss useful improvements or bug fixes to my projects, and I guess that is possible. I really have no way to know without spending time reviewing these unsolicited PRs to separate the good from the bad. When I was sure that every contribution had the effort of a person behind it this review work was justified and I even enjoyed it. In today's slop-filled world this is reverse centaur work and it is not for me, so I only pay attention to PRs that come from engaged contributors.
My advice if you can only code with the help of an LLM and need fixes or improvements in a project of mine is that you don't waste your tokens on a PR, since I will ignore it. Instead, describe the problem in an issue, and let me handle the work. I do not want an LLM-generated novel with chapters, bullet points and emojis, just a simple description of the problem in your own voice. Since you will be saving some of those expensive tokens, you could also consider a donation, which will likely motivate me to prioritize your problem!
Does open source matter anymore?
This is a question that I constantly ask myself, and I do not have a clear answer yet. I still do a lot of coding, both for work and for fun, but in the last few years I have been less interested in sharing the things that I make. I still have enough interest to keep my current open source projects updated, but I have a bunch of recent projects that I can't bring myself to make public.
My perception is that there is less interest in open source, and in coding in general. The main reason I love coding is that it is a challenge, and I think this is actually the same reason why a lot of people prefer to give money to an AI lab and get a machine to spit out code for them, even with the risk of the code being subpar.
Will this trend continue to the point that nobody codes anymore and it is only machines doing it? I hope not, but we'll have to wait and see. I will continue to oppose a future in which we all have to be reverse centaurs, with the machines (and their billionaire owners) calling the shots.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
