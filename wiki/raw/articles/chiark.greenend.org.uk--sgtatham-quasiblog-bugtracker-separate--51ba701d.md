---
title: "Separation of concerns in a bug tracker"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/bugtracker-separate/"
fetched_at: 2026-04-27T07:00:52.383186+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Separation of concerns in a bug tracker

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/bugtracker-separate/

Separation of concerns in a bug tracker
[Simon Tatham, 2024-11-01]
Introduction
I write software, both professionally and on a ‘serious’ basis
      in my free time. So I interact with bug trackers. That means I
      form opinions about them.
Over the last few years I’ve had some recurring reasons to
      complain about various bug trackers, and gradually come to the
      conclusion that what I’m really annoyed by is a fundamental
      wrongness in the
data representation
, more than the
      user interfaces. (Of course the user interfaces can be quite
      annoying too, but that doesn’t distinguish bug trackers from any
      other kind of software!)
In this article I’ll present some of my complaints, and then
      describe a ‘separation of concerns’ principle I’d
like
to see in a bug tracker, which I think would make me less
      annoyed, if it were done well.
Disclaimer
: this collection of rants is all
      based on my own experience – the bug trackers I happen to have
      used in the past. There may well be other widely used bug
      trackers with different properties; I didn’t do an exhaustive
      review of the most popular trackers I
haven’t
used.
(Indeed, perhaps there’s a bug tracker that already has the
      property I’m going to talk about! I’d be interested to hear
      about it if so, especially if it’s free software.)
Some rants
I’m going to list three separate annoyances here, and in the
      next section I’ll argue how they’re all related.
One general emphasis you might notice here is that when I use a
      bug tracker, I’m often concerned with the ease of
      running
automated queries
against its data. This seems
      to be a thing I find myself wanting to do more often than most
      people.
(Perhaps because I cling to an old-fashioned view that the
      purpose of computers is reliably automating stuff – not running
      heavyweight Javascript UIs that can only be used interactively.
      And the less said about
unreliable
automation systems
      currently in the news, the better.)
Unified ‘Fix Version’ field
In Jira – or at least in Jira schemas I’ve used – bugs have a
      ‘Fix Version’ field, which I dislike, because it’s a combination
      of definite reality and fond hopes. Depending on other data, it
      might indicate three different kinds of information:
A
known fact about the past
. If the bug
          is marked as fixed, and Fix Version says 1.2.3, and that is
          the number of a release that’s already gone out of the door,
          then this is a fact: the bug
really was
fixed in
          already-released version 1.2.3.
A
fact about the present
, indicating
          a
likelihood about the future
. If the bug
          is marked as fixed, with Fix Version 1.2.4, and that
          version
hasn’t
been released yet, then it means the
          bug has been fixed on the branch that we plan to make 1.2.4
          from. So it
will
be fixed in the actual 1.2.4
          release …
… probably. Unless something a bit unexpected happens.
            Maybe it will manage to regress without being caught by
            the tests. Or maybe the fix will have to be reverted
            because it caused a bigger problem. Or we change our mind
            about which branch 1.2.4 comes from. Or other even less
            likely things.
An
intention for the future
: if the bug
          isn’t fixed at all, then setting Fix Version = 2.0.0 says
          that project management
wants
to get this fixed for
          the major 2.0.0 release next year.
Sometimes those management intentions are very firm.
            Sometimes they’re aspirational: “we’d
like
to fix
            it for 2.0.0, but we recognise that there might not turn
            out to be time”. And sometimes they
seem
like
            firm intentions, until a fortnight before the deadline …
            and suddenly there’s one of those “Rapid Descoping
            Phases”, in which a lot of bugs get their Fix Version
            bulk-updated to something further in the future, and
            everyone quietly pretends that that was the intention all
            along and that nobody was caught by
            surprise.
That
difference of meaning is typically
            not recorded at all by the bug tracker,
even
taking account of all the other fields of the ticket!
These different meanings of ‘Fix Version’ go with other
      differences. They’re subject to change with very different
      probabilities, for very different reasons, and often even by
      different people. A project manager updates the fix-version for
      an unfixed bug whenever they change their mind about future
      plans, which happens often. A developer might update it for a
fixed
bug if they’ve just belatedly found out it wasn’t
      fixed after all, or perhaps that it
was
fixed as a side
      effect of other work without noticing. This happens much more
      rarely.
Lumping them all into the same field makes it awkward to query
      for a specific property. If you’re looking specifically for
      facts, you can’t just ask for ‘bugs with Fix Version <
      1.3.0’. Especially not since release numbers often aren’t
      ordered with the released versions sorting before the unreleased
      ones: even after 1.3.0 is released, quite possibly patch release
      1.2.1 against the earlier 1.2.0 release is still in the future,
      so you might still catch a mix of facts and intentions with that
      simple query even though it
looks
as if it’s restricted
      entirely to stuff in the past.
Instead, you have to write a much more complicated query that
      takes several other fields of the record into account, to
      exclude the hopes and dreams occupying the same table column as
      the hard facts you’re after. (And surely
vice versa
too:
      if the intentions and plans are what you’re searching for,
      surely the facts get in your way in a corresponding fashion.)
Not every bug tracker makes this mistake. I’ve seen at least
      one that has separate fields for ‘Target Version’ and ‘Fixed In
      Version’: respectively, when do we
want
to fix it, and
      when
have
we fixed it? I think that’s heading in the
      right direction, but (as I’ll discuss later) not going
      far
enough
.
Two-tier Status and Resolution fields
I’ve seen more than one bug tracker that separates the state of
      a ticket into two fields. The top-level field, called something
      like ‘State’ or ‘Status’, is as simple as possible – perhaps
      even as simple as having two states ‘Open’ and ‘Closed’. Then,
      if the ticket is closed, a secondary field called something like
      ‘Resolution’ indicates
in what way
it’s closed, with
      values such as ‘Fixed’, ‘Cannot Reproduce’, ‘Not A Bug’ (perhaps
      it was user misunderstanding), or the dreaded ‘Won’t Fix’ (it is
      a bug, we totally admit it, but we’re not going to do anything
      about it).
You can see the logic behind the separation, from one point of
      view. I want to find something to work on. Where do I look? At
      the tickets whose Status is ‘Open’. All of the ‘Closed’ states
      have in common that you don’t intend to do any work on them.
But, again, this combination of states is an awkward conflation
      of facts about the code with intentions about the future, and
      it’s hard to pick out just one of them. If I want to find
      out
what bugs exist in the code
, I have to do a search
      that picks out tickets with state ‘Open’, and
also
tickets with state ‘Closed’ and resolution ‘Won’t Fix’. Those
      ones are still bugs, even if we’re not going to fix them!
I’m not saying that ‘Won’t Fix’ is an abomination
in
      itself
. Developers have limited effort, and software always
      has more bugs than you’d like. Any realistic team must
      acknowledge that they’ll never have time to fix
all
the
      bugs; if you’re trying to plan your work, that probably means
      deciding that a
specific
bug is one of the ones you
      don’t ever expect to get round to. So you do need
some
way of marking a bug as being in that state. But it’s awkward,
      and I think leads people to overestimate the actual quality of
      their software, to make that state a sub-case of ‘closed’
      instead of a sub-case of ‘still a bug’.
Fake bugs for other kinds of to-do item
Usually, when there’s a bug, we plan to fix it. (Not counting
      the ‘Won’t Fix’ state I just mentioned.) So your bug list
      naturally forms part of your to-do list.
A common choice, and again quite natural from some points of
      view, is to decide that it simplifies things if your bug list
      is, by definition,
all
of your to-do list. Half the
      stuff you planned to do is on there already, after all. Now all
      you have to do is create ‘bug’ records describing any other work
      you want to do, and then you can look in just one place for
      everything.
This is also helpful for tracking progress. Keep a count of the
      currently open tickets – or maybe weight each one by some
      estimate of its size – and you get a low-cost way to give some
      kind of a number for how far through a large batch of work we
      are.
Seems nice in principle. But in my view it falls down when you
      look at many of the details.
For a start, I think this is the concept that drives the
      two-tier system I mentioned in the previous section, with the
      particularly awkward classification of ‘Won’t Fix’ as a special
      case of ‘done’. That data organisation is privileging the ‘to-do
      list’ aspect of a bug tracker
over
the ‘actually
      tracking bugs’ aspect: it’s easy to query whether something is
      currently a to-do item, and less easy to query whether it’s a
      bug. I do actually want to track bugs, and if my bug tracker
      makes that difficult, it’s been hijacked by someone with a
      different agenda!
What about feature work?
Usually
the lack of a feature
      isn’t itself considered a bug (although sometimes it can
      happen). But you certainly do often
plan
to implement a
      feature. So you have to make a bug record, or a
      bug-
like
record, to represent your plan to implement
      that feature – in effect, representing the feature as a sort of
      ‘anti-bug’. This often fits awkwardly: fields like ‘Severity’ or
      ‘In what version did the bug appear?’ don’t really make sense
      when the ‘bug’ is the lack of a feature. Some systems (like
      Jira) let you have a different type of record for feature work,
      with different fields, but that comes with its own problems –
      writing reliable automated queries is
even more
complicated when not everything has the same fields.
Even more confusing for progress-tracking purposes is work that
      leads to the
creation
of bug tickets: investigative
      work, such as new kinds of testing. Imagine that you’ve decided
      one of your developers is going to try to use your software to
      do a large task of some kind that nobody’s tried before and that
      you don’t expect will quite work yet, and when they find out
      what parts of it don’t work, they’ll raise bug tickets for the
      problems. Now your plan of tracking progress by watching the bug
      count reduce is completely confused, because if this project
      is
successful
, the bug count goes
up!
Then there’s work where the measure of success
      is
independent
of what it does to the bug list. For
      example: “we have
n
months available in this release
      cycle to spend on trying to improve performance.”
      This
might
involve fixing some already-known bugs of
      the form ‘some specific thing is slow’, if those known bugs turn
      out to be easy and/or make a significant difference. Or it might
      involve
finding
previously unrecorded specific
      performance problems, and fixing them – perhaps creating tickets
      for the ones you found and fixed, to record that they existed in
      the past, and perhaps also creating still-open tickets for the
      ones you found but didn’t have time to fix this time round. But
      the measure of success of a plan like this is not anything to do
      with the bug list: regardless of whether the number of bug
      records, or the number of
fixed
bug records, increased
      or decreased, the work was a success if
performance got
      better
.
Finally, there’s work that happens outside the system of
      branches and releases of your main project. ‘What release will
      this be fixed in?’ doesn’t make sense for completely internal
      work like ‘unbreak the CI system’, if that system is serving all
      the release and development branches of your product equally.
      The true answer will be something like ‘all of them, but not
      until next week’!
Separation of concerns
I think all three of these rants arise from the same root
      cause. A record in a typical bug tracker does double duty: it
      records factual information about a bug that exists, and it also
      records plans and intentions. Sometimes these go naturally
      together, but not always – and when they don’t, all of the
      problems above arise.
So my key proposal is: a bug tracker ought to clearly
      separate
facts
from
plans
.
I don’t quite mean putting them in totally different
      applications. Certainly they’ll need to refer to each other;
      you’d need to do atomic transactions in the tracker that cover
      both at once; and in some cases you’d want to
enforce
that both things are updated at once (because the data would be
      left in an inconsistent and nonsensical state otherwise). So
      probably they’d want to be separate tables in the same database,
      or some analogue of that concept if the bug tracker is built on
      something other than a literal database.
The facts ‘table’ would record things like:
What bugs exist in this code?
Which versions of the code does a bug exist in?
How serious is each bug, in
objective
terms, in the
      sense that they’re based on facts and are unlikely to keep
      changing for a particular bug? Such as:
Is it a security vulnerability?
Is it a safety hazard?
Does it have an easy workaround?
If not, does it at least have a really difficult
            and awkward workaround?
You’d update the facts table when new facts of this kind are
      discovered (like finding a new bug), or created (like making a
      new commit that fixes the bug), or when facts you thought you
      knew are found to be inaccurate (oops, turns out we
      misunderstood last year, and fixed the wrong bug).
Meanwhile, the plans table would record things like:
What things do we
intend
to spend time working on?
In what time frame?
How serious is each piece of work, in
subjective
terms that
      can easily change as priorities and users fluctuate? Such as:
Do we care about it enough to postpone this other work?
Are any users clamouring for it right now? (And are any
            of them paying well?)
Does it feed in to whatever larger goal is our current
            highest priority in the longer term?
In the prototypical case, you’d create a pair of parallel
      records in both tables. Someone reports a bug, so you have to
      make a facts record saying that the bug exists; you intend to
      fix it, so you make a plans record describing that intention.
      The system would certainly need to make it easy to do this
      double operation.
But the value of the separation is that it gives more
      flexibility for that not to be the
only
way to work: in
      reality, facts and plans don’t always match up, and this
      structure can represent that directly, instead of trying to
      contort reality to fit the wrong model.
Facts link to source control; plans link to
      time periods
I think
neither
side of this division wants to be
      thinking about ‘releases’ as the primary idea of when/where
      something is fixed or implemented.
The facts side of the bug tracker is for answering questions
      like:
does this bug exist in a particular state of the
      source?
And there’s no reason why that should be restricted
      to talking about the granularity of
releases
. You might
      very well want to record which commit introduced a bug, and
      which commit(s) fixed it.
Once you have that information, it ought to be possible to
      autogenerate the information about which
numbered
      releases
do and don’t have the bug (and also which planned
      future releases are expected to have it fixed), which would save
      a lot of manual faff updating fix-version fields when release
      plans change.
Meanwhile, the plans side is mostly about
time
      periods
. Not all work we do in this release cycle will
      actually go into the release itself (such as my earlier example
      of having to unbreak the CI, which is a purely internal
      secondary code base, not released at all). But all of it has to
      be done by the deadline. So plan records
also
don’t
      focus primarily on releases: they focus on
      release
cycles
, or any other time period or deadline of
      interest.
This deals with that awkwardness about having to pretend that
      work on cross-branch internal systems is destined for a certain
      release, with the nonsensical implication that it’s going to go
      on to the source-control branch for that release. In this model,
      neither side of the divide has to tell a lie. Fact records can
      choose which source control repositories they refer to: facts
      about bugs in the product link to the product repo, but this
      fact about a bug in the CI system links to the CI repo instead.
      Meanwhile, the plans record says with perfect truth that the aim
      is to get the CI bug fixed within the current release cycle, and
      doesn’t have to do it by abusing fields like ‘what releases does
      this bug exist in?’.
Feature requests are only plans, until they’re
      implemented
Earlier I mentioned the common practice of modelling a feature
      as an anti-bug, so that the record really describes the state
      of
not
having the feature: the ‘present in $version?’
      state really means that the feature
wasn’t
present in
      that version, and closing the ticket means the feature
      has
appeared
rather than (as with a bug) that it’s
      gone. But I think that’s awkward, and a bit
      counterintuitive.
As I said earlier, one reason it’s a bad fit is that real bugs
      can usefully have a bunch of data fields that don’t really apply
      to the lack of a feature, like “when was the problem
      introduced?”.
But a more important way that ‘a bug’ and ‘the lack of a
      feature’ aren’t the same is: bugs are
      usually
discovered
. Some user reports the bug, and it
      comes as a surprise to the developers, who hadn’t previously
      known that particular thing didn’t work. But usually, when
      software doesn’t have a certain feature, the developers knew it
      all along: you’re not
surprised
by suddenly discovering
      you don’t have support for
XYZ
.
The thing that causes someone to open a ‘bug’ record for a
      feature request is not that you’ve just discovered you
don’t
      have
that feature: it’s that you’ve just discovered
      somebody
wants
it. You open the ticket because a user –
      or lots of users, or a manager, or at any rate
someone
– has asked you for the feature, or offered to pay for the
      feature, or somehow made an incentive to add the feature. But
      nothing has changed about
your knowledge of what the
      software is like
at that instant. In other words, a feature
      request is entirely a
plan
, not a fact.
So when a feature is requested, you don’t make a fact record
      for it
at all
. Requests or requirements for new
      features live entirely on the ‘plans’ side of the divide –
      reflecting the truth that, for the moment, they are vapourware.
      You’d only create a fact record for the feature once it’s
      actually implemented in at least one version. That is, once
      it
is
a fact.
In which case, I think it makes more sense to have the fact
      record for a newly added feature have
positive
sense,
      describing the presence of the feature and not its absence: the
      ‘present in’ field (or whatever it’s called) indicates that the
      feature
does
exist in a certain version.
Facts about the source code aren’t all
bad
facts. Some
      of them are good things!
Each to their own: planners update
      plans, developers update facts
If your organisation has clearly separated roles of
      project-manager types who plan the project, and developers who
      actually fix the bugs, then
mostly
the planners will
      work in the plans table, constantly updating their ideas of what
      things are expected to be fixed when, as information comes in
      about how fast work is progressing and what new requirements
      have appeared from outside the team.
Meanwhile, the developers will be updating the facts table:
      recording that bugs are fixed, adding extra information while
      investigating them, raising extra bug records as new things are
      discovered. So they mostly don’t collide with each other, like
      both trying to update the same ‘Fix Version’ field in ways that
      reflect plans and facts respectively.
Of course, sometimes the planners and the developers are the
      same people, or at least
some
people play a dual role,
      partly planning and partly doing. That’s also fine, of course –
      but even then, I think framing each operation as ‘here I’m
      updating the plans table, yesterday I updated the facts table’
      can keep it clearer which kind of work you’re doing at a given
      time.
Plans table can be weeded while the factual
      bug records stay open
If the planning people don’t want to be constantly reminded of
      48,000 bugs that have been around for decades and that nobody is
      ever realistically going to get round to fixing, then they can
      close any associated plan records, and their view of the world
      is kept nice and clean. Perhaps they might even get the numbers
      to balance, with the amount of planned work more or less
      matching the amount of time and effort available to do it.
Closing the plan record for a bug is the analogue in this
      system of closing the
whole bug
as ‘Won’t Fix’. But
      with this system, the
facts
record for the same bug is
      unchanged when you do it – reflecting the reality that a bug
      doesn’t
stop being a bug
just because you don’t have
      any plans to fix it.
So now you can measure the health of the planning (are we
      overloaded? are we going to finish on time?) and the quality of
      the code (do we in fact have a ton of bugs?) independently,
      without either answer being polluted by concerns related to the
      other.
Time is accounted to plans, not bugs
If you’re paid to work on a piece of software, your
      organisation probably wants to be sure you’re spending your time
      (i.e. their money) on the things they think are important.
      Perhaps this might involve a system of detailed time accounting,
      where you record every day what bug(s) you spent your time
      working on. Or perhaps it’s less formal than that, and project
      management just keep track of whether the list of planned work
      is reducing at the rate they expect, and only start looking into
      details if they find it’s not.
Whatever the details, this accounting can lead to awkwardness
      in edge cases, if bugs are conflated with plans. For example,
      maybe a bug that was closed as ‘Won’t Fix’ needs to be fixed
      after all, because it’s actually getting in the way of something
      that’s on the plan for this release. In a ‘one record type’ bug
      tracker, maybe you now have to reopen the bug and start
      accounting your time to it (formally or informally). And maybe
      that means having an argument with a manager about why you’ve
      taken it on yourself to overrule their decision that there were
      far more important things to do than fix that bug.
With my suggested separation, your time is accounted to
      the
plan
, not the bug. If you find you have to get some
      other bug out of your way in order to make progress towards the
      goal of the current plan, then you just keep accounting your
      time towards that plan, and when you’ve fixed the bug, you
      update the
fact
record for that bug to say so.
(Perhaps it might turn out that there
was
a plan
      record for that bug you fixed in passing: maybe it wasn’t in
      total ‘Won’t Fix’ state, but instead, was planned for next
      year’s 2.0.0 release instead of this month’s 1.2.(
n
+1).
      That’s fine too: plan and bug records should be connected enough
      that it will be flagged up to someone that that plan record now
      probably doesn’t have any work left that needs doing. Some
      project manager gets a piece of good news!)
You don’t have to have plans at all
Some types of software project don’t really
plan
at
      all, in the ‘multiple release cycles’ / ‘Gantt chart’ /
      ‘burndown chart’ / ‘we promise this will be done by March’ sort
      of style.
A pure hobby project is developed on the basis of ‘Do I feel
      like a bit of coding this weekend? I wonder what would be fun to
      do.’ A developer who takes this attitude isn’t making plans at
      all. They code when they feel like it; they release (if at all)
      when it seems like a good idea.
Even a more serious free-software project might not have much
      ability to commit to plans, if no developer is being paid to
      work full-time on the project. Unpaid volunteers are always at
      the mercy of other demands on their time. They can’t commit
      to
definitely
fixing a certain amount of stuff and
      making a release in
n
months – they might turn out not to
      have time to work on it at all.
For these types of project, the standard type of bug tracker
      with planning aspects built in becomes a
source of
      guilt
. Every time they look at it it reminds them of
      all the promises to their users (or at least expectations)
      they’ve broken. Maintaining the software turns from a labour of
      love – “I program because it’s fun for me, and it makes people’s
      lives better too, everyone’s happy!” – into a chore that at best
      reduces the level of guilt (“oh, god, I suppose I ought to at
      least get
some
of this to-do list done this weekend”).
      You might as well be doing housework.
But with a bug tracker that separates facts from plans, there’s
      a really simple way to configure a project with no ability or
      obligation to plan.
Just don’t have a plans table at
      all!
You might very well still need to record the
facts
about what your software does and doesn’t get right. (As an aid
      to your own memory, but also, it might inspire other volunteers
      to pick a thing off the list and help fix it!) But there’s no
      implication of commitment to fixing it on a particular schedule
      – and so you don’t constantly feel nagged by not having met a
      load of those commitments.
That’s why
      my
wishlist
      page for PuTTY
– the closest thing it has to a bug tracker –
      is very close to being in this form. It’s
almost
100%
      facts-oriented: the only planning-related field is a very
      coarse-grained ‘priority’, as much to guide potential
      contributors as for our own use. If it were conventional, I’d
      probably have burned out on PuTTY work a decade ago.
Well, why don’t you write this bug tracker, then?
I have a pretty low bar for starting new software projects.
      Quite often, when I think of a property that existing software
      in a niche doesn’t have, I dive straight in and start writing
      one of my own which does have that property.
So, having described this design principle for a bug tracker,
      perhaps I should get on with it and write one? (A more serious
      one than PuTTY’s static web page, that is.)
Not right now, this time.
Firstly, even the parts of this design I’ve talked about aren’t
      complete. I’ve described a central concept, but there’s a lot of
      detail around the edges that I’ve handwaved away. In particular,
      I said it should be easy to make a pair of linked records for a
      bug and a plan to fix it – but I haven’t actually said how that
      should work. I don’t have a detailed idea of what the UI should
      look like, only what criteria I’d assess a design against if I
      saw one.
(And I don’t even know for sure that there
is
a
      detailed UI design that would satisfy me. When all you have is
      vague requirements like ‘so-and-so should be easy’, there’s no
      guarantee that they’re implementable at all.)
Secondly, there are a lot of things about writing a bug tracker
      that I haven’t even described at all, and take a lot of design
      thought. Just because I have an idea about
one
thing a
      bug tracker could do better (in my own opinion), doesn’t mean I
      have any idea how to do the
rest
of those things well.
      It would be a shame to write a system that was brilliant in one
      respect and completely unusable in five others, and I think this
      is far enough outside my usual skill set that I’d be at risk of
      it.
Thirdly, if I wrote a bug tracker with ‘bug’ and ‘plan’
      records, I wouldn’t use half of it myself. My own free-software
      projects are in the ‘not much planning’ category I mentioned
      above, because I’m not paid to work on them full-time, and
      neither is anyone else. I’d be one of the people taking
      advantage of the option to
not
have a planning table –
      I’d use it in ‘bugs only’ mode, and not end up testing any of
      the interesting parts!
