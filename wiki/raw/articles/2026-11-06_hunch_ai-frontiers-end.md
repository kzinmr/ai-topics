---
title: "The End of AI Frontiers (John Langford)"
type: article
created: 2026-11-08
updated: 2026-11-08
source: https://hunch.net/?p=13764006
published: 2026-11-06
tags: [microsoft, ai-research, microsoft-research, ai-frontiers, john-langford]
sha256: 3325f156fd645c0a58b74de160ce3555651e6fa9766990fb571ab37b9a528591
---

The End of AI Frontiers – Machine Learning (Theory) 

 Skip to content 

 Machine Learning (Theory) 

 Machine learning and learning theory research 

 Posted on 11/6/2026 11/7/2026 by John Langford The End of AI Frontiers 

 In 2023 after the ChatGPT release, it was clear to me that research needed to be more organized to succeed than was typical within Microsoft Research . The amount of support and focus which other research groups were applying was great enough that even with a clever idea pursued by one person it was likely to arrive late and unconvincing because one person could not move fast enough and the baselines which one person could assemble just were not strong enough to really show that an idea was worth taking flight. Several other folks thought similarly and we organized to create the AI Frontiers sub-organization within MSR. 
 In AI Frontiers, we actively tried to organize coherent research efforts. This was not precisely “top down” or “bottom up”, but rather mostly somewhere in the messy middle. There were disagreements of course, and resolving them was sometimes quite challenging. Compute availability was also an often-severe bottleneck. But at a high level I was under the general impression that the organization was succeeding in doing pioneering things, particularly given the small size of AIF (~50 people) and relative to what we could do previously. Much of the work of AIF was figuring out how to make agents work, for example the Autogen orchestration framework and the Fara computer use agent. In NYC however, several of us were interested in developing new fundamental capabilities such as the Next Latent objective which enables extrapolation, Dion3 which creates an optimized/improved Muon, or the Full Bandwidth Transformer which efficiently makes models function substantially more powerfully via recursion. 
 We also actively tried to share with the rest of MSR. For example, AIF decided to develop a monorepo that was shared by default with all of Microsoft Research. In this monorepo for example was the proven-capable edge scale pretraining codebase I talked about in the COLM keynote last month. This might seem like a minor detail, but the amount effort required to create a well-formed model creation pipeline is substantial and I’m aware of at least 4 efforts (the other 3 not in public-within-MSR repos) trying to develop model building pipelines. 
 In early September we were reorged into Microsoft AI . On the surface this could make sense, because putting two different AI organizations together creates opportunities for better concentration of effort, and there were places where AIF was ahead of MAI and of course vice-versa (MAI is much larger). In practice, there are substantial issues because the philosophy of the ex- Inflection leadership of MAI is incompatible. The core philosophy there is scaling, and aggressively not research. This might shock some folks who naturally think that the way you make better models is via research but there is plenty of evidence that bigger models are better models as far as the quality of the predictions they make and from a business perspective returns to scale are far more predictable than returns to research. In a scaling-only environment of course the primary effort is on getting/making/refining data, which is quite a step away from what we were working on. Aside from the incompatible focus, there was plenty of evidence that they just did not really want us. 
 It’s a tough situation to find yourself in. I consider the scaling-only focus to be both misdirected and not fun. It is an understandable failure mode—scaling is straightforward and it’s common for people to give up on a tradeoff between multiple competing ideals (like innovation and size) by short-sightedly adopting one in totality and dropping the other. But returns to research are real and significant. For example, the Bytedance experiments suggest a variant of the Full Bandwidth Transformer might be comparable to a model of twice the size, implying significant savings in training and inference for the same capability. Do the math—how much is it worth to halve training and inference cost given that the industry has investments approaching a trillion dollars? 
 So I situated my folks as best I could and left. I am quite fortunate in that there are many other people in the world who are capable of seeing the value of research and innovation which is my intrinsic center of interest. Every other founding AIF leadership team member seems to have come to a similar conclusion. 
 This does leave a question: Why not go back to MSR? I chatted with folks a bit but could not get away from two serious obstacles. The first is that I am just not comfortable being at a company where the research I do has no path to real use. I could not get innovation into use (or even seriously considered) when I was in MAI, so the prospects for success from MSR seem quite small. The second is that I’m afraid there’s a breakdown of the basic deal in MSR: do good work and good things happen. As far as I can tell we did good work and were non-consensually reorged away. Unfortunately, I would not be surprised to see that kind of thing continue to happen until MSR leadership develops a will to effectively organize to meet the moment. 
 So AI Frontiers is over. I’m sorry to say that there will not be internships with the folks there in the coming year—I enjoyed working with interns on many occasions. And my best wishes for the folks I leave behind. It is not hard to imagine a Microsoft of the future which becomes attractive for research again if the people in control can develop a little bit more wisdom. 
 Twitter/X thread . 

 Categories Machine Learning 

 4 Replies to “The End of AI Frontiers” 

 Anonymous says: 

 11/7/2026 at 2:19 pm 

 Going through you Who? What? Why? page, I clicked on your collaborators. Seems like Drew Bagnell has let his mindchild.org domain registration expire and it’s been taken over by a pornographic website. 
 Best probably to leave his name up by remove the link. 

 Reply 

 John Langford says: 

 11/7/2026 at 6:50 pm 

 Ah thanks. Definitely a failure mode of the internet. 

 Reply 

 jae kwon says: 

 11/7/2026 at 5:24 pm 

 see gnosh.ai. 
we are raising, and will hire the brightest from your team. 

 Reply 

 Anonymous says: 

 11/7/2026 at 7:28 pm 

 our field has been screwed for 12 years now john 
 you know it, i know it, the real leaders know it. 
 but the one supposed leader who has never been shy about his genealogy has certainly reaped what he has sought for so long, in spite of the innumerable rumours of his competTYveness with his juniors, many of whom he inspired. 
 time to blow this thing up and take back our field 

 Reply 

 Leave a Reply Cancel reply Your email address will not be published. Required fields are marked * Comment * Name 
 Email 
 Website 
 Save my name, email, and website in this browser for the next time I comment. 

 Δ 

 Post navigation 
 Previous Post Previous Curbing AI with Flight Recorders, Brainwash Entrapment Tests, and 3rd Party Evaluation 

 Details 

 A modest proposal 
 How to Contribute a Post 
 Who? What? Why? 
 Why did my comment not appear? 

 Search for: 

 Search 

   Subscribe 
 John on Twitter Recent Comments Anonymous on The End of AI Frontiers John Langford on The End of AI Frontiers jae kwon on The End of AI Frontiers Anonymous on The End of AI Frontiers John Langford on An AI Miracle Malcontent Categories 

 Active (12)

 AI (19)

 Announcements (116)

 applications (4)

 Bayesian (18)

 Boosting (1)

 Code (17)

 Competitions (24)

 Computation (6)

 Conferences (95)

 Coronavirus (2)

 CS (4)

 Deep (5)

 Definitions (11)

 Economics (3)

 Empirical (6)

 Exploration (6)

 Funding (23)

 General (73)

 generative (1)

 Graduates (2)

 Information Theory (4)

 Interactive (5)

 Language (12)

 Machine Learning (331)

 Mathematics (2)

 MDL (1)

 medical (1)

 Meta (4)

 Neuroscience (2)

 Online (38)

 Organization (16)

 Papers (45)

 parallel (1)

 politics (1)

 Prediction Theory (20)

 Privacy (1)

 Problem Design (2)

 Problems (31)

 Questions (3)

 Reductions (32)

 Reinforcement (30)

 Research (54)

 Reviewing
 (24)

 Robots (2)

 Semisupervised (4)

 Solutions (5)

 Statistics (6)

 structured (7)

 Supervised (15)

 Teaching (18)

 Theory (8)

 Trees (2)

 Universal Learning (5)

 Unsupervised (7)

 Vision (6)

 Workshop (36)

 ML Related 

 Gelman—SMCISS 
 ICML Paper Discussion 
 Inductio Ex Machina 
 KD Nuggets 
 Kernel Machines 
 Machine Learning Thoughts 
 MLOSS 
 Reinforcement Learning 
 SM, DM, & ML 
 Wikipedia: Machine Learning 

 Research 

 Computational Complexity 
 Computer Research Policy 
 Geomblog 
 Mathematics 
 Mathematics and Computation 
 Michael Nielsen 
 Oddhead 
 Quantum Algorithms 
 Quantum Pontiff 

 Meta 

 Register Log in 
 Entries feed 
 Comments feed 

 WordPress.org

## HN discussion highlights (item 50406563, 467pts)

[smokel] This refers specifically to "AI Frontiers", a research group within Microsoft Research that focuses on fundamental advances in AI. There is no end in sight to real AI frontiers. Perhaps "The End of Microsoft Research's AI Frontiers Group" would be a less ambiguous title.

[sheepscreek] Yeah, I went down the rabbit hole scratching my head the whole time. This is about the group at Microsoft Research that was disbanded or reorged into what is now Microsoft Research. To the author: 100% need this kind of thinking. It’s a balancing act. Historically though, dedicated labs haven’t had the best track record at commercializing their tech. The skillset differs vastly from running a product-focused business. That said, even within this narrow scope - there are areas ripe for research. 

[xlayn] I see this playing the same way in the other big companies that have a pressure to deliver (cough *value for shareholders*)

[Zigurd] > There is no end in sight to real AI frontiers. That statement is broad enough to be unfalsifiable, but if you narrow it down just a bit to scaling LLMs, maybe there is an end in sight. At least financial markets are skeptical of there being no end in sight. If scaling LLMs really was the road to God in a box, then compute demand would be infinite, and nobody building to meet that demand would have a junk debt rating. Did those money people just not get it?

[frolix] The real news is "The End of Microsoft Research". Langford's group is just one of many that have been parted out over the last year or so. The division that was T&R under Kevin Scott was quietly dissolved about a year ago and MSR was reorged under Azure Security with the AzSec leader as hatchetman for the department. MSR itself doesn't have a future beyond a few years at most I reckon. I don't suspect Kevin Scott will be around much longer either since his department keeps getting reduced and is

[fraywing] To me, all signs point to US over investment in hardware capacity to support the "frontier" when in reality the next major breakthroughs are likely radical optimizations that end in increased consumer training and inference efficiency. I'm not sure how that, combined with open models inching up on frontier intelligence, is compatible with these massive AI IPO valuations? It seems like closed model AI demand has a lot of contingencies that are ultimately fragile and possibly short sighted.

[uptrails] The article is about a guy leaving Microsoft and the disbanding of an internal team called "AI Frontiers".

[senordevnyc] Do you think humanity is just going to run out of problems that need the smartest intelligence? If so, then yeah, increasing efficiency 100x means we hit that point much faster. If not, then it just means we make improvements 100x faster.

[kylestanfield] Everyone wants radically more efficient AI. That doesn’t mean it’s coming any time soon. And when models are twice as efficient, guess what happens next. We try making one twice as big for the same cost.

[joegibbs] If they make more efficient models won’t people just use the big data centres to make and run even bigger more powerful models than they can currently support? Or massive swarms of agents to look at all different avenues of a problem?

[outside1234] Microsoft is a really shitty place to work right now. There are a hundred stories like this all over the company like this.

[rwmj] They've offered voluntary redundancy to a quite large proportion of the staff (a quarter?) so they'll also soon be losing anyone with employment prospects elsewhere.

[vladkens] I see a lot of news about waves of layoffs in large tech companies. Is MS the only shitty place now? I think all of them are, maybe except OpenAI & Anthropic, since they're building something new and are kind of on the "good" side right now.

[AnotherGoodName] This is true in every large company right now. The transformer based approach is seen as a highway to race down in terms of training and building better models with minimal organizational distractions allowed while every company puts its foot down on this highway. Exploratory research into other AI methods is highly discouraged for now and organizations are encouraging transformer based scale out and iteration as a top priority. As an example Meta literally fired it's previously head of AI who h
