---
title: "Interconnects Podcast: Kimi K3.1 Pro, the new cyber reality, and Muse musings"
date: 2026-10-25
source: "interconnects.ai (Nathan Lambert / Florian Brand), publication_id=48206 post_id=221950500"
author: "Nathan Lambert, Florian Brand"
url: https://www.interconnects.ai/p/podcast-kimi-k31-pro-the-new-cyber
fetched_via: curl + <article> paragraph extraction (Substack HTML, isAccessibleForFree: true)
tags: [newsletter, raw]
---

# Interconnects Podcast: Kimi K3.1 Pro, the new cyber reality, and Muse musings

- **Source:** interconnects.ai (Nathan Lambert / Florian Brand), publication_id=48206 post_id=221950500
- **Author:** Nathan Lambert, Florian Brand
- **URL:** https://www.interconnects.ai/p/podcast-kimi-k31-pro-the-new-cyber
- **Date:** 2026-10-25

---

19
 
 1

 1 ×

 0:00
 Current time : 0:00 / Total time : -46:42

 -46:42

 Audio playback is not supported on your browser. Please upgrade. 

 Podcast: Kimi K3.1 Pro, the new cyber reality, and Muse musings

19
 
 1
 
 Share
 Transcript

 We — Nathan and Florian — wanted to discuss all the messy trade-offs of a busy week in AI and ask all the pressing questions like:

Why did Kimi K3.1 Pro have a mixed reaction with such incredible benchmarks? Will it be adopted?

Were we wrong about the risks of open-weight models and cybersecurity?

Why do cyber experts discuss recent events so differently than AI experts?

What comes next in the few months? What will change our minds?

We will write more about this subject, but wanted to bring you behind the curtain as we aspire to quickly learn more about the cybersecurity industry and trends across the last few years that have been leading us today. We conclude the podcast with some lighter topics, from Muse-maxing to excitement in still hiring junior technical talent. Please send us questions and topics, as we plan to record more of these podcasts going forward.

Listen on Apple Podcasts , Spotify , and wherever you get your podcasts . For other Interconnects podcasts, go here . YouTube ↓

08:15 Kimi’s open-weight cyber principles

15:54 PHP2Shell, LiteLLM, and the new internet

24:00 Abliterated APIs, safeguards, and trusted access

31:41 Anthropic not hiring juniors employees

My thread with Dean Ball about the “boy who cried wolf” story of the frontier labs

Kimi K3.1 Pro on Artificial Analysis Intelligence Index

Kimi K3.1 on Artificial Analysis defensive cyber benchmarks

Open-weight Mythos would’ve been fine take

PHP “hasn’t caused a disaster yet” update

Abliteration.ai serving abliterated models API

Morph serving abliterated DeepSeek via API

Joshua Saxe’s Substack on AI and cybersecurity

Azeem Azhar, “The internet’s Wuhan moment”

Anthropic, “How employment is changing at Anthropic”

00:00:00 Nathan Lambert: We are back with another Interconnects podcast. We are with Florian, eval guy, recently moved to SF. Florian, is Kimi K3.1 Pro , name is a mouthful, going to live up to the benchmark scores, for example on Artificial Analysis , or where is it going to land?

00:00:17 Florian Brand: In the past, the Kimi models always lived up to the expectations, but this release is kind of weird compared to the others. I think it is also partially because they are becoming more professional, and the previous model drops were kind of out of nowhere. This time, which also got some criticism, they launched a bigger social media campaign, which allegedly also involved paying people to post about the model without disclosing.

00:00:56 Nathan Lambert: I think a lot of companies do this and tell you not to mention it, but it’s a mess. It’s bad form. No company should do it. Essentially, one person tweeted a screenshot of the press instructions for Kimi that said, “Don’t say this is a paid promotion.” And to my knowledge, no one has corroborated it after that.

00:01:15 Florian Brand: Yeah, and there are right now a few of these model launches, including by American companies, that are just very obviously astroturfed. We have seen launches where it’s thousands of retweets and a few hundred likes, because it works so well to get the attention. Some of them disclose that it is a paid ad while others don’t. But in general, we have seen the professionalization of model launches over time, and pretty quickly. A year ago, everyone just dropped the model, then patched vLLM afterwards, so no one was actually able to run any of the open models for a while. Now you get all the inference frameworks on day one, you get all the inference providers on day one. Or, which is also what we see more and more, the model creator has a few weeks of exclusive access before they release the weights. And that’s also what’s happening with K3.1 Pro. I think it’s two weeks of exclusive access before they release the model weights.

00:02:38 Nathan Lambert: They said the weights would come out by November 4th. And the headline things... I don’t know if I’m going to be able to share screen. I don’t have this set up on this computer. But the headline is this Artificial Analysis number where it’s ahead of GPT-6 Astra. And then if you look at the Kimi K3.1 blog, they have their headline numbers, which are really strong, and then they also have some numbers later on which seem a bit more jagged. I think it was Terminal-Bench Science , which is 20 points behind GPT-6 Astra. I think there were a few others, like ProgramBench . Do you know Terminal-Bench Science and ProgramBench? Are any of these things that people think are important benchmarks for frontier models? Or how do you explain the fact that on Artificial Analysis the model is top, what, three, four? It’s the two latest Claude 5.5 models, Muse Wonder Full, and then Kimi K3.1, which looks crazy. It just looks like totally crazy scores, and I think everybody is still surprised by it. But then there’s this long tail of details that you use to evaluate a model now. I had posted a thread on Twitter of, “What are people’s impressions?” And there’s a lot of people that are like, “This seems not great,” and then some people that are like, “Yeah, it’s fine.” I don’t know, there’s a mixed bag. Relative to K3, which I think was pretty unanimously, this feels like a big model and the post-training seemed a little bit undercooked for that. Maybe this is just a tiny bit RL fried. We’ll see where we land.

00:04:26 Florian Brand: For the benchmarks, one of the things is that the benchmarks that are right now used by Artificial Analysis, they will post their new version probably very soon after we release this podcast.

00:04:43 Nathan Lambert: We can’t tell you the exact date, but both of us know.

00:04:48 Florian Brand: In general, the Artificial Analysis benchmarks are rather short in terms of time horizon, whereas something like ProgramBench is really long and also very explorative. Other benchmarks are telling the model, “All right, this is the goal, and I want you to reach it,” whereas ProgramBench is more like, “All right, here’s what I want, but you need to explore a lot.” And I think that might be the reason that we see some differences: their RL training is still more towards the exploitative side of model training versus the explorative side, where you need to find the solution somehow before you actually know what you’re doing.

00:05:41 Nathan Lambert: But if you’re using a three trillion parameter model, I feel like you kind of want it to be pretty robust at exploration. Because if you’re going to want to use a model for pretty known coding tasks, like using DeepSeek-V4.1-Flash-1017 , which is not that far behind on these scores, it’s just going to be way faster. It might not be wildly different on cost per task with the actual token numbers. That’s why I think it’s pretty reasonable criticism of this Kimi release: a big model has got to be... Because it’s going to be slower, it’s got to be like Fable, which is just... I still think Fable is really nice if you’re doing very blurry things. I revert to it when checking my slides over sometimes, where I just feel like it kind of gets me a bit better, where Opus is really, really grindy. I think the open-weight models are better in this kind of grindy perspective, because you can just get them to be faster and cheaper.

00:06:44 Nathan Lambert: It seems like Kimi is gearing up for this Flash-style release with their naming change. Previous Kimi models were just K2, K2.6, K3, and now this is K3.1 Pro. So a lot of the company forecasting, investment-y side of interest on Twitter was, a lot hinges on this for Kimi, because it’s kind of true. We’re not the inference experts, but serving the model seems like you’ve got to commit way more resources to serve this three trillion versus this 700 billion parameter model. You’re going to need NVL72 racks, I’m guessing, to do it well.

00:07:21 Florian Brand: To fit the model, you need B300s, one node per model replica, which is kind of awkward, versus other models which you can even fit on H100s, or H200s rather, which are more readily available. Splitting models is always awkward compared to having one model replica per node, or using existing nodes to fit the full weights. So in that regard, three trillion is just out of, or just in the range of what you can host somewhat reasonably, but it is kind of annoying compared to all the Flash models and all the smaller models, where you can use so many of the existing GPUs that people have.

00:08:15 Nathan Lambert: Do you think Kimi’s shooting itself in the foot a little bit by saying it’s slowing its own cyber capabilities? In the blog post, I can read some of this, because it’s really good for people to say. “Open-weight principles. These evaluations frame our open-weight release decision. First, we aim not to release open weights that would extend the absolute frontier of cyber capability. K3.1 Pro’s offensive cyber capability is, by design, below what our pipeline can produce, and remains behind that of frontier proprietary models.” And they go on to say... I don’t know if the mid-training part is in this, but essentially they manipulated the mid-training data to down-weight cyber capabilities and see that that can last into the post-training. Do you think this would reflect upon the other benchmarks that they have, and maybe some of this long-horizon weakness? Or do you think that people could actually separate this?

00:09:08 Florian Brand: I think people can very well separate these things. I talked to a bunch of other people, and I think that style of release is really good. You want very broad access for everyone to find all the bugs and to patch all the bugs, which is net positive for the world. And Kimi saying they still release the capable model for the defensive side, but they don’t want to advance the offensive side. What I’ve heard from cybersecurity professionals is that exploiting and being able to go through or wreck a whole organization is way harder, because you need very long-horizon capabilities, and you need to persist through all the stages that you penetrate. That’s where closed models, especially GPT-5.6 Sol , a model that’s named often in this regard, are just way, way better than open models. And I think that is important. We want all our code to be secure, and that should happen pretty fast. But for this, you don’t need long horizon. You don’t need all the CTF-style challenges. So throwing these out of the training mix is a reasonable decision, and it helps them position against the fearmongering that once an open model with Mythos-level capabilities, which we arguably have in some regards, is released, the world will end. Which we haven’t seen so far, and I don’t think will happen in the near future. So open models get way more scrutiny than closed models in this regard, and them positioning themselves as, “We are the responsible actors,” is a smart move.

00:11:23 Nathan Lambert: Okay, we can transition into the “you can hack everything” part of this segment. There’s a lot going on here, and Florian and I are both not cyber experts, but it is worth discussing, because I’m kind of of the opinion that the cyber experts that I read talk about this from an ecosystem perspective. All measurements like vulnerability detection, time to exploitation, have been on these exponentials before ChatGPT came out, and there wasn’t a step change as AI models came out, and they focus on this ecosystem perspective. But when you come to the AI people, which is our corner of Twitter, people love to debate open versus closed models and Mythos and things like this. And then the messy middle is, what is the effect of the Daybreak programs and Mythos and things like this on broader society? I feel like I’m trying to muddle through this without getting too stuck into any one point of view. But I really don’t think it is that much of an open versus closed and a capability model thing.

00:12:33 Nathan Lambert: I wish I could go relive the Mythos moment, because my impression was that they made it quickly seem like a cyber weapon. I can go revisit their communications about what they actually said, because it might have been more that they were like, “This is a step change in cyber,” and then the government was very scared of it and took it very, very seriously, and then that pipeline spiraled into this communications of the AI safety community potentially forecasting more problems. It’s hard to hold people accountable for what the media ecosystem does, but also if you are the most prominent company in the world, you are partially responsible for how all of this works. So I’ve gotten pushback from people in the program that are like, “We didn’t say that the world would end when Mythos came out. We just said that there’d be a ton of problems.” And in some ways they are right that there are a ton of vulnerabilities being found. But I do distinctly remember the boy-who-cried-wolf vibe of a lot of the AI safety companies over the last few years. I had this exchange with Dean Ball where I was trying to point this out to him on Twitter, and I was like, “Dog, we’ve been doing this for years.” The boy who cried wolf is a classic parable for a reason, and it seems like a bit of a blind spot, and I just can’t understand it.

00:13:50 Nathan Lambert: But we’re in it, and the vulnerabilities are being found en masse, and I would say there’s a slight uptick in visible hackings. It might be that there’s more hackings within the Twitter community. A lot of cyber people I’ve talked to use reported cyber damages, which a lot of them are through ransomware, as the trend to look at. Historically, AI has been attributed to a very, very low percentage of cyber damages. So if cyber damages do skyrocket with attribution to AI, that is a very difficult world. But the vulnerability finding is very, very unsettling, but we don’t know exactly what it’ll translate into. That’s where I stand, and the reason as to why that translation might not happen. For example, I like Joshua Saxe’s work a lot, and he talks about how the supply chain of cyber hackers is very weak. These people tend to have competition. The population are people that self-select because they cannot get better jobs, and this population of people might also not be people that are willing to do cyber attacks that I would describe as loud and very high damage. So I think there’s a very high likelihood that nation-state actors are using AI to collect information and infiltrate at a large scale. But it’s not clear who the people are in the world that are willing to use AI models to cause mass damage in the physical world. And I don’t like that being... That’s a horrible thing to be like, “Okay, we’re going to figure out whether or not that’s true in the next four months,” but it literally might be where we’re at with the number of vulnerabilities out there. And I think you’ve been following the PHP issue, which I don’t know if you want to summarize for people, and then also some of these things that you’ve been following in the commentary after that.

00:15:54 Florian Brand: So the PHP issue is basically that for years there was a bug which allows you, in PHP, to execute code remotely. So anyone can use any PHP website, which are a lot of the websites on the web. WordPress is one of the biggest ecosystems which runs on PHP. And the OpenAI Patch the Planet program, together with some other AI security researchers or cybersecurity researchers, found this bug and then reported it to the PHP Foundation, worked with other actors to patch this, and then released the patch all at once. Because PHP powers so many parts of the web, and it is a really, really strong exploit, really high risk, a lot of websites even went offline for a while just to patch this, which is the right response. And obviously because it was so high profile, and people think about Mythos and think about open model releases, that has kicked off a number of takes that now everyone who can run an open model basically can hack the world. But the interesting thing is that there are numerous reports that the mass exploitation hasn’t happened and isn’t happening yet.

00:17:37 Nathan Lambert: Wait, did you see the tweet about the DeepSeek swarm fixing it ?

00:17:42 Nathan Lambert: I don’t know if it’s real, but somebody that works at a big cloud company was like, “We’re literally seeing mass fixing at scale by somebody, or a DeepSeek swarm.” Great meme. Coin flip on if it’s real.

00:17:59 Florian Brand: But in general, the expectation of some people seems to be that the second it drops, everyone is able to write code and exploit and is able to scan all the websites and do mass damage, and that doesn’t seem to have happened, which is great for the current state of the world. And I think we will see similar things in the future, so very quick fixes by responsible actors, which is the vast majority. Like you have said, the people who work in cybersecurity are experts at their job. They get those jobs, and there is so much money in fixing things. All the cybersecurity firms, Anthropic and OpenAI, all the AI players as well make a lot of money with these programs, so single nefarious actors are the minority. And nation states, I would say, are completely out of that question, because if you are a nation state, you have completely different capabilities. You might run completely different models and abuse these things for a long time. So I wouldn’t say it’s fair to say that now that open models are becoming better at these things, nation states didn’t have these capabilities for a while, or can’t train models to advance their own capabilities. We are basically seeing that the overall dynamics are staying the same, but are accelerated by a lot.

00:19:49 Florian Brand: The other interesting thing, especially if you think about things like ransomware, is that people still haven’t woken up that they need to patch their systems. I’ve had a few friends who work at very small or medium businesses, and they are like, “Oh, yeah, that sounds horrible. Let me check my PHP version.” And it is so far out of life that they don’t get the security patches, because they didn’t update their PHP versions or their systems for years. So they are vulnerable to a bunch of other security bugs, which still weren’t exploited, which is also very interesting. Another thing that plays into the argument that right now the amount of nefarious actors is very small, and things can stay accessible for way longer than people think, is the LiteLLM hack . LiteLLM is a software library where you can use one endpoint and then ping every provider, which basically allows you to save a lot of lines of code. And they got compromised again this week, which, with all the PHP stuff and other security vulnerabilities, just contributed to the impression that everything is insecure. They did a preliminary report that the reason why they got hacked again is that they had an API key committed to GitHub for five months. So it was accessible in some way, or it was readable for five months, and five months later, someone exploited that and used that to spread malware.

00:21:44 Nathan Lambert: I don’t think we’re in a world where we’re defense dominant, but I don’t think that offensive capabilities being higher is necessarily a lot of the bottleneck, which is very messy. But that’s probably why it’s not changing that much, because yes, the cost and ability to do cyberattacks is going way up, but the institutions that are doing them, that doesn’t necessarily 10X their output in what they’re doing. But the defensive side is worrisome. Azeem Azhar had a good piece on Exponential View , which was just, this is day zero of the new internet, and potentially things will never be as secure and op
