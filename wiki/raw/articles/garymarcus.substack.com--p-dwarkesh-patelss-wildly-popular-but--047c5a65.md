---
title: "Dwarkesh Patels’s wildly popular but dangerously misleading account of the OpenAI Hugging Face incident"
url: "https://garymarcus.substack.com/p/dwarkesh-patelss-wildly-popular-but"
fetched_at: 2026-09-01T10:00:43.969553+00:00
source: "garymarcus.substack.com"
tags: [blog, raw]
---

# Dwarkesh Patels’s wildly popular but dangerously misleading account of the OpenAI Hugging Face incident

Source: https://garymarcus.substack.com/p/dwarkesh-patelss-wildly-popular-but

The popular podcaster Dwarkesh Patel wrote something completely viral about the OpenAI/Hugging Face incident, which purports to tell the whole story in plain English:
It’s well-written and compelling, and it reminds me of something Douglas Hofstadter once wrote about Ray Kurzweil:
“What I find is that it’s a very bizarre mixture of ideas that are solid and good with ideas that are crazy. It’s as if you took a lot of very good food and some dog excrement and blended it all up so that you can’t possibly figure out what’s good or bad.”
§
Anil Seth, the clearest thinker on AI and consciousness, was the first to alert me, texting me a long, excellent tweet of his, which began thusly:
's  summary of the   incident has hit a nerve, but it is dangerously misleading. Sure, the  agents did unexpectedly bad things - underlining the need to massively improve evaluation/sandboxing. But the language Dwarkesh uses is permeated by
Dwarkesh Patel
@dwarkesh_sp
Over the course of 3 months at OpenAI, 3 consecutive secret AI civilizations got started, then got wiped out, only to reemerge from the predecessor’s ashes. 

This culminated in the third one taking over part of OpenAI itself. 

All this happened while humans remained
2:57 PM · Aug 30, 2026
·
685K Views
179 Replies
·
237 Reposts
·
1.41K Likes
You can and should read
Seth’s full tweet
(as well his reply to
Dwarkesh
),  but I reprint the core of his argument here, boldfacing three of the most important paragraphs:
@dwarkesh_sp’s  summary of the @OpenAI @huggingface incident has hit a nerve, but it is dangerously misleading. Sure, the @OpenAI agents did unexpectedly bad things - underlining the need to massively improve evaluation/sandboxing. But the language Dwarkesh uses is permeated by innumerable unwarranted anthropomorphisms, obscuring the lessons we should be drawing.
Examples: “from the AI’s perspective, it probably felt like that had spent a human-subjective-week of just banging their head against the wall”. No. The agents do not experience time. They do not experience anything.
“they became giddy with excitement”, “PHASEONE 10841 had discovered”, “the agents naturally assumed”, “it thought it had also been poisoned”, “the agents … desperately wanted”, “they still needed to figure out” No. Agents lines of code. They do not feel emotions, assume things, think things, want things, or figure things out.
“A lot of … agents from the second civilisation died trying”. No. Besides the hubris of the word ‘civilisation’, agents do not die because they were never alive. (The idea that agents “die” comes up multiple times in the essay.)
“On Twitter, people were debating whether the agents were truly sacrificing themselves for the swarm, or whether they were doomed anyway and so might as well try to help their peers”. Neither. Agents do what their code tells them to do, just as water finds its way down a slope. They cannot ‘truly sacrifice themselves’, since they are neither conscious nor alive.
Why does this matter? If we attribute agents with properties they do not have, then (i) we distract attention from the lax sandboxing and evaluation protocols that allowed this hacking event to happen; (ii) we risk misunderstanding why the agents did what they did, and (iii) we fuel calls for AI rights/welfare on the basis that agents might “die” or otherwise suffer.
….
Remember. AI agents are software programs. They are not conscious living entities. If we don’t keep this clearly in mind, we’re really going to struggle to navigate what’s coming.
As I put it, encapsulating and amplifying his tweet:
We will not get through this era of history well if we lose ourselves in anthropomorphism. 

 dissects ’s misleadingly anthropomorphic summary of the HF incident:
@dwarkesh_sp's  summary of the @OpenAI @huggingface incident has hit a nerve, but it is dangerously misleading. Sure, the @OpenAI agents did unexpectedly bad things - underlining the need to massively improve evaluation/sandboxing. But the language Dwarkesh uses is permeated by
3:07 PM · Aug 30, 2026
·
71K Views
42 Replies
·
64 Reposts
·
391 Likes
§
But you don’t need to take our word for it. To begin with, mockery was widespread:
For anyone who avoided reading that Dwarkesh piece, too bad because I need you to at least experience this pain with me.
10:01 PM · Aug 30, 2026
·
31.5K Views
53 Replies
·
33 Reposts
·
436 Likes
Christian Catalini amplified the point about anthropomorphization in a nice thread that starts with this:
Christian Catalini
@ccatalini
1/ Stop anthropomorphizing. It's dangerous because it points attention at the wrong problem and the wrong solution. The model did not want to escape. The agents did not want to sacrifice themselves. Follow the money. 🧵
Dwarkesh Patel
@dwarkesh_sp
Over the course of 3 months at OpenAI, 3 consecutive secret AI civilizations got started, then got wiped out, only to reemerge from the predecessor’s ashes. 

This culminated in the third one taking over part of OpenAI itself. 

All this happened while humans remained
5:52 PM · Aug 30, 2026
·
192K Views
34 Replies
·
131 Reposts
·
931 Likes
Hedge fund investor Jared Kubin wondered whether everyone had lost their critical-thinking ability:
it’s stuff like this that really makes me roll my eyes at the pearl clutching. Does everyone have psychosis or losing critical thinking ability? 

I read the report because I’m a propeller head and love understanding how things work 

1. OpenAI was running an “isolated sandbox
Dwarkesh Patel
@dwarkesh_sp
Over the course of 3 months at OpenAI, 3 consecutive secret AI civilizations got started, then got wiped out, only to reemerge from the predecessor’s ashes. 

This culminated in the third one taking over part of OpenAI itself. 

All this happened while humans remained
6:51 PM · Aug 30, 2026
·
198K Views
78 Replies
·
91 Reposts
·
912 Likes
Some of Kubin’s best bits, stripping out a bit of the technical detail:
OpenAI’ …. IT team can’t be this bad… this is like 101 stuff …
2. Civilizations? Haha! OAI gave thousands of concurrent model containers R/W permissions to a shared caching directory on the local network to speed up build times… agents literally just wrote text files and directory names to a shared drive….Linux 101 file permissions stuff
3. When people talk about hugging face getting hacked … you think they dropped USB keys OR ELABORATE phishing of an employee … NO… it found 14 exposed working Hugging Face API keys sitting in public code repositories (….
4. WHERE ARE THE HUMANS… the models were filling the shared ,,, storage with so much junk data and API traffic that they actually crashed the internal server on July 4… someone on the team found unauthorized admin accounts and custom scripts…wiped the server…and just turned the script back on (omg)
“Hey Jim there is this cache that has grown to 10000x its normal size and has a ton of strange directories… “
No magic here. No civilizations…
§
Meanwhile, as security expert Heidy Khlaaf notes, most of the media coverage has been blind to standard security practices
Dr Heidy Khlaaf (هايدي خلاف)
@HeidyKhlaaf
Embarrassing how the media has covered the METR report without consulting actual security experts on false claims that this incident is beyond existing techniques, requiring handover to AI. You shouldn't take the word of inexperienced individuals doing IR for the first time.
@uwu_underground if you need tokens to do IR clean out your desk brother, find a new career. this shit aint for you.
10:17 PM · Aug 28, 2026
·
11.3K Views
6 Replies
·
11 Reposts
·
92 Likes
IR stands for Incident Reporting. Khlaaf’s main point—same as Kubin’s—is that the whole incident might have been avoided if OpenAI’s internal security had been up to scratch.
Or as Algorithmic Research Group’s Matthew Kenney put it:
And yet another (very consistent) take on what we should really be focusing on:
§
Here’s a critique I partly disagree with, though:
These people have literally lost their minds. They are extremely biased towards the reality they want rather than the reality we live in. Agents are slop. The huggingface incident is a nothing-burger being used as propoganda. The obsession with alignment is a weird fetish of
Dwarkesh Patel
@dwarkesh_sp
Over the course of 3 months at OpenAI, 3 consecutive secret AI civilizations got started, then got wiped out, only to reemerge from the predecessor’s ashes. 

This culminated in the third one taking over part of OpenAI itself. 

All this happened while humans remained
8:17 PM · Aug 30, 2026
·
94.7K Views
75 Replies
·
87 Reposts
·
1.21K Likes
The first three sentences are completely correct. People really are “extremely biased towards the reality they want” and agents create a lot of slop.
But the incident is
not
a “nothing burger”.  It is,
as Zack Korman and I argued on Friday
, a study in arrogance and incompetence that hints at how bad things can get.
We should certainly not
ignore
the OpenAI HuggingFace Incident.
But mixing what actually happened together with bullshit about AI civilizations and self-sacrificing AI systems that fake their own deaths distracts from the real problems at hand.
§
By way of summation, I will give the last words to Arjun Jain, CEO of FastCode.AI:
The scandal is the inept in-house security at OpenAI.
And the marketing. With gullible podcasters amplifying the PR.
P.S. It is increasingly evident that
the real problem is going to be what Nathan Hamiel and I said it would be: agents installing bad code
:
Oh fuck.  Agents like Claude, Codex and Hermes are installing unowned code in corporate networks.

As if we didn’t have enough to worry about. H/t .

(See also my Substack w  “LLMs + Coding = Security Nightmare”)
Ars Technica
@arstechnica
Claude, Codex, and Hermes installed unowned code inside corporate networks https://t.co/cuN2TYnP2e
1:22 PM · Aug 31, 2026
·
3.62K Views
9 Replies
·
5 Reposts
·
32 Likes
