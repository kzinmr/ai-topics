---
title: "Bureaulogy"
url: "https://grantslatton.com/bureaulogy"
fetched_at: 2026-04-29T07:02:16.537290+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Bureaulogy

Source: https://grantslatton.com/bureaulogy

Bureaulogy
I'm fascinated by the formation, evolution, and perpetuation of bureaucracies.
If I were to ever lose my mind and decide to go do a sociology PhD, I'd absolutely do it about bureaucracy. I'd want to establish a new subdiscipline of
bureaulogy
— the study of bureaucracies.
I think this subdiscipline is just as real and interesting as something like anthropology or psychology.
Some principal questions of the field would be:
Why do bureaucracies inevitably form in every organization of humans on a long enough time scale?
What are the common elements shared by all bureaucracies, and what leads to these commonalities?
Why do bureaucracies lead to inevitable organizational decline and eventual collapse?
What methods or techniques can be used to slow bureaucratic decline?
Is bureaucratic decline deliberately reversible?
This post attempts to start answering a few of these questions.
Why do bureaucracies form?
The following reasons are in no particular order.
Dunbar's number
Dunbar's number
is a hypothetical number of relationships the typical person can keep track of. It's around 150. It's a little pop-psychology, but there's certainly something there.
In my experience, once the size of an organization exceeds a critical threshold in this vicinity, bureaucratic tendencies accelerate rapidly.
Below this number, it's possible for everyone to have some context on what everyone else is doing, and if they don't, the context is easily attainable by talking to 1-2 people.
Here's an example scenario where bureaucracy forms:
Alice is a longtime employee in an organization that has grown to 300 people. Bob is a new employee on the other side of the org from Alice.
One day, Bob does something stupid and causes an outage.
Alice could have told Bob the thing was stupid and would cause an outage if only she had known, but the org is so big, she can't keep track of everyone anymore, especially all these new-hires.
Alice proposes that all changes must first create a change proposal document that must be circulated and approved by all the senior engineers of each sub-organization so outages like this won't happen again.
Voila, a pretty extreme bureaucratic process has been formed (with good intentions!).
Upside-Downside asymmetry
It's generally true that actual losses are perceived as worse than missing out on possible gains.
Concretely, imagine an opportunity with a 60% chance of gaining $100, and a 40% chance of losing $50. A rational actor should probably take this chance! The expected value is $40.
But that expected value treats the dollars that might be gained as equal to those that might be lost. But the employee is not necessarily optimizing for dollars to the company — they are optimizing for their own individual status within the company.
For psychological reasons, it could be that losing $1 hurts one's status as much as gaining $4 helps it. Under such a ratio, the expected value of this opportunity
to the individual decision-maker
is -20 status-adjusted dollars. The decision-maker decides to do nothing instead of take the opportunity.
I've seen this play out, and the ratios are actually
far
worse in real life. One project blows up and loses $1M. Another is wildly successful and gains $100MM. The magnitude of the status gain and status loss are similar, despite 100x different monetary magnitude.
This is somewhat related to the idea of
loss aversion
but it's not quite the same thing, because it's not the individual
perceiving
a loss to themselves as being worse than a gain. It's their peers
actually acting as if
the loss is much worse than the gain.
Inclusivity impulses
It's often the case that a decision only needs buy-in from 1-3 key people to be finalized and executed.
However, in a team situation, this dynamic creates an implicit hierarchy of who is high-judgment, valuable, etc — the implication being the excluded members are
not
.
So most people, not wanting to be seen as rude, will simply invite the whole team to the meeting.
Blame-assignment hesitance
It's natural to avoid blame for oneself. But the flip side of this is most people also want to avoid blaming others for social cohesion reasons. It's awkward to place the blame on a colleague.
This tendency will lead to the creation of well-defined bureaucratic processes that allows one to blame the process instead of the person, because blaming the process is much less painful.
Team-oriented ownership
This one usually comes hand-in-hand with blame-avoidance tendency. If you have a service or process owned by a single individual, and that thing has an issue, it's clear whose fault it is. However, if it's owned by a team, the blame is more diffuse and less painful.
Team-oriented ownership creates communication overhead and necessitates processes to coordinate, thus creating bureaucracy.
Promotion legibility
In a very small company, small enough that there are no "teams" — less than 20 people, perhaps — you really don't even need formal job leveling. No SDE 1, SDE2, Staff Engineer, etc. Just CEO, engineer, marketing guy, etc.
Once you get above this number, but still below Dunbar's number (see above), you will probably want levels of some sort because you'll be split into teams, teams have leaders, etc.
When you're below Dunbar's number, you don't need strict promotion criteria. Everyone has a somewhat accurate sense of where they fall in the lineup of delivering business value, because everyone has context on everyone else.
You get promoted to SDE2 when the business value you deliver is in the ballpark of other SDE2s. There is no formal criteria, just relative comparison.
Once you exceed Dunbar's number, this falls apart. The relative rankings at one end of the org will start to drift from the other end.
Different directors' sub-orgs will be known for having softer promotion bars and will attract a certain type of ladder-climbing engineer.
Seeing perceived inferior peers get promoted will generate morale issues in adjacent orgs with higher promotion bars.
This morale problem will result in more formal promotion criteria being instituted.
"To get from SDE1 to SDE2, you need to check these 10 boxes. Push 5 major changes to prod. Mentor an intern. Successfully get 3 design documents approved." Etc.
This promotion criteria forms an entire bureaucratic box-checking culture.
Selection effects
Bureaucracy begets bureaucracy. Specifically, once you have some bureaucratic culture created by other listed mechanisms, that culture
will attract people who thrive in that culture
.
That is, you will attract people who like bureaucracy. These people will create more bureaucracy.
Related reading:
Incentives as selection effects
— an excellent essay about what kind of employees you attract by the ever-wise Sebastian Bensusan.
The central thrust of Sebastian's essay is:
When you apply a new incentive, you select for a new population that prefers the incentive.
When you create promotion checklists, you attract the kind of person who wants to follow a promotion checklist. When you mandate design documents, you attract the kind of person who likes to write design documents. When you create a bureaucracy, you attract bureauphiles.
Methods to slow bureaucratic decline
This section is mostly a mirror of the "Why do bureaucracies form" section above. You slow bureaucratic decline by doing the opposite of what promotes bureaucratic decline.
Nonetheless, let's discuss some tactics with case studies.
Minimize headcount
If exceeding Dunbar's number is bad, you must minimize headcount. WhatsApp had hundreds of millions of users with 55 employees. Instagram had 13 employees when acquired by Facebook. Craigslist 50. The list goes on.
Where you cannot minimize headcount, you must divide the company into organizations that are effectively separate companies. AWS S3, for instance, could basically be its own company independent of the rest of AWS or Amazon as a whole. The rest of Amazon calls S3 with the same API the public customers do.
Fire aggressively
This one is tricky to write, since I don't know if I'm the kind of person who can actually employ it. But it does empirically work in the case of Elon's companies.
There are a few reasons to fire aggressively.
One is to keep headcount low. Just because you're a billion user company who
could
have 10,000 employees doesn't mean you
should
have 10,000 employees if you could get by with 100.
Another is that firing people, particularly middle managers, prevents bureaucratic structures from forming. This is obviously a blunt instrument, but it works. It forces people to go directly to the source of the issue rather than through a chain of intermediaries, because those intermediaries are unstable in this regime.
Finally and most generally, there is an optimal amount of firing, but in practice you can never hit it. You will always fire too many, or too few. If your goal is to stay agile, you must err towards too many. If you fire too few, eventually your org will be dominated by those you probably should have fired.
This is the most painful policy to implement for most non-sociopaths but empirically seems to be the only way to stave off sclerosis in the long term.
Directly responsible individual
Each process, line of code, document, etc should have a single person who
owns
those things.
By own, I mean the person can explain:
What it does
Why it can't be simplified or deleted
If it can be simplified or deleted, what the plan is for doing so
How it interfaces with other things
The person who owns those other things
What improvements they've been thinking of
What keeps them up at night, i.e. what might go wrong
The anti-bureaucratic advantages of this are many:
It is clear if someone is doing an egregiously bad job of managing the things they own and should be replaced — this is much harder or impossible with shared team ownership
There is no communication overhead within a person's own mind about how to manage their thing, so they can operate and optimize much faster
Because this person owns their thing, and knows the individual person who owns adjacent things, those people can work 1-on-1 which is easily 10x more efficient than team-on-team interfacing
If a person owns a thing that needs to be deleted/replaced, it is a lot easier to move that 1 person to a different thing, whereas a team is much more likely to try to "defend its turf" to preserve its existence (often driven by the team manager whose incentives are not aligned here)
Vibes-oriented promotion process
There are two main ways to do promotions:
Somewhat capriciously, at the whim of whatever command chain you're in
By a formal process with checklists and criteria to get promoted
If you only look at legible metrics, #2 seems superior. Employees have clarity on what they need to do to get promoted. There is less room for unfairness or nepotism. It's easier to standardize across far-flung parts of the company.
The downside is illegible but huge. The fundamental problem with a bureaucratic promotion process is:
You want to align employee incentives with company success
There is no well-defined algorithm for company success that you can write down (if there were, every company would be following it and be successful)
Therefore, any checklist you write down is a crude approximation of the company's success function and not entirely aligned
Here's a contrived example. Your senior engineers write a lot of code. So you add a checklist item: to get promoted to senior, you must commit 100K lines of code. Congratulations, you have now incentivized creating bloat.
The only checklist item you can actually put that is fully aligned is "creates business value". But how to define business value?
Some things are easy to put a dollar value on. But many others aren't. What's the dollar value of additional tests? What's the value of better documentation? It's just a judgment call.
No matter what checklist you create, it will be exploitable in ways that do not promote business value.
Not only is it exploitable, but you have also now created a selection effect to attract the kind of employee who thinks they will better be able to exploit it.
Less sinisterly, even employees who aren't explicitly trying to exploit the promotion process, but are still just drawn to the legibility of a checklist, are not as good as the ones who do their jobs with only business value in mind.
Implementing a promotion process based on executive intuition and not checklists is hard and has illegibility issues, but the alternative is horribly misaligned incentives and eventual company sclerosis.
Executive intuition promotion process also enables fighting the upside-downside asymmetry described above. The checklist method will often overly penalize risk-taking that doesn't work out. A smart executive knows that sometimes you swing and miss, and that's ok.
A note on Elon
At the risk of sounding like a complete Elon fanboy, there really is nobody that does all this better than him. Tesla and SpaceX are among the best examples of large companies (>10,000 employees) that still move incredibly fast. How do they do it?
Here's an example email that Elon sent to Tesla employees. I have bolded particularly relevant sections.
Subject: Communication Within Tesla
There are two schools of thought about how information should flow within companies. By far the most common way is chain of command, which means that you always flow communication through your manager.
The problem with this approach is that, while it serves to enhance the power of the manager, it fails to serve the company.
Instead of a problem getting solved quickly, where a person in one dept talks to a person in another dept and makes the right thing happen, people are forced to talk to their manager who talks to their manager who talks to the manager in the other dept who talks to someone on his team. Then the info has to flow back the other way again. This is incredibly dumb. Any manager who allows this to happen, let alone encourages it,
will soon find themselves working at another company
. No kidding.
Anyone at Tesla can and should email/talk to anyone else according to what they think is the fastest way to
solve a problem for the benefit of the whole company
. You can talk to your manager’s manager without his permission, you can talk directly to a VP in another dept, you can talk to me, you can talk to anyone without anyone else’s permission. Moreover, you should consider yourself obligated to do so until the right thing happens. The point here is not random chitchat, but rather ensuring that we execute ultra-fast and well. We obviously cannot compete with the big car companies in size, so we must do so with intelligence and agility.
One final point is that managers should work hard to ensure that they are not creating silos within the company that create an us vs. them mentality or impede communication in any way.
This is unfortunately a natural tendency and needs to be actively fought
. How can it possibly help Tesla for depts to erect barriers between themselves or see their success as relative within the company instead of collective? We are all in the same boat.
Always view yourself as working for the good of the company and never your dept
.
Thanks,
Elon
Some notes on this email:
Several mentions of the importance of aligning with business value as the primary goal
Threat to fire people who don't do this
Acknowledgment that bureaucratic tendencies exist and must be actively fought
Conclusion
Nobody sets out to create a bureaucracy. But it's not enough not to pursue bureaucracy. You have to become a student of the bureaucratic dark arts and use that knowledge to ward against it.
You have to study bureaulogy.
A request
If you have any additions to this article — mechanisms that bureaucracies form or can be fought — send me an email and I'll try to work it in. I'm particularly interested in anecdotes from real experience.
