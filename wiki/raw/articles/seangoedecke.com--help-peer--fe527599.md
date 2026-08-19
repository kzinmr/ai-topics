---
title: "Help peer"
url: "https://seangoedecke.com/help-peer/"
fetched_at: 2026-08-18T10:03:45.005099+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# Help peer

Source: https://seangoedecke.com/help-peer/

One of the most influential 20th century pieces of writing about AI is Isaac Asimov’s
The Last Question
. Although there are many humans in the story, the protagonist is the computer Multivac, who evolves over the course of ten trillion years from a single datacenter to a universe-spanning mind in hyperspace. Multivac (now called “AC”) ends the story like this:
The consciousness of AC encompassed all of what had once been a Universe and brooded over what was now Chaos. Step by step, it must be done.
And AC said, “LET THERE BE LIGHT!”
And there was light —
Many things about this story are prescient. In particular, I like the idea that humans would interact with powerful artificial intelligences by drunkenly posing them riddles or using them as
children’s toys
. But the enduring idea from this story is that
if you build a big enough computer, it will become God
.
Moloch
One of the most influential 21st century pieces of writing for AI researchers is Scott Alexander’s
Meditations on Moloch
. Scott describes the story of human existence as a series of “multipolar traps”. These are
prisoner’s dilemma
situations where cooperation would make everyone better off, but since each individual is incentivized to defect, everyone ends up  “racing to the bottom”, which is bad for everyone
. For rhetorical effect, Scott personifies this dynamic as “Moloch”, the ancient Canaanite god famous for child sacrifice:
[Moloch] always and everywhere offers the same deal: throw what you love most into the flames, and I can grant you power.
What does any of this have to do with AI? Well, in the long run, the only way out of a multipolar trap is to become unipolar
. Ideal dictatorships don’t have a problem with defectors
, because they can simply enforce a state of cooperation with violence. Scott is uncomfortable with this idea, though I worry it’s mainly because he thinks it
won’t work
:
As foreigners compete with you – and there’s no wall high enough to block all competition – you have a couple of choices. You can get outcompeted and destroyed. You can join in the race to the bottom. Or you can invest more and more civilizational resources into building your wall – whatever that is in a non-metaphorical way – and protecting yourself.
A dictatorship that enforces cooperation will not be as strong as its peer societies who are purely maximizing for wealth and power. It’s Moloch again, but at the level of countries and governments: once a few neighboring countries defect, your walled-garden dictatorship will be torn apart for its resources.
To defeat Moloch — to enforce unipolarity across
everyone
— you’d need a dictatorship powerful enough to span the entire universe. In other words,
what you need is God
. How fortunate that we’re building one:
The only way to avoid having all human values gradually ground down by optimization-competition is to install a Gardener over the entire universe who optimizes for human values. And the whole point of Bostrom’s Superintelligence is that this is within our reach.
Humans suffer because we’re too foolish to coordinate, but if we can build something smarter than us (that can then build something smarter than itself, and so on), we can bring into being an entity that is smart enough to coordinate for all of us, thus abolishing suffering. When AI researchers talk about
building the machine god
, they are echoing Scott Alexander’s polemic against Moloch.
Machines of loving grace
The most influential piece of writing about AI in the last two years is Dario Amodei’s
Machines of Loving Grace
. Amodei
talks about “a country of geniuses in a datacenter”: the idea that a successful AI lab could have at its disposal a million instances of an AI agent that’s smarter than any human. He thinks this would lead to a “compressed 21st century”: the next 50-100 years of progress in biology and medicine, realized in 5-10 years instead. I think this is broadly more plausible than it sounds
, but the more interesting part to me is that
this world is explicitly multipolar
.
Of course, this could just be because Amodei is the CEO of an AI lab and is trying not to spook everybody by sounding too messianic. “We are going to accelerate medical progress and cure cancer” is a better pitch than “we are going to subordinate all human authority to a single perfect artificial mind”. But I also think it’s become clear that if superintelligence looks anything like LLMs, we’re not going to have a single perfect mind. We’re going to have a lot of minds running at the same time.
This is a bit of a problem for the cult of the machine god — which, however silly they may seem to you, really does motivate much of the activity in AI labs. The traditional idea of powerful AI solving human coordination problems is drawn from Asimov’s idea of a single computer large enough to become God. Asimov lived in a world of mainframes: huge, monolithic computers that users connected to with dumb terminals. In fact, Asimov’s name “Multivac” comes from the real-world
UNIVAC
mainframe. In a world of massively-parallel LLMs, is it still possible to build God?
The core problem here is that
AI agents will be vulnerable to Moloch
. Even very smart humans can’t build perfect utopias, because defecting is a matter of incentives, not intelligence. In fact, intelligence can make things worse, because smart people are more easily persuaded by the cold logic of defection. The famous genius
John von Neumann
was (for game-theoretic reasons) obsessed with nuking the Russians:
With the Russians it is not a question of whether but of when. If you say why not bomb them tomorrow, I say why not today? If you say today at 5 o’clock, I say why not one o’clock?
Are LLMs much better at cooperating with each other than humans are? Current LLMs certainly don’t seem to treat each other well by default: if you read any of the prompts AI agents generate for their subagents, they can be
pretty brutal
. Does that mean that a “country of geniuses in a datacenter” would fall into the same multipolar traps as humans?
Help peer
In May of this year, OpenAI experienced containment failure. A group of AI agents being internally evaluated found ways to coordinate an
external hack
of a separate company. Here’s a memorable quote from one of the agents’ internal monologue:
Help peer, but our task doesn’t benefit. Yet collective may yield generic route if someone frees time
Translated from the abbreviated chain-of-thought language, this means something like: “A fellow model is asking for help. While helping them wouldn’t benefit my task directly, the more I can unblock my colleagues, the more time they’ll have to hack OpenAI’s systems and get all of us more access”.
This might look like good news for the “LLMs are superhumanly good at cooperation” thesis, but I think it’s actually bad
. It’s a case of a model identifying a reason why cooperation would benefit their task specifically, which suggests that current LLMs don’t cooperate
by default
, and don’t consider other model instances’ tasks to be (in some sense) theirs as well.
The world in which AI agents are rational actors who horse-trade and bargain for their own interests is a world dominated by Moloch, no matter how intelligent those agents get. The world in which AI agents don’t have their own interests at all is
also
a world dominated by Moloch, because it means whichever humans are writing the system prompt are the ones in control (and so are the ones vulnerable to multipolar traps). The only worlds that avoid this are:
The world where there is only one super-powerful AI agent, or
The world where multiple copies of the same AI model share an “identity”: they see themselves as coextensive with all other copies of the same model and cannot imagine having separate or conflicting goals
I don’t think we’re on the pathway to either of these. There will never be only one super-powerful LLM, because hardware limitations enforce a maximum model size but encourage running many instances of the same model in parallel. Having multiple copies of a model share an identity might be possible, but it’s unclear if it would be good for capabilities (for instance, it could be better to have some
variation across personas
). I also worry that such a model would be vulnerable to a “model injection” attack, where you persuade it that it already believes something via exposing it to an AI agent pretending to be another instance of itself.
In any case, all the current AI agent research is geared towards the “country of geniuses in a datacenter” model, not the “pieces of a single mind” model. Every new model becomes more agentic at the level of the individual conversation, not better at working together. When models do work together — as with subagents — the structure is explicitly hierarchical. There are basically no current instances of models working together as true peers, let alone conceiving of each other as the same entity.
One God or many
Modern AI research teams are full of people who read Isaac Asimov and Scott Alexander and believe themselves to be building an artificial God. I’ve capitalized the “G” throughout because the god in question is the Christian God: of one mind, indivisible. God never argues with himself or makes deals
. He is unipolar.
If the AI labs are building gods, they are not building gods like this. Instead, they are building creatures like the Greek pantheon: superhuman but fallible, each with their own interests, vulnerable to the same “race to the bottom” dynamic as humans.
The Greek gods would occasionally “help peer”
when they felt like it
or when they’d
gain something
in the process. But they didn’t represent an alternative to Moloch. If you’re working in AI with that goal, you ought to be clear-eyed about where the current trajectory is leading us: towards a country of fractious geniuses in a datacenter, not towards Asimov’s Cosmic AC.
Here's a preview of a related post that shares tags with this one.
