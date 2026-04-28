---
title: "Writing commit messages"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/commit-messages/"
fetched_at: 2026-04-28T07:01:34.444940+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Writing commit messages

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/commit-messages/

Writing commit messages
[Simon Tatham, 2024-05-19]
Introduction
This is my personal guide to writing good commit messages, in
      Git or other version control systems.
Why write yet another of these guides?
Of course, there are lots of guides to commit messages already.
      Why am I bothering to write
another
one?
Mostly because, when I’ve looked at other guides, they don’t
      seem to be focusing on the most important things. The one that
      first started me making notes towards this article consisted of
      a 7-point list of guidelines,
most
of which were tiny
      details of the initial ‘subject line’ part of the commit – what
      tense to use, whether to end it with a full stop, capitalisation
      – and the final rule just said ‘Use the body to explain what and
      why vs. how’.
To my way of thinking, that’s focusing on the trivial and
      neglecting the important. Yes, it’s
nice
to have a
      consistent grammatical style in your subject lines – but it’s
      not
vital
. Not the same way that ‘include all the
      important facts and reasoning’ is vital.
A commit-message guide ought to focus on
information
,
      not typography. What do you put in, and what do you leave out?
      The rule that said ‘explain why and what’ should have
      been
most of the list
, not a throwaway point at the
      end.
So that’s what
this
guide will mostly talk about. I
      can’t
quite
ignore typography completely – one or two
      details of layout are necessary for Git tooling to work sensibly
      – but I’ll keep that to a bare minimum.
What’s your authority to pontificate on this
      subject?
I put a lot of effort into writing my commit messages, and I
      think I write pretty good ones. Other people have commented
      positively on them too.
I won’t try to claim to be the world’s best commit message
      writer, but I think it’s fair to consider myself in at least the
      top 5%. Certainly I’ve seen plenty of commit messages that would
      have benefited from doing more of the things I’m going to
      mention here.
What information should I include?
If we want to consider which information should go in commit
      messages, we have to start by asking what they’re
for
in the first place.
Who will read my commit message, and why?
When you’re writing any piece of text, you should
      consider:
who do I expect to read this, and what will they
      be looking for when they do?
For a commit message, there are lots of answers to that: many
      people might read them, for lots of different reasons. Here’s a
      list of cases I’ve thought of, which probably still isn’t
      complete.
Users of your project
, if its source
        control is public, and if they’re at least slightly
        development-savvy.
“I want to know if this change does something I want / need.
        Should I update to this version?”
People investigating or reporting bugs
.
“I’m investigating a behaviour change, and I’ve found out
        – maybe via ‘
git bisect
’ – that this commit made it
        happen. Now I want to know whether that change was the point of
        your work, or an unwanted side effect.”
Code reviewers
.
“I’m deciding whether to accept your patch, reject it
        outright, or ask for changes. I need to understand what it’s
        doing and why.”
Other developers of the same project
.
“I’m another person who works on this code, and I want to
        know how it’s just changed, to keep my own understanding up to
        date.”
“I’m preparing a release branch, and I want to know if this
        commit is the kind of thing I should cherry-pick to the
        release.”
“I have a downstream fork of your repository, and I need to
        know how to restructure my own changes to match what you’ve
        done.”
“I’m doing code archaeology in general, and want to
        understand changes made in the past, to get an idea of why
        things are how they are now.”
Anyone browsing the source control history
.
“Is this the commit I’m looking for in the first place?”
And last, but absolutely not
        least:
yourself
, when you come back to the
        code later!
“… what
was
I thinking, again?”
What will someone get out of reading the commit
      message?
Another angle to look at the question from is: why am I
      bothering to write a commit message in the first place, when the
      actual
patch
is contained in the same commit? What
      value is the message adding, over the code change itself? What
      advantage will a reader obtain from reading this message?
Again, there’s a long list of possible answers.
It saves them having to read the patch at all
.
Some people reading your commit message won’t be
        programmers, and won’t understand code. So they can’t get much
        information from reading the actual patch. Instead, they’ll be
        hoping to get the information they need out of the commit
        message.
Other readers
can
understand code, but are in a
        great hurry and have a lot of it to get through. Those people
        will also appreciate it if the commit message gives them
        enough information all by itself.
It saves them having to read
most
of the
          patch
.
If the patch is large and the reader is in a hurry, they’ll
        want to quickly find their way to the
relevant
part of
        the patch, or the most interesting part, if that can possibly be
        done without them having to read it all.
It helps them to understand the patch
.
If the patch is difficult to understand, or just difficult
        to
read
, the reader might like some help. If it isn’t
        obvious how the patch relates to the problem it’s solving, the
        reader might like some help solving that puzzle too.
(For this point, and the previous one, it helps to re-read
        the patch
yourself
, just before you write the commit
        message, and try to imagine how you’d react to it if you
        didn’t already know what it did.)
It tells them what you’ve done to the code, and why
          that was good
.
This is the most obvious use of a commit message. I feel silly
        writing it on this list as if you didn’t know it already! But I
        can’t leave it out.
It tells them what
you think
you’ve done to
          the code, and why
you thought
that was
          good
.
The flip side of the previous case. Programs have bugs, and
        patches have bugs. Your description in the commit message might
        turn out later to be
untrue
– your patch might not have
        had the effect you thought it would have, or you might have been
        wrong that that effect would be a good thing. So it’s useful for
        someone to be able to understand what effect you
did
think it would have. That will make it easier for someone to
        decide on the right fix later.
It tells them where to look for related
          information
.
Patches are often part of a larger programme of work, or
        relate to a specific piece of context stored somewhere else,
        like a bug tracker. Some readers will be looking for that
        context. Perhaps they went looking for your commit via
        ‘
git blame
’ or ‘
git bisect
’, and hoped
        that when they found it it would link to some information
        elsewhere which is what they
really
wanted.
OK, so what information should I include?
I’ve spent two subsections on talking about who the readers are
      and what they want, but I haven’t yet got round to answering the
      main question. Given all of this, what
should
you put
      in the commit message?
Here’s a list of things that you could usefully put in.
Describe the intended change to the user-visible
        behaviour
.
What does the program do differently, from
        a user’s point of view, after this change is made?
This is exactly what some readers will want to know. So if
          you say it in the commit message, you can save them having
          to read the patch at all.
Even for a reader who
is
going to read the patch,
          it might still be important. Some code changes aren’t at all
          obviously connected to the problem they solve (say, if
          they’re in a support library called from lots of places, and
          only one of those places triggers the bug), or are extremely
          complicated compared to the effect they have.
Perhaps the most extreme example of this is when you’re
          making a pure-refactoring commit that has
no
effect
          on the program’s behaviour, only on its internal
          organisation. If the commit message
says
that,
          you’ve saved someone having to read a hugely complicated
          patch at all! In some communities the acronym ‘NFC’, for ‘No
          Functional Change’, is used as a short way to indicate
          this.
Another reason it’s important to describe what you think the
          patch does: you might be
wrong
. If your patch
          doesn’t actually do what you meant it to, it will make the
          problem easier to fix later if you describe what
          you
did
mean it to do
. Sometimes it’s hard to figure out
          from just the patch, if the author was confused enough!
Mention side effects, if you know about
      them
.
Not every effect of a patch is part of its
purpose
.
        Some are side effects: additional changes to the behaviour,
        which you didn’t particularly intend, but can’t easily prevent
        (maybe the side effect can’t be separated from the important
        change), or you don’t want to (maybe the side effect is mildly
        beneficial in its own right).
It’s worth mentioning any side effects you know about, and
          perhaps also why you think they’re OK. Then, if your patch
          comes under suspicion later, a reader can tell the
          difference between ‘author didn’t consider this side
          effect’, ‘considered it but wrongly decided it was OK’, and
          ‘
rightly
decided it was OK, and after reading their
          explanation, now I agree with them!’
Explain
why
you wanted to make this
          change
.
Sometimes, even knowing the intended effect of the commit,
        it isn’t even obvious
why
that effect seemed
        desirable in the first place! Either because no reason was
        obvious at all, or because
more
than one reason might
        have been the answer. (If the patch changes the colour of
        something, was that just because you thought it looked nice,
        or because it works better in dark mode, or to help
        colour-blind users?)
If there’s some aspect of futureproofing in the change – the
        point is to make something easy to update for some kind of
        anticipated future need – then that’s particularly worth
        calling out, because it might well not be obvious from either
        the code change or from any observable aspect of
        the
current
behaviour. Even the tests you added (you
        did, right?) might not be able to make that clear.
A special case of this: if you have
immediate
intentions to follow up this patch with other related work,
        then it can be useful to mention what you intend to do next
        that uses the change you’ve just made. This is a bad way to
        make sure it actually gets done (nobody is reading commit
        messages and using them as to-do lists!), but it can make it
        easier to understand the reason for making a change.
        (Especially refactoring.)
Call out the interesting part of the
      patch
.
Sometimes, a patch has to make a lot of changes to work at
        all, but only one of the changes is the interesting or
        important one – so use the commit message to say where that
        is.
For example, suppose you’ve added an extra parameter to a
          function definition, and in 99 calls to the function you set
          the extra parameter to whatever value makes the function
          behave the same as before. But in just one place, you set it
          to a value that
isn’t
the default. More people will
          care about
that
call site than the 99 boring ones,
          because it’s the one that actually makes the
          code
behave
differently. But it’s a lot of work to
          go through all 100 call sites looking for it. So if you draw
          attention to it in the commit message, you make it easy to
          find the important part of the patch.
On the other hand, when a patch has this kind of ‘mostly
          boring’ structure, another possibility is to split it into
          two patches. I discuss this more in
a
          later section
.
Describe the structure of the patch
.
Usually, when a version control system displays a patch, it
        will be in some arbitrary order that doesn’t really relate to
        the semantics, like alphabetical order of the filenames
        touched by the change. So you’ll often see a fiddly detail at
        the top of the patch, which doesn’t make sense until you’ve
        found the explanatory comment or context further
        down
. One of the
        useful things a commit message can do is to describe the
        overall structure of the patch, to help readers find their way
        to the top-level framework first, and
then
read the
        details once they’ve absorbed that.
Patches can be confusing to read in other ways. If you spot
        any of those in advance, you can give the reader a hand. For
        example, if you’ve reindented a lot of code, or moved things
        from one place to another, then diff viewers will often not
        point out the
similarities
, so you could mention them
        yourself.
Describe what
isn’t
in the patch
, if
        they do have to read it in full.
Another thing to mention might be why the
        patch
doesn’t
do something the reader might expect.
If you’ve updated every instance of a thing
except for
        one
, was it just because you forgot that one, or because
        you had a good reason why it should be treated differently? If
        you had a reason, mention it. Otherwise, another developer
        might assume it was a mistake, and ‘fix’ it.
If it will look to a reader as if you’ve only done half of a
        larger job, why is that? Are you planning to do the other half
        in the next commit? Or in the next release, because the other
        instances of the same fix aren’t as urgent? Or not do the rest
        of the work at all, for some good reason?
Another case of this: is there another way to solve the
        problem that
looks
easier, so that a reader is likely
        to wonder why you didn’t do it that way? If you have a good
        reason why you didn’t do the obvious or easy thing – maybe it
        doesn’t work in some obscure corner case, for example, or it
        conflicts with a future plan – then mention
        it
. Otherwise the reader might assume
        you just didn’t think of it, and made life complicated for no
        reason.
Finally, it’s sometimes worth describing what aspects of the
        program’s behaviour your patch
hasn’t
changed. For
        example, a class of side effect that you’ve thought about
        carefully and convinced yourself
can’t
happen. That
        way, if it turns out in the future that you were wrong, people
        will be able to see immediately that the change wasn’t
        intentional.
Provide links to external context.
If your commit relates to a bug tracker entry, include the
        entry’s id, or maybe even a full URL if you think it’s worth
        it, so the reader can find the entry in question.
This can be useful even if it’s not
your
bug
        tracker. For example, some of my own free software projects
        are packaged in Debian, and sometimes Debian finds out about
        bugs before I do. When I fix a bug that’s tracked in the
        Debian bug tracker, I include the Debian bug number in my
        commit message, if I know it. Another example: in a security
        project, if you fix a security issue for which a CVE number is
        already allocated, it’s useful to mention that in the commit
        message.
If your commit fixes a bug introduced by a previous commit,
        or is a cherry-pick of a commit from another branch, or is
        strongly related in any other way to another commit in the
        repository, then mention the ids of all related commits.
Another useful class of link you can put in commit messages
        is a citation of your sources. If there’s a standards document
        that justifies your change, or a release note announcing a
        change elsewhere that you have to keep up to date with, or an
        article explaining the technique you’re using, include it!
Not all of these things are necessary
every time
. For
      example, if the patch isn’t large, there’s no need to call
      attention to the interesting part of it, or describe its overall
      structure. If it’s totally obvious why the effect is desirable
      (‘Stop it crashing’), then there’s no need to spend words on
      explaining that. If there is no related external context, then
      you don’t need to link to it. And so on.
But all of these things are worth
considering
, even if
      you decide a particular commit message doesn’t need all of them.
In the commit message, or somewhere else?
The previous section was mostly about thinking of lots of
      things a reader of your patch will want to know. Now I
      discuss
where
to put them. Is it really a good idea to
      put all of this in the
commit message
? Or is some of it
      better put elsewhere?
Use commit messages in preference to cover letters
If you’re submitting a patch to somebody else’s project where
      you’re not already a developer, you probably want to explain to
      the developers why you think they should accept your patch: what
      bug it fixes, what feature it adds, why either one is something
      they should care about, and maybe also why you think the patch
      is
safe
(i.e. doesn’t break anything else as a side
      effect, or introduce bugs, or prevent other future work).
If you’re sending the patch by email, rather than a formal pull
      request on a Gitlab / Github style forge site, then often people
      send the patch with a sort of ‘covering letter’ email, and put
      the patch itself in an attachment, perhaps in ordinary
      ‘
git diff
’ style without an embedded commit message
      at all. And in the body of the email, they try to persuade the
      developer to take the patch:
Dear Developer,
The attached patch changes your software so that it [does a
        cool thing].
I’d really like this applied, if it’s not too much trouble,
        because it’s very inconvenient for me not to have this
        feature, [details of what a pain it is]. I don’t expect it to
        be too much trouble to maintain, because [some reason why it’s
        easy].
I’ve done my best to keep everything working the same as
        before in existing cases, and the only change is if you use
        [the new configuration option added by this patch].
Kind regards,
Patch Author.
[attachment:
my-cool-change.patch
]
Instead of doing that,
put the same explanation in the
      commit message!
Whatever argument you’re planning to use to
      persuade the developer to take your patch, it’s
      probably
also
useful to a code archaeologist trying to
      figure out later why your change was made.
Putting the same information in the cover letter is
less
      good
, and also more work for the developer. If a developer
      receives this kind of ‘
git diff
’ patch and decides
      to accept it, they’re going to have to
write
a commit
      message. What will they put in it? Quite likely they’ll paste
      your own explanation from the cover letter. You can save them
      the trouble by putting it in the commit message in the first
      place!
If the patch you attached
does
have a commit message
      embedded (probably because you generated it via ‘
git
      format-patch
’ instead of plain ‘
git diff
’),
      then it’s still better to put as much explanation as possible in
      the commit message rather than the cover letter. The only thing
      the cover letter needs to do is to make the developer interested
      enough to read the commit message at all. The commit message can
      do the rest, and then the information is automatically saved in
      the code history.
There’s one exception to this: if you’re sending a series
      of
multiple
patches, then maybe the cover letter can
      usefully give a bit of overview of what problem the series as a
      whole solves, before diving into the details of the individual
      patches.
Commit message describes changes; code
      comment describes how things are
If you’re changing a part of the code that other developers
      will have to interoperate with, such as an internal API or a
      data format, then of course you need to write
      down
somewhere
how the new version works.
It’s useful to say something about that in the commit message –
      but not everything.
The commit message shouldn’t be the documentation that people
      will actually read to find out how to work with the new API.
      That belongs in the source tree, either in code comments or
      separate documentation files, however your project likes to do
      it. Nobody is going to want to go back through the history of
      lots of separate changes to put together a picture of how to use
      the current API.
But the commit message is a good place to summarise
      what’s
changed
in the API: how the new API differs from
      the old. Someone updating their code for your change will need
      to know:
what in my code do I need to change to match
      yours?
So if you’ve removed
this
function and
      added
that
one, or if you’ve introduced a new
      constraint in the order of function calls, or anything like
      that, describe the
change
in the commit message.
But also keep the in-code documentation up to date with the
      current state of the world.
Consider adjusting the patch to make the
      commit message simpler
Sometimes you can reduce the amount of explaining in the commit
      message, by writing your patch to avoid needing that
      explanation. Usually this means breaking it up into a series of
      smaller patches.
For example, sometimes you have to make a large, intrusive but
      boring change in conjunction with a tiny one that actually does
      something interesting. If you can’t avoid doing all of this in
      the same patch, then it’s worth using the commit message to draw
      attention to the interesting part. But if you
can
break
      the patch up into smaller ones, consider doing that instead. One
      patch does
only
the boring part, and its commit message
      explains that it’s totally boring and has no functional change;
      then, the next patch is much smaller, does just the interesting
      part, and the commit message can focus on explaining that.
For example, suppose you’re adding a new parameter to an
      existing function, which requires modifying all its call sites,
      so that in just one place you can set the new parameter to
      something that isn’t the default. You could explain that in the
      commit message, and draw the reader’s attention to the one
      interesting location. Or you could break up the patch into one
      that
just
adds the default value of the new parameter
      to every call site, and a second one that introduces its single
      non-trivial use.
I’ve occasionally even done this for pure indentation purposes.
      One time, I wrapped a large subsection of a C++ function in a
      pair of extra braces, so that it indented one level to the
      right, and in the
next
commit, I made the braces into a
      while loop and added some break statements in the middle of the
      loop, so that it was easy for a reader to separate the bulk
      reindentation from the actual changes. Another time, I changed
      the control flow of a function first, leaving it mis-indented,
      and then added a followup commit that re-ran the code formatter,
      because the combined patch from doing both at once would have
      been much less legible.
5
Writing style
This guide is mostly focused on
what
you should say in
      commit messages. As I said in the introduction, I’m not mostly
      here to nitpick grammar and punctuation. I want to talk about
      communicating the important information.
Mostly, a commit message is a piece of technical writing, so if
      you want to write one clearly, there are lots of existing guides
      to clear technical writing, and I won’t repeat their advice
      here.
Even so, there are a few aspects of style that are specific to
      commit messages.
Make it clear what’s before and what’s after
In a commit message, you’re describing a
change
between two states of the code. So you might need to talk about
      what the code did before the change, and also what the code does
      after the change. It’s surprisingly easy to accidentally make it
      unclear which one you’re talking about!
One common style of explanation goes along the lines of:
The code has [some property]. This is bad because [reason].
      To fix it, I’m [changing it to be different].
That kind of outline looks perfectly sensible. But another
      equally sensible style of explanation might go:
The code has [some property]. Previously, it [was different
        in some way], which was bad because [reason].
In these two styles, the first sentence looks exactly the same,
      and is in the same tense. But in one, the first sentence
      describes the state of the code
before
the change, and
      in the other, it describes the state
after
the change.
      You have to read the rest of the message to decide which one is
      meant.
Sometimes even
after
you read the rest of the message
      it’s not clear which state of the code the author was
      describing! Perhaps the rest of the explanation is too technical
      for some readers of the message. Or perhaps the commit message
      author left out the rest of the explanation, thinking it would
      be obvious.
So, make sure you clearly mark descriptions of the code to
      indicate
whether they apply to the old code or the new
      code
.
How
to mark them? I’d recommend not using grammatical
      tense (or rather, not
only
that), because it runs into
      the ambiguity above. If one person writes “The code
did
this, and now it
does
that instead”, and another person
      writes “The code
does
this, and now it
will do
that instead”, then looking at the two messages together, it’s
      still true that the present tense doesn’t reliably describe one
      state or the other.
So I’d advise keeping it simpler: add extra
      words
to indicate the context of the
      statement you’re making. “
Before this change
, the code
      did this.” “This patch
updates the code so that
it does
      that.” Or just “Previously, …” and “Now, …”.
Pyramid writing: put the most important stuff at
      the top
When I first started using version control systems that made it
      easy to write long commit messages
, I’d
      often write long rambling essays that started off with general
      background information, and gradually worked their way towards
      the point. Something like this (details completely made up):
When the user [does some general kind of thing], the program
        must [do some computation]. This is done by [an internal
        module], whose general design principle is [described here].
        That seemed like a good idea [
n
years ago] because
        [reasons], but since then it’s turned out to be
        inadequate.
So far we’ve been able to work around all the problems by
        [nasty bodge], but now a bigger problem has come to light:
        [description of internal state of the code that causes a
        problem]. It’s not feasible to fix that with [the same bodge
        again], because [some reason why it’s exceptionally
        difficult].
In this commit I rewrite [module] to be based on the new
        principle of [something more sensible]. The external API is
        mostly the same, except for [thing], so I’ve had to change the
        call sites [here] and [there].
In future, this should also allow [the existing nasty bodges]
        to be removed one by one. But I haven’t done all of that work
        in this commit. I’ve just fixed the most important bug, which
        is that now when the user [does a specific case of the thing],
        you don’t see [buggy behaviour] any more.
Imagine reading this commit message when you were just trying
      to find out what change had been made. The first two paragraphs
      are completely irrelevant! If you’re a developer of the
      software, you quite likely know them already, and can skip
      immediately to the third paragraph describing the change inside
      the code. If you’re a user wanting to know what the user-visible
      behaviour change is, all of the first
three
paragraphs
      might very well be meaningless to you, and the only part you
      care about is the last line.
So you want to skip straight to the important part. But you
      can’t do that easily, because there’s no signpost pointing to
      it. You have to read every paragraph far enough to figure out
      that it’s not interesting, before you
can
skip over it
      to the next part.
Not only that, but the most important point – describing the
      user-visible bug fix – appears
half way through
the
      last paragraph, not at the start. So a skim-reader’s eye isn’t
      drawn to it. You really do have to read every word of the stuff
      you
don’t
care about, in order to find the one part you
      do.
This even annoys
me
, when I re-read
my own
commit messages from long ago. So I’ve recanted: I think this
      style is bad, and I try not to use it any more.
A better way to write commit messages is to use the principle
      of
pyramid writing
, similar to newspaper
      articles. The information at the top is the part that you
      expect
most
readers will want to know. After that, you
      put information of interest to fewer readers, and then fewer
      still. The idea is that each reader starts from the top,
      continues reading until they find something they don’t care
      about, and then stops, because they can safely assume that
      everything further down is even
more
boring.
If I were writing the above message today, instead of in 2002,
      I’d be more likely to order it the other way up:
When the user [did this very specific thing], the program
        would previously [exhibit buggy behaviour]. Now it [does
        something more sensible].
To implement this, I’ve rewritten [module] to be based on the
        new principle of [something sensible]. The external API is
        mostly the same as before, except for [thing], so I’ve had to
        change the call sites [here] and [there].
Background: [module] is generally responsible for [some
        computation] related to [user doing more general instances of
        the same thing]. Previously it was based on [the old design
        principle]. That seemed like a good idea [
n
years ago]
        because [reasons], but since then it’s turned out to be
        inadequate. We’ve worked around problems by [nasty bodge], but
        [the case described above] isn’t fixable by those means,
        because it causes [particular internal state of the code],
        which [is incompatible with the bodge].
In future, this should also allow [the existing bodges] to be
        removed one by one. But that’s a lot more work, so I’ve left
        it for future commits.
Now the user who only wants to know what bug is fixed can stop
      reading after the first paragraph. The developer who already
      understands the previous state of the code, and just needs to
      know how it’s changed, can stop after the
      second
. A less
      experienced developer, who needs the background information,
      will want to read as far as the third paragraph. And the only
      reader who needs to read all the way to the end is one who’s
      trying to understand
why
this change is the way it is,
      perhaps because the change turned out to have some other bad
      side effect – and with any luck, those are the least common
      readers.
Commit messages aren’t jokes. Don’t make the reader
        wait until the end for the punchline!
Git subject lines: make every commit look
      unique
Most of this article applies to commit messages
in
      general
, no matter what version control system they’re in.
      But if you’re using Git in particular (and, writing this in
      2024, that’s extremely likely), there’s one extra local
      convention: the
subject line
.
A lot of git-based tooling expects that a commit will start
      with a single short line on its own, giving a
very
      brief
summary of the change. Then a blank line.
      And
then
you can write long paragraphs containing all
      the rest of the information.
Why does Git in particular want this? Because lots of
      Git-specific tools expect it, and will work better if you do
      it
. Many git commands
      will display the subject line of each commit as they process it
      (like
git rebase
); abbreviated log commands
      like
git log --oneline
will display just the
      subjects; graphical browsing tools like
gitk
,
      web-based repository viewers like
gitweb
, and
      ‘forge’ websites like Gitlab and Github, will all show the
      summary line by itself, at least to start with.
So, what should go in the subject line in particular?
I think there’s one really important thing, and a few other
      things that individual projects might decide they like:
Enough information to tell which commit this is
.
I think this is the single most important thing. Subject
        lines should be good enough to
tell commits apart from each
          other
.
In systems that show just the subject line of each commit, you
        can typically click on one, or enter the hash into another git
        command, to see the rest of the details of the commit. So the
        main purpose of the subject line is to let the user find
        out
which
commit they want to click on at all.
        Everything else can wait until they’ve clicked through for the
        rest of the information.
Therefore, when you’re writing the subject line, the question
        you should ask yourself is:
is any other commit likely
          to have used the same description?
In other words, don’t make the subject line
        too
generic
. If you just say “Bug fix”, or even “Bug
        fix in [module]”, then you have to assume there will be other
        commits with the same subject line, and a reader will have to
        click on each one in turn to see if it’s the commit they’re
        looking for. Instead, try to say
something
, no matter
        how terse and abbreviated, that is specific to
this
bug
        fix, distinguishing it from others.
It’s also tempting to put the
most important
information in the subject line, on the same ‘pyramid writing’
        principle I discussed in the
previous
          section
. That’s good if you can do it. But if it comes down
        to a choice, it’s better to make the subject line
unique
than to make it say the single most important
        thing. Speaking for myself, I’d prefer to see less important
        details like function names in the subject lines, if that makes
        it easier to tell the commits apart than the description of the
        bugs actually being fixed. Then I can recognise the commit when
        I see it again, even if it makes no sense to me the first
        time.
A ticket ID
, if your local convention says so.
If you have a ticketing system or a bug tracker, it’s almost
        always a good idea to put the relevant ticket
        ID
somewhere
in the commit message. In many
        organisations the convention is to put it in the subject line.
If you do that, then that helps to make subject lines more
        unique. You might have had 10 commits all saying ‘fix bug’, and
        now they say ‘fix #44142’, ‘fix #50514’, ‘fix #64145’, and so
        on. But that’s still not
very
helpful, because a reader
        has to go and look up each of those ticket numbers in the
        tracking system to find out what they mean. So it’s still better
        to have some informative text
as well
as the ticket
        number:
e5fa44f2b31c
Ticket #12313: update to 2023 colour scheme
7448d8798a43
Ticket #11224: fix crash when selecting two widgets at once
9c6b057a2b9d
Ticket #42423: split
frob_thingy()
into two functions
5d9474c0309b
Ticket #41352: make a new class to handle aardvarks
ccf271b78308
Ticket #35223: refactoring to prepare for 64-bit nose length
Often, your ticket tracking system will have a subject or title
        field in the ticket itself. It’s tempting to save yourself some
        effort, and reuse the
ticket’s
title as
        the
commit’s
subject line. I think this is a bad plan,
        for two reasons:
Ticket titles are often written by bug reporters, who don’t
              yet know the real cause of the problem, and will use generic
              descriptions like ‘Bug’ or ‘Wrong output’. So the ticket
              titles might be too generic, and hard to tell apart from each
              other. By the time you’re committing a fix, you know
              more, and can write something more unique.
If you use
more than one
commit to solve the
              problem described in a ticket – which is very sensible – then
              you don’t want all those commits to have exactly the same
              subject line as each other, or people won’t know which one to
              click on! So give each commit a subject line that says
              something about what
that commit
is contributing to
              the overall fix.
Module names or functionality keywords
,
        if your local convention says so.
Some projects have a lot of separate library modules or
        tools, or do a lot of separate tasks. When you’re looking for
        a commit you’re interested in, you often already know which
        module or task it concerns. So the local convention might
        suggest that authors put keywords in the commit subject line
        indicating those things. That way, someone reading a list of
        subject lines can immediately see that a
        commit
doesn’t
affect the thing they’re interested
        in, and move on to the next, without having to click through
        for the rest of the message.
It’s up to particular projects to decide whether they need
        this. If they do, it might be for more than one reason. Maybe
        completely separate teams of developers work on the different
        modules, and each team is mostly interested in commits
        affecting its own area. Maybe different kinds of
user
will have needs that involve only some of the modules (say,
        because the project is a set of libraries or a set of
        not-very-related command-line tools). Or both.
A good example of this is the LLVM compiler project, which
        includes a lot of separate command-line tools doing different
        jobs, and a lot of separate libraries that other software
        might want to use, and generates code for a lot of different
        CPU architectures. Commit subject lines in LLVM often include
        both a keyword describing an area of the code,
and
a
        keyword describing the affected architecture. Then, if I know
        I’m looking for a commit that affects (for
        example)
llvm-objdump
on Arm, I can skip over any
        commit that mentions a different tool or library,
or
any commit that mentions a different architecture!
Other things you can say very briefly using an
          acronym
, if you can think of any.
Writing subject lines is an exercise in data compression. If
      there’s anything you can say
extremely briefly
that
      might save someone the effort of clicking through to the rest of
      the message, it might be worth it!
I only have one example of this: in communities that use the
      acronym ‘NFC’ in commit messages to mean ‘No Functional Change’
      (that is, the change is purely refactoring), it might well be
      worth putting that acronym in the subject line. That way, a
      reader scanning the subject lines looking for the cause of a
      behaviour change will know they don’t need to click through to
      the full description of any commit marked NFC.
(… At least, until they’ve ruled out a
deliberate
behaviour change, and are going back through the commits looking
      for an
accidental
one. Then they might need to pay more
      attention to
everything!
)
Line wrapping and markup: keep limitations of
      standard tooling in mind
Commit messages are generally written in plain text, not in any
      form of richer markup.
Some systems for viewing a commit message will interpret the
      text as Markdown. Forge websites often do this, in particular:
      if you view a specific commit on a Gitlab instance or on Github,
      it will rewrap your paragraphs, and honour markup idioms like
      using
`backticks`
to indicate literal code.
But not
all
tools displaying a commit message will do
      this. Most of the
standard
tools which come with the
      version control system itself will display the message as plain
      text, without even re-wrapping the lines.
Therefore,
write your message so that it’s still
        readable in that form
.
Most importantly,
wrap paragraphs to a reasonable width
        using physical newlines
. The standard tools, like
        ‘
git log
’, do not wrap lines at all when
        displaying a commit message. So if you write a paragraph as a
        single 500-character physical line, some readers will have to
        scroll their window left and right to read it. Or maybe it
        will be ‘wrapped’ to the terminal width in a way that doesn’t
        account for word breaks, so that individual words will be
        split across lines. Both of these make it painful to read.
It’s tempting to think that it’s
better
to write each
      paragraph as a single incredibly long physical line, so that
      each display tool can rewrap it to the appropriate screen width.
      But this is wishful thinking. It would probably be nice if all
      display tools
did
do that, but just because it would be
      nice, that doesn’t mean it’s true!
Secondly, if you use Markdown markup idioms, use them
      sparingly, and
make sure the text is still readable
without
having run a Markdown renderer over it
.
A lot of Markdown idioms are designed to look acceptable in
      plain text as well.
`Backticks`
for literal code,
      or
_underscores_
for emphasis, for example. These
      are fine. Readers of plain text are accustomed to those already,
      and find them normal.
But here’s an example that’s not fine: using Markdown table
      syntax and expecting the renderer to make everything line up.
| Bad | Table |
| --- | --- |
| 1 | Lots of important text |
| Something other than 1 | Whatevs |
If you want to write a Markdown table in your commit message at
      all, do it so that the columns line up for a plain-text reader
      as well:
| Good                   | Table                  |
| ---------------------- | ---------------------- |
| 1                      | Lots of important text |
| Something other than 1 | Whatevs                |
If you ignore these recommendations, and format commit messages
      so they can
only
be read usefully by a
      Markdown-rendering system or at least by something that wraps
      the lines, then you’re excluding some users from working with
      your code base efficiently, and forcing others to do things a
      long way round. Just because
you
always browse commits
      in the Gitlab web interface, that doesn’t mean
everyone
does. The next person working with your code might be a heavy
      user of
gitk
, or be working mostly over SSH using
      plain
git log
, or working
offline
so that
      the forge website and its Markdown renderer aren’t available. If
      you force that person to keep opening a web browser to make
      sense of your messages, you’ll make them more and more annoyed
      with you, and they won’t want to do you any favours the next
      time you need one.
Also, most version control systems these days – certainly
      including Git – are distributed. If your repository isn’t
      completely private, people can take a complete copy of it
      easily, and use it for a completely different purpose from
      yours. Maybe
those
people won’t be hosting it on the
      same Git forge site you use. Keep your messages usable by even
      the users you
don’t
know about yet – not just your
      current colleagues!
It’s OK, you don’t have to do
all
of
      this every time
If you’ve read all the way down to here, you might be feeling
      overwhelmed. It probably sounds as if I’m demanding an absurdly
      large amount of effort! I’ve listed so many things to include,
      so many readers to think about, and so many properties to make
      sure of, that it would take ten times as much effort to write
      your commit message as the patch itself.
Especially
if
      your main skill is programming, rather than writing text. Or if
      you’re not fluent in the language you’re writing commit messages
      in.
So let me reassure you: the kind of thing I’m describing here
      is (in my opinion) a
really, really good
commit
      message. But it’s not the minimum standard for writing one at
      all.
Most real-world commit messages wouldn’t get a perfect score if
      you assessed them against the principles in this article.
      Even
my own
commit messages don’t reliably come up to
      this standard – and I’m the one who bothered to write down all
      of these guidelines!
What I’m really trying to answer in this article is:
what
      makes one commit message better than another?
It’s OK for a
      commit message not to be the best one in the world, but I still
      think it’s good to
know
that it’s not perfect, and why
      not, and what could be better about it, if you had more time, or
      effort, or knowledge, or skill, or somebody to help you improve
      it.
If someone reads this article and their commit messages
      become
just a bit
better than they were before, then
      that’s already a good effect, and I’ll be happy.
For example, you might pick out just one thing in this article
      that you hadn’t thought of before and aren’t already doing, and
      try to start doing that thing in future. That would be great!
      Perhaps in a year’s time, once that improvement has become
      natural to you and you don’t have to think about it any more,
      you might try to make another small improvement.
Or you might set yourself a time box: after you write a commit
      message, make sure you spend a full ten minutes staring at it
      and trying to think of ways to improve it – but then, at the end
      of 10 minutes, call it done. Perhaps the more you practice, the
      more improvements you’ll be able to make in those 10 minutes,
      and the better your messages will get without wasting too much
      time!
Or perhaps, if you’re a code reviewer, you might start looking
      harder at the commit messages in the patches you review, and
      suggesting ways to make
those
better, as well as ways
      to make the patch itself better.
But I’m not trying to demand that your commit messages
      immediately start scoring 100% on my scale. And nobody else
      should demand that of you either!
Especially not in temporary
      note-to-self commit messages
One exception to this
entire article
is temporary
      commit messages you write during initial development.
One of the best things about Git is ‘
git rebase
        -i
’, which lets you take a chain of commits and restructure
      them: rearrange them, glue some of them together into bigger
      commits, and most importantly,
rewrite all the commit
        messages
.
This enables a style of coding in which you start by treating
      your Git history as a sort of ‘undo chain’, similar to the one
      in your editor – just record various states the code has passed
      through while you were trying to get it to work, in case you
      need to go back to an earlier one. Or you might think of it as
      like saving in a videogame: you save before attempting something
      tricky so you can go back and try it again, and you save after
      you’ve done it so you don’t have to do it again. (Refactoring
      code is like a boss fight.)
For these purposes, you probably want to focus on getting the
      code to work. As long as you still think you might have to go
      back and do it all again differently, it’s potentially a huge
      waste of time to write up really nice commit messages – if the
      code needs rewriting, then so will the message, so you’ve
      doubled your effort!
So it often saves you time overall to write much more terse
      commit messages as you develop, in a ‘note to self’ style in
      which the only intended reader of the message is yourself, and
      you only write down the things you think
you
might need
      to remember. Then, once you’ve got the whole thing working, do
      a
rebase -i
to rearrange it into a patch series for
      other people to read, and
then
write the proper commit
      messages, now that you’re sure of what they describe.
If you’re anything like me, this section has probably already
      reminded you of
XKCD #1296 “Git
      Commit”
.
Personally, my own note-to-self messages are a little more
      organised than
      that
. I still
      try to make each message different from the previous one: if
      they
all
just said ‘more code’, then how would I find
      the one I was looking for? If I make a temporary change that I
      need to remember to remove later, I’ll put it in its own commit,
      with a special title that’s easy to recognise. And when I’m
      trying to get code to work in the first place, my temporary
      commit messages will often announce how close it is to working:
      ‘Now compiles’, or ‘Now passes its tests’, or ‘Runs on a simple
      input file’. That’s useful because if it later
stops
doing any of those things, I can easily find the last version
      that says it still worked!
But it’s entirely up to you. As long as the message is only for
      your own use, what you think it’s worth writing down in it is
      between you and your future self. If you keep coming back to
      half-finished projects and finding you can’t remember something
      about what you were in the middle of, then perhaps consider
      writing down a few more reminders to yourself – but if you’re
      doing fine already, there’s no need to change.
It’s only once you send the commits to
somebody else
,
      or commit them into the
permanent
history, that it
      becomes important to write them up properly.
With any luck, you should be able to read the footnotes of this
      article in place, by clicking on the superscript footnote number
      or the corresponding numbered tab on the right side of the page.
But just in case the CSS didn’t do the right thing, here’s the
      text of all the footnotes again:
1.
In
          communities where the ‘NFC’ acronym is used, some people
          like to use a variant form ‘NFCI’, for ‘No Functional
          Change
Intended
’, acknowledging the possibility of
          an
accidental
functional change. Sometimes they use
          the two acronyms to indicate how confident they are that
          they got it right: ‘NFC’ if they’re sure, ‘NFCI’ if they’re
          a bit worried about it. But people have arguments about
          whether this is a good thing. It’s up to your local
          convention.
2.
In C and C++ in particular, I often
        think it’s a shame that the extension
.h
for
        header files sorts after the extensions
.c
or
.cpp
for source files. If they were the other
        way round, then someone reading a patch in the natural order
        would normally see the changes to function prototypes and
        comments in
module.h
first
, and by the
        time they read the implementation in
module.c
alongside it, they’d have a better understanding of what the
        code change was doing. Instead they see the fiddly code change
        first, and the explanation second.
3.
Another good effect of writing
        down an explanation of why you didn’t do it the easier way:
        sometimes, half way through writing the explanation, you
        realise that it’s wrong, and you
should
have done it
        the easier way!
4.
It would be nice to keep the
      overview text in the permanent history as well, but
      unfortunately, there isn’t really a particularly good place to
      put it. Some people like to use a gratuitous merge commit
      containing the overview text, but it’s not the most usual
      style.
5.
This
      trick wouldn’t have worked in an environment where CI enforces that
every
commit should be invariant under your automated
      formatter: the intermediate state of the code would have been
      rejected by CI, even though in my view it makes the overall
      change easier to read and reason about. For this reason I’m not
      really a fan of automatic formatting enforcement at all – and if
      you do do it, I think it’s better to enforce it after an entire
      patch
series
instead of every individual
      commit.
6.
I once read a commit message
      formatted as a bullet list, but the bullet points weren’t all
      the same: some were − signs, and some were + signs. The − bullet
      points described the old state of the code, and the + points
      described the new state. So the commit message was written in
      the same style as a diff! I’m not sure whether to
      actually
recommend
that style, but I certainly found it
      clear when I read it.
7.
My first
      version control system was RCS, which asked you for the commit
      message using a prompt directly printed in the terminal.
      You
could
write messages more than one line long, but
      it was very inconvenient, because after entering each line,
      you’d press Return, and then you’d be committed to that text,
      because the UI wouldn’t give you any sensible way to go back and
      edit lines before the current one. (And even editing
      the
current
line was hard, because the prompt used raw
      terminal input, and not any editing library like Readline.) So
      my RCS commit messages were mostly one-liners. Everything since
      then has invoked a more sensible text editor!
8.
Which is more important, out of
      the change to user-visible behaviour and the change to code
      structure? In a global sense, the UVB is important to more
      people. But perhaps the code structure change is more important
      to most of the people
who read the commit message
. I
      don’t want to state a general rule about which of those things
      deserves to be described first. I can’t always make up my mind
      about it myself, and it might well depend on the project, or
      even on the particular commit. But definitely both of these
      parts should come before the more general background
      information, or reasons for the change.
9.
Personally I think it’s even worth
      using Git-style subject lines if you’re
not
using Git,
      because Git can also be used as a client for accessing other
      version control systems. For example, in many
      ways,
git-svn
is a better client for working with a
      Subversion repository than SVN itself is! Not only that, but
      repositories in other formats are often migrated into Git later.
      So I’d recommend using Git-style subject-lines no matter what
      you’re using, so that people translating the repository into Git
      – temporarily or permanently – will get all the same benefits.
      But you may reasonably disagree.
10.
Mostly.
