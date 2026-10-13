---
title: Google SRE - SRE vs DevOps, Similarity and Difference
source_url: https://sre.google/workbook/how-sre-relates/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/how-sre-relates.html
original_sha256: df84fcd1320f7d56655f034a4ccff408511c4f8beb9f11ef77321fce8f67b5d0
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/how-sre-relates/
ingested: '2026-10-14'
sha256: c1bd8f8c70d384b2744186daf07135c1bb22e7680008ba627c05ede94d81f889
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
How SRE Relates to DevOps
class SRE implements interface DevOps
By Niall Richard Murphy,
Liz Fong-Jones, and Betsy Beyer,
with Todd Underwood, Laura Nolan,
and Dave Rensin
Operations, as a discipline, is
hard
.
1
Not only is there the generally unsolved question of how to run systems well, but the best practices that
have
been found to work are highly context-dependent and far from widely adopted. There is also the largely unaddressed question of how to run operations teams well. Detailed analysis of these topics is generally thought to originate with
Operational Research
devoted to improving processes and output in the Allied military during World War II, but in reality, we have been thinking about how to
operate things better for millennia
.
Yet, despite all this effort and thought, reliable production operations remains elusive—particularly in the domains of
information technology
and
software operability
. The enterprise world, for example, often treats operations as a cost center,
2
which makes meaningful improvements in outcomes difficult if not impossible. The tremendous short-sightedness of this approach is not yet widely understood, but dissatisfaction with it has given rise to a revolution in how to organize what we do in IT.
That revolution stemmed from trying to solve a common set of problems. The newest solutions to these problems are called by two separate names—DevOps and Site Reliability Engineering (SRE). Although we talk about them individually as if they are totally separate reactions to the enterprise mentality just described,
3
we hope to persuade you that in fact they are much more alike, and practitioners of each have much more in common, than you might assume.
But first, some background on the key tenets of each.
Background on DevOps
DevOps is a loose set of practices, guidelines, and culture designed to break down silos in IT development, operations, networking, and security. Articulated by John Willis, Damon Edwards, and Jez Humble,
CA(L)MS
—which stands for Culture, Automation, Lean (as in
Lean management
; also see
continuous delivery
), Measurement, and Sharing—is a useful acronym for remembering the key points of DevOps philosophy. Sharing and collaboration are at the forefront of this movement. In a DevOps approach, you improve something (often by automating it), measure the results, and share those results with colleagues so the whole organization can improve. All of the CALMS principles are facilitated by a supportive culture.
DevOps, Agile, and a variety of other business and software reengineering techniques are all examples of a general worldview on how best to do business in the modern world. None of the elements in the DevOps philosophy are easily separable from each other, and this is essentially by design. There are, however, a few key ideas that can be discussed in relative isolation.
No More Silos
The first key idea is
no more silos
. This is a reaction to a couple ideas:
The historically popular but now increasingly old-fashioned arrangement of separate operations and development teams
The fact that extreme
siloization of knowledge
, incentives for purely local optimization, and
lack of collaboration
have in many cases been actively bad for business
4
Accidents Are Normal
The second key idea is that accidents are not just a result of the isolated actions of an individual, but rather result from missing safeguards for when things inevitably go wrong.
5
For example, a bad interface inadvertently encourages the wrong action under pressure; a system misfeature makes failure inevitable if the (unarticulated) wrong circumstances occur; broken monitoring makes it impossible to know if something is wrong, never mind
what
is wrong. Some more traditionally minded businesses possess the cultural instinct to root out the mistake maker and punish them. But doing so has its own consequences: most obviously, it creates incentives to confuse issues, hide the truth, and blame others, all of which are ultimately unprofitable distractions. Therefore, it is more profitable to focus on speeding recovery than preventing accidents.
Change Should Be Gradual
The third key idea is that
change is best when it is small and frequent
. In environments where change committees meet monthly to discuss thoroughly documented plans to make changes to the mainframe configuration, this is a radical idea. However, this is not a new idea. The notion that all changes must be considered by experienced humans and batched for efficient consideration turns out to be more or less the opposite of best practice. Change is risky, true, but the correct response is to split up your changes into smaller subcomponents where possible. Then you build a steady pipeline of low-risk change out of regular output from product, design, and infrastructure changes.
6
This strategy, coupled with automatic testing of smaller changes and reliable rollback of bad changes, leads to approaches to change management like
continuous integration (CI)
and
continuous delivery or deployment (CD)
.
Tooling and Culture Are Interrelated
Tooling is an important component of DevOps, particularly given the emphasis on managing change correctly—today, change management relies on highly specific tools. Overall, however, proponents of DevOps strongly emphasize organizational culture—rather than tooling—as the key to success in adopting a new way of working. A good culture can work around broken tooling, but the opposite rarely holds true. As the saying goes,
culture eats strategy for breakfast
. Like operations, change itself is hard.
Measurement Is Crucial
Finally, measurement is particularly crucial in the overall business context of, for example, breaking down silos and incident resolution. In each of these environments, you establish the reality of what’s happening by means of objective measurement, verify that you’re changing the situation as you expect, and create an objective foundation for conversations that different functions agree upon. (This applies in both business
and
other contexts, such as on-call.)
Background on SRE
Site Reliability Engineering (SRE) is a term (and associated job role) coined by Ben Treynor Sloss, a VP of engineering at Google.
7
As we can see in the previous section, DevOps is a broad set of principles about whole-lifecycle collaboration between operations and product development. SRE is a job role, a set of practices (described next) we’ve found to work, and some beliefs that animate those practices. If you think of DevOps as a philosophy and an approach to working, you can argue that SRE implements some of the philosophy that DevOps describes, and is somewhat closer to a concrete definition of a job or role than, say, “DevOps engineer.”
8
So, in a way,
class SRE implements interface DevOps
.
Unlike the DevOps movement, which originated from collaborations between leaders and practitioners at multiple companies, SRE at Google inherited much of its culture from the surrounding company before the term
SRE
became widely popularized across the industry. Given that trajectory, the discipline as a whole currently does not foreground cultural change by default quite as much as DevOps. (That doesn’t imply anything about whether cultural change is necessary to do SRE in an arbitrary organization, of course.)
SRE is defined by the following concrete principles.
Operations Is a Software Problem
The basic tenet of SRE is that doing operations well is a software problem. SRE should therefore use software engineering approaches to solve that problem. This is across a wide field of view, encompassing everything from process and business change to similarly complicated but more traditional software problems, such as rewriting a stack to eliminate single points of failure in business logic.
Manage by Service Level Objectives (SLOs)
SRE does not attempt to give everything 100% availability. As discussed in our first book,
Site Reliability Engineering
, this is the wrong target for a number of reasons. Instead, the product team and the SRE team select an appropriate availability target for the service and its user base, and the service is managed to that SLO.
9
Deciding on such a target requires strong collaboration from the business. SLOs have cultural implications as well: as collaborative decisions among stakeholders, SLO violations bring teams back to the drawing board, blamelessly.
Work to Minimize Toil
For SRE, any manual, structurally mandated operational task is abhorrent. (That doesn’t mean we don’t
have
any such operations: we have plenty of them. We just don’t like them.) We believe that if a machine
can
perform a desired operation, then a machine often
should
.
This is a distinction (and a value)
not often seen in other organizations, where toil
is
the job, and that’s what you’re paying a person to do. For SRE in the Google context, toil is
not
the job—it can’t be. Any time spent on operational tasks means time not spent on project work—and project work is how we make our services more reliable and scalable.
Performing operational tasks does, however, by “the wisdom of production,” provide vital input into decisions. This work keeps us grounded by providing real-time feedback from a given system. Sources of toil need to be identifiable so you can minimize or eliminate them. However, if you find yourself in a position of operational underload, you may need to push new features and changes more often so that engineers remain familiar with the workings of the service you support.
The Wisdom of Production
A note on “the wisdom of production”: by this phrase, we mean the wisdom you get from something running in production—the messy details of how it
actually
behaves, and how software should
actually
be designed, rather than a whiteboarded view of a service isolated from the facts on the ground. All of the pages you get, the tickets the team gets, and so on, are a direct connection with reality that should inform better system design and behavior.
Automate This Year’s Job Away
The real work in this area is determining what to automate, under what conditions, and how to automate it.
SRE as practiced in Google has a hard limit of how much time a team member can spend on toil, as opposed to engineering that produces lasting value: 50%. Many people think of this limit as a
cap
. In fact, it’s much more useful to think of it as a
guarantee
—an explicit statement, and enabling mechanism, for taking an engineering-based approach to problems rather than just toiling at them over and over.
There is an unintuitive and interesting interaction between this benchmark and how it plays out when we think about automation and toil. Over time, an SRE team winds up automating all that it can for a service, leaving behind things that can’t be automated (
the Murphy-Beyer effect
). Other things being equal, this comes to dominate what an SRE team does unless other actions are taken. In the Google environment, you tend to either add more services, up to some limit that still supports 50% engineering time, or you are so successful at your automation that you can go and do something else completely different instead.
Move Fast by Reducing the Cost of Failure
One of the main benefits of SRE engagement is not necessarily increased reliability, although obviously that does happen; it is actually improved product development output. Why? Well, a reduced mean time to repair (MTTR) for common faults results in increased product developer velocity, as engineers don’t have to waste time and focus cleaning up after these issues. This follows from the well-known fact that the later in the product lifecycle a problem is discovered,
the more expensive it is to fix
. SREs are specifically charged with improving undesirably late problem discovery, yielding benefits for the company as a whole.
Share Ownership with Developers
Rigid boundaries between “application development” and “production” (sometimes called programmers and operators) are counterproductive. This is especially true if the segregation of responsibilities and classification of ops as a cost center leads to power imbalances or discrepancies in esteem or pay.
SREs tend to be inclined to focus on production problems rather than business logic problems, but as their approach brings software engineering tools to bear on the problem, they share skill sets with product development teams. In general, an SRE has particular expertise around the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of the service(s) they are looking after. Those specific (and usually well-defined) competencies are the bread-and-butter of what SRE does for a product and for the associated product development team.
10
Ideally, both product development and SRE teams should have a holistic view of the stack—the frontend, backend, libraries, storage, kernels, and physical machine—and no team should jealously own single components. It turns out that you can get a lot more done if you “blur the lines”
11
and have SREs instrument JavaScript, or product developers qualify kernels: knowledge of how to make changes and the authority to do so are much more widespread, and incentives to jealously guard any particular function are removed.
In
Site Reliability Engineering
, we did not make it sufficiently clear that product development teams in Google own their service by default. SRE is neither available nor warranted for the bulk of services, although SRE principles still inform how services are managed throughout Google.
12
The ownership model when an SRE team works with a product development team is ultimately a shared model as well.
Use the Same Tooling, Regardless of Function or Job Title
Tooling is an incredibly important determinant of behavior, and it would be naive to assume that the efficacy of SRE in the Google context has nothing to do with the widely accessible
unified codebase
, the wide array of software and systems tooling, the
highly optimized and proprietary
production stack, and so on. Yet we share this absolute assumption with DevOps: teams minding a service
13
should use the same tools, regardless of their role in the organization. There is no good way to manage a service that has one tool for the SREs and another for the product developers, behaving differently (and potentially catastrophically so) in different situations. The more divergence you have, the less your company benefits from each effort to improve each individual tool.
Compare and Contrast
Looking at the preceding principles, we immediately see quite a lot of commonality in the points outlined:
DevOps and SRE are both contingent on an acceptance that change is necessary in order to improve. Without that, there’s not much room for maneuvering.
14
Collaboration is front and center for DevOps work. An effective shared ownership model and partner team relationships are necessary for SRE to function. Like DevOps, SRE also has strong values shared across the organization, which can make climbing out of team-based silos slightly easier.
Change management is best pursued as small, continual actions, the majority of which are ideally both automatically tested and applied. The critical interaction between change and reliability makes this especially important for SRE.
The right tooling is critically important, and tooling to a certain extent determines the scope of your acts. Yet we must not focus too hard on whether something is achieved using some specific set of tools; at the end of the day, API orientation for system management is a more important philosophy that will outlast any particular implementation of it.
Measurement is absolutely key to how both DevOps and SRE work. For SRE, SLOs are dominant in determining the actions taken to improve the service. Of course, you can’t have SLOs without measurement (as well as cross-team debate—ideally among product, infrastructure/SRE, and the business). For DevOps, the act of measurement is often used to understand what the outputs of a process are, what the duration of feedback loops is, and so on. Both DevOps and SRE are data-oriented things, whether they are professions or philosophies.
The brute reality of managing production services means that bad things happen occasionally, and you have to talk about why. SRE and DevOps both practice
blameless postmortems
in order to offset unhelpful, adrenaline-laden reactions.
Ultimately, implementing DevOps
or
SRE is a holistic act; both hope to make the whole of the team (or unit, or organization) better, as a function of working together in a highly specific way. For both DevOps and SRE, better velocity should be the outcome.
15
As you can see, there are many areas of commonality between DevOps and SRE.
Yet there are significant differences as well. DevOps is in some sense a wider philosophy and culture. Because it effects wider change than does SRE, DevOps is more context-sensitive. DevOps is relatively silent on how to run operations at a detailed level. For example, it is not prescriptive around the precise management of services. It chooses instead to concentrate on breaking down barriers in the wider organization. This has much value.
SRE, on the other hand, has relatively narrowly defined responsibilities and its remit is generally service-oriented (and end-user-oriented) rather than whole-business-oriented. As a result, it brings an opinionated intellectual framework (including concepts like
error budgets
) to the problem of how to run systems effectively. Although SRE is, as a profession, highly aware of incentives and their effects, it in turn is relatively silent on topics like siloization and information barriers. It would support CI and CD not necessarily because of the business case, but because of the improved operational practices involved. Or, to put it another way, SRE
believes in the same things as DevOps but for slightly different reasons
.
Organizational Context and Fostering Successful Adoption
DevOps and SRE have a very large conceptual overlap in how they operate. As you might expect, they also have a similar set of conditions that have to be true within the organization in order for them to a) be implementable in the first place, and b) obtain the maximum benefit from that implementation. As
Tolstoy almost but never quite said
, effective operations approaches are all alike, whereas broken approaches are all broken in their own way. Incentives can in part explain why that is.
If an organization’s culture values the benefits of a DevOps approach and is willing to bear those costs—typically expressed as difficulties in hiring, the energy required to maintain fluidity in teams and responsibilities, and increased financial resources dedicated to compensating a skill set that is necessarily more rare—then that organization must also make sure the
incentives
are correct in order to achieve the full benefit of this approach.
Specifically, the following should hold true in the context of both DevOps and SRE.
Narrow, Rigid Incentives Narrow Your Success
Many companies accidentally define formal incentives that undermine collective performance. To avoid this mistake, don’t structure incentives to be narrowly tied to launch-related or reliability-related outcomes. As
any economist
can tell you, if there
is
a numeric measure, people will find a way to game it to bad effect, sometimes even in a completely well-intentioned way.
16
Instead, you should allow your people the freedom to find the right tradeoffs. As discussed earlier, DevOps or SRE can act as an accelerant for your product team in general, allowing the rest of the software org to ship features to customers in a continuous and reliable fashion. Such a dynamic also fixes one persistent problem with the traditional and divergent systems/software group approach: the lack of a feedback loop between design and production. A system with early SRE engagement (ideally, at design time) typically works better in production after deployment, regardless of who is responsible for managing the service. (Nothing slows down feature development like losing user data.)
It’s Better to Fix It Yourself; Don’t Blame Someone Else
Furthermore, avoid any incentives to pass off the blame for production incidents or system failures onto other groups. In many ways, the dynamics of passing off blame is the core problem with the traditional model for engineering operations, as separating operations and software teams allows separate incentives to emerge. Instead, consider adopting the following practices to combat blame passing at an organizational level:
Don’t just allow, but actively
encourage
, engineers to change code and configuration when required for the product. Also allow these teams the authority to be radical within the limits of their mission, thereby eliminating incentives to proceed more slowly.
Support blameless postmortems.
17
Doing so eliminates incentives to downplay or cover up a problem. This step is crucial in fully understanding the product and actually optimizing its performance and functionality, and relies on the wisdom of production mentioned previously.
Allow support to move away from products that are irredeemably operationally difficult. The threat of support withdrawal motivates product development to fix issues both in the run-up to support and once the product is itself supported, saving everyone time. What it means to be “irredeemably operationally difficult” may differ depending on your context—the dynamic here should be one of mutually understood responsibilities. Pushback to other orgs might be a softer, “We think there are higher-value uses of the time of people with this skill set,” or framed within the limit of, “These people will quit if they’re tasked with too much operational work and aren’t given the opportunity to use their engineering skill set.” At Google, the practice of outright withdrawing support from such products has become institutional.
Consider Reliability Work as a Specialized Role
At Google, SRE and product development are separate organizations. Each group has its own focus, priorities, and management, and does not have to do the bidding of the other. However, the product development teams effectively fund the
growth of SRE with new hires
when a product is successful. In this way, product development has a stake in the success of SRE teams, just as SREs have a stake in the success of the product development teams. SRE is also fortunate to receive high-level support from management, which ensures that engineering teams’ objections to supporting services “the SRE way” are generally short-lived. You don’t need to have an org chart to do things differently, though—you just need a different community of practice to emerge.
Regardless of whether you fork your organizational chart or use more informal mechanisms, it’s important to recognize that specialization creates challenges. Practitioners of DevOps and SRE benefit from having a community of peers for support and career development, and job ladders that reward them
18
for the unique skills and perspectives they bring to the table.
It’s important to note that the organizational structure employed by Google, as well as some of the aforementioned incentives, is
somewhat
reliant on a sizeable organization. For example, if your 20-person startup has only one (comparatively small) product, there’s not much sense in allowing withdrawal of operational support. It’s still possible to take a DevOps-style approach,
19
but the ability to improve an operationally poor product is undermined if literally all you can do is help it grow. Usually, though, people have more choice than they imagine about how to fulfill those growth needs versus the rate at which technical debt accumulates.
20
When
Can Substitute for
Whether
However, when your organization or product grows beyond a certain size, you can exercise more latitude in what products to support, or how to
prioritize
that support. If it’s clear that support for system X is going to happen much sooner than support for system Y, the implicit conditionality can play much the same role as the choice to
not
support services in the SRE world.
At Google, SRE’s strong partnership with product development has proven to be critically important: if such a relationship exists at your organization, then the decision to withdraw (or supply) support can be based on objective data about comparative operational characteristics, thereby avoiding otherwise nonproductive conversations.
A productive relationship between SRE and product development also helps in avoiding the organizational anti-pattern in which a product development team has to ship a product or feature before it’s quite ready. Instead, SRE can work with a development team to improve the product before the burden of maintenance shifts away from the people with the most expertise to fix it.
Strive for Parity of Esteem: Career and Financial
Finally, make sure that the career incentives to do the right thing are in place: we want our DevOps/SRE organization to be held in the same esteem as their product development counterparts. Therefore, members of each team should be rated by roughly the same methods and have the same financial incentives.
Conclusion
In many ways, DevOps and SRE sit, in both practice and philosophy, very close to each other in the overall landscape of IT operations.
Both DevOps and SRE require discussion, management support, and buy-in from the people actually doing the work to make serious progress. Implementing either of them is a journey and not a quick fix: the practice of rename-and-shame
21
is a hollow one, unlikely to yield benefit. Given that it is a more opinionated implementation of how to perform operations, SRE has more concrete suggestions on how to change your work practices earlier on in that journey, albeit requiring specific adaptation. DevOps, having a wider focus, is somewhat more difficult to reason about and translate into concrete steps, but precisely because of that wider focus, is likely to meet with weaker initial resistance.
But practitioners of each use many of the same tools, the same approaches to change management, and the same data-based decision-making mindset. At the end of the day, we all face the same persistent problem: production, and making it better—no matter what we’re called.
For those interested in further reading, the following suggestions should help you develop a wider understanding of the cultural, business, and technical underpinnings of the operations revolution taking place right now:
Site Reliability Engineering
Effective DevOps
The Phoenix Project
The Practice of Cloud System Administration: DevOps and SRE Practices for Web Services, Volume 2
Accelerate: The Science of Lean Software and DevOps
1
Note that as this discussion appears in a book about SRE, some of this discussion is specific to software service operations, as opposed to IT operations.
2
Mary Poppendieck has an excellent article on this called “
The Cost Center Trap
.” Another way in which this approach fails is when a very large and improbable disaster completely wipes out the cost savings you made by moving to a low-grade operations model (c.f. the
British Airways outage in May 2017
).
3
Of course, there are a number of other potential reactions. For example, ITIL® is another approach to IT management that advocates for better standardization.
4
Note also that because this is a complicated world, there are also
positive effects
to
partitioning
, silos, and the like, but the downsides seem to be particularly pernicious in the domain of operations.
5
See
https://en.wikipedia.org/wiki/Normal_Accidents
.
6
Higher-risk changes, or those unvalidatable by automatic means, should obviously still be vetted by humans, if not enacted by them.
7
The history of SRE at Google is that it sprang from a precursor team, which was more operationally focused, and Ben provided the impetus for treating the problem from an engineering standpoint.
8
This is a misnomer in a large number of ways, perhaps the most fundamental being that you can’t just hire some people, call them “DevOps engineers,” and expect benefits immediately. You have to buy into the whole philosophy of changing how you work in order to benefit. As
Andrew Clay Shafer says
, “People sell DevOps, but you can’t buy it.” And, as Seth Vargo points out in
“The 10 Myths of DevOps”
, you can’t “hire a DevOp to fix your organization.”
9
A service level objective is a target for performance of a particular metric (e.g., available 99.9% of the time).
10
Of course, not every team does everything, but those are the most common headings under which SRE works.
11
Perform a layering violation, if you think of this as layered stacks.
12
In fact, there’s a Production Readiness Review for onboarding
anything
; SRE won’t just onboard services from a standing start.
13
A service is loosely defined as software running to perform some business need, generally with availability constraints.
14
Within Google, that question is largely settled, and services change state, configuration, ownership, direction, and so on, all the time. To a certain extent, SRE at Google is the beneficiary of the “change is necessary” argument having been fought and won a number of times in the past. But not completely
evenly distributed
, as William Gibson might say.
15
See relevant research at
https://devops-research.com/research.html
.
16
See
https://en.wikipedia.org/wiki/Goodhart%27s_law
and
https://skybrary.aero/bookshelf/books/2336.pdf
.
17
See, for example,
https://codeascraft.com/2012/05/22/blameless-postmortems/
.
18
In orgs that have well-developed cultures of either. Early-stage companies likely do not have established ways to reward these job roles.
19
Indeed, arguably, that’s your
only
choice unless you outsource operations.
20
For a discussion of how to apply SRE principles in different contexts, see
SRE Team Lifecycles
.
21
In other words, simply retitling a group DevOps or SRE with no other change in their organizational positioning, resulting in inevitable shaming of the team when promised improvement is not forthcoming.
