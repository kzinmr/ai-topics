---
title: "Who’s behind Warp? - Meet the team"
source: "Warp Blog"
url: "https://www.warp.dev/blog/whos-behind-warp-meet-the-team"
scraped: "2026-05-10T01:28:25.280711+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Who’s behind Warp? - Meet the team

**Source**: [https://www.warp.dev/blog/whos-behind-warp-meet-the-team](https://www.warp.dev/blog/whos-behind-warp-meet-the-team)

Company
Who’s behind Warp? - Meet the team
Agata Cieplik
September 1, 2021
My idea for a perfect opening line of this blog post was to use a quote about the importance of building a great team. I scrolled through pages of quotes from personas such as Henry Ford, or Michael Jordan, eventually settling on… nothing. We all know that teamwork is critical and a huge part of engineering work, no need to back this up by famous people’s quotes! It becomes even more important in small companies and startups, such as Warp—where everyone works together to deliver the best terminal experience to other developers. In the last post we uncovered a little bit about
how we think about building the product;
in today’s, I’ll introduce you to people behind Warp and the story of how we built the new terminal!
Why did I join Warp?
Let me start by telling you my part of this story.
As a person who rides a 700lbs motorcycle that doesn’t have a reverse (try parking that thing!) and a digital clock is its most advanced piece of technology; who writes her code in Vim and still mixes all the ingredients for the cake manually—I clearly like to... do things in a more traditional way. No wonder the terminal has been my main tool ever since I started working as an engineer.
I was initially very skeptical about Warp—after all bash scripts,
grep,
sed
and
awk
can already get you a pretty long way when working with the terminal, right? I was still curious about what the company has to offer, and that’s why I joined one of the first user research sessions. I even borrowed a MacOS laptop specifically for this!
This was the first time I met the entire Warp team and got to try the application. Learning about the roadmap (especially the team features that will improve efficiency and safety of devops work!) and seeing how user-focused the team is, was what got me excited about the product and the company. 2 months ago I quit my job as an Infrastructure Software Engineer in Dropbox, and joined Warp—the company that builds a next-gen Rust-based terminal.
Why did Zach decide to build a terminal?
Zach, whom you might’ve seen on
Twitter
or a recent
webinar
(talking about Warp, obviously), is the CEO of Warp. He previously worked as a Principal Engineer at Google, CTO at Time and co-founded the venture-backed startup SelfMade, yet his interests circle around improving the developer’s experience.
Zach Lloyd, Warp's CEO
There’re plenty of tools around that improve the development process in one way or another—focusing on a broad group of engineers, or on a very specific niche. However, only 2 are truly used by almost every programmer there is—they are IDEs and code editors or a terminal. The former already went a long way—we’ve had Eclipse and JetBrains, or IntelliJ; there was notepad and Atom and Sublime; and nowadays VSCode seems to be the
majority’s favorite IDE and code editing tool
.
On the other hand, the terminal stayed the same for almost 40 years (and still counting)! It’s slowly evolving with extra functionality coming from new shells (like
fish
) or prompt-tools (like
starship.rs
). Yet, the main experience has stayed the same, and modern terminals still emulate the physical ones, implementing the subset of functionality from
VT100
(hence the correct term is actually “terminal emulator”). Lack of innovation in this area is what made Zach take a closer look at building a terminal. And that’s how Warp was born.
People behind Warp
Soon, Shikhiu, Michelle, and Aloke joined Zach in the effort of working on Warp. The initial prototype was an Electron app, though the poor performance pushed the team to pivot and rewrite the application in Rust. Besides making Warp an OS-native, and blazingly fast application which utilizes GPU rendering, Rust is a language with a strong community support and tools that make it easy to ramp up new developers (Rustlings, we’re looking at you!). As a result the team (with support from Nathan Sobo—the Atom editor creator) created a Rust UI framework which we plan to open source in the near future.
Michelle, Aloke & Shikhiu
Michelle used to work as an engineering intern in Facebook, Slack, and Robinhood. She also pursued an entrepreneurial path co-founding the first health tech incubator in Yale and creating her own health tech app during her college years. Viral growth and user feedback loops are clearly her thing, however, not the only thing. Michelle has a black belt in taekwondo; loves watching movies and analyzing them for hours afterwards; and recently she started to learn how to drive (on the streets of New York City!).
The only person who did not pick up Rust (just yet), is Shikhiu. His excuse is being the Founding Designer. As a master of Figma, Shikhiu creates mockups of new Warp features in minutes, helping the team visualize the work and iterate faster. He recently told me he’s into plants, which would explain why the “leafy” terminal theme (soon to ship in Warp) is so beautiful. He used to work at Adobe and later on at Google where he led a team of 30+ designers on design for the Docs suite, yet (luckily for us) he chose to join us to reimagine the terminal product experience!
Work in progress of themes in Warp - with "leafy" being one of the concepts!
‍
Working as a TL for Google Docs, Aloke had already collaborated with Shikhiu during his time in Google. He also came across multiple TODOs left in the Google Docs codebase by the mysterious
zachlloyd
, but hadn't had a chance to work with Zach prior to joining Warp. Before his interview with Warp, Aloke dropped a very sharp knife on his foot, but decided to tough it up and pass the interview with a bleeding foot. This definitely showed how dedicated he is, though we are all glad that he saw a doctor and his foot is now fully healed… Besides cooking as a hobby, Aloke lifts (not just our spirits) and is very much into public transportation. He gets triggered by lack of periods at the end of the comment, since that makes it an
incomplete
sentence—I like to think it was the reason he started working on
completions
in Warp.
Currently, Warp consists of 7 engineers with Zheng, Chuck, Kevin and me joining over the course of the last 6 months.
Zheng, Chuck, Kevin & me all wearing our Warp's T-Shirts
Chuck plays a critical role in the team since he’s the only person with prior Rust experience. Besides being a mentor, who leaves helpful and constructive feedback in our PRs, Chuck collects
Pez candy dispensers
and can solve a Rubik’s cube in under 1 minute. One of the things that drew him to Warp is being able to improve developers’ experience first hand—he used to work in the devtools team in LinkedIn and maintains
Volta
tool manager. Working on the terminal was a logical next step.
After a few years of working at Dropbox, Zheng decided to dive into the startup world. First, she worked for Gem, and later on met Zach and the team. She deeply cares about the work culture, so her joining Warp says a lot about the company. She likes to travel, pet cute animals and drink good wine; and also she likes to dig really deep into why and how our users use the terminal and other tools day to day. That’s why her current main focus is driving the tmux-like experience in Warp.
Kevin is our most recent hire. He joined as a full-time engineer only a month ago, but has been working part-time at Warp for the past year. He spent his college years traveling to different countries while continuing the education remotely and recently graduated. As part of his international adventures, he interned in a Japanese company in Tokyo for 2 summers, and thanks to that polished not only his engineering skills, but also learned to speak the language! During his internships he tried himself in different fields, including data science and ML, and figured that he’s really interested in developing tools for other engineers, wanted to work on something that will have a direct impact on users and was pretty much a blank canvas. Warp matched his interests perfectly.
Over the summer, we also worked with Saumya & Matt—summer interns who delivered functionality such as notification on long running commands and custom theming. Big thanks to both of you!
Working at Warp
The team works remotely and is spread across different time zones (though we recently opened an optional office space in NYC!). The company was founded during the peak of COVID-19 pandemic, so it couldn’t have been different anyways.
We meet daily to discuss progress and show demos of new features, and organize more Zoom meetings whenever necessary. As a group of very opinionated people (who in the tech industry isn’t?), we sometimes tend to stay online longer, discussing new ideas, making sure that everybody has a space to express their point of view. Somehow we still manage to make the majority of the decisions unanimously - unless it’s about the fate of the
ctrl-r
keybinding… In those moments of doubt, Blue’s (Zach’s dog) appearance in the background cheers everyone up, especially when he tries to eat our CEO’s dinner. Altersnatively, Backup (my dog) sometimes comes to the standup and adds his voice to the pool of our opinions.
When it comes to figuring out the road map for Warp, we try not to rely on our personal views only. Hence, the closed beta program and user focus groups - both helping us learn what’s the right set of features to build next. Zach wrote about our
8 product principles
in a separate post, and you can read more about the team’s culture and approach on his blog:
thezbook.com
.
And most importantly—if you feel like our culture suits you and you’re passionate about bringing the developers’ experience to the next level—we are
hiring
and would love to work with you!
Related articles
Apr 28, 2026  ·  4 min
The virtuous loop of open, automated development
With today’s open-sourcing of Warp, our goal is to create a new way of building, where humans and agents collaborate in the open to ship better software, more quickly.
Mar 16, 2026  ·  8 min
What happens when you give the company 4 hours to automate everything
The Warp team held a company-wide hackathon to build with Oz, our cloud agent platform. Here's every project, from docs migrations to churn detection, that shipped in just 4 hours.
Feb 10, 2026  ·  12 min
Introducing Oz: the orchestration platform for cloud agents
Run hundreds of coding agents in parallel with full visibility and full control
