---
title: "Slow down to speed up: AI and software engineering"
source_url: "https://youtu.be/5wks1W-auKY"
date: 2026-06-23
author: "Gergely Orosz (The Pragmatic Engineer)"
channel: "The Pragmatic Engineer"
event: "Craft Conference 2026, Budapest"
duration: "52m23s"
captured: 2026-06-25
type: transcript
tags: [ai-software-engineering, ai-agents, cursor, meta, instagram-exploit, token-maxing, openai, uber, software-craft, career-advice]
---

Good morning, Budapest. It's awesome to
to be back. Today, I'd like to talk
about some people, a few thousand that
are having a terrible week uh this week.
And this is specifically people inside
Meta and Instagram. I talk with a lot of
people in the industry. I have a lot of
friends inside of these companies. I
have even more I guess contact software
engineers who message me to tell me what
they're seeing, what what's happening.
And this week has been the worst in Meta
or Facebook history in probably forever.
So what happened is on Monday, we've had
the goofiest ever Instagram exploit. It
wasn't even an exploit, but it it was a
security breach. It was an attack.
What what happened is
I mean I I mean this this is from a
software engineer writing a book. It
this is the the most most goofy thing.
So there was two steps to this exploit.
Step one is you had to fake your
location to a victim. Let's say you
wanted to take over Barack Obama's
account on Instagram with like I don't
know tens of millions of followers. You
fake your location with a VPN to the US
and then you went to Meta AI you and
said that hey my account has been hacked
and could you please send verification
code to the AI to this email that I own.
And then step two was there was no step
two. This was it. Meta AI sent out a
code to you and you could take over
anyone's account.
This is this is the first zero authent
zero off password reset and we're
software engineers. You know what this
is? This is this is a bug. But the thing
that I couldn't get my head around is I
know people at when it was used to be
called Facebook. They have a really
strong engineering culture. They have
the globe's best automated rollout
canary system. They have so many layers
of verification. They have really good
engineers. They have manual code
reviews. and none of it. They have a
trust and safety team for God's sake.
Their trust, Instagram's trust and
safety teams is closer to 100 engineers
whose job is to keep this platform
secure. And you know, a few things
happened. The next day on Tuesday,
Meta's chief information security
officer sent an email saying, "I'm I'm
out. I'm quitting." This was very
interesting because Meta has just kicked
off a se an outage investigation. They
call it SEV inside of meta. And in the
middle of that and in even before it
concluded, the chief information
security officer stepping down. So I
asked around I I asked the people I know
at Instagram. I I happen to know people
on Instagram's trust and safety team.
Well, turns out they were only on trust
and safety team. So they even, you know,
shared me more details. You're hearing
this for the first time ever, by the
way. It's not an attack press. It
probably will be. It was AI. Of course,
it faking was AI. The thing that caused
the issue was AI written code that was
reviewed by AI and not humans at Meta.
And I'm thinking to myself, how could
have this happened at Meta? I mean, it
wasn't just AI. There's more to the
story. It was AI maxing, it was layoff,
and it was AI psychosis at Meta. And
what I mean with this is a AIX.
If in April I I wrote about this this
new trend called token maxing which was
happening across so many companies
including Meta, including Amazon,
including Uber, engineers were starting
to be measured on AI token usage at at
all these companies and they start to
inflate it. They just want to get to the
to the top leaderboard. They told the AI
let's do some like dumb stuff and you
know I get to more tokens but I I don't
need the work. And at Meta there was a
leaderboard and you could get status
like session immortal token and legend.
Uh in April meta killed this project but
but people were burning crazy amounts of
of things. Now AI usage inside of Meta
was part of performance evaluation.
It it wasn't like officially made up but
people inside of Meta are smart. They if
you had a low token count you know
that's not a great signal. So people
just start to inflate their token count.
So they start to use AI for anything and
everything. Write it by hand. Nah, why
why do it? Ask the AI. Read the
documentation. Nah, let let me use the
AI to to read it for me so it can just
burn a bunch of tokens. This is the
craziest thing that's happening, but you
know, inside a meta AI is free. And
again, these people want to have higher
bonuses. And they just use AI for
everything. Um, and yeah, the the code
that caused this SE was also AI
generated. Of of course, they use it AI
to review it as well. They use it to
triple review it, etc. The second part
to this thing was layoffs set meta. Meta
told the 10% of of of staff 8,000 people
will were laid off in 20th of May but
Meta told people or the press told
everyone that the layoffs are coming a
month before. So what people were doing
is as they were thinking oh am I going
to be laid off all of them they start to
use more AI because they didn't want
their token numbers to be down because
they didn't want to be fired for not
using enough tokens. You you see where
this is going, right? And they were not
really busy, you know, doing their work.
They were just worried about like, all
right, like let me get this inflated. So
inside of trust and safety team, people
were not thinking about trust and safety
were thinking about token maxing. And
finally,
I was wondering if I should call this AI
psychosis because psychosis is a very
serious psychological condition and
that's why I put it in brackets. But
I'll I'll show you why I I chose this
this name. Instagram had a tr thread a
trust and safety organization that was
built up over like seven or eight years.
A really good team mostly based in
London.
40% of this team before 20th of May was
reassigned to do manual data labeling.
They they were told on Thursday that
starting on Monday, you are no longer
working on this team. you are moving to
this new team in Alexander Wang's org
xscalei and you will be doing AI data
labeling which means you get these tasks
it's a GitHub GitHub pull request you
need to review it you need to add some
tests you need to add some feedback and
then then you do the next and then you
add some tests and you add some feedback
and you and you do the next these highly
skilled people they were not given a
choice now inside meta until now every
engineer was treated like royalty they
were given a choice they were not given
a choice so 40% of the organization just
boom gone There's five closer to 5,000
developers inside of Meta doing manual
AI labeling. And there's a running joke
inside of Meta that this is bigger than
OpenAI. This data labeling or Meta
clearly wants to build this amazing AI
model. Oh, and after the layoffs and
after the reassignments, most teams are
less than half the size. Some don't have
on call coverage anymore, which means
that in some services, there's just no
one picking up on call. This again has
never happened inside of Meta. And this
is what I mean by AI cycles. This is
fully self-inflicted. This is coming
from Mark Zuckerberg. This is coming
from Alexander Wang. This is coming from
the top. They're saying we don't care.
We it's so important for us to build
this model that we will risk our
business and we don't care if you know
we get hacked or something like that.
Morale is as low as has been in in Meta.
I've I've seen low morale. This is way
worse than the 20 2022 203 layoffs. Uh,
and oh, and yeah, if this wasn't enough,
in the US, they're recording your
screen. They're recording all your
screen strokes to train an AI. So, I uh,
it's the easiest time to hire to recruit
from Meta right now. Uh, and the
engineers that I talked to, they just
feel super let down. Meta used to treat
engineers like royalty and salary,
composition. You you could choose your
team. It was a good world event. And the
CEO, Mark Zuckerberg, he is a software
engineer. He wrote a lot of Facebook's
code. and they feel we don't matter
anymore. We're tools. We've been thrown
away. Uh a lot of people are are have
been given large retainer bonuses who
have not been fired. You stay. We're
giving you money. They are still
interviewing and they told me they're
interviewing not because of the layoffs
because they know they can find a job at
Meta. You know, these are super highly
paid people. They they can get a not as
highly paid jobs. They're in demand. But
they said, "I don't know if I'm going to
be assigned to data labeling." And as a
professional, I did not sign up to
become a manual data labeler. And a
bunch of my colleagues are doing that
and interviewing. So Meta is destroying
their engineering organization that
they've built up over 22 years. And I
think this might be end of the
incredibly strong Facebook engineering
culture that I know and I I I've learned
to actually love even though I've never
worked inside of Facebook and so many of
my friends have. So this is because of
AI. Now, not all companies are like
meta. This is pretty extreme, but it's
happening. It's happening right now. The
these are these are facts. But the
industry has a pretty interesting time.
And today, I want to talk about this. I
want to talk about what how everything
has changed in the past six months when
it comes to software engineering or or
well at least coding.
I'm going to give you a tour of the tech
industry of what what other tech
companies are doing. I'll give you a
brief tour uh because this is what what
what my head is in in day in day out.
And again, I'm I'm I talk with a lot of
these people. I I visit these companies.
I'm friends with a bunch of them. And
then I'll share a few trends that are
happening across the tech industry. And
then I'll close with advice to software
engineers and engineering leaders on how
we can navigate to prepare to to do the
best that we can and and also just you
know come out of this whole thing
stronger.
So everything has changed in this past
six month. This is a pretty dramatic uh
uh thing to say and but
it it it it has changed. So uh DHH David
Hellmire Hansen, creator of Ruby on
Rails, he was on my podcast in February
and and he told me that he actually
wrote this uh on on Twitter that just in
summer 2025, he spoke with Lux Freedman
in October and he said that AI was not
writing any of his his code directly.
But part of his resistance resistance
was that the models were not good enough
and it has now flipped by February.
Most of his code is being written by AI.
Now this is a person, you know, he's a
he's big into software craftsmanship. He
is not paid by any lab, but he decided
the models are now good enough. They
write better code than I can. He
actually told me this on the podcast. So
I I listen to to people like DHH uh in
in this sense. Simon Willis is someone
who is the one of the most uh quoted
person on Hacker News. He is an
independent software engineer. I love
Simon. Uh he uh he's he's also a friend.
Uh he created Django and he writes this
really good daily newsletter pretty much
where where he just experiments, he
builds open source and tries out all the
models. And he said that the models
released in November 2025, specifically
Opus 4.6 and GPT 5.4 uh have elevated
agents to being genuinely useful. we've
had the six months to get used to this
idea now. So, no wonder that companies
are now starting to spend big money to
spend this. So, he's also saying that
it's has changed. I got some data from
some of our partners, my friends at
Linear uh shared this data never never
shared before on how
how t how teams are using now agents to
ship more code. They are comparing teams
that are on linear and they're not using
AI agents and teams that are and by now
the teams that are using agents are
shipping five times as more code. We'll
talk about quality later but th this is
massive 5x increase. I mean we've
probably had five increp
like 20 years before and this is in less
than two years. uh
friends at cursor have shared uh details
on how devs using cursor are changing
the lines of code they produce in a year
and in a year it has gone up by almost
two and a half times from three up 4,000
lines of code to more than 8,000 lines
of code just on cursor so you know we're
we're seeing this acceleration the size
of PRs also from cursor is up by 3x so
if you combine those two that's six
times as much code and you know a lot of
you are kind of like I see smiling I we
know that there's six times as many bugs
yeah we'll again we're going to get
there
and also data from cursor the percentage
of devs using cursor who are accepting
changes from the AI without any manual
review is massively up in January this
is when opus 4.7 came out uh GPT 5.5
came out and what a lot of companies
realize that clock code cursor codecs
They're actually really really useful
and they're starting to trust it. And
again, remember when I told about you
about meta
merging to production without human
review? Yeah, that that was somewhere
there. So, what are tech companies doing
right now? And let me give you a bit of
a tour of the industry. So, uh at
Entrophic, I I visited their offices
last fall and I I talked with Boris
Churnney just in February, the creator
of Claw Code. And here's what they're
they're they're doing. Uh Boris
specifically runs five parallel agents
on his laptop all the time. He ships 20
to 30 pull requests a date and this is
on top of leading all of quad code. He's
very much a hands-on leader. He told me
that the PRDS writing documents to plan
are dead. They're using prototypes
across entropic to replace them.
Today 100% of cloud code is generated by
cloud code. Inside Entrophic is not 100%
but it's closer to 70 to 90% and there's
no target. This is just people using it
again but this is entropic. we shouldn't
be too surprised. Uh and then the
company built cloud co-work in only 10
days. Uh and it's become a massive
commercial success for them. Uh it
generates so much revenue. In fact, I
have some sources inside of Microsoft.
Microsoft tried to build a cloud co-work
because cloud co-work is really good for
for Excel and Windows to use it on
machine. Microsoft still doesn't have an
answer two and a half months later. I
heard that Sacha Nadella gave a deadline
of a month to this team to build it and
they couldn't build it. So don't forget
that there's differences between
companies and traffic is accelerated by
AI. Some companies are kind of held back
despite AI like Microsoft and again
we'll talk a little bit about that as
well. Open AI open AI also at uh a
friend from uh the pragmatic summit uh
in San Francisco in February. That's us
on stage uh with him and the Codex team.
We talked about a bunch of stuff and and
what he told me is uh some interesting
stuff. They have inside of OpenAI they
they have an internal version of the
chat GPT app and they have fix it
button. You can literally just take a
screenshot and say fix this bug and it
goes to codeex. It generates a a pull
request and an engineer can merge it. In
fact, even a non-engineer can merge it
and there's safety nets there. AI code
review obviously is everywhere. They
have multiple layers of it. uh they have
tiered versions. There's some code that
can go in with just AI code review into
production and there's some code the
critical path that humans need to
review, engineers need to review. Uh
most devs obviously run several agents.
There's this joke that uh when you're
walking around engineers are bringing
their laptop and it's slightly open.
It's slightly open so the local agent
can still keep keep running. And when I
was I did a video interview uh with one
of the OpenAI folks and I was just
jokingly asking like, "Oh, so like
throughout this interview, did you have
agents running?" He's like, "Did you
have an agent running?" He's like, "I
didn't have an agent running. I had
five." And I was like, "Oh, okay." Like
it's it's common for people to go into
meetings and their agents are running.
They're thinking about agents. They they
keep it on track. Like again, but these
are they are the most AI pilled people
in the industry. And of course, you
know, they they greatly believe in all
this. They all talk about AGI and and
when it's coming, not if it's coming.
But this inside of them, most people
don't really write code inside of
OpenAI. This has changed in October.
They still like there were devs who
wrote 30% of their code and 70% with AI,
but 30% by hand. And I think it's just
slowly going away. The Codeex team
obviously writes it all with Codex. And
they're telling me that taste, knowing
what to build is becoming pretty
important uh in inside the company.
Codeex also improves itself as as a fun
fact. It tests itself all the time. It
runs all the tests overnight. They kick
it off because most of the team is in
San Francisco. So it's one time zone. Uh
they have codeex run itself and look for
ways to improve itself. And by the
morning it comes up with improvement
suggestions which they either accept or
or reject. And when they have meetings
and debugging sessions when they start
the meeting they have voice notes that
they send to codeex as it goes and it
comes back by the middle or end of the
meeting with like results. It's it
sounds like science fiction, but again
that that's how they're working inside
of cursor. I I visited their office in
October in in San Francisco. Um they
they have you take off your shoes and
it's sometimes it's a mess, sometimes
it's super organized. There's like a
sorting algorithm invisibly happening
inside of their office. It's it's really
interesting slashcool. Uh but they're a
very nice group of of folks. Uh they
have gone all in on agents as of January
as well. They're like it used to be all
tabs and the editor. They're kind of
like moving on to agents. They still
have the old old experience but it's
increasing the old one. They they built
their own coding model. They're one of
the only companies outside of open air
and traffic who have a really good
coding model. I have no affiliation with
cursor. Uh but their composer model is
cheap which is going to be important as
as I'll talk about it. Uh and they
operate tens of thousands of NVIDIA GPUs
in massive data centers. They're leasing
it from Azure uh AWS and so on. And most
of their inference used to be uh
inference used to be so generating the
the response. It used to be their
biggest cost, but now they're also
training their models. So they're kind
of turning into this mini AI lab. And of
course now SpaceX is about to purchase
them or not or who knows, but it it
seems it's going to happen. Uh they're
also just everyone at Cursor is
technical. This is Lee Robinson
developer relationships at at Cursor. He
wrote u with Cursor. He migrated all of
cursor's sites to a different CMS with
and of course you know he's sharing how
how much he's cost to show that it's
very economical but this is this is not
a software engineer by job and everyone
a cursor is like that so these labs are
everyone goes there Google uh briefly
everything is custom at Google
everything including their ID Google's
internal ID is called cider they have
strange names for everything it used to
be a web-based tool now it's a visual
studio fork uh they have a thing called
jet ski which is anti-gravity but the
internal version which is integrated
with their their monor repo piper and
all of their other internal systems uh
they have critique a code review tool
which again they don't use github they
don't use all these everything is custom
inside of Google AI is of course
integrated gemini is integrated nicely
in there they have code search which is
the source graph for rest of the world
in fact source graph got inspired by
Google has some of the best code search
inside of Google they don't they don't
make it available uh uh outside and they
Google has so many internal systems.
Borg which is their version of
Kubernetes uh Monarch which is their
version of data dog uh many many more
piper their version of monor repo AI is
integrated into all of these things and
it's all integrated together really
really nicely so inside it's a really
good experience only problem inside of
Google is Gemini is just not as good as
Opus or GPT 5.5 and inside of Google
whenever engineers can use cloth code
they do but only they can only use it
inside the Gemini or which means that
Google doesn't have as good of adoption
of AI than some of the other companies.
Kind of weird, but they're working on
it. The CEO knows, he admitted it. They
want to get a better model about it.
And finally, Meta uh they they want to
build their state-of-the-art AI model.
Everything is about this. Uh they do
have an internal tool like Metamate.
That's their that's their AI tool for
coding. They have this thing called
trajectories. Whenever you you know when
you see GitHub commits inside of Meta,
you see the exact prompt that people
did. They rolled it out in December and
people in Meta got upset because no one
told them this would be public and you
could see like you know like staff
engineers saying like can you write me a
for loop and it it was all public and
everyone could see it. So some people
inside of meta, I talked with this dev
and he said like, you know, I started to
write my my my uh my uh chats with the
meta AI the code generation in Polish
because fewer people can read it now.
Okay, it but you know right now at Meta
they have bigger things to to worry
about. Uh this force reassignment to
build AI model force tracking of
everything. It's clear meta Mark
Zuckerberg wants Meta to have an model
that's better than Opus 4.8. eight. I
think either he's going to get it in a
few next few months or all of meta is a
lot a lot of meta is going to be like
disb not not disbanded but very very
demotivated.
Uh Uber my old company uh I talk with
them in detail. I have a deep dive on
the primatic engineer if you're
interested in learning about more of
these details. They built so much
in-house tooling and a lot of companies
do this but I'm just going to like
quickly show you how much in-house AI
tooling a company like Uber built. Uber
has about 3,000 engineers. So, just keep
that in mind. They have an AI, well,
they have a developer experience team
who is now pretty much an AI experience
team of like about 20 people or so. So,
they built an internal MCP gateway.
Pretty clear. You can, you know,
discover, register, do all do all sorts
of jazz. They built an Uber agent
builder, which is a no code way to build
agents for the rest of the business.
They have an Uber agent studio where you
can like drag and put together your
agents. Again, there's uh OpenAI has
something like this publicly. That's
open a As a Asian builder, but it's it's
for the nontechnical folks. They have
Uber Asian Builder Registry, which so
Uber is 3,000 engineers, but 20,000
other people. Those 20,000 people use
this thing. They create this stuff, they
plug it up, and engineers built this for
them. Uh Uber has an AI FX CLI. I'm just
going to call this the cloud code for
Uber pretty much. They built it
themselves, integrated with all their
system using all the different models,
etc. They have Uber Minion, which is
running background agents at scale. Uh
so you can again this is sim similar
thing as cursor background agents except
it's integrated into Uber's monor repo
and experimentation system called
morphus and and all of the other jazz
really really nicely and it works a lot
better. So even though devs can use
cloud code they will use minions because
it just works better and faster. For
example uber minions when you give it a
prompt it will analyze it and it will
give you a suggestion that ah these
prompts could work better results faster
cheaper etc. So this clock doesn't have
this yet. They have Uber code inbox. Uh
people are getting so many AI so many
pull code reviews that are are now you
know mostly AI reviewing code that
they're creating a system to show this
one needs your attention. This is
important. Focus on these things. So
people when they get into work they
start going through these things.
They're trying to make code a bit more
fun. They have something called smart
assignments where there's SLAs's where
you need if this is not this person
doesn't respond in like a day it goes to
the next one. It's a bit like on call
tooling again all all custom. They have
risk profiles. They will try to identify
this code change looks faking risky. You
need to you know like look at this
closer. And they have U review which is
the code rabbit or the uh the the sonar
uh for for for
Uber's internal again all all custom
work. So they build all this MCP agent
builder CLI minions etc. And the other
large tech companies they're doing the
same. I'm not going to run you all this.
Stripe has minions tool shed blueprints.
Z boxes ramp has inspect glass dojo
sensei. Sensei is a funny one. Shopify,
Sidekick, LM proxy, dev MCP server,
Airbnb, One everything, Catalyst and so
on. They all build their own own stuff.
Uh they have a dedicated infraorg
building all of these for all these
companies. So if you thought, you know,
you're pretty cool for like integrating
Slack into into integrating AI agent
into Slack, you are pretty cool. But
this is this is next level. I talk with
a bunch of startups and I'm not going to
go through all of them, but the general
trends I I see there uh it's kind of the
usual agents are are doing coding, doing
code review. There's a bunch of
creativity mostly about Slack. You know,
people tax Slack. I I saw a startup
recently that raised $70 million uh in
series B. They just told the agent like
fix all bugs in the codebase. Haha. And
everyone's laughing in Slack. And then
the agent came back like, "Oh, I
actually found like four critical
authentication issues where your back
door was wide open." And people were
like, Okay. I mean, that's that's what
startups are. They they didn't know like
their how their house is exposed. Uh uh
they're they're usually plugging in the
AI agents, integrating them, and some of
them are having fun vibe coding SAS. I
think it's just engineers having fun. I
don't think it's really a business
thing, but it's it's it's it's I only
see this inside of startups, not really
inside of big companies. And inside
traditional companies, so this is the
most interesting thing. It's all the
same. I mean, not the level of Uber.
They don't have dev platform teams, but
they are not really lagging behind. Uh,
for example, Cisco rolled out Codeex to
18,000 engineers back in January when
Codex was pretty small and they're doing
a bunch of complex migrations. JP Morgan
Chase built a multi- aent framework,
which is a fancy way of saying that it
just uses multiple specialized agents to
label customer interaction data. They
use evals, judgebased aggregates. Like,
it's it's kind of cool stuff like even
inside of these companies.
So this is what's going on inside. Now I
want to give you some of the trends that
I see crosscutting everywhere or most
mostly everywhere.
One of the big things that comes from
Laura Tacho. Uh this is me at the
pragmatic summit with Laura and and with
Martin Valor in San Francisco. She uh I
I messaged her last actually last night
and she replied this this morning. Uh I
was asking what do you see Lara? Uh
because she was C2 at DX. she's now uh
heading up pretty much developer
experience at AWS and she said that many
organizations get stuck uh not seeing
they see individuals doing great but the
teams are not like the team output is
not there and she said is because they
are thinking about AI as a productivity
tool for engineer for individuals and
she calls it of the individual speed up
juice things like email summaries slack
automations even code generation
however the companies that are moving
faster and they're seeing the result.
For teams, they are doing something
different.
They begin with a business outcome. For
example, I want to deploy to production
faster or I want to push more features
out with the same quality or I want to
improve quality. Spotify is a very good
example. We don't hear too much about
Spotify, but I talked with their CTO
about a month and a half ago. We had
lunch and he told me that their quality
for their their bar for using AI is the
quality needs to stay the same. So
they're not seeing a huge increase in
output but they have built a lot of
internal tools to check for the quality
and they're slowing down the rollouts of
AI versus you know what Meta is doing or
whatever they're not doing. And again,
that was their goal at Spotify. And
Laura was saying that you need you want
to build an agentic system that reduces
handoffs, that makes it easier to find
information and removes friction while
maintaining quality. That last part is
very important. Few companies do that.
And and you know, maturity comes from
applying AI to the system and not the
individual. And a lot of people are
focusing on the indiv individual and
that's why we're not seeing it. And she
wrote this mental model. She created
this. uh she was saying most companies
are in this thing where when you have AI
usage that is either individual or team
level and decision-m that is either
simple automation or agentic systems
most companies are in this bottom uh
left corner where you have individuals
doing simple automation where most
companies want to be is where they have
team level agentic systems but to get
there you need to do what I've shown you
Uber to do you you need to build a lot
of systems that integrate you need to
iterate on this it takes time. It takes
a massive investment. You're not going
to be able to buy claw code or cursor or
whatever vendor tells you to do that uh
that it does it because you need to
build it into your system with your
engineers. That's what Uber is doing for
sure.
Now, other trend token maxing and
tooling addiction. Um
hopefully some of you might be doing it,
some of you might not. It's going out of
style by the way just just I'm talking.
There is just a big pressure to look
productive and to not have a low token
count, especially inside of US tech
companies that don't really care about
budget until they do. But right now,
they some of them still don't. It's it's
it's ending. A token maxing is is when
you're just burning all these tokens
without value shipped on purpose. And
again, I I've talked to this happens at
Meta, Amazon, even in Microsoft
everywhere where they have internal
leaderboards. Microsoft still has it. I
don't know why they're not shutting it
down. They should listen to me. Uh there
uh also the pricing of these tools feels
a bit of addictive. You buy the $10 plan
or the $20 individual plan and then you
run into a limit and a generous limit.
But then you run to a limit and then
you're like ah let me buy the $100 plan
or the $200 plan. And once you buy it,
you now feel pressure if you're buying
it for yourself that you're not using
your your allowance. So you're starting
to use it more. And next thing you know,
you went out and you're now on on API
pricing. And also with every prompt once
you start using the AI agent the first
few months it's a bit like it's gambling
for some people get sucked into it
really like gambling. It's just one more
prompt one more prompt. People are not
sleeping that well. You're you're waking
up and thinking about your agents. If
you're paying if you're uh your company
if you're paying out of pocket you feel
AI being wasted. It's it's it's weird.
It's addictive.
Another trend is middle management
managers are just being cut either laid
off or inside of meta reassigned to
individual contributors or being told
you you need to be hands-on meaning you
need to manage less and and do more more
work. uh there's just a flattening
happening and the interesting and a and
whenever a management is fired or or
laid off it's said oh it's because of AI
whatever it doesn't help but the
interesting thing about this is
what happens if we have less middle
management I mean it's popular to hate
on middle management on managers senior
managers and directors top level
management is a sea level the CTO and
the middle management is everything in
between uh maybe until front line
management engineering management and
you know usually we don't know what
directors do uh or or if they're
necessary. However, in my experience,
good middle management, good directors,
good senior entry managers, they are
very technical. They could be hands-on,
but they choose not to. But they listen,
they see what's happening. They pay
attention and they make small changes.
Ah, there's a lot of outages we're
having right now. And software engineers
will just pile on and and do nothing.
They will stop and be like, "Okay, let's
create a task team. Let's build this
system. uh you you get I will pull you
off these teams and we'll make our
engineering culture better. Good
engineering management improves
engineering culture and a lot of
companies are getting rid of engine
management or or bidd management and
engineering culture will go down. This
is a fact as far as I'm concerned.
Another interesting trend at the same
time CEOs and CTOs are back to coding.
uh Gillor Moranch uh founder and CEO of
Verscell. I I had a lunch with him on on
one of the investor events in in
February as well. uh he was right saying
recently that he is seeing so many cos
and CTOs are back to coding with a fury
with all this enthusiasm and he has
public company CEOs DMing him saying hey
we're using Versell or cloud code and
you know like I'm I'm doing it I'm so
excited again and this is all the time
while we're having less middle
management now imagine having less
middle manager to protect engineers and
the co and CT are coding vibe coding and
they're saying oh it's they think it's
complete but you know it's it's not
really complete
a mega trend that is happening like and
it starts to like I noticed this a week
two weeks ago. So, I wrote about it a
week ago and then today uh
like to uh hold on and and then today I
I see uh Sam Alman, this is just from
this morning saying that he is noticing
that AI budgets are seemingly become a
huge issue for some companies and
something that has come up and something
that has never happened before. And I
was pinging people at OpenAI like does
he read my newsletter because I wrote I
I wrote about this last week for
subscribers and someone open said like
someone posted into Slack and like Sam
read it and but it's happening and this
is coming out of the blue. There's this
joke going around as of yesterday on
Reddit saying hey uh oh baby I see
$15,000 are gone from your from your
shared account. Like is this what I
think it is? engagement Frank.
Yeah, I I feel for that guy. He's soon
going to be single,
assuming it's it's it's not a joke. Uh
but it's it's happening and it's getting
worse. Uh Antropic has turned on API
pricing for enterprise customers,
meaning anyone who's not a startup or an
individual is not getting discounts.
GitHub Copilot turned it on just two
days ago on the 1 of June and people are
pissed because they are have burned
through their usual budget of let's say
$200 or or however much it was in three
days that used to take a month and they
are and this is hitting everyone right
now. Everyone will be paying a lot more.
Now Uber is an interesting case again
because in March their CTO uh said that
they have burned through the whole
budget for the year with AI costs and we
were wondering what they're going to do
but we now know they are now setting a
cap of $1,500 $1,500 per month per
engineer on AI and if you hit that
you're going to use the free models and
I've been doing research this is what a
lot of companies are doing a lot of
companies not doing this much some doing
$200 and then you're going uses zero
models on GitHub copilot and now
engineers want to do it but this is a
very very fresh trend costs are it's
ridiculous when it's as much as an
engineer and no one no one wants to pay
that no matter what the AL apps say
and finally some trends across the
software craft we've talked about like
kind of business trends and and and AI
trends but what is happening to software
engineering and and the craft the
conference that we're here one is a huge
drop in quality everywhere this one
comes from yours truly that's my account
I was so pissed off at claude.ai,
their flagship website, for about a
month for a month. Every time I went to
the website, this is the website itself.
Uh I I did a screen recording after I
got pissed off enough uh because it kept
happening and no one was fixing it. You
went to the main website, cloud.ai, and
I immediately start typing my my quote.
And here I'm starting to type, how can I
do this? And as soon as I type, how can
there's a refresh? Now, there's a React
uh life cycle component happening here
where the page finally refreshes and it
loses all that I've typed before and I
maybe I'm old school. I use the website
so much it just kept happening and
happening and finally I tweeted about it
saying like how on earth does Entro oh
and I'm paid user. I'm not a free user.
There's millions of people hitting this
every single day and Entrophic doesn't
care and they're building AGI. So, I
tweeted about it. Uh and the product
manager on the team said, "Oh, great
feedback. I dug into this. this it will
be fixed. This is the short way of
saying, "Oh, thanks. We have no clue
that millions of people every day are
doing this. Oh, and we are not even dog
fooding our own stuff." And this was
there for a month. So, and oh, and we're
the fastest moving and biggest and most
profitable company, but we don't like a
a bank does so much better in this
sense. There's not these I mean, we can
argue if if they fix it that quickly,
but and they did fix it eventually, but
this is entropic. And and it's not just
entropic. Open AAI OpenAI
bragged about how they built this
amazing agent builder that is similar to
Uber's internal agent builder in only
six weeks with one engineer with, you
know, codecs. Amazing. Great. Um,
quality is terrible. People on launch
tried to use it and they kept running
into so many issues. Their forum is full
of of comments which are unresolved.
OpenAI did not come back and fix it.
This is from three months after launch.
someone saying I was bullish on agent
builder when it came out but for example
P 0 type bugs are not getting fixed or
takes ages it just seems like
abandonware so I mean was it worth it
for them building this thing and then
just forgetting about it and AI clearly
didn't help build higher quality
software it's faster but it's just
Amazon uh
a AWS
an engineer allowed the internal Cairo
AI coding tool to make certain changes
and the agent opted to delete and
recreate an environment inside of Amazon
causing a massive outage. Amazon had AI
bugs that were happen because the AI
generated code where Amazon stores their
com's flagship website part of it went
down. This never happened with Amazon.
Same thing as it never happened with
with meta and this is over reliance on
AI or not caring about quality. Amazon
has has made this change uh that it now
requires a senior engineer to review any
AI generated change because they realize
the junior engineers will just say looks
good to me and it causes an issue.
Open code uh is the leading AI hardness.
Uh they're they're like the cloud code
for open source and they use all
different models. Daxrad is the founder
and I love DAX because he's super
honest. They are building a super
popular AI tool. They have almost a
million daily active users. They're
growing. They've grown 10x since the
last four four or five months and he's
very and he doesn't he's kind of
skeptical of AI hype but this is a guy
who's built developer tools but it's I I
love Daxis he's really authentic on my
podcast just last week he told me we're
shipping way more hacks where we should
have first rethought the whole system
from the ground up redesigned it to make
more flex make it more flexible so I
think our judgment meaning the open code
team's judgment is off and he was also
saying how you know we're in the AI
coding tool space but you know what's
not happening?
No competitor is beating us because
they're using AI better than we do. And
he said that frankly, I don't think
we're using AI that well. Like we're
actually telling ourselves to use less
AI and there's no competitor that is
beating us because they're doing faster.
In fact, they're kind of winning because
they're still one of the most quality
harnesses because they're slowing down.
Do you know what is a contradiction?
a CEO and founder of an AI company
saying we need to use a bit less AI and
he he actually told me we need to do
more thinking we should build fewer
things and build the things that matter.
I'm paying attention to him
I'll I'll
I'll send that to Dax. And another trend
related to this is just everything is
broken. Uh GitHub is is such a prime
example. Uh this was two weeks ago. all
your poll requests were gone on GitHub
for about 8 to 12 hours. Uh there's a
there's an alternative GitHub uptime
tracker. I think it's you just have to
search for the actual the missing GitHub
status. Uh something like that which
tracks all outages that they report and
it estimates and B based on this
estimate they don't even have one nine
which is means they're down some part of
GitHub is down 10% of the time which is
absolutely unserious but this is a
serious company. I talked with the
GitHub team. I talked with their COO and
they gave me data that they didn't give
anyone else because they published
graphs without the numbers but they gave
me the numbers and they told me it's
because of the load. Now the load is
this. It is a 3x load increase over 2
years time. And they were like, oh, you
know, like this is a huge load increase.
We could have never prepared for that.
And I'm saying
really
that's it. This is bringing GitHub down
to nines. I I'm I do not buy this. Maybe
there's other things, but something was
really broken inside of GitHub. I'm not
going to say this is AI generated code
but if GitHub cannot
deal with a 3x increase over two years
and sure this will be 5x increase later
you're doing something wrong guys like
other startups pick up this load
laughing and there there's there's
details github has a has a Ruby on rails
model and so on and so forth but yeah um
it's just breaking and uh Mario Zechner
the creator of pi which is what powers
open code uh this is the Austri it's
with Armenure the Austrian AI mafia who
are on my podcast he told me it just
feels software has become a brittle mess
everywhere 98% uptime feels like the
norm on most services user interfaces
have the weirdest bugs I showed you one
and on on on cloud but it's everywhere
and he says that I give you that it's
been the case for longer than agents
exist we've always had it but it feels
to be accelerating everywhere you feel
you see this I even saw with modar
telecom the other I don't think I was AI
generated because I don't think they use
AI but yeah I had a big like software
issue with them and I needed to call
customer support.
One more trend is slob buries the
software engineer who still care. Here's
what's happening.
There's a lot more poll requests. Uh
there's just a lot more code. Uh and a
lot more are AI generated. Uh most
developers inside a company uh have
review fitting and they see it's AI
generated. their AI review went and they
said let's they said it looks good to me
LGTM or you know I'm not sure how uh but
they just do a thumb and they never
reviewed it. There are a few developers
who do review it. Hands up if you
actually like still review code like
properly. Hands up if you if you give it
an honest shot.
Yeah. But there there are many of you
who still try and you still catch the
bugs and you still push back and you
still see that the agent has duplicated
code or well the developer is the agent.
You push back and they are being
overwhelmed. They are being burnt out.
They are being fed up. They are feeling
that they're not rewarded. Oh and when
it comes to performance review time,
they're not going to be rewarded.
They're not seen as the ones pushing out
all the features. So some of them are
burnt out and some of them just quit.
Dax told me that at open code they are
hiring a bunch of these people who are
leaving their companies h because
they're just burnt out being the sole
person still keeping things alive and no
one care. Engineering management is
gone. They've either let them go or
they're now now less hands-on. So
there's no one left to care.
Finally, I I talked with Kent Beck. Uh
he'll be this keynote peer tomorrow and
he summarized this really well. Kent is
amazing at summarizing findings. He
said, "We're accumulating code faster
than we accumulate trust." He said that
with code you need to trust it. You need
to understand it. We don't have time to
do that right now.
AI also amplifies software engineering
experience. So seniors gain the most uh
judgment is rewarded. And we see this
everywhere. Hill Wayne, he'll be a
speaker tomorrow. But he was telling me
how some people are saying oh AI will
help with formal verification with TLA a
very complicated language. He'll show
you a demo tomorrow. And he said the
only people who have been successful
with AI generating TLA plus
specifications that work are TLA plus
specification experts who in the prompt
gave the exact specification of what
kind of prompt to generate. Everyone
else good luck with that. And this is
true for software. If you're a junior
engineer, if you've never built a mobile
application, you can prompt a native iOS
app, you can prompt the agent, it'll
build something, but you know, it's not
going to be maintainable.
Uh old patterns are seeming to coming
back. Uh Dax told me how domain driven
design and verbals guardrails they're
using this open code all the time
because agents are the new junior
engineers. You can start off a lot of
them but these junior engineers I mean
if you think of it like that they need a
lot of guardrails and we used to these
boring enterprise patterns used to
become unpopular because they're long a
long winded you have to explain you have
to type out but they keep agents in
check. So, it might be time to dust off
some of these books and start to use
design patterns again. I'm actually dead
serious about this.
So, this is where we are. Uh, it's it's
just a lot of change, all all sorts of
of things. It's confusing. I'll leave
you with with a little advice. One is is
the the title of the talk, slow down to
speed up
you. My suggestion is to cap your daily
agent usage to what you can either
review or verify. You might not need to
read the code. Peter Shamberger, creator
of OpenClaw. I did a podcast with him.
He said that he ships code that he does
not read, but he builds his own
verification systems. He thinks in
architecture. He always looks at the
module. He has the AI draw AI diagrams
for him. So verify, do not ship more
than you can verify or this might mean
reviewing. By the way, as well, uh, tech
depth is now very cheap to remove. We're
talking about how it's built up. Have
the eight kick off the 80 to remove the
tech deb. Be the chief tech deck remover
on your team. you will feel better for
it and it's much easier. Forget that
it's hard to remove it. It's not. And if
you're not removing it, you're not using
AI efficiently for yourself.
Uh experiment with different different
usage of AI agents because there's no
one-sizefits-all and and you know,
listen to talk with with with friends
how they're using it. Get ideas, tell
them what you're doing. And you know,
like just spend more time thinking and
understanding. This is what Dax, the
creator of Open Code, he says that he
used to spend 95% of time thinking and
5% of time coding. And he said like,
"Yeah, AI is cool because now I can uh I
can now spend 25% less time coding. So I
spend 96% of time thinking and 4% of
time coding." You're not going to have
the luxury, but you know, like it's a
good way to think about it
and you just spend time thinking and
understanding
one thing about working in different
way. Michelle Hashimoto is the creator
of GOI uh founder of of Hashikarp, a
really nice guy. He was also on the
pragmatic engineer podcast in March and
his rule for building software. He came
up with this. He is not an AI maxi but
he likes to be productive. He has one
agent in the background always doing
something. He said if I'm coding I want
an agent planning. If they're coding I
want to be reviewing. And he always has
just one extra agent. He does not use
multi- agents. But this is what I mean
by experiment. Some people use five
agents and they can manage. I don't know
how personally. Michelle found that he
can use only one agent. He has like this
this buddy that he has all the time and
he said it works for him for now at
least. So just experiment, try different
ways of doing things. You don't need to
go overboard. He's a very productive
engineer. He does not care about AI. He
cares about like writing high quality
software.
From Addios Manny uh I I met him two
years ago back in Google and also also a
friend. He
said one of the best things, don't
outsource learning. It's just too easy
to let the AI write code while you skip
all of the learning. The bug get fixed,
but your mental model does not. We're
trading off your capacity for present-
day speed, and the tools don't force us.
So, you need to just whenever you use
these AI agents, do not skip the
learning. Understand, learn something
when you use an AI agent. And this is
what I mean. You don't need to review
all the code, but you need to learn
something from or build a system, have
it build something for you.
Uh when when I look around on a job
market, I have I have some good news.
The job market seems okay globally. I
they did a deep dive in the pragmatic
engineer. Uh and you'll have access to
to that deep dive, the full one, uh very
soon. Um the top tech companies are
hiring more than they have before. So
it's going up. It's not as good as as
before. Now the bad news is that in in
the US and in the UK, we're seeing 20%
increase in software engineering. This
is not AI engine. This is software
engineering. In Germany and France,
we're seeing 13% and 10% decrease, which
is it's not terrible, but it's not
great. This is from two years ago, and
in Canada, it's flat. I don't have data
deals from Hungary, but as we know,
Hungary is very much tied, as we know on
the press, to Germany a lot. So, a
similar trend might be happening. This
is data from indeed. It's a pretty
reliable data source. Uh, and I I I
trust them. uh now on the job market in
the US and and US tech companies the top
tech companies AI engineering is an
absolute blast in hiring so this is AI
engineering is part of software
engineering it's now taking up about 10%
of all software engineering is going up
so anything a engineering means you're
building rag you're building evals
you're building systems that are doing
something with LLMs
future profiting for your career my
personal advice build things that that
build on top of AI and LMS because you
will get hands-on with rag AI
engineering by the book by AI
engineering by Chip Huan. It's a very
practical book and try to build
something either on the side build your
own podcast recommendation system or
whatever or at work show off to your
colleagues answer and even your managers
and your your you know your your
colleagues will be happy to see oh
really cool like you just built an
internal tool to do XYZ.
Don't uh outsource your your your
thinking to AI. Try to think more on
product understand the business. Um
there's a book called product uh the
product-minded engineer. I have a blog
post called the product-minded engineer.
Talk to product managers. Uh and you
know just understand how the business
works. It it is more important and try
to become a domain expert. Uh try to
become this industry insider. If you are
working in agriculture company,
understand the agriculture because
there's a lot of software engineers but
there's very few who have talked with
farmers. If you're working at an
automotive company, talk with the
mechanical engineers as well. Again, if
you build that domain expertise outside
of software engineering, you will be in
demand the next time your company is
does either downsizing or you want to
move elsewhere.
If you are engineering leaders, my
advice to you, you need to be hands-on
or you need to stay hands-on. Some of
you will think, uh, not again, yes,
again, otherwise you will be out this
time. And it is easier to do this with
AI. You can turn to AI to explain stuff
for you. You can you can start to to
contribute stuff. I'm hearing at
companies where the top of the top
hundred committers, five are uh are
product managers and so on or or
engineering leaders. And also you can
just help integrate AI into the systems
level. That removes friction
except you will be doing less people
management. You will and the business
expects you to do less of it. If you
love doing people management,
either you know either you burn yourself
out or or you will do less of it. And if
you're an engineer, if you're a
developer, you will get less career
support. Also, we're probably going to
less pay rises and some of those things
for a while. But again, it's just we
will have less management with all the
good and and all all the bad parts of
it. Finally, I I'll close with this. The
change I I I talked with Martin Fowler,
I talked with Grady Bush, I talked with
all these people. They all said change
has never been this fast in the software
industry since the 60s easily in in in
12 months. We've had AI go mainstream
across coding tools. If you are
overwhelmed, absolutely okay. A lot of
us are overwhelmed. I I was overwhelmed.
Sometimes I still am overwhelmed with
with how fast this change and how not
predictable it is. But from just time
time to time, pat yourself on the back.
You are keeping up. It's hard.
Look around. just stop for a little bit
and make a change. How can I make this
more sustainable? How can I produce more
quality? How can I stop do how can auto
automate some of these things? And then
rinse and repeat.
Gerge Oros everybody.