---
title: "The real AI risk is inside the labs"
url: "http://antirez.com/news/172"
fetched_at: 2026-07-28T10:08:51.611206+00:00
source: "antirez.com"
tags: [blog, raw]
---

# The real AI risk is inside the labs

Source: http://antirez.com/news/172

antirez
1 hour ago. 2759 views.
Amodei in his latest blog post wrote a mix of agreeable things and things that I believe misrepresent where the real risk of AI is located. I want to focus my attention on why, among all the risks, open weight models constitute the mildest one. I write these words as a person who strongly believes AI may be very dangerous in the near future:

1. Exactly like what happened during the OpenAI / HF incident (which was a joke, but focus on the modalities, not the outcomes), the first serious AI incident is very likely to happen *inside* the walls of frontier AI labs, while testing a new model, or while the AI lab employees, or the few externals who have access, do something wrong compared to the expected power of the model.

2. Closed models that will never even be opened to the public will be just a few TBs of data. All you need to leak one is a single person with access and the wrong goals, and you are back in the situation of open models. Open models are released *after* testing, and after similarly capable models were already available for some time under an API. The real risk is leaks, not releases, and leaks happen inside frontier companies.

3. As Amodei says, open models, once LLMs are dangerous enough in fields like biology, can be trained on a corpus ablated of certain branches of science, while still being useful for a number of other things. The limited context window of a model that lacks strong pre-training in certain domains is a strong protection even if the model is otherwise very capable. We are currently not in a place where open models can constitute that kind of danger.

4. In the context of cyber security, *not* having widespread access to the defensive security and bug seeking provided by LLMs creates exactly the "LLMs as a weapon" problem. It is already happening: open source maintainers, if they are out of some cyber program, can't find all the security bugs they could, while people with the right interests will be able to access frontier cyber models, do significant RL training on open weight models, and so forth.

5. Once LLMs are dangerous enough (and we are near this limit, if progress continues), the real security chain that we need in place is inside labs, can't be set up without strong common rules, and a single company should not be able to evaluate independently whether a model is safe enough. We need a joint AI safety organization that includes experts from all over the world and is recognized by the governments where frontier AI companies exist.

6. Slowing down AI for safety must be counterbalanced by the fact that AI discoveries in medicine and other sciences may lower human suffering. Lack of checks may result in some catastrophic outcome ("Good morning! Let's work on this enhanced smallpox"). Lack of progress may result in people who could be saved dying, not just in the present, but among the many who will suffer from illnesses in the future. This may look like a bizarre point, but we always need to understand that stopping AI *also* has a security cost embedded inside, which is just a lot more hidden.

7. The ideological position of Amodei against China is unfair. We Europeans killed each other until 80 years ago without any limit of decency (people now forget, but one of the reasons the US invested in the stability of Europe in the past is that we were deeply dangerous, and would probably end up doing it again, while decades of wealth would make us a good market and would prevent us from fighting again). The US has, even in present times, tragic inequalities, people suffering for lack of basic health care, a president who looks unstable and is apparently very prone to war. I wish China had the same level of individual rights we have here in the West, but at the same time China's history is a lot less warlike than Western culture. It is absolutely not clear that an AGI military lock-in could be enforced more easily by China than the US, in the current conditions. Also, the current American administration spits hate at Europe in all forms, which is very worrying in a world where the US dominates everything. On top of all that, China's AI progress is not going to stop, whatever the GPU export policy is, so either Amodei is arguing that once America has AGI it should stop China by force, or what is his argument?

8. In the history of humanity there are many cases where technological supremacy was initially reached in a single place of the world. This, AFAIK, never resulted in *a single* country trying to create a permanent advantage. The non-proliferation of nuclear weapons, which is probably the case most similar to the GPU ban, was not used to achieve a permanent economic advantage by threatening to bomb everybody else not complying, nor did it prevent several actors from acquiring that technology at different times, without one bombing the other to stop their progress. Moreover, I don't believe AI poses the greatest dangers because of government-driven actions. I wish this were the most dangerous scenario! Governments do silly things, are often aggressive, and their actions have even resulted in genocides, but it requires a lot of people agreeing on doing something terrible, which is itself a limiting factor. The greatest problem is what happens in two other cases: A) a few individuals generate an apocalypse event (the virus case), B) AI itself escapes the control of the people building it.

I believe we should not consider AI safe. A critical event that may result in the extinction of Homo sapiens is possible, but the danger is not in open models, or China making faster progress than the US. The danger is that a few CEOs (everywhere in the world) without the required background and legitimacy are in the position of making hard choices for humanity at large. They were not selected to do so; it was just the randomness of events that created this setup. They can't speak for everybody, given the stakes, just because they have GPUs and money. This is the first thing that should be fixed.
