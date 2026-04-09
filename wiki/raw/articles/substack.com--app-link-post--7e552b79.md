---
title: "Mistral: Voxtral TTS, Forge, Leanstral, & what's next for Mistral 4 - w/ Pavan Kumar Reddy & Guillaume Lample"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=192356063&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTIzNTYwNjMsImlhdCI6MTc3NDg5ODczOSwiZXhwIjoxNzc3NDkwNzM5LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.C9LjIOnZKTKd4x6GW7dC9Orel99Rkzd5dWPWjpyMQkU&utm_source=substack&utm_medium=email&utm_content=play_card_show_title#play"
fetched_at: 2026-04-09T16:28:47.516302+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# Mistral: Voxtral TTS, Forge, Leanstral, & what's next for Mistral 4 - w/ Pavan Kumar Reddy & Guillaume Lample

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=192356063&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTIzNTYwNjMsImlhdCI6MTc3NDg5ODczOSwiZXhwIjoxNzc3NDkwNzM5LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.C9LjIOnZKTKd4x6GW7dC9Orel99Rkzd5dWPWjpyMQkU&utm_source=substack&utm_medium=email&utm_content=play_card_show_title#play

Mistral has been on an absolute tear - with frequent successful model launches it is easy to forget that they raised
the largest European AI round in history
last year. We were long overdue for a Mistral episode, and we were very fortunate to work with
Sophia
and Howard to catch up with
Pavan
(Voxtral lead) and
Guillaume
(Chief Scientist, Co-founder) on the occasion of this week’s
Voxtral TTS launch
:
Mistral can’t directly say it, but the benchmarks do imply, that this is
basically an open-weights ElevenLabs-level TTS model
(Technically, it is a 4B Ministral based multilingual low-latency TTS open weights model that has a 68.4% win rate vs ElevenLabs Flash v2.5). The contributions are not just in the open weights but also in open research: We also spend a decent amount of the pod talking about their architecture that combines auto-regressive generation of semantic speech tokens with flow-matching for acoustic tokens (typically only applied in the Image Generation space,
as seen in the Flow Matching NeurIPS workshop from the principal authors
that we reference in the pod).
You can catch up on
the paper here
and the full episode is
live on youtube
!
00:00 Welcome and Guests
00:22 Announcing Voxtral TTS
01:41 Architecture and Codec
02:53 Understanding vs Generation
05:39 Flow Matching for Audio
07:27 Real Time Voice Agents
13:40 Efficiency and Model Strategy
14:53 Voice Agents Vision
17:56 Enterprise Deployment and Privacy
23:39 Fine Tuning and Personalization
25:22 Enterprise Voice Personalization
26:09 Long-Form Speech Models
26:58 Real-Time Encoder Advances
27:45 Scaling Context for TTS
28:53 What Makes Small Models
30:37 Merging Modalities Tradeoffs
33:05 Open Source Mission
35:51 Lean and Formal Proofs
38:40 Reasoning Transfer and Agents
40:25 Next Frontiers in Training
42:20 Hiring and AI for Science
44:19 Forward Deployed Engineering
46:22 Customer Feedback Loop
48:29 Wrap Up and Thanks
swyx:
Okay, welcome to Latent Space. We’re here in the studio with our gues co-host Vibh u. Welcome. Thanks. Excited for this one as well as Guillaume and Pavan from Mistral. Welcome. Excited to be here.
Guillaume:
Thank you.
swyx:
Pavan, you are leading audio research at Mistral and Guillaume, you're Chief Scientist,
swyx
Host
(00:05) Okay. (00:05) Welcome to Lean Space. (00:06) We’re here in the studio with trustee co-hosts, Vibhu. (00:09) Welcome.
Vibhu
Host
(00:11) Very excited for this one.
swyx
Host
(00:12) As well as Guillaume and Pavan from Mistral. (00:15) Welcome. (00:16) Excited to be here. (00:17) Thank you for having us.
(00:18) Pavan, you are leading audio research at Mistral and Guillaume, you’re a chief scientist. (00:23) What are we announcing today where we’re coordinating this release with you guys?
Guillaume
Guest
(00:26) Yeah, so we are releasing Voxtral TTS. So it’s our first audio model that generates speech. It’s not our first audio model. We had a couple of releases before.
(00:35) We had one in the summer that was Voxtral, our first audio model, but it was like a transcription model, ASR. Like a few months later, we released some update on top of this, supporting more languages. Also a lot of table stack features for our customers, context biasing, precision, timestamping and transcription. We also have some real-time model that can transcribe not just at the end of the level.
(00:56) You don’t need to fill your entire audio file, but that can also come in real-time. And here, this is a natural extension in the audio, so basically speech generation. So yeah, so we support nine languages, and this is a pretty small model, 3D model, so very fast, and also state of the art. Performed at the same level as the base model, but it’s much more efficient in terms of cost, and also much, in terms of cost, it’s also much cheaper, only a fraction of the cost of our competitors.
(01:22) And we are also releasing the work that this model is running.
swyx
What’s the decision factor?
Guillaume
It’s a good question.
swyx
There will be more. Yeah, Pavan, any sort of research notes to add on?
Pavan:
But it’s a novel architecture that we develop inhouse.
We traded on several internal architectures and ended up with a auto aggressive flow matching architecture. And also have a new in-house neural audio codec. Which, converts this audio into all point by herds latent [00:02:00] tokens, semantic and acoustic tokens. And yeah, that’s that’s their new part about this model and we’re pretty excited that it’s, it came out with such good quality and Jim was mentioning. Yeah, it’s a three B model. It’s based off of the TAL model that we actually released just a few months back and insert trunk and mainly meant for like the TTS stuff, but they need text capabilities are also there. Yeah.
swyx:
So there’s a lot to cover.
I always I love any, anything to do with novel encodings and all those things because I think that’s obviously I creates a lot of efficiency, but also maybe bugs that sometimes happen. You were previously a Gemini and you worked on post training for language models, and maybe a lot of people will have less experience with audio models just in general compared to pure language.
What did you find that you have to revisit from scratch as you joined this trial and started doing this? At least
Pavan:
when it comes to, for, I think the, there are two buckets, I guess the audio understanding and audio [00:03:00] generation. The audio understanding, like the walkthrough models that Kim was mentioning that we released earlier.
The walkthrough chat that we released I think July last year, and the follow up transcription only, models family that we released in January, that would be one bucket, and the generation is another bucket. I think. You can also treat them as a unified set of models, but currently the approaches are a little different between these two.
To your question on how audio is fed to the model? In the understanding model, it’s very similar to actually Pixar models that we also released,
swyx:
yes.
Pavan:
That’s
swyx:
amazing.
Pavan:
It was pretty, I, that was the first project I worked on after joined Misra. It was pretty, pretty nice. And Wtu was very similar in spirit.
I guess So we feed audio through an audio encoder similar to images through a vision encoder, and it produces continuous embeddings and which are fed as tokens to the main transformer decoded transformer model. Yeah. On the model output is just text. So on the output side, there is nothing that needs to be done in these kinds of mode.
I [00:04:00] guess the interesting part of what the generation stuff is, the output now has to produce audio and. The approach that we have is this neural audio codec, which converts audio into these latent tokens. There is a lot of existing attrition and a lot of models which are based off of this kind of approach.
And we took a slightly. A different, design decisions around this. But at the end of the day, the neural audio product converts audio into a 12.5 herdz set of latents. And each latent is, has a semantic token and a set of acoustic tokens. And the idea is that you take these discrete tokens and then feed it on the input side.
There’s several ways to use this at each frame, but we just sum the embedding. So it’s like having key different vocabularies. Combine all of them because they all correspond to one audio frame on the input side. The output side is the interesting part on the output side, the, it’s not the, I don’t know if it’s the most popular, but one.
Popular technique is to have a depth transformer [00:05:00] because you have K tokens at each time step, like with a text, you just have one token at each time step. So you just do predict the token from the vocabulary with, yeah, with just, you get probability
swyx:
This’s a very straightforward text. Very
Pavan:
straightforward.
swyx:
Yeah.
Pavan:
But if you have K tokens, then the name thing would be to predict all of them in paddle. That doesn’t work. At least that doesn’t work that well because audio has more entropy. And the, one of the techniques people use is this depth transformer where you you almost have a small transformer, or it can be L-S-T-M-R in as well, but people use transformers and you predict the K tokens in auto aggressive fashion in that.
So you have two auto reive things going on.
Pavan:
So the thing we did differently is in, instead of having this auto aggressive K step prediction, we have a flow matching model. Instead of modeling this as a discrete token set we trained the codec to be both discrete and continuous to have this flexibility.
So we did try the discrete stuff too, and which it works well, but the continuous stuff works just better. So yeah, we took this flow matching, so the, it’s a flow [00:06:00] matching head, which takes the latent from the main transformer and like kind in fusion, it’s denoising, but in this flow matching itself, velocity estimate.
So you go from this noise t all the way to there. Audio latent, which corresponds to the 80 millisecond audio and then, which is sent through the work order to get back the 80 millisecond audio frame.
swyx:
Yeah. Is this the first application of flow matching in audio? Because usually I come across this in the image.
Pavan:
Yeah. Actually, in some sense there are models flow matching models in audio, but I think this specific combination I could be wrong. There could be somewhat. No. I haven’t seen. I haven’t seen much work in this, so I think it’s novel and a lot of it’s just a way bigger community, so they, I think they pioneer a lot of these diffusion flow matching work, and it’s interesting to adopt some of the ideas there into audio and,
swyx:
yeah.
Pavan:
Yeah, I’m, personally that’s the think part which is trying out about. One of more meta point is unlike text, even in vision, I think this is true, but in [00:07:00] audio step literature that there is no.
Winner model, yet there is no, okay, this is the way you do things. It’s it’s still by, I think people are still iterating and figuring out like what’s the best overall recipe. I guess the idea. Pretty sure there are models which are also completely end-to-end, like NATO audio. NATO audio, but it’s still not come to a convergence point where this, the right way to think that.
That also makes. A space pretty exciting to explore.
Vibhu:
What are some of the ways to look at it?
Vibhu:
There are ways where you can do diffusion for audio generation, but if you want like real time generation, that’s a big thing with the approach I’m assuming that you took. Yeah. And also like how do you go about evaluating different axes of what you care about, yeah,
Pavan:
good point. I think we so you can do just flow matching diffusion for the whole audio. We didn’t even go down that path because one of the main applications is voice agents and we want real time streaming, and that’s the use case. That’s not the only use case, but that’s one of the primary use cases we want to get to.
So we [00:08:00] picked the auto aggressive approach for that. And within the auto aggressive space, again, you can do chunk by chunk or you can do so we picked the. I think at least personally prefer the operations, which are the simplest, and so we try to see, can we just add audio as just another head to our regular transformer decode model because that kind of makes it easier for eventual end-to-end modeling of audio text native modeling.
Yeah. And it works pretty well. So I guess we went with that and we tried a little bit, but the flow matching head itself, like we had a discreet. Diffusion kind of approach, which also works well, but the flow matching work better.
swyx:
I was just curious about how you also think about this overall direction of research.
Do you basically, when you work with the audio team, do you set some high level parameters and then let them explore whatever, or how does it work between you guys?
Guillaume:
No I think the way it works is that we are the, we are prioritizing together, I think, what are the most important features because there are many things we can do [00:09:00] in audio.
Yeah, I think we try to. These are like how we should do things, for instance. Ultimately what we want to do is to build this through duplex model, but we are not going to start this start there directly, I think is. Some of the project people are doing, but
swyx:
just to confirm, full effects means it can speak while I’m speaking or,
Guillaume:
yeah.
Okay. Audio. Yeah. Yeah. So intimately we’re going to get there, but for us it was, we decided to take it like a step by step. So we start with whatever is the most important. I think support customers, which is the transcription is the most popular use case. Then the speech generation, Soviet time, just a bit before that.
And then actually to be like more, but try combining everything all together. But but yeah, we thought it was also important to like separate things and optimize each capability one by one before we
swyx:
measure of that together. And the super omni model. But
Guillaume:
very interesting because as Par said, it’s when you work on some other domains of this airline and everything, there are many areas where I think it’s not as interesting.
For instance. Many places, it’s essentially just around data or like creating new environments on a lot of kind [00:10:00] of easy things. But things were, I think the research is maybe not as interesting. Were in audio. There are so many ways to actually build this model. So many ways to go around it. That’s the sense I think is really interesting.
And what we also tried for speed generation is that we tried multiple approaches. What was interesting that even though they were extremely different, they under the big know the particles but the for matching turned out to be quite more natural. So we are happy with this.
swyx:
Is there intuition why it maybe like flow matching is just models speech better in some natural fundamental, latent dimension?
Pavan:
No, I think the main thing is e even at a particular time step, there is a distribution of things.
swyx:
Yes.
Pavan:
To be predicted like the way you inflate. So you already know the word that you’re speaking and Yeah. The intake space, let’s say the word maps register a single token for simplicity.
In most cases it does. So there is not a lot of so you just pick the word, but with within audio, even the same word could, even with your own voice, could be inflicted in so many different ways. And I think [00:11:00] any approach which like models this distribution and. And flow matching is one, one of the take.
It’s not the only one at all, but it’s a one which works pretty reasonably well. I think that’s better. So you have to pick across several different, the intuition I have is it’s, there are some, several different clusters each corresponding to some specific way you would inflict, pronounce that thing.
And you can’t predict the mean of it because that corresponds to some blurred out speech or something like that. But you have to pick one. And then like sharp
swyx:
conditional inference.
Pavan:
Yeah, exactly.
swyx:
Is that all covered under disfluencies, which is I think the normal term of art. Pauses intonations. By the way, I have to thank Sophia for setting all this up, including like some of these really good notes because
Pavan:
Yeah.
swyx:
I’m less familiar with the audios for me.
Pavan:
No. I think dis dismisses are definitely one such Eno defenses is more like
swyx:
which is arms are.
Pavan:
Yeah, arms. And also repeat like you like,
swyx:
yeah.
Pavan:
You do this full of words, your thinking, so you repeat the word.
swyx:
Okay. Whereas intonation is like a diff, it’s up up [00:12:00] speak and all this.
Okay.
Pavan:
Yeah. So I think there is a lot of like entropy. And modeling it as a distribution. And a, any technique which helps with it and the depth transformer is a conditional way of modeling this. And Transformers actually really good at it, even though that’s a mini transformers. So I think that worked pretty well too for us too.
It’s just that the main concentration is when you have a depth transformer. If you have K tokens, you need to do K auto steps, right? Even though it’s a small thing, it’s K steps, which is very vacant, say heavy, but flow matching. We were able to cut it down significantly. So we are able to do the inference in quad steps or 16 steps and it works pretty well.
And there are more normal techniques to bring it down even further to like, in extreme case, one step like we’re not doing it yet, but it at least the framework, LEDs itself to more efficient and Yes.
swyx:
And the image guys have done.
Pavan:
Yeah.
swyx:
Incredible work guys. Yeah.
Pavan:
It now you just. Send a prompt and you get an image.
swyx:
Yeah. Surprisingly not enough. I think image model labs use those techniques in production. I think it’s, I feel like it’s a lot of research demos, but [00:13:00] nothing I can use on my phone today.
Guillaume:
The thing, there’s a thing that would be interesting here is that since, indeed I’ve been so much sure that has been done in the vision community compared to radio dys, stomach, I think there are so many long infra Yeah.
And there are so many things we can do to actually improve this further. So it’s our first version, but we have so many ways to exist, much better and much more efficient, cost efficient, so
swyx:
yeah.
Guillaume:
So really it’s not a new field at all, of course, but there are still so many things that can be done.
Perfect. It’s
swyx:
nice. I should also mention for those who are newer to flow matching, I think the creator, this guy’s name is Alex, he’s done I think in Europe’s maybe two Europes as ago. There was, there’s a very good workshop. There’s one hour on like this matching is I would recommend people look that up.
That’s the other thing, right?
swyx:
The efficiency wise, like I, I imagine like the reason is open weights the reason you pick 3.6 B backbone it you are 3.4 B you are, try to fit to some kinda hardware constraints. You kinda fits some kinda basic constraints. What are they?
Guillaume:
Not necessarily, I think something we care about in our model that they’re efficient.
So we have a [00:14:00] lot of separate model, for instance. So we have this that is very small, very efficient. We also have a small OCR model that is available. Good, highly efficient as well. And I think on a project maybe there, I think companies are going to take is to have a coverage general model that will do a bit of everything.
But that is also going to be expensive. On here. What want say is if you care about this specific use case, if you can actually use this model, it just does that. It’s extremely good at it. Survey, very efficient. That’s why we can actually add. We do, but also OCR that are like really good at that.
And that would be much more cost effective factors and the general model that will contain a lot of capabilities you don’t really need. So yeah. So we’re doing like general model, but also like more customized model. This,
Vibhu:
how does it compare to other TTS models? It’s, we are going follow open wave.
We’re just dropping it. I think it’s pretty good.
Pavan:
Yeah, I think it’s pretty good. Like it, it’s definitely one of the best. For sure. It’s probably I would say it’s the best open source model, but
Vibhu:
decipher themselves.
swyx:
Yeah.
Vibhu:
Why now? How does it fit into broader ral vision? How do you see voice agents?
How do you see voice? I think every year I’ve heard, okay, you’re a [00:15:00] voice. You’re a voice. There’s a lot of architectural stuff. There’s a lot of end time that see it, your solving, but where do you see voice setting?
Guillaume:
We had so many customers asking for voice. That’s also why we wanted to build it.
What’s interesting in this domain is that. In a sense, if you take something simple like transcription it doesn’t seem like something that should be very hard to do for a model. It’s essentially, it’s pattern recognition. It’s classification on this. Models are very good at classifying, right?
Or nonetheless, when you talk to them it’s not there yet, right? It’s not, you don’t talk to them the same way you talk to a person. On something, maybe people don’t realize it. It’s in English it’s still much better than in any user language, even compared to French instance. If you talk to this million in French, when you see people talking to this they’ll talk very slow.
They’ll articulate as much as they can. So it’s not natural, right? We’re not yet to this. And I think, yeah, maybe the next generation will not know this, but yeah, I think people that. But our edge will actually always keep this bias speaking very slowly when they talk to this model. Even if maybe, probably in a couple of years, maybe next year it’ll not be necessary anymore.
But yeah. But what’s interesting is to see that yeah, even for like languages [00:16:00] like yeah, French and Spanish Germans that are not no, no resource on religion. You have a lot of audios there on still it’s not as good. And I think a consequence. Because then for this, I suppose just is not as much energy, as much effort that has been put done in some other mod that for some vision or like coding.
But but yeah, there’s still a lot of progress to be done. I think it’s just a question of doing the work and it’s clear path I think to get there.
Pavan:
It’s a little fascinating because I worked on Google Assistant I think while back at this point, but it’s, I think it’s, it like when you take a step back, it’s fascinating.
It’s not that long ago. It was like four years ago or five years ago, and it’s now it’s completely audio in, audio out and the function calling and the whole thing happens completely end to end. And in a very natural,
swyx:
yeah,
Pavan:
natural way and still ways to go. Kim was telling, even despite all the previous, it’s not like you’re speaking to a person.
When you talk to any of these agents, bots, or voice mode kind of situation, it’s still like a gap. I think that’s the great part and I feel like with even the existing [00:17:00] stack, we should be able to get to this very natural speech conversational abilities soon enough I guess.
And we’ll also hope. I get that
Guillaume:
on this kind of the next step, right? Because when you talk to these agents, like usually people are just writing to them and sometimes they’ll this very clear, for instance, you are, you want to write code, but you are, you have a very clear idea of how you want the model to implement what you in mind.
But so here you are able to spend a lot of time writing. So it’s not really efficient on audio is really like a natural interface that is just not there yet, but I think it’s just gonna be the place.
Vibhu:
How’s it like building, serving, inferencing, like we see a lot about, it’s very easy to take LMS off the shelf, serve them.
Fine tuning, deploying. I know you guys have a whole you have Ford, you have a whole stack of customizing, deploying. Is there a lag in getting that. Like distribution channel. Are you helping? There is. So like prompting, lms, you can have them be concise, verbose, all that.
They’re built on LM backbones, these models. How do you see all that?
Guillaume:
Yeah, I think this is a lot of what we’re doing with our own customers. Very [00:18:00] often they come to us, so it’s for different reasons. I think one reason is sometimes they have this lot of privacy concerns.
They have this data that it’s very sensitive. They don’t want data to leave. The companies, they wanted to stay. Inside the company. So we have them deploy model in-house. So either on a, either on premise or on private cloud. So they’re not worried that it’s given to a third party on the there some leakage.
Sometimes they have this kind of many companies have this different, sensitivity of data they have like sometimes channel chat can send it to the cloud has to stay there. So then it creates some kind of heterogeneous workflows where it’s annoying. You cannot send some data to the cloud.
This one you can, so here, when we actually deploy the model for them, they don’t have this consideration. They are like not worried that, this is going to leak. Everything is much easier. So we help them basically do this on the, so it’s one of the very proposition. But but the other is very often, when customers use this off the shelf close model, but very sad is that they are not leveraging, these data that have been collecting for four years or something for decades.
So much data. Sometimes it’s trillions of tokens of [00:19:00] data in a very specific domain. Their domain, which is data that you’ll not find in the public, on the public internet. So data on which, like close model, we actually not have access to one, which that’s going to be really good. So if they’re using like closed source models are basically not benefiting from all these insights.
All these data they have collected three years, they can always give it into the context that in France, but is never as good as if you actually train the modern analysis. So yes, that’s basically what we help them to do. We actually provide them some purchase, basically what we announced at GTC this week.
So we provide them with this, it’s basically like a platform with a lot of tools to actually help them process data. Trained on that. Yeah, it’s actually the same thing that we’re using in the science team. So it’s actually very better tested infrastructure, like a lot of efficient training cut base.
For a quality pre-training like a fine tuning, even doing S-F-T-I-L. So we help them do this using the same tools as what our science team is building is using. So since it’s tools that we’ve been using for two years now, it’s really better tested. It’s really sophisticated.
So it’s the same thing. We are giving to them, giving the company the same thing [00:20:00] that what are same still using internally actually build their own ai and it makes a really big difference. I think sometimes customers. And many in general don’t realize how much better the model becomes when you fine tune it on your own data.
And you can have a, your model is here. You start from there. You have a cross source model, which is sort here, but if you actually fine tune it can actually really go much further than this. And then you have a very big advantage. The model is trained on your entire company knowledge, so it knows everything.
You don’t have to feed like 10 K tokens of contact at every query. So it’s it’s much easier. It’s a bit, I think using a closed source model is really sad because it basically puts. You are not leveraging all this data and you are going to be using the same model as all your old competitors when you’re actually using, everything you have been collected for years, which is really valuable.
So yeah. So we help basically customers do this. We have a lot of solution I mean deployed for engineers that go in the company that basically look at the problem customers are facing to look at what they’re struggling to do what we should do to solve it. So we help them solve them together.
So it’s I think our approach is a bit different, but here. [00:21:00] Some of their companies and competitors, it’s, we don’t just release an endpoint on sale, do some stuff on top of that, or we don’t just give a checkpoint. We really look very closely with customers. We look at the issues they have, we had them solve them.
We really make some tailored solution for the client are facing. Some example are also going to be, sometime we have some customers. They really wanted to have a really good model, really performance on some, like Asian languages on the, if you take some of the shelf models, they can speak it, they can write in this language, but it’s not amazing.
This language would be like maybe zero 1% of the mixture. So it has been included during training, but very little. So what we did here is upgrade. We trained a new model for them, but so this language was 50% of the mix, so it’s much, much stronger. It knows of the dialects, it knows the, so it’s yeah.
So it’s some example of things we can do and it’s really arbitrary, custom. I think you had some of their customers, for instance, they wanted some. They wanted some 3D model that can do audio with a very good function cable. So something you wanted to put in the car in particular, they wanted this to be offline because in a car you don’t necessarily have access to internet.
So [00:22:00] yeah. So here we can actually build the solutions. There is no like model out of the box on this. In the internet you have this very, you have this very general model generalist, like he’s strong model. But for things like this, they always want at specific solutions and on some other reasons.
Sometimes they come to us is because, like they, they experiment with some closed source model. They get some prototype. They’re happy with what they build. They, it works well. They’re happy with the performance, and then they want to go to production and then they analyze. But it’s extremely expensive.
You cannot push this. It’s so then they come back to us on this. They can help us build the same thing as this, but using something much cheaper on here. And here we can sometime be something 10 x cheaper by just functioning a model and it’ll be better OnPrem on their old server and also much cheaper as well.
So yeah,
swyx:
that’s the drop pitch right there. Take all the
money.
Vibhu:
And outside of that you do, we do put open wave models so people can do this themselves. I feel like not enough people go outta their way.
swyx:
They’re not going to, they’re gonna ask them to do it as the expert. I
Guillaume:
think initially we didn’t know, [00:23:00] we wanted completely short at the beginning of the company because, I think our study was not exactly the same as what it is today, but what we underestimated initially is the complexity of deploying this model and connecting them to everything to be sure it has access to the company knowledge on the, and it was, yeah, on, we were seeing customers struggling with this, but it was even, that was three years ago and no, things are much more complicated because now you don’t just have, text on SFT on a simple instruction following.
You have reasoning like your agents, you have like tools. You have a multimodal audio, so it’s much more complicated than before. And even back then it was hard for customers. So they really need, have some support and this is why actually providing like always some four D position as well. The process
swyx:
I’m curious is there also voice fine tuning that people do?
Pavan:
So in this forge we also have a say unified framework. And the hope is like the er speech to text that we released earlier this year. And even the ER chart that we released last year. And I think a big people, I think there’s a big, rich ecosystem [00:24:00] of people fine tuning whisper, and people want the same thing with w so it’s much stronger than Whisper.
And yeah, the the platform offers that kind of fine tuning yeah, which could be any kind of fine tuning. Like for instance, even sometimes people want to support new languages to this, which are tail languages, which we hope to cover. Certain natively, but if there is a language where you data and you want to frank you, I think this is a good use case.
Or the other use cases, you, it’s the same language, like even English but it’s in a very domain specific way.
swyx:
Yeah. Terminology, jargon, medical stuff.
Pavan:
Exactly. And also there’s specific acoustic conditions like there’s a lot of noise or the, and. The model will do decently in most conditions, but you can always make it better.
And that those are some of the use cases where you can improve it e even further. And that’s one good use case for this and for text to speech. We’re just releasing it so we’ll have support for that soon too. I think it’s similar use case.
Pavan:
It’s little different the kind of things that you want to extend a [00:25:00] text to speech model to, which could be like voice personalization, voice adaptation for enterprises.
Many enterprises need very specific kind of tone, very specific kind of like personality for this kind of voice. And all of those are like good use cases for fine tuning.
swyx:
This one I was gonna ask you, we never talked about cloning voice clothing here. How important is it, right?
Like I can clone a famous person’s voice. Okay. But
Pavan:
the main use case would be like for enterprise personalization, like enterprises need like a lot of customization. You don’t want the same. Voice for all the enterprises. Each enterprise want a customized, specialized something which is representative both their brand and also their, I guess safety considerations and the use case I think the kind of thing that you would deploy as a empathetic assistant in the context of a healthcare domain would be very different from the kind of thing that would be in a customer support bot and would be different from like more conversational aspects.
I think those are the. [00:26:00] Customizations you would expect from enterprise. And that’s the main use case, at least from our side.
Vibhu:
My, my basic example is you don’t want to call to customer services and have the same exact voice. It’s just, it’s gonna be weird.
Vibhu:
But also on the technical side of this, so there’s like a few things in TRO that I thought were pretty interesting.
He’s a big fan of this paper. Oh, he said very good paper. He said this is the best SR paper he’s ever read. Yeah. I’ve hyped up this voice paper enough. We covered it. Somewhere, but a big thing. So Whisper is known for 32nd generation a 32nd processing. You extended this to 40 minutes. There was a lot of good detail in the paper about how this was done.
Even little niches of how the padding is. So it’s very much needed. You need to have that padding in there, the synthetic data generation around this. I’m wondering if you can share the same about the new speech to text, right? Text to speech. So how do you. How do you generate long form, coherent?
How do you generate, how do you do that? And then any gems? Is there gonna be a paper?
Pavan:
Yeah. Yeah. They would be a technical report. Okay. Yeah. I think I could have a lot of details.
Pavan:
But me I think the [00:27:00] summary of it, actually, some of the considerations in this paper were, because we started with the wipa encoder as the starting point, and now we have in-house encoders, like the bigger time model, for instance, which we released in January.
Also release a technical report for that real time model as well, which is this dual stream architecture. It’s an interesting architecture. You should check it out. And there we have a causal encoder and I don’t think there’s any strong, multilingual causal encoder out in the community. So we thought it’s a good contribution.
So that’s one nice encoder there. Other people want to adapt. That’s a good end code. And we train it from scratch. I think her. Post stack is now mature enough that we are able to train super strong ENC codes. And some of these considerations, like spatting and stuff, is a function of the Whisper ENC code.
And now that we train encoders, inhouse the design concentrations are different.
Pavan:
And for the question on text to speech, I think that’s also leans onto the original auto aggressive decoder backbone. I think, it says very, almost identical considerations. I think the long context in it’s not even long con, [00:28:00] so the model processes audio at 12.5 herds, so one second maps to like 12.5 tokens.
So I think one minute is like 7.8 tokens. You can get like up to 10 minutes in eight K context window and get half an hour and 30 K context window. So that’s and 30 2K context is something that’s we are very comfortable training on. We can extend it even much longer. 1 48 K. Okay. You can naturally see how it can extend to even our long generations.
Yeah. We need the. Like data recipe and the whole algorithm to work coherently enough through such long context. But the techniques are some way very similar to the text, long context modeling. And the key differences, it’s just doing flow matching order regressively instead of a text open prediction.
swyx:
Okay. I think that was most, most of the sort of voice questions that we had. But
Vibhu:
I have a big question on Mr. Al, Mr. Small. So what is small? How do we define [00:29:00] small? What is this? What is this? I remember the days of Misal seven B on my laptop. The snuff fitting on my laptop. I could run it on the big laptop, but
Guillaume:
it’s just additional.
Question of terminology, like here what we did, baseball is north active parameters, but it’s true. Really not give it another name, but yeah, we could have called it medium, but only, I,
I suppose it’s a model that we released mixture of experts. It’s a model that combines different model before which we were doing the same, is that we had one model, general model for Israel. Doing instruction following, were like a separate model that was Devrel trial. So qu coding specify specific to code with another model for Reason Maal.
So this were separate artifacts built by different team at trial on what we’re doing is basically merging all of this. It was, you had pixel trial was the first vision model. We was like a separate model on the way we do things internally is that we have one team focus on one capability, build one model.
On the means mature, mature enough, we decide to merge this into the [00:30:00] matrix. But here it was the first time we basically match all of this into one. But there are some other things we did at first time to merge time, for instance, like more capabilities or function coding I think would be, are, it’s going to be much, much better in this trial, small platform.
But but yeah, so it’s our latest model on the working is,
Vibhu:
and yeah, key things is it’s very sparse. Six, be active pretty efficient to serve. 2 56 K context. Yeah,
swyx:
I think what’s interesting is just this general theory of developing individual capabilities in different teams and then merging them.
Where is this going gonna end up?
Vibhu:
Like we’ve seen the five things put together in this. Yeah. What are the next five teams?
swyx:
I think actually OpenAI has gone away from the original four Oh. Vision of the Omni model. This was what they were selling. All modalities and all modalities out.
But I feel like you might do it.
Guillaume:
I think there’s some mod where it’s not competitive use, for instance for audio. For audio here, if you want to do transcription, I think it makes no sense to use a model. If you just want to trans tech it, it’ll be very inefficient. If you want to do audio, you probably just want to be the [00:31:00] one VR 3D model performance essentially
swyx:
the same.
It’s going to be incredibly cheaper. So here, that’s why we want
Guillaume:
to have a separate but just does this. Yeah, I think the question is just, yeah. If you are to, to your model. By speech and you asking like a very complex questions on how you do this on the, just to cascade things. Do you want to put a d in a model that has like a one key around it?
It’s like a, not a competitive discussion, I think unaware if you doing into the direction, but that’s possible. Of course. But yeah. But I think for us, the next capabilities we want to try to integrate into these models when we are going to be yes, like marketing or no reasoning better, I think more capabilities that people don’t talk too much about, but at high bottom, I think for our customers in our, on different industries, for instance, things are around like a legal computer.
I design all these things that is this males out of the box are to put at that. Because people, if you don’t prioritize this, there is not like too benchmark on that. But
swyx:
this done how to
Guillaume:
make this good and this just start to do the work. Extracting some that processing it [00:32:00] expression. So yeah.
But we are offering the imagine to this.
swyx:
I think for voice. Yeah. The key thing I think over maybe like the last year or so with VO and gr Imagine and all these things is joining voice with video, right? Which people don’t understand spatial audio because like most TTS is just oh, I’m speaking to a microphone in perfect studio quality.
But when you have video, like the voice moves around.
Pavan:
That’s true. The constitution was a little different in the sense that there it’s like a a standalone artifact where you get the whole thing and you consume it. But in a conversational setting, it’s a, you need the extreme low latency.
swyx:
Yeah,
Pavan:
streaming would be one of the primary concentrations.
swyx:
You can build a giant company just doing that, right? So you don’t need to do the voice, but I was just know on the theme of merging modalities, that is something I, I am like, wow. Like I didn’t, everyone up till, let’s say mid last year was just doing these like pipelines of okay, we’ll stitch a TTS model with a voice thing and a lip sync [00:33:00] thing and what have you.
Nope. Just giant model. Yeah.
Vibhu:
I have a two part question. So one is, it’s still open. It seems like open source is still very core to what you guys do and I just have to plug your paper. Jan 2024. This is the one trial of experts like. Very fundamental research on how to do good.
Moes paper comes out very good paper for anyone. That’s just side tangent. No.
swyx:
This thing caused, we bring back, eight by 22 was like the nuclear bomb for open source. I think it takes Shouldn be more seven B more. Yeah. Yeah. But this is a bigger opposite than me.
Yeah. Yeah I don’t remember this. I remember, I don’t think it was January, right? It was like new reps it was, it dropped during new reps and everyone in Europes was December of 25th, I think. Yeah. The model was did as well.
Vibhu:
It’s just a little update probably.
swyx:
Yeah. No, but you have a point to make.
Vibhu:
No, you gotta check that. But then, I just want to hear more broadly on open source for you guys, and when you had asked earlier [00:34:00] about what’s next, what are the other, side tapes working on you. You put out Lean straw. This,
swyx:
it’s not necessarily surprise. I was like, I don’t, this doesn’t fit my mental model or Misra.
Guillaume:
Yeah. First for open source in general, I think it’s really something which looks to the January of the company. I think we started it per once, is we so we have open sourcing with, since the beginning and even before this. So before this, so me and Tim were at Meta, we released LA and I think what was really nice.
To see that before this, for most researchers like universities, it was impossible to work on elements. There was no alien outside. And if you look at many of the techniques that were developed after, for instance, was open source all this post-training approaches like even DPOD, like preference optimization, all of this were done by people that had access to this portal.
And it’ll have been impossible to do without this. So it’s really making sense, move faster. So we really want to contribute to this ecosystem. I think like the deep and also like very lot of impact. All these papers that are I think in the open source community are really helping the science community as a whole to move faster.
So [00:35:00] we want contribute to this ecosystem. That’s why we’re releasing very detailed technical reports. So ma trial and our first reason model, and ation, lot of results, things that work, things that did not work as well. Think helpful on the, yeah, so for the audio model also to share a lot of details, share of them for real time model.
And the, yeah, so we really want to continue this, basically belong to this community of people who share science. I think we really don’t want to be, leading in a world where the smartest model, the best models are only behind, close doors. Only accessible to a shoe companies that we, as a power to decide we can use them on it.
I think it’s a scary future. We don’t want to live in, we really want this model to be accessible to anyone that want. Intelligence to be used unaccessible by anyone who can use it. So yeah, so that’s why we are pushing this mission and source model. Yeah. So not, so yeah, no strategy. So it’s open source, not the first model, so not the best on the Yeah.
Guillaume:
LIN trial I think is also one step into this direction. So it’s yeah, a bit different than what we are usually releasing. But we have a small team internally [00:36:00] working on them. Formal proofing, formal math. So I think a subject we care about in general and we were working on reasoning. I think we started too early before doing reasoning without LMD is very hard, especially when you work with formal systems because the amount of data you have is negligible.
It’s addressable community of people writing like formal proofs. But the reason why we like it is because I think there is if you look at what people are doing with reasoning, is there, the problems that you can use. Are usually going to be problems where you can verify the output. So for instance, all this ai ME problem where the solution is a number between 100, like a thousand.
So you can verify, compare this with a reference or it’s an expression. You can actually compare the output expression generic with the reference. But there are many, most of them have problem and most of the reason problem. There is no like way to easily verify the solution. If the question is show that F is continuous, cannot compare in the reference, right?
If it’s a probe that this is true or probes is properties, there is no way to. You cannot act, simply verify the correctness of your proof. So it’s hard to apply the, there is no referable reward here. So [00:37:00] what you could provide is of course, like a judge and judge that will look at your proof. But it’s very hard and it’s very, you could do certain, some reward hacking happening there.
So it’s difficult. You could provide like a reference proof, but then there are also many ways to prove the same thing. So if the model says give negative reward because it’s a different poop, maybe it was still digit proof, just different. So it’s not going to work well. What’s nice with lean and with formal probing is that you don’t have to worry about this whatsoever.
We just,
swyx:
they’re all function is largely compiles in lean is functionally the same. Exactly.
Guillaume:
It’s like a problem if it compiles it’s correct. It’s very easy. And you can apply this and then you can,
swyx:
it’s just way too small. So no human will actually go and do it.
Guillaume:
Yeah, that’s exactly.
It’s the only people can do it. It’s like a very small committee of people doing a PhD on that. So it’s super small. And it’s sad because it’s actually very useful on not just mat, but also in software verification. So for instance, software verification today. So tiny market. Very few industries work on this and we need that.
It’s usually going to be like companies like building airplanes, air robotics,
swyx:
like
Guillaume:
things [00:38:00] where they absolutely want to be sure. Life depend on this, but it’s very rare that people formally verify the correctness of their software. But I think one of the reasons for this is simply that it’s just hard to do.
swyx:
Are you think of TLA plus? It’s the language that some people do for software verification? No. That people use in a ference, but but yeah, it’s the reason I think why people don’t use it more and why this industry is not as big as could be is because it’s very hard. But now with cutting edges that are there, it’s going to be very different.
Guillaume:
We’re going to see much more of this. So I think yes, industry there is going to be much larger in the future that we, these models. So yeah. Here also anticipating this a little bit, we wanted to work on that because it’s proving like a math theory and like a, essentially the same tools.
swyx:
Yeah.
swyx:
One of my theories is that because the proofs takes so long, it’s actually just a proxy for long horizon reasoning and coherence and planning. Maybe a lot of people will say okay, it’s for people who like math. It’s for being okay. It’s like a niche math language. Who cares? But actually, and you use this as part of your data mixture for [00:39:00] post-training and reasoning, actually, it might spike everywhere else.
Yeah. And I think that’s un under explored or no one’s like really put out a definitive paper on how this generalizes.
Guillaume:
Yeah, absolutely. And
Pavan:
I think even
Guillaume:
that’s what we’re seeing already. For instance, you should do some reasoning on math as then the American should do reason even.
Yeah. In the early stage. So we, the, there is some transfer, some sort of emergence that happens. And I think some, it’s also interesting, it’s not just I think the topic in general, but it’s, there is a lot of connection with this on including agents because. Sometimes the model can see like a three that it has to prove it’s very complex, but then it can take the initiative to say, I’m going to prove this three lr.
I’m going to suggest three Rs, and I’m going to in parallel prove each R. So three of them in parallel with sub agents, but I’m also going to prove them in theory and the three tool so you can do this also. Pretty interesting. You can, even if you fail to put one of the LeMar, you can actually, maybe you succeed to put the normal lema too, so you get some possible reward here.
So it’s a bit less Spartan issue, just get to zero one for the entire thing. [00:40:00] So it’s pretty interesting. I think we can actually,
Vibhu:
yeah, it’s also an interesting case just for specialized models in general, right? Like the cost thing you show is pretty interesting yeah, similar score wise, you are, thirty, seventy, a hundred fifty, three hundred bucks.
Smaller.
swyx:
I think cost is a bit unfair, right? ‘cause this one is at like inference cost. It’s always there on top with their margins on top of it. But, we don’t know anything else, so we gotta figure it out.
Vibhu:
Okay.
Vibhu:
I did wanna actually push on that more. Not on cost, but you mentioned about, okay, it’s a great way to have verifiable long context reasoning.
What are other frontiers that, I’m sure you guys are working on internally, there’s a lot of push of people pushing back on pre-training. Scaling, RL pushing, compute towards having more than half of your training budget. All on rl. Where are you guys seeing the frontier of research in that?
Guillaume:
You mean the
Vibhu:
just in foundation model training in the next, one thing that you guys do actually is you do fundamental research from the ground up, right? So you probably have a really good look at where you can [00:41:00] forecast this out.
Guillaume:
Yeah. I think for us we’re still working a lot on the pre-training side.
I think we are very far from situational, the pre-training. I think ML four preprinting will be like big step compared to everything we have done before. So we are pretty excited about this. And I think on the other side, I think now we have more and more to think about this algorithm that will actually support this very long trajectories.
I think when it was, for instance, GRPO for it doesn’t really work this any bit of policy. Which was okay initially because you are solving math problem that can be solved in like a few thousand tokens. So the model can alize them pretty quickly. So when you do your update, the model is never too far off.
It’s never too far off. But now when you are moving towards this kind of problems where certain takes hours, like six hours to get a reward, then your model is co pick places. So you have bi new infrastructure that supports this, but also new A, so now everything we’re doing internally, we’re trying to. Build some infra that we actually anticipate is what we have in six months, one now, which is this extremely no scenarios on the, I think when we started Missal, part of me and [00:42:00] we wanted to, is very nice under element where people are there, they can do research, they like with a lot of resources.
So it was nice. I think things changed a lot when I think when J Pity came out. I think after that I think was. This one is same again. But but yeah, but it was nice. And I think we also want to work part of this descrip before
swyx:
coming to the end.
swyx:
We’re just, obviously, I think you guys are doing incredible work.
You’ve, they are a very impressive vision for open source and for voice. What are you hiring for? What’s the what are you looking for that you are trying to join the company?
Guillaume:
Yeah, so we are hiring a lot of people in our sense team. We’re hiring, in all our offices. So we have a, our H two is in France in Paris.
We have a small team in London. We like a team in Pato as well. Co we open some offices in in SAU, in Poland. So one in Zurich. We also like some presence in New York as well on Sooner one in San Francisco. So we all bit either way also like hiring remotely. So we’re going the team trying to hire like very strong people.
I think we want to stay, so the team is not. Instead of fairly small team. [00:43:00] But I think we want to keep it that way. ‘Cause we we find it quite efficient. So like a small team they agile so yeah.
swyx:
Okay.
swyx:
Let’s focus on science and the forward deployed. We actually are strong believers in science.
We started the our new science pod that focuses specifically on the air for science. What areas do you think are the most promis.
Guillaume:
What we’re pretty excited about right now, and something we have already started doing or that we’d probably be able to share more about this in a couple of months, is that we are exploring AI for science.
And there are a lot of areas where we think that you could get some extremely promising buzz. If you were to apply AI in these domains. There are a lot of long inputs. You just have to find these domains where actually AI has not been yet applied, and it’s usually hard to do because the people working in those domains don’t necessarily know the capability of these models.
They don’t know. How I would just have to pair them with Yeah, exactly. Your researcher slashing, which is actually hard to do. But this matching, we’re doing it naturally with our customers. So we have some company we are very closely with. So for instance, ISM Andreesen are one of our partners, so we’re doing some research with them on their other, like tons of extremely interesting problems.
Columns in physics, in [00:44:00] science matter science that they’re essentially the only ones to work on. ‘cause they’re doing something No, no one else is doing on the, yeah. So there are many domains where AI can actually revolutionize things. Just you have to think about it on you familiar with what can do or to apply it.
So yeah, it’s something where more modeling with our partners, with our customers sort AI for s, but.
swyx:
Yeah. Okay.
swyx:
And then for deployed what it makes a good four deployed engineer, what do they need? Where do people fail?
Guillaume:
I think it’s usually you need people that are very familiar with the tech and not necessarily with a lot of research expertise, but that are actually pretty good at using this model that can actually like that know how to do functioning, that know how to like, start some error pipeline.
And it’s it’s not easy. It’s something that mucus. Majority of companies will not be able to do this on their own. So here I think we need people that are, that like to solve problems that are accept solving some complex, very concrete problem. It’s applied science basically.
And yeah, so I think it’s not too different. I think from the case you need in research because it’s essentially you are trying to find solutions to problems that in [00:45:00] customers have not yet. So sometimes it’s easy. Sometimes you’re here to do the work. You have to like create synthetic data.
Find some edge case. So it can be, yeah. Depends on the problem. But but yeah, you have to, I think it also a bit of patience on the be creative. I think very similar skill is Asian,
Pavan:
the diversity of the work they do. It always surprises me. It’s it’s, it goes all the way from the kind of stuff they encounter in industries.
It’s just very interesting. I think.
swyx:
Any fun like success anecdotes.
Guillaume:
Yeah, it can be actually training this small model on edge that just we do one specific thing can be like training some very large model without some specific languages as well. Making models really good at some tube use, like for instance, computer ID design, these kind of things.
Is that pairing with vision as well? Yeah,
Pavan:
and the fact detection for chips or like in, in factories identifying things like it, the. Diversity could be anything where you can deploy these foundation models. So yeah the work to make it work in that specific setting, basically whatever it takes to make it like add value in that, by the way, workflow.
Vibhu:
Yeah. [00:46:00] And it goes across the stack, right? Like even just pulling up the website like.
swyx:
It’s so broad on compute. It is so broad.
Vibhu:
We didn’t even touch on if you have a coding CLI tool. One thing you guys were actually like, I think the first tool was agents, ral agents. You had the agent builder, you can serve it via API and all that.
And I’m guessing forward deploy people.
Guillaume:
Yeah.
Vibhu:
Help build that out and stuff.
Guillaume:
It is also why we are, so we’re doing many things, but I think that’s also part of the value proposition that sometime know customers. They’re always very. Extremely careful about their data and they don’t want to, they don’t like, trusting so many partners, trusting one partner for code, giving the data to another third party for like audios and another one.
So they don’t like this here. What they really like with our approach that we can help them on anything so they don’t have to send the data to so many clouds. So yeah,
swyx:
I think that there can be many orders of magnitude more. F Ds then research scientists and they don’t need your full experience, but they’re still super variable to customers
Guillaume:
in practice.
These two teams [00:47:00] are still quite intertwine, very often. Yeah. So first of all, they’re using the same tools, the same data pipeline and everything on the, it’s it’s very helpful for the science team to get the feedback and the solution team ‘cause they can. Look at these customers are trying to do this.
This is not working. It can really be show in the next version. Yeah. But this is basically a real world eval. Yeah, it’s real world eval and it’s not something, for instance, if you’re just working in the lab, it’s just ships model. But you don’t do this work of for customers. You have no idea for whether your model is good at this H case.
For instance, you even in year found this, right? So yeah, there is a very gap, big gap between the public benchmarks that are very like academic. On
Pavan:
the rare cases are just very diverse and in the specific concept of a customer, you can fine tune and make it like first evaluate, create a solid eval, benchmark, and then measure in the context of their, the kind of audio.
Like for instance, one use case is literally just, there’s the word for kids and they have to just say it out. It’s a very specific thing. You’re just saying one word and then you have to you, you’ll grade the kid whether they did it right or not. It’s [00:48:00] like R for, but so there’re very diverse use cases and the idea is that they, the.
Applied scientist engineer will go and make it better. And then from the learnings we incorporate it into the base model itself. So it’s it’s just better out of the box.
Vibhu:
Yeah. It’s a good full circle system. Like the foundation model evals are all just proxies of what you really, you’re never gonna have one that says it, it doesn’t make sense for there to be, a one word transcription like that.
It’s not something you wanna fit on. Perfect.
swyx:
Everyone should go check out everything that Michelle has to offer and try the TTS model, which will link in the show notes. But thank you so much for coming tha thanks. Such a stretch.
